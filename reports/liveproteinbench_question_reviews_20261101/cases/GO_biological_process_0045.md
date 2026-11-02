# GO_biological_process_0045

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — regulation of transcription by RNA polymerase II

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLTDRVLATKEALVVALGDNWERYRANMKNWFRSRWTKEEFDAESRKILTPDKLHLHNQFLLALLNKIDAFAPLENPPAVQTSSSSGNRSKRRKRSSRTFAERLNFELSDVLDFVAEDNMQIIRPPTTIGIPSDQQQQQLQSQRYCAQELFLPDAGFIMGRFLIGAWEIGLVSVDDNVAEYVAMAVQVLLKDLLSAIIKKRKHYKTSGEGNFYYDVGAPLRDPSLRNTVTRQKVDDTPLELDKELNTANFMRRQNDDVTFLSACEEVQPTERTVITLKDCQLALRDRNLIGSHAVYSINMERLNMMMH

[Multiple Choices]
A. regulation of transcription by RNA polymerase II
B. negative regulation of protein catabolic process
C. mitotic DNA damage checkpoint signaling
D. modulation of process of another organism
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

> The exact sequence match is annotated for regulation of transcription by RNA polymerase II (GO:0006357). The cited functional annotation describes this protein as a SAGA-complex component, and reports support from published studies of SAGA-mediated transcriptional activation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Knowing that a SAGA-complex component participates in transcription regulation would favor A, but that protein-specific functional identity is not established by the supplied sequence and choices alone.


**Missing item-specific fact**

> The sequence's identity as Drosophila Ada1-2, a SAGA-complex component, or equivalent protein-specific evidence linking it to transcription regulation.


**Reason**

> The sequence does not provide a sufficiently distinctive, self-evident basis for choosing this specific biological process over the alternatives without recognizing the protein or using external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports option A; no evidence supplied here supports another listed choice as a comparably defensible process.


### Important caveats

- The GO annotation for A is IBA (inferred from biological aspect of ancestor), not a direct experimental GO evidence code.
- The functional description has experimental evidence codes and cites studies, but those studies were not independently reviewed here.
- Reviewer-only sequence identity and annotations were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Knowing that a SAGA-complex component participates in transcription regulation would favor A, but that protein-specific functional identity is not established by the supplied sequence and choices alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's identity as Drosophila Ada1-2, a SAGA-complex component, or equivalent protein-specific evidence linking it to transcription regulation.",
    "reason": "The sequence does not provide a sufficiently distinctive, self-evident basis for choosing this specific biological process over the alternatives without recognizing the protein or using external annotation."
  },
  "case_id": "GO_biological_process_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated for regulation of transcription by RNA polymerase II (GO:0006357). The cited functional annotation describes this protein as a SAGA-complex component, and reports support from published studies of SAGA-mediated transcriptional activation."
  },
  "important_caveats": [
    "The GO annotation for A is IBA (inferred from biological aspect of ancestor), not a direct experimental GO evidence code.",
    "The functional description has experimental evidence codes and cites studies, but those studies were not independently reviewed here.",
    "Reviewer-only sequence identity and annotations were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports option A; no evidence supplied here supports another listed choice as a comparably defensible process."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated for regulation of transcription by RNA polymerase II (GO:0006357). The cited functional annotation describes this protein as a SAGA-complex component, and reports support from published studies of SAGA-mediated transcriptional activation.",
    "evidence_ids": ["C1", "C5", "C7", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Knowing that a SAGA-complex component participates in transcription regulation would favor A, but that protein-specific functional identity is not established by the supplied sequence and choices alone.",
    "missing_item_specific_fact": "The sequence's identity as Drosophila Ada1-2, a SAGA-complex component, or equivalent protein-specific evidence linking it to transcription regulation.",
    "reason": "The sequence does not provide a sufficiently distinctive, self-evident basis for choosing this specific biological process over the alternatives without recognizing the protein or using external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports option A; no evidence supplied here supports another listed choice as a comparably defensible process."
  },
  "important_caveats": [
    "The GO annotation for A is IBA (inferred from biological aspect of ancestor), not a direct experimental GO evidence code.",
    "The functional description has experimental evidence codes and cites studies, but those studies were not independently reviewed here.",
    "Reviewer-only sequence identity and annotations were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q8IPA1 (TAD12_DROME), named 'Transcriptional adapter 1-2' (Ada1-2), a Drosophila SAGA complex subunit. The FUNCTION comment (C5, H6) with ECO:0000269 experimental evidence states it is a component of the SAGA multiprotein complex that activates transcription by remodeling chromatin and mediating histone acetylation/deubiquitination. The specific GO term GO:0006357 'regulation of transcription by RNA polymerase II' is annotated (C7, H7) with IBA:GO_Central evidence (curatorial inference from the SAGA complex annotation). SAGA is a well-established RNA Pol II transcription coactivator, so the assignment is scientifically sound, though the direct evidence for this specific protein's role in Pol II transcription is inferential from complex membership rather than protein-specific experiments.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H6](#evidence-h6), [H7](#evidence-h7), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains WD40-like repeats and a basic region (SKRRKRSSR) suggestive of a nuclear scaffolding/adaptor protein, and lacks kinase, protease, or DNA-binding domains. These features weakly disfavour B (protease inhibitors/E3 regulators), C (checkpoint kinases like ATM/ATR/Mec1), and D (secreted/pathogenicity effectors). However, WD40 repeats are ubiquitous across transcription, DNA damage, and proteostasis proteins, so they cannot specifically single out 'regulation of transcription by RNA polymerase II' over the other nuclear processes. No sequence motif uniquely identifies SAGA membership or Ada1-2 identity.


**Missing item-specific fact**

> The specific identification of this sequence as Ada1-2, a SAGA complex subunit, and the knowledge that SAGA is a Pol II transcription coactivator. This requires recognizing the protein from a database or literature rather than deriving the process from general sequence features.


**Reason**

> While generic features (WD40 repeats, nuclear basic residues, absence of enzymatic domains) can eliminate some distractors (especially D), they cannot positively and uniquely assign the protein to Pol II transcription regulation rather than to DNA damage checkpoint or protein catabolism regulation. The definitive link to SAGA/transcription requires item-specific knowledge of this protein's identity and complex membership.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GO annotation GO:0006357 is present in the UniProt entry and matches option A exactly. No other option appears as an annotation for this protein. The SAGA complex function is unambiguously transcriptional, making A the only defensible choice given the correct protein identification.


### Important caveats

- The GO:0006357 annotation carries IBA:GO_Central evidence (curatorial inference from SAGA complex annotation), not direct experimental evidence for Ada1-2 specifically. However, multiple PubMed references (16980620, 21764853, 24493646, 30559249) with ECO:0000269 confirm SAGA's role in transcription activation.
- The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. The sequence itself has been in databases since 2003 (sequence version 1).
- The accession Q8IPA1 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence.
- Drosophila Ada1-2 is the ortholog of yeast Ada1 and human ADA2B; its SAGA membership is well-characterized experimentally in Drosophila.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains WD40-like repeats and a basic region (SKRRKRSSR) suggestive of a nuclear scaffolding/adaptor protein, and lacks kinase, protease, or DNA-binding domains. These features weakly disfavour B (protease inhibitors/E3 regulators), C (checkpoint kinases like ATM/ATR/Mec1), and D (secreted/pathogenicity effectors). However, WD40 repeats are ubiquitous across transcription, DNA damage, and proteostasis proteins, so they cannot specifically single out 'regulation of transcription by RNA polymerase II' over the other nuclear processes. No sequence motif uniquely identifies SAGA membership or Ada1-2 identity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this sequence as Ada1-2, a SAGA complex subunit, and the knowledge that SAGA is a Pol II transcription coactivator. This requires recognizing the protein from a database or literature rather than deriving the process from general sequence features.",
    "reason": "While generic features (WD40 repeats, nuclear basic residues, absence of enzymatic domains) can eliminate some distractors (especially D), they cannot positively and uniquely assign the protein to Pol II transcription regulation rather than to DNA damage checkpoint or protein catabolism regulation. The definitive link to SAGA/transcription requires item-specific knowledge of this protein's identity and complex membership."
  },
  "case_id": "GO_biological_process_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H6",
      "H7",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q8IPA1 (TAD12_DROME), named 'Transcriptional adapter 1-2' (Ada1-2), a Drosophila SAGA complex subunit. The FUNCTION comment (C5, H6) with ECO:0000269 experimental evidence states it is a component of the SAGA multiprotein complex that activates transcription by remodeling chromatin and mediating histone acetylation/deubiquitination. The specific GO term GO:0006357 'regulation of transcription by RNA polymerase II' is annotated (C7, H7) with IBA:GO_Central evidence (curatorial inference from the SAGA complex annotation). SAGA is a well-established RNA Pol II transcription coactivator, so the assignment is scientifically sound, though the direct evidence for this specific protein's role in Pol II transcription is inferential from complex membership rather than protein-specific experiments."
  },
  "important_caveats": [
    "The GO:0006357 annotation carries IBA:GO_Central evidence (curatorial inference from SAGA complex annotation), not direct experimental evidence for Ada1-2 specifically. However, multiple PubMed references (16980620, 21764853, 24493646, 30559249) with ECO:0000269 confirm SAGA's role in transcription activation.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. The sequence itself has been in databases since 2003 (sequence version 1).",
    "The accession Q8IPA1 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence.",
    "Drosophila Ada1-2 is the ortholog of yeast Ada1 and human ADA2B; its SAGA membership is well-characterized experimentally in Drosophila."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GO annotation GO:0006357 is present in the UniProt entry and matches option A exactly. No other option appears as an annotation for this protein. The SAGA complex function is unambiguously transcriptional, making A the only defensible choice given the correct protein identification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q8IPA1 (TAD12_DROME), named 'Transcriptional adapter 1-2' (Ada1-2), a Drosophila SAGA complex subunit. The FUNCTION comment (C5, H6) with ECO:0000269 experimental evidence states it is a component of the SAGA multiprotein complex that activates transcription by remodeling chromatin and mediating histone acetylation/deubiquitination. The specific GO term GO:0006357 'regulation of transcription by RNA polymerase II' is annotated (C7, H7) with IBA:GO_Central evidence (curatorial inference from the SAGA complex annotation). SAGA is a well-established RNA Pol II transcription coactivator, so the assignment is scientifically sound, though the direct evidence for this specific protein's role in Pol II transcription is inferential from complex membership rather than protein-specific experiments.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H6", "H7", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains WD40-like repeats and a basic region (SKRRKRSSR) suggestive of a nuclear scaffolding/adaptor protein, and lacks kinase, protease, or DNA-binding domains. These features weakly disfavour B (protease inhibitors/E3 regulators), C (checkpoint kinases like ATM/ATR/Mec1), and D (secreted/pathogenicity effectors). However, WD40 repeats are ubiquitous across transcription, DNA damage, and proteostasis proteins, so they cannot specifically single out 'regulation of transcription by RNA polymerase II' over the other nuclear processes. No sequence motif uniquely identifies SAGA membership or Ada1-2 identity.",
    "missing_item_specific_fact": "The specific identification of this sequence as Ada1-2, a SAGA complex subunit, and the knowledge that SAGA is a Pol II transcription coactivator. This requires recognizing the protein from a database or literature rather than deriving the process from general sequence features.",
    "reason": "While generic features (WD40 repeats, nuclear basic residues, absence of enzymatic domains) can eliminate some distractors (especially D), they cannot positively and uniquely assign the protein to Pol II transcription regulation rather than to DNA damage checkpoint or protein catabolism regulation. The definitive link to SAGA/transcription requires item-specific knowledge of this protein's identity and complex membership."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GO annotation GO:0006357 is present in the UniProt entry and matches option A exactly. No other option appears as an annotation for this protein. The SAGA complex function is unambiguously transcriptional, making A the only defensible choice given the correct protein identification."
  },
  "important_caveats": [
    "The GO:0006357 annotation carries IBA:GO_Central evidence (curatorial inference from SAGA complex annotation), not direct experimental evidence for Ada1-2 specifically. However, multiple PubMed references (16980620, 21764853, 24493646, 30559249) with ECO:0000269 confirm SAGA's role in transcription activation.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. The sequence itself has been in databases since 2003 (sequence version 1).",
    "The accession Q8IPA1 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence.",
    "Drosophila Ada1-2 is the ortholog of yeast Ada1 and human ADA2B; its SAGA membership is well-characterized experimentally in Drosophila."
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

**Accession:** `Q8IPA1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 169. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:17.256572+00:00.  

```json
"Q8IPA1"
```

Source SHA-256: `40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:17.256572+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0051866","source":"FlyBase"}],"value":"Transcriptional adapter 1-2"}}}
```

Source SHA-256: `40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:17.256572+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16980620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21764853","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24493646","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30559249","source":"PubMed"}],"value":"Component of the transcription regulatory complex SAGA, a multiprotein complex that activates transcription by remodeling chromatin and mediating histone acetylation and deubiquitination (PubMed:16980620, PubMed:21764853, PubMed:24493646, PubMed:30559249). The SAGA complex predominantly acetylates histone H3 (PubMed:30559249)"}]}
```

Source SHA-256: `40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)  
**Locator:** `/uniProtKBCrossReferences/30`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:17.256572+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000303","id":"33004486","source":"PubMed"}],"id":"GO:0045893","properties":[{"key":"GoTerm","value":"P:positive regulation of DNA-templated transcription"},{"key":"GoEvidenceType","value":"NAS:ComplexPortal"}]}
```

Source SHA-256: `40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)  
**Locator:** `/uniProtKBCrossReferences/31`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:17.256572+00:00.  

```json
{"database":"GO","id":"GO:0006357","properties":[{"key":"GoTerm","value":"P:regulation of transcription by RNA polymerase II"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)  
**Locator:** `lines 111-117`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 169 / 1.  
**Retrieved:** 2026-11-02T04:32:22.664157+00:00.  

```text
CC   -!- FUNCTION: Component of the transcription regulatory complex SAGA, a
CC       multiprotein complex that activates transcription by remodeling
CC       chromatin and mediating histone acetylation and deubiquitination
CC       (PubMed:16980620, PubMed:21764853, PubMed:24493646, PubMed:30559249).
CC       The SAGA complex predominantly acetylates histone H3 (PubMed:30559249).
CC       {ECO:0000269|PubMed:16980620, ECO:0000269|PubMed:21764853,
CC       ECO:0000269|PubMed:24493646, ECO:0000269|PubMed:30559249}.
```

Source SHA-256: `87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)  
**Locator:** `lines 169-169`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 169 / 1.  
**Retrieved:** 2026-11-02T04:32:22.664157+00:00.  

```text
DR   GO; GO:0006357; P:regulation of transcription by RNA polymerase II; IBA:GO_Central.
```

Source SHA-256: `87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 65427-65443`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0006357
name: regulation of transcription by RNA polymerase II
namespace: biological_process
alt_id: GO:0006358
alt_id: GO:0010551
def: "Any process that modulates the frequency, rate or extent of transcription mediated by RNA polymerase II." [GOC:curators, GOC:txnOH]
synonym: "global transcription regulation from Pol II promoter" RELATED []
synonym: "regulation of gene-specific transcription from RNA polymerase II promoter" RELATED []
synonym: "regulation of global transcription from Pol II promoter" RELATED []
synonym: "regulation of transcription from Pol II promoter" EXACT []
synonym: "regulation of transcription from RNA polymerase II promoter" EXACT []
synonym: "regulation of transcription from RNA polymerase II promoter, global" RELATED []
xref: Reactome:R-HSA-8864260 "Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors"
is_a: GO:0006355 ! regulation of DNA-templated transcription
relationship: regulates GO:0006366 ! transcription by RNA polymerase II

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
