# Heme-complex generation: one qualitative demonstration

Qwen3.8-27B generated one complete sequence. Protenix-mini-ISM v0.5.0 produced all five predicted complexes; every sample is retained.

These are computational structure and confidence observations. There is no measured binding, validated function, accuracy score or native NatureLM replication.

All five predicted complexes contain severe atomic overlaps: their minimum protein–HEM heavy-atom distances range from 0.068 to 0.819 Å. Delivery checks confirm complete, finite coordinate files. The observed overlaps prevent treating these models or their contact counts as evidence of physically plausible binding.

| Sample | Minimum heavy-atom distance (Å) | Contact pairs within 4 Å |
|---|---:|---:|
| P39_GENERATED_SINGLE_sample_0.cif | 0.650 | 427 |
| P39_GENERATED_SINGLE_sample_1.cif | 0.270 | 1002 |
| P39_GENERATED_SINGLE_sample_2.cif | 0.068 | 342 |
| P39_GENERATED_SINGLE_sample_3.cif | 0.716 | 421 |
| P39_GENERATED_SINGLE_sample_4.cif | 0.819 | 405 |

The artificial 512-residue resource gate and two exact-copy delivery checks passed before the single demonstration.

- One newly declared generic heme-binding prompt and one generated outcome; original NatureLM prompt, selected cohort and denominator are unavailable.
- Uses the acquired Proteo-R1 Protenix fork d60af043 and released mini-ISM v0.5.0, five samples/five diffusion steps/seed101, fp32 Torch kernels without MSA/templates; exact NatureLM predictor configuration is unavailable.
- The whole canonical sequence must contain20–512residues; no crop, repair, redesign, selection or retry is permitted. This declared interface is not the original paper sampling condition.
- All five complexes are retained without HemeList, keyword, model-confidence or geometric selection.
- Generation uses a compact JSON regex that preserves every20–512residue canonical sequence while excluding formatting whitespace; this is a prospective delivery adaptation.
- Confidence and heavy-atom proximity are computational observations only. No measured binding, functional validation, accuracy score or native-paper comparison is claimed.

## Complete question and saved sequence

This is the explicitly declared available prompt, rather than an unreleased NatureLM test case.

Design a heme-binding protein sequence.

Return one JSON object with the single key "sequence", containing a complete protein sequence of 20 to 512 residues using only the 20 standard amino-acid letters. Do not return an explanation or claim experimental validation.

```text
MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAANTQVVKNVIHAVRNSGDAATSMNNSGAADFAMGALDDLILPTPSNVRLFVDRFKEVNGDDFAGYLGAAALGKHLARKEVVMDAMKCEQDAPGVTWDDAAYNSNSKLTDNADLAACDYDEDDMQKTEEGILEEGGRLYFELLCYRLEHNHIRELQKELLGKALVGKVLTARTCGKLFVVYAMVQEAKTQKVGQNSVLKCSRYKKMERSFKKDDAGVLLKVLFVMAKGEERFMAEEGKKALVAIVMKTAFAGTVMEGADDWVTDPTLAVYVFNDLPTGRYVTLICYNLEFGRGSGGSDN
```
