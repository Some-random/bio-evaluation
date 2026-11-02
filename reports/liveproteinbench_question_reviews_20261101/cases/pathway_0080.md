# pathway_0080

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Cofactor biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIVKISWPKNNITSECFRRFGSFKRRSKSKKMSAFIEETKSLLPRIAFIACGCFSPPTPMHLRMFEIAKDHFEMQGTHRVVGGIISPTHDSYGKKGLASALDRCAMVKLATQSSNWIRLSDWEVHQNQWMRTQAVLQHHQNYINNHINSGGGGGDDGENTHLPGWLPRGLHDSRDPVHLKLLCGADLLESFAVPGLWAEADIEDIVANHGLVVITRAGSNPGKFIFDSDILTKYQSNITLITNWVPNEVSSTLIRRLLGRGQSVKYLLDDLVLEYIKRQRLFNFKSKYITDAVRPNHLLFNHAYTDNNKNANSYSIGDQLEQDMDESDTPSPQLQHTPTSRVFCCGEVPLRGSKVLRSGPGQAVQVITMQADEKEESQAKKQKISQVQL

[Multiple Choices]
A. Cofactor biosynthesis
B. Steroid biosynthesis
C. 5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis. .
D. Protein biosynthesis
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

> The exact sequence matches Drosophila NMNAT. UniProt assigns it to NAD(+) cofactor biosynthesis, with computational RuleBase and cited experimental evidence supporting the pathway annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone offers no clear, general biological clue that distinguishes these pathway categories; recognizing a particular enzyme from its sequence would require protein-specific identification.


**Missing item-specific fact**

> That this protein is nicotinamide-nucleotide adenylyltransferase (NMNAT), catalyzing a step in NAD(+) biosynthesis.


**Reason**

> The pathway assignment is supported by reviewer-only annotation for the sequence-matched protein, but that annotation and the experimentally supported protein function are absent from the question. Inferring them requires protein-specific identification or external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the supported NAD(+) biosynthesis assignment, cofactor biosynthesis is the fitting listed choice; the alternatives describe unrelated pathway categories.


### Important caveats

- The pathway annotation includes both computational evidence and cited experimental evidence; the underlying primary papers were not independently reviewed here.
- The author’s exact source snapshot is unknown, although the sequence matches the historical and current records checked.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone offers no clear, general biological clue that distinguishes these pathway categories; recognizing a particular enzyme from its sequence would require protein-specific identification.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this protein is nicotinamide-nucleotide adenylyltransferase (NMNAT), catalyzing a step in NAD(+) biosynthesis.",
    "reason": "The pathway assignment is supported by reviewer-only annotation for the sequence-matched protein, but that annotation and the experimentally supported protein function are absent from the question. Inferring them requires protein-specific identification or external annotation."
  },
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches Drosophila NMNAT. UniProt assigns it to NAD(+) cofactor biosynthesis, with computational RuleBase and cited experimental evidence supporting the pathway annotation."
  },
  "important_caveats": [
    "The pathway annotation includes both computational evidence and cited experimental evidence; the underlying primary papers were not independently reviewed here.",
    "The author’s exact source snapshot is unknown, although the sequence matches the historical and current records checked."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the supported NAD(+) biosynthesis assignment, cofactor biosynthesis is the fitting listed choice; the alternatives describe unrelated pathway categories."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches Drosophila NMNAT. UniProt assigns it to NAD(+) cofactor biosynthesis, with computational RuleBase and cited experimental evidence supporting the pathway annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone offers no clear, general biological clue that distinguishes these pathway categories; recognizing a particular enzyme from its sequence would require protein-specific identification.",
    "missing_item_specific_fact": "That this protein is nicotinamide-nucleotide adenylyltransferase (NMNAT), catalyzing a step in NAD(+) biosynthesis.",
    "reason": "The pathway assignment is supported by reviewer-only annotation for the sequence-matched protein, but that annotation and the experimentally supported protein function are absent from the question. Inferring them requires protein-specific identification or external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the supported NAD(+) biosynthesis assignment, cofactor biosynthesis is the fitting listed choice; the alternatives describe unrelated pathway categories."
  },
  "important_caveats": [
    "The pathway annotation includes both computational evidence and cited experimental evidence; the underlying primary papers were not independently reviewed here.",
    "The author’s exact source snapshot is unknown, although the sequence matches the historical and current records checked."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VC03 (NMNA_DROME) is explicitly annotated with the pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1' (evidence codes ECO:0000255|RuleBase and ECO:0000269|PubMed from three independent publications). A second pathway comment also places it under 'Cofactor biosynthesis; NAD(+) biosynthesis; deamido-NAD(+) from nicotinate D-ribonucleotide.' The sequence matches exactly (389 aa, SHA-256 confirmed). The author key 'Cofactor biosynthesis' is directly supported by both computational and experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6), [C4](#evidence-c4), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can partially eliminate distractors by general reasoning: the sequence lacks cytochrome P450 heme-binding motifs (arguing against steroid biosynthesis), does not resemble ribosomal proteins or translation factors (arguing against protein biosynthesis), and lacks the specific domains of tRNA thiolation/modification enzymes (arguing against option C). However, positively identifying 'Cofactor biosynthesis' requires recognizing the protein as a nucleotidyltransferase of the NMNAT family and knowing that NAD+ biosynthesis is classified under 'Cofactor biosynthesis' in pathway ontologies. The sequence alone does not unambiguously encode 'this is an adenylyltransferase that makes NAD+,' which is the specific item-level fact needed.


**Missing item-specific fact**

> Recognition that this 389-aa protein is Nicotinamide-nucleotide adenylyltransferase (NMNAT, EC 2.7.7.1/2.7.7.18) catalyzing the final step of NAD+ biosynthesis, and that NAD+ biosynthesis is formally categorized under 'Cofactor biosynthesis' in pathway databases.


**Reason**

> While elimination of clearly wrong options (steroid enzymes, ribosomal proteins, tRNA modification enzymes) is feasible from general sequence features, the positive assignment to 'Cofactor biosynthesis' depends on identifying the specific enzyme family (NMNAT) and its product (NAD+, a cofactor). This identification is a protein-specific fact not derivable from generic sequence heuristics alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices are well-separated biologically. NAD+ biosynthesis is unambiguously 'Cofactor biosynthesis' in standard pathway classification. The distractors (steroid biosynthesis, a very specific tRNA modification pathway, and protein biosynthesis) do not overlap with nucleotidyltransferase-mediated NAD+ synthesis. No alternative option is defensible.


### Important caveats

- The pathway annotation carries both RuleBase (computational) and PubMed (experimental) evidence codes, strengthening the annotation's reliability.
- The reviewer-only evidence was absent from the evaluated model's input; the model must work from the 389-aa sequence and four pathway labels alone.
- The sequence is from Drosophila melanogaster (fruit fly), which may limit training-data familiarity compared to human orthologs.
- Distractor C (5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis) is an extremely specific pathway name that tests familiarity with tRNA modification pathway nomenclature rather than general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can partially eliminate distractors by general reasoning: the sequence lacks cytochrome P450 heme-binding motifs (arguing against steroid biosynthesis), does not resemble ribosomal proteins or translation factors (arguing against protein biosynthesis), and lacks the specific domains of tRNA thiolation/modification enzymes (arguing against option C). However, positively identifying 'Cofactor biosynthesis' requires recognizing the protein as a nucleotidyltransferase of the NMNAT family and knowing that NAD+ biosynthesis is classified under 'Cofactor biosynthesis' in pathway ontologies. The sequence alone does not unambiguously encode 'this is an adenylyltransferase that makes NAD+,' which is the specific item-level fact needed.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this 389-aa protein is Nicotinamide-nucleotide adenylyltransferase (NMNAT, EC 2.7.7.1/2.7.7.18) catalyzing the final step of NAD+ biosynthesis, and that NAD+ biosynthesis is formally categorized under 'Cofactor biosynthesis' in pathway databases.",
    "reason": "While elimination of clearly wrong options (steroid enzymes, ribosomal proteins, tRNA modification enzymes) is feasible from general sequence features, the positive assignment to 'Cofactor biosynthesis' depends on identifying the specific enzyme family (NMNAT) and its product (NAD+, a cofactor). This identification is a protein-specific fact not derivable from generic sequence heuristics alone."
  },
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6",
      "C4",
      "C7",
      "C8",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VC03 (NMNA_DROME) is explicitly annotated with the pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1' (evidence codes ECO:0000255|RuleBase and ECO:0000269|PubMed from three independent publications). A second pathway comment also places it under 'Cofactor biosynthesis; NAD(+) biosynthesis; deamido-NAD(+) from nicotinate D-ribonucleotide.' The sequence matches exactly (389 aa, SHA-256 confirmed). The author key 'Cofactor biosynthesis' is directly supported by both computational and experimental evidence."
  },
  "important_caveats": [
    "The pathway annotation carries both RuleBase (computational) and PubMed (experimental) evidence codes, strengthening the annotation's reliability.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must work from the 389-aa sequence and four pathway labels alone.",
    "The sequence is from Drosophila melanogaster (fruit fly), which may limit training-data familiarity compared to human orthologs.",
    "Distractor C (5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis) is an extremely specific pathway name that tests familiarity with tRNA modification pathway nomenclature rather than general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated biologically. NAD+ biosynthesis is unambiguously 'Cofactor biosynthesis' in standard pathway classification. The distractors (steroid biosynthesis, a very specific tRNA modification pathway, and protein biosynthesis) do not overlap with nucleotidyltransferase-mediated NAD+ synthesis. No alternative option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VC03 (NMNA_DROME) is explicitly annotated with the pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1' (evidence codes ECO:0000255|RuleBase and ECO:0000269|PubMed from three independent publications). A second pathway comment also places it under 'Cofactor biosynthesis; NAD(+) biosynthesis; deamido-NAD(+) from nicotinate D-ribonucleotide.' The sequence matches exactly (389 aa, SHA-256 confirmed). The author key 'Cofactor biosynthesis' is directly supported by both computational and experimental evidence.",
    "evidence_ids": ["C5", "C6", "H5", "H6", "C4", "C7", "C8", "C9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can partially eliminate distractors by general reasoning: the sequence lacks cytochrome P450 heme-binding motifs (arguing against steroid biosynthesis), does not resemble ribosomal proteins or translation factors (arguing against protein biosynthesis), and lacks the specific domains of tRNA thiolation/modification enzymes (arguing against option C). However, positively identifying 'Cofactor biosynthesis' requires recognizing the protein as a nucleotidyltransferase of the NMNAT family and knowing that NAD+ biosynthesis is classified under 'Cofactor biosynthesis' in pathway ontologies. The sequence alone does not unambiguously encode 'this is an adenylyltransferase that makes NAD+,' which is the specific item-level fact needed.",
    "missing_item_specific_fact": "Recognition that this 389-aa protein is Nicotinamide-nucleotide adenylyltransferase (NMNAT, EC 2.7.7.1/2.7.7.18) catalyzing the final step of NAD+ biosynthesis, and that NAD+ biosynthesis is formally categorized under 'Cofactor biosynthesis' in pathway databases.",
    "reason": "While elimination of clearly wrong options (steroid enzymes, ribosomal proteins, tRNA modification enzymes) is feasible from general sequence features, the positive assignment to 'Cofactor biosynthesis' depends on identifying the specific enzyme family (NMNAT) and its product (NAD+, a cofactor). This identification is a protein-specific fact not derivable from generic sequence heuristics alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated biologically. NAD+ biosynthesis is unambiguously 'Cofactor biosynthesis' in standard pathway classification. The distractors (steroid biosynthesis, a very specific tRNA modification pathway, and protein biosynthesis) do not overlap with nucleotidyltransferase-mediated NAD+ synthesis. No alternative option is defensible."
  },
  "important_caveats": [
    "The pathway annotation carries both RuleBase (computational) and PubMed (experimental) evidence codes, strengthening the annotation's reliability.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must work from the 389-aa sequence and four pathway labels alone.",
    "The sequence is from Drosophila melanogaster (fruit fly), which may limit training-data familiarity compared to human orthologs.",
    "Distractor C (5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis) is an extremely specific pathway name that tests familiarity with tRNA modification pathway nomenclature rather than general biology."
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

**Accession:** `Q9VC03` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 187. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
"Q9VC03"
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0039254","source":"FlyBase"}],"value":"Nicotinamide mononucleotide adenylyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0039254","source":"FlyBase"}],"value":"dNmnat"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU362021","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"17132048","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19403820","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26616331","source":"PubMed"}],"value":"2.7.7.1"},{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU362021","source":"RuleBase"}],"value":"2.7.7.18"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU362021","source":"RuleBase"}],"value":"Nicotinamide-nucleotide adenylyltransferase"}}}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU362021","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"17132048","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19403820","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26616331","source":"PubMed"}],"value":"Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1"}]}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/comments/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cofactor biosynthesis; NAD(+) biosynthesis; deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1"}]}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"citation":{"authors":["Zhai R.G.","Cao Y.","Hiesinger P.R.","Zhou Y.","Mehta S.Q.","Schulze K.L.","Verstreken P.","Bellen H.J."],"citationCrossReferences":[{"database":"PubMed","id":"17132048"},{"database":"DOI","id":"10.1371/journal.pbio.0040416"}],"citationType":"journal article","firstPage":"e416","id":"17132048","journal":"PLoS Biol.","lastPage":"e416","publicationDate":"2006","title":"Drosophila NMNAT maintains neural integrity independent of its NAD synthesis activity.","volume":"4"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBCELLULAR LOCATION","TISSUE SPECIFICITY","DISRUPTION PHENOTYPE","MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255"]}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"citation":{"authors":["Sasaki Y.","Vohra B.P.","Lund F.E.","Milbrandt J."],"citationCrossReferences":[{"database":"PubMed","id":"19403820"},{"database":"DOI","id":"10.1523/jneurosci.5469-08.2009"}],"citationType":"journal article","firstPage":"5525","id":"19403820","journal":"J. Neurosci.","lastPage":"5535","publicationDate":"2009","title":"Nicotinamide mononucleotide adenylyl transferase-mediated axonal protection requires enzymatic activity but not increased levels of neuronal nicotinamide adenine dinucleotide.","volume":"29"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":7,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/references/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"citation":{"authors":["Ruan K.","Zhu Y.","Li C.","Brazill J.M.","Zhai R.G."],"citationCrossReferences":[{"database":"PubMed","id":"26616331"},{"database":"DOI","id":"10.1038/ncomms10057"}],"citationType":"journal article","firstPage":"10057","id":"26616331","journal":"Nat. Commun.","lastPage":"10057","publicationDate":"2015","title":"Alternative splicing of Drosophila Nmnat functions as a switch to enhance neuroprotection under stress.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":10,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBCELLULAR LOCATION","ALTERNATIVE SPLICING","INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS","NUCLEAR LOCALIZATION SIGNAL","MUTAGENESIS OF LYS-380"]}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)  
**Locator:** `lines 178-181`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 187 / 4.  
**Retrieved:** 2026-11-02T04:33:19.400018+00:00.  

```text
CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from
CC       nicotinamide D-ribonucleotide: step 1/1.
CC       {ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048,
CC       ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331}.
```

Source SHA-256: `6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)  
**Locator:** `lines 182-183`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 187 / 4.  
**Retrieved:** 2026-11-02T04:33:19.400018+00:00.  

```text
CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; deamido-NAD(+)
CC       from nicotinate D-ribonucleotide: step 1/1. {ECO:0000305}.
```

Source SHA-256: `6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 80. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
