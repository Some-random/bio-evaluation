#!/usr/bin/env python3
"""Export aggregate follow-up evidence; never export raw datasets or weights."""
from datetime import datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.local/source_recovery_round2_2026-10-19'
FIELDS = ('stage', 'status', 'updated_at_pacific', 'finished_at_pacific', 'pid',
          'downloaded_files', 'downloaded_bytes', 'planned_source_files',
          'planned_vendor_files', 'planned_vendor_bytes', 'verified_vendor_chunk_bytes',
          'all_selected_files_verified', 'recovered_images', 'remaining_missing_images',
          'original_name_native1024_images', 'current_source_rendering_images',
          'historical_byte_verified_images', 'unrecovered_native1024_images',
          'academic_alternate_rendering_images',
          'academic_alternate_rendering_additional_page_identities',
          'docrag_verified_images', 'docrag_failed_images',
          'docrag_original_name_native1024_images',
          'processed_native_dimension1024_images', 'native_resolution_page_identities_available',
          'unrecovered_native1024_definition', 'recovered_images_definition',
          'official_cif_structure_count', 'direct_legacy_chain_compatible_count',
          'split_chain_cases_requiring_mapping_review',
          'planned_missing_images', 'mixed_source_recovery_definition',
          'exact_native_table3_ready', 'native_mask_and_test_roster_definitions_recovered',
          'exact_historical_numbered_structure_bytes_verified',
          'authenticated_dataset_complete', 'authenticated_dataset_verified_files',
          'authenticated_dataset_planned_files', 'authenticated_dataset_verified_bytes',
          'authenticated_dataset_failed_files',
          'failed_source_count', 'hf_existing_login_found', 'hf_access_status',
          'planned_structures', 'verified_structures', 'model_calls',
          'new_inference_calls', 'inference_calls', 'training')


def read(path):
    return json.loads(path.read_text()) if path.is_file() else None


def main():
    records = {}
    hashes = {}
    for name in ('pfarena', 'slidevqa', 'paper_artifacts', 'structural', 'rabd_imgt', 'ryze_protocol'):
        path = BASE / name / 'status.json'
        raw = path.read_bytes() if path.is_file() else None
        source = json.loads(raw) if raw is not None else None
        records[name] = {'available': source is not None,
                         'source_path': str(path.relative_to(ROOT))}
        if source is not None:
            records[name]['summary'] = {k: source[k] for k in FIELDS if k in source and
                (source[k] is None or type(source[k]) in (int, float, str, bool))}
            hashes[str(path.relative_to(ROOT))] = hashlib.sha256(raw).hexdigest()
    for folder in ('pfarena', 'paper_artifacts', 'structural', 'slidevqa', 'rabd_imgt', 'ryze_protocol'):
        for name in ('PUBLIC_SUMMARY.json', 'completion.json', 'PUBLIC_SUMMARY.md', 'RECOVERY_SUMMARY.md',
                     'demo_fixture_validation.json', 'source_protocol_contract.json',
                     'glm_arxiv_fanout_patch_receipt.json'):
            path = BASE / folder / name
            if path.is_file():
                hashes[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    stamp = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    data = {'generated_at_pacific': stamp,
            'role': 'aggregate_source_recovery_evidence_not_benchmark_results',
            'new_inference_calls': 0, 'new_training': False,
            'full_catalog_complete': False, 'model_weights_published': False,
            'restricted_slidevqa_content_published': False,
            'workers': records, 'evidence_receipt_sha256': hashes,
            'interpretation': 'Reproduction code, live source renderings and reconstructed protocols are explicitly distinct from exact native paper artifacts.'}
    vendor = read(BASE / 'structural/manifest.json') or {}
    data['verified_vendor_assets'] = [{k: a[k] for k in (
        'id', 'state', 'bytes', 'sha256', 'publisher_sha256_verified',
        'publisher_multipart_etag_verified') if k in a}
        for a in vendor.get('assets', []) if a.get('id')]
    data['local_transport_validation'] = read(BASE / 'structural/range_resume_validation_receipt.json')
    for name in ('completion.json', 'completion_reconciliation.json'):
        path = BASE / 'pfarena/authenticated' / name
        if path.is_file():
            hashes[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    native_preflight = {}
    for name, filename in (('pfarena', 'PUBLIC_SUMMARY.json'), ('slidevqa', 'source_preflight.json')):
        path = BASE / name / 'native_preflight' / filename
        receipt = read(path)
        if receipt is not None:
            hashes[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
            # PFArena's explicit public projection contains aggregate source checks only.
            # SlideVQA exports scalar coverage/provenance, never per-case licensed records.
            native_preflight[name] = receipt if name == 'pfarena' else {
                k: v for k, v in receipt.items() if v is None or type(v) in (int, float, str, bool)}
    data['native_input_preflight'] = native_preflight
    target = ROOT / 'reports/SOURCE_RECOVERY_FOLLOWUP_2026-10-19.json'
    target.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    structural = records['structural'].get('summary', {})
    pfarena = records['pfarena'].get('summary', {})
    slide = read(BASE / 'slidevqa/visrag_image_recovery_completion.json') or {}
    current = read(BASE / 'slidevqa/decoded_current_rendering_completion.json') or {}
    slide_status = records['slidevqa'].get('summary', {})
    rabd_status = records['rabd_imgt'].get('summary', {})
    verified_vendor = sum(a.get('state') == 'downloaded_verified' for a in vendor.get('assets', []) if a.get('id'))
    lines = ['# Follow-up recovery of evaluation inputs and tools', '',
        'Snapshot: ' + stamp + ' (America/Los_Angeles).', '',
        'The initial bulk transfers were not the end of source recovery. This follow-up checked author histories, supplements, public original-image copies and tool dependencies. No new benchmark inference, training or model forwards were run.', '',
        '| Area | Additional recovery | Exact remaining limit |', '|---|---|---|',
        '| PFArena | Authenticated official dataset: ' + str(pfarena.get('authenticated_dataset_verified_files', 'unknown')) + '/' + str(pfarena.get('authenticated_dataset_planned_files', 'unknown')) + ' publisher-verified files (' + str(pfarena.get('authenticated_dataset_verified_bytes', 'unknown')) + ' bytes), plus 247 verified source/history artifacts. User-enabled access resolved the former 401 prerequisite. | Dataset availability is resolved. Native preparation/input review and strict scorer coverage remain necessary; the default lenient evaluator fabricates missing-assay substitutes and must not be used for reported scores. |',
        '| SlideVQA | Processed 1024px same-deck/page copies: ' + str(slide_status.get('processed_native_dimension1024_images', slide_status.get('docrag_verified_images', 'unknown'))) + '/300. Additionally, ' + str(slide_status.get('original_name_native1024_images', slide.get('recovered_images', 'unknown'))) + ' original-name native-resolution academic copies, ' + str(current.get('verified', 'unknown')) + ' current deck renderings and 9 academic alternate renderings are separately archived. | The processed corpus re-encodes images: 0/860 available overlaps were byte/pixel-identical. All seven independent native-resolution copies matched the correct processed page in the identity check. This closes missing page availability, while exact historical image encoding remains unresolved. |',
        '| NatureLM / SFM | Complete paper/supplement sources, official daily PDF, all 30 property prompts, 20 historical author revisions and a published SciReasoner reproduction with data/evaluator code recovered. | Exact binary target mapping, absolute temporal cohort, fine-tuned property heads and 1,000-reference IDs remain unlocated. The reproduction\'s threshold/wiring do not establish the native mapping; its 99% clustering differs from the paper\'s 50% condition. |',
        '| Proteo-R1 / MEAN tools | Complete pinned repository archives verified against 173 and 73 Git blobs; pinned Protenix submodule acquired; 83 fixture/helper/evaluator files materialized. All five official demo fixture sets pass presence and NPZ CRC checks. Vendor files verified: ' + str(verified_vendor) + '/5. | Five public demo cases are not the full paper holdout. Model execution and native full-cohort identity remain separate work. |',
        '| RAbD / P40 | Recovered the current official SAbDab2 structures for the exact 60-entry roster, plus a publisher-verified 60-reference PDB bundle from AAMFM. Released IMGT numbering code defines deterministic CDR-H3 masks. Validation stage: ' + str(rabd_status.get('stage', 'unknown')) + '. | 57 current official structures have straightforward legacy-chain compatibility; three scFv entries split older chain identities. AAMFM uses cropped inputs and changes 15 original chain contracts. Neither bundle is silently substituted for exact historical MEAN inputs. |',
        '| Ryze / V07 | 26 additional artifacts and 32 reverified author code files; complete histories and released mapping inventories checked. An isolated, synthetic-tested preparation patch preserves all questions sharing a figure instead of overwriting 45,601 mappings. | Released entrypoints differ in image-plus-OCR versus OCR-only input, decoding and system labels. No certified ChartQA implementation, original Table 3 cohort or aggregation records were located. The patch does not change original source or benchmark outputs. |', '',
        '## Current tool transfer', '',
        'Stage: ' + str(structural.get('stage', 'unknown')) + '. Verified range bytes: ' + str(structural.get('verified_vendor_chunk_bytes', 'unknown')) + ' / ' + str(structural.get('planned_vendor_bytes', 'unknown')) + '. Sparse file size is never counted as transferred or verified data. Final file SHA256 and publisher SHA256 or multipart ETag checks are recorded separately.', '',
        '## Precise paper-protocol gaps', '',
        'NatureLM/SFM recovery includes 75 HTTP artifacts (22,776,793 bytes), the 30 official property prompts and the published reproduction. The reproduction supplies a numerical threshold but wires a different evaluator cascade and uses 99% rather than the paper\'s 50% clustering. Its code cannot certify the native binary mapping, temporal cohort or property-head contract. These are specific unresolved artifacts, rather than a claim that useful source code is unavailable.', '',
        'Ryze\'s released mapping inventories cover 100,000 ArxivQA questions over 54,399 figures and 2,215 SlideVQA questions over 400 decks. They identify released inputs, not the exact membership of the Table 3 runs. A single binary outcome over all 2,215 SlideVQA cases cannot reproduce two reported percentages under ordinary rounding; another cohort or aggregation could explain them. No paper-error claim follows. The recovered protocol receipt records the differing entrypoints, absent ChartQA implementation and missing original execution records.', '',
        'The ArxivQA fanout patch is frozen separately with synthetic checks for shared-image questions, existing outputs and dry-run behavior. It is a preparation correction, not a new score. Source recovery alone does not authorize benchmark dispatch.', '',
        '[Preparation patch](../scripts/source_preparation/ryze_arxiv_fanout_20261019.patch) · [Synthetic patch-check receipt](SOURCE_PREPARATION_REPAIR_2026-10-19.json). Seven additional local transport tests cover exact ranges, response lengths, corruption detection and completed-file reuse; they made no network or model calls.', '',
        '## Source and publication boundaries', '',
        'Original acquisition receipts and frozen Qwen outputs are preserved. Image archives, restricted SlideVQA material, raw reproduction data, source files with unreviewed credential-like comments and model weights stay local. This page exports aggregate counts and provenance only.', '',
        '[Initial acquisition](SOURCE_ACQUISITION_PROGRESS_2026-10-19.md) · [Official PFArena](https://github.com/AMix-Bio/PFArena) · [Proteo-R1](https://github.com/smiles724/Proteo-R1) · [MEAN](https://github.com/THUNLP-MT/MEAN) · [NatureLM resources](https://github.com/NatureLM/Resources) · [Ryze-Data](https://github.com/Chivier/Ryze-Data)', '',
        'Live aggregate receipts feed the existing two-hour progress schedule. A completed source search is not a completed benchmark score.']
    extra = []
    if 'pfarena' in native_preflight or 'slidevqa' in native_preflight:
        extra = ['## Offline input preflight begun at 8 PM PDT', '',
                 'These are newly timestamped checks from the 8 PM update, not evidence of intervening background evaluation between 6 and 8 PM. No inference, scoring or protocol adoption occurred.', '']
    if 'pfarena' in native_preflight:
        pfa = native_preflight['pfarena']
        counts = ', '.join(x['task_id'] + ' ' + str(x['on_disk_target_table_count'])
                           for x in pfa['per_task_path_coverage'])
        extra += ['PFArena: ' + counts + ' = ' + str(pfa['target_table_count']) +
                  ' task tables, with all pinned target paths present and nonempty and all 29 T4 context pairs available. These are file/table counts, not model calls or benchmark cases. Ten source files pass syntax checks. Input/reference isolation, a frozen case-scoped configuration and runtime/delivery checks remain unfinished.', '',
                  'The direct LLM branch does not inherently require PLM or AlphaFold calls. The native strict scorer checks assay coverage and minimum top-k counts, but does not enforce a complete candidate permutation; missing ranking tails are assigned deterministic ranks. Strict scoring alone must not be described as full answer delivery. Native formulas remain unchanged, and no actual prediction coverage or score effect has been assessed.', '']
    if 'slidevqa' in native_preflight:
        vis = native_preflight['slidevqa']
        extra += ['SlideVQA: verified ' + str(vis['question_page_links_verified']) +
                  ' ordered case-to-page links across ' + str(vis['expected_distinct_page_identities']) +
                  ' page identities and ' + str(vis['expected_deck_count']) + ' decks. An explicitly prospective condition using 7,700 originals plus 300 processed copies covers ' +
                  str(vis['prospective_questions_with_all20_images']) + '/' + str(vis['expected_question_count']) +
                  ' questions with all 20 images, compared with 2,125 using only the first acquisition. Missing, duplicate, foreign and reordered page references are zero. This establishes input availability for that distinct encoding condition; it has not been adopted or dispatched and does not establish the paper\'s exact Ryze recipe.', '']
    boundary = lines.index('## Source and publication boundaries')
    lines[boundary:boundary] = extra
    (ROOT / 'reports/SOURCE_RECOVERY_FOLLOWUP_2026-10-19.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'generated_at_pacific': stamp, 'worker_records': len(records),
                      'vendor_files_verified': verified_vendor, 'evidence_receipts': len(hashes)}))


if __name__ == '__main__':
    main()
