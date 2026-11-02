# GO_molecular_function_0161

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — 1-(5-phosphoribosyl)-5-&#91;(5-phosphoribosylamino)methylideneamino&#93;imidazole-4-carboxamide isomerase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQCSVQFRPCIDIHKGKVKQIVGSTLKDLKDDDGSDPITNFESDKSAAEYATLYKQDGLKGGHVIMLGADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEGASHVIVTSYVFNNGQMDLERLKDLVRIVGKERLVLDLSCRKKEGKYAIVTDRWQKFSDVSLDAKVMEFLANFADEFLVHGVDVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA

[Multiple Choices]
A. 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity
B. NADP binding
C. zinc ion binding
D. O-methyltransferase activity
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

> The supplied sequence exactly matches the reviewed Medicago truncatula HISN3 entry. Its function and catalytic-activity annotations identify the 5′-ProFAR-to-PrFAR isomerization, with experimental evidence cited from PubMed; the matching GO molecular-function annotation is option A.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence does not, by general biological reasoning alone, establish this specific substrate and isomerase activity over the other choices.


**Missing item-specific fact**

> The protein-specific identification as HISN3 and its experimentally supported 5′-ProFAR isomerase activity.


**Reason**

> Selecting A requires the protein’s specific functional annotation or experimental characterization, neither of which is supplied in the question. Recognizing the sequence from an external database would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports option A; the supplied evidence does not establish another listed function for this sequence.


### Important caveats

- The functional and annotation evidence is reviewer-only and was not available to the evaluated model.
- The sequence match and cited experimental evidence support the key, but do not make the question answerable from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence does not, by general biological reasoning alone, establish this specific substrate and isomerase activity over the other choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as HISN3 and its experimentally supported 5′-ProFAR isomerase activity.",
    "reason": "Selecting A requires the protein’s specific functional annotation or experimental characterization, neither of which is supplied in the question. Recognizing the sequence from an external database would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "GO_molecular_function_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Medicago truncatula HISN3 entry. Its function and catalytic-activity annotations identify the 5′-ProFAR-to-PrFAR isomerization, with experimental evidence cited from PubMed; the matching GO molecular-function annotation is option A."
  },
  "important_caveats": [
    "The functional and annotation evidence is reviewer-only and was not available to the evaluated model.",
    "The sequence match and cited experimental evidence support the key, but do not make the question answerable from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports option A; the supplied evidence does not establish another listed function for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Medicago truncatula HISN3 entry. Its function and catalytic-activity annotations identify the 5′-ProFAR-to-PrFAR isomerization, with experimental evidence cited from PubMed; the matching GO molecular-function annotation is option A.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence does not, by general biological reasoning alone, establish this specific substrate and isomerase activity over the other choices.",
    "missing_item_specific_fact": "The protein-specific identification as HISN3 and its experimentally supported 5′-ProFAR isomerase activity.",
    "reason": "Selecting A requires the protein’s specific functional annotation or experimental characterization, neither of which is supplied in the question. Recognizing the sequence from an external database would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports option A; the supplied evidence does not establish another listed function for this sequence."
  },
  "important_caveats": [
    "The functional and annotation evidence is reviewer-only and was not available to the evaluated model.",
    "The sequence match and cited experimental evidence support the key, but do not make the question answerable from the sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProt G7IFI7 (HISN3_MEDTR, Medicago truncatula). The entry is annotated with GO:0003949 (the exact term in option A) with evidence code IDA:UniProtKB, supported by X-ray crystallography at 1.54 Å in complex with substrate 5'-ProFAR and product PrFAR, mutagenesis, and kinetic studies (PubMed:39186852, 2024). The EC number 5.3.1.16 and catalytic activity are experimentally confirmed. The expected answer is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence lacks a Rossmann-fold NADP-binding motif (GxGxxG), eliminating B. It lacks a Cys/His zinc-binding cluster, eliminating C. It lacks the VLDVGxG or other methyltransferase signature motifs, eliminating D. The sequence displays alternating hydrophobic/hydrophilic patterns consistent with a TIM barrel fold (e.g., 'GADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEGASHVIVTSYVFNNGQMDLERLKDLVRIVGKERLVLDLSCRKKEGKYAIVTDRWQKFSDVSLDAKVMEFLANFADEFLVHGVDVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA'), which is the hallmark of intramolecular isomerases including ProFAR isomerase. By elimination of cofactor-binding and transferase functions, the isomerase activity (A) is the only consistent option.


**Missing item-specific fact**

> Positive identification of the specific ProFAR isomerase (HisI) subfamily versus other TIM barrel isomerases (e.g., HisA, triosephosphate isomerase) from sequence alone would require detailed family-level sequence knowledge or database lookup. However, the elimination-based argument is sufficient to distinguish A from B, C, and D.


**Reason**

> While positively naming the exact isomerase from sequence is difficult, the three distractors each require a specific structural motif (Rossmann fold, zinc-binding cluster, methyltransferase signature) that is absent from the sequence. The TIM barrel architecture visible in the sequence is consistent with an intramolecular isomerase. This provides meaningful biological grounds to select A over B, C, and D without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D each require specific structural motifs (Rossmann fold, zinc-binding cluster, methyltransferase VLDVGxG) that are absent from the sequence. The generic 'metal ion binding' annotation (GO:0046872, IEA:UniProtKB-KW) in the entry refers to a sodium ion observed in the crystal structure, not zinc, and is a keyword-based inference, not experimental zinc-binding evidence. No option other than A is defensible.


### Important caveats

- The GO annotation (GO:0003949) carries evidence code IDA (Inferred from Direct Assay), based on 2024 X-ray crystallography and biochemical characterization (PubMed:39186852), representing strong experimental evidence.
- The UniProt entry was first public on 2025-06-18, after the approximate benchmark construction date; however, the sequence itself was submitted in 2012 and the annotation was added later.
- The entry also carries a generic 'metal ion binding' GO term (GO:0046872, IEA:UniProtKB-KW) which is not specific to zinc and should not be confused with option C.
- The positive identification of ProFAR isomerase specifically (vs. other TIM barrel isomerases) from sequence alone remains challenging; the reasoning relies primarily on elimination of the three clearly incompatible distractors.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks a Rossmann-fold NADP-binding motif (GxGxxG), eliminating B. It lacks a Cys/His zinc-binding cluster, eliminating C. It lacks the VLDVGxG or other methyltransferase signature motifs, eliminating D. The sequence displays alternating hydrophobic/hydrophilic patterns consistent with a TIM barrel fold (e.g., 'GADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEGASHVIVTSYVFNNGQMDLERLKDLVRIVGKERLVLDLSCRKKEGKYAIVTDRWQKFSDVSLDAKVMEFLANFADEFLVHGVDVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA'), which is the hallmark of intramolecular isomerases including ProFAR isomerase. By elimination of cofactor-binding and transferase functions, the isomerase activity (A) is the only consistent option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of the specific ProFAR isomerase (HisI) subfamily versus other TIM barrel isomerases (e.g., HisA, triosephosphate isomerase) from sequence alone would require detailed family-level sequence knowledge or database lookup. However, the elimination-based argument is sufficient to distinguish A from B, C, and D.",
    "reason": "While positively naming the exact isomerase from sequence is difficult, the three distractors each require a specific structural motif (Rossmann fold, zinc-binding cluster, methyltransferase signature) that is absent from the sequence. The TIM barrel architecture visible in the sequence is consistent with an intramolecular isomerase. This provides meaningful biological grounds to select A over B, C, and D without requiring memorization of this specific protein's database entry."
  },
  "case_id": "GO_molecular_function_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H2",
      "H3",
      "H4",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt G7IFI7 (HISN3_MEDTR, Medicago truncatula). The entry is annotated with GO:0003949 (the exact term in option A) with evidence code IDA:UniProtKB, supported by X-ray crystallography at 1.54 Å in complex with substrate 5'-ProFAR and product PrFAR, mutagenesis, and kinetic studies (PubMed:39186852, 2024). The EC number 5.3.1.16 and catalytic activity are experimentally confirmed. The expected answer is directly and experimentally supported."
  },
  "important_caveats": [
    "The GO annotation (GO:0003949) carries evidence code IDA (Inferred from Direct Assay), based on 2024 X-ray crystallography and biochemical characterization (PubMed:39186852), representing strong experimental evidence.",
    "The UniProt entry was first public on 2025-06-18, after the approximate benchmark construction date; however, the sequence itself was submitted in 2012 and the annotation was added later.",
    "The entry also carries a generic 'metal ion binding' GO term (GO:0046872, IEA:UniProtKB-KW) which is not specific to zinc and should not be confused with option C.",
    "The positive identification of ProFAR isomerase specifically (vs. other TIM barrel isomerases) from sequence alone remains challenging; the reasoning relies primarily on elimination of the three clearly incompatible distractors."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D each require specific structural motifs (Rossmann fold, zinc-binding cluster, methyltransferase VLDVGxG) that are absent from the sequence. The generic 'metal ion binding' annotation (GO:0046872, IEA:UniProtKB-KW) in the entry refers to a sodium ion observed in the crystal structure, not zinc, and is a keyword-based inference, not experimental zinc-binding evidence. No option other than A is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt G7IFI7 (HISN3_MEDTR, Medicago truncatula). The entry is annotated with GO:0003949 (the exact term in option A) with evidence code IDA:UniProtKB, supported by X-ray crystallography at 1.54 Å in complex with substrate 5'-ProFAR and product PrFAR, mutagenesis, and kinetic studies (PubMed:39186852, 2024). The EC number 5.3.1.16 and catalytic activity are experimentally confirmed. The expected answer is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H2", "H3", "H4", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence lacks a Rossmann-fold NADP-binding motif (GxGxxG), eliminating B. It lacks a Cys/His zinc-binding cluster, eliminating C. It lacks the VLDVGxG or other methyltransferase signature motifs, eliminating D. The sequence displays alternating hydrophobic/hydrophilic patterns consistent with a TIM barrel fold (e.g., 'GADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEGASHVIVTSYVFNNGQMDLERLKDLVRIVGKERLVLDLSCRKKEGKYAIVTDRWQKFSDVSLDAKVMEFLANFADEFLVHGVDVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA'), which is the hallmark of intramolecular isomerases including ProFAR isomerase. By elimination of cofactor-binding and transferase functions, the isomerase activity (A) is the only consistent option.",
    "missing_item_specific_fact": "Positive identification of the specific ProFAR isomerase (HisI) subfamily versus other TIM barrel isomerases (e.g., HisA, triosephosphate isomerase) from sequence alone would require detailed family-level sequence knowledge or database lookup. However, the elimination-based argument is sufficient to distinguish A from B, C, and D.",
    "reason": "While positively naming the exact isomerase from sequence is difficult, the three distractors each require a specific structural motif (Rossmann fold, zinc-binding cluster, methyltransferase signature) that is absent from the sequence. The TIM barrel architecture visible in the sequence is consistent with an intramolecular isomerase. This provides meaningful biological grounds to select A over B, C, and D without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D each require specific structural motifs (Rossmann fold, zinc-binding cluster, methyltransferase VLDVGxG) that are absent from the sequence. The generic 'metal ion binding' annotation (GO:0046872, IEA:UniProtKB-KW) in the entry refers to a sodium ion observed in the crystal structure, not zinc, and is a keyword-based inference, not experimental zinc-binding evidence. No option other than A is defensible."
  },
  "important_caveats": [
    "The GO annotation (GO:0003949) carries evidence code IDA (Inferred from Direct Assay), based on 2024 X-ray crystallography and biochemical characterization (PubMed:39186852), representing strong experimental evidence.",
    "The UniProt entry was first public on 2025-06-18, after the approximate benchmark construction date; however, the sequence itself was submitted in 2012 and the annotation was added later.",
    "The entry also carries a generic 'metal ion binding' GO term (GO:0046872, IEA:UniProtKB-KW) which is not specific to zinc and should not be confused with option C.",
    "The positive identification of ProFAR isomerase specifically (vs. other TIM barrel isomerases) from sequence alone remains challenging; the reasoning relies primarily on elimination of the three clearly incompatible distractors."
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

**Accession:** `G7IFI7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 82. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:47.235961+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39186852","source":"PubMed"}],"value":"5'-proFAR isomerase 3"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39186852","source":"PubMed"}],"value":"Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase HISN3"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39186852","source":"PubMed"}],"value":"Protein HISTIDINE BIOSYNTHESIS 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39186852","source":"PubMed"}],"value":"MtHISN3"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39186852","source":"PubMed"}],"value":"5.3.1.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39186852","source":"PubMed"}],"value":"1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase HISN3, chloroplastic"}}}
```

Source SHA-256: `12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:47.235961+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39186852","source":"PubMed"}],"value":"Component of the histidine biosynthesis pathway that catalyzes the isomerization of 5'-ProFAR (pro-phosphoribosyl formimino-5-aminoimidazole-4-carboxamide ribonucleotide, referred as 1-(5-phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-ribosylamino)methylideneamino]imidazole-4-carboxamide) to PrFAR (phosphoribulosyl formimino-5-aminoimidazole-4-carboxamide ribonucleotide, referred as 5-[(5-phospho-1-deoxy-D-ribulos-1-ylimino)methylamino]-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide) (PubMed:39186852)"}]}
```

Source SHA-256: `12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:47.235961+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39186852","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:15470"}}],"reaction":{"ecNumber":"5.3.1.16","evidences":[{"evidenceCode":"ECO:0000269","id":"39186852","source":"PubMed"}],"name":"1-(5-phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-ribosylamino)methylideneamino]imidazole-4-carboxamide = 5-[(5-phospho-1-deoxy-D-ribulos-1-ylimino)methylamino]-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:15469"},{"database":"ChEBI","id":"CHEBI:58435"},{"database":"ChEBI","id":"CHEBI:58525"}]}}
```

Source SHA-256: `12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)  
**Locator:** `/uniProtKBCrossReferences/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:47.235961+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39186852","source":"PubMed"}],"id":"GO:0003949","properties":[{"key":"GoTerm","value":"F:1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:47.235961+00:00.  

```json
{"citation":{"authors":["Witek W.","Imiolczyk B.","Ruszkowski M."],"citationCrossReferences":[{"database":"PubMed","id":"39186852"},{"database":"DOI","id":"10.1016/j.plaphy.2024.109065"}],"citationType":"journal article","firstPage":"109065","id":"39186852","journal":"Plant Physiol. Biochem.","lastPage":"109065","publicationDate":"2024","title":"Structural, kinetic, and evolutionary peculiarities of HISN3, a plant 5'-ProFAR isomerase.","volume":"215"},"referenceNumber":5,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.54 ANGSTROMS) OF 42-312 IN COMPLEX WITH SODIUM ION; 5'-PROFAR AND PRFAR","FUNCTION","MUTAGENESIS OF ASP-57 AND 74-LEU--SER-80","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","COFACTOR","PATHWAY"]}
```

Source SHA-256: `12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)  
**Locator:** `lines 77-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:28:50.784174+00:00.  

```text
RN   [5]
RP   X-RAY CRYSTALLOGRAPHY (1.54 ANGSTROMS) OF 42-312 IN COMPLEX WITH SODIUM
RP   ION; 5'-PROFAR AND PRFAR, FUNCTION, MUTAGENESIS OF ASP-57 AND
RP   74-LEU--SER-80, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES,
RP   COFACTOR, AND PATHWAY.
RX   PubMed=39186852; DOI=10.1016/j.plaphy.2024.109065;
RA   Witek W., Imiolczyk B., Ruszkowski M.;
RT   "Structural, kinetic, and evolutionary peculiarities of HISN3, a plant 5'-
RT   ProFAR isomerase.";
RL   Plant Physiol. Biochem. 215:109065-109065(2024).
```

Source SHA-256: `57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)  
**Locator:** `lines 87-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:28:50.784174+00:00.  

```text
CC   -!- FUNCTION: Component of the histidine biosynthesis pathway that
CC       catalyzes the isomerization of 5'-ProFAR (pro-phosphoribosyl formimino-
CC       5-aminoimidazole-4-carboxamide ribonucleotide, referred as 1-(5-
CC       phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-
CC       ribosylamino)methylideneamino]imidazole-4-carboxamide) to PrFAR
CC       (phosphoribulosyl formimino-5-aminoimidazole-4-carboxamide
CC       ribonucleotide, referred as 5-[(5-phospho-1-deoxy-D-ribulos-1-
CC       ylimino)methylamino]-1-(5-phospho-beta-D-ribosyl)imidazole-4-
CC       carboxamide) (PubMed:39186852). {ECO:0000269|PubMed:39186852}.
```

Source SHA-256: `57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)  
**Locator:** `lines 96-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:28:50.784174+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=1-(5-phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-
CC         ribosylamino)methylideneamino]imidazole-4-carboxamide = 5-[(5-
CC         phospho-1-deoxy-D-ribulos-1-ylimino)methylamino]-1-(5-phospho-beta-D-
CC         ribosyl)imidazole-4-carboxamide; Xref=Rhea:RHEA:15469,
CC         ChEBI:CHEBI:58435, ChEBI:CHEBI:58525; EC=5.3.1.16;
CC         Evidence={ECO:0000269|PubMed:39186852};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:15470;
CC         Evidence={ECO:0000269|PubMed:39186852};
```

Source SHA-256: `57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)  
**Locator:** `lines 147-147`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:28:50.784174+00:00.  

```text
DR   GO; GO:0003949; F:1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity; IDA:UniProtKB.
```

Source SHA-256: `57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 31924-31942`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0003949
name: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity
namespace: molecular_function
def: "Catalysis of the reaction: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide = 5-[(5-phospho-1-deoxy-D-ribulos-1-ylimino)methylamino]-1-(5-phospho-D-ribosyl)imidazole-4-carboxamide." [EC:5.3.1.16, RHEA:15469]
synonym: "1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide aldose-ketose-isomerase activity" RELATED [EC:5.3.1.16]
synonym: "1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide ketol-isomerase activity" RELATED [EC:5.3.1.16]
synonym: "N-(5'-phospho-D-ribosylformimino)-5-amino-1-(5''-phosphoribosyl)-4-imidazolecarboxamide isomerase activity" RELATED [EC:5.3.1.16]
synonym: "N-(phosphoribosylformimino) aminophosphoribosylimidazolecarboxamide isomerase activity" RELATED [EC:5.3.1.16]
synonym: "phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase activity" RELATED [EC:5.3.1.16]
synonym: "phosphoribosylformiminoaminophosphoribosylimidazolecarboxamide isomerase activity" RELATED [EC:5.3.1.16]
xref: EC:5.3.1.16
xref: KEGG_REACTION:R04640
xref: MetaCyc:PRIBFAICARPISOM-RXN
xref: RHEA:15469
is_a: GO:0016861 ! intramolecular oxidoreductase activity, interconverting aldoses and ketoses
property_value: skos:exactMatch EC:5.3.1.16
property_value: skos:exactMatch RHEA:15469

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 161. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
