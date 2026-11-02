# pathway_0019

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTIRGTLSELSRAADAFAHEVDEAGYGDYTFLPDNSPFDLSFLTSKGLEARGSLIAAAEKILRLAKGPQGCLASFADTKGIEMGTIQALTQLEVPDKVPLQGSITYEELAGVIRVAPELLQRLVRLAALAGFLIEDESGAVRHTAMSAVFLRDTAAGDTARFLFDVDMRAYSFFADSLRLDPSGQNIGDGPTALAFQHDSDDQGNRPTIWDILERNPIQRARFHSTMQALGSFPSHLLKHILVAHDWHSIGSLVDVGGSLGHASLVIAENFPEIRITVQDLPDVVERGRSSLPTVPHAERVSFQAHDLFQEQAIIADAYFLRQILHDWPDGDAERIVRCLIPAMRPGAKLLIMDIVVPEPGAISPYMEKYLRTYDVSMFSMFSAKERTVQQLRDLVERCSARLQFQGISCPPGSATSLLSWVYSAE

[Multiple Choices]
A. Pyrimidine metabolism
B. Secondary metabolite biosynthesis. .
C. Glycan degradation
D. tetrahydrofolate interconversion. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the sequence in the UniProt record identifying FrzF as an O-methyltransferase in secondary metabolite biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269), although the cited paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support recognizing an enzyme such as a methyltransferase, but that enzyme class alone does not establish which pathway it participates in among these choices.


**Missing item-specific fact**

> The protein-specific association of FrzF with FR901483 biosynthesis and the secondary-metabolite pathway.


**Reason**

> That pathway association is not provided in the question and cannot be inferred reliably from the sequence alone; distinguishing the intended choice requires a protein-specific annotation or experimental fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied input does not establish a pathway-specific association for any option. Reviewer-only evidence supports B, but does not make that fact available to the evaluated model.


### Important caveats

- The reviewer evidence matches the exact sequence and cites experimental evidence for the pathway annotation; the primary paper was not independently assessed.
- The author's source snapshot is unknown, though a sequence-matched historical UniProt record also contains the pathway annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support recognizing an enzyme such as a methyltransferase, but that enzyme class alone does not establish which pathway it participates in among these choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific association of FrzF with FR901483 biosynthesis and the secondary-metabolite pathway.",
    "reason": "That pathway association is not provided in the question and cannot be inferred reliably from the sequence alone; distinguishing the intended choice requires a protein-specific annotation or experimental fact."
  },
  "case_id": "pathway_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the UniProt record identifying FrzF as an O-methyltransferase in secondary metabolite biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269), although the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer evidence matches the exact sequence and cites experimental evidence for the pathway annotation; the primary paper was not independently assessed.",
    "The author's source snapshot is unknown, though a sequence-matched historical UniProt record also contains the pathway annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied input does not establish a pathway-specific association for any option. Reviewer-only evidence supports B, but does not make that fact available to the evaluated model."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the UniProt record identifying FrzF as an O-methyltransferase in secondary metabolite biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269), although the cited paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support recognizing an enzyme such as a methyltransferase, but that enzyme class alone does not establish which pathway it participates in among these choices.",
    "missing_item_specific_fact": "The protein-specific association of FrzF with FR901483 biosynthesis and the secondary-metabolite pathway.",
    "reason": "That pathway association is not provided in the question and cannot be inferred reliably from the sequence alone; distinguishing the intended choice requires a protein-specific annotation or experimental fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied input does not establish a pathway-specific association for any option. Reviewer-only evidence supports B, but does not make that fact available to the evaluated model."
  },
  "important_caveats": [
    "The reviewer evidence matches the exact sequence and cites experimental evidence for the pathway annotation; the primary paper was not independently assessed.",
    "The author's source snapshot is unknown, though a sequence-matched historical UniProt record also contains the pathway annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7T8J1Z8 (FRZF_CLASX) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:33372776 (Zhang et al., JACS 2021). The protein is O-methyltransferase FrzF, a component of the FR901483 immunosuppressant biosynthetic gene cluster in Cladobotryum sp. The sequence matches exactly (427 AA, SHA256 confirmed). The annotation is experimentally supported, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains recognizable SAM-dependent methyltransferase motifs (GGSLGH, DWDW/DWDG) indicating a Rossmann-fold class I methyltransferase. However, methyltransferases are ubiquitous across all four listed pathways: pyrimidine metabolism (e.g., thymidylate synthase), tetrahydrofolate interconversion (folate-dependent methyl transfer), glycan degradation (rare but possible), and secondary metabolite biosynthesis. No sequence motif uniquely identifies this enzyme as belonging to secondary metabolite biosynthesis rather than central metabolism methylation.


**Missing item-specific fact**

> The specific identity of this protein as FrzF, a cluster-specific O-methyltransferase in the FR901483 biosynthetic gene cluster of Cladobotryum sp., is required to assign it to 'Secondary metabolite biosynthesis' rather than a central metabolic methylation pathway. This requires knowledge of the organism (fungal), the gene cluster context, and the specific substrate methylated by this enzyme.


**Reason**

> While the sequence reveals methyltransferase function through conserved motifs, the pathway assignment among the four choices depends on knowing this is a specialized fungal biosynthetic cluster enzyme rather than a central metabolism methyltransferase. The sequence alone does not provide sufficient grounds to distinguish secondary metabolite biosynthesis from tetrahydrofolate interconversion or pyrimidine metabolism, all of which involve methyl transfer reactions.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Option D (tetrahydrofolate interconversion) is a plausible distractor because methyltransferases participate in folate cycling, and without knowing the specific substrate and organism context, a model might reason that a SAM-dependent methyltransferase could be involved in folate metabolism. However, the protein lacks canonical DHFR or serine hydroxymethyltransferase features, making D less defensible than B for a knowledgeable reviewer. The distinction ultimately requires item-specific knowledge.


### Important caveats

- The pathway annotation carries ECO:0000269 (direct assay), indicating experimental confirmation rather than computational inference.
- The protein is from Cladobotryum sp. (a fungus), and the 'secondary metabolite' designation reflects its role in a specialized biosynthetic cluster (FR901483), not a general metabolic pathway.
- The sequence motifs (GGSLGH, DWDW) confirm methyltransferase function but do not specify the pathway without additional context.
- The reviewer-only evidence was not available to the evaluated model; the model must rely solely on sequence analysis and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable SAM-dependent methyltransferase motifs (GGSLGH, DWDW/DWDG) indicating a Rossmann-fold class I methyltransferase. However, methyltransferases are ubiquitous across all four listed pathways: pyrimidine metabolism (e.g., thymidylate synthase), tetrahydrofolate interconversion (folate-dependent methyl transfer), glycan degradation (rare but possible), and secondary metabolite biosynthesis. No sequence motif uniquely identifies this enzyme as belonging to secondary metabolite biosynthesis rather than central metabolism methylation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as FrzF, a cluster-specific O-methyltransferase in the FR901483 biosynthetic gene cluster of Cladobotryum sp., is required to assign it to 'Secondary metabolite biosynthesis' rather than a central metabolic methylation pathway. This requires knowledge of the organism (fungal), the gene cluster context, and the specific substrate methylated by this enzyme.",
    "reason": "While the sequence reveals methyltransferase function through conserved motifs, the pathway assignment among the four choices depends on knowing this is a specialized fungal biosynthetic cluster enzyme rather than a central metabolism methyltransferase. The sequence alone does not provide sufficient grounds to distinguish secondary metabolite biosynthesis from tetrahydrofolate interconversion or pyrimidine metabolism, all of which involve methyl transfer reactions."
  },
  "case_id": "pathway_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7T8J1Z8 (FRZF_CLASX) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:33372776 (Zhang et al., JACS 2021). The protein is O-methyltransferase FrzF, a component of the FR901483 immunosuppressant biosynthetic gene cluster in Cladobotryum sp. The sequence matches exactly (427 AA, SHA256 confirmed). The annotation is experimentally supported, not merely computational."
  },
  "important_caveats": [
    "The pathway annotation carries ECO:0000269 (direct assay), indicating experimental confirmation rather than computational inference.",
    "The protein is from Cladobotryum sp. (a fungus), and the 'secondary metabolite' designation reflects its role in a specialized biosynthetic cluster (FR901483), not a general metabolic pathway.",
    "The sequence motifs (GGSLGH, DWDW) confirm methyltransferase function but do not specify the pathway without additional context.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely solely on sequence analysis and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Option D (tetrahydrofolate interconversion) is a plausible distractor because methyltransferases participate in folate cycling, and without knowing the specific substrate and organism context, a model might reason that a SAM-dependent methyltransferase could be involved in folate metabolism. However, the protein lacks canonical DHFR or serine hydroxymethyltransferase features, making D less defensible than B for a knowledgeable reviewer. The distinction ultimately requires item-specific knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7T8J1Z8 (FRZF_CLASX) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:33372776 (Zhang et al., JACS 2021). The protein is O-methyltransferase FrzF, a component of the FR901483 immunosuppressant biosynthetic gene cluster in Cladobotryum sp. The sequence matches exactly (427 AA, SHA256 confirmed). The annotation is experimentally supported, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains recognizable SAM-dependent methyltransferase motifs (GGSLGH, DWDW/DWDG) indicating a Rossmann-fold class I methyltransferase. However, methyltransferases are ubiquitous across all four listed pathways: pyrimidine metabolism (e.g., thymidylate synthase), tetrahydrofolate interconversion (folate-dependent methyl transfer), glycan degradation (rare but possible), and secondary metabolite biosynthesis. No sequence motif uniquely identifies this enzyme as belonging to secondary metabolite biosynthesis rather than central metabolism methylation.",
    "missing_item_specific_fact": "The specific identity of this protein as FrzF, a cluster-specific O-methyltransferase in the FR901483 biosynthetic gene cluster of Cladobotryum sp., is required to assign it to 'Secondary metabolite biosynthesis' rather than a central metabolic methylation pathway. This requires knowledge of the organism (fungal), the gene cluster context, and the specific substrate methylated by this enzyme.",
    "reason": "While the sequence reveals methyltransferase function through conserved motifs, the pathway assignment among the four choices depends on knowing this is a specialized fungal biosynthetic cluster enzyme rather than a central metabolism methyltransferase. The sequence alone does not provide sufficient grounds to distinguish secondary metabolite biosynthesis from tetrahydrofolate interconversion or pyrimidine metabolism, all of which involve methyl transfer reactions."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Option D (tetrahydrofolate interconversion) is a plausible distractor because methyltransferases participate in folate cycling, and without knowing the specific substrate and organism context, a model might reason that a SAM-dependent methyltransferase could be involved in folate metabolism. However, the protein lacks canonical DHFR or serine hydroxymethyltransferase features, making D less defensible than B for a knowledgeable reviewer. The distinction ultimately requires item-specific knowledge."
  },
  "important_caveats": [
    "The pathway annotation carries ECO:0000269 (direct assay), indicating experimental confirmation rather than computational inference.",
    "The protein is from Cladobotryum sp. (a fungus), and the 'secondary metabolite' designation reflects its role in a specialized biosynthetic cluster (FR901483), not a general metabolic pathway.",
    "The sequence motifs (GGSLGH, DWDW) confirm methyltransferase function but do not specify the pathway without additional context.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely solely on sequence analysis and general biological knowledge."
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

**Accession:** `A0A7T8J1Z8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis cluster protein F"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"O-methyltransferase FrzF"}}}
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"Secondary metabolite biosynthesis"}]}
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Tamura Y.","Tang M.","Qiao T.","Sato M.","Otsu Y.","Sasamura S.","Taniguchi M.","Watanabe K.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33372776"},{"database":"DOI","id":"10.1021/jacs.0c12352"}],"citationType":"journal article","firstPage":"132","id":"33372776","journal":"J. Am. Chem. Soc.","lastPage":"136","publicationDate":"2021","title":"Biosynthesis of the Immunosuppressant (-)-FR901483.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"11231"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:54.122159+00:00.  

```text
ID   FRZF_CLASX              Reviewed;         427 AA.
AC   A0A7T8J1Z8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-JUN-2021, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=O-methyltransferase FrzF {ECO:0000303|PubMed:33372776};
DE            EC=2.1.1.- {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein F {ECO:0000303|PubMed:33372776};
GN   Name=FrzF {ECO:0000303|PubMed:33372776};
OS   Cladobotryum sp.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.
OX   NCBI_TaxID=2040732;
```

Source SHA-256: `b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)  
**Locator:** `lines 14-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:54.122159+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND
RP   PATHWAY.
RC   STRAIN=11231;
RX   PubMed=33372776; DOI=10.1021/jacs.0c12352;
RA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,
RA   Taniguchi M., Watanabe K., Tang Y.;
RT   "Biosynthesis of the Immunosuppressant (-)-FR901483.";
RL   J. Am. Chem. Soc. 143:132-136(2021).
```

Source SHA-256: `b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)  
**Locator:** `lines 72-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:54.122159+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis.
CC       {ECO:0000269|PubMed:33372776}.
```

Source SHA-256: `b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
