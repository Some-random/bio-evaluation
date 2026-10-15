"""Prepare original VQA-RAD and author-released English SLAKE test inputs.

No inference, training, model selection or grader calls. Native questions and
original image bytes are separated from target answers and grouping metadata.
"""
import argparse
import base64
from collections import Counter
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import types
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'sources/medical_vqa'
OUTPUT = ROOT / 'data/medical_vqa'
REPORT = ROOT / 'reports/medical_vqa_preparation.json'
SL_REV = 'a9083ce6c34ac3ffb17671a605962924d8a8f9e9'
LL_REV = 'b9a98a736d2ef05bcf5ff345be6403fb3a664eaf'
VARIANT = 'NATIVE_TEST_QUESTION_IMAGE_LOCAL_ZERO_SHOT'
RAD_JSON_SHA = '948b7156059b864cf72344fb10669233526b175c243e5a046d20d4201d297a95'
SL_IMAGES_SHA = '44eb7d9214e1ac5b7946e237b669401866df9114fd9a3618c5a84fbffcded0b0'


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    return sha256(path.read_bytes())


def git_blob_sha(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\x00' + raw).hexdigest()


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()
    save_bytes(path, raw)


def save_bytes(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != raw:
            raise ValueError('Refusing to overwrite changed prepared artifact: ' + str(path))
        return
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_bytes(raw)
    tmp.replace(path)


def fetch(name, url, expected_sha=None, offline=False):
    path = SOURCE / name
    if not path.exists():
        if offline:
            raise FileNotFoundError('Required source unavailable offline: ' + name)
        SOURCE.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + '.download')
        result = subprocess.run(['curl', '-fLsS', '--retry', '2', '--max-time', '600', url, '-o', str(tmp)],
                                capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(f'Public source acquisition failed ({result.returncode}): {name}')
        if expected_sha and file_sha(tmp) != expected_sha:
            raise ValueError('Publisher SHA256 mismatch: ' + name)
        tmp.replace(path)
    if expected_sha and file_sha(path) != expected_sha:
        raise ValueError('Publisher SHA256 mismatch: ' + name)
    return path


def source_entry(path, url, **extra):
    return {'path': str(path.relative_to(ROOT)), 'url': url, 'bytes': path.stat().st_size,
            'sha256': file_sha(path), **extra}


def safe_member(name):
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or '\\' in name:
        raise ValueError('Unsafe archive member')
    return name


def image_format(raw):
    if raw.startswith(b'\xff\xd8\xff'):
        return 'image/jpeg', '.jpg'
    if raw.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'image/png', '.png'
    raise ValueError('Native image is not a supported original PNG/JPEG')


def model_case(task, row, image_bytes):
    """Only input-side fields are accessed; gold answers cannot alter prompts."""
    if task == 'V01':
        source_id = row['qid']
    elif task == 'V02':
        source_id = row['qid']
    else:
        raise ValueError('Unsupported medical VQA task')
    question = row['question']
    if not isinstance(question, str) or not question:
        raise ValueError('Missing native question')
    mime, _ = image_format(image_bytes)
    url = 'data:' + mime + ';base64,' + base64.b64encode(image_bytes).decode('ascii')
    return {'task': task, 'case_id': f'{task}:{source_id}', 'variant': VARIANT, 'split': 'test',
            'messages': [{'role': 'user', 'content': [
                {'type': 'text', 'text': question}, {'type': 'image_url', 'image_url': {'url': url}}]}]}


def select_test_rows(task, rows):
    if task == 'V01':
        return [row for row in rows if row['phrase_type'] in {'test_freeform', 'test_para'}]
    if task == 'V02':
        return [row for row in rows if row['q_lang'] == 'en']
    raise ValueError('Unsupported task')


def label_for(task, row, image_sha):
    answer_type = row['answer_type'].strip()
    if answer_type not in {'OPEN', 'CLOSED'}:
        raise ValueError('Unknown native answer type')
    answer = row['answer']
    if not isinstance(answer, (str, int, float)) or isinstance(answer, bool):
        raise ValueError('Unsupported reference answer')
    return {'task': task, 'case_id': f"{task}:{row['qid']}", 'variant': VARIANT, 'split': 'test',
            'source_qid': row['qid'], 'target_answer': str(answer), 'answer_type': answer_type,
            'image_sha256': image_sha}


def native_metrics_modules():
    """Load unchanged, pinned official scorer utilities without their CLI/deps."""
    package_name = '_bioeval_native_llava_med_v1'
    if package_name + '.evaluate_metrics' in sys.modules:
        return sys.modules[package_name + '.glossary'], sys.modules[package_name + '.evaluate_metrics']
    package = types.ModuleType(package_name)
    package.__path__ = [str(SOURCE)]
    sys.modules[package_name] = package
    for name in ['utils', 'glossary', 'evaluate_metrics']:
        path = SOURCE / ('llava_v1_' + name + '.py')
        spec = importlib.util.spec_from_file_location(package_name + '.' + name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
    return sys.modules[package_name + '.glossary'], sys.modules[package_name + '.evaluate_metrics']


def score_answer(prediction, label):
    """Native paper headline components; no LLM judge or candidate remapping."""
    if not isinstance(prediction, str):
        prediction = ''
    glossary, metrics = native_metrics_modules()
    pred = glossary.normalize_word(prediction.lower())
    gold = glossary.normalize_word(label['target_answer'].lower())
    if label['answer_type'] == 'OPEN':
        f1, precision, recall = metrics.calculate_f1score(pred, gold)
        return {'open_token_recall': recall, 'open_token_precision': precision, 'open_token_f1': f1}
    if label['answer_type'] == 'CLOSED':
        # Preserve the original run_eval.py behavior, including substring quirks.
        return {'closed_native_hit': float(('yes' in pred or 'no' in pred) and gold in pred)}
    raise ValueError('Unknown answer group')


def acquire_native_metrics(offline):
    base = f'https://raw.githubusercontent.com/microsoft/LLaVA-Med/{LL_REV}/'
    paths = {
        'llava_v1_evaluate_metrics.py': 'llava/eval/eval_metrics/evaluate_metrics.py',
        'llava_v1_glossary.py': 'llava/eval/eval_metrics/glossary.py',
        'llava_v1_utils.py': 'llava/eval/eval_metrics/utils.py',
        'llava_v1_run_eval.py': 'llava/eval/run_eval.py',
        'llava_v1_model_vqa_med.py': 'llava/eval/model_vqa_med.py',
        'llava_v1_README.md': 'README.md',
    }
    tree_path = fetch('llavamed_v1_tree.json',
                      f'https://api.github.com/repos/microsoft/LLaVA-Med/git/trees/{LL_REV}?recursive=1', offline=offline)
    tree = {item['path']: item for item in json.loads(tree_path.read_text())['tree']}
    entries = []
    for name, remote in paths.items():
        path = fetch(name, base + remote, offline=offline)
        if git_blob_sha(path.read_bytes()) != tree[remote]['sha']:
            raise ValueError('Pinned official source code blob mismatch: ' + remote)
        entries.append(source_entry(path, base + remote, publisher_git_blob_sha1=tree[remote]['sha'], publisher_digest_verified=True))
    return entries


def prepare_rows(task, rows, archive_path, member_for, publisher_images=None):
    target = OUTPUT / task
    inputs, labels, images, ledger = [], [], {}, []
    with zipfile.ZipFile(archive_path) as archive:
        for row in rows:
            member = safe_member(member_for(row))
            raw = archive.read(member)
            image_sha = sha256(raw)
            if publisher_images is not None:
                expected = publisher_images[member]['sha256']
                if expected != image_sha:
                    raise ValueError('Original image publisher SHA256 mismatch: ' + member)
            mime, suffix = image_format(raw)
            image_path = target / 'images' / (image_sha + suffix)
            save_bytes(image_path, raw)
            case = model_case(task, row, raw)
            inputs.append(case)
            labels.append(label_for(task, row, image_sha))
            image_key = str(image_path.relative_to(ROOT))
            if image_key not in images:
                from PIL import Image
                import io
                with Image.open(io.BytesIO(raw)) as image:
                    image.verify()
                with Image.open(io.BytesIO(raw)) as image:
                    width, height = image.size
                images[image_key] = {'path': image_key, 'bytes': len(raw), 'sha256': image_sha,
                                     'mime_type': mime, 'width': width, 'height': height, 'original_member': member,
                                     'publisher_image_sha256_verified': publisher_images is not None}
            ledger.append({'case_id': case['case_id'], 'source_qid': row['qid'], 'original_image_member': member,
                           'image_path': image_key, 'image_sha256': image_sha,
                           'question_utf8_sha256': sha256(row['question'].encode('utf-8'))})
    ids = [case['case_id'] for case in inputs]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate native test IDs')
    for name, values in [('model_inputs.jsonl', inputs), ('labels.jsonl', labels), ('input_provenance.jsonl', ledger)]:
        save_bytes(target / name, ''.join(json.dumps(value, ensure_ascii=False) + '\n' for value in values).encode())
    save_json(target / 'image_manifest.json', list(images.values()))
    save_json(target / 'ordered_case_ids.json', ids)
    return {'status': 'prepared_native_test', 'task': task, 'variant': VARIANT, 'cases': len(inputs),
            'unique_images': len(images), 'answer_groups': dict(Counter(label['answer_type'] for label in labels)),
            'input_file': str((target / 'model_inputs.jsonl').relative_to(ROOT)),
            'label_file': str((target / 'labels.jsonl').relative_to(ROOT)),
            'case_ids_file': str((target / 'ordered_case_ids.json').relative_to(ROOT)),
            'image_manifest': str((target / 'image_manifest.json').relative_to(ROOT)),
            'files': [{'path': str(path.relative_to(ROOT)), 'bytes': path.stat().st_size, 'sha256': file_sha(path)}
                      for path in sorted(target.glob('*')) if path.is_file()],
            'model_facing_fields': ['original_question_text', 'original_image_bytes'],
            'scorer_only_fields': ['target_answer', 'answer_type', 'source_qid'],
            'prompt_policy': 'Original source question string unchanged; one original image; no answer-type-derived instruction, reference/caption, candidate answer list or system message.',
            'model_comparison': 'Qwen zero-shot image/question baseline; native dataset/split/metrics, distinct model chat template and task-training regime from paper systems.',
            'contamination': 'Public release; prior model exposure unknown. Native VQA-RAD has train/test image overlap; no local training or retrieval uses these artifacts.'}


def prepare_rad(offline=False):
    meta_url = 'https://api.osf.io/v2/nodes/89kps/files/osfstorage/'
    listing = json.loads(fetch('osf_files.json', meta_url, offline=offline).read_text())
    by_name = {item['attributes']['name']: item for item in listing['data']}
    data_item = by_name['VQA_RAD Dataset Public.json']
    assert data_item['attributes']['extra']['hashes']['sha256'] == RAD_JSON_SHA
    original = fetch('rad_original.json', data_item['links']['download'], RAD_JSON_SHA, offline)
    archive_url = 'https://files.osf.io/v1/resources/89kps/providers/osfstorage/5b21453986d8510011c277bc/?zip='
    archive = fetch('rad_original_images.zip', archive_url, offline=offline)
    images = {}
    index, url = 1, 'https://api.osf.io/v2/nodes/89kps/files/osfstorage/5b21453986d8510011c277bc/?page%5Bsize%5D=100'
    page_sources = []
    while url:
        name = 'rad_image_listing.json' if index == 1 else f'rad_image_listing_page{index}.json'
        page_path = fetch(name, url, offline=offline)
        page = json.loads(page_path.read_text())
        page_sources.append(source_entry(page_path, url))
        for image in page['data']:
            attrs = image['attributes']
            images[attrs['name']] = attrs['extra']['hashes']
        url = page['links']['next']
        index += 1
    with zipfile.ZipFile(archive) as z:
        assert set(z.namelist()) == set(images)
        for name, hashes in images.items():
            if sha256(z.read(safe_member(name))) != hashes['sha256']:
                raise ValueError('Original full image archive failed publisher digest verification')
    node_url = 'https://api.osf.io/v2/nodes/89kps/'
    node = json.loads(fetch('rad_osf_node.json', node_url, offline=offline).read_text())
    license_url = node['data']['relationships']['license']['links']['related']['href']
    license_path = fetch('rad_osf_license.json', license_url, offline=offline)
    license_data = json.loads(license_path.read_text())
    rows = select_test_rows('V01', json.loads(original.read_text()))
    result = prepare_rows('V01', rows, archive, lambda row: row['image_name'], images)
    assert result['cases'] == 451 and result['unique_images'] == 203
    assert result['answer_groups'] == {'CLOSED': 272, 'OPEN': 179}
    result.update({'source_homepage': 'https://osf.io/89kps/', 'source_release': 'original OSF files, version1, 2018-06-13',
                   'selection': 'Original row order; phrase_type in {test_freeform,test_para}; no target-answer filtering.',
                   'license': license_data['data']['attributes'],
                   'source_files': [source_entry(original, data_item['links']['download'], publisher_sha256=RAD_JSON_SHA,
                                                 publisher_digest_verified=True), source_entry(archive, archive_url,
                                                 full_archive_image_count=len(images), every_image_publisher_sha256_verified=True),
                                    source_entry(license_path, license_url)] + page_sources})
    return result


def prepare_slake(offline=False):
    meta = json.loads(fetch('slake_hf.json', f'https://huggingface.co/api/datasets/BoKelvin/SLAKE/revision/{SL_REV}?blobs=true', offline=offline).read_text())
    if meta['sha'] != SL_REV:
        raise ValueError('SLAKE source revision mismatch')
    files = {item['rfilename']: item for item in meta['siblings']}
    base = f'https://huggingface.co/datasets/BoKelvin/SLAKE/resolve/{SL_REV}/'
    test = fetch('slake_original_test.json', base + 'test.json', offline=offline)
    if git_blob_sha(test.read_bytes()) != files['test.json']['blobId']:
        raise ValueError('SLAKE test metadata publisher Git blob mismatch')
    archive = fetch('slake_original_imgs.zip', base + 'imgs.zip', SL_IMAGES_SHA, offline)
    if files['imgs.zip']['lfs']['sha256'] != SL_IMAGES_SHA:
        raise ValueError('SLAKE publisher archive identity mismatch')
    card = fetch('slake_original_README.md', base + 'README.md', offline=offline)
    if git_blob_sha(card.read_bytes()) != files['README.md']['blobId']:
        raise ValueError('SLAKE dataset card blob mismatch')
    rows = select_test_rows('V02', json.loads(test.read_text()))
    result = prepare_rows('V02', rows, archive, lambda row: 'imgs/' + row['img_name'])
    assert result['cases'] == 1061 and result['unique_images'] == 96
    assert result['answer_groups'] == {'OPEN': 645, 'CLOSED': 416}
    result.update({'source_homepage': 'https://www.med-vqa.com/slake/', 'source_dataset': 'BoKelvin/SLAKE',
                   'source_revision': SL_REV, 'license': 'CC-BY-4.0, as declared on author HuggingFace card',
                   'source_release_caveat': 'Author website notes SLAKE1.0 was cleaned after original publication; exact 1061-case English test agrees with LLaVA-Med paper counts.',
                   'selection': 'Original test.json row order; q_lang == en only; no target-answer filtering.',
                   'source_files': [source_entry(test, base + 'test.json', publisher_git_blob_sha1=files['test.json']['blobId'], publisher_digest_verified=True),
                                    source_entry(archive, base + 'imgs.zip', publisher_sha256=SL_IMAGES_SHA, publisher_digest_verified=True),
                                    source_entry(card, base + 'README.md')]})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task', choices=['V01', 'V02', 'all'], default='all')
    parser.add_argument('--offline', action='store_true')
    args = parser.parse_args()
    report = json.loads(REPORT.read_text()) if REPORT.exists() else {'datasets': {}}
    report.update({'updated_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'inference_dispatched': False,
                   'native_scoring_source_revision': LL_REV,
                   'native_scoring_files': acquire_native_metrics(args.offline),
                   'scorer_contract': {'normalization': 'Unchanged official glossary.normalize_word; lowercase, punctuation, articles, numeric words and contractions.',
                                       'open_metric': 'Mean calculate_f1score(prediction,reference)[2] token recall over all OPEN cases; invalid/missing outputs count zero.',
                                       'closed_metric': 'Unchanged run_eval.py CLOSED branch: normalized output contains yes or no and contains normalized target. Substring quirks preserved and disclosed.',
                                       'additional_diagnostics': 'Native open token precision and F1 can be reported separately. Native named exactmatch is not strict exact equality.',
                                       'candidate_remapped_open_accuracy': 'Not prepared: requires source training-derived candidate.json; not reconstructed from test labels.',
                                       'parser': 'Full final assistant content string, no answer-key-assisted extraction or paid grader.'},
                   'restrictions': ['Preparation only; no model inference or authorization edits.', 'Source answers, answer groups, image metadata and reference contexts stay scorer-side.',
                                    'Public benchmark exposure unknown; no contamination-free claim.', 'Research evaluation, not clinical deployment.']})
    for task, fn in [('V01', prepare_rad), ('V02', prepare_slake)]:
        if args.task not in [task, 'all']:
            continue
        try:
            report['datasets'][task] = fn(args.offline)
        except (OSError, ValueError, RuntimeError, KeyError, zipfile.BadZipFile) as error:
            report['datasets'][task] = {'status': 'blocked', 'error_type': type(error).__name__, 'reason': str(error)}
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
        summary = report['datasets'][task]
        print(json.dumps({key: summary.get(key) for key in ['task', 'status', 'cases', 'unique_images', 'answer_groups', 'reason']}), flush=True)
    return 0 if all(report['datasets'].get(t, {}).get('status') == 'prepared_native_test'
                    for t in (['V01', 'V02'] if args.task == 'all' else [args.task])) else 1


if __name__ == '__main__':
    raise SystemExit(main())
