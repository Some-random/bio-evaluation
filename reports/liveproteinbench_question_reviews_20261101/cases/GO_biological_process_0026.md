# GO_biological_process_0026

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — positive regulation of Ras protein signal transduction

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDRKRKLICDAFKVKKLRGSCSRDETDLKTSTSPYPDFTEDPHGAVSYLCALFPRKLFNDTLPPLFLKHQLYSLMQDRTVVDRLLSSLQQKGEVCLVQTGFDLDTFMVVMTDDLRRTALSSSEGDSRATVVRKFLDCDLLLSPNISYGRDEMMMKHRFSDGEITQLVRAGLLTVRDAGSWWLAVPGAGRFITHFIKGRKALLSQIRRSRYKEVLLTDLSTRKAPPNLRLGMEFHIHDIIGAGLVDCVPTASGILLRISET

[Multiple Choices]
A. negative regulation of microtubule depolymerization
B. positive regulation of Ras protein signal transduction
C. spermatogenesis
D. cytosolic mRNA polyadenylation
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

> The exact sequence matches a UniProt record annotated to positive regulation of Ras protein signal transduction (GO:0046579), including in the historical record. This is IBA evidence, a computational phylogenetic inference, not direct experimental confirmation. The record separately reports an experimentally supported TC-NER function, which is not among the choices.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The supplied sequence and choices do not provide a clear biological feature that distinguishes Ras signaling from the other listed processes.


**Missing item-specific fact**

> The sequence-specific GO annotation linking this protein to positive regulation of Ras protein signal transduction is needed to select B; that annotation is absent from the input.


**Reason**

> The key is supported by a sequence-matched database annotation, but that item-specific annotation is not inferable from the sequence and choices by a concrete general biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the only listed choice directly supported by the matched GO annotation. However, calling it the protein's primary process is not established by that annotation, and the reported experimentally supported TC-NER function is not offered as an option.


### Important caveats

- The Ras-process annotation is IBA (inferred from biological aspect of ancestor), not direct experimental evidence.
- The experimentally supported function described in the record is transcription-coupled nucleotide excision repair; it does not directly confirm or refute the Ras annotation.
- The author's exact source snapshot is unknown, though the sequence and the historical annotation match.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence and choices do not provide a clear biological feature that distinguishes Ras signaling from the other listed processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific GO annotation linking this protein to positive regulation of Ras protein signal transduction is needed to select B; that annotation is absent from the input.",
    "reason": "The key is supported by a sequence-matched database annotation, but that item-specific annotation is not inferable from the sequence and choices by a concrete general biological argument."
  },
  "case_id": "GO_biological_process_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated to positive regulation of Ras protein signal transduction (GO:0046579), including in the historical record. This is IBA evidence, a computational phylogenetic inference, not direct experimental confirmation. The record separately reports an experimentally supported TC-NER function, which is not among the choices."
  },
  "important_caveats": [
    "The Ras-process annotation is IBA (inferred from biological aspect of ancestor), not direct experimental evidence.",
    "The experimentally supported function described in the record is transcription-coupled nucleotide excision repair; it does not directly confirm or refute the Ras annotation.",
    "The author's exact source snapshot is unknown, though the sequence and the historical annotation match."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only listed choice directly supported by the matched GO annotation. However, calling it the protein's primary process is not established by that annotation, and the reported experimentally supported TC-NER function is not offered as an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated to positive regulation of Ras protein signal transduction (GO:0046579), including in the historical record. This is IBA evidence, a computational phylogenetic inference, not direct experimental confirmation. The record separately reports an experimentally supported TC-NER function, which is not among the choices.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The supplied sequence and choices do not provide a clear biological feature that distinguishes Ras signaling from the other listed processes.",
    "missing_item_specific_fact": "The sequence-specific GO annotation linking this protein to positive regulation of Ras protein signal transduction is needed to select B; that annotation is absent from the input.",
    "reason": "The key is supported by a sequence-matched database annotation, but that item-specific annotation is not inferable from the sequence and choices by a concrete general biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only listed choice directly supported by the matched GO annotation. However, calling it the protein's primary process is not established by that annotation, and the reported experimentally supported TC-NER function is not offered as an option."
  },
  "important_caveats": [
    "The Ras-process annotation is IBA (inferred from biological aspect of ancestor), not direct experimental evidence.",
    "The experimentally supported function described in the record is transcription-coupled nucleotide excision repair; it does not directly confirm or refute the Ras annotation.",
    "The author's exact source snapshot is unknown, though the sequence and the historical annotation match."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1L8F8I9 (WHR1/STK19 from Xenopus laevis) does carry GO:0046579 (positive regulation of Ras protein signal transduction) as a database annotation (evidence C6, H5). However, this annotation carries the evidence code IBA:GO_Central, meaning it is a computational inference propagated from orthologs via GO_Central, not an experimentally validated function. The experimentally validated function (ECO:0000269, PubMed 39547228) is transcription-coupled nucleotide excision repair (TC-NER), a DNA repair process. The expected answer is technically present in the annotation record but represents a low-confidence computational assignment that is contradicted by the primary experimental evidence.

Citations as saved: [C6](#evidence-c6), [H5](#evidence-h5), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No concrete biological argument can be constructed from the 260-aa sequence alone to distinguish 'positive regulation of Ras protein signal transduction' from the other three options. The sequence lacks recognizable Ras-pathway motifs (e.g., Ras-binding domains, SH2/SH3 domains, GEF/GAP catalytic cores). The protein's actual experimental function (TC-NER/DNA repair) is not among the choices. There is no domain architecture or sequence feature that would lead a reasoning model to prefer option B over A, C, or D.


**Missing item-specific fact**

> The specific database annotation linking this exact sequence (STK19/WHR1 from Xenopus laevis) to GO:0046579 via IBA:GO_Central. Without knowing the UniProt entry and its GO cross-references, the four options are indistinguishable from sequence features alone.


**Reason**

> Selecting the correct answer requires recognizing this specific protein and recalling its (low-confidence, computationally propagated) GO annotation. No general biological reasoning from the sequence distinguishes option B from A, C, or D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four options, none matches the experimentally validated primary function (TC-NER/DNA repair). Option B is the only one with any database annotation (albeit IBA:GO_Central, a low-confidence computational propagation). Options A, C, and D have no annotation support for this protein. While B is the 'least unsupported' choice, the question's premise of identifying a 'primary biological process' is undermined because the true primary process (DNA repair) is absent from the options.


### Important caveats

- The GO:0046579 annotation is IBA:GO_Central (computational inference from orthologs), not experimental evidence. The experimental evidence (PubMed 39547228, 2024) establishes TC-NER as the validated function.
- The protein is annotated as an 'Inactive serine/threonine-protein kinase 19' (STK19) but its kinase activity is inactive; its actual role is as a DNA-binding factor in TC-NER.
- The experimentally validated primary biological process (DNA repair / TC-NER, GO:0006281) is not offered as a choice, making the question's framing of 'primary biological process' problematic.
- The IBA:GO_Central annotation may reflect a secondary or indirect role in Ras signaling inferred from pathway associations in other organisms, not a direct experimentally demonstrated function of this Xenopus protein.
- The sequence is from Xenopus laevis (African clawed frog); the Ras signaling annotation was propagated from orthologs in other species.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No concrete biological argument can be constructed from the 260-aa sequence alone to distinguish 'positive regulation of Ras protein signal transduction' from the other three options. The sequence lacks recognizable Ras-pathway motifs (e.g., Ras-binding domains, SH2/SH3 domains, GEF/GAP catalytic cores). The protein's actual experimental function (TC-NER/DNA repair) is not among the choices. There is no domain architecture or sequence feature that would lead a reasoning model to prefer option B over A, C, or D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific database annotation linking this exact sequence (STK19/WHR1 from Xenopus laevis) to GO:0046579 via IBA:GO_Central. Without knowing the UniProt entry and its GO cross-references, the four options are indistinguishable from sequence features alone.",
    "reason": "Selecting the correct answer requires recognizing this specific protein and recalling its (low-confidence, computationally propagated) GO annotation. No general biological reasoning from the sequence distinguishes option B from A, C, or D."
  },
  "case_id": "GO_biological_process_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H5",
      "C5",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1L8F8I9 (WHR1/STK19 from Xenopus laevis) does carry GO:0046579 (positive regulation of Ras protein signal transduction) as a database annotation (evidence C6, H5). However, this annotation carries the evidence code IBA:GO_Central, meaning it is a computational inference propagated from orthologs via GO_Central, not an experimentally validated function. The experimentally validated function (ECO:0000269, PubMed 39547228) is transcription-coupled nucleotide excision repair (TC-NER), a DNA repair process. The expected answer is technically present in the annotation record but represents a low-confidence computational assignment that is contradicted by the primary experimental evidence."
  },
  "important_caveats": [
    "The GO:0046579 annotation is IBA:GO_Central (computational inference from orthologs), not experimental evidence. The experimental evidence (PubMed 39547228, 2024) establishes TC-NER as the validated function.",
    "The protein is annotated as an 'Inactive serine/threonine-protein kinase 19' (STK19) but its kinase activity is inactive; its actual role is as a DNA-binding factor in TC-NER.",
    "The experimentally validated primary biological process (DNA repair / TC-NER, GO:0006281) is not offered as a choice, making the question's framing of 'primary biological process' problematic.",
    "The IBA:GO_Central annotation may reflect a secondary or indirect role in Ras signaling inferred from pathway associations in other organisms, not a direct experimentally demonstrated function of this Xenopus protein.",
    "The sequence is from Xenopus laevis (African clawed frog); the Ras signaling annotation was propagated from orthologs in other species."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, none matches the experimentally validated primary function (TC-NER/DNA repair). Option B is the only one with any database annotation (albeit IBA:GO_Central, a low-confidence computational propagation). Options A, C, and D have no annotation support for this protein. While B is the 'least unsupported' choice, the question's premise of identifying a 'primary biological process' is undermined because the true primary process (DNA repair) is absent from the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1L8F8I9 (WHR1/STK19 from Xenopus laevis) does carry GO:0046579 (positive regulation of Ras protein signal transduction) as a database annotation (evidence C6, H5). However, this annotation carries the evidence code IBA:GO_Central, meaning it is a computational inference propagated from orthologs via GO_Central, not an experimentally validated function. The experimentally validated function (ECO:0000269, PubMed 39547228) is transcription-coupled nucleotide excision repair (TC-NER), a DNA repair process. The expected answer is technically present in the annotation record but represents a low-confidence computational assignment that is contradicted by the primary experimental evidence.",
    "evidence_ids": ["C6", "H5", "C5", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No concrete biological argument can be constructed from the 260-aa sequence alone to distinguish 'positive regulation of Ras protein signal transduction' from the other three options. The sequence lacks recognizable Ras-pathway motifs (e.g., Ras-binding domains, SH2/SH3 domains, GEF/GAP catalytic cores). The protein's actual experimental function (TC-NER/DNA repair) is not among the choices. There is no domain architecture or sequence feature that would lead a reasoning model to prefer option B over A, C, or D.",
    "missing_item_specific_fact": "The specific database annotation linking this exact sequence (STK19/WHR1 from Xenopus laevis) to GO:0046579 via IBA:GO_Central. Without knowing the UniProt entry and its GO cross-references, the four options are indistinguishable from sequence features alone.",
    "reason": "Selecting the correct answer requires recognizing this specific protein and recalling its (low-confidence, computationally propagated) GO annotation. No general biological reasoning from the sequence distinguishes option B from A, C, or D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, none matches the experimentally validated primary function (TC-NER/DNA repair). Option B is the only one with any database annotation (albeit IBA:GO_Central, a low-confidence computational propagation). Options A, C, and D have no annotation support for this protein. While B is the 'least unsupported' choice, the question's premise of identifying a 'primary biological process' is undermined because the true primary process (DNA repair) is absent from the options."
  },
  "important_caveats": [
    "The GO:0046579 annotation is IBA:GO_Central (computational inference from orthologs), not experimental evidence. The experimental evidence (PubMed 39547228, 2024) establishes TC-NER as the validated function.",
    "The protein is annotated as an 'Inactive serine/threonine-protein kinase 19' (STK19) but its kinase activity is inactive; its actual role is as a DNA-binding factor in TC-NER.",
    "The experimentally validated primary biological process (DNA repair / TC-NER, GO:0006281) is not offered as a choice, making the question's framing of 'primary biological process' problematic.",
    "The IBA:GO_Central annotation may reflect a secondary or indirect role in Ras signaling inferred from pathway associations in other organisms, not a direct experimentally demonstrated function of this Xenopus protein.",
    "The sequence is from Xenopus laevis (African clawed frog); the Ras signaling annotation was propagated from orthologs in other species."
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

**Accession:** `A0A1L8F8I9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1L8F8I9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:38.441901+00:00.  

```json
"A0A1L8F8I9"
```

Source SHA-256: `ad121addbcd5ab2ddb9a4d4104d154031c10f6b01c3d00ae1a3f60d2e7b4b482`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1L8F8I9.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:38.441901+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39547228","source":"PubMed"}],"value":"DNA-binding protein which is required for efficient transcription-coupled nucleotide excision repair (TC-NER). Acts as part of a TC-NER complex which assembles and interacts with RNA polymerase II (RNAPII) when it stalls at DNA lesions"}]}
```

Source SHA-256: `ad121addbcd5ab2ddb9a4d4104d154031c10f6b01c3d00ae1a3f60d2e7b4b482`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1L8F8I9.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:38.441901+00:00.  

```json
{"database":"GO","id":"GO:0046579","properties":[{"key":"GoTerm","value":"P:positive regulation of Ras protein signal transduction"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `ad121addbcd5ab2ddb9a4d4104d154031c10f6b01c3d00ae1a3f60d2e7b4b482`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1L8F8I9.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:38.441901+00:00.  

```json
{"citation":{"authors":["Mevissen T.E.T.","Kuemmecke M.","Schmid E.W.","Farnung L.","Walter J.C."],"citationCrossReferences":[{"database":"PubMed","id":"39547228"},{"database":"DOI","id":"10.1016/j.cell.2024.10.020"}],"citationType":"journal article","firstPage":"7091","id":"39547228","journal":"Cell","lastPage":"7106.e24","publicationDate":"2024","title":"STK19 positions TFIIH for cell-free transcription-coupled DNA repair.","volume":"187"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","IDENTIFICATION IN TC-NER COMPLEX","MUTAGENESIS OF 78-ARG--ARG-83; 82-ASP-ARG-83; 206-ARG-ARG-207; 209-ARG-TYR-210; ASP-217 AND 250-ALA-SER-251"]}
```

Source SHA-256: `ad121addbcd5ab2ddb9a4d4104d154031c10f6b01c3d00ae1a3f60d2e7b4b482`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1L8F8I9?format=txt&versions=32)  
**Locator:** `lines 46-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:42.652193+00:00.  

```text
CC   -!- FUNCTION: DNA-binding protein which is required for efficient
CC       transcription-coupled nucleotide excision repair (TC-NER). Acts as part
CC       of a TC-NER complex which assembles and interacts with RNA polymerase
CC       II (RNAPII) when it stalls at DNA lesions.
CC       {ECO:0000269|PubMed:39547228}.
```

Source SHA-256: `ebe39938ded0ac0ae49422b85786307a60b6a7afeabc2975efc8da71525f3fb4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1L8F8I9?format=txt&versions=32)  
**Locator:** `lines 84-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:42.652193+00:00.  

```text
DR   GO; GO:0006281; P:DNA repair; IEA:UniProtKB-KW.
```

Source SHA-256: `ebe39938ded0ac0ae49422b85786307a60b6a7afeabc2975efc8da71525f3fb4`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1L8F8I9?format=txt&versions=32)  
**Locator:** `lines 85-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:42.652193+00:00.  

```text
DR   GO; GO:0046579; P:positive regulation of Ras protein signal transduction; IBA:GO_Central.
```

Source SHA-256: `ebe39938ded0ac0ae49422b85786307a60b6a7afeabc2975efc8da71525f3fb4`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
