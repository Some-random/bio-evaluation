# GO_biological_process_0166

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — regulation of protein K48-linked ubiquitination

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSRRALRRLRGEQRGQEPLGPDALQFVLLDDDDAEEEGPKTGLGGRRPGGAGKEGVRVNNRFELINIEDLEDDLVVNGERSDCTLPDSASSGNKGRAKHGNPENKQDGDAAAKAGSSEQSNASGKLRKKKKKQKNKKSCTGESSENGLEDIDRILERIEDSSGFSHPGPPPLSSRKHVLYVEHRHLNPDTELKRYFGARAVLGEQRPRQRQRVYPKCTWLTTPKSTWPRYSKPGLSMRLLESKKGLSFFAFEHSEEYQQAQHKFLVAVESMEPNNIVALLQTSPYHVDSLLQLSDACRFQEDQEMARDLIGEPAYPHLLPMEKSWCRRPHWSFYLALYKQMSFLEKRGCPRTALEYCKLILSLEPDEDPLCMLLLIDHMALRARNYEYLIRLFQEWEAHRNLSQLPNFAFSVPLAYFLLSQQTDLPDHELSSARQQASLLIQQALTMFPGVLMPLLEYCSVRPDATVSNHRFFGPDAEISQPPALSQLVSLYLGRSHFLWKEPAIMSWLEENVHEVLEAVDSGDPAVEACENRRKVLYQRAPRNIHRHVILSEIKEAVAALPSDVTTQSVMGFDPLPPVDTIYSYVRPERLSPVSHGNTIALFFRSLLPNYTTEGERLEEGVAGGPNRNQGLNRLMLAVRDMMANFHFNDLEVPREDNPEGEGDWD

[Multiple Choices]
A. carboxylic acid metabolic process
B. innate immune response
C. regulation of protein K48-linked ubiquitination
D. regulated exocytosis
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

> The exact sequence matches rat TCF25. Its annotation says it promotes formation of K48-linked polyubiquitin chains in the ribosome quality control complex, and assigns the matching GO process. This supports C, though the RQC role is stated as by similarity and the GO annotation is ISO:RGD, not direct experimental evidence for this exact sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a clear general biological feature that identifies regulation of K48-linked ubiquitination over the other listed processes.


**Missing item-specific fact**

> The needed fact is the protein-specific identification and functional annotation of this sequence as TCF25, a ribosome quality control complex component that promotes K48-linked ubiquitination.


**Reason**

> The key is supported by sequence-matched annotation, but that annotation and protein-specific function are absent from the question input. Inferring the option requires external identification or remembered knowledge of this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the sequence-matched annotation specifically supports C; the supplied evidence does not identify the other options as functions of this protein.


### Important caveats

- The matching GO annotation is based on ISO:RGD, and the RQC/K48-linked function is described as by similarity; do not treat it as direct experimental proof for this rat sequence.
- The source annotation snapshot available to the original author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a clear general biological feature that identifies regulation of K48-linked ubiquitination over the other listed processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The needed fact is the protein-specific identification and functional annotation of this sequence as TCF25, a ribosome quality control complex component that promotes K48-linked ubiquitination.",
    "reason": "The key is supported by sequence-matched annotation, but that annotation and protein-specific function are absent from the question input. Inferring the option requires external identification or remembered knowledge of this protein."
  },
  "case_id": "GO_biological_process_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches rat TCF25. Its annotation says it promotes formation of K48-linked polyubiquitin chains in the ribosome quality control complex, and assigns the matching GO process. This supports C, though the RQC role is stated as by similarity and the GO annotation is ISO:RGD, not direct experimental evidence for this exact sequence."
  },
  "important_caveats": [
    "The matching GO annotation is based on ISO:RGD, and the RQC/K48-linked function is described as by similarity; do not treat it as direct experimental proof for this rat sequence.",
    "The source annotation snapshot available to the original author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence-matched annotation specifically supports C; the supplied evidence does not identify the other options as functions of this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches rat TCF25. Its annotation says it promotes formation of K48-linked polyubiquitin chains in the ribosome quality control complex, and assigns the matching GO process. This supports C, though the RQC role is stated as by similarity and the GO annotation is ISO:RGD, not direct experimental evidence for this exact sequence.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a clear general biological feature that identifies regulation of K48-linked ubiquitination over the other listed processes.",
    "missing_item_specific_fact": "The needed fact is the protein-specific identification and functional annotation of this sequence as TCF25, a ribosome quality control complex component that promotes K48-linked ubiquitination.",
    "reason": "The key is supported by sequence-matched annotation, but that annotation and protein-specific function are absent from the question input. Inferring the option requires external identification or remembered knowledge of this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence-matched annotation specifically supports C; the supplied evidence does not identify the other options as functions of this protein."
  },
  "important_caveats": [
    "The matching GO annotation is based on ISO:RGD, and the RQC/K48-linked function is described as by similarity; do not treat it as direct experimental proof for this rat sequence.",
    "The source annotation snapshot available to the original author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A8I6ASZ5 (TCF25_RAT, 666 aa, sequence SHA256 confirmed). The UniProt entry carries GO:0061945 (regulation of protein K48-linked ubiquitination) with evidence code ISO:RGD, and the FUNCTION comment explicitly states the protein is 'required to promote formation of Lys-48-linked polyubiquitin chains during ubiquitination of incompletely synthesized proteins by LTN1.' The annotation and function description are consistent with the expected answer. However, the evidence is inferred-by-similarity (ISO:RGD, 'By similarity' in the function text), not direct experimental validation for this specific rat protein; the only PubMed reference (32805187) concerns NFATC4 suppression, not K48 ubiquitination.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> None identifiable from the sequence alone. The 666-aa sequence lacks recognizable catalytic or structural motifs (no RING/U-box domains, no ubiquitin-conjugating enzyme fold, no SNARE motifs, no immune-receptor domains, no carboxylic-acid-metabolism enzyme motifs). Basic N-terminal stretches (RRKKKKQKNKK) could suggest a nuclear localization signal, but this is too generic to favor K48-linked ubiquitination over the other three options. TCF25/NULP1 is an obscure RQC-complex subunit without widely recognized domain signatures.


**Missing item-specific fact**

> The specific identification of this sequence as TCF25/NULP1, a ribosome-quality-control-complex subunit that promotes Lys-48 polyubiquitin chain formation during LTN1-mediated ubiquitination of nascent chains, together with the associated GO:0061945 annotation (ISO:RGD). This protein-specific annotation is not derivable from sequence motifs or general biological reasoning.


**Reason**

> The sequence contains no distinctive, widely recognized domains that would allow a knowledgeable biologist to reason from general principles to 'regulation of protein K48-linked ubiquitination' as opposed to the other three options. Correct selection depends on recognizing or looking up this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt entry annotates GO:0061945 and GO:0072344 (rescue of stalled ribosome) for this protein. Neither GO:0072344 nor any term corresponding to options A, B, or D appears in the annotation. Among the four provided choices, only C matches an annotated GO term, so the options are distinguishable once the correct annotation is known.


### Important caveats

- The GO annotation evidence code is ISO:RGD (inferred by similarity via RGD), and the function text qualifies the RQC/ubiquitination role as 'By similarity.' Direct experimental evidence for K48-linked ubiquitination regulation by this specific rat protein is not present in the supplied evidence.
- The accession was inferred from dataset metadata (reviewer-only); it was not provided to the evaluated model.
- The ontology snapshot used by the benchmark authors is unknown; the current GO term name matches option C exactly.
- The protein also has a PubMed-supported role in suppressing NFATC4 (cardiac hypertrophy), which is unrelated to any of the four options and does not create ambiguity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "None identifiable from the sequence alone. The 666-aa sequence lacks recognizable catalytic or structural motifs (no RING/U-box domains, no ubiquitin-conjugating enzyme fold, no SNARE motifs, no immune-receptor domains, no carboxylic-acid-metabolism enzyme motifs). Basic N-terminal stretches (RRKKKKQKNKK) could suggest a nuclear localization signal, but this is too generic to favor K48-linked ubiquitination over the other three options. TCF25/NULP1 is an obscure RQC-complex subunit without widely recognized domain signatures.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this sequence as TCF25/NULP1, a ribosome-quality-control-complex subunit that promotes Lys-48 polyubiquitin chain formation during LTN1-mediated ubiquitination of nascent chains, together with the associated GO:0061945 annotation (ISO:RGD). This protein-specific annotation is not derivable from sequence motifs or general biological reasoning.",
    "reason": "The sequence contains no distinctive, widely recognized domains that would allow a knowledgeable biologist to reason from general principles to 'regulation of protein K48-linked ubiquitination' as opposed to the other three options. Correct selection depends on recognizing or looking up this specific protein's database annotation."
  },
  "case_id": "GO_biological_process_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A8I6ASZ5 (TCF25_RAT, 666 aa, sequence SHA256 confirmed). The UniProt entry carries GO:0061945 (regulation of protein K48-linked ubiquitination) with evidence code ISO:RGD, and the FUNCTION comment explicitly states the protein is 'required to promote formation of Lys-48-linked polyubiquitin chains during ubiquitination of incompletely synthesized proteins by LTN1.' The annotation and function description are consistent with the expected answer. However, the evidence is inferred-by-similarity (ISO:RGD, 'By similarity' in the function text), not direct experimental validation for this specific rat protein; the only PubMed reference (32805187) concerns NFATC4 suppression, not K48 ubiquitination."
  },
  "important_caveats": [
    "The GO annotation evidence code is ISO:RGD (inferred by similarity via RGD), and the function text qualifies the RQC/ubiquitination role as 'By similarity.' Direct experimental evidence for K48-linked ubiquitination regulation by this specific rat protein is not present in the supplied evidence.",
    "The accession was inferred from dataset metadata (reviewer-only); it was not provided to the evaluated model.",
    "The ontology snapshot used by the benchmark authors is unknown; the current GO term name matches option C exactly.",
    "The protein also has a PubMed-supported role in suppressing NFATC4 (cardiac hypertrophy), which is unrelated to any of the four options and does not create ambiguity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry annotates GO:0061945 and GO:0072344 (rescue of stalled ribosome) for this protein. Neither GO:0072344 nor any term corresponding to options A, B, or D appears in the annotation. Among the four provided choices, only C matches an annotated GO term, so the options are distinguishable once the correct annotation is known."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A8I6ASZ5 (TCF25_RAT, 666 aa, sequence SHA256 confirmed). The UniProt entry carries GO:0061945 (regulation of protein K48-linked ubiquitination) with evidence code ISO:RGD, and the FUNCTION comment explicitly states the protein is 'required to promote formation of Lys-48-linked polyubiquitin chains during ubiquitination of incompletely synthesized proteins by LTN1.' The annotation and function description are consistent with the expected answer. However, the evidence is inferred-by-similarity (ISO:RGD, 'By similarity' in the function text), not direct experimental validation for this specific rat protein; the only PubMed reference (32805187) concerns NFATC4 suppression, not K48 ubiquitination.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "None identifiable from the sequence alone. The 666-aa sequence lacks recognizable catalytic or structural motifs (no RING/U-box domains, no ubiquitin-conjugating enzyme fold, no SNARE motifs, no immune-receptor domains, no carboxylic-acid-metabolism enzyme motifs). Basic N-terminal stretches (RRKKKKQKNKK) could suggest a nuclear localization signal, but this is too generic to favor K48-linked ubiquitination over the other three options. TCF25/NULP1 is an obscure RQC-complex subunit without widely recognized domain signatures.",
    "missing_item_specific_fact": "The specific identification of this sequence as TCF25/NULP1, a ribosome-quality-control-complex subunit that promotes Lys-48 polyubiquitin chain formation during LTN1-mediated ubiquitination of nascent chains, together with the associated GO:0061945 annotation (ISO:RGD). This protein-specific annotation is not derivable from sequence motifs or general biological reasoning.",
    "reason": "The sequence contains no distinctive, widely recognized domains that would allow a knowledgeable biologist to reason from general principles to 'regulation of protein K48-linked ubiquitination' as opposed to the other three options. Correct selection depends on recognizing or looking up this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry annotates GO:0061945 and GO:0072344 (rescue of stalled ribosome) for this protein. Neither GO:0072344 nor any term corresponding to options A, B, or D appears in the annotation. Among the four provided choices, only C matches an annotated GO term, so the options are distinguishable once the correct annotation is known."
  },
  "important_caveats": [
    "The GO annotation evidence code is ISO:RGD (inferred by similarity via RGD), and the function text qualifies the RQC/ubiquitination role as 'By similarity.' Direct experimental evidence for K48-linked ubiquitination regulation by this specific rat protein is not present in the supplied evidence.",
    "The accession was inferred from dataset metadata (reviewer-only); it was not provided to the evaluated model.",
    "The ontology snapshot used by the benchmark authors is unknown; the current GO term name matches option C exactly.",
    "The protein also has a PubMed-supported role in suppressing NFATC4 (cardiac hypertrophy), which is unrelated to any of the four options and does not create ambiguity."
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

**Accession:** `A0A8I6ASZ5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.287559+00:00.  

```json
"A0A8I6ASZ5"
```

Source SHA-256: `db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.287559+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BQ70","source":"UniProtKB"}],"value":"Nuclear localized protein 1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"1309054","source":"RGD"}],"value":"Transcription factor 25"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"TCF-25"}]}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Ribosome quality control complex subunit TCF25"}}}
```

Source SHA-256: `db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.287559+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3L2","source":"UniProtKB"},{"evidenceCode":"ECO:0000250","id":"Q9BQ70","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"32805187","source":"PubMed"}],"value":"Component of the ribosome quality control complex (RQC), a ribosome-associated complex that mediates ubiquitination and extraction of incompletely synthesized nascent chains for proteasomal degradation (By similarity). In the RQC complex, required to promote formation of 'Lys-48'-linked polyubiquitin chains during ubiquitination of incompletely synthesized proteins by LTN1 (By similarity). May negatively regulate the calcineurin-NFAT signaling cascade by suppressing the activity of transcription factor NFATC4 (PubMed:32805187). May play a role in cell death control (By similarity)"}]}
```

Source SHA-256: `db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.287559+00:00.  

```json
{"database":"GO","id":"GO:0061945","properties":[{"key":"GoTerm","value":"P:regulation of protein K48-linked ubiquitination"},{"key":"GoEvidenceType","value":"ISO:RGD"}]}
```

Source SHA-256: `db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)  
**Locator:** `lines 72-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:34.894954+00:00.  

```text
CC   -!- FUNCTION: Component of the ribosome quality control complex (RQC), a
CC       ribosome-associated complex that mediates ubiquitination and extraction
CC       of incompletely synthesized nascent chains for proteasomal degradation
CC       (By similarity). In the RQC complex, required to promote formation of
CC       'Lys-48'-linked polyubiquitin chains during ubiquitination of
CC       incompletely synthesized proteins by LTN1 (By similarity). May
CC       negatively regulate the calcineurin-NFAT signaling cascade by
CC       suppressing the activity of transcription factor NFATC4
CC       (PubMed:32805187). May play a role in cell death control (By
CC       similarity). {ECO:0000250|UniProtKB:Q8R3L2,
CC       ECO:0000250|UniProtKB:Q9BQ70, ECO:0000269|PubMed:32805187}.
```

Source SHA-256: `02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)  
**Locator:** `lines 113-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:34.894954+00:00.  

```text
DR   GO; GO:0061945; P:regulation of protein K48-linked ubiquitination; ISO:RGD.
```

Source SHA-256: `02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 360905-360912`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0061945
name: regulation of protein K48-linked ubiquitination
namespace: biological_process
def: "Any process that modulates the rate, frequency or extent of protein K-48-linked ubiquitination, a protein ubiquitination process in which a polymer of ubiquitin, formed by linkages between lysine residues at position 48 of the ubiquitin monomers, is added to a protein. K48-linked ubiquitination targets the substrate protein for degradation." [PMID:23460740]
is_a: GO:1902914 ! regulation of protein polyubiquitination
relationship: regulates GO:0070936 ! protein K48-linked ubiquitination

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 166. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
