# catalytic_activity_0092

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — cyclo(L-Trp-L-Trp) + 2 dimethylallyl diphosphate = cyclo(N(8)-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dimethylallyl)-L-Trp) + 2 diphosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTVTKEAPEVMPFEGLTEEINLMSDNERVWWQKTGSMLSRVLSSADYTWKEQHKHLKFYAQVLLPHLGPYPQSFRSSITRSGLPFELSINYQQNGNPLVVRIGFEPLNALSGTPDDPFNQAPAAEVLSLLDQMHIPGFDSQIWDKAVEHHTVNHTEREALRDSDLGAGYIRSQTAYGFDLLRDGNIAVKGYSFPALKCQITGQSMAQMMAGLVADLAPLVDCSQAFAIVDEYLQDTGYDERAFFSWDFVEPSRSRLKLYTGSSSVTWGKLAEVWTLGNRVQNPTVARGLEYLRQLFDLIKLSDGQRNIVVAFDDRQDSSKETPLLWNYEMRAGDPTPLTKIYFPVHGENDLQVINGVAEFLCQIGLSHGKTYVEKVKSYYPGIDLSTTERFTSWVSFAYTEKTGVYLSTYYHSSTDNPWKMTTEEDSQL

[Multiple Choices]
A. apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)
B. O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine + succinate + H(+)
C. cyclo(L-Trp-L-Trp) + 2 dimethylallyl diphosphate = cyclo(N(8)-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dimethylallyl)-L-Trp) + 2 diphosphate
D. UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-galactosamine
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

> The supplied sequence exactly matches the UniProt sequence for this protein. Its catalytic-activity annotation gives the reaction in choice C and cites ECO:0000269 evidence linked to the 2017 paper. This supports the key, although the cited experiment was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Recognizing a prenyltransferase-like enzyme could make prenylation a plausible reaction class, but the sequence and choices alone do not establish this protein's specific substrate, reaction, or prenylation sites.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental finding that this enzyme prenylates cyclo(L-Trp-L-Trp) twice to produce the product in choice C.


**Reason**

> Choosing C requires knowing the substrate specificity and product of this particular enzyme; broad sequence-based classification would not establish that exact transformation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reactions, and the sequence-matched annotation supports choice C.


### Important caveats

- The UniProt annotation is linked to experimental evidence, but the primary paper was not independently validated here.
- The exact data-source snapshot used by the question author is unknown; the checked historical and current entries match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Recognizing a prenyltransferase-like enzyme could make prenylation a plausible reaction class, but the sequence and choices alone do not establish this protein's specific substrate, reaction, or prenylation sites.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this enzyme prenylates cyclo(L-Trp-L-Trp) twice to produce the product in choice C.",
    "reason": "Choosing C requires knowing the substrate specificity and product of this particular enzyme; broad sequence-based classification would not establish that exact transformation."
  },
  "case_id": "catalytic_activity_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for this protein. Its catalytic-activity annotation gives the reaction in choice C and cites ECO:0000269 evidence linked to the 2017 paper. This supports the key, although the cited experiment was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt annotation is linked to experimental evidence, but the primary paper was not independently validated here.",
    "The exact data-source snapshot used by the question author is unknown; the checked historical and current entries match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the sequence-matched annotation supports choice C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for this protein. Its catalytic-activity annotation gives the reaction in choice C and cites ECO:0000269 evidence linked to the 2017 paper. This supports the key, although the cited experiment was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Recognizing a prenyltransferase-like enzyme could make prenylation a plausible reaction class, but the sequence and choices alone do not establish this protein's specific substrate, reaction, or prenylation sites.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this enzyme prenylates cyclo(L-Trp-L-Trp) twice to produce the product in choice C.",
    "reason": "Choosing C requires knowing the substrate specificity and product of this particular enzyme; broad sequence-based classification would not establish that exact transformation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the sequence-matched annotation supports choice C."
  },
  "important_caveats": [
    "The UniProt annotation is linked to experimental evidence, but the primary paper was not independently validated here.",
    "The exact data-source snapshot used by the question author is unknown; the checked historical and current entries match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A2Z5U367 (OKAC_PENOH, Prenyltransferase okaC from Penicillium ochrochloron) is sequence-matched to the benchmark input (SHA256 identical, 429 aa). The catalytic activity annotation (C5, H4) explicitly states the reaction in Choice C verbatim, supported by experimental evidence (ECO:0000269|PubMed:28631282, Lai et al. Angew. Chem. Int. Ed. 2017). The EC number 2.5.1.- (transferase, transferring alkyl/aryl groups) is consistent with a prenyltransferase.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> In principle, if one could identify the protein as a prenyltransferase (EC 2.5.1.-) from sequence motifs (e.g., tryptophan-rich regions common in fungal indole prenyltransferases), then among the four options only C describes a prenyltransferase reaction; A is a nucleotidyltransferase, B is a PLP-dependent γ-synthase, and D is an epimerase. However, no universally recognized, unambiguous sequence motif in the provided 429-aa sequence definitively identifies this as a prenyltransferase acting on cyclo(L-Trp-L-Trp) with double DMAPP prenylation at N8 and 6a positions.


**Missing item-specific fact**

> The specific substrate identity (cyclo(L-Trp-L-Trp)), the exact prenylation positions (N8 and 6a), the stoichiometry (2 DMAPP), and the product structure are highly specific biochemical facts established experimentally in Lai et al. 2017 (PubMed:28631282). These cannot be deduced from general sequence features without database lookup or memorization of this particular protein's characterized activity.


**Reason**

> Identifying this protein's exact catalytic reaction from its amino acid sequence alone requires either recognizing it as a specific fungal indole prenyltransferase (a specialized, non-obvious motif-based inference) or recalling the UniProt/literature annotation. The specificity of the substrate (cyclo(L-Trp-L-Trp)) and the regiochemistry of double prenylation are item-specific experimental facts not derivable from general biological reasoning on the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent entirely different enzyme classes (nucleotidyltransferase, PLP-dependent γ-synthase, prenyltransferase, epimerase), so once the enzyme class is identified, only one option is viable. There is no genuine ambiguity among the choices; the difficulty lies solely in identifying the enzyme class from the sequence.


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269) from a 2017 Angew. Chem. paper, so the catalytic activity is experimentally established, not merely computational.
- The sequence match is exact (SHA256 confirmed) between the benchmark input and UniProt A0A2Z5U367.
- Fungal indole prenyltransferases do share some conserved features (e.g., tryptophan-rich stretches), but these are not sufficient for unambiguous identification without specialized knowledge or database access.
- The entry was first publicly released in 2025-02-05; the underlying experimental data is from 2017, so the knowledge predates the benchmark construction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "In principle, if one could identify the protein as a prenyltransferase (EC 2.5.1.-) from sequence motifs (e.g., tryptophan-rich regions common in fungal indole prenyltransferases), then among the four options only C describes a prenyltransferase reaction; A is a nucleotidyltransferase, B is a PLP-dependent γ-synthase, and D is an epimerase. However, no universally recognized, unambiguous sequence motif in the provided 429-aa sequence definitively identifies this as a prenyltransferase acting on cyclo(L-Trp-L-Trp) with double DMAPP prenylation at N8 and 6a positions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (cyclo(L-Trp-L-Trp)), the exact prenylation positions (N8 and 6a), the stoichiometry (2 DMAPP), and the product structure are highly specific biochemical facts established experimentally in Lai et al. 2017 (PubMed:28631282). These cannot be deduced from general sequence features without database lookup or memorization of this particular protein's characterized activity.",
    "reason": "Identifying this protein's exact catalytic reaction from its amino acid sequence alone requires either recognizing it as a specific fungal indole prenyltransferase (a specialized, non-obvious motif-based inference) or recalling the UniProt/literature annotation. The specificity of the substrate (cyclo(L-Trp-L-Trp)) and the regiochemistry of double prenylation are item-specific experimental facts not derivable from general biological reasoning on the sequence."
  },
  "case_id": "catalytic_activity_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A2Z5U367 (OKAC_PENOH, Prenyltransferase okaC from Penicillium ochrochloron) is sequence-matched to the benchmark input (SHA256 identical, 429 aa). The catalytic activity annotation (C5, H4) explicitly states the reaction in Choice C verbatim, supported by experimental evidence (ECO:0000269|PubMed:28631282, Lai et al. Angew. Chem. Int. Ed. 2017). The EC number 2.5.1.- (transferase, transferring alkyl/aryl groups) is consistent with a prenyltransferase."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2017 Angew. Chem. paper, so the catalytic activity is experimentally established, not merely computational.",
    "The sequence match is exact (SHA256 confirmed) between the benchmark input and UniProt A0A2Z5U367.",
    "Fungal indole prenyltransferases do share some conserved features (e.g., tryptophan-rich stretches), but these are not sufficient for unambiguous identification without specialized knowledge or database access.",
    "The entry was first publicly released in 2025-02-05; the underlying experimental data is from 2017, so the knowledge predates the benchmark construction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes (nucleotidyltransferase, PLP-dependent γ-synthase, prenyltransferase, epimerase), so once the enzyme class is identified, only one option is viable. There is no genuine ambiguity among the choices; the difficulty lies solely in identifying the enzyme class from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A2Z5U367 (OKAC_PENOH, Prenyltransferase okaC from Penicillium ochrochloron) is sequence-matched to the benchmark input (SHA256 identical, 429 aa). The catalytic activity annotation (C5, H4) explicitly states the reaction in Choice C verbatim, supported by experimental evidence (ECO:0000269|PubMed:28631282, Lai et al. Angew. Chem. Int. Ed. 2017). The EC number 2.5.1.- (transferase, transferring alkyl/aryl groups) is consistent with a prenyltransferase.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "In principle, if one could identify the protein as a prenyltransferase (EC 2.5.1.-) from sequence motifs (e.g., tryptophan-rich regions common in fungal indole prenyltransferases), then among the four options only C describes a prenyltransferase reaction; A is a nucleotidyltransferase, B is a PLP-dependent γ-synthase, and D is an epimerase. However, no universally recognized, unambiguous sequence motif in the provided 429-aa sequence definitively identifies this as a prenyltransferase acting on cyclo(L-Trp-L-Trp) with double DMAPP prenylation at N8 and 6a positions.",
    "missing_item_specific_fact": "The specific substrate identity (cyclo(L-Trp-L-Trp)), the exact prenylation positions (N8 and 6a), the stoichiometry (2 DMAPP), and the product structure are highly specific biochemical facts established experimentally in Lai et al. 2017 (PubMed:28631282). These cannot be deduced from general sequence features without database lookup or memorization of this particular protein's characterized activity.",
    "reason": "Identifying this protein's exact catalytic reaction from its amino acid sequence alone requires either recognizing it as a specific fungal indole prenyltransferase (a specialized, non-obvious motif-based inference) or recalling the UniProt/literature annotation. The specificity of the substrate (cyclo(L-Trp-L-Trp)) and the regiochemistry of double prenylation are item-specific experimental facts not derivable from general biological reasoning on the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes (nucleotidyltransferase, PLP-dependent γ-synthase, prenyltransferase, epimerase), so once the enzyme class is identified, only one option is viable. There is no genuine ambiguity among the choices; the difficulty lies solely in identifying the enzyme class from the sequence."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2017 Angew. Chem. paper, so the catalytic activity is experimentally established, not merely computational.",
    "The sequence match is exact (SHA256 confirmed) between the benchmark input and UniProt A0A2Z5U367.",
    "Fungal indole prenyltransferases do share some conserved features (e.g., tryptophan-rich stretches), but these are not sufficient for unambiguous identification without specialized knowledge or database access.",
    "The entry was first publicly released in 2025-02-05; the underlying experimental data is from 2017, so the knowledge predates the benchmark construction."
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

**Accession:** `A0A2Z5U367` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 17. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U367.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.637409+00:00.  

```json
"A0A2Z5U367"
```

Source SHA-256: `745553ffe5a45d604d8813919c97ac2acacebb93a50f27ada859db8468138868`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U367.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.637409+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Okaramines biosynthesis cluster protein C"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"value":"2.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Prenyltransferase okaC"}}}
```

Source SHA-256: `745553ffe5a45d604d8813919c97ac2acacebb93a50f27ada859db8468138868`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U367.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.637409+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:82696"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"name":"cyclo(L-Trp-L-Trp) + 2 dimethylallyl diphosphate = cyclo(N(8)-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dimethylallyl)-L-Trp) + 2 diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:82695"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:57623"},{"database":"ChEBI","id":"CHEBI:181817"},{"database":"ChEBI","id":"CHEBI:232460"}]}}
```

Source SHA-256: `745553ffe5a45d604d8813919c97ac2acacebb93a50f27ada859db8468138868`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U367.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.637409+00:00.  

```json
{"citation":{"authors":["Lai C.Y.","Lo I.W.","Hewage R.T.","Chen Y.C.","Chen C.T.","Lee C.F.","Lin S.","Tang M.C.","Lin H.C."],"citationCrossReferences":[{"database":"PubMed","id":"28631282"},{"database":"DOI","id":"10.1002/anie.201705501"}],"citationType":"journal article","firstPage":"9478","id":"28631282","journal":"Angew. Chem. Int. Ed.","lastPage":"9482","publicationDate":"2017","title":"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise Pathway of Okaramines.","volume":"56"},"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `745553ffe5a45d604d8813919c97ac2acacebb93a50f27ada859db8468138868`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U367?format=txt&versions=17)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:24:53.857223+00:00.  

```text
ID   OKAC_PENOH              Reviewed;         429 AA.
AC   A0A2Z5U367;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-OCT-2018, sequence version 1.
DT   28-JAN-2026, entry version 17.
DE   RecName: Full=Prenyltransferase okaC {ECO:0000303|PubMed:28631282};
DE            EC=2.5.1.- {ECO:0000269|PubMed:28631282};
DE   AltName: Full=Okaramines biosynthesis cluster protein C {ECO:0000303|PubMed:28631282};
GN   Name=okaC {ECO:0000303|PubMed:28631282};
OS   Penicillium ochrochloron.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=69780;
```

Source SHA-256: `416679d3c491f97848e803aee8701828ad6e72beb06f8d3e3bffdc5bcae8d22d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U367?format=txt&versions=17)  
**Locator:** `lines 59-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:24:53.857223+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=cyclo(L-Trp-L-Trp) + 2 dimethylallyl diphosphate = cyclo(N(8)-
CC         (alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dimethylallyl)-L-
CC         Trp) + 2 diphosphate; Xref=Rhea:RHEA:82695, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:57623, ChEBI:CHEBI:181817, ChEBI:CHEBI:232460;
CC         Evidence={ECO:0000269|PubMed:28631282};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82696;
CC         Evidence={ECO:0000269|PubMed:28631282};
```

Source SHA-256: `416679d3c491f97848e803aee8701828ad6e72beb06f8d3e3bffdc5bcae8d22d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 92. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
