# GO_biological_process_0107

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — peroxisome organization

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSNSPPSSSSSGKGLSIPRKLALNAINEIQNRSNDYLLSKRGGKGLEEGRKRAALAAVISTVSSVGADRLTKADFDELRDLSEQESHDKVHFMDKLTNKLLDAIPRRSDESMDELRKRLEDRHRVEQPGLSIKRISRNFKTLSSKMDLVFSLQYSIIHVISWDKPSLTLTFLILYTWGCLMPYLFLVYPVFYVLTGVLIPNYLYRHPLAKPDIIPTRARGDSSIFGFLRTENAWELDRQRILLERSRTLERILSQELELSTISSRTSTDSEDEGSSSLFYEVFTADSKSNLVFKAVLEEDEETTEKGRTGVVDKVKLLINMRDLQNLTSDIIKMMTRMQDSIYENYSFKDEKRSTKHFFNLIALILITIVLGPYIPWRAIFIITVWVLILLKHPNRQHILKQLKPATKHKLPPKHRTEVKRRASRLGELIVDDPPQYRTIQIYQIEKQDLIKPSVYELYMYSSSIFNESDTLRIQKKDPRGLPISHWCKLPAQAGNSRKRIGQWTPIRDPGASKTVSWMRWRLTESGHMTSPASIVVAVLCVRLSDTAGHQKSDRGSTMIPEPVRRKAV

[Multiple Choices]
A. peroxisome organization
B. intracellular calcium ion homeostasis
C. regulation of transcription by RNA polymerase II
D. positive regulation of transcription by RNA polymerase II
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the record for PEX24. Its function annotation, marked with experimental evidence, says it contributes to peroxisome tethering to the ER for organelle biogenesis, positioning, and segregation; this supports peroxisome organization. The separate GO annotation is computationally inferred (IEA), not itself experimental.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic segments, consistent with a membrane protein, but that does not identify a peroxisomal role or distinguish peroxisome organization from calcium homeostasis.


**Missing item-specific fact**

> The protein-specific fact that this sequence is PEX24 and contributes to peroxisome tethering and biogenesis is absent from the input.


**Reason**

> The key is supported by reviewer-only, sequence-matched functional evidence, but the sequence and choices alone do not provide a meaningful basis for selecting the specific peroxisome process.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence alone does not distinguish the choices reliably, but the available sequence-matched functional evidence supports A; it does not provide comparable support for another listed option.


### Important caveats

- The functional annotation cites experimental evidence, but the primary paper was not independently retrieved or validated here.
- The GO:0007031 annotation is recorded as IEA:UniProtKB-ARBA, a computational annotation.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic segments, consistent with a membrane protein, but that does not identify a peroxisomal role or distinguish peroxisome organization from calcium homeostasis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is PEX24 and contributes to peroxisome tethering and biogenesis is absent from the input.",
    "reason": "The key is supported by reviewer-only, sequence-matched functional evidence, but the sequence and choices alone do not provide a meaningful basis for selecting the specific peroxisome process."
  },
  "case_id": "GO_biological_process_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the record for PEX24. Its function annotation, marked with experimental evidence, says it contributes to peroxisome tethering to the ER for organelle biogenesis, positioning, and segregation; this supports peroxisome organization. The separate GO annotation is computationally inferred (IEA), not itself experimental."
  },
  "important_caveats": [
    "The functional annotation cites experimental evidence, but the primary paper was not independently retrieved or validated here.",
    "The GO:0007031 annotation is recorded as IEA:UniProtKB-ARBA, a computational annotation.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not distinguish the choices reliably, but the available sequence-matched functional evidence supports A; it does not provide comparable support for another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the record for PEX24. Its function annotation, marked with experimental evidence, says it contributes to peroxisome tethering to the ER for organelle biogenesis, positioning, and segregation; this supports peroxisome organization. The separate GO annotation is computationally inferred (IEA), not itself experimental.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic segments, consistent with a membrane protein, but that does not identify a peroxisomal role or distinguish peroxisome organization from calcium homeostasis.",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is PEX24 and contributes to peroxisome tethering and biogenesis is absent from the input.",
    "reason": "The key is supported by reviewer-only, sequence-matched functional evidence, but the sequence and choices alone do not provide a meaningful basis for selecting the specific peroxisome process."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not distinguish the choices reliably, but the available sequence-matched functional evidence supports A; it does not provide comparable support for another listed option."
  },
  "important_caveats": [
    "The functional annotation cites experimental evidence, but the primary paper was not independently retrieved or validated here.",
    "The GO:0007031 annotation is recorded as IEA:UniProtKB-ARBA, a computational annotation.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is PEX24 (UniProt W1QDU5), a peroxisomal membrane protein. The experimental function annotation (ECO:0000269, PubMed:32665322) states it 'contributes to tethering of peroxisomes to the endoplasmic reticulum for organelle biogenesis, positioning and segregation.' The GO annotation GO:0007031 (peroxisome organization) is present in the entry (though tagged IEA:UniProtKB-ARBA), and the underlying experimental evidence from Wu et al. 2020 directly supports a role in peroxisome organization. The GO term definition ('assembly, arrangement of constituent parts, or disassembly of a peroxisome') matches the protein's demonstrated function in peroxisome biogenesis, positioning, and segregation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can partially eliminate distractors: the sequence lacks canonical DNA-binding domains (zinc fingers, bZIP, helix-turn-helix) making transcription regulation (C, D) unlikely, and lacks EF-hand or other calcium-binding motifs making calcium homeostasis (B) unlikely. However, positively identifying 'peroxisome organization' requires recognizing the protein as a peroxisomal membrane protein (PEX24). The sequence contains transmembrane-like hydrophobic stretches and coiled-coil regions, but these features are shared across many membrane proteins (mitochondrial, ER, vesicular) and do not uniquely indicate peroxisomal membrane targeting. No well-defined peroxisomal membrane targeting signal (mPTS) is recognizable as a simple sequence motif.


**Missing item-specific fact**

> The specific identity of the protein as PEX24 (or recognition of its domain architecture as belonging to the peroxisome biogenesis machinery) is needed to positively assign 'peroxisome organization' rather than other membrane-protein-associated processes. This requires either database lookup of the sequence or memorization of PEX24's function.


**Reason**

> While elimination of B, C, D is partially feasible through absence of characteristic motifs, confirming A specifically requires knowing this is a peroxisomal membrane protein involved in peroxisome biogenesis. The sequence features (hydrophobic TM regions, coiled coils) are generic to many membrane proteins and do not uniquely point to peroxisomes without prior knowledge of PEX24 or training on similar peroxisomal membrane proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A (peroxisome organization) is consistent with the protein's experimentally validated function. Options B, C, and D have no supporting evidence and are inconsistent with the protein's domain architecture. No ambiguity in the correct answer.


### Important caveats

- The GO:0007031 annotation carries evidence code IEA:UniProtKB-ARBA (automatic rule-based), but the underlying FUNCTION comment is supported by experimental evidence (ECO:0000269, PubMed:32665322, Wu et al. 2020).
- The protein is from Ogataea parapolymorpha (methylotrophic yeast), a non-model organism; PEX24 was characterized relatively recently (2020 publication, 2025 UniProt integration).
- The sequence-match is confirmed (SHA256 identical between benchmark and UniProt entries), so the annotation applies to the exact sequence provided.
- The protein lacks canonical peroxisomal matrix targeting signals (PTS1/PTS2), consistent with its role as a membrane protein rather than a matrix enzyme.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can partially eliminate distractors: the sequence lacks canonical DNA-binding domains (zinc fingers, bZIP, helix-turn-helix) making transcription regulation (C, D) unlikely, and lacks EF-hand or other calcium-binding motifs making calcium homeostasis (B) unlikely. However, positively identifying 'peroxisome organization' requires recognizing the protein as a peroxisomal membrane protein (PEX24). The sequence contains transmembrane-like hydrophobic stretches and coiled-coil regions, but these features are shared across many membrane proteins (mitochondrial, ER, vesicular) and do not uniquely indicate peroxisomal membrane targeting. No well-defined peroxisomal membrane targeting signal (mPTS) is recognizable as a simple sequence motif.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of the protein as PEX24 (or recognition of its domain architecture as belonging to the peroxisome biogenesis machinery) is needed to positively assign 'peroxisome organization' rather than other membrane-protein-associated processes. This requires either database lookup of the sequence or memorization of PEX24's function.",
    "reason": "While elimination of B, C, D is partially feasible through absence of characteristic motifs, confirming A specifically requires knowing this is a peroxisomal membrane protein involved in peroxisome biogenesis. The sequence features (hydrophobic TM regions, coiled coils) are generic to many membrane proteins and do not uniquely point to peroxisomes without prior knowledge of PEX24 or training on similar peroxisomal membrane proteins."
  },
  "case_id": "GO_biological_process_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The protein is PEX24 (UniProt W1QDU5), a peroxisomal membrane protein. The experimental function annotation (ECO:0000269, PubMed:32665322) states it 'contributes to tethering of peroxisomes to the endoplasmic reticulum for organelle biogenesis, positioning and segregation.' The GO annotation GO:0007031 (peroxisome organization) is present in the entry (though tagged IEA:UniProtKB-ARBA), and the underlying experimental evidence from Wu et al. 2020 directly supports a role in peroxisome organization. The GO term definition ('assembly, arrangement of constituent parts, or disassembly of a peroxisome') matches the protein's demonstrated function in peroxisome biogenesis, positioning, and segregation."
  },
  "important_caveats": [
    "The GO:0007031 annotation carries evidence code IEA:UniProtKB-ARBA (automatic rule-based), but the underlying FUNCTION comment is supported by experimental evidence (ECO:0000269, PubMed:32665322, Wu et al. 2020).",
    "The protein is from Ogataea parapolymorpha (methylotrophic yeast), a non-model organism; PEX24 was characterized relatively recently (2020 publication, 2025 UniProt integration).",
    "The sequence-match is confirmed (SHA256 identical between benchmark and UniProt entries), so the annotation applies to the exact sequence provided.",
    "The protein lacks canonical peroxisomal matrix targeting signals (PTS1/PTS2), consistent with its role as a membrane protein rather than a matrix enzyme."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A (peroxisome organization) is consistent with the protein's experimentally validated function. Options B, C, and D have no supporting evidence and are inconsistent with the protein's domain architecture. No ambiguity in the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is PEX24 (UniProt W1QDU5), a peroxisomal membrane protein. The experimental function annotation (ECO:0000269, PubMed:32665322) states it 'contributes to tethering of peroxisomes to the endoplasmic reticulum for organelle biogenesis, positioning and segregation.' The GO annotation GO:0007031 (peroxisome organization) is present in the entry (though tagged IEA:UniProtKB-ARBA), and the underlying experimental evidence from Wu et al. 2020 directly supports a role in peroxisome organization. The GO term definition ('assembly, arrangement of constituent parts, or disassembly of a peroxisome') matches the protein's demonstrated function in peroxisome biogenesis, positioning, and segregation.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can partially eliminate distractors: the sequence lacks canonical DNA-binding domains (zinc fingers, bZIP, helix-turn-helix) making transcription regulation (C, D) unlikely, and lacks EF-hand or other calcium-binding motifs making calcium homeostasis (B) unlikely. However, positively identifying 'peroxisome organization' requires recognizing the protein as a peroxisomal membrane protein (PEX24). The sequence contains transmembrane-like hydrophobic stretches and coiled-coil regions, but these features are shared across many membrane proteins (mitochondrial, ER, vesicular) and do not uniquely indicate peroxisomal membrane targeting. No well-defined peroxisomal membrane targeting signal (mPTS) is recognizable as a simple sequence motif.",
    "missing_item_specific_fact": "The specific identity of the protein as PEX24 (or recognition of its domain architecture as belonging to the peroxisome biogenesis machinery) is needed to positively assign 'peroxisome organization' rather than other membrane-protein-associated processes. This requires either database lookup of the sequence or memorization of PEX24's function.",
    "reason": "While elimination of B, C, D is partially feasible through absence of characteristic motifs, confirming A specifically requires knowing this is a peroxisomal membrane protein involved in peroxisome biogenesis. The sequence features (hydrophobic TM regions, coiled coils) are generic to many membrane proteins and do not uniquely point to peroxisomes without prior knowledge of PEX24 or training on similar peroxisomal membrane proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A (peroxisome organization) is consistent with the protein's experimentally validated function. Options B, C, and D have no supporting evidence and are inconsistent with the protein's domain architecture. No ambiguity in the correct answer."
  },
  "important_caveats": [
    "The GO:0007031 annotation carries evidence code IEA:UniProtKB-ARBA (automatic rule-based), but the underlying FUNCTION comment is supported by experimental evidence (ECO:0000269, PubMed:32665322, Wu et al. 2020).",
    "The protein is from Ogataea parapolymorpha (methylotrophic yeast), a non-model organism; PEX24 was characterized relatively recently (2020 publication, 2025 UniProt integration).",
    "The sequence-match is confirmed (SHA256 identical between benchmark and UniProt entries), so the annotation applies to the exact sequence provided.",
    "The protein lacks canonical peroxisomal matrix targeting signals (PTS1/PTS2), consistent with its role as a membrane protein rather than a matrix enzyme."
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

**Accession:** `W1QDU5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 36. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QDU5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:05.762905+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Peroxin-24"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32665322","source":"PubMed"}],"value":"Peroxisomal membrane protein PEX24"}}}
```

Source SHA-256: `a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QDU5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:05.762905+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32665322","source":"PubMed"}],"value":"With PEX32, contributes to tethering of peroxisomes to the endoplasmic reticulum for organelle biogenesis, positioning and segregation"}]}
```

Source SHA-256: `a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QDU5.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:05.762905+00:00.  

```json
{"database":"GO","id":"GO:0007031","properties":[{"key":"GoTerm","value":"P:peroxisome organization"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-ARBA"}]}
```

Source SHA-256: `a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QDU5?format=txt&versions=36)  
**Locator:** `lines 32-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:34:09.234705+00:00.  

```text
CC   -!- FUNCTION: With PEX32, contributes to tethering of peroxisomes to the
CC       endoplasmic reticulum for organelle biogenesis, positioning and
CC       segregation. {ECO:0000269|PubMed:32665322}.
```

Source SHA-256: `35693919ce4aaade7dbc7068810713aa80e421568f8ede865776b2f733bc2302`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QDU5?format=txt&versions=36)  
**Locator:** `lines 66-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:34:09.234705+00:00.  

```text
DR   GO; GO:0007031; P:peroxisome organization; IEA:UniProtKB-ARBA.
```

Source SHA-256: `35693919ce4aaade7dbc7068810713aa80e421568f8ede865776b2f733bc2302`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 72605-72618`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0007031
name: peroxisome organization
namespace: biological_process
def: "A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of a peroxisome. A peroxisome is a small, membrane-bounded organelle that uses dioxygen (O2) to oxidize organic molecules." [GOC:mah]
subset: goslim_drosophila
subset: goslim_generic
subset: goslim_pir
subset: goslim_pombe
subset: goslim_yeast
synonym: "peroxisome organisation" EXACT []
synonym: "peroxisome organization and biogenesis" RELATED [GOC:mah]
is_a: GO:0006996 ! organelle organization

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
