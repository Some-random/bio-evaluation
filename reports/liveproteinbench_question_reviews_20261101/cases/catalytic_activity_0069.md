# catalytic_activity_0069

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSPRPQIKVGVLGATGTVGQRFIELLAAHPYFALHALGASSRSAGQQYARVVRWKLPSPIPDAVRHMVVHECRPDAPGFAECGVVFSGLDADVAGDIENAFRAADLVVYSNAKNYRRDPLCPLIVPLVNPSHLSIIPYQREQLGLKKGYIVTNANCSTTGIVVPLAALEKAFGPLDTVIVTTLQAISGAGYPGVSSLDIMDNVVPLISGEEDKIEWETNKILGGVTPDNKAFDLHAPKQINVSATCTRVPVIDGHTGCVSVKFARSPPPSVAEVENAFREYTCDAQHLGVPSAPAQAIVVHDAPDRPQPRLDKNLHNGACVSVGRIRECPVFDIKFVCLIDNVRLGAATSSIINAEIAVEKGLIQ

[Multiple Choices]
A. L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)
B. a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in RNA + ADP + phosphate + CoA + H(+)
C. guanosine in U6 snRNA + S-adenosyl-L-methionine = N(2)-methylguanosine in U6 snRNA + S-adenosyl-L-homocysteine + H(+)
D. D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+)
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

> The supplied sequence exactly matches the UniProt sequence for aspartate-semialdehyde dehydrogenase, annotated EC 1.2.1.11 with the reaction in choice A. The annotation cites experimental evidence, though the cited primary studies were not independently assessed here.

Citations as saved: [H1](#evidence-h1), [H5](#evidence-h5), [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a glycine-rich N-terminal dinucleotide-binding motif (VGVLGATGTVG) and a conserved-looking HxxxC region (HMVVHEC), consistent with an NAD(P)-dependent dehydrogenase family. Among the choices, A is the NADP-dependent dehydrogenase reaction; the other options are RNA modification or acetyl-transfer reactions.


**Missing item-specific fact**

> No indispensable external annotation is required in principle, although identifying the precise enzyme family and substrate from sequence motifs depends on protein-family knowledge.


**Reason**

> The sequence provides meaningful evidence for the dehydrogenase class and cofactor use, which distinguishes A from the alternatives. The motifs alone are not a direct experimental demonstration of the full substrate-specific reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The curated reaction annotation for the exact-matching sequence supports A, and the alternatives describe distinct reaction classes.


### Important caveats

- The reviewer-only UniProt evidence was not supplied to the evaluated model.
- The annotation cites experimental evidence, but the primary papers were not independently retrieved or validated.
- The exact historical source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich N-terminal dinucleotide-binding motif (VGVLGATGTVG) and a conserved-looking HxxxC region (HMVVHEC), consistent with an NAD(P)-dependent dehydrogenase family. Among the choices, A is the NADP-dependent dehydrogenase reaction; the other options are RNA modification or acetyl-transfer reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No indispensable external annotation is required in principle, although identifying the precise enzyme family and substrate from sequence motifs depends on protein-family knowledge.",
    "reason": "The sequence provides meaningful evidence for the dehydrogenase class and cofactor use, which distinguishes A from the alternatives. The motifs alone are not a direct experimental demonstration of the full substrate-specific reaction."
  },
  "case_id": "catalytic_activity_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H5",
      "C1",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for aspartate-semialdehyde dehydrogenase, annotated EC 1.2.1.11 with the reaction in choice A. The annotation cites experimental evidence, though the cited primary studies were not independently assessed here."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence was not supplied to the evaluated model.",
    "The annotation cites experimental evidence, but the primary papers were not independently retrieved or validated.",
    "The exact historical source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The curated reaction annotation for the exact-matching sequence supports A, and the alternatives describe distinct reaction classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for aspartate-semialdehyde dehydrogenase, annotated EC 1.2.1.11 with the reaction in choice A. The annotation cites experimental evidence, though the cited primary studies were not independently assessed here.",
    "evidence_ids": ["H1", "H5", "C1", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a glycine-rich N-terminal dinucleotide-binding motif (VGVLGATGTVG) and a conserved-looking HxxxC region (HMVVHEC), consistent with an NAD(P)-dependent dehydrogenase family. Among the choices, A is the NADP-dependent dehydrogenase reaction; the other options are RNA modification or acetyl-transfer reactions.",
    "missing_item_specific_fact": "No indispensable external annotation is required in principle, although identifying the precise enzyme family and substrate from sequence motifs depends on protein-family knowledge.",
    "reason": "The sequence provides meaningful evidence for the dehydrogenase class and cofactor use, which distinguishes A from the alternatives. The motifs alone are not a direct experimental demonstration of the full substrate-specific reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The curated reaction annotation for the exact-matching sequence supports A, and the alternatives describe distinct reaction classes."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence was not supplied to the evaluated model.",
    "The annotation cites experimental evidence, but the primary papers were not independently retrieved or validated.",
    "The exact historical source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5KPK7 (sequence matched exactly, 365 aa) is annotated as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)' supported by experimental evidence (ECO:0000269 from PubMed:26527262 and PubMed:29608391). X-ray crystallography (PDB 5CEF, 2.60 Å) independently confirms the function. The expected answer matches the annotated reaction exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear GxGxxG motif ('GVLGATG' at positions ~5-11), the hallmark of a Rossmann fold for nucleotide (NAD/NADP) binding. This immediately eliminates choices B and D, which require acetyl-CoA as a cofactor and belong to the acetyltransferase family (no Rossmann fold). Between the remaining A (NADP-dependent dehydrogenase) and C (SAM-dependent methyltransferase), the 'ANCSTTG' motif near position 170 contains a catalytic cysteine characteristic of aspartate-semialdehyde dehydrogenase's active site, and the overall ~365-aa single-domain architecture with the dehydrogenase-type fold pattern is inconsistent with a typical RNA methyltransferase. The 'GHTGCVSVK' region further supports a dehydrogenase active-site environment.


**Missing item-specific fact**

> None strictly required. Recognizing the GxGxxG Rossmann motif and the ANC catalytic-cysteine motif as hallmarks of NAD(P)-dependent dehydrogenases (specifically ASADH) is general structural-biochemistry knowledge.


**Reason**

> The GxGxxG motif eliminates acetyltransferase options (B, D) through general fold knowledge. The ANC catalytic motif and overall dehydrogenase architecture distinguish A from C (methyltransferase) using recognizable active-site signatures. While distinguishing A from C is more challenging than eliminating B/D, it relies on well-established motif knowledge rather than memorizing a single database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices B and D are clearly eliminated by the Rossmann-fold GxGxxG motif (incompatible with acetyl-CoA-dependent acetyltransferases). Choice C (SAM-dependent methyltransferase) is less clearly eliminated by the GxGxxG motif alone (methyltransferases also use Rossmann folds), but the ANC catalytic-cysteine motif, the specific domain architecture, and the absence of a typical methyltransferase catalytic core (e.g., motif I with the conserved aspartate) argue against it. Choice A remains the single most defensible answer.


### Important caveats

- The GxGxxG Rossmann motif is shared by NAD(P)-dependent dehydrogenases and SAM-dependent methyltransferases; distinguishing A from C relies on recognizing the ANC catalytic motif and overall fold architecture, which is more specialized knowledge.
- The UniProt annotation is supported by experimental evidence (X-ray crystallography PDB 5CEF, enzymatic assays), not merely computational transfer.
- The sequence match to Q5KPK7 is exact (SHA-256 confirmed) in both current and historical (v121) snapshots.
- The physiological direction is noted as right-to-left (reductive amination direction) in the annotation, but the reaction equation as written in choice A is the standard EC 1.2.1.11 formulation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear GxGxxG motif ('GVLGATG' at positions ~5-11), the hallmark of a Rossmann fold for nucleotide (NAD/NADP) binding. This immediately eliminates choices B and D, which require acetyl-CoA as a cofactor and belong to the acetyltransferase family (no Rossmann fold). Between the remaining A (NADP-dependent dehydrogenase) and C (SAM-dependent methyltransferase), the 'ANCSTTG' motif near position 170 contains a catalytic cysteine characteristic of aspartate-semialdehyde dehydrogenase's active site, and the overall ~365-aa single-domain architecture with the dehydrogenase-type fold pattern is inconsistent with a typical RNA methyltransferase. The 'GHTGCVSVK' region further supports a dehydrogenase active-site environment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Recognizing the GxGxxG Rossmann motif and the ANC catalytic-cysteine motif as hallmarks of NAD(P)-dependent dehydrogenases (specifically ASADH) is general structural-biochemistry knowledge.",
    "reason": "The GxGxxG motif eliminates acetyltransferase options (B, D) through general fold knowledge. The ANC catalytic motif and overall dehydrogenase architecture distinguish A from C (methyltransferase) using recognizable active-site signatures. While distinguishing A from C is more challenging than eliminating B/D, it relies on well-established motif knowledge rather than memorizing a single database entry."
  },
  "case_id": "catalytic_activity_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5KPK7 (sequence matched exactly, 365 aa) is annotated as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)' supported by experimental evidence (ECO:0000269 from PubMed:26527262 and PubMed:29608391). X-ray crystallography (PDB 5CEF, 2.60 Å) independently confirms the function. The expected answer matches the annotated reaction exactly."
  },
  "important_caveats": [
    "The GxGxxG Rossmann motif is shared by NAD(P)-dependent dehydrogenases and SAM-dependent methyltransferases; distinguishing A from C relies on recognizing the ANC catalytic motif and overall fold architecture, which is more specialized knowledge.",
    "The UniProt annotation is supported by experimental evidence (X-ray crystallography PDB 5CEF, enzymatic assays), not merely computational transfer.",
    "The sequence match to Q5KPK7 is exact (SHA-256 confirmed) in both current and historical (v121) snapshots.",
    "The physiological direction is noted as right-to-left (reductive amination direction) in the annotation, but the reaction equation as written in choice A is the standard EC 1.2.1.11 formulation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B and D are clearly eliminated by the Rossmann-fold GxGxxG motif (incompatible with acetyl-CoA-dependent acetyltransferases). Choice C (SAM-dependent methyltransferase) is less clearly eliminated by the GxGxxG motif alone (methyltransferases also use Rossmann folds), but the ANC catalytic-cysteine motif, the specific domain architecture, and the absence of a typical methyltransferase catalytic core (e.g., motif I with the conserved aspartate) argue against it. Choice A remains the single most defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5KPK7 (sequence matched exactly, 365 aa) is annotated as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)' supported by experimental evidence (ECO:0000269 from PubMed:26527262 and PubMed:29608391). X-ray crystallography (PDB 5CEF, 2.60 Å) independently confirms the function. The expected answer matches the annotated reaction exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear GxGxxG motif ('GVLGATG' at positions ~5-11), the hallmark of a Rossmann fold for nucleotide (NAD/NADP) binding. This immediately eliminates choices B and D, which require acetyl-CoA as a cofactor and belong to the acetyltransferase family (no Rossmann fold). Between the remaining A (NADP-dependent dehydrogenase) and C (SAM-dependent methyltransferase), the 'ANCSTTG' motif near position 170 contains a catalytic cysteine characteristic of aspartate-semialdehyde dehydrogenase's active site, and the overall ~365-aa single-domain architecture with the dehydrogenase-type fold pattern is inconsistent with a typical RNA methyltransferase. The 'GHTGCVSVK' region further supports a dehydrogenase active-site environment.",
    "missing_item_specific_fact": "None strictly required. Recognizing the GxGxxG Rossmann motif and the ANC catalytic-cysteine motif as hallmarks of NAD(P)-dependent dehydrogenases (specifically ASADH) is general structural-biochemistry knowledge.",
    "reason": "The GxGxxG motif eliminates acetyltransferase options (B, D) through general fold knowledge. The ANC catalytic motif and overall dehydrogenase architecture distinguish A from C (methyltransferase) using recognizable active-site signatures. While distinguishing A from C is more challenging than eliminating B/D, it relies on well-established motif knowledge rather than memorizing a single database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B and D are clearly eliminated by the Rossmann-fold GxGxxG motif (incompatible with acetyl-CoA-dependent acetyltransferases). Choice C (SAM-dependent methyltransferase) is less clearly eliminated by the GxGxxG motif alone (methyltransferases also use Rossmann folds), but the ANC catalytic-cysteine motif, the specific domain architecture, and the absence of a typical methyltransferase catalytic core (e.g., motif I with the conserved aspartate) argue against it. Choice A remains the single most defensible answer."
  },
  "important_caveats": [
    "The GxGxxG Rossmann motif is shared by NAD(P)-dependent dehydrogenases and SAM-dependent methyltransferases; distinguishing A from C relies on recognizing the ANC catalytic motif and overall fold architecture, which is more specialized knowledge.",
    "The UniProt annotation is supported by experimental evidence (X-ray crystallography PDB 5CEF, enzymatic assays), not merely computational transfer.",
    "The sequence match to Q5KPK7 is exact (SHA-256 confirmed) in both current and historical (v121) snapshots.",
    "The physiological direction is noted as right-to-left (reductive amination direction) in the annotation, but the reaction equation as written in choice A is the standard EC 1.2.1.11 formulation."
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

**Accession:** `Q5KPK7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 121. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
"Q5KPK7"
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26527262","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"26527262","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24286"}}],"reaction":{"ecNumber":"1.2.1.11","evidences":[{"evidenceCode":"ECO:0000269","id":"26527262","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"name":"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24284"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:537519"}]}}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"citation":{"authors":["Dahal G.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"26527262"},{"database":"DOI","id":"10.1107/s2053230x15017495"}],"citationType":"journal article","firstPage":"1365","id":"26527262","journal":"Acta Crystallogr. F Struct. Biol. Commun.","lastPage":"1371","publicationDate":"2015","title":"Structure of a fungal form of aspartate semialdehyde dehydrogenase from Cryptococcus neoformans.","volume":"71"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5CEF","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.60 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT"]}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
ID   DHAS_CRYD1              Reviewed;         365 AA.
AC   Q5KPK7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   15-FEB-2005, sequence version 1.
DT   28-JAN-2026, entry version 121.
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};
GN   OrderedLocusNames=CNA02450 {ECO:0000312|EMBL:AAW40826.1};
OS   Cryptococcus deneoformans (strain JEC21 / ATCC MYA-565) (Cryptococcus
OS   neoformans var. neoformans serotype D).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=214684 {ECO:0000312|Proteomes:UP000002149};
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 46-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
RN   [4] {ECO:0007744|PDB:5CEF}
RP   X-RAY CRYSTALLOGRAPHY (2.60 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.
RX   PubMed=26527262; DOI=10.1107/s2053230x15017495;
RA   Dahal G., Viola R.E.;
RT   "Structure of a fungal form of aspartate semialdehyde dehydrogenase from
RT   Cryptococcus neoformans.";
RL   Acta Crystallogr. F Struct. Biol. Commun. 71:1365-1371(2015).
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 61-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-
CC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;
CC         Evidence={ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;
CC         Evidence={ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 69. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
