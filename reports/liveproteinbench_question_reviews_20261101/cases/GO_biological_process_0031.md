# GO_biological_process_0031

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — saponin biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSAKMLHVVMYPWFAYGHMIPFLHLSNKLAETGHKVTYILPPKALTRLQNLNLNPTQITFRTITVPRVDGLPAGAENVTDIPDITLHTHLATALDRTRPEFETIVELIKPDVIMYDVAYWVPEVAVKYGAKSVAYSVVSAASVSLSKTVVDRMTPLEKPMTEEERKKKFAQYPHLIQLYGPFGEGITMYDRLTGMLSKCDAIACRTCREIEGKYCQYLSTQYEKKVTLTGPVLPEPEVGATLEAPWSEWLSRFKLGSVLFCAFGSQFYLDKDQFQEIILGLEMTNLPFLMAVQPPKGCATIEEAYPEGFAERVKDRGVVTSQWVQQLVILAHPAVGCFVNHCAFGTMWEALLSEKQLVMIPQLGDQILNTKMLADELKVGVEVERGIGGWVSKENLCKAIKSVMDEDSEIGKDVKQSHEKWRATLSSKDLMSTYIDSFIKDLQALVE

[Multiple Choices]
A. regulation of leaf senescence
B. response to misfolded protein
C. saponin biosynthetic process
D. regulation of Rab protein signal transduction
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

> The exact sequence matches a UniProt record annotated with saponin biosynthetic process (GO:0016135, IDA); the record also describes an experimentally supported role as a glycosyltransferase in the saponin pathway. The matched historical record contains the same GO annotation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with an enzyme, but the supplied sequence and choices do not reveal its specific substrate or pathway. General sequence reasoning does not distinguish saponin biosynthesis from the other listed processes with confidence.


**Missing item-specific fact**

> The protein's characterized function as a glycosyltransferase acting in the saponin biosynthetic pathway, or an equivalent protein-specific annotation.


**Reason**

> Choosing C depends on knowing the protein-specific pathway role, which is absent from the input. Recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone does not discriminate the choices, but the matched protein-specific evidence supports C; no evidence supplied supports another option as an equally defensible process.


### Important caveats

- The reviewer-only source records match the input sequence, but the author's exact source snapshot is unknown.
- The GO annotation is marked IDA and cites a publication; this supports the key but is not independent validation performed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with an enzyme, but the supplied sequence and choices do not reveal its specific substrate or pathway. General sequence reasoning does not distinguish saponin biosynthesis from the other listed processes with confidence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's characterized function as a glycosyltransferase acting in the saponin biosynthetic pathway, or an equivalent protein-specific annotation.",
    "reason": "Choosing C depends on knowing the protein-specific pathway role, which is absent from the input. Recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "case_id": "GO_biological_process_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated with saponin biosynthetic process (GO:0016135, IDA); the record also describes an experimentally supported role as a glycosyltransferase in the saponin pathway. The matched historical record contains the same GO annotation."
  },
  "important_caveats": [
    "The reviewer-only source records match the input sequence, but the author's exact source snapshot is unknown.",
    "The GO annotation is marked IDA and cites a publication; this supports the key but is not independent validation performed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not discriminate the choices, but the matched protein-specific evidence supports C; no evidence supplied supports another option as an equally defensible process."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated with saponin biosynthetic process (GO:0016135, IDA); the record also describes an experimentally supported role as a glycosyltransferase in the saponin pathway. The matched historical record contains the same GO annotation.",
    "evidence_ids": ["C1", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with an enzyme, but the supplied sequence and choices do not reveal its specific substrate or pathway. General sequence reasoning does not distinguish saponin biosynthesis from the other listed processes with confidence.",
    "missing_item_specific_fact": "The protein's characterized function as a glycosyltransferase acting in the saponin biosynthetic pathway, or an equivalent protein-specific annotation.",
    "reason": "Choosing C depends on knowing the protein-specific pathway role, which is absent from the input. Recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not discriminate the choices, but the matched protein-specific evidence supports C; no evidence supplied supports another option as an equally defensible process."
  },
  "important_caveats": [
    "The reviewer-only source records match the input sequence, but the author's exact source snapshot is unknown.",
    "The GO annotation is marked IDA and cites a publication; this supports the key but is not independent validation performed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1IQ05 (GT791_SAPOF, SoUGT79T1) is annotated with GO:0016135 'saponin biosynthetic process' via IDA (Inferred from Direct Assay) based on experimental evidence from PubMed:39043959 (Nat. Chem. Biol. 2025). The FUNCTION comment explicitly states it is 'Component of the oleanane-type triterpene saponins biosynthetic pathway' and describes its glycosyltransferase activity on a saponin precursor (QA-triF to QA-triFR). The sequence SHA256 matches exactly. The annotation is experimentally derived, not computational inference.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [H1](#evidence-h1), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains features consistent with a plant UDP-glycosyltransferase (UGT family, PSPG motif region in the C-terminal half). A glycosyltransferase catalyzes the transfer of sugar moieties to acceptor molecules — a biosynthetic/conjugation enzymatic activity. Among the four options, only C ('saponin biosynthetic process') describes a biosynthetic/metabolic process in which a glycosyltransferase would directly participate. Options A ('regulation of leaf senescence'), B ('response to misfolded protein'), and D ('regulation of Rab protein signal transduction') are regulatory, stress-response, or signaling processes that do not naturally involve a glycosyltransferase as a primary functional participant. Thus, identifying the protein as an enzyme (specifically a glycosyltransferase) and applying general biological reasoning that enzymes catalyze biosynthetic reactions rather than 'regulate' or 'respond to' processes allows elimination of A, B, and D, leaving C as the only consistent option.


**Missing item-specific fact**

> The specific substrate identity (oleanane-type triterpene saponin precursor QA-triF) cannot be determined from sequence alone. However, since 'saponin biosynthetic process' is the only biosynthetic option among the four, the elimination-based reasoning path does not require knowing the exact substrate.


**Reason**

> The reasoning path requires (1) recognizing the protein as a glycosyltransferase from conserved domain features (PSPG motif), which is a standard bioinformatics recognition task, and (2) applying general biological knowledge that a glycosyltransferase participates in a biosynthetic process rather than a regulatory or stress-response process. This is a concrete biological argument that meaningfully distinguishes C from A, B, and D without requiring memorization of this specific protein's annotation. The specific 'saponin' label cannot be positively identified from sequence, but it is the only biosynthetic option, making elimination sufficient.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe regulatory/signaling/stress-response processes incompatible with a glycosyltransferase enzyme's primary function. Option C is the sole biosynthetic/metabolic process among the choices. No other option is defensible for a glycosyltransferase.


### Important caveats

- The reasoning path assumes the model can identify the protein as a UGT/glycosyltransferase from the sequence (PSPG motif recognition). If the model cannot perform this family-level identification, the question becomes lookup-dependent.
- The specific 'saponin' identification (as opposed to, e.g., flavonoid glycosylation) cannot be made from sequence alone; the answer relies on C being the only biosynthetic option among the four distractors.
- The UniProt annotation is IDA (Inferred from Direct Assay) based on a 2025 Nat. Chem. Biol. paper (PubMed:39043959), representing strong experimental evidence.
- The GO term GO:0016135 definition confirms saponins are 'glycosides of plants in which the aglycan group is a terpene or steroid and the sugar group is a glucose, galactose, pentose, methylpentose or oligosaccharide,' consistent with a glycosyltransferase's enzymatic role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features consistent with a plant UDP-glycosyltransferase (UGT family, PSPG motif region in the C-terminal half). A glycosyltransferase catalyzes the transfer of sugar moieties to acceptor molecules — a biosynthetic/conjugation enzymatic activity. Among the four options, only C ('saponin biosynthetic process') describes a biosynthetic/metabolic process in which a glycosyltransferase would directly participate. Options A ('regulation of leaf senescence'), B ('response to misfolded protein'), and D ('regulation of Rab protein signal transduction') are regulatory, stress-response, or signaling processes that do not naturally involve a glycosyltransferase as a primary functional participant. Thus, identifying the protein as an enzyme (specifically a glycosyltransferase) and applying general biological reasoning that enzymes catalyze biosynthetic reactions rather than 'regulate' or 'respond to' processes allows elimination of A, B, and D, leaving C as the only consistent option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (oleanane-type triterpene saponin precursor QA-triF) cannot be determined from sequence alone. However, since 'saponin biosynthetic process' is the only biosynthetic option among the four, the elimination-based reasoning path does not require knowing the exact substrate.",
    "reason": "The reasoning path requires (1) recognizing the protein as a glycosyltransferase from conserved domain features (PSPG motif), which is a standard bioinformatics recognition task, and (2) applying general biological knowledge that a glycosyltransferase participates in a biosynthetic process rather than a regulatory or stress-response process. This is a concrete biological argument that meaningfully distinguishes C from A, B, and D without requiring memorization of this specific protein's annotation. The specific 'saponin' label cannot be positively identified from sequence, but it is the only biosynthetic option, making elimination sufficient."
  },
  "case_id": "GO_biological_process_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5",
      "H1",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1IQ05 (GT791_SAPOF, SoUGT79T1) is annotated with GO:0016135 'saponin biosynthetic process' via IDA (Inferred from Direct Assay) based on experimental evidence from PubMed:39043959 (Nat. Chem. Biol. 2025). The FUNCTION comment explicitly states it is 'Component of the oleanane-type triterpene saponins biosynthetic pathway' and describes its glycosyltransferase activity on a saponin precursor (QA-triF to QA-triFR). The sequence SHA256 matches exactly. The annotation is experimentally derived, not computational inference."
  },
  "important_caveats": [
    "The reasoning path assumes the model can identify the protein as a UGT/glycosyltransferase from the sequence (PSPG motif recognition). If the model cannot perform this family-level identification, the question becomes lookup-dependent.",
    "The specific 'saponin' identification (as opposed to, e.g., flavonoid glycosylation) cannot be made from sequence alone; the answer relies on C being the only biosynthetic option among the four distractors.",
    "The UniProt annotation is IDA (Inferred from Direct Assay) based on a 2025 Nat. Chem. Biol. paper (PubMed:39043959), representing strong experimental evidence.",
    "The GO term GO:0016135 definition confirms saponins are 'glycosides of plants in which the aglycan group is a terpene or steroid and the sugar group is a glucose, galactose, pentose, methylpentose or oligosaccharide,' consistent with a glycosyltransferase's enzymatic role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe regulatory/signaling/stress-response processes incompatible with a glycosyltransferase enzyme's primary function. Option C is the sole biosynthetic/metabolic process among the choices. No other option is defensible for a glycosyltransferase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1IQ05 (GT791_SAPOF, SoUGT79T1) is annotated with GO:0016135 'saponin biosynthetic process' via IDA (Inferred from Direct Assay) based on experimental evidence from PubMed:39043959 (Nat. Chem. Biol. 2025). The FUNCTION comment explicitly states it is 'Component of the oleanane-type triterpene saponins biosynthetic pathway' and describes its glycosyltransferase activity on a saponin precursor (QA-triF to QA-triFR). The sequence SHA256 matches exactly. The annotation is experimentally derived, not computational inference.",
    "evidence_ids": ["C5", "C7", "H3", "H5", "H1", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains features consistent with a plant UDP-glycosyltransferase (UGT family, PSPG motif region in the C-terminal half). A glycosyltransferase catalyzes the transfer of sugar moieties to acceptor molecules — a biosynthetic/conjugation enzymatic activity. Among the four options, only C ('saponin biosynthetic process') describes a biosynthetic/metabolic process in which a glycosyltransferase would directly participate. Options A ('regulation of leaf senescence'), B ('response to misfolded protein'), and D ('regulation of Rab protein signal transduction') are regulatory, stress-response, or signaling processes that do not naturally involve a glycosyltransferase as a primary functional participant. Thus, identifying the protein as an enzyme (specifically a glycosyltransferase) and applying general biological reasoning that enzymes catalyze biosynthetic reactions rather than 'regulate' or 'respond to' processes allows elimination of A, B, and D, leaving C as the only consistent option.",
    "missing_item_specific_fact": "The specific substrate identity (oleanane-type triterpene saponin precursor QA-triF) cannot be determined from sequence alone. However, since 'saponin biosynthetic process' is the only biosynthetic option among the four, the elimination-based reasoning path does not require knowing the exact substrate.",
    "reason": "The reasoning path requires (1) recognizing the protein as a glycosyltransferase from conserved domain features (PSPG motif), which is a standard bioinformatics recognition task, and (2) applying general biological knowledge that a glycosyltransferase participates in a biosynthetic process rather than a regulatory or stress-response process. This is a concrete biological argument that meaningfully distinguishes C from A, B, and D without requiring memorization of this specific protein's annotation. The specific 'saponin' label cannot be positively identified from sequence, but it is the only biosynthetic option, making elimination sufficient."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe regulatory/signaling/stress-response processes incompatible with a glycosyltransferase enzyme's primary function. Option C is the sole biosynthetic/metabolic process among the choices. No other option is defensible for a glycosyltransferase."
  },
  "important_caveats": [
    "The reasoning path assumes the model can identify the protein as a UGT/glycosyltransferase from the sequence (PSPG motif recognition). If the model cannot perform this family-level identification, the question becomes lookup-dependent.",
    "The specific 'saponin' identification (as opposed to, e.g., flavonoid glycosylation) cannot be made from sequence alone; the answer relies on C being the only biosynthetic option among the four distractors.",
    "The UniProt annotation is IDA (Inferred from Direct Assay) based on a 2025 Nat. Chem. Biol. paper (PubMed:39043959), representing strong experimental evidence.",
    "The GO term GO:0016135 definition confirms saponins are 'glycosides of plants in which the aglycan group is a terpene or steroid and the sugar group is a glucose, galactose, pentose, methylpentose or oligosaccharide,' consistent with a glycosyltransferase's enzymatic role."
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

**Accession:** `A0AAW1IQ05` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:32.727746+00:00.  

```json
"A0AAW1IQ05"
```

Source SHA-256: `7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:32.727746+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). A glycosyltransferase that mediates the conversion of QA-triF to QA-triFR via the elongation of the C-28 sugar chain with a deoxyhexose on the D-fucose moiety (PubMed:39043959)"}]}
```

Source SHA-256: `7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:32.727746+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39043959","source":"PubMed"}],"id":"GO:0016135","properties":[{"key":"GoTerm","value":"P:saponin biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:34.746032+00:00.  

```text
ID   GT791_SAPOF             Reviewed;         447 AA.
AC   A0AAW1IQ05;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-NOV-2024, sequence version 1.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=UDP-glucosyl transferase 79T1 {ECO:0000303|PubMed:39043959};
DE            Short=SoUGT79T1 {ECO:0000303|PubMed:39043959};
DE            EC=2.4.1.- {ECO:0000269|PubMed:39043959};
GN   Name=UGT79T1 {ECO:0000303|PubMed:39043959};
GN   Synonyms=Saoffv11049136m {ECO:0000303|PubMed:39043959};
GN   ORFNames=RND81_09G214900 {ECO:0000312|EMBL:KAK9691727.1};
OS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.
OX   NCBI_TaxID=3572;
```

Source SHA-256: `8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:34.746032+00:00.  

```text
CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.
CC       saponarioside A and saponarioside B) biosynthetic pathway, leading to
CC       the production of natural products with detergent properties used as
CC       traditional sources of soap (PubMed:39043959). A glycosyltransferase
CC       that mediates the conversion of QA-triF to QA-triFR via the elongation
CC       of the C-28 sugar chain with a deoxyhexose on the D-fucose moiety
CC       (PubMed:39043959). {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)  
**Locator:** `lines 75-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:34.746032+00:00.  

```text
DR   GO; GO:0016135; P:saponin biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 123836-123847`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016135
name: saponin biosynthetic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the formation of saponins, glycosides of plants in which the aglycan (sapogenin) group is a terpene or steroid and the sugar group is a glucose, a galactose, a pentose, a methylpentose or an oligosaccharide. Saponins are powerful surfactant agents and membrane active; they are, hence, toxic to animals on injection." [GOC:curators]
synonym: "saponin anabolism" EXACT []
synonym: "saponin biosynthesis" EXACT []
synonym: "saponin formation" EXACT []
synonym: "saponin synthesis" EXACT []
is_a: GO:0016134 ! saponin metabolic process
is_a: GO:0016138 ! glycoside biosynthetic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 31. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
