#!/usr/bin/env python3
"""Write disabled GFP-only prospective protocols, without inference or training."""
from __future__ import annotations
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REVISION = '1e331e8c6d80677fcf446d84bb2de8811dfecc09'
MODEL_REVISION = '1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    contract = json.loads((ROOT / 'data/proxy_generation_native/P42/native_reference_contract.json').read_text())
    source = contract['sequence']
    assert len(source) == 237 and hashlib.sha256(source.encode()).hexdigest() == contract['sequence_sha256']
    source_path = ROOT / contract['source_file']
    raw = source_path.read_bytes()
    tree = json.loads((ROOT / 'sources/stride_tree.json').read_text())
    native_path = 'scripts/eval/infer_protein_vllm.py'
    blob = next(r['sha'] for r in tree['tree'] if r['path'] == native_path)
    assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == blob
    # Only the already inspected pure prompt builder is compiled. No imports,
    # generation entrypoint, checkpoint loading, random mutation or forward call.
    module = ast.parse(raw)
    node = next(n for n in module.body if isinstance(n, ast.FunctionDef) and n.name == 'build_prompt')
    namespace = {'List': list, 'Dict': dict}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(source_path), 'exec'), namespace)
    native_messages = namespace['build_prompt'](source)
    assert [r['role'] for r in native_messages] == ['system', 'user']
    additions = {
        'replace_only': '\nEvaluation condition for this sample:\nMake only amino-acid replacements and preserve the sequence length. The final sequence must differ from WT at exactly 1, 2, or 3 amino-acid positions. Return one candidate under these constraints.\n',
        'full_atomic': '\nEvaluation condition for this sample:\nINSERT, DELETE, and REPLACE of individual amino acids are permitted. The minimum number of these operations needed to transform WT into the final sequence must be exactly 1, 2, or 3. Return one candidate under these constraints.\n',
    }
    out = ROOT / 'data/stride_gfp_qualified_p42'
    out.mkdir(exist_ok=True)
    files = []
    for regime, addition in additions.items():
        messages = [dict(r) for r in native_messages]
        messages[1]['content'] += addition
        variant = f'QWEN_GFP_QUALIFIED_{regime.upper()}_ENDPOINT_1_TO_3'
        path = out / f'{regime}.inputs.proposed.jsonl'
        assert not path.exists(), f'Preserve previous proposal: {path}'
        rows = [{'task_id':'P42', 'case_id':f'p42:{regime}:{i:03d}',
                 'protocol_variant':variant, 'split':'fixed_publisher_anchor_generated_candidates',
                 'sample_index':i, 'seed':42+i, 'messages':messages} for i in range(100)]
        path.write_text(''.join(json.dumps(r, ensure_ascii=True) + '\n' for r in rows))
        files.append({'regime':regime, 'path':str(path.relative_to(ROOT)), 'sha256':sha(path),
                      'rows':100, 'variant':variant, 'prospective_prompt_addition':addition})
    asset_receipts = json.loads((ROOT / 'reports/proxy_oracle_acquisition.json').read_text())['assets']
    assets = [r for r in asset_receipts if r.get('repository') in {
        'SaProtHub/Model-Fluorescence-650M', 'westlake-repl/SaProt_650M_AF2'}]
    assert len(assets) == 8 and all(r['publisher_digest_verified'] for r in assets)
    plan = {
        'task_id':'P42', 'status':'disabled_pending_root_review_and_specialized_runner_runtime_freeze',
        'execution_authorized':False, 'generation_authorized':False, 'oracle_forward_authorized':False,
        'proposal_kind':'qualified_adaptation_with_partial_native_metrics',
        'exact_native_paper_replication':False, 'original_paper':'https://arxiv.org/html/2603.03573v1',
        'source_revision':SOURCE_REVISION, 'model_id':'Qwen/Qwen3.8-27B', 'model_revision':MODEL_REVISION,
        'model_precision':'BF16', 'source_sequence_sha256':contract['sequence_sha256'],
        'inputs':files, 'total_candidate_slots':200, 'candidate_slots_per_regime':100,
        'seed_schedule':{'rule':'42 + sample_index', 'range_inclusive':[42,141],
                         'reused_across_regimes':True,
                         'qualification':'Explicit HTTP sampling adaptation from publisher persistent RNG and n=10 batching. No identical-prompt seed42 reuse for every candidate.'},
        'generation':{'temperature':0.7, 'top_p':0.9, 'top_k':-1, 'min_p':0.0,
                      'max_tokens':1024, 'n':1, 'presence_penalty':0.0, 'frequency_penalty':0.0,
                      'repetition_penalty':1.0, 'enable_thinking':True},
        'sampling_controls':{'preserve_all_duplicates':True, 'no_retries_or_output_repair':True,
                             'no_sampling_until_valid_or_improved':True,
                             'no_oracle_feedback_or_candidate_selection':True,
                             'all_200_generations_frozen_before_oracle_scoring':True},
        'system_and_user_roles':'Retain both native messages; append only the declared regime endpoint constraint to the user message.',
        'channel_handling':'Archive actual reasoning/final independently. For source parser compatibility only, an explicit reasoning field is reconstructed as <think>reasoning</think>final. Never recover a candidate from reasoning-only JSON or repair malformed final JSON.',
        'validity':{'alphabet':'uppercase AA20, no sequence normalization or cropping',
                    'replace_only':'same length and Hamming distance 1..3',
                    'full_atomic':'Levenshtein distance 1..3 under unit INSERT/DELETE/REPLACE costs',
                    'endpoint_vs_trajectory':'Endpoint distance proves existence of a short edit path, not correctness or length of a model-generated trajectory. Trajectory correctness remains unassessed.'},
        'oracle':{'assets':assets, 'device':'cpu', 'dtype':'float32',
                  'runtime_environment':'NEW isolated CPU environment, not the active vLLM environment; exact dependency lock must be frozen before any load/forward.',
                  'native_preprocessing':'Append # after each amino acid, pinned EsmTokenizer, padding=True, truncation=True, max_length=1024; retain full eligible sequences.',
                  'head_load_requirement':'Restore the pinned trained classifier and all LoRA adapter tensors. Audit loaded keys; never score with a random/unrestored classification head.',
                  'forward_order':'Source once, then exact first-occurrence unique eligible candidates in frozen regime/source-order; map cached scores back to all duplicate slots.',
                  'maximum_distinct_sequence_scores':201,
                  'numeric_comparison':'Raw finite float32 oracle scores; strict candidate > source, no tolerance/rounding/threshold selection.'},
        'metrics':{'qualified_oracle_success':'number of eligible improved samples /100, preserving invalid/missing generation slots as failures',
                   'improved_sequence_uniqueness':'distinct improved AA strings / improved sample count; null if denominator0',
                   'native_novelty':None, 'native_novelty_status':'blocked_missing_exact_positive_SFT_Dplus_membership',
                   'missing_oracle_handling':'Any eligible candidate with missing/nonfinite score withholds primary success/uniqueness; never impute score0.',
                   'diagnostics':['format delivery','endpoint validity','length finish count','length-changing endpoints','duplicate count','oracle failures'],
                   'task_completion_claim':'Qualified success/uniqueness may complete; P42 full native metric set remains incomplete while novelty/protocol recovery is blocked.'},
        'frozen_dependencies':[{'path':p,'sha256':sha(ROOT/p)} for p in [
            'scripts/stride_gfp_qualified_contract.py','scripts/prepare_stride_gfp_qualified_proposal.py',
            'sources/proxy_generation_native/stride__scripts__eval__infer_protein_vllm.py',
            'sources/stride__scripts__eval__score_fluorescence.py',
            'data/proxy_generation_native/P42/native_reference_contract.json',
            'sources/proxy_generation_native/saprot_adapter_tensor_inventory.json']],
        'remaining_execution_gates':['Root approves concrete qualified case/protocol scope.',
             'New specialized runner preserves native system+user roles and records per-slot distinct seeds/raw channels.',
             'Freeze HTTP request, scorer wrapper and separate CPU oracle runtime/dependencies.',
             'Freeze all asset/tokenizer/preprocessing hashes and audit trained classifier restoration before forward.',
             'Audit actual prompt tokens plus1024 output against publisher4096 context bound.'],
        'interpretation':{'likely_demands_provisional':['learned sequence-property prediction','local candidate proposal','instruction-following under endpoint constraints'],
                          'information_supplied':'Publisher GFP anchor, native goal/system/user prompt and declared endpoint regime constraint; no oracle outputs, labels, D+ membership, tools or training.',
                          'reference_evidence':'Fixed trained SaProt regression-head predictions, not new laboratory measurements.',
                          'good_score':'Higher oracle-scored candidates within this declared endpoint budget and sampling protocol.',
                          'bad_score':'Limited eligible delivery or oracle improvement under this budget; does not isolate reasoning capability.',
                          'rationale_correctness':'Unassessed separately from outcome scores; unsupported mechanisms are not automatically false.',
                          'contamination':'Prior exposure to public GFP data is unknown.'},
    }
    dest = ROOT / 'configs/stride_gfp_qualified_p42.proposed.json'
    assert not dest.exists(); dest.write_text(json.dumps(plan, indent=2) + '\n')
    print(json.dumps({'proposal':str(dest), 'sha256':sha(dest), 'input_rows':200}, indent=2))

if __name__ == '__main__':
    main()
