# EC_number_0044

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.2.2.19

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTFGAEVDQVWPAVTGDSPHLTNFGRKLLKDCRQVQKPIGGYENLGNVIKLSAEFPLEFGVNSVKVYRQSPSRLARINEEVASAYPLIHERTLGLYLQYLEHKCRWGNAVEKPIYRNLSLCGFVQRLLVKRCASFFARNDKYLLVSGESGASGFEAVGTREEKAPLVLANVLSYDDIKLSALLSVSSRTEFVNEGERTNCGHVDLNTKTLERHGVIVGMIGARLSRRNLMEFQDIVIARQQNTRERGYGMALDEPATTRDEDYRRLWREFYATRDLIHGQAVIDNQRFGPSKNKMDVFDNLVMKRRYAISFDMLLLEAEARAKRVKKLAYIHVVGFGLGVWKAAEQQERIFMETFEQRMRTLGNRLNNVGLVHFSWFSITHCGGLSNGSLIEIPGHPKDGIRVLISKRNPARKLSDPEHAGMLLVVSYAWDGNALPGNEFWMKMLQSTGDSSTACSTLVAELHNPYINTKFCNGGNLHIASPEHGVLHIAEYAKRVIRSESDAL

[Multiple Choices]
A. 3.2.2.5
B. 3.2.2.19
C. 2.4.1.392
D. 1.14.14.104
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the UniProt entry annotated as EC 3.2.2.19. The entry reports catalytic activities assigned this EC with experimental evidence (ECO:0000269), including hydrolysis of ADP-ribosylated arginine on proteins and free arginine.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features might suggest a hydrolase or ADP-ribose-related protein, but the supplied sequence and choices do not establish the precise substrate specificity needed to select a complete EC number.


**Missing item-specific fact**

> The protein-specific catalytic activity: that this enzyme hydrolyzes ADP-ribosylated arginine, as experimentally assigned to EC 3.2.2.19.


**Reason**

> Choosing among the candidate EC numbers requires the protein's specific functional annotation or experimental characterization, which is not provided in the question. Matching the sequence to a remembered database entry would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence has an experimentally supported annotation for choice B; the supplied reviewer evidence does not support another listed EC number for this sequence.


### Important caveats

- The annotation evidence cites a publication with experimental evidence codes, but the underlying study was not independently reviewed here.
- The historical and current UniProt records match the supplied sequence; the benchmark author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features might suggest a hydrolase or ADP-ribose-related protein, but the supplied sequence and choices do not establish the precise substrate specificity needed to select a complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity: that this enzyme hydrolyzes ADP-ribosylated arginine, as experimentally assigned to EC 3.2.2.19.",
    "reason": "Choosing among the candidate EC numbers requires the protein's specific functional annotation or experimental characterization, which is not provided in the question. Matching the sequence to a remembered database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as EC 3.2.2.19. The entry reports catalytic activities assigned this EC with experimental evidence (ECO:0000269), including hydrolysis of ADP-ribosylated arginine on proteins and free arginine."
  },
  "important_caveats": [
    "The annotation evidence cites a publication with experimental evidence codes, but the underlying study was not independently reviewed here.",
    "The historical and current UniProt records match the supplied sequence; the benchmark author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has an experimentally supported annotation for choice B; the supplied reviewer evidence does not support another listed EC number for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as EC 3.2.2.19. The entry reports catalytic activities assigned this EC with experimental evidence (ECO:0000269), including hydrolysis of ADP-ribosylated arginine on proteins and free arginine.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features might suggest a hydrolase or ADP-ribose-related protein, but the supplied sequence and choices do not establish the precise substrate specificity needed to select a complete EC number.",
    "missing_item_specific_fact": "The protein-specific catalytic activity: that this enzyme hydrolyzes ADP-ribosylated arginine, as experimentally assigned to EC 3.2.2.19.",
    "reason": "Choosing among the candidate EC numbers requires the protein's specific functional annotation or experimental characterization, which is not provided in the question. Matching the sequence to a remembered database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has an experimentally supported annotation for choice B; the supplied reviewer evidence does not support another listed EC number for this sequence."
  },
  "important_caveats": [
    "The annotation evidence cites a publication with experimental evidence codes, but the underlying study was not independently reviewed here.",
    "The historical and current UniProt records match the supplied sequence; the benchmark author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry Q9W2W5 (ADPR1_DROME, Drosophila melanogaster, 505 AA, sequence SHA256 matched) assigns EC 3.2.2.19 (ADP-ribosylarginine hydrolase CG2909) with experimental evidence ECO:0000269 from PubMed:38503748 (Zhang et al., Nat. Commun. 2024) and X-ray crystallography PDB:8DMT. The catalytic reaction N(omega)-(ADP-D-ribosyl)-L-arginyl-&#91;protein&#93; + H2O = ADP-D-ribose + L-arginyl-&#91;protein&#93; is confirmed experimentally. The sequence in the question matches the source entry exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a macrodomain-like fold (e.g., the 'VSGESGASGFEAVG' region), which is associated with ADP-ribosyl recognition. This could help a knowledgeable expert eliminate C (2.4.1.392, a glycosyltransferase) and D (1.14.14.104, a cytochrome P450 oxidoreductase) as they belong to entirely different EC classes. However, distinguishing A (3.2.2.5, NAD+ glycohydrolase) from B (3.2.2.19, ADP-ribosylarginine hydrolase) within the same 3.2.2.x glycohydrolase class requires knowing the specific substrate specificity of this protein—whether it hydrolyzes NAD+ or specifically cleaves the ADP-ribosyl-arginine glycosidic bond. This was only experimentally determined in 2024.


**Missing item-specific fact**

> The specific substrate selectivity of this Drosophila CG2909 protein—namely, that it hydrolyzes the N-glycosidic bond of ADP-ribosyl-arginine (not NAD+)—which was established experimentally in 2024 (PubMed:38503748, PDB:8DMT) and is not reliably inferable from the sequence alone without specialized knowledge of macrodomain subfamily substrate preferences.


**Reason**

> While the macrodomain fold narrows the class to 3.2.2.x, the critical distinction between EC 3.2.2.5 (NAD+ glycohydrolase, Rossmann-fold enzymes like CD38) and EC 3.2.2.19 (ADP-ribosylarginine hydrolase, macrodomain enzymes) requires item-specific knowledge of this protein's experimentally determined substrate specificity. The EC 3.2.2.19 annotation was only added in 2025 based on 2024 experimental data. A model without memorization of this specific protein's annotation would struggle to reliably distinguish A from B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 3.2.2.5 and 3.2.2.19 are glycosylases (EC 3.2.2.x) acting on N-glycosyl compounds involving ADP-ribose chemistry. Without knowing the specific substrate (NAD+ vs. ADP-ribosyl-arginine), both A and B are plausible from a sequence-only perspective, though the macrodomain fold weakly favors B. Options C and D are in different EC classes and are more clearly eliminable.


### Important caveats

- The EC 3.2.2.19 annotation for this protein was only assigned in February 2025 based on a 2024 experimental paper; prior to that, the protein's exact EC number was not established in databases.
- The macrodomain fold identification provides a weak reasoning path toward ADP-ribosylhydrolase activity over NAD+ glycohydrolase, but this is highly specialized knowledge not generally available to a model without memorization.
- The identity of the protein (Q9W2W5) was inferred by the reviewer from dataset metadata; the evaluated model only sees the raw sequence.
- Distractors C (transferase) and D (oxidoreductase) are in unrelated EC classes and serve as easy eliminations, but the critical A-vs-B distinction is the substantive challenge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a macrodomain-like fold (e.g., the 'VSGESGASGFEAVG' region), which is associated with ADP-ribosyl recognition. This could help a knowledgeable expert eliminate C (2.4.1.392, a glycosyltransferase) and D (1.14.14.104, a cytochrome P450 oxidoreductase) as they belong to entirely different EC classes. However, distinguishing A (3.2.2.5, NAD+ glycohydrolase) from B (3.2.2.19, ADP-ribosylarginine hydrolase) within the same 3.2.2.x glycohydrolase class requires knowing the specific substrate specificity of this protein—whether it hydrolyzes NAD+ or specifically cleaves the ADP-ribosyl-arginine glycosidic bond. This was only experimentally determined in 2024.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate selectivity of this Drosophila CG2909 protein—namely, that it hydrolyzes the N-glycosidic bond of ADP-ribosyl-arginine (not NAD+)—which was established experimentally in 2024 (PubMed:38503748, PDB:8DMT) and is not reliably inferable from the sequence alone without specialized knowledge of macrodomain subfamily substrate preferences.",
    "reason": "While the macrodomain fold narrows the class to 3.2.2.x, the critical distinction between EC 3.2.2.5 (NAD+ glycohydrolase, Rossmann-fold enzymes like CD38) and EC 3.2.2.19 (ADP-ribosylarginine hydrolase, macrodomain enzymes) requires item-specific knowledge of this protein's experimentally determined substrate specificity. The EC 3.2.2.19 annotation was only added in 2025 based on 2024 experimental data. A model without memorization of this specific protein's annotation would struggle to reliably distinguish A from B."
  },
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry Q9W2W5 (ADPR1_DROME, Drosophila melanogaster, 505 AA, sequence SHA256 matched) assigns EC 3.2.2.19 (ADP-ribosylarginine hydrolase CG2909) with experimental evidence ECO:0000269 from PubMed:38503748 (Zhang et al., Nat. Commun. 2024) and X-ray crystallography PDB:8DMT. The catalytic reaction N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein] is confirmed experimentally. The sequence in the question matches the source entry exactly."
  },
  "important_caveats": [
    "The EC 3.2.2.19 annotation for this protein was only assigned in February 2025 based on a 2024 experimental paper; prior to that, the protein's exact EC number was not established in databases.",
    "The macrodomain fold identification provides a weak reasoning path toward ADP-ribosylhydrolase activity over NAD+ glycohydrolase, but this is highly specialized knowledge not generally available to a model without memorization.",
    "The identity of the protein (Q9W2W5) was inferred by the reviewer from dataset metadata; the evaluated model only sees the raw sequence.",
    "Distractors C (transferase) and D (oxidoreductase) are in unrelated EC classes and serve as easy eliminations, but the critical A-vs-B distinction is the substantive challenge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 3.2.2.5 and 3.2.2.19 are glycosylases (EC 3.2.2.x) acting on N-glycosyl compounds involving ADP-ribose chemistry. Without knowing the specific substrate (NAD+ vs. ADP-ribosyl-arginine), both A and B are plausible from a sequence-only perspective, though the macrodomain fold weakly favors B. Options C and D are in different EC classes and are more clearly eliminable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry Q9W2W5 (ADPR1_DROME, Drosophila melanogaster, 505 AA, sequence SHA256 matched) assigns EC 3.2.2.19 (ADP-ribosylarginine hydrolase CG2909) with experimental evidence ECO:0000269 from PubMed:38503748 (Zhang et al., Nat. Commun. 2024) and X-ray crystallography PDB:8DMT. The catalytic reaction N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein] is confirmed experimentally. The sequence in the question matches the source entry exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a macrodomain-like fold (e.g., the 'VSGESGASGFEAVG' region), which is associated with ADP-ribosyl recognition. This could help a knowledgeable expert eliminate C (2.4.1.392, a glycosyltransferase) and D (1.14.14.104, a cytochrome P450 oxidoreductase) as they belong to entirely different EC classes. However, distinguishing A (3.2.2.5, NAD+ glycohydrolase) from B (3.2.2.19, ADP-ribosylarginine hydrolase) within the same 3.2.2.x glycohydrolase class requires knowing the specific substrate specificity of this protein—whether it hydrolyzes NAD+ or specifically cleaves the ADP-ribosyl-arginine glycosidic bond. This was only experimentally determined in 2024.",
    "missing_item_specific_fact": "The specific substrate selectivity of this Drosophila CG2909 protein—namely, that it hydrolyzes the N-glycosidic bond of ADP-ribosyl-arginine (not NAD+)—which was established experimentally in 2024 (PubMed:38503748, PDB:8DMT) and is not reliably inferable from the sequence alone without specialized knowledge of macrodomain subfamily substrate preferences.",
    "reason": "While the macrodomain fold narrows the class to 3.2.2.x, the critical distinction between EC 3.2.2.5 (NAD+ glycohydrolase, Rossmann-fold enzymes like CD38) and EC 3.2.2.19 (ADP-ribosylarginine hydrolase, macrodomain enzymes) requires item-specific knowledge of this protein's experimentally determined substrate specificity. The EC 3.2.2.19 annotation was only added in 2025 based on 2024 experimental data. A model without memorization of this specific protein's annotation would struggle to reliably distinguish A from B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 3.2.2.5 and 3.2.2.19 are glycosylases (EC 3.2.2.x) acting on N-glycosyl compounds involving ADP-ribose chemistry. Without knowing the specific substrate (NAD+ vs. ADP-ribosyl-arginine), both A and B are plausible from a sequence-only perspective, though the macrodomain fold weakly favors B. Options C and D are in different EC classes and are more clearly eliminable."
  },
  "important_caveats": [
    "The EC 3.2.2.19 annotation for this protein was only assigned in February 2025 based on a 2024 experimental paper; prior to that, the protein's exact EC number was not established in databases.",
    "The macrodomain fold identification provides a weak reasoning path toward ADP-ribosylhydrolase activity over NAD+ glycohydrolase, but this is highly specialized knowledge not generally available to a model without memorization.",
    "The identity of the protein (Q9W2W5) was inferred by the reviewer from dataset metadata; the evaluated model only sees the raw sequence.",
    "Distractors C (transferase) and D (oxidoreductase) are in unrelated EC classes and serve as easy eliminations, but the critical A-vs-B distinction is the substantive challenge."
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

**Accession:** `Q9W2W5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 173. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
"Q9W2W5"
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"value":"3.2.2.19"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"ADP-ribosylarginine hydrolase CG2909"}}}
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.2.19","evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"name":"N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14885"},{"database":"Rhea","id":"RHEA-COMP:10532"},{"database":"Rhea","id":"RHEA-COMP:15087"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29965"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:142554"}]}}
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.2.19","evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"name":"N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-arginine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20784"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:32682"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:60267"}]}}
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Fu J.","Rack J.G.M.","Li C.","Voorneveld J.","Filippov D.V.","Ahel I.","Luo Z.Q.","Das C."],"citationCrossReferences":[{"database":"PubMed","id":"38503748"},{"database":"DOI","id":"10.1038/s41467-024-46649-2"}],"citationType":"journal article","firstPage":"2452","id":"38503748","journal":"Nat. Commun.","lastPage":"2452","publicationDate":"2024","title":"Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a conserved arginine-specific macrodomain.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8DMT","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.28 ANGSTROMS) OF 12-498","FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 173 / 1.  
**Retrieved:** 2026-11-02T04:33:51.554411+00:00.  

```text
ID   ADPR1_DROME             Reviewed;         505 AA.
AC   Q9W2W5;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 173.
DE   RecName: Full=ADP-ribosylarginine hydrolase CG2909 {ECO:0000305};
DE            EC=3.2.2.19 {ECO:0000269|PubMed:38503748};
GN   ORFNames=CG2909 {ECO:0000312|FlyBase:FBgn0030189};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 173 / 1.  
**Retrieved:** 2026-11-02T04:33:51.554411+00:00.  

```text
DE   RecName: Full=ADP-ribosylarginine hydrolase CG2909 {ECO:0000305};
DE            EC=3.2.2.19 {ECO:0000269|PubMed:38503748};
```

Source SHA-256: `d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)  
**Locator:** `lines 77-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 173 / 1.  
**Retrieved:** 2026-11-02T04:33:51.554411+00:00.  

```text
RN   [4] {ECO:0007744|PDB:8DMT}
RP   X-RAY CRYSTALLOGRAPHY (2.28 ANGSTROMS) OF 12-498, FUNCTION, AND CATALYTIC
RP   ACTIVITY.
RX   PubMed=38503748; DOI=10.1038/s41467-024-46649-2;
RA   Zhang Z., Fu J., Rack J.G.M., Li C., Voorneveld J., Filippov D.V., Ahel I.,
RA   Luo Z.Q., Das C.;
RT   "Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a
RT   conserved arginine-specific macrodomain.";
RL   Nat. Commun. 15:2452-2452(2024).
```

Source SHA-256: `d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)  
**Locator:** `lines 89-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 173 / 1.  
**Retrieved:** 2026-11-02T04:33:51.554411+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-
CC         ribose + L-arginyl-[protein]; Xref=Rhea:RHEA:14885, Rhea:RHEA-
CC         COMP:10532, Rhea:RHEA-COMP:15087, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:29965, ChEBI:CHEBI:57967, ChEBI:CHEBI:142554;
CC         EC=3.2.2.19; Evidence={ECO:0000269|PubMed:38503748};
```

Source SHA-256: `d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)  
**Locator:** `lines 95-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 173 / 1.  
**Retrieved:** 2026-11-02T04:33:51.554411+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-
CC         arginine; Xref=Rhea:RHEA:20784, ChEBI:CHEBI:15377, ChEBI:CHEBI:32682,
CC         ChEBI:CHEBI:57967, ChEBI:CHEBI:60267; EC=3.2.2.19;
CC         Evidence={ECO:0000269|PubMed:38503748};
CC   ---------------------------------------------------------------------------
CC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms
CC   Distributed under the Creative Commons Attribution (CC BY 4.0) License
CC   ---------------------------------------------------------------------------
```

Source SHA-256: `d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 44. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
