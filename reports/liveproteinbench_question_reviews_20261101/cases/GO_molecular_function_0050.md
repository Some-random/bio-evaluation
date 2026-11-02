# GO_molecular_function_0050

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — N6-methyladenosine-containing RNA reader activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGDAPLPPGSGKEFTQVQQQHNNYSNHQQQHAFASQYDMTQQQQPFGRGLSGPYNMGLMMHALPHPSYRPGQQQQHQYGSPPNTNGNAQPMPQAHGNNTMNSMPGPPQYYMQQQHGLPPQYYAQQMQGSQQQQQHQRGSMSPRANMALYQQPHTQGQQYYYPQGAQFPNHGPMPQNSMLAGPYPLASHMQHVDHRLAQRQVGDQRDVDNTEQSQPRVDGARFESQSNVVRGPPRKPRQSGHAIWIGNLPPQTDLMSLVYHVCKEAPGLESLFLISKSNCAFANFKDEEACISAQQKIHDSKFQTVRLVSRLRKSTVEGATGLTAPTGPAASAPQSNISQEVKGDALSVVTTTEDLIASSNVSSPKVTSPAPVETDRSAPQKEKYFILKSLTVEDLEQSIKTGIWATQAHNEKALNKAYETAESVYLIFSANKSGEYFGYARMTSQINEDPAAAVEFAPKAQAASDVALPKAIPTEANEYMPKGSIMDDSERGTIFWEADPPEDADGVDSNDTTTAAVADDTVSIKSCETGGPDSKVWGKPFQIEWLSVARLPFYRTRGIRNPWNSNREVKIARDGTELEPSVGRKLTGLFTSRGVGQLQQQPHPHHHHVMGGGMPMPGGMVHGYPPMYAQ

[Multiple Choices]
A. rRNA (uridine-N3-)-methyltransferase activity
B. snRNA methyltransferase activity
C. tetraketide alpha-pyrone synthase activity
D. N6-methyladenosine-containing RNA reader activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches UniProt entry G4MRQ6, which names the protein as a YTH-domain-containing family protein and annotates m6A-containing RNA reader activity. The functional description says it recognizes and binds m6A-containing mRNAs, but this specific activity is supported by similarity; the GO assignment is computational (IEA:TreeGrafter), not direct experimental evidence for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a low-complexity region and a more structured region, but the input does not provide a clear, general-purpose motif that establishes m6A recognition. Selecting D depends on identifying the structured region as a YTH domain and knowing its specific association with m6A-reader activity.


**Missing item-specific fact**

> That this sequence belongs to the YTH-domain reader family, whose members recognize m6A-containing RNA.


**Reason**

> The family assignment and its specific ligand recognition are not stated in the question. Without that protein-family fact or a domain annotation, the sequence and choices alone do not meaningfully distinguish D from the other specific activities.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence’s annotation supports D, and the alternatives describe distinct activities with no comparable support in the supplied sequence.


### Important caveats

- The reviewer-only database evidence supports the key but was not supplied to the evaluated model.
- The cited GO term is computationally assigned; the UniProt description attributes m6A recognition to similarity, while its cited experimental evidence concerns pathogenicity rather than direct demonstration of this protein’s RNA-binding activity.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a low-complexity region and a more structured region, but the input does not provide a clear, general-purpose motif that establishes m6A recognition. Selecting D depends on identifying the structured region as a YTH domain and knowing its specific association with m6A-reader activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence belongs to the YTH-domain reader family, whose members recognize m6A-containing RNA.",
    "reason": "The family assignment and its specific ligand recognition are not stated in the question. Without that protein-family fact or a domain annotation, the sequence and choices alone do not meaningfully distinguish D from the other specific activities."
  },
  "case_id": "GO_molecular_function_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry G4MRQ6, which names the protein as a YTH-domain-containing family protein and annotates m6A-containing RNA reader activity. The functional description says it recognizes and binds m6A-containing mRNAs, but this specific activity is supported by similarity; the GO assignment is computational (IEA:TreeGrafter), not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The reviewer-only database evidence supports the key but was not supplied to the evaluated model.",
    "The cited GO term is computationally assigned; the UniProt description attributes m6A recognition to similarity, while its cited experimental evidence concerns pathogenicity rather than direct demonstration of this protein’s RNA-binding activity.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence’s annotation supports D, and the alternatives describe distinct activities with no comparable support in the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry G4MRQ6, which names the protein as a YTH-domain-containing family protein and annotates m6A-containing RNA reader activity. The functional description says it recognizes and binds m6A-containing mRNAs, but this specific activity is supported by similarity; the GO assignment is computational (IEA:TreeGrafter), not direct experimental evidence for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a low-complexity region and a more structured region, but the input does not provide a clear, general-purpose motif that establishes m6A recognition. Selecting D depends on identifying the structured region as a YTH domain and knowing its specific association with m6A-reader activity.",
    "missing_item_specific_fact": "That this sequence belongs to the YTH-domain reader family, whose members recognize m6A-containing RNA.",
    "reason": "The family assignment and its specific ligand recognition are not stated in the question. Without that protein-family fact or a domain annotation, the sequence and choices alone do not meaningfully distinguish D from the other specific activities."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence’s annotation supports D, and the alternatives describe distinct activities with no comparable support in the supplied sequence."
  },
  "important_caveats": [
    "The reviewer-only database evidence supports the key but was not supplied to the evaluated model.",
    "The cited GO term is computationally assigned; the UniProt description attributes m6A recognition to similarity, while its cited experimental evidence concerns pathogenicity rather than direct demonstration of this protein’s RNA-binding activity.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G4MRQ6 (YTH1_PYRO7) is annotated with GO:1990247 'N6-methyladenosine-containing RNA reader activity' (evidence IEA:TreeGrafter, C7/H5). The protein is named 'YTH domain-containing family protein 1' / 'M6A reader YTH1' (C4). The FUNCTION comment states it 'specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs' (C5/H3), with the m6A recognition part annotated by similarity (ECO:0000250) and the pathogenicity role supported by PubMed:30535195 (ECO:0000269). The sequence matches the entry exactly (630 AA, SHA256 confirmed). The GO term definition (GO4) aligns with the option text. Note: the specific m6A-reader molecular function annotation is computational (TreeGrafter/By similarity) rather than direct experimental evidence for this particular protein, but the annotation is consistent and the PubMed reference supports the m6A pathway involvement.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly argue by elimination: the sequence lacks recognizable Rossmann-fold/SAM-binding motifs expected for methyltransferases (eliminating A and B) and lacks polyketide synthase domain architecture (eliminating C), leaving D by default. However, this negative reasoning from a 630-aa sequence dominated by low-complexity regions (QQQ, PPP, N-rich stretches) is unreliable for motif absence arguments, and the positive identification of the YTH domain as an m6A reader requires knowing the YTH domain consensus sequence and its specific association with m6A recognition.


**Missing item-specific fact**

> The specific identification of the YTH domain within this sequence and its established role as an m6A-binding adaptor. The YTH domain consensus motifs and their correspondence to m6A recognition are item-specific knowledge not derivable from general biological reasoning about the raw sequence, which is heavily interspersed with low-complexity regions that obscure domain boundaries.


**Reason**

> The sequence provides no obvious catalytic motifs for methyltransferase or polyketide synthase activity, but positively identifying the m6A reader function requires recognizing the YTH domain from sequence, which is essentially memorizing a protein-family consensus. The instructions state that recognizing a sequence and recalling its database entry does not constitute reasoning. The elimination-based argument (no methyltransferase motifs → not A/B; no PKS domains → not C) is too weak given the low-complexity nature of the sequence to constitute 'meaningful grounds' for distinguishing the answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular functions (two methyltransferases, one polyketide synthase, one adaptor/binding protein). The YTH domain is structurally and functionally distinct from all three catalytic options. There is no realistic ambiguity among the choices given the protein's identity.


### Important caveats

- The GO:1990247 annotation carries evidence code IEA:TreeGrafter (computational transfer), not direct experimental evidence for this specific protein. The m6A recognition function is annotated 'By similarity' (ECO:0000250).
- The PubMed:30535195 reference (Shi et al., 2019) provides experimental evidence for m6A pathway involvement in pathogenicity but the molecular function annotation itself is transferred.
- The sequence is 630 AA with extensive low-complexity regions (poly-Q, poly-P, N-rich), making de novo domain identification from raw sequence particularly difficult.
- The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot date is unknown but the sequence version has been stable since 2011.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly argue by elimination: the sequence lacks recognizable Rossmann-fold/SAM-binding motifs expected for methyltransferases (eliminating A and B) and lacks polyketide synthase domain architecture (eliminating C), leaving D by default. However, this negative reasoning from a 630-aa sequence dominated by low-complexity regions (QQQ, PPP, N-rich stretches) is unreliable for motif absence arguments, and the positive identification of the YTH domain as an m6A reader requires knowing the YTH domain consensus sequence and its specific association with m6A recognition.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of the YTH domain within this sequence and its established role as an m6A-binding adaptor. The YTH domain consensus motifs and their correspondence to m6A recognition are item-specific knowledge not derivable from general biological reasoning about the raw sequence, which is heavily interspersed with low-complexity regions that obscure domain boundaries.",
    "reason": "The sequence provides no obvious catalytic motifs for methyltransferase or polyketide synthase activity, but positively identifying the m6A reader function requires recognizing the YTH domain from sequence, which is essentially memorizing a protein-family consensus. The instructions state that recognizing a sequence and recalling its database entry does not constitute reasoning. The elimination-based argument (no methyltransferase motifs → not A/B; no PKS domains → not C) is too weak given the low-complexity nature of the sequence to constitute 'meaningful grounds' for distinguishing the answer."
  },
  "case_id": "GO_molecular_function_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H3",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G4MRQ6 (YTH1_PYRO7) is annotated with GO:1990247 'N6-methyladenosine-containing RNA reader activity' (evidence IEA:TreeGrafter, C7/H5). The protein is named 'YTH domain-containing family protein 1' / 'M6A reader YTH1' (C4). The FUNCTION comment states it 'specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs' (C5/H3), with the m6A recognition part annotated by similarity (ECO:0000250) and the pathogenicity role supported by PubMed:30535195 (ECO:0000269). The sequence matches the entry exactly (630 AA, SHA256 confirmed). The GO term definition (GO4) aligns with the option text. Note: the specific m6A-reader molecular function annotation is computational (TreeGrafter/By similarity) rather than direct experimental evidence for this particular protein, but the annotation is consistent and the PubMed reference supports the m6A pathway involvement."
  },
  "important_caveats": [
    "The GO:1990247 annotation carries evidence code IEA:TreeGrafter (computational transfer), not direct experimental evidence for this specific protein. The m6A recognition function is annotated 'By similarity' (ECO:0000250).",
    "The PubMed:30535195 reference (Shi et al., 2019) provides experimental evidence for m6A pathway involvement in pathogenicity but the molecular function annotation itself is transferred.",
    "The sequence is 630 AA with extensive low-complexity regions (poly-Q, poly-P, N-rich), making de novo domain identification from raw sequence particularly difficult.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot date is unknown but the sequence version has been stable since 2011."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular functions (two methyltransferases, one polyketide synthase, one adaptor/binding protein). The YTH domain is structurally and functionally distinct from all three catalytic options. There is no realistic ambiguity among the choices given the protein's identity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G4MRQ6 (YTH1_PYRO7) is annotated with GO:1990247 'N6-methyladenosine-containing RNA reader activity' (evidence IEA:TreeGrafter, C7/H5). The protein is named 'YTH domain-containing family protein 1' / 'M6A reader YTH1' (C4). The FUNCTION comment states it 'specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs' (C5/H3), with the m6A recognition part annotated by similarity (ECO:0000250) and the pathogenicity role supported by PubMed:30535195 (ECO:0000269). The sequence matches the entry exactly (630 AA, SHA256 confirmed). The GO term definition (GO4) aligns with the option text. Note: the specific m6A-reader molecular function annotation is computational (TreeGrafter/By similarity) rather than direct experimental evidence for this particular protein, but the annotation is consistent and the PubMed reference supports the m6A pathway involvement.",
    "evidence_ids": ["C4", "C5", "C7", "H3", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly argue by elimination: the sequence lacks recognizable Rossmann-fold/SAM-binding motifs expected for methyltransferases (eliminating A and B) and lacks polyketide synthase domain architecture (eliminating C), leaving D by default. However, this negative reasoning from a 630-aa sequence dominated by low-complexity regions (QQQ, PPP, N-rich stretches) is unreliable for motif absence arguments, and the positive identification of the YTH domain as an m6A reader requires knowing the YTH domain consensus sequence and its specific association with m6A recognition.",
    "missing_item_specific_fact": "The specific identification of the YTH domain within this sequence and its established role as an m6A-binding adaptor. The YTH domain consensus motifs and their correspondence to m6A recognition are item-specific knowledge not derivable from general biological reasoning about the raw sequence, which is heavily interspersed with low-complexity regions that obscure domain boundaries.",
    "reason": "The sequence provides no obvious catalytic motifs for methyltransferase or polyketide synthase activity, but positively identifying the m6A reader function requires recognizing the YTH domain from sequence, which is essentially memorizing a protein-family consensus. The instructions state that recognizing a sequence and recalling its database entry does not constitute reasoning. The elimination-based argument (no methyltransferase motifs → not A/B; no PKS domains → not C) is too weak given the low-complexity nature of the sequence to constitute 'meaningful grounds' for distinguishing the answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular functions (two methyltransferases, one polyketide synthase, one adaptor/binding protein). The YTH domain is structurally and functionally distinct from all three catalytic options. There is no realistic ambiguity among the choices given the protein's identity."
  },
  "important_caveats": [
    "The GO:1990247 annotation carries evidence code IEA:TreeGrafter (computational transfer), not direct experimental evidence for this specific protein. The m6A recognition function is annotated 'By similarity' (ECO:0000250).",
    "The PubMed:30535195 reference (Shi et al., 2019) provides experimental evidence for m6A pathway involvement in pathogenicity but the molecular function annotation itself is transferred.",
    "The sequence is 630 AA with extensive low-complexity regions (poly-Q, poly-P, N-rich), making de novo domain identification from raw sequence particularly difficult.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot date is unknown but the sequence version has been stable since 2011."
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

**Accession:** `G4MRQ6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 50. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:40.980195+00:00.  

```json
"G4MRQ6"
```

Source SHA-256: `1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:40.980195+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"M6A reader YTH1"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30535195","source":"PubMed"}],"value":"YTH domain-containing family protein 1"}}}
```

Source SHA-256: `1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:40.980195+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A9P4XWM4","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"30535195","source":"PubMed"}],"value":"Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs, and regulates their stability (By similarity). M6A is a modification present at internal sites of mRNAs and some non-coding RNAs and plays a role in mRNA stability and processing (By similarity). Plays a role in pathogenicity towards plant host (PubMed:30535195)"}]}
```

Source SHA-256: `1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:40.980195+00:00.  

```json
{"database":"GO","id":"GO:1990247","properties":[{"key":"GoTerm","value":"F:N6-methyladenosine-containing RNA reader activity"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50)  
**Locator:** `lines 33-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-02T04:28:43.231635+00:00.  

```text
CC   -!- FUNCTION: Specifically recognizes and binds N6-methyladenosine (m6A)-
CC       containing mRNAs, and regulates their stability (By similarity). M6A is
CC       a modification present at internal sites of mRNAs and some non-coding
CC       RNAs and plays a role in mRNA stability and processing (By similarity).
CC       Plays a role in pathogenicity towards plant host (PubMed:30535195).
CC       {ECO:0000250|UniProtKB:A0A9P4XWM4, ECO:0000269|PubMed:30535195}.
```

Source SHA-256: `0e3fd045231c72df6a89528c9ea84aac218d1c347b0c4633352bdbffaaf288d9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50)  
**Locator:** `lines 69-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-02T04:28:43.231635+00:00.  

```text
DR   GO; GO:1990247; F:N6-methyladenosine-containing RNA reader activity; IEA:TreeGrafter.
```

Source SHA-256: `0e3fd045231c72df6a89528c9ea84aac218d1c347b0c4633352bdbffaaf288d9`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 550531-550538`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1990247
name: N6-methyladenosine-containing RNA reader activity
namespace: molecular_function
def: "A protein adaptor that recognizes and binds an RNA molecule modified by N6-methyladenosine (m6A), a modification present at internal sites of mRNAs and some non-coding RNAs." [PMID:22575960, PMID:24284625]
synonym: "N6-methyladenosine-containing RNA binding" RELATED []
is_a: GO:0140517 ! protein-RNA adaptor activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
