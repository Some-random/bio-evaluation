# GO_molecular_function_0120

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — aspartate kinase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSASTPTAPYLEDLVRNSLDQNLPWVVQKYGGTSVGKSLDNITKIVGSYIDNGSKVAIVCSARSTQTKSLGTTNLLLQASREALQPAMSSSGDGRSGSMSGTATPFYPKRVGSGFFGKDQSTSMTSSVSSLSQLESQLGRSGSPSPFQSSSSRSPPRSPATPSQDSSISQEPAFHATVDLIKKGHLEAARASLKGGPLRDELEEEIERDCESLRSFLYAAQIIDEISPRSQDSIVGTGERLACKIVAAALRDRGVDSELVVLDNIVDASMSAASEAVSVDAGDQGVAQLGQEFYDQLSFRLGERLRECGQRVPVVTGYFGPVPGSLLAQIGRGYTDLCAALCAVGLKASELQVWKEVDGIFTADPRKVPSARLVPIITPDEAAELTYYGSEVIHPFTMEQVIRARIPIRIKNVENPSGAGTVIYPDVGFPRGLDTEPPKAERIVEGVDERMPTAVTIKDEIIVLNIHSNRKTLSHGFLARIFGTLDRAGVVVDLISTSEVHVSMAMQDFLNRKRLERLVKDLEKIGEVTVSKDMAILSLVGRNMRNAIGSAGLMFASLARAMINIEMISQGASEINISCVIENKDAIKALNVIHESCLSYPRSPATEMAGLQLQ

[Multiple Choices]
A. phosphorelay response regulator activity
B. aspartate kinase activity
C. lysine-acetylated histone binding
D. hydrolase activity
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

> The exact supplied sequence matches the Cryptococcus neoformans aspartokinase entry. Its function annotation reports aspartate phosphorylation with experimental evidence, supporting choice B; the reaction assignment is also recorded with a similarity-based evidence qualifier.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone and the broad choices do not provide a clear, general biological argument that identifies aspartate kinase activity rather than the other candidate functions.


**Missing item-specific fact**

> The protein-specific functional identification of this sequence as an aspartokinase, established by annotation or sequence-homology evidence.


**Reason**

> The key is supported by reviewer-only evidence, but that evidence was not supplied to the evaluated model. Identifying the exact protein or a diagnostic homology would require item-specific knowledge; merely predicting from sequence is not a concrete argument supplied by the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supported aspartate kinase function is distinct from the response-regulator, histone-binding, and broad hydrolase alternatives.


### Important caveats

- The sequence match is confirmed for the cited UniProt record, but the author's original source snapshot is unknown.
- The specific catalytic reaction annotation is similarity-based; the function comment cites experimental evidence, which was not independently checked against the primary paper.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone and the broad choices do not provide a clear, general biological argument that identifies aspartate kinase activity rather than the other candidate functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification of this sequence as an aspartokinase, established by annotation or sequence-homology evidence.",
    "reason": "The key is supported by reviewer-only evidence, but that evidence was not supplied to the evaluated model. Identifying the exact protein or a diagnostic homology would require item-specific knowledge; merely predicting from sequence is not a concrete argument supplied by the question."
  },
  "case_id": "GO_molecular_function_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the Cryptococcus neoformans aspartokinase entry. Its function annotation reports aspartate phosphorylation with experimental evidence, supporting choice B; the reaction assignment is also recorded with a similarity-based evidence qualifier."
  },
  "important_caveats": [
    "The sequence match is confirmed for the cited UniProt record, but the author's original source snapshot is unknown.",
    "The specific catalytic reaction annotation is similarity-based; the function comment cites experimental evidence, which was not independently checked against the primary paper."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported aspartate kinase function is distinct from the response-regulator, histone-binding, and broad hydrolase alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the Cryptococcus neoformans aspartokinase entry. Its function annotation reports aspartate phosphorylation with experimental evidence, supporting choice B; the reaction assignment is also recorded with a similarity-based evidence qualifier.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone and the broad choices do not provide a clear, general biological argument that identifies aspartate kinase activity rather than the other candidate functions.",
    "missing_item_specific_fact": "The protein-specific functional identification of this sequence as an aspartokinase, established by annotation or sequence-homology evidence.",
    "reason": "The key is supported by reviewer-only evidence, but that evidence was not supplied to the evaluated model. Identifying the exact protein or a diagnostic homology would require item-specific knowledge; merely predicting from sequence is not a concrete argument supplied by the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported aspartate kinase function is distinct from the response-regulator, histone-binding, and broad hydrolase alternatives."
  },
  "important_caveats": [
    "The sequence match is confirmed for the cited UniProt record, but the author's original source snapshot is unknown.",
    "The specific catalytic reaction annotation is similarity-based; the function comment cites experimental evidence, which was not independently checked against the primary paper."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry J9VS37 (sequence matched, 615 aa) is annotated as Aspartokinase (EC 2.7.2.4) with experimental evidence (ECO:0000269, PubMed:18757810) for the FUNCTION comment 'Phosphorylates aspartate.' The catalytic activity is L-aspartate + ATP = 4-phospho-L-aspartate + ADP. GO:0004072 (aspartate kinase activity) is annotated to this entry. The sequence matches both current and historical (v66) records.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains nucleotide-binding motifs (e.g., GSGFFG, GSG-rich regions) and the overall ~615-aa architecture with regulatory flanking regions and a central catalytic domain is characteristic of the amino acid kinase family (transferases), which positively identifies it as a kinase rather than a hydrolase (D) or a binding protein (C). The absence of a canonical receiver-domain architecture (conserved His-Asp phosphorelay pair in the correct structural context) eliminates phosphorelay response regulator activity (A). Among the four options, only B is a kinase/transferase function, making it the sole survivor after domain-level elimination.


**Missing item-specific fact**

> Precise identification of 'aspartate' as the substrate (vs. other amino acid kinase substrates like homoserine or N-acetylglutamate) would require identifying specific active-site residues conferring aspartate specificity; however, no competing amino-kinase option is presented, so the elimination logic suffices to select B.


**Reason**

> A knowledgeable reader can recognize kinase motifs to eliminate C and D, note the absence of receiver-domain features to eliminate A, and conclude B. The specific substrate identity ('aspartate') is not independently derivable from sequence without database lookup, but the question's option set makes this unnecessary for correct selection.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (response regulator), C (histone binding), and D (hydrolase) are clearly incompatible with the observed kinase/transferase architecture. No other amino acid kinase is offered as a distractor, so B is the unique defensible choice among the four.


### Important caveats

- The GO annotation for this entry carries evidence code ISS/IEA (inferred by similarity to P10869) rather than direct experimental characterization of the Cryptococcus enzyme's kinetics; however, the PubMed:18757810 reference provides experimental evidence for the aspartate-phosphorylation function in this organism.
- The specific identification of 'aspartate' as substrate from raw sequence alone is difficult; the question is answerable primarily by elimination of clearly wrong functional classes rather than by reading substrate specificity from active-site residues.
- Reviewer-only evidence (UniProt accession, GO annotation) was not available to the evaluated model; the reasoning argument relies solely on domain/motif recognition from the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains nucleotide-binding motifs (e.g., GSGFFG, GSG-rich regions) and the overall ~615-aa architecture with regulatory flanking regions and a central catalytic domain is characteristic of the amino acid kinase family (transferases), which positively identifies it as a kinase rather than a hydrolase (D) or a binding protein (C). The absence of a canonical receiver-domain architecture (conserved His-Asp phosphorelay pair in the correct structural context) eliminates phosphorelay response regulator activity (A). Among the four options, only B is a kinase/transferase function, making it the sole survivor after domain-level elimination.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of 'aspartate' as the substrate (vs. other amino acid kinase substrates like homoserine or N-acetylglutamate) would require identifying specific active-site residues conferring aspartate specificity; however, no competing amino-kinase option is presented, so the elimination logic suffices to select B.",
    "reason": "A knowledgeable reader can recognize kinase motifs to eliminate C and D, note the absence of receiver-domain features to eliminate A, and conclude B. The specific substrate identity ('aspartate') is not independently derivable from sequence without database lookup, but the question's option set makes this unnecessary for correct selection."
  },
  "case_id": "GO_molecular_function_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry J9VS37 (sequence matched, 615 aa) is annotated as Aspartokinase (EC 2.7.2.4) with experimental evidence (ECO:0000269, PubMed:18757810) for the FUNCTION comment 'Phosphorylates aspartate.' The catalytic activity is L-aspartate + ATP = 4-phospho-L-aspartate + ADP. GO:0004072 (aspartate kinase activity) is annotated to this entry. The sequence matches both current and historical (v66) records."
  },
  "important_caveats": [
    "The GO annotation for this entry carries evidence code ISS/IEA (inferred by similarity to P10869) rather than direct experimental characterization of the Cryptococcus enzyme's kinetics; however, the PubMed:18757810 reference provides experimental evidence for the aspartate-phosphorylation function in this organism.",
    "The specific identification of 'aspartate' as substrate from raw sequence alone is difficult; the question is answerable primarily by elimination of clearly wrong functional classes rather than by reading substrate specificity from active-site residues.",
    "Reviewer-only evidence (UniProt accession, GO annotation) was not available to the evaluated model; the reasoning argument relies solely on domain/motif recognition from the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (response regulator), C (histone binding), and D (hydrolase) are clearly incompatible with the observed kinase/transferase architecture. No other amino acid kinase is offered as a distractor, so B is the unique defensible choice among the four."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry J9VS37 (sequence matched, 615 aa) is annotated as Aspartokinase (EC 2.7.2.4) with experimental evidence (ECO:0000269, PubMed:18757810) for the FUNCTION comment 'Phosphorylates aspartate.' The catalytic activity is L-aspartate + ATP = 4-phospho-L-aspartate + ADP. GO:0004072 (aspartate kinase activity) is annotated to this entry. The sequence matches both current and historical (v66) records.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains nucleotide-binding motifs (e.g., GSGFFG, GSG-rich regions) and the overall ~615-aa architecture with regulatory flanking regions and a central catalytic domain is characteristic of the amino acid kinase family (transferases), which positively identifies it as a kinase rather than a hydrolase (D) or a binding protein (C). The absence of a canonical receiver-domain architecture (conserved His-Asp phosphorelay pair in the correct structural context) eliminates phosphorelay response regulator activity (A). Among the four options, only B is a kinase/transferase function, making it the sole survivor after domain-level elimination.",
    "missing_item_specific_fact": "Precise identification of 'aspartate' as the substrate (vs. other amino acid kinase substrates like homoserine or N-acetylglutamate) would require identifying specific active-site residues conferring aspartate specificity; however, no competing amino-kinase option is presented, so the elimination logic suffices to select B.",
    "reason": "A knowledgeable reader can recognize kinase motifs to eliminate C and D, note the absence of receiver-domain features to eliminate A, and conclude B. The specific substrate identity ('aspartate') is not independently derivable from sequence without database lookup, but the question's option set makes this unnecessary for correct selection."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (response regulator), C (histone binding), and D (hydrolase) are clearly incompatible with the observed kinase/transferase architecture. No other amino acid kinase is offered as a distractor, so B is the unique defensible choice among the four."
  },
  "important_caveats": [
    "The GO annotation for this entry carries evidence code ISS/IEA (inferred by similarity to P10869) rather than direct experimental characterization of the Cryptococcus enzyme's kinetics; however, the PubMed:18757810 reference provides experimental evidence for the aspartate-phosphorylation function in this organism.",
    "The specific identification of 'aspartate' as substrate from raw sequence alone is difficult; the question is answerable primarily by elimination of clearly wrong functional classes rather than by reading substrate specificity from active-site residues.",
    "Reviewer-only evidence (UniProt accession, GO annotation) was not available to the evaluated model; the reasoning argument relies solely on domain/motif recognition from the supplied sequence."
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

**Accession:** `J9VS37` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 66. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
"J9VS37"
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"value":"2.7.2.4"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartokinase"}}}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18757810","source":"PubMed"}],"value":"Phosphorylates aspartate, the first step in the biosynthesis of amino acids that derive from aspartate (the aspartate family of amino acids), including methioinine and threonine, the latter of which is a precursor to isoleucine"}]}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23777"}}],"reaction":{"ecNumber":"2.7.2.4","evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"name":"L-aspartate + ATP = 4-phospho-L-aspartate + ADP","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23776"},{"database":"ChEBI","id":"CHEBI:29991"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"database":"GO","id":"GO:0004072","properties":[{"key":"GoTerm","value":"F:aspartate kinase activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
ID   AK_CRYN9                Reviewed;         615 AA.
AC   J9VS37;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-NOV-2012, sequence version 1.
DT   28-JAN-2026, entry version 66.
DE   RecName: Full=Aspartokinase {ECO:0000305};
DE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};
GN   Name=HOM3 {ECO:0000303|PubMed:18757810};
GN   ORFNames=CNAG_04347 {ECO:0000312|EMBL:AFR97078.1};
OS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)
OS   (Cryptococcus neoformans var. grubii serotype A).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 41-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
CC   -!- FUNCTION: Phosphorylates aspartate, the first step in the biosynthesis
CC       of amino acids that derive from aspartate (the aspartate family of
CC       amino acids), including methioinine and threonine, the latter of which
CC       is a precursor to isoleucine. {ECO:0000269|PubMed:18757810}.
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 45-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;
CC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;
CC         Evidence={ECO:0000250|UniProtKB:P10869};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;
CC         Evidence={ECO:0000250|UniProtKB:P10869};
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 80-80`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
DR   GO; GO:0004072; F:aspartate kinase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 120. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
