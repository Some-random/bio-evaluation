# catalytic_activity_0147

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — &#91;thioredoxin&#93;-dithiol + NADP(+) = &#91;thioredoxin&#93;-disulfide + NADPH + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MANILENQLFTAAKTIEQQLDQQLDRLDNLDSDDLKVLREQRLREMKDLNNKKQEWLRNGHGTYTELADEKEFFEMSKKSPNIVCHFYRDSTERCKIVDMHLKILAAKHVEAKFCKVNAEKTPFLTQRLRIKVIPTIALVKDSKTKDFIVGFTDLGNCDDFATEMLEWRIAHSGAIDYKGDLMQPPDVKRKPFINRPQKTIRGGYDSDDSDIDLDD

[Multiple Choices]
A. [thioredoxin]-dithiol + NADP(+) = [thioredoxin]-disulfide + NADPH + H(+)
B. N-acetylneuraminate + CTP = CMP-N-acetyl-beta-neuraminate + diphosphate
C. beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)
D. (19E)-geissoschizine + reduced [NADPH--hemoprotein reductase] + O2 = rhazimal + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry annotated with EC 1.8.1.9 and the reaction in choice A. The annotation carries experimental-evidence code ECO:0000269 and is also present in the historical record available by the stated cutoff. This supports the key, though the cited primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices name distinct, specific enzyme reactions, but the supplied sequence alone offers no clear motif or context that identifies which one this protein catalyzes. General sequence reasoning does not establish the precise catalytic activity.


**Missing item-specific fact**

> The protein-specific functional assignment or experimental evidence that this sequence catalyzes the thioredoxin/NADP(+) reaction.


**Reason**

> Selecting A depends on knowing the identity or catalytic annotation of this particular protein, information absent from the input. Reviewer-only database evidence supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports A; it does not establish any competing option for this sequence.


### Important caveats

- The sequence match is exact, and the relevant historical database record includes the catalytic-activity annotation.
- The annotation cites experimental evidence, but the cited paper was not independently examined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices name distinct, specific enzyme reactions, but the supplied sequence alone offers no clear motif or context that identifies which one this protein catalyzes. General sequence reasoning does not establish the precise catalytic activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment or experimental evidence that this sequence catalyzes the thioredoxin/NADP(+) reaction.",
    "reason": "Selecting A depends on knowing the identity or catalytic annotation of this particular protein, information absent from the input. Reviewer-only database evidence supports the key but was not supplied to the evaluated model."
  },
  "case_id": "catalytic_activity_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated with EC 1.8.1.9 and the reaction in choice A. The annotation carries experimental-evidence code ECO:0000269 and is also present in the historical record available by the stated cutoff. This supports the key, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact, and the relevant historical database record includes the catalytic-activity annotation.",
    "The annotation cites experimental evidence, but the cited paper was not independently examined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A; it does not establish any competing option for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated with EC 1.8.1.9 and the reaction in choice A. The annotation carries experimental-evidence code ECO:0000269 and is also present in the historical record available by the stated cutoff. This supports the key, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices name distinct, specific enzyme reactions, but the supplied sequence alone offers no clear motif or context that identifies which one this protein catalyzes. General sequence reasoning does not establish the precise catalytic activity.",
    "missing_item_specific_fact": "The protein-specific functional assignment or experimental evidence that this sequence catalyzes the thioredoxin/NADP(+) reaction.",
    "reason": "Selecting A depends on knowing the identity or catalytic annotation of this particular protein, information absent from the input. Reviewer-only database evidence supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A; it does not establish any competing option for this sequence."
  },
  "important_caveats": [
    "The sequence match is exact, and the relevant historical database record includes the catalytic-activity annotation.",
    "The annotation cites experimental evidence, but the cited paper was not independently examined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9VGV8 (PhLP3_DROME) annotates EC 1.8.1.9 with the exact reaction '&#91;thioredoxin&#93;-dithiol + NADP(+) = &#91;thioredoxin&#93;-disulfide + NADPH + H(+)', supported by experimental evidence (ECO:0000269, PubMed:39480878, 2024 PLoS ONE paper). The benchmark sequence matches the UniProt sequence exactly (216 aa, SHA-256 identical). The annotation is backed by a primary experimental study demonstrating thioredoxin reductase activity for PhLP3.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The 216-aa sequence lacks the canonical thioredoxin reductase architecture (~475-500 aa with FAD/NADPH-binding domains and the Cys-Val-Asn-Val active-site motif). No obvious FAD-binding Rossmann fold, no clear CVNV motif, and no heme-binding CXXCH motif are identifiable. The sequence does not positively indicate EC 1.8.1.9 over the other three options through general structural or motif reasoning.


**Missing item-specific fact**

> The 2024 experimental finding (PubMed:39480878) demonstrating that Drosophila PhLP3, a 216-aa phosducin-like chaperone protein, possesses thioredoxin reductase (EC 1.8.1.9) activity. Without knowing this specific protein identity and its recently characterized non-canonical enzymatic function, the sequence alone provides no reliable basis to select A over B, C, or D.


**Reason**

> While the distractors belong to different enzyme classes (nucleotidyltransferase, kinase, P450-type monooxygenase) and one might weakly argue by elimination that no kinase or heme-binding motifs are present, this negative evidence does not positively identify thioredoxin reductase activity in a 216-aa protein that lacks canonical TrxR structural features. The correct answer depends on knowing the specific 2024 experimental characterization of PhLP3 as an EC 1.8.1.9 enzyme, which is a non-obvious, recently discovered function not inferable from sequence motifs or general enzyme classification logic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (oxidoreductase, transferase, kinase, monooxygenase). If the protein is correctly identified as PhLP3 with its experimentally validated EC 1.8.1.9 activity, the answer is unambiguous. The difficulty lies in protein identification and function assignment from a short sequence, not in ambiguity between the choices themselves.


### Important caveats

- The EC 1.8.1.9 annotation for PhLP3 is a 2024 experimental finding (PubMed:39480878); this is a non-canonical function for a phosducin-like protein traditionally studied as a G-protein/ciliary assembly chaperone.
- The annotation evidence code ECO:0000269 indicates direct experimental evidence, not computational inference or similarity transfer.
- The protein is only 216 aa, far smaller than canonical thioredoxin reductases (~475-500 aa), making motif-based identification particularly unreliable.
- The identity origin (accession Q9VGV8) was inferred from dataset metadata and was absent from the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 216-aa sequence lacks the canonical thioredoxin reductase architecture (~475-500 aa with FAD/NADPH-binding domains and the Cys-Val-Asn-Val active-site motif). No obvious FAD-binding Rossmann fold, no clear CVNV motif, and no heme-binding CXXCH motif are identifiable. The sequence does not positively indicate EC 1.8.1.9 over the other three options through general structural or motif reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The 2024 experimental finding (PubMed:39480878) demonstrating that Drosophila PhLP3, a 216-aa phosducin-like chaperone protein, possesses thioredoxin reductase (EC 1.8.1.9) activity. Without knowing this specific protein identity and its recently characterized non-canonical enzymatic function, the sequence alone provides no reliable basis to select A over B, C, or D.",
    "reason": "While the distractors belong to different enzyme classes (nucleotidyltransferase, kinase, P450-type monooxygenase) and one might weakly argue by elimination that no kinase or heme-binding motifs are present, this negative evidence does not positively identify thioredoxin reductase activity in a 216-aa protein that lacks canonical TrxR structural features. The correct answer depends on knowing the specific 2024 experimental characterization of PhLP3 as an EC 1.8.1.9 enzyme, which is a non-obvious, recently discovered function not inferable from sequence motifs or general enzyme classification logic."
  },
  "case_id": "catalytic_activity_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9VGV8 (PhLP3_DROME) annotates EC 1.8.1.9 with the exact reaction '[thioredoxin]-dithiol + NADP(+) = [thioredoxin]-disulfide + NADPH + H(+)', supported by experimental evidence (ECO:0000269, PubMed:39480878, 2024 PLoS ONE paper). The benchmark sequence matches the UniProt sequence exactly (216 aa, SHA-256 identical). The annotation is backed by a primary experimental study demonstrating thioredoxin reductase activity for PhLP3."
  },
  "important_caveats": [
    "The EC 1.8.1.9 annotation for PhLP3 is a 2024 experimental finding (PubMed:39480878); this is a non-canonical function for a phosducin-like protein traditionally studied as a G-protein/ciliary assembly chaperone.",
    "The annotation evidence code ECO:0000269 indicates direct experimental evidence, not computational inference or similarity transfer.",
    "The protein is only 216 aa, far smaller than canonical thioredoxin reductases (~475-500 aa), making motif-based identification particularly unreliable.",
    "The identity origin (accession Q9VGV8) was inferred from dataset metadata and was absent from the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (oxidoreductase, transferase, kinase, monooxygenase). If the protein is correctly identified as PhLP3 with its experimentally validated EC 1.8.1.9 activity, the answer is unambiguous. The difficulty lies in protein identification and function assignment from a short sequence, not in ambiguity between the choices themselves."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9VGV8 (PhLP3_DROME) annotates EC 1.8.1.9 with the exact reaction '[thioredoxin]-dithiol + NADP(+) = [thioredoxin]-disulfide + NADPH + H(+)', supported by experimental evidence (ECO:0000269, PubMed:39480878, 2024 PLoS ONE paper). The benchmark sequence matches the UniProt sequence exactly (216 aa, SHA-256 identical). The annotation is backed by a primary experimental study demonstrating thioredoxin reductase activity for PhLP3.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The 216-aa sequence lacks the canonical thioredoxin reductase architecture (~475-500 aa with FAD/NADPH-binding domains and the Cys-Val-Asn-Val active-site motif). No obvious FAD-binding Rossmann fold, no clear CVNV motif, and no heme-binding CXXCH motif are identifiable. The sequence does not positively indicate EC 1.8.1.9 over the other three options through general structural or motif reasoning.",
    "missing_item_specific_fact": "The 2024 experimental finding (PubMed:39480878) demonstrating that Drosophila PhLP3, a 216-aa phosducin-like chaperone protein, possesses thioredoxin reductase (EC 1.8.1.9) activity. Without knowing this specific protein identity and its recently characterized non-canonical enzymatic function, the sequence alone provides no reliable basis to select A over B, C, or D.",
    "reason": "While the distractors belong to different enzyme classes (nucleotidyltransferase, kinase, P450-type monooxygenase) and one might weakly argue by elimination that no kinase or heme-binding motifs are present, this negative evidence does not positively identify thioredoxin reductase activity in a 216-aa protein that lacks canonical TrxR structural features. The correct answer depends on knowing the specific 2024 experimental characterization of PhLP3 as an EC 1.8.1.9 enzyme, which is a non-obvious, recently discovered function not inferable from sequence motifs or general enzyme classification logic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (oxidoreductase, transferase, kinase, monooxygenase). If the protein is correctly identified as PhLP3 with its experimentally validated EC 1.8.1.9 activity, the answer is unambiguous. The difficulty lies in protein identification and function assignment from a short sequence, not in ambiguity between the choices themselves."
  },
  "important_caveats": [
    "The EC 1.8.1.9 annotation for PhLP3 is a 2024 experimental finding (PubMed:39480878); this is a non-canonical function for a phosducin-like protein traditionally studied as a G-protein/ciliary assembly chaperone.",
    "The annotation evidence code ECO:0000269 indicates direct experimental evidence, not computational inference or similarity transfer.",
    "The protein is only 216 aa, far smaller than canonical thioredoxin reductases (~475-500 aa), making motif-based identification particularly unreliable.",
    "The identity origin (accession Q9VGV8) was inferred from dataset metadata and was absent from the evaluated model input."
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

**Accession:** `Q9VGV8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 205. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.511607+00:00.  

```json
"Q9VGV8"
```

Source SHA-256: `001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.511607+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39480878","source":"PubMed"}],"value":"1.8.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0037843","source":"FlyBase"}],"value":"Phosducin-like protein 3"}}}
```

Source SHA-256: `001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.511607+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.8.1.9","evidences":[{"evidenceCode":"ECO:0000269","id":"39480878","source":"PubMed"}],"name":"[thioredoxin]-dithiol + NADP(+) = [thioredoxin]-disulfide + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20345"},{"database":"Rhea","id":"RHEA-COMP:10698"},{"database":"Rhea","id":"RHEA-COMP:10700"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29950"},{"database":"ChEBI","id":"CHEBI:50058"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.511607+00:00.  

```json
{"citation":{"authors":["Petit C.","Kojak E.","Webster S.","Marra M.","Sweeney B.","Chaikin C.","Jemc J.C.","Kanzok S.M."],"citationCrossReferences":[{"database":"PubMed","id":"39480878"},{"database":"DOI","id":"10.1371/journal.pone.0306676"}],"citationType":"journal article","firstPage":"e0306676","id":"39480878","journal":"PLoS ONE","lastPage":"e0306676","publicationDate":"2024","title":"The evolutionarily conserved PhLP3 is essential for sperm development in Drosophila melanogaster.","volume":"19"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","TISSUE SPECIFICITY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 205 / 1.  
**Retrieved:** 2026-11-01T06:28:51.609437+00:00.  

```text
ID   PHLP3_DROME             Reviewed;         216 AA.
AC   Q9VGV8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 205.
DE   RecName: Full=Phosducin-like protein 3 {ECO:0000312|FlyBase:FBgn0037843};
DE            EC=1.8.1.9 {ECO:0000269|PubMed:39480878};
GN   Name=PhLP3 {ECO:0000312|FlyBase:FBgn0037843};
GN   ORFNames=CG4511 {ECO:0000312|FlyBase:FBgn0037843};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 205 / 1.  
**Retrieved:** 2026-11-01T06:28:51.609437+00:00.  

```text
DE   RecName: Full=Phosducin-like protein 3 {ECO:0000312|FlyBase:FBgn0037843};
DE            EC=1.8.1.9 {ECO:0000269|PubMed:39480878};
```

Source SHA-256: `ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)  
**Locator:** `lines 92-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 205 / 1.  
**Retrieved:** 2026-11-01T06:28:51.609437+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=[thioredoxin]-dithiol + NADP(+) = [thioredoxin]-disulfide +
CC         NADPH + H(+); Xref=Rhea:RHEA:20345, Rhea:RHEA-COMP:10698, Rhea:RHEA-
CC         COMP:10700, ChEBI:CHEBI:15378, ChEBI:CHEBI:29950, ChEBI:CHEBI:50058,
CC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349; EC=1.8.1.9;
CC         Evidence={ECO:0000269|PubMed:39480878};
```

Source SHA-256: `ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
