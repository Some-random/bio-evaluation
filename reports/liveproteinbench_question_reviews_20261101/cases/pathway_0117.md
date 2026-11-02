# pathway_0117

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Antifungal biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MYDVIVVGAGWCGLAAAKTYLQTCPTARLLVVDGDSSIGGTWSKERLYPHLVAEAHYGLFEFSDLPMRREGILPDGRIPSAAVHAYLTEYATKFGLLPRIRLNTWIEDIRQDPTAIGDDKAPYWTLQVAGSSQPLQARKLIIATGLTSEPRMPSFPGREDFEGHVLHSKMMGRADTGKLLNDPSIRHVVVYGGSKSAFDAVYLLLRAGKTVDWVIREGGGGPSIMTPLNILGQPSFRLNNSRVMSLFSPNPFEVAGERSWWQRVMHQRAGTFAQLLVVWFWRVLAYLLQRPWKYDYSVNGKQLKPILGLDSVLWSPATLGVMTHPTLWEDIHSGERVTIRRQNITALGQNKHVVLSNGDRITADMVVCATGWHARHSLFTPDEQLAVGLPSTSSFDPKSQAHWLNLQKAADEEILEEFPLLQNCPIALPPVRCEDDHHLYRFVAPSSGPLAQERLIAYVGFLRTTGAPIVYEAQSLWATAYLTGALHVPALEEREKEVARTNAWIRRRYICGRKVPFALFDFLPYVDMLYRDLGVNSRRKKNAVSE

[Multiple Choices]
A. Alkaloid biosynthesis
B. Antifungal biosynthesis. .
C. chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7. .
D. tetrahydrofolate biosynthesis
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

> The exact sequence matches a UniProt entry annotated with the pathway “Antifungal biosynthesis.” The annotation is linked to a cited publication, though the supplied evidence does not independently establish the experimental basis for that assignment.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is annotated as a FAD-dependent monooxygenase, but that broad enzyme class does not by itself distinguish antifungal biosynthesis from the other listed pathways.


**Missing item-specific fact**

> The protein-specific association with the antifungal biosynthetic pathway, reported in the cited literature and database annotation.


**Reason**

> The pathway association is not provided in the question. Recognizing the sequence or retrieving its protein-specific annotation would be needed to select B; generic sequence-based enzyme-family clues do not establish that pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence’s pathway annotation supports B; the other choices are not supported by the supplied sequence information alone.


### Important caveats

- The pathway annotation is database evidence associated with a publication, not an independently reviewed experimental result in the supplied evidence.
- The exact author source snapshot is unknown, although the sequence matches both the archived and current UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is annotated as a FAD-dependent monooxygenase, but that broad enzyme class does not by itself distinguish antifungal biosynthesis from the other listed pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific association with the antifungal biosynthetic pathway, reported in the cited literature and database annotation.",
    "reason": "The pathway association is not provided in the question. Recognizing the sequence or retrieving its protein-specific annotation would be needed to select B; generic sequence-based enzyme-family clues do not establish that pathway."
  },
  "case_id": "pathway_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with the pathway “Antifungal biosynthesis.” The annotation is linked to a cited publication, though the supplied evidence does not independently establish the experimental basis for that assignment."
  },
  "important_caveats": [
    "The pathway annotation is database evidence associated with a publication, not an independently reviewed experimental result in the supplied evidence.",
    "The exact author source snapshot is unknown, although the sequence matches both the archived and current UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence’s pathway annotation supports B; the other choices are not supported by the supplied sequence information alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with the pathway “Antifungal biosynthesis.” The annotation is linked to a cited publication, though the supplied evidence does not independently establish the experimental basis for that assignment.",
    "evidence_ids": ["H3", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is annotated as a FAD-dependent monooxygenase, but that broad enzyme class does not by itself distinguish antifungal biosynthesis from the other listed pathways.",
    "missing_item_specific_fact": "The protein-specific association with the antifungal biosynthetic pathway, reported in the cited literature and database annotation.",
    "reason": "The pathway association is not provided in the question. Recognizing the sequence or retrieving its protein-specific annotation would be needed to select B; generic sequence-based enzyme-family clues do not establish that pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence’s pathway annotation supports B; the other choices are not supported by the supplied sequence information alone."
  },
  "important_caveats": [
    "The pathway annotation is database evidence associated with a publication, not an independently reviewed experimental result in the supplied evidence.",
    "The exact author source snapshot is unknown, although the sequence matches both the archived and current UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXV6 (LAN4_PYRDE) explicitly annotates the pathway as 'Antifungal biosynthesis' (evidence C5, H3), supported by PubMed:33857369. The protein is a FAD-dependent monooxygenase in the lanomycin biosynthetic gene cluster of Pyrenophora dematioidea. Lanomycin is a natural product CYP51 inhibitor (antifungal agent), making the pathway annotation 'Antifungal biosynthesis' (i.e., biosynthesis of an antifungal compound) scientifically accurate. The sequence matches the reviewed entry exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence shows a FAD-dependent monooxygenase (Rossmann-fold-like GxGxxG motifs near N-terminus, GGGK nucleotide-binding motifs) from a fungal source. Options C (shikimate pathway step 7/7, EPSP synthase) and D (tetrahydrofolate biosynthesis) can be excluded by general knowledge: these involve specific bacterial/plant enzymes unrelated to fungal FAD monooxygenases. However, distinguishing 'Antifungal biosynthesis' (B) from 'Alkaloid biosynthesis' (A) requires knowing that this particular FAD monooxygenase participates in lanomycin biosynthesis and that lanomycin is classified as an antifungal CYP51 inhibitor rather than an alkaloid. No sequence feature or general biological principle distinguishes a fungal secondary-metabolite FAD monooxygenase as belonging to 'antifungal biosynthesis' versus 'alkaloid biosynthesis' without the item-specific gene-cluster annotation.


**Missing item-specific fact**

> The identity of this protein as 'Lanomycin biosynthesis cluster protein 4' and the classification of lanomycin as an antifungal compound (CYP51 inhibitor) rather than an alkaloid. This is a protein-specific database annotation (PubMed:33857369) not derivable from the amino acid sequence alone.


**Reason**

> While options C and D are eliminable by general pathway knowledge, the critical discrimination between A and B requires knowing the specific biosynthetic gene cluster membership and the pharmacological classification of the product (lanomycin = antifungal, not alkaloid). This is an item-specific annotation fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly incorrect for a fungal FAD monooxygenase. Option A (Alkaloid biosynthesis) is a plausible-sounding distractor for a fungal secondary-metabolite enzyme but is factually wrong since lanomycin is a polyene macrolide-type antifungal, not an alkaloid. Only B matches the UniProt pathway annotation. No other option is genuinely defensible given the actual protein identity.


### Important caveats

- The UniProt pathway annotation 'Antifungal biosynthesis' refers to biosynthesis of an antifungal compound (lanomycin), not to a host-defense antifungal pathway. The phrasing could confuse a reader into thinking it refers to the organism's own antifungal defense.
- The entry was first publicly released on 2025-02-05 (entry version 2 archived by 2025-04-09). If the benchmark was constructed before this date, the annotation may not have been available in the author's source snapshot.
- The pathway label 'Antifungal biosynthesis' is a UniProt-curated term specific to this gene cluster; it is not a standard KEGG/MetaCyc pathway name, which may affect generalizability of the answer format.
- All reviewer evidence is post-hoc and was absent from the evaluated model's input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence shows a FAD-dependent monooxygenase (Rossmann-fold-like GxGxxG motifs near N-terminus, GGGK nucleotide-binding motifs) from a fungal source. Options C (shikimate pathway step 7/7, EPSP synthase) and D (tetrahydrofolate biosynthesis) can be excluded by general knowledge: these involve specific bacterial/plant enzymes unrelated to fungal FAD monooxygenases. However, distinguishing 'Antifungal biosynthesis' (B) from 'Alkaloid biosynthesis' (A) requires knowing that this particular FAD monooxygenase participates in lanomycin biosynthesis and that lanomycin is classified as an antifungal CYP51 inhibitor rather than an alkaloid. No sequence feature or general biological principle distinguishes a fungal secondary-metabolite FAD monooxygenase as belonging to 'antifungal biosynthesis' versus 'alkaloid biosynthesis' without the item-specific gene-cluster annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of this protein as 'Lanomycin biosynthesis cluster protein 4' and the classification of lanomycin as an antifungal compound (CYP51 inhibitor) rather than an alkaloid. This is a protein-specific database annotation (PubMed:33857369) not derivable from the amino acid sequence alone.",
    "reason": "While options C and D are eliminable by general pathway knowledge, the critical discrimination between A and B requires knowing the specific biosynthetic gene cluster membership and the pharmacological classification of the product (lanomycin = antifungal, not alkaloid). This is an item-specific annotation fact."
  },
  "case_id": "pathway_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXV6 (LAN4_PYRDE) explicitly annotates the pathway as 'Antifungal biosynthesis' (evidence C5, H3), supported by PubMed:33857369. The protein is a FAD-dependent monooxygenase in the lanomycin biosynthetic gene cluster of Pyrenophora dematioidea. Lanomycin is a natural product CYP51 inhibitor (antifungal agent), making the pathway annotation 'Antifungal biosynthesis' (i.e., biosynthesis of an antifungal compound) scientifically accurate. The sequence matches the reviewed entry exactly."
  },
  "important_caveats": [
    "The UniProt pathway annotation 'Antifungal biosynthesis' refers to biosynthesis of an antifungal compound (lanomycin), not to a host-defense antifungal pathway. The phrasing could confuse a reader into thinking it refers to the organism's own antifungal defense.",
    "The entry was first publicly released on 2025-02-05 (entry version 2 archived by 2025-04-09). If the benchmark was constructed before this date, the annotation may not have been available in the author's source snapshot.",
    "The pathway label 'Antifungal biosynthesis' is a UniProt-curated term specific to this gene cluster; it is not a standard KEGG/MetaCyc pathway name, which may affect generalizability of the answer format.",
    "All reviewer evidence is post-hoc and was absent from the evaluated model's input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incorrect for a fungal FAD monooxygenase. Option A (Alkaloid biosynthesis) is a plausible-sounding distractor for a fungal secondary-metabolite enzyme but is factually wrong since lanomycin is a polyene macrolide-type antifungal, not an alkaloid. Only B matches the UniProt pathway annotation. No other option is genuinely defensible given the actual protein identity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXV6 (LAN4_PYRDE) explicitly annotates the pathway as 'Antifungal biosynthesis' (evidence C5, H3), supported by PubMed:33857369. The protein is a FAD-dependent monooxygenase in the lanomycin biosynthetic gene cluster of Pyrenophora dematioidea. Lanomycin is a natural product CYP51 inhibitor (antifungal agent), making the pathway annotation 'Antifungal biosynthesis' (i.e., biosynthesis of an antifungal compound) scientifically accurate. The sequence matches the reviewed entry exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence shows a FAD-dependent monooxygenase (Rossmann-fold-like GxGxxG motifs near N-terminus, GGGK nucleotide-binding motifs) from a fungal source. Options C (shikimate pathway step 7/7, EPSP synthase) and D (tetrahydrofolate biosynthesis) can be excluded by general knowledge: these involve specific bacterial/plant enzymes unrelated to fungal FAD monooxygenases. However, distinguishing 'Antifungal biosynthesis' (B) from 'Alkaloid biosynthesis' (A) requires knowing that this particular FAD monooxygenase participates in lanomycin biosynthesis and that lanomycin is classified as an antifungal CYP51 inhibitor rather than an alkaloid. No sequence feature or general biological principle distinguishes a fungal secondary-metabolite FAD monooxygenase as belonging to 'antifungal biosynthesis' versus 'alkaloid biosynthesis' without the item-specific gene-cluster annotation.",
    "missing_item_specific_fact": "The identity of this protein as 'Lanomycin biosynthesis cluster protein 4' and the classification of lanomycin as an antifungal compound (CYP51 inhibitor) rather than an alkaloid. This is a protein-specific database annotation (PubMed:33857369) not derivable from the amino acid sequence alone.",
    "reason": "While options C and D are eliminable by general pathway knowledge, the critical discrimination between A and B requires knowing the specific biosynthetic gene cluster membership and the pharmacological classification of the product (lanomycin = antifungal, not alkaloid). This is an item-specific annotation fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incorrect for a fungal FAD monooxygenase. Option A (Alkaloid biosynthesis) is a plausible-sounding distractor for a fungal secondary-metabolite enzyme but is factually wrong since lanomycin is a polyene macrolide-type antifungal, not an alkaloid. Only B matches the UniProt pathway annotation. No other option is genuinely defensible given the actual protein identity."
  },
  "important_caveats": [
    "The UniProt pathway annotation 'Antifungal biosynthesis' refers to biosynthesis of an antifungal compound (lanomycin), not to a host-defense antifungal pathway. The phrasing could confuse a reader into thinking it refers to the organism's own antifungal defense.",
    "The entry was first publicly released on 2025-02-05 (entry version 2 archived by 2025-04-09). If the benchmark was constructed before this date, the annotation may not have been available in the author's source snapshot.",
    "The pathway label 'Antifungal biosynthesis' is a UniProt-curated term specific to this gene cluster; it is not a standard KEGG/MetaCyc pathway name, which may affect generalizability of the answer format.",
    "All reviewer evidence is post-hoc and was absent from the evaluated model's input."
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

**Accession:** `P0DXV6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:48.282490+00:00.  

```json
"P0DXV6"
```

Source SHA-256: `604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:48.282490+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Lanomycin biosynthesis cluster protein 4"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"1.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"FAD-dependent monooxygenase"}}}
```

Source SHA-256: `604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV6.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:48.282490+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"Antifungal biosynthesis"}]}
```

Source SHA-256: `604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV6.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:48.282490+00:00.  

```json
{"citation":{"authors":["Liu N.","Abramyan E.D.","Cheng W.","Perlatti B.","Harvey C.J.B.","Bills G.F.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33857369"},{"database":"DOI","id":"10.1021/jacs.1c01516"}],"citationType":"journal article","firstPage":"6043","id":"33857369","journal":"J. Am. Chem. Soc.","lastPage":"6047","publicationDate":"2021","title":"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"TTI-1096"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","PATHWAY"]}
```

Source SHA-256: `604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:50.838620+00:00.  

```text
ID   LAN4_PYRDE              Reviewed;         546 AA.
AC   P0DXV6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   09-APR-2025, entry version 2.
DE   RecName: Full=FAD-dependent monooxygenase {ECO:0000303|PubMed:33857369};
DE            EC=1.-.-.- {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Lanomycin biosynthesis cluster protein 4 {ECO:0000303|PubMed:33857369};
DE   Flags: Precursor;
GN   Name=ORF4 {ECO:0000303|PubMed:33857369};
OS   Pyrenophora dematioidea (Helminthosporium dematioideum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Pleosporomycetidae; Pleosporales; Pleosporineae; Pleosporaceae;
OC   Pyrenophora.
OX   NCBI_TaxID=139229;
```

Source SHA-256: `1aa3327dc9591ccf3b323653d57490eeb83ea02899e48e37df4e6dc51b099591`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2)  
**Locator:** `lines 16-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:50.838620+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.
RC   STRAIN=TTI-1096;
RX   PubMed=33857369; DOI=10.1021/jacs.1c01516;
RA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,
RA   Tang Y.;
RT   "Targeted genome mining reveals the biosynthetic gene clusters of natural
RT   product CYP51 inhibitors.";
RL   J. Am. Chem. Soc. 143:6043-6047(2021).
```

Source SHA-256: `1aa3327dc9591ccf3b323653d57490eeb83ea02899e48e37df4e6dc51b099591`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2)  
**Locator:** `lines 37-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:50.838620+00:00.  

```text
CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000305|PubMed:33857369}.
```

Source SHA-256: `1aa3327dc9591ccf3b323653d57490eeb83ea02899e48e37df4e6dc51b099591`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
