"""Build a source-only P34 feasibility report; never load weights or run a model."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED = ["AMIE", "avGFP", "E4B", "LGK", "UBE2I"]
OUT = ROOT / "reports/p34_five_landscape_feasibility_2026-10-15"


def sha(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main() -> None:
    sizes = json.loads((ROOT / "reports/p34_five_landscape_input_size_audit.json").read_text())
    tokenizer = "reports/p34_qwen_likelihood_tokenizer_feasibility.json"
    assert sha(tokenizer) == "b5b00b4757b7d1a45bf024adb5b24521d544fc73f85e07aa6fec3a5340b5ec1e"
    native = "sources/p34_five_landscape_feasibility/"
    sources = [
        native + "evaluator.py", native + "model__modeling_esm.py",
        native + "native_cli_source.sh", native + "configs__mutaplm_inference.yaml",
        native + "allowed_contexts.json", native + "esm1b__vocab.txt",
        native + "esm2__vocab.txt", native + "esm2_metadata_info.json",
        "sources/muta__model__mutaplm.py",
        "sources/proxy_generation_native/muta__model__esm_landscape.py",
        "sources/proxy_generation_native/pex_selected_assets_receipt.json",
        "sources/proxy_generation_native/esm1b_base_info.json",
        "sources/proxy_generation_native/esm1b_base_tree.json",
        "reports/p34_five_landscape_input_size_audit.json", tokenizer,
    ]
    rows = []
    for row in sizes["rows"]:
        name, length = row["landscape"], row["sequence_characters"]
        assert name in ALLOWED
        rows.append({
            **row,
            "native_complete_run_states_per_seed": 181,
            "native_states_all_20_seeds": 3620,
            "native_complete_run_proposal_batch_calls_all_seeds": 920,
            "native_complete_run_oracle_batch_calls_all_seeds": 1020,
            "native_complete_run_oracle_scalar_values_all_seeds": 4020,
            "conditional_if_all_states_keep_initial_length": {
                "binary_position_plus_33_complete_newline_labels_prefix_evaluations_per_state": 45 * length,
                "all_20_seeds_prefix_evaluations": 45 * length * 3620,
                "binary_position_plus_33_prefix_free_label_events_per_state": 12 * length,
                "all_20_seeds_prefix_free_event_evaluations": 12 * length * 3620,
                "categorical_complete_position_plus_33_complete_labels_per_state": 45 * length + 1,
                "categorical_all_20_seeds_prefix_evaluations": (45 * length + 1) * 3620,
            },
        })

    report = {
        "task_id": "P34",
        "date": "2026-10-15",
        "status": "source_only_feasible_adapter_design_requires_protocol_resolution_not_activated",
        "allowed_landscapes": ALLOWED,
        "held_landscape_excluded": "AAV",
        "entire_six_landscape_paper_setting_completed": False,
        "scope": {
            "model_forward_calls": 0, "model_generations": 0, "new_training": False,
            "sampler_executed": False, "new_large_base_acquired": False,
            "new_protocol_frozen": False, "existing_frozen_files_modified": False,
            "raw_fitness_or_mutation_rows_acquired": False,
            "access_note": "An earlier shared fitness_dataset.py display exposed the held key's dictionary entry; root was informed. No held sequence, weights, rows, calls, or downloads were accessed. Subsequent selection used AST and the five-name allowlist.",
        },
        "conclusion": {
            "prediction_task_retained": True,
            "missing_learned_qwen_joint_head_is_not_a_task_exclusion": True,
            "qualified_adapter_mathematically_possible": True,
            "same_published_paper_condition_established": False,
            "reason": "A Qwen likelihood adapter can supply nonnegative full-grid weights and preserve the released selection/oracle budgets, but the source uses per-position binary mass and all33 classes, and differs from paper Algorithm1. A categorical-position/AA20 shortcut would silently change head scale and support. Dynamic string edits and the unprobed full-prefix interface prevent a fixed actual request count or an activation-ready native claim.",
        },
        "primary_sources": {
            "mutaplm_commit": "495815b2069419d19d9449a59070d0fb24b596d1",
            "evaluator_url": "https://github.com/PharMolix/MutaPLM/blob/495815b2069419d19d9449a59070d0fb24b596d1/evaluator.py#L190-L323",
            "head_url": "https://github.com/PharMolix/MutaPLM/blob/495815b2069419d19d9449a59070d0fb24b596d1/model/modeling_esm.py#L1358-L1373",
            "wrapper_url": "https://github.com/PharMolix/MutaPLM/blob/495815b2069419d19d9449a59070d0fb24b596d1/model/mutaplm.py#L760-L821",
            "oracle_url": "https://github.com/PharMolix/MutaPLM/blob/495815b2069419d19d9449a59070d0fb24b596d1/model/esm_landscape.py#L25-L45",
            "paper_url": "https://arxiv.org/html/2410.22949v1#A3.SS4",
            "pex_commit": "9ed7a814f0cd17920728641a58736f781bff9ece",
            "esm1b_revision": "7b37824baec4d3658e1df7479222a7c79b465b76",
            "esm2_metadata_revision": "08e4846e537177426273712802403f7ba8261b6c",
            "esm_metadata_note": "ESM2 and ESM1b vocab.txt bytes agree. Only small pinned config/tokenizer/vocabulary metadata were acquired; no encoder weights.",
        },
        "released_native_math": {
            "tensor_axes": "[current parent batch B, padded ESM-token positions P, ESM vocabulary33]; initial P=L+2 for canonical starting sequences",
            "position_weight": "r[b,p]=softmax(position_logits[b,p,:]/0.5)[1] * attention_mask[b,p]; then r[:,0]=0 and r[input_ids==2]=0",
            "residue_weight": "a[b,p,k]=softmax(AA_logits[b,p,:]/0.5)[k], k=0..32",
            "new_local_weight": "q[b,p,k]=r[b,p]*a[b,p,k]. Positions are not normalized globally; sum(q) equals sum(r), not1.",
            "prior": "W[b,p,k]=q[b,p,k]+previous_selected_weight[b], broadcast over every P*33 cell after source position masks. Initial previous weight is0. Selected W becomes next round's previous weight; no logarithm, multiplication, sign inversion, or global softmax is applied in the released evaluator.",
            "parent_mass": "sum_{p,k} W[b,p,k] = sum_p r[b,p] + P*33*previous_selected_weight[b] (including cells whose q is0). Rescaling q per parent changes competition against this inherited term.",
            "sampling": "torch.multinomial(W.flatten(),20), default replacement=False; implicit weight normalization only inside multinomial. Native RNG seed is torch.random.manual_seed(seed), seed0..19 once per independent run.",
            "order": "torch contiguous flatten: parent then token position then AA class. parent=floor(index/(P*33)); position=floor((index mod(P*33))/33); AA=ESM batch_decode(index mod33). Retain the sampled order and all duplicates across different cells/parents/rounds.",
            "string_edit": "cur[:position-1] + decoded_AA + cur[position:] using the ESM token position directly as a Python character offset. No WT/self-substitution, AA20, duplicate, BOS/EOS/padding, or sequence-validity filter is applied after sampling.",
            "oracle_feedback": "None: round fitness scores are logged and aggregated; model weights, sampling weights, parent ranking and next-round membership do not receive them.",
            "batch_size": 4,
            "proposal_batch_count_per_seed": "ceil(1/4)+9*ceil(20/4)=46 batches, representing1+9*20=181 parent states",
            "oracle_batch_count_per_seed": "1 initial batch +10*ceil(20/4)=51, containing1+10*20=201 scalar values",
        },
        "source_paper_protocol_differences": [
            "Paper Algorithm1 describes summed head scores followed by global softmax and sampling without replacement. Released code uses the local probability product plus an added inherited weight. These are separate protocol targets; no equivalence has been demonstrated.",
            "The released LGK goal is 'Increase in activity.'; TableA9 says 'Increased enzyme activity.'. Use the chosen source condition verbatim and qualify it.",
            "The paper depicts multi-point substitutions. Released support includes all33 classes and WT; positive inherited weight also revives BOS/EOS/padding cells from round2. A later canonical-only repair would alter that source condition.",
            "The paper describes SD shading; released arrays use np.var(ddof=0), and the printed Avg-score error term mistakenly reuses max-score variance. Preserve source outputs and label variance honestly; do not call it SD.",
        ],
        "dynamic_axis_and_length_risks": {
            "not_observed_failures": True,
            "facts": [
                "All33 native classes include27 single-character strings and6 special-token strings. The longest decoded string '<null_1>' has8 characters. Native WT substitutions may be no-ops.",
                "A sampled position0 produces cur[:-1]+AA+cur[0:], potentially nearly doubling character length. EOS/padding cells may append or index beyond the actual sequence; there is no source repair.",
                "After special strings or position0, ESM-token positions need not equal Python character positions. Different batch padding widths could make torch.cat fail; this is a source-level possibility, not a failure observed here.",
                "The native model tokenizer caps token length at1026 while the oracle caps1024. Exact source preservation cannot silently crop Qwen's full sequence or impose a fixed character-length invariant.",
            ],
            "loose_character_growth_bound": "With first-round position0 excluded and at most8 inserted characters, n1<=L+7; then n10<=(L+14)*512-7. This is only a conservative syntactic upper bound, not an empirical forecast.",
        },
        "information_supplied": {
            "source": "Current full protein string, the fixed five-name function descriptions, and each released objective. Source optimizer sets use_gt_function=True and muta_prompt='Not Available'; it does not infer a function first.",
            "source_context_file": native + "allowed_contexts.json",
            "not_supplied_to_qwen": "Oracle scores, assay labels, raw fitness train/valid rows, mutations selected by another model, and hidden/reference answers.",
            "incidental_loader": "FitnessDataset.__init__ opens valid.json and logs two examples in generic setup, but FitnessOptimizeEvaluator.evaluate only consumes dataset.starting_sequence. A standalone source-method adapter can provide that immutable start without acquiring/exposing those unused records; this wrapper dependency is not an assay-data scientific requirement.",
            "input_sizing": "Pinned-Qwen tokenizer only. Named-field concatenations below contain the full allowed start/function/goal; they are illustrative sizing, not approved prompts. Chat/task/prefix overhead and subsequent dynamic sequence growth remain additional.",
        },
        "qualified_execution_proposal_not_approved": {
            "label": "Qwen zero-shot replacement-head adapter with released-source sampler, five permitted landscapes",
            "possible_route_closest_to_head_type": [
                "Freeze a per-position binary textual likelihood question yielding logits for select/keep, normalized with source temperature0.5; do not normalize binary select probabilities across positions.",
                "Freeze per-position 33-class conditional label likelihoods, retaining the exact native vocabulary index mapping, WT eligibility and special/noncanonical strings; turn complete class log-likelihoods into a33-way softmax at0.5.",
                "Return q[b,p,k]=r[b,p]*a[b,p,k] with exact ESM token-axis masking. Pass that tensor through the original source prior addition, flattening, multinomial, selected-weight carry and string edit unchanged. Use source batch size4 and seed0..19.",
                "Archive every conditional likelihood/prefix, original input/payload, complete grid, tensor/mask shape, selected flat cell/order, prior weights, RNG states and every oracle input/output. No outcome-based retry, invalid-cell repair, deduplication, replacement, fitness selection, or training.",
                "Keep scoring isolated with the fixed original ESM1b encoder and the five existing trained decoder heads. Validate exact state restoration before any forward and preserve source1024-token preprocessing/batching.",
                "Freeze choice of complete-label event (with terminator) versus prefix-free token-label event before calls. Each is a distinct adaptation; neither is proof of learned-head equivalence.",
            ],
            "categorical_factorization_alternative": "p(position)*p(AA|position) gives a valid new nonnegative proposal grid. It is a separately qualified Qwen adapter because the native position head is Bernoulli per position; global position normalization changes inherited-weight scale. An AA20-only grid also changes support. Do not label this exact native-head semantics.",
            "paper_algorithm_route": "A separate prospective implementation could target paper Algorithm1 instead of the released source. It must resolve the head-score definition and declared sampling support, preserve20x10x20 and the exact original oracle, and explicitly disclose that released prior math was not used. Not approved or implemented here.",
            "synthetic_prerequisites_before_task_forward": [
                "Verify assistant-prefill semantics and all required fixed logprob-token IDs on loopback using synthetic strings only; installed-source acceptance of up to128 IDs is not a runtime proof. Existing observed proof covers two first-token IDs only.",
                "Synthetic nonbiological tensor fixtures must show identical source flatten/index/order/prior/mask behavior and exact20-without-replacement selection; do not sample any task protein before approval.",
                "Choose failure handling prospectively for source-validity/shape/context errors: report an incomplete run rather than repair or silently fill a missing budget.",
                "Resolve published-paper vs released-source target and approve the five-landscape scope, prompt/type calibration, class event and runtime budget, then freeze every executable/config/source/input/oracle hash.",
            ],
        },
        "likelihood_runtime_cost": {
            "exact_expression": "For proposed binary+complete-newline33-label head, conditional prefix evaluations =45*sum_over_18100_parent_states M_state, where M_state counts actual unmasked native token positions. The33-class trie needs44 evaluations per position and the binary question1. For prefix-free class-label cylinder events it is12*sum M_state (11 AA+1 binary). No sequences have been sampled, so actual M_state is unknown.",
            "conditional_all_five_initial_length_unchanged_complete_label_evaluations": 208186200,
            "conditional_all_five_initial_length_unchanged_prefix_free_event_evaluations": 55516320,
            "conditional_all_five_categorical_complete_position_scheme": 208204300,
            "http_qualification": "These are conditional next-token-prefix evaluations and equal HTTP calls only for the currently envisaged one-prefix-per-chat-request implementation. Prospective batching could reduce transport calls, not the number of conditional prefix distributions; prefix caching/teacher-forced interfaces need separate source and runtime proof.",
            "canonical20_diagnostic": "Integers1..439 need1..3 digit tokens. Complete position labels must terminate or use another preregistered prefix-free form. The old20-AA 2L+1-call proposal was diagnostic and does not preserve native33 support or the binary position-head type.",
            "wall_clock": "No measured rate for this full adapter exists. Estimate only after synthetic interface/throughput validation: time = prefix-evaluation count / validated aggregate evaluations-per-second, plus oracle time. No new biological forward is needed to check interface throughput.",
            "local_api_spend": 0,
            "base_weights_if_later_authorized_bytes": 2609617413,
            "base_note": "One original HuggingFace ESM1b pytorch_model.bin file, pinned LFS SHA256ebb8a35768179581f91fc01b93cf78facba2821c3bab1452abb38ef2a7f6e7b1. Already acquired five trained heads total23,658,275bytes. No base acquisition performed here.",
        },
        "oracle_and_metrics": {
            "reference_source": "Fixed original learned ESM1b landscape plus author-trained1280->512 Attention1d/MLP decoder for each permitted landscape; not a unique reference sequence and not direct experimental truth.",
            "preprocessing": "MutaPLM source EsmTokenizer(add_special_tokens=True,truncation=True,padding=True,max_length=1024); EsmModel.last_hidden_state; source decoder pools all returned positions without an explicitly supplied padding mask. Preserve batch size4 rather than substituting sequence-by-sequence evaluation.",
            "initial_lengths": "All five starts haveL+2<=441 and initially fit the cutoff. Later exact coverage is conditional on native edits; do not silently claim all future characters are scored.",
            "metrics": "Per seed/round: mean of20 scalar oracle scores and round maximum with cumulative maximum carried across rounds. Across20seeds: mean and source population variance for both trajectories. Report initial oracle value, all values, raw-source variance and separately labeled SD if computed prospectively.",
            "full_five_budget_if_complete": {"independent_runs":100,"rounds_per_run":10,"sampled_cells_per_round":20,"selected_candidates":20000,"initial_values":100,"oracle_scalar_values":20100,"proposal_states":18100,"source_proposal_batch_calls":4600,"source_oracle_batch_calls":5100},
            "comparison_scope": "Five permitted per-landscape curves can be compared descriptively with corresponding paper curves only after protocol/oracle/starting-asset qualifications. The complete six-landscape benchmark remains unexecuted and held; do not average or claim complete-paper ranking.",
        },
        "interpretation_table": [
            {"evaluation":"P34 five permitted landscape optimization","likely_task_demands_provisional":"Sequence/function conditioning, residue-effect priors, proposal calibration and multistep search; learned protein representations may be essential. Classification of demands does not establish an internal reasoning process.","information_supplied":"Full current protein, fixed released function text and objective; no assay labels or fitness feedback.","reference_answer_source":"Author-trained fixed ESM1b landscape predictions, scored after selection.","good_score_establishes":"Higher predicted fitness under the frozen proxy, sampler and declared candidate/oracle budget for these five starts.","good_score_does_not_establish":"Experimental improvement, mechanistic explanation correctness, memorization absence, reasoning suitability, or a full-six paper ranking.","bad_score_establishes":"Lower proxy-scored performance for this declared adapter/search condition; could reflect sequence representations, calibration, interface semantics or search interactions and does not by itself prove inability to reason biologically."},
        ],
        "remaining_blockers_or_decisions": [
            "Resolve paper Algorithm1 versus released source math and native support/invalid-cell behavior before claiming a native protocol.",
            "Approve and freeze a precise Qwen likelihood replacement-head interface; no variant, mask or calibration choice may be selected after task outcomes.",
            "Expanded fixed-ID and assistant-prefill runtime remain unprobed; exact actual request budget is candidate-dependent under native edits.",
            "The original2.61GB ESM1b encoder is metadata-only; acquisition and exact decoder/base restoration require later authorization and verification.",
            "Starting files and five heads are publisher PEX assets with pinned receipts; exact identity to every historical MutaPLM paper starting artifact remains source-qualified.",
            "The sixth landscape remains held and cannot be counted as completed or rerouted.",
        ],
        "per_landscape_sizing_and_conditional_budgets": rows,
        "source_hashes": {path:sha(path) for path in sources},
    }
    OUT.with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n")
    lines = [
        "# P34: five-landscape source-only feasibility review", "",
        "A Qwen replacement-head baseline is scientifically possible; absence of a trained joint head is not grounds to drop this prediction task. It is not activation-ready or established as an exact paper replication. No forward pass, generation, sampler, training, base download, or existing frozen-file edit occurred.", "",
        "Allowed scope: **AMIE, avGFP, E4B, LGK, UBE2I**. The sixth landscape stays held. Five-landscape results cannot stand in for the complete paper setting.", "",
        "The [released head](https://github.com/PharMolix/MutaPLM/blob/495815b2069419d19d9449a59070d0fb24b596d1/model/modeling_esm.py#L1358-L1373) returns a per-position binary mutation probability at temperature0.5 times a33-class AA softmax at0.5. It masks BOS/EOS/padding positions before returning. It has neither a global position normalization nor a WT/AA20 filter.", "",
        "The [released optimizer](https://github.com/PharMolix/MutaPLM/blob/495815b2069419d19d9449a59070d0fb24b596d1/evaluator.py#L190-L323) adds the previous selected weight to every next-grid cell, then samples20 flattened cells without replacement. This revives previously masked positions from round2. Native Python string editing uses token positions as character offsets; special strings and position0 can change length. These are source properties, not failures observed in this audit. Repairing them changes the condition.", "",
        "The [paper Algorithm1](https://arxiv.org/html/2410.22949v1#A3.SS4) instead describes summed head scores and a global softmax. LGK goal wording also differs. The paper's SD wording does not match released population-variance outputs. Select and disclose one protocol target prospectively; neither a silent repair nor a claim that both are identical is valid.", "",
        "A concrete source-shaped adapter would ask a fixed binary likelihood question at each native token position and obtain all33 conditional class likelihoods, apply the two temperature0.5 normalizations, then return the exact-shaped product grid. Preserve the original prior, flattening, RNG, sampling, string edits, batch size4 and trained oracle. A categorical position×residue factorization is another valid declared baseline, but changes native position-mass calibration. Keep all33 classes and no outcome-based retries or repairs. No prompt or protocol was frozen here.", "",
        "For a complete run, each landscape uses20seeds×10rounds×20selected cells,3,620 proposal states,920 source proposal batches,1,020 oracle batches and4,020 oracle scalar values. Across five:18,100 states,4,600 proposal batches,5,100 oracle batches and20,100 scalar values. The oracle does not feed selection. These complete-run counts do not guarantee source code will finish after malformed edits.", "",
        "| Landscape | Start residues | Full start/function/goal tokens¹ | Oracle tokens initially | 33-class complete-label prefix evaluations² | Prefix-free label-event evaluations² |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        counts=row["conditional_if_all_states_keep_initial_length"]
        lines.append(f"| {row['landscape']} | {row['sequence_characters']} | {row['illustrative_named_fields_tokens']} | {row['oracle_initial_special_inclusive_residue_tokens']} | {counts['all_20_seeds_prefix_evaluations']:,} | {counts['all_20_seeds_prefix_free_event_evaluations']:,} |")
    lines.extend([
        "", "¹ Pinned local Qwen tokenizer only; illustrative named fields, before chat/task/prefix overhead. Full current sequences cannot silently be cropped. Later native edits may greatly increase length.",
        "", "² Conditional on every state retaining its starting length. Binary+33 complete-newline labels requires45 evaluations per actual unmasked position; the separately defined prefix-free class event requires12. Totals are208,186,200 or55,516,320 respectively. These equal HTTP calls only with one prefix per request; batching changes transport count. Actual counts depend on native candidate lengths. Neither interface has a full runtime proof. Decimal positions are multi-token; all33 support and prefix behavior were checked with tokenizer metadata only.",
        "", "Use the exact original ESM1b encoder and five existing trained decoder heads, including the source1024-token cutoff, special tokens and batching. The five starts initially fit; future native edits may not. The2,609,617,413-byte encoder remains metadata-only. Learned weights must be restored and audited before any later forward. Unused raw valid.json rows are not scientifically required by the optimizer and must not be exposed to Qwen through generic loader logging.",
        "", "| Evaluation | Likely demands (provisional) | Information supplied | Reference source | What scores establish |",
        "|---|---|---|---|---|",
        "| Five permitted P34 landscapes | Sequence/function conditioning, residue-effect priors, calibration and multistep search; learned representations may matter | Current full sequence, fixed function and objective; no assay data or oracle feedback | Fixed author-trained ESM1b proxy | High: stronger proxy-scored candidates under the frozen search budget. Low: weaker performance for this adapter/search. Neither validates a rationale, experimental improvement, memorization absence or an internal computation. |",
        "", "Before activation: resolve paper/source target; freeze the full likelihood-head contract and failure handling; prove the extended fixed-ID/assistant-prefill interface with synthetic strings; verify source-tensor equivalence using nonbiological fixtures; audit the original oracle restoration and approve resource cost. Do not add candidate filters, deduplicate, substitute an encoder/head, or use post-outcome calibration.",
        "", "The JSON records complete math, indexing, hashes, source-qualified starting-asset provenance, all per-landscape counts and explicit blockers. Existing results remain untouched.",
    ])
    OUT.with_suffix(".md").write_text("\n".join(lines) + "\n")
    for suffix in [".json", ".md"]:
        path=OUT.with_suffix(suffix)
        print(path.relative_to(ROOT), hashlib.sha256(path.read_bytes()).hexdigest(), len(path.read_bytes()))


if __name__ == "__main__":
    main()
