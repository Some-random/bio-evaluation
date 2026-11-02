# GO_biological_process_0021

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — NAD biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMESAVTAHTLRIAMAQFDFPVGAVTQNTDRIIEYIAAARDEFEADIVLFPELAISGYPPEDLLLRPGFLAHCEQALARIAAATRGIVAVVGWPQSAGSVVYNAASVLREGRIEATYRKRELPNYAVFDERRYFDVDPDGDNCVVTVKGVQVGVVICEDLWFAEPLAKTVQAGAELVLVPNASPYERGKHAQRDALLAERTRESGAAIAYLNVVGGQDALVFDGASVVADGDGTVHPAAAAFVDQWLVVDYAAGERSFTPVVWVDDGDESMDALAWRAVVRGLKDYCGKNGFRKVWLGLSGGIDSALVLAMAVDALGGENVTAVRLPSRYTAGLSNDLADEQCRALGVKLETIAIEPAFEGLLAALGPLFADTQPDITEENLQSRSRGVILMALSNKFGGLVLTTGNKSEYAVGYATIYGDMCGGYAPLKDLYKTEVFGLAKWRNTVGGAPVIPPAVISRPPSAELRDNQTDQDSLPPYDVLDGILYRYVDQEQSRDDIVAAGYAADTVEHVLRLVRLNEWKRHQAAPGPKVSRRAFGRERRYPITNGYSGQ

[Multiple Choices]
A. tRNA acetylation
B. inflammatory response
C. negative regulation of apoptotic process in bone marrow cell
D. NAD biosynthetic process
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

> The exact sequence matches a bacterial protein annotated as glutamine-dependent NAD(+) synthetase, which catalyzes formation of NAD from deamido-NAD; the annotation assigns it to NAD+ biosynthesis. The function and GO annotation are computationally supported by HAMAP/UniRule rather than established here by direct experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a bacterial enzyme and the options make several broad alternatives less plausible, but identifying NAD+ biosynthesis requires recognizing the specific enzyme family and its reaction.


**Missing item-specific fact**

> That this exact sequence is a glutamine-dependent NAD+ synthetase (NadE) catalyzing the final amidation step in NAD formation.


**Reason**

> The input supplies only the sequence and choices, not a protein-family annotation, organism context, or reaction. Inferring the specific process depends on the protein-specific identity or an equivalent external sequence analysis; recognizing the exact sequence from memory would not itself constitute reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supported function and pathway map directly to option D; the other choices describe unrelated processes.


### Important caveats

- The sequence match is exact, but the author’s source snapshot is unknown.
- The cited functional and GO annotations are computational (HAMAP/UniRule); the supplied evidence does not independently establish the enzyme’s activity experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a bacterial enzyme and the options make several broad alternatives less plausible, but identifying NAD+ biosynthesis requires recognizing the specific enzyme family and its reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this exact sequence is a glutamine-dependent NAD+ synthetase (NadE) catalyzing the final amidation step in NAD formation.",
    "reason": "The input supplies only the sequence and choices, not a protein-family annotation, organism context, or reaction. Inferring the specific process depends on the protein-specific identity or an equivalent external sequence analysis; recognizing the exact sequence from memory would not itself constitute reasoning from the supplied input."
  },
  "case_id": "GO_biological_process_0021",
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
    "reason": "The exact sequence matches a bacterial protein annotated as glutamine-dependent NAD(+) synthetase, which catalyzes formation of NAD from deamido-NAD; the annotation assigns it to NAD+ biosynthesis. The function and GO annotation are computationally supported by HAMAP/UniRule rather than established here by direct experimental evidence."
  },
  "important_caveats": [
    "The sequence match is exact, but the author’s source snapshot is unknown.",
    "The cited functional and GO annotations are computational (HAMAP/UniRule); the supplied evidence does not independently establish the enzyme’s activity experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported function and pathway map directly to option D; the other choices describe unrelated processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a bacterial protein annotated as glutamine-dependent NAD(+) synthetase, which catalyzes formation of NAD from deamido-NAD; the annotation assigns it to NAD+ biosynthesis. The function and GO annotation are computationally supported by HAMAP/UniRule rather than established here by direct experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a bacterial enzyme and the options make several broad alternatives less plausible, but identifying NAD+ biosynthesis requires recognizing the specific enzyme family and its reaction.",
    "missing_item_specific_fact": "That this exact sequence is a glutamine-dependent NAD+ synthetase (NadE) catalyzing the final amidation step in NAD formation.",
    "reason": "The input supplies only the sequence and choices, not a protein-family annotation, organism context, or reaction. Inferring the specific process depends on the protein-specific identity or an equivalent external sequence analysis; recognizing the exact sequence from memory would not itself constitute reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported function and pathway map directly to option D; the other choices describe unrelated processes."
  },
  "important_caveats": [
    "The sequence match is exact, but the author’s source snapshot is unknown.",
    "The cited functional and GO annotations are computational (HAMAP/UniRule); the supplied evidence does not independently establish the enzyme’s activity experimentally."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A0H2X6L3 (NADE_XANC8), annotated as glutamine-dependent NAD(+) synthetase (EC 6.3.5.1). The HAMAP-Rule annotation (ECO:0000255) and a 2024 experimental paper (PubMed:38429435, disruption phenotype) confirm the protein catalyzes ATP-dependent amidation of deamido-NAD to form NAD. The GO term GO:0009435 'NAD+ biosynthetic process' is directly assigned (IEA:UniProtKB-UniRule), and 'NAD biosynthetic process' is listed as an EXACT synonym of GO:0009435, matching option D verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits bacterial characteristics (no signal peptide typical of eukaryotic secreted proteins, codon-usage-like composition, ~552 aa multi-domain architecture). Options B (inflammatory response, GO:0006954, defined for 'vertebrate tissue') and C (negative regulation of apoptotic process in bone marrow cell, GO:0071866) are vertebrate-specific processes and cannot apply to a bacterial protein. Option A (tRNA acetylation, GO:0051391) requires a small tRNA-modifying enzyme, inconsistent with the large multi-domain architecture observed. The N-terminal region contains a glutamine amidotransferase (GAT) catalytic motif (conserved Cys in 'CEQ' context) and the C-terminal region shows a synthetase domain with the 'GDMCGGYAP' motif characteristic of NadE, together with an ATP-binding P-loop-like 'GWPQSAGS' motif. This two-domain GAT+synthetase architecture in a bacterial protein is diagnostic of NAD+ synthetase, pointing to NAD biosynthetic process.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distractors are eliminable by general biological reasoning: two are vertebrate-specific (B, C), one is a structurally incompatible enzyme class (A). The positive identification relies on recognizing the well-known GAT+synthetase two-domain architecture of NadE, which is standard enzymology knowledge rather than a single-database lookup. The sequence motifs (GAT catalytic Cys, P-loop, synthetase 'GDMCGGYAP') provide concrete structural grounds for the answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are strictly vertebrate processes inapplicable to a bacterial protein. Option A describes a small tRNA-modifying enzyme, structurally incompatible with the observed ~552 aa multi-domain architecture. Only D is consistent with both the organismal context and the domain architecture.


### Important caveats

- The GO annotation for GO:0009435 carries evidence code IEA:UniProtKB-UniRule (computational inference from HAMAP-Rule MF_02090), not direct experimental assignment of the GO term. However, the 2024 disruption-phenotype paper (PubMed:38429435) provides experimental support for the protein's role in NAD+ biosynthesis in this organism.
- The reviewer-only evidence was not available to the evaluated model; the reasoning path described relies on general domain-architecture knowledge and organismal context inferable from the sequence.
- The GO term name in the ontology is 'NAD+ biosynthetic process' while the option text reads 'NAD biosynthetic process'; this is an EXACT synonym per GO:0009435, so the match is valid.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits bacterial characteristics (no signal peptide typical of eukaryotic secreted proteins, codon-usage-like composition, ~552 aa multi-domain architecture). Options B (inflammatory response, GO:0006954, defined for 'vertebrate tissue') and C (negative regulation of apoptotic process in bone marrow cell, GO:0071866) are vertebrate-specific processes and cannot apply to a bacterial protein. Option A (tRNA acetylation, GO:0051391) requires a small tRNA-modifying enzyme, inconsistent with the large multi-domain architecture observed. The N-terminal region contains a glutamine amidotransferase (GAT) catalytic motif (conserved Cys in 'CEQ' context) and the C-terminal region shows a synthetase domain with the 'GDMCGGYAP' motif characteristic of NadE, together with an ATP-binding P-loop-like 'GWPQSAGS' motif. This two-domain GAT+synthetase architecture in a bacterial protein is diagnostic of NAD+ synthetase, pointing to NAD biosynthetic process.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distractors are eliminable by general biological reasoning: two are vertebrate-specific (B, C), one is a structurally incompatible enzyme class (A). The positive identification relies on recognizing the well-known GAT+synthetase two-domain architecture of NadE, which is standard enzymology knowledge rather than a single-database lookup. The sequence motifs (GAT catalytic Cys, P-loop, synthetase 'GDMCGGYAP') provide concrete structural grounds for the answer."
  },
  "case_id": "GO_biological_process_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H3",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A0H2X6L3 (NADE_XANC8), annotated as glutamine-dependent NAD(+) synthetase (EC 6.3.5.1). The HAMAP-Rule annotation (ECO:0000255) and a 2024 experimental paper (PubMed:38429435, disruption phenotype) confirm the protein catalyzes ATP-dependent amidation of deamido-NAD to form NAD. The GO term GO:0009435 'NAD+ biosynthetic process' is directly assigned (IEA:UniProtKB-UniRule), and 'NAD biosynthetic process' is listed as an EXACT synonym of GO:0009435, matching option D verbatim."
  },
  "important_caveats": [
    "The GO annotation for GO:0009435 carries evidence code IEA:UniProtKB-UniRule (computational inference from HAMAP-Rule MF_02090), not direct experimental assignment of the GO term. However, the 2024 disruption-phenotype paper (PubMed:38429435) provides experimental support for the protein's role in NAD+ biosynthesis in this organism.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning path described relies on general domain-architecture knowledge and organismal context inferable from the sequence.",
    "The GO term name in the ontology is 'NAD+ biosynthetic process' while the option text reads 'NAD biosynthetic process'; this is an EXACT synonym per GO:0009435, so the match is valid."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are strictly vertebrate processes inapplicable to a bacterial protein. Option A describes a small tRNA-modifying enzyme, structurally incompatible with the observed ~552 aa multi-domain architecture. Only D is consistent with both the organismal context and the domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A0H2X6L3 (NADE_XANC8), annotated as glutamine-dependent NAD(+) synthetase (EC 6.3.5.1). The HAMAP-Rule annotation (ECO:0000255) and a 2024 experimental paper (PubMed:38429435, disruption phenotype) confirm the protein catalyzes ATP-dependent amidation of deamido-NAD to form NAD. The GO term GO:0009435 'NAD+ biosynthetic process' is directly assigned (IEA:UniProtKB-UniRule), and 'NAD biosynthetic process' is listed as an EXACT synonym of GO:0009435, matching option D verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H3", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits bacterial characteristics (no signal peptide typical of eukaryotic secreted proteins, codon-usage-like composition, ~552 aa multi-domain architecture). Options B (inflammatory response, GO:0006954, defined for 'vertebrate tissue') and C (negative regulation of apoptotic process in bone marrow cell, GO:0071866) are vertebrate-specific processes and cannot apply to a bacterial protein. Option A (tRNA acetylation, GO:0051391) requires a small tRNA-modifying enzyme, inconsistent with the large multi-domain architecture observed. The N-terminal region contains a glutamine amidotransferase (GAT) catalytic motif (conserved Cys in 'CEQ' context) and the C-terminal region shows a synthetase domain with the 'GDMCGGYAP' motif characteristic of NadE, together with an ATP-binding P-loop-like 'GWPQSAGS' motif. This two-domain GAT+synthetase architecture in a bacterial protein is diagnostic of NAD+ synthetase, pointing to NAD biosynthetic process.",
    "missing_item_specific_fact": "",
    "reason": "The distractors are eliminable by general biological reasoning: two are vertebrate-specific (B, C), one is a structurally incompatible enzyme class (A). The positive identification relies on recognizing the well-known GAT+synthetase two-domain architecture of NadE, which is standard enzymology knowledge rather than a single-database lookup. The sequence motifs (GAT catalytic Cys, P-loop, synthetase 'GDMCGGYAP') provide concrete structural grounds for the answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are strictly vertebrate processes inapplicable to a bacterial protein. Option A describes a small tRNA-modifying enzyme, structurally incompatible with the observed ~552 aa multi-domain architecture. Only D is consistent with both the organismal context and the domain architecture."
  },
  "important_caveats": [
    "The GO annotation for GO:0009435 carries evidence code IEA:UniProtKB-UniRule (computational inference from HAMAP-Rule MF_02090), not direct experimental assignment of the GO term. However, the 2024 disruption-phenotype paper (PubMed:38429435) provides experimental support for the protein's role in NAD+ biosynthesis in this organism.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning path described relies on general domain-architecture knowledge and organismal context inferable from the sequence.",
    "The GO term name in the ontology is 'NAD+ biosynthetic process' while the option text reads 'NAD biosynthetic process'; this is an EXACT synonym per GO:0009435, so the match is valid."
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

**Accession:** `A0A0H2X6L3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 49. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"NAD(+) synthase [glutamine-hydrolyzing]"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NAD(+) synthetase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NADS"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"6.3.5.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"Glutamine-dependent NAD(+) synthetase"}}}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"Catalyzes the ATP-dependent amidation of deamido-NAD to form NAD. Uses L-glutamine as a nitrogen source"}]}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1"}]}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"database":"GO","id":"GO:0009435","properties":[{"key":"GoTerm","value":"P:NAD+ biosynthetic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniRule"}]}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"citation":{"authors":["Xu G.","Ma J.","Fang Q.","Peng Q.","Jiao X.","Hu W.","Zhao Q.","Kong Y.","Liu F.","Shi X.","Tang D.J.","Tang J.L.","Ming Z."],"citationCrossReferences":[{"database":"PubMed","id":"38429435"},{"database":"DOI","id":"10.1038/s42003-024-05921-3"}],"citationType":"journal article","firstPage":"255","id":"38429435","journal":"Commun. Biol.","lastPage":"255","publicationDate":"2024","title":"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.","volume":"7"},"referenceComments":[{"type":"STRAIN","value":"8004"}],"referenceNumber":2,"referencePositions":["DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
ID   NADE_XANC8              Reviewed;         552 AA.
AC   A0A0H2X6L3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-SEP-2015, sequence version 1.
DT   28-JAN-2026, entry version 49.
DE   RecName: Full=Glutamine-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_02090};
DE            EC=6.3.5.1 {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthase [glutamine-hydrolyzing] {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthetase {ECO:0000303|PubMed:38429435};
DE            Short=NADS {ECO:0000303|PubMed:38429435};
GN   Name=nadE {ECO:0000255|HAMAP-Rule:MF_02090};
GN   OrderedLocusNames=XC_1067 {ECO:0000312|EMBL:AAY48137.1};
OS   Xanthomonas campestris pv. campestris (strain 8004).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Lysobacterales; Lysobacteraceae; Xanthomonas.
OX   NCBI_TaxID=314565;
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 37-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the ATP-dependent amidation of deamido-NAD to form
CC       NAD. Uses L-glutamine as a nitrogen source. {ECO:0000255|HAMAP-
CC       Rule:MF_02090}.
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 47-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from
CC       deamido-NAD(+) (L-Gln route): step 1/1. {ECO:0000255|HAMAP-
CC       Rule:MF_02090}.
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 73-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
DR   GO; GO:0009435; P:NAD+ biosynthetic process; IEA:UniProtKB-UniRule.
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 96227-96257`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009435
name: NAD+ biosynthetic process
namespace: biological_process
alt_id: GO:0006736
def: "The chemical reactions and pathways resulting in the formation of nicotinamide adenine dinucleotide (NAD+), a coenzyme that interconverts with its reduced form, NADH, in many redox and catabolic reactions. NAD+ is derived from various sources including vitamin B3." [PMID:28648096]
synonym: "NAD (oxidized) biosynthesis" EXACT []
synonym: "NAD (oxidized) biosynthetic process" EXACT []
synonym: "NAD (reduced) biosynthesis" EXACT []
synonym: "NAD (reduced) biosynthetic process" EXACT []
synonym: "NAD anabolism" EXACT []
synonym: "NAD biosynthesis" EXACT []
synonym: "NAD biosynthetic process" EXACT []
synonym: "NAD formation" EXACT []
synonym: "NAD synthesis" EXACT []
synonym: "NADH biosynthesis" EXACT []
synonym: "NADH biosynthetic process" EXACT []
synonym: "nicotinamide adenine dinucleotide biosynthesis" EXACT []
synonym: "nicotinamide adenine dinucleotide biosynthetic process" EXACT []
synonym: "oxidized NAD biosynthesis" EXACT []
synonym: "oxidized NAD biosynthetic process" EXACT []
synonym: "oxidized nicotinamide adenine dinucleotide biosynthesis" EXACT []
synonym: "oxidized nicotinamide adenine dinucleotide biosynthetic process" EXACT []
synonym: "reduced NAD biosynthesis" EXACT []
synonym: "reduced NAD biosynthetic process" EXACT []
synonym: "reduced nicotinamide adenine dinucleotide biosynthesis" EXACT []
synonym: "reduced nicotinamide adenine dinucleotide biosynthetic process" EXACT []
is_a: GO:0006164 ! purine nucleotide biosynthetic process
is_a: GO:0019359 ! nicotinamide nucleotide biosynthetic process
is_a: GO:0019674 ! NAD+ metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
