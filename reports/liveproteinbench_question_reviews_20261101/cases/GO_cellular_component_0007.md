# GO_cellular_component_0007

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGRDARRLPLLPFLLLLLAAAAGVAESATDAEAIHDLARSVPALGWDGDNVCGFEGVTCERGGAGKVTELNLADRGLSGTLPDSLSSLTSLTALQLQGNALTGAVPSLARMGSLARLALDGNAFTSLPPDFLHGLTSLQYLTMENLPLPPWPVPDAIANCSSLDTFSASNASISGPFPAVLATLVSLRNLRLSYNNLTGGLPPELSSLIAMESLQLNNQRSDDKLSGPIDVIASMKSLKLLWIQSNKFTGPIPDLNGTQLEAFNVRDNMLTGVVPPSLTGLMSLKNVSLSNNNFQGPKPAFAAIPGQDEDSGNGFCLNTPGPCSPLTTTLLQVAEGFGYPYELAKTWKGNDPCSPAWVGIVCTSSDVSMINLSRKNLSGRISPALANLTRLARLDLSNNNLTGVIPDVLTTLPSLTVLNVANNRLTGEVPKFKPSVNVLAQGNLFGQSSGSSGGGGGSDGDSSSSDSAGGGKSKPNTGMIIGIIVAVIILFACIALLVHHRKKKNVEKFRPVSTKTSPAESEMMKIQVVGANGISNGSSAFPTELYSHVSAANSSNISELFESHGMQLSVEVLLKATNNFSEDCILGRGGFGVVFKGNLNGKLVAVKRCDSGTMGTKGQEEFLAEIDVLRKVRHRHLVALLGYCTHGNERLLVYEYMSGGTLREHLCDLQQSGFIPLTWTQRMTIALDVARGIEYLHGLAQETFIHRDLKPSNILLDQDLRAKVSDFGLVKLAKDTDKSLMTRIAGTFGYLAPEYATTGKVTTKVDVYAYGVILMEMITGRKVLDDSLPDDETHLVTIFRRNILDKEKFRKFVDPTLELSAEGWTSLLEVADLARHCTAREPYQRPDMCHCVNRLSSLVDQWKPTNIDEDDYEGETSEMGLHQQLEKWRCDDFTISDSDTFGSFNVPRKYNG

[Multiple Choices]
A. microtubule
B. plasma membrane
C. Dbf4-dependent protein kinase complex
D. matrilin complex
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

* Protein Sequence: The amino acid sequence of the protein.
* Multiple Choices: Candidate answers for the protein-related question.

Please think step-by-step about this problem:
1. Analyze the protein sequence carefully.
2. Consider the biological context and function.
3. Evaluate each multiple-choice option.
4. Provide your reasoning process.
5. Finally, give your answer.

Provide your response in the following format:
1. reasoning: [Your detailed reasoning here]
2. answer: Your final answer, which should be "A", "B", "C" or "D".
```

</details>

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates the protein to the cell membrane and plasma membrane; the plasma-membrane GO annotation has experimental evidence (IDA).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal signal peptide, a long extracellular repeat-rich region, a single transmembrane segment, and a cytosolic protein-kinase domain. This is characteristic of a single-pass receptor protein and strongly favors plasma membrane over the listed microtubule, kinase-complex, and matrilin-complex choices.


**Missing item-specific fact**

> No protein-specific annotation is essential to distinguish these choices, although sequence topology alone cannot establish the exact membrane destination as conclusively as localization data can.


**Reason**

> The sequence provides a concrete receptor topology that meaningfully favors plasma membrane among the options. The reviewer-only experimental annotation corroborates the key but is not needed as input for that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, plasma membrane is strongly favored by the sequence's secretory signal, single-pass membrane anchor, and intracellular kinase domain.


### Important caveats

- Experimental support in the retrieved record is sequence-matched, but the author's exact source snapshot is unknown.
- Sequence topology supports plasma-membrane targeting but does not by itself exclude localization to other cellular membranes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal signal peptide, a long extracellular repeat-rich region, a single transmembrane segment, and a cytosolic protein-kinase domain. This is characteristic of a single-pass receptor protein and strongly favors plasma membrane over the listed microtubule, kinase-complex, and matrilin-complex choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is essential to distinguish these choices, although sequence topology alone cannot establish the exact membrane destination as conclusively as localization data can.",
    "reason": "The sequence provides a concrete receptor topology that meaningfully favors plasma membrane among the options. The reviewer-only experimental annotation corroborates the key but is not needed as input for that distinction."
  },
  "case_id": "GO_cellular_component_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the cell membrane and plasma membrane; the plasma-membrane GO annotation has experimental evidence (IDA)."
  },
  "important_caveats": [
    "Experimental support in the retrieved record is sequence-matched, but the author's exact source snapshot is unknown.",
    "Sequence topology supports plasma-membrane targeting but does not by itself exclude localization to other cellular membranes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, plasma membrane is strongly favored by the sequence's secretory signal, single-pass membrane anchor, and intracellular kinase domain."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the cell membrane and plasma membrane; the plasma-membrane GO annotation has experimental evidence (IDA).",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal signal peptide, a long extracellular repeat-rich region, a single transmembrane segment, and a cytosolic protein-kinase domain. This is characteristic of a single-pass receptor protein and strongly favors plasma membrane over the listed microtubule, kinase-complex, and matrilin-complex choices.",
    "missing_item_specific_fact": "No protein-specific annotation is essential to distinguish these choices, although sequence topology alone cannot establish the exact membrane destination as conclusively as localization data can.",
    "reason": "The sequence provides a concrete receptor topology that meaningfully favors plasma membrane among the options. The reviewer-only experimental annotation corroborates the key but is not needed as input for that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, plasma membrane is strongly favored by the sequence's secretory signal, single-pass membrane anchor, and intracellular kinase domain."
  },
  "important_caveats": [
    "Experimental support in the retrieved record is sequence-matched, but the author's exact source snapshot is unknown.",
    "Sequence topology supports plasma-membrane targeting but does not by itself exclude localization to other cellular membranes."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2R560 (OsWSS1, Receptor protein kinase WSS1) is annotated with GO:0005886 (plasma membrane) via IDA evidence from PubMed:35693165 (C6, H4). The subcellular location comment states 'Cell membrane; Single-pass type I membrane protein' with ECO:0000269 (inferred from direct assay) (C5, H3). GO:0005886 has 'cell membrane' as an EXACT synonym (GO2). The sequence architecture (signal peptide, single TM helix, extracellular LRR domain, intracellular kinase domain) is fully consistent with a single-pass type I membrane receptor kinase at the plasma membrane.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains: (1) an N-terminal signal peptide (MGRDARRLPLLPFLLLLLAAAAGVAESA) indicating entry into the secretory/membrane pathway; (2) a hydrophobic transmembrane segment (MIIGIIVAVIILFACIALLVHHRKKK) with positive-inside residues, consistent with a single-pass type I membrane protein; (3) an extracellular leucine-rich repeat (LRR) domain with multiple LxxLxLxxN motifs; (4) an intracellular serine/threonine kinase domain with canonical HRD, DFG, and activation-loop motifs. This architecture defines a plant receptor-like kinase (RLK), which by definition resides at the plasma membrane. Microtubule (A) requires tubulin-like GTPase folds absent here. Dbf4-dependent kinase complex (C) is a nuclear DNA-replication complex (Cdc7/Dbf4), incompatible with a membrane receptor. Matrilin complex (D) is an animal cartilage ECM trimer, irrelevant to a plant receptor kinase.


**Missing item-specific fact**

> None critical. The signal peptide, TM domain, LRR architecture, kinase motifs, and plant origin are all visible in the supplied sequence and sufficient to eliminate all distractors and select plasma membrane.


**Reason**

> A model can identify the signal peptide, transmembrane helix, extracellular LRR repeats, and intracellular kinase domain directly from the sequence. These features unambiguously indicate a single-pass membrane receptor kinase at the plasma membrane. Each distractor is eliminable by general biology: tubulin lacks LRR/kinase folds (rules out A); Dbf4/DDK is nuclear and not a membrane receptor (rules out C); matrilin is an animal cartilage ECM protein absent in plants (rules out D). No protein-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence architecture (signal peptide + single TM + extracellular LRR + intracellular kinase) is diagnostic of a plasma-membrane receptor-like kinase. All three distractors are clearly incompatible: microtubule requires tubulin, Dbf4 complex is nuclear, and matrilin complex is animal cartilage ECM. Only B is defensible.


### Important caveats

- The UniProt IDA annotation (PubMed:35693165) provides experimental confirmation of plasma membrane localization, strengthening the key beyond pure sequence inference.
- The GO term GO:0005886 'plasma membrane' has 'cell membrane' as an EXACT synonym, so the UniProt 'Cell membrane' annotation maps directly to the option text 'plasma membrane'.
- The protein is from Oryza sativa (rice); the matrilin complex distractor is animal-specific, making it trivially eliminable for any model aware of plant vs. animal biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains: (1) an N-terminal signal peptide (MGRDARRLPLLPFLLLLLAAAAGVAESA) indicating entry into the secretory/membrane pathway; (2) a hydrophobic transmembrane segment (MIIGIIVAVIILFACIALLVHHRKKK) with positive-inside residues, consistent with a single-pass type I membrane protein; (3) an extracellular leucine-rich repeat (LRR) domain with multiple LxxLxLxxN motifs; (4) an intracellular serine/threonine kinase domain with canonical HRD, DFG, and activation-loop motifs. This architecture defines a plant receptor-like kinase (RLK), which by definition resides at the plasma membrane. Microtubule (A) requires tubulin-like GTPase folds absent here. Dbf4-dependent kinase complex (C) is a nuclear DNA-replication complex (Cdc7/Dbf4), incompatible with a membrane receptor. Matrilin complex (D) is an animal cartilage ECM trimer, irrelevant to a plant receptor kinase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The signal peptide, TM domain, LRR architecture, kinase motifs, and plant origin are all visible in the supplied sequence and sufficient to eliminate all distractors and select plasma membrane.",
    "reason": "A model can identify the signal peptide, transmembrane helix, extracellular LRR repeats, and intracellular kinase domain directly from the sequence. These features unambiguously indicate a single-pass membrane receptor kinase at the plasma membrane. Each distractor is eliminable by general biology: tubulin lacks LRR/kinase folds (rules out A); Dbf4/DDK is nuclear and not a membrane receptor (rules out C); matrilin is an animal cartilage ECM protein absent in plants (rules out D). No protein-specific database lookup is required."
  },
  "case_id": "GO_cellular_component_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2R560 (OsWSS1, Receptor protein kinase WSS1) is annotated with GO:0005886 (plasma membrane) via IDA evidence from PubMed:35693165 (C6, H4). The subcellular location comment states 'Cell membrane; Single-pass type I membrane protein' with ECO:0000269 (inferred from direct assay) (C5, H3). GO:0005886 has 'cell membrane' as an EXACT synonym (GO2). The sequence architecture (signal peptide, single TM helix, extracellular LRR domain, intracellular kinase domain) is fully consistent with a single-pass type I membrane receptor kinase at the plasma membrane."
  },
  "important_caveats": [
    "The UniProt IDA annotation (PubMed:35693165) provides experimental confirmation of plasma membrane localization, strengthening the key beyond pure sequence inference.",
    "The GO term GO:0005886 'plasma membrane' has 'cell membrane' as an EXACT synonym, so the UniProt 'Cell membrane' annotation maps directly to the option text 'plasma membrane'.",
    "The protein is from Oryza sativa (rice); the matrilin complex distractor is animal-specific, making it trivially eliminable for any model aware of plant vs. animal biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence architecture (signal peptide + single TM + extracellular LRR + intracellular kinase) is diagnostic of a plasma-membrane receptor-like kinase. All three distractors are clearly incompatible: microtubule requires tubulin, Dbf4 complex is nuclear, and matrilin complex is animal cartilage ECM. Only B is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2R560 (OsWSS1, Receptor protein kinase WSS1) is annotated with GO:0005886 (plasma membrane) via IDA evidence from PubMed:35693165 (C6, H4). The subcellular location comment states 'Cell membrane; Single-pass type I membrane protein' with ECO:0000269 (inferred from direct assay) (C5, H3). GO:0005886 has 'cell membrane' as an EXACT synonym (GO2). The sequence architecture (signal peptide, single TM helix, extracellular LRR domain, intracellular kinase domain) is fully consistent with a single-pass type I membrane receptor kinase at the plasma membrane.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains: (1) an N-terminal signal peptide (MGRDARRLPLLPFLLLLLAAAAGVAESA) indicating entry into the secretory/membrane pathway; (2) a hydrophobic transmembrane segment (MIIGIIVAVIILFACIALLVHHRKKK) with positive-inside residues, consistent with a single-pass type I membrane protein; (3) an extracellular leucine-rich repeat (LRR) domain with multiple LxxLxLxxN motifs; (4) an intracellular serine/threonine kinase domain with canonical HRD, DFG, and activation-loop motifs. This architecture defines a plant receptor-like kinase (RLK), which by definition resides at the plasma membrane. Microtubule (A) requires tubulin-like GTPase folds absent here. Dbf4-dependent kinase complex (C) is a nuclear DNA-replication complex (Cdc7/Dbf4), incompatible with a membrane receptor. Matrilin complex (D) is an animal cartilage ECM trimer, irrelevant to a plant receptor kinase.",
    "missing_item_specific_fact": "None critical. The signal peptide, TM domain, LRR architecture, kinase motifs, and plant origin are all visible in the supplied sequence and sufficient to eliminate all distractors and select plasma membrane.",
    "reason": "A model can identify the signal peptide, transmembrane helix, extracellular LRR repeats, and intracellular kinase domain directly from the sequence. These features unambiguously indicate a single-pass membrane receptor kinase at the plasma membrane. Each distractor is eliminable by general biology: tubulin lacks LRR/kinase folds (rules out A); Dbf4/DDK is nuclear and not a membrane receptor (rules out C); matrilin is an animal cartilage ECM protein absent in plants (rules out D). No protein-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence architecture (signal peptide + single TM + extracellular LRR + intracellular kinase) is diagnostic of a plasma-membrane receptor-like kinase. All three distractors are clearly incompatible: microtubule requires tubulin, Dbf4 complex is nuclear, and matrilin complex is animal cartilage ECM. Only B is defensible."
  },
  "important_caveats": [
    "The UniProt IDA annotation (PubMed:35693165) provides experimental confirmation of plasma membrane localization, strengthening the key beyond pure sequence inference.",
    "The GO term GO:0005886 'plasma membrane' has 'cell membrane' as an EXACT synonym, so the UniProt 'Cell membrane' annotation maps directly to the option text 'plasma membrane'.",
    "The protein is from Oryza sativa (rice); the matrilin complex distractor is animal-specific, making it trivially eliminable for any model aware of plant vs. animal biology."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q2R560` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 23. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35693165","source":"PubMed"}],"value":"Protein WATER-SOAKED SPOT1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"35693165","source":"PubMed"}],"value":"OsWSS1"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P43298","source":"UniProtKB"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Receptor protein kinase WSS1"}}}
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"35693165","source":"PubMed"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9905","value":"Single-pass type I membrane protein"}}]}
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"35693165","source":"PubMed"}],"id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2R560?format=txt&versions=23)  
**Locator:** `lines 99-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-01T06:28:32.565844+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:35693165};
CC       Single-pass type I membrane protein {ECO:0000255}.
```

Source SHA-256: `8a1500792a74c38b22c2f5627966de80a760b1fed597a74e00b3d2510fcaa15a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2R560?format=txt&versions=23)  
**Locator:** `lines 130-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-01T06:28:32.565844+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IDA:UniProtKB.
```

Source SHA-256: `8a1500792a74c38b22c2f5627966de80a760b1fed597a74e00b3d2510fcaa15a`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
