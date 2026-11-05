# LiveProteinBench: Luna’s review of Luna versus Qwen 4B epoch 5

**[Inspect the 30 Qwen answers with sequence-reading flags](qwen_sequence_reading_mismatches_30_20261105.md)**

## What was tested

This page shows a saved diagnostic study of **50 solution pairs**. The 50 were randomly sampled, using seed 42, from **653 questions on which the frozen benchmark scoring marked Luna correct and Qwen 4B epoch 5 wrong**. This selection deliberately focuses on a subset favoring Luna; it is not a representative sample of the benchmark or of every Qwen model.

GPT-6 Luna judged the two saved solutions with model names masked. It saw cached biological evidence, but the answer key was omitted. It rated the knowledge demonstrated in each visible solution and the reasoning expressed in it, each on a 0–2 scale. The sample selection used the frozen V3 benchmark choices. All 50 pairs received valid two-axis ratings.

## What Luna’s judgment found

| Judge's axis | Luna mean, 0–2 | Qwen mean, 0–2 | Luna higher | Tie | Qwen higher |
|---|---:|---:|---:|---:|---:|
| Demonstrated biological knowledge | 1.72 | 0.12 | 50/50 (100%) | 0 | 0 |
| Reasoning in the saved solution | 1.76 | 0.08 | 48/50 (96%) | 1/50 (2%) | 1/50 (2%) |

The judge’s explanations often point to questionable biological identifications or unsupported links between a claimed premise and an answer in the Qwen solution. The individual cases below show what the judge actually said, including [the case where Qwen received the higher reasoning score](cases/active_site_0087.md) and [the reasoning tie](cases/temperature_0038.md).

## How to interpret this comparison

- **Selected sample:** all 50 were drawn from cases scored Luna-correct and Qwen-wrong, so these percentages do not estimate either model’s full-benchmark performance or the frequency of these errors in general.
- **Luna judged its own solutions:** the labels were masked, but model writing style and the difference in available text could remain recognizable. Another judge or an expert may disagree.
- **Different saved text:** Qwen’s saved thinking and final answer were available; for Luna, the judge saw its visible explanation and final answer. Luna’s private provider reasoning was unavailable.
- **What the scores mean:** they describe the judge’s assessment of displayed text. They do not establish what knowledge either model contains, what caused its answer, or whether hidden reasoning faithfully produced it.
- **Evidence:** the judge saw cached evidence, which may be incomplete. Each case links to an existing published question-and-evidence page. The saved evidence IDs shown below refer to the judge’s original packet; they should not be assumed to map to identically numbered IDs on that earlier page.

## All 50 case reviews

Open a case to read the original saved answers, the complete Qwen thinking shown to the judge, and all four saved judge explanations. Qwen’s thinking is collapsed on each case page. Luna’s private provider reasoning was unavailable.

**Knowledge and reasoning can overlap.** Incorrect biological knowledge can lead an answer astray and affect the reasoning built on it. The judge was instructed to assess reasoning from stated premises separately from the truth of those premises, but these ratings are subjective and may not succeed in separating those effects. A false premise can still support a logically coherent argument; the two scores do not establish independent causes of an error.

| Case | Luna knowledge | Qwen knowledge | Luna reasoning | Qwen reasoning |
|---|---:|---:|---:|---:|
| [GO_biological_process_0098](cases/GO_biological_process_0098.md) | 2 | 0 | 2 | 0 |
| [EC_number_0088](cases/EC_number_0088.md) | 2 | 0 | 2 | 0 |
| [GO_molecular_function_0134](cases/GO_molecular_function_0134.md) | 2 | 0 | 2 | 0 |
| [GO_molecular_function_0063](cases/GO_molecular_function_0063.md) | 2 | 0 | 2 | 0 |
| [GO_molecular_function_0003](cases/GO_molecular_function_0003.md) | 1 | 0 | 2 | 0 |
| [GO_biological_process_0168](cases/GO_biological_process_0168.md) | 1 | 0 | 1 | 0 |
| [GO_biological_process_0074](cases/GO_biological_process_0074.md) | 2 | 0 | 1 | 0 |
| [motif_position_0037](cases/motif_position_0037.md) | 2 | 1 | 2 | 0 |
| [GO_biological_process_0048](cases/GO_biological_process_0048.md) | 2 | 0 | 2 | 0 |
| [ph_0007](cases/ph_0007.md) | 1 | 0 | 1 | 0 |
| [catalytic_activity_0122](cases/catalytic_activity_0122.md) | 2 | 0 | 2 | 0 |
| [EC_number_0101](cases/EC_number_0101.md) | 1 | 0 | 2 | 0 |
| [EC_number_0099](cases/EC_number_0099.md) | 2 | 0 | 2 | 0 |
| [GO_biological_process_0057](cases/GO_biological_process_0057.md) | 2 | 0 | 2 | 0 |
| [GO_cellular_component_0189](cases/GO_cellular_component_0189.md) | 1 | 0 | 2 | 0 |
| [GO_molecular_function_0026](cases/GO_molecular_function_0026.md) | 2 | 0 | 2 | 0 |
| [cofactor_0121](cases/cofactor_0121.md) | 2 | 0 | 2 | 0 |
| [temperature_0024](cases/temperature_0024.md) | 2 | 0 | 2 | 0 |
| [EC_number_0091](cases/EC_number_0091.md) | 1 | 0 | 1 | 0 |
| [pathway_0063](cases/pathway_0063.md) | 1 | 0 | 1 | 0 |
| [GO_cellular_component_0138](cases/GO_cellular_component_0138.md) | 2 | 0 | 2 | 0 |
| [catalytic_activity_0117](cases/catalytic_activity_0117.md) | 2 | 0 | 2 | 0 |
| [GO_cellular_component_0192](cases/GO_cellular_component_0192.md) | 2 | 0 | 2 | 0 |
| [catalytic_activity_0179](cases/catalytic_activity_0179.md) | 2 | 0 | 2 | 0 |
| [ph_0006](cases/ph_0006.md) | 1 | 0 | 2 | 0 |
| [GO_molecular_function_0138](cases/GO_molecular_function_0138.md) | 2 | 0 | 2 | 0 |
| [EC_number_0018](cases/EC_number_0018.md) | 2 | 0 | 2 | 0 |
| [GO_cellular_component_0025](cases/GO_cellular_component_0025.md) | 2 | 1 | 2 | 0 |
| [active_site_0100](cases/active_site_0100.md) | 2 | 0 | 2 | 0 |
| [GO_cellular_component_0020](cases/GO_cellular_component_0020.md) | 2 | 0 | 2 | 0 |
| [GO_cellular_component_0182](cases/GO_cellular_component_0182.md) | 2 | 0 | 2 | 0 |
| [active_site_0087](cases/active_site_0087.md) | 1 | 0 | 0 | 1 |
| [GO_biological_process_0056](cases/GO_biological_process_0056.md) | 2 | 0 | 2 | 0 |
| [catalytic_activity_0047](cases/catalytic_activity_0047.md) | 2 | 1 | 2 | 0 |
| [GO_biological_process_0063](cases/GO_biological_process_0063.md) | 1 | 0 | 1 | 0 |
| [catalytic_activity_0001](cases/catalytic_activity_0001.md) | 2 | 0 | 2 | 0 |
| [active_site_0113](cases/active_site_0113.md) | 2 | 0 | 2 | 0 |
| [temperature_0038](cases/temperature_0038.md) | 1 | 0 | 1 | 1 |
| [GO_molecular_function_0106](cases/GO_molecular_function_0106.md) | 1 | 0 | 1 | 0 |
| [EC_number_0132](cases/EC_number_0132.md) | 2 | 0 | 2 | 0 |
| [cofactor_0013](cases/cofactor_0013.md) | 2 | 0 | 2 | 0 |
| [motif_position_0009](cases/motif_position_0009.md) | 2 | 0 | 2 | 0 |
| [GO_biological_process_0129](cases/GO_biological_process_0129.md) | 1 | 0 | 1 | 0 |
| [catalytic_activity_0042](cases/catalytic_activity_0042.md) | 2 | 0 | 2 | 0 |
| [GO_biological_process_0021](cases/GO_biological_process_0021.md) | 2 | 0 | 2 | 0 |
| [pathway_0010](cases/pathway_0010.md) | 1 | 0 | 1 | 0 |
| [GO_molecular_function_0173](cases/GO_molecular_function_0173.md) | 2 | 0 | 2 | 0 |
| [transmembrane_0104](cases/transmembrane_0104.md) | 2 | 1 | 2 | 1 |
| [transmembrane_0059](cases/transmembrane_0059.md) | 2 | 1 | 2 | 1 |
| [catalytic_activity_0006](cases/catalytic_activity_0006.md) | 2 | 1 | 2 | 0 |
