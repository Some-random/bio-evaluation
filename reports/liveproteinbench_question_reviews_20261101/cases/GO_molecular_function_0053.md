# GO_molecular_function_0053

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — hydrolase activity, hydrolyzing O-glycosyl compounds

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLLYLVALFVASICSVTAQTWTSCNPLTTTCPPDQALGINTTFTFNKTLDDTIWNVTNGVLSHTDEGTEFTITGENQSPTMQSNFYIFFGIVESHVKMAKGAGIISSIVLQSDDLDEIDWEWVGYNTSEVQSNYFGKGNNETFNRGGYHYVPNADTEFHNYTTYWTQEKLEWWIDGKLARTLTYEDSQGAGKYYPQTPCNIRYGIWPAGIKGNAQGTIEWAGGLVDYSKAPFTMVLQSVRVHDFHTGKEYNYTDHSGSWQSIDVIAGNSTIANAIQNPPKSLSEKWAELPTGAKAGVYIGAGCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN

[Multiple Choices]
A. beta-glucuronidase activity
B. hydrolase activity, hydrolyzing O-glycosyl compounds
C. identical protein binding
D. histone H3K18 acetyltransferase activity
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

> The matched protein is annotated as a chitinase with experimentally supported endochitinase activity. Endochitinase activity is a child of the broad GO term in choice B, hydrolase activity, hydrolyzing O-glycosyl compounds. The protein also has transglycosylase activity, but that does not contradict B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO1](#evidence-go1), [GO3](#evidence-go3), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a signal-peptide-like N-terminus and a long enzyme-like region with an acidic motif compatible with a secreted fungal glycoside hydrolase. That supports the broad carbohydrate-hydrolase option over beta-glucuronidase, protein binding, or histone acetyltransferase activity, though it does not establish the exact enzyme identity.


**Missing item-specific fact**

> Confirmation that this particular protein has chitinase activity, and its additional transglycosylase activity, requires protein-specific annotation or experimental evidence; those details are not supplied in the question.


**Reason**

> The broad choice B can be meaningfully favored from sequence-level and biological clues without knowing the exact database entry. The precise dual activity is item-specific, but is not needed to select this broad parent GO category.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports chitinase activity, whose GO term falls under B. Choice A names a different, more specific glycosidase activity; C and D describe unrelated functions.


### Important caveats

- The UniProt record and experimental activity evidence are reviewer-only and were not supplied to the evaluated model.
- The sequence clues support a broad functional inference, not certainty about the exact substrate or the protein's additional transglycosylase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a signal-peptide-like N-terminus and a long enzyme-like region with an acidic motif compatible with a secreted fungal glycoside hydrolase. That supports the broad carbohydrate-hydrolase option over beta-glucuronidase, protein binding, or histone acetyltransferase activity, though it does not establish the exact enzyme identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Confirmation that this particular protein has chitinase activity, and its additional transglycosylase activity, requires protein-specific annotation or experimental evidence; those details are not supplied in the question.",
    "reason": "The broad choice B can be meaningfully favored from sequence-level and biological clues without knowing the exact database entry. The precise dual activity is item-specific, but is not needed to select this broad parent GO category."
  },
  "case_id": "GO_molecular_function_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "GO1",
      "GO3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The matched protein is annotated as a chitinase with experimentally supported endochitinase activity. Endochitinase activity is a child of the broad GO term in choice B, hydrolase activity, hydrolyzing O-glycosyl compounds. The protein also has transglycosylase activity, but that does not contradict B."
  },
  "important_caveats": [
    "The UniProt record and experimental activity evidence are reviewer-only and were not supplied to the evaluated model.",
    "The sequence clues support a broad functional inference, not certainty about the exact substrate or the protein's additional transglycosylase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports chitinase activity, whose GO term falls under B. Choice A names a different, more specific glycosidase activity; C and D describe unrelated functions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein is annotated as a chitinase with experimentally supported endochitinase activity. Endochitinase activity is a child of the broad GO term in choice B, hydrolase activity, hydrolyzing O-glycosyl compounds. The protein also has transglycosylase activity, but that does not contradict B.",
    "evidence_ids": ["C4", "C5", "C6", "GO1", "GO3", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a signal-peptide-like N-terminus and a long enzyme-like region with an acidic motif compatible with a secreted fungal glycoside hydrolase. That supports the broad carbohydrate-hydrolase option over beta-glucuronidase, protein binding, or histone acetyltransferase activity, though it does not establish the exact enzyme identity.",
    "missing_item_specific_fact": "Confirmation that this particular protein has chitinase activity, and its additional transglycosylase activity, requires protein-specific annotation or experimental evidence; those details are not supplied in the question.",
    "reason": "The broad choice B can be meaningfully favored from sequence-level and biological clues without knowing the exact database entry. The precise dual activity is item-specific, but is not needed to select this broad parent GO category."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports chitinase activity, whose GO term falls under B. Choice A names a different, more specific glycosidase activity; C and D describe unrelated functions."
  },
  "important_caveats": [
    "The UniProt record and experimental activity evidence are reviewer-only and were not supplied to the evaluated model.",
    "The sequence clues support a broad functional inference, not certainty about the exact substrate or the protein's additional transglycosylase activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q4WXE6, Crh-like protein 3 from Aspergillus fumigatus) is experimentally characterized (PubMed:30971696, ECO:0000269) as a chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-). Its GO annotation GO:0008843 (endochitinase activity) is_a GO:0004568 (chitinase activity) is_a GO:0004553 (hydrolase activity, hydrolyzing O-glycosyl compounds). Thus GO:0004553 is a valid ancestor of the protein's experimentally demonstrated chitinase activity. Among the four choices, B is the only term consistent with the protein's catalytic function; A (beta-glucuronidase, EC 3.2.1.31), C (identical protein binding), and D (histone H3K18 acetyltransferase) are unrelated to this protein's demonstrated activities.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [GO3](#evidence-go3), [GO4](#evidence-go4), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable GH18 glycoside hydrolase family motifs (e.g., 'GENQSP' and 'DDEIDWEWVGY' containing the DXXDXDXE catalytic motif characteristic of chitinases), a cleavable N-terminal signal peptide indicating a secreted enzyme, and a C-terminal transmembrane anchor. These features identify the protein as a secreted glycoside hydrolase acting on O-glycosyl bonds (chitin), which maps to GO:0004553. Beta-glucuronidase (option A, GH79 family) has a completely different fold and motif architecture. Options C and D are excluded by the absence of any protein-protein interaction or histone-binding domain features. The reasoning path from GH18 motifs → chitinase → O-glycosyl hydrolase is a legitimate biochemical inference.


**Missing item-specific fact**

> None critical. Recognizing GH18 motifs from a raw sequence requires familiarity with protein family signatures, which is standard biochemistry knowledge, not a lookup of a specific database entry.


**Reason**

> A knowledgeable scientist can identify the GH18 catalytic motifs, the signal peptide, and the transmembrane anchor to classify the protein as a secreted glycoside hydrolase acting on O-glycosyl bonds, thereby selecting B over A (wrong enzyme family), C (no binding domain), and D (no histone interaction features). The reasoning does not require memorizing a specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein has dual chitinase/transglycosylase activity, the transglycosylase GO term (GO:0016757, glycosyltransferase activity) is not among the choices. Among the four provided options, only B (GO:0004553) is a valid ancestor of the protein's demonstrated chitinase activity. The other three options are clearly unrelated to this protein's function.


### Important caveats

- The protein is a dual chitinase/transglycosylase; GO:0004553 captures only the hydrolase component, not the transferase component. However, since no transferase option is provided, B remains the best available answer.
- The GO:0008843 annotation carries evidence code IEA:UniProtKB-EC (inferred from EC number), while the transglycosylase activity has ECO:0000269 (direct experimental evidence). The chitinase EC assignment itself is ECO:0000305 (inferred from sequence similarity to characterized homologs via PubMed:30971696).
- Recognition of GH18 motifs from a raw 363-aa sequence requires moderate protein-family expertise; this is standard biochemistry knowledge but not trivial for a non-specialist.
- The sequence match is confirmed (SHA256 match between benchmark and UniProt Q4WXE6 sequence version 2, 363 aa).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable GH18 glycoside hydrolase family motifs (e.g., 'GENQSP' and 'DDEIDWEWVGY' containing the DXXDXDXE catalytic motif characteristic of chitinases), a cleavable N-terminal signal peptide indicating a secreted enzyme, and a C-terminal transmembrane anchor. These features identify the protein as a secreted glycoside hydrolase acting on O-glycosyl bonds (chitin), which maps to GO:0004553. Beta-glucuronidase (option A, GH79 family) has a completely different fold and motif architecture. Options C and D are excluded by the absence of any protein-protein interaction or histone-binding domain features. The reasoning path from GH18 motifs → chitinase → O-glycosyl hydrolase is a legitimate biochemical inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognizing GH18 motifs from a raw sequence requires familiarity with protein family signatures, which is standard biochemistry knowledge, not a lookup of a specific database entry.",
    "reason": "A knowledgeable scientist can identify the GH18 catalytic motifs, the signal peptide, and the transmembrane anchor to classify the protein as a secreted glycoside hydrolase acting on O-glycosyl bonds, thereby selecting B over A (wrong enzyme family), C (no binding domain), and D (no histone interaction features). The reasoning does not require memorizing a specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "GO1",
      "GO3",
      "GO4",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The protein (Q4WXE6, Crh-like protein 3 from Aspergillus fumigatus) is experimentally characterized (PubMed:30971696, ECO:0000269) as a chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-). Its GO annotation GO:0008843 (endochitinase activity) is_a GO:0004568 (chitinase activity) is_a GO:0004553 (hydrolase activity, hydrolyzing O-glycosyl compounds). Thus GO:0004553 is a valid ancestor of the protein's experimentally demonstrated chitinase activity. Among the four choices, B is the only term consistent with the protein's catalytic function; A (beta-glucuronidase, EC 3.2.1.31), C (identical protein binding), and D (histone H3K18 acetyltransferase) are unrelated to this protein's demonstrated activities."
  },
  "important_caveats": [
    "The protein is a dual chitinase/transglycosylase; GO:0004553 captures only the hydrolase component, not the transferase component. However, since no transferase option is provided, B remains the best available answer.",
    "The GO:0008843 annotation carries evidence code IEA:UniProtKB-EC (inferred from EC number), while the transglycosylase activity has ECO:0000269 (direct experimental evidence). The chitinase EC assignment itself is ECO:0000305 (inferred from sequence similarity to characterized homologs via PubMed:30971696).",
    "Recognition of GH18 motifs from a raw 363-aa sequence requires moderate protein-family expertise; this is standard biochemistry knowledge but not trivial for a non-specialist.",
    "The sequence match is confirmed (SHA256 match between benchmark and UniProt Q4WXE6 sequence version 2, 363 aa)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has dual chitinase/transglycosylase activity, the transglycosylase GO term (GO:0016757, glycosyltransferase activity) is not among the choices. Among the four provided options, only B (GO:0004553) is a valid ancestor of the protein's demonstrated chitinase activity. The other three options are clearly unrelated to this protein's function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q4WXE6, Crh-like protein 3 from Aspergillus fumigatus) is experimentally characterized (PubMed:30971696, ECO:0000269) as a chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-). Its GO annotation GO:0008843 (endochitinase activity) is_a GO:0004568 (chitinase activity) is_a GO:0004553 (hydrolase activity, hydrolyzing O-glycosyl compounds). Thus GO:0004553 is a valid ancestor of the protein's experimentally demonstrated chitinase activity. Among the four choices, B is the only term consistent with the protein's catalytic function; A (beta-glucuronidase, EC 3.2.1.31), C (identical protein binding), and D (histone H3K18 acetyltransferase) are unrelated to this protein's demonstrated activities.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "GO1", "GO3", "GO4", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable GH18 glycoside hydrolase family motifs (e.g., 'GENQSP' and 'DDEIDWEWVGY' containing the DXXDXDXE catalytic motif characteristic of chitinases), a cleavable N-terminal signal peptide indicating a secreted enzyme, and a C-terminal transmembrane anchor. These features identify the protein as a secreted glycoside hydrolase acting on O-glycosyl bonds (chitin), which maps to GO:0004553. Beta-glucuronidase (option A, GH79 family) has a completely different fold and motif architecture. Options C and D are excluded by the absence of any protein-protein interaction or histone-binding domain features. The reasoning path from GH18 motifs → chitinase → O-glycosyl hydrolase is a legitimate biochemical inference.",
    "missing_item_specific_fact": "None critical. Recognizing GH18 motifs from a raw sequence requires familiarity with protein family signatures, which is standard biochemistry knowledge, not a lookup of a specific database entry.",
    "reason": "A knowledgeable scientist can identify the GH18 catalytic motifs, the signal peptide, and the transmembrane anchor to classify the protein as a secreted glycoside hydrolase acting on O-glycosyl bonds, thereby selecting B over A (wrong enzyme family), C (no binding domain), and D (no histone interaction features). The reasoning does not require memorizing a specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has dual chitinase/transglycosylase activity, the transglycosylase GO term (GO:0016757, glycosyltransferase activity) is not among the choices. Among the four provided options, only B (GO:0004553) is a valid ancestor of the protein's demonstrated chitinase activity. The other three options are clearly unrelated to this protein's function."
  },
  "important_caveats": [
    "The protein is a dual chitinase/transglycosylase; GO:0004553 captures only the hydrolase component, not the transferase component. However, since no transferase option is provided, B remains the best available answer.",
    "The GO:0008843 annotation carries evidence code IEA:UniProtKB-EC (inferred from EC number), while the transglycosylase activity has ECO:0000269 (direct experimental evidence). The chitinase EC assignment itself is ECO:0000305 (inferred from sequence similarity to characterized homologs via PubMed:30971696).",
    "Recognition of GH18 motifs from a raw 363-aa sequence requires moderate protein-family expertise; this is standard biochemistry knowledge but not trivial for a non-specialist.",
    "The sequence match is confirmed (SHA256 match between benchmark and UniProt Q4WXE6 sequence version 2, 363 aa)."
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

**Accession:** `Q4WXE6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 98. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.355475+00:00.  

```json
{"flag":"Precursor","includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30971696","source":"PubMed"}],"value":"3.2.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Chitinase crh3"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30971696","source":"PubMed"}],"value":"2.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Chitin transglycosylase crh3"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Crh-like protein 3"}}}
```

Source SHA-256: `e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.355475+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30971696","source":"PubMed"}],"value":"Dual chitinase/transglycosylase that plays a role in cell wall architecture (PubMed:30971696). Chitinase and transglycosylase activities are coupled (PubMed:30971696). Required for the polysaccharide cross-linking at the septa and the cell wall (PubMed:30971696). More specifically, transfers chitin to 1,6-beta-glucan in the cell wall (PubMed:30971696)"}]}
```

Source SHA-256: `e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.355475+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.14","evidences":[{"evidenceCode":"ECO:0000305","id":"30971696","source":"PubMed"}],"name":"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins."}}
```

Source SHA-256: `e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.355475+00:00.  

```json
{"database":"GO","id":"GO:0008843","properties":[{"key":"GoTerm","value":"F:endochitinase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-EC"}]}
```

Source SHA-256: `e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)  
**Locator:** `lines 54-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 2.  
**Retrieved:** 2026-11-02T04:31:00.140024+00:00.  

```text
CC   -!- FUNCTION: Dual chitinase/transglycosylase that plays a role in cell
CC       wall architecture (PubMed:30971696). Chitinase and transglycosylase
CC       activities are coupled (PubMed:30971696). Required for the
CC       polysaccharide cross-linking at the septa and the cell wall
CC       (PubMed:30971696). More specifically, transfers chitin to 1,6-beta-
CC       glucan in the cell wall (PubMed:30971696).
CC       {ECO:0000269|PubMed:30971696}.
```

Source SHA-256: `af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)  
**Locator:** `lines 61-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 2.  
**Retrieved:** 2026-11-02T04:31:00.140024+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide
CC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;
CC         Evidence={ECO:0000305|PubMed:30971696};
```

Source SHA-256: `af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)  
**Locator:** `lines 94-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 2.  
**Retrieved:** 2026-11-02T04:31:00.140024+00:00.  

```text
DR   GO; GO:0008843; F:endochitinase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 44250-44263`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004553
name: hydrolase activity, hydrolyzing O-glycosyl compounds
namespace: molecular_function
alt_id: GO:0016800
def: "Catalysis of the hydrolysis of any O-glycosyl bond." [GOC:mah]
synonym: "O-glucosyl hydrolase activity" EXACT []
xref: EC:3.2.1.-
xref: Reactome:R-HSA-5694563 "ABHD10 hydrolyses MPAG"
xref: Reactome:R-HSA-6786652 "CHIT1 hydrolyses CHIT to 3xADGP"
xref: Reactome:R-HSA-9661820 "Bacterial GUSB hydrolyses BDG to BIL"
is_a: GO:0016798 ! hydrolase activity, acting on glycosyl bonds
property_value: skos:exactMatch EC:3.2.1.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 44534-44541`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004568
name: chitinase activity
namespace: molecular_function
def: "Catalysis of the hydrolysis of (1->4)-beta linkages of N-acetyl-D-glucosamine (GlcNAc) polymers of chitin and chitodextrins." [GOC:bf, GOC:kah, GOC:pde, PMID:11468293]
xref: Reactome:R-HSA-6786421 "CHIA hydrolyses chitin"
is_a: GO:0004553 ! hydrolase activity, hydrolyzing O-glycosyl compounds

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 88913-88926`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008843
name: endochitinase activity
namespace: molecular_function
def: "Catalysis of the hydrolysis of nonterminal (1->4)-beta linkages of N-acetyl-D-glucosamine (GlcNAc) polymers of chitin and chitodextrins. Typically, endochitinases cleave randomly within the chitin chain." [EC:3.2.1.14, GOC:bf, GOC:kah, GOC:pde, PMID:11468293]
synonym: "1,4-beta-poly-N-acetylglucosaminidase" EXACT [EC:3.2.1.14]
synonym: "chitinase" EXACT [EC:3.2.1.14]
synonym: "chitodextrinase" EXACT [EC:3.2.1.14]
synonym: "poly-beta-glucosaminidase" EXACT [EC:3.2.1.14]
xref: EC:3.2.1.14
xref: MetaCyc:3.2.1.14-RXN
is_a: GO:0004568 ! chitinase activity
property_value: skos:exactMatch EC:3.2.1.14

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 53. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
