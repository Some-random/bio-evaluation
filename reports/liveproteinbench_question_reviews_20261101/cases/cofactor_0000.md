# cofactor_0000

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKYAHVGLNVTNLEKSIEFYSKLFGAEPVKVKPDYAKFLLESPGLNFTLNLRDEVNGNQVGHFGIQVESTEEVVAHKNRLAENGILSQYDEINTTCCYALQDKFWIHDPDGNEWEFFYTKTTVEENSTHPPTCCVNEPNVEKAECCSPTASSNKDTSNCCS

[Multiple Choices]
A. pyridoxal 5'-phosphate
B. [4Fe-4S] cluster
C. Fe(2+)
D. FAD
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt entry, which annotates Fe(2+) as the cofactor with experimental evidence codes citing two publications. This supports Choice C for this protein, while the evidence is a database annotation grounded in cited experimental work rather than information provided in the question.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a metal-binding protein, but its residues do not provide a defensible basis for distinguishing Fe(2+) from the other listed cofactors.


**Missing item-specific fact**

> The protein-specific identification and experimentally supported cofactor annotation linking this sequence to Fe(2+).


**Reason**

> Selecting C requires an item-specific annotation or experimental fact absent from the sequence-and-choices input; recognizing the sequence from an external database would be lookup or memorization, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only, sequence-matched annotation supports Fe(2+); the supplied evidence does not support another listed choice.


### Important caveats

- The database’s cofactor annotation cites experimental evidence, but the cited primary studies were not independently reviewed here.
- The exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a metal-binding protein, but its residues do not provide a defensible basis for distinguishing Fe(2+) from the other listed cofactors.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and experimentally supported cofactor annotation linking this sequence to Fe(2+).",
    "reason": "Selecting C requires an item-specific annotation or experimental fact absent from the sequence-and-choices input; recognizing the sequence from an external database would be lookup or memorization, not reasoning from the supplied information."
  },
  "case_id": "cofactor_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry, which annotates Fe(2+) as the cofactor with experimental evidence codes citing two publications. This supports Choice C for this protein, while the evidence is a database annotation grounded in cited experimental work rather than information provided in the question."
  },
  "important_caveats": [
    "The database’s cofactor annotation cites experimental evidence, but the cited primary studies were not independently reviewed here.",
    "The exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only, sequence-matched annotation supports Fe(2+); the supplied evidence does not support another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry, which annotates Fe(2+) as the cofactor with experimental evidence codes citing two publications. This supports Choice C for this protein, while the evidence is a database annotation grounded in cited experimental work rather than information provided in the question.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a metal-binding protein, but its residues do not provide a defensible basis for distinguishing Fe(2+) from the other listed cofactors.",
    "missing_item_specific_fact": "The protein-specific identification and experimentally supported cofactor annotation linking this sequence to Fe(2+).",
    "reason": "Selecting C requires an item-specific annotation or experimental fact absent from the sequence-and-choices input; recognizing the sequence from an external database would be lookup or memorization, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only, sequence-matched annotation supports Fe(2+); the supplied evidence does not support another listed choice."
  },
  "important_caveats": [
    "The database’s cofactor annotation cites experimental evidence, but the cited primary studies were not independently reviewed here.",
    "The exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProtKB entry A0A059WI14 (ARSI_BACX0, 161 AA, sequence SHA256 matched) explicitly annotates the cofactor as Fe(2+) (ChEBI:CHEBI:29033) with evidence code ECO:0000269 (inferred from direct assay) supported by two independent experimental papers (PubMed:24821808, 2014; PubMed:28936873, 2017). This is experimental, not merely computational, evidence. The protein is the C-As lyase ArsI, a trivalent organoarsenical cleaving enzyme (EC 1.13.11.-).

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Partial reasoning can eliminate FAD (no Rossmann-fold GxGxxG motif at the N-terminus) and PLP (no conserved catalytic lysine in a recognizable PLP-binding pocket). However, the critical distinction between Fe(2+) (choice C) and &#91;4Fe-4S&#93; (choice B) cannot be reliably resolved from the sequence alone. The 161-residue protein contains His residues (H5, H62, H73) and Cys residues (C96, C97, and multiple C-terminal cysteines), which are compatible with either a mononuclear Fe(2+) center or a &#91;4Fe-4S&#93; cluster. The irregular CC-pair cysteine spacing argues weakly against a canonical 4Fe-4S ferredoxin-type arrangement, but this heuristic is insufficient to definitively exclude &#91;4Fe-4S&#93;.


**Missing item-specific fact**

> The specific identity of this protein as ArsI (a novel C-As lyase with no well-characterized homologous family) and its experimentally determined mononuclear Fe(2+) coordination environment (His-5, His-62, Cys-96, Cys-97, Glu-115) are item-specific facts not derivable from the sequence. The cofactor assignment was established by direct biochemical assay (ECO:0000269), not by sequence-similarity transfer, confirming it is an empirical finding rather than a sequence-predictable property.


**Reason**

> While general knowledge of Rossmann folds and PLP motifs can eliminate two distractors, the final choice between the two iron-dependent options (Fe(2+) vs &#91;4Fe-4S&#93;) requires knowing the specific protein family or its experimentally characterized metal site. This protein is a novel enzyme (first characterized 2014) with no close homologs in standard databases, making family-based inference unavailable. The distinction is an item-specific experimental fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> From sequence alone, both &#91;4Fe-4S&#93; (B) and Fe(2+) (C) are plausible given the presence of multiple Cys and His residues. A knowledgeable reviewer might argue the irregular CC-pair cysteine spacing disfavors a canonical 4Fe-4S, but this is a weak heuristic and not conclusive without structural data. The question wording does not provide functional context (e.g., 'this enzyme cleaves a C-As bond using O2') that would guide the model toward a mononuclear dioxygenase-type Fe(2+) center.


### Important caveats

- The protein is a novel enzyme (ArsI, C-As lyase) first characterized in 2014; it lacks a well-known homologous family, making family-based cofactor inference unreliable.
- The cofactor assignment is backed by direct experimental assay (ECO:0000269) from two independent studies, making it a robust annotation.
- The evaluated model receives only the raw sequence and four choices with no functional context, protein name, or EC number.
- The reviewer-only UniProt accession was inferred mechanically from dataset metadata and was absent from the model input.
- Elimination of FAD and PLP via absence of canonical motifs is reasonable but does not resolve the B-vs-C distinction with confidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Partial reasoning can eliminate FAD (no Rossmann-fold GxGxxG motif at the N-terminus) and PLP (no conserved catalytic lysine in a recognizable PLP-binding pocket). However, the critical distinction between Fe(2+) (choice C) and [4Fe-4S] (choice B) cannot be reliably resolved from the sequence alone. The 161-residue protein contains His residues (H5, H62, H73) and Cys residues (C96, C97, and multiple C-terminal cysteines), which are compatible with either a mononuclear Fe(2+) center or a [4Fe-4S] cluster. The irregular CC-pair cysteine spacing argues weakly against a canonical 4Fe-4S ferredoxin-type arrangement, but this heuristic is insufficient to definitively exclude [4Fe-4S].",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as ArsI (a novel C-As lyase with no well-characterized homologous family) and its experimentally determined mononuclear Fe(2+) coordination environment (His-5, His-62, Cys-96, Cys-97, Glu-115) are item-specific facts not derivable from the sequence. The cofactor assignment was established by direct biochemical assay (ECO:0000269), not by sequence-similarity transfer, confirming it is an empirical finding rather than a sequence-predictable property.",
    "reason": "While general knowledge of Rossmann folds and PLP motifs can eliminate two distractors, the final choice between the two iron-dependent options (Fe(2+) vs [4Fe-4S]) requires knowing the specific protein family or its experimentally characterized metal site. This protein is a novel enzyme (first characterized 2014) with no close homologs in standard databases, making family-based inference unavailable. The distinction is an item-specific experimental fact."
  },
  "case_id": "cofactor_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProtKB entry A0A059WI14 (ARSI_BACX0, 161 AA, sequence SHA256 matched) explicitly annotates the cofactor as Fe(2+) (ChEBI:CHEBI:29033) with evidence code ECO:0000269 (inferred from direct assay) supported by two independent experimental papers (PubMed:24821808, 2014; PubMed:28936873, 2017). This is experimental, not merely computational, evidence. The protein is the C-As lyase ArsI, a trivalent organoarsenical cleaving enzyme (EC 1.13.11.-)."
  },
  "important_caveats": [
    "The protein is a novel enzyme (ArsI, C-As lyase) first characterized in 2014; it lacks a well-known homologous family, making family-based cofactor inference unreliable.",
    "The cofactor assignment is backed by direct experimental assay (ECO:0000269) from two independent studies, making it a robust annotation.",
    "The evaluated model receives only the raw sequence and four choices with no functional context, protein name, or EC number.",
    "The reviewer-only UniProt accession was inferred mechanically from dataset metadata and was absent from the model input.",
    "Elimination of FAD and PLP via absence of canonical motifs is reasonable but does not resolve the B-vs-C distinction with confidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "From sequence alone, both [4Fe-4S] (B) and Fe(2+) (C) are plausible given the presence of multiple Cys and His residues. A knowledgeable reviewer might argue the irregular CC-pair cysteine spacing disfavors a canonical 4Fe-4S, but this is a weak heuristic and not conclusive without structural data. The question wording does not provide functional context (e.g., 'this enzyme cleaves a C-As bond using O2') that would guide the model toward a mononuclear dioxygenase-type Fe(2+) center."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProtKB entry A0A059WI14 (ARSI_BACX0, 161 AA, sequence SHA256 matched) explicitly annotates the cofactor as Fe(2+) (ChEBI:CHEBI:29033) with evidence code ECO:0000269 (inferred from direct assay) supported by two independent experimental papers (PubMed:24821808, 2014; PubMed:28936873, 2017). This is experimental, not merely computational, evidence. The protein is the C-As lyase ArsI, a trivalent organoarsenical cleaving enzyme (EC 1.13.11.-).",
    "evidence_ids": ["C5", "H5", "C6", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Partial reasoning can eliminate FAD (no Rossmann-fold GxGxxG motif at the N-terminus) and PLP (no conserved catalytic lysine in a recognizable PLP-binding pocket). However, the critical distinction between Fe(2+) (choice C) and [4Fe-4S] (choice B) cannot be reliably resolved from the sequence alone. The 161-residue protein contains His residues (H5, H62, H73) and Cys residues (C96, C97, and multiple C-terminal cysteines), which are compatible with either a mononuclear Fe(2+) center or a [4Fe-4S] cluster. The irregular CC-pair cysteine spacing argues weakly against a canonical 4Fe-4S ferredoxin-type arrangement, but this heuristic is insufficient to definitively exclude [4Fe-4S].",
    "missing_item_specific_fact": "The specific identity of this protein as ArsI (a novel C-As lyase with no well-characterized homologous family) and its experimentally determined mononuclear Fe(2+) coordination environment (His-5, His-62, Cys-96, Cys-97, Glu-115) are item-specific facts not derivable from the sequence. The cofactor assignment was established by direct biochemical assay (ECO:0000269), not by sequence-similarity transfer, confirming it is an empirical finding rather than a sequence-predictable property.",
    "reason": "While general knowledge of Rossmann folds and PLP motifs can eliminate two distractors, the final choice between the two iron-dependent options (Fe(2+) vs [4Fe-4S]) requires knowing the specific protein family or its experimentally characterized metal site. This protein is a novel enzyme (first characterized 2014) with no close homologs in standard databases, making family-based inference unavailable. The distinction is an item-specific experimental fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "From sequence alone, both [4Fe-4S] (B) and Fe(2+) (C) are plausible given the presence of multiple Cys and His residues. A knowledgeable reviewer might argue the irregular CC-pair cysteine spacing disfavors a canonical 4Fe-4S, but this is a weak heuristic and not conclusive without structural data. The question wording does not provide functional context (e.g., 'this enzyme cleaves a C-As bond using O2') that would guide the model toward a mononuclear dioxygenase-type Fe(2+) center."
  },
  "important_caveats": [
    "The protein is a novel enzyme (ArsI, C-As lyase) first characterized in 2014; it lacks a well-known homologous family, making family-based cofactor inference unreliable.",
    "The cofactor assignment is backed by direct experimental assay (ECO:0000269) from two independent studies, making it a robust annotation.",
    "The evaluated model receives only the raw sequence and four choices with no functional context, protein name, or EC number.",
    "The reviewer-only UniProt accession was inferred mechanically from dataset metadata and was absent from the model input.",
    "Elimination of FAD and PLP via absence of canonical motifs is reasonable but does not resolve the B-vs-C distinction with confidence."
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

**Accession:** `A0A059WI14` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 22. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:54.040783+00:00.  

```json
"A0A059WI14"
```

Source SHA-256: `8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:54.040783+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29033"},"evidences":[{"evidenceCode":"ECO:0000269","id":"24821808","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28936873","source":"PubMed"}],"name":"Fe(2+)"}],"commentType":"COFACTOR"}
```

Source SHA-256: `8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:54.040783+00:00.  

```json
{"citation":{"authors":["Yoshinaga M.","Rosen B.P."],"citationCrossReferences":[{"database":"PubMed","id":"24821808"},{"database":"DOI","id":"10.1073/pnas.1403057111"}],"citationType":"journal article","firstPage":"7701","id":"24821808","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"7706","publicationDate":"2014","title":"A C-As lyase for degradation of environmental organoarsenical herbicides and animal husbandry growth promoters.","volume":"111"},"referenceComments":[{"type":"STRAIN","value":"MD1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:54.040783+00:00.  

```json
{"citation":{"authors":["Pawitwar S.S.","Nadar V.S.","Kandegedara A.","Stemmler T.L.","Rosen B.P.","Yoshinaga M."],"citationCrossReferences":[{"database":"PubMed","id":"28936873"},{"database":"DOI","id":"10.1021/acs.est.7b03180"}],"citationType":"journal article","firstPage":"11115","id":"28936873","journal":"Environ. Sci. Technol.","lastPage":"11125","publicationDate":"2017","title":"Biochemical Characterization of ArsI: A Novel C-As Lyase for Degradation of Environmental Organoarsenicals.","volume":"51"},"referenceComments":[{"type":"STRAIN","value":"MD1"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","3D-STRUCTURE MODELING","MUTAGENESIS OF HIS-5; HIS-62; 96-CYS-CYS-97 AND GLU-115"]}
```

Source SHA-256: `8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)  
**Locator:** `lines 16-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:23:56.065730+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
RP   AND BIOPHYSICOCHEMICAL PROPERTIES.
RC   STRAIN=MD1;
RX   PubMed=24821808; DOI=10.1073/pnas.1403057111;
RA   Yoshinaga M., Rosen B.P.;
RT   "A C-As lyase for degradation of environmental organoarsenical herbicides
RT   and animal husbandry growth promoters.";
RL   Proc. Natl. Acad. Sci. U.S.A. 111:7701-7706(2014).
```

Source SHA-256: `64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)  
**Locator:** `lines 25-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:23:56.065730+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, 3D-STRUCTURE
RP   MODELING, AND MUTAGENESIS OF HIS-5; HIS-62; 96-CYS-CYS-97 AND GLU-115.
RC   STRAIN=MD1;
RX   PubMed=28936873; DOI=10.1021/acs.est.7b03180;
RA   Pawitwar S.S., Nadar V.S., Kandegedara A., Stemmler T.L., Rosen B.P.,
RA   Yoshinaga M.;
RT   "Biochemical Characterization of ArsI: A Novel C-As Lyase for Degradation
RT   of Environmental Organoarsenicals.";
RL   Environ. Sci. Technol. 51:11115-11125(2017).
```

Source SHA-256: `64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)  
**Locator:** `lines 79-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:23:56.065730+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;
CC         Evidence={ECO:0000269|PubMed:24821808, ECO:0000269|PubMed:28936873};
```

Source SHA-256: `64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
