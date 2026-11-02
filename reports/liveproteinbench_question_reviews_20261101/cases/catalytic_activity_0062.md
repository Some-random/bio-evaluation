# catalytic_activity_0062

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — a D-glucoside + &#91;(1-&gt;2)-beta-D-glucosyl&#93;(n) = a beta-D-glucosyl-(1-&gt;2)-D-glucoside + &#91;(1-&gt;2)-beta-D-glucosyl&#93;(n-1)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKPHNSEKYFVKNGQPHFLISGEVHYFRINPKLWRNHLQLLKQTGADTVSTYIPWDWHEIEEDDFDFEGKTHPARNLIRFIKLCKEENLDLIVKPGPYILAEYENQGLPSWLLKKLSKNAFALDENGNVISPDLVSYLSDEFLEYTFKWYDKVMPIISKHQKEHYGPITMMQLCNEIGVFQWLSGKSDYNPKVINLYKEFIIQRYKTIEKLNSVYSTNYNSFDDLKAPSGKIKLRSDYCAYFDFHLFFREYYNKYISILKNKIRSFGINIKLTHNIPGWIYGNASELPMLISTYSEIMKNHPDIIFGLDHIPEFVSFRNAHSDLACNKILEAMQPEAPVWAAEFQAGTREHHVKAYAKDLETFYIASLAHGIKGFNYYMFSQGINPEGKGFYGKTFYFQTALDAASNKLALYDSIKKVNRFIRKEQKDLLRTNVNSEICVGFYKPYFFTELISSQLLKEKKLNVEELGLYIDPRFLREEILFNGLLRGLQTLNYNYDVVDLENCDLKSLTAYKQLWITSAEFMDAETQNLLSEFVLNGGNLILYPAVPTLDNYLNRCEILKNNFGIEFITKDSSHKVSAFGIEDVFTAFSKKQIYNDTNSKPIAFTQENEICGIRKKIGKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQFVVRENNKSRYIFFLNYHNERKTFNYRKSSELKKKKSEEISIAPFSYKVIKENK

[Multiple Choices]
A. N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2
B. (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O
C. nicotinate beta-D-ribonucleotide + ATP + H(+) = deamido-NAD(+) + diphosphate
D. a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)
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

> The supplied sequence exactly matches the historical UniProt entry for this protein. That entry assigns EC 2.4.1.391 and records reaction D with ECO:0000269 evidence linked to a characterization paper, supporting the keyed activity.

Citations as saved: [H4](#evidence-h4), [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme reactions, but the sequence and choices alone provide no clear general biological argument that identifies this protein as the beta-1,2-glucosyltransferase in D.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental characterization assigning this sequence to EC 2.4.1.391 and reaction D.


**Reason**

> Selecting D depends on knowing the function of this particular sequence; the supporting annotation and paper were reviewer-only, not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe distinct transformations; the supplied evidence supports D for the sequence-matched protein.


### Important caveats

- The annotation is linked to experimental evidence in a cited publication, but that primary paper was not independently retrieved or validated here.
- The exact author source snapshot is unknown; the historical entry and current entry both match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct enzyme reactions, but the sequence and choices alone provide no clear general biological argument that identifies this protein as the beta-1,2-glucosyltransferase in D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization assigning this sequence to EC 2.4.1.391 and reaction D.",
    "reason": "Selecting D depends on knowing the function of this particular sequence; the supporting annotation and paper were reviewer-only, not supplied in the question."
  },
  "case_id": "catalytic_activity_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical UniProt entry for this protein. That entry assigns EC 2.4.1.391 and records reaction D with ECO:0000269 evidence linked to a characterization paper, supporting the keyed activity."
  },
  "important_caveats": [
    "The annotation is linked to experimental evidence in a cited publication, but that primary paper was not independently retrieved or validated here.",
    "The exact author source snapshot is unknown; the historical entry and current entry both match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct transformations; the supplied evidence supports D for the sequence-matched protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical UniProt entry for this protein. That entry assigns EC 2.4.1.391 and records reaction D with ECO:0000269 evidence linked to a characterization paper, supporting the keyed activity.",
    "evidence_ids": ["H4", "H3", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme reactions, but the sequence and choices alone provide no clear general biological argument that identifies this protein as the beta-1,2-glucosyltransferase in D.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization assigning this sequence to EC 2.4.1.391 and reaction D.",
    "reason": "Selecting D depends on knowing the function of this particular sequence; the supporting annotation and paper were reviewer-only, not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct transformations; the supplied evidence supports D for the sequence-matched protein."
  },
  "important_caveats": [
    "The annotation is linked to experimental evidence in a cited publication, but that primary paper was not independently retrieved or validated here.",
    "The exact author source snapshot is unknown; the historical entry and current entry both match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt I0AIT9 (B12GT_IGNAJ) from Ignavibacterium album (716 aa, sequence matched in both current and historical snapshots). The UniProt entry annotates the protein as Beta-1,2-glucosyltransferase (EC 2.4.1.391) with the catalytic activity exactly matching Choice D. The evidence code is ECO:0000269 (direct assay evidence) from PubMed:35065074 (Kobayashi et al., J. Biol. Chem. 2022), supported by X-ray crystallography of 11 PDB structures (7VKW–7VL6) in complexes with beta-D-glucose, sophorose, and alternative substrates. This is experimental, not merely computational, evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> None available from the supplied sequence. The protein is a recently characterized (2022) beta-1,2-glucosyltransferase from the obscure bacterium Ignavibacterium album, assigned the very specific EC number 2.4.1.391. No well-known glycosyltransferase family motif (e.g., GT-A/GT-B signature sequences) or other recognizable catalytic motif is apparent in the raw sequence that would allow a model to distinguish this enzyme from the three distractors (a phosphopantothenoylcysteine decarboxylase, an HMG-CoA dehydratase, and a nicotinate-ribonucleotide adenylyltransferase) through general biological reasoning. Distinguishing a glycosyltransferase from a nucleotidyltransferase (the two transferase options) would require knowledge of the specific active-site architecture and substrate-binding residues unique to this newly described enzyme class.


**Missing item-specific fact**

> The specific annotation that this exact 716-aa sequence from Ignavibacterium album is a beta-1,2-glucosyltransferase (EC 2.4.1.391) characterized in 2022. Identifying the enzyme requires recognizing the sequence as I0AIT9 and recalling or looking up its UniProt annotation, or having memorized the 2022 JBC characterization. No general sequence-to-function heuristic in standard biochemistry training would yield this specific EC assignment.


**Reason**

> The enzyme was only characterized in 2022, the UniProt entry was first published in April 2025, and the organism is an obscure anaerobic bacterium. The sequence lacks recognizable motifs that would let a model assign it to a specific glycosyltransferase subfamily or distinguish it from the other three mechanistically unrelated enzymes. Selection of the correct answer depends on item-specific database knowledge or memorization of this particular entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent mechanistically distinct enzyme classes (decarboxylase, dehydratase, nucleotidyltransferase, glycosyltransferase), so they are not confusable with one another once the correct class is identified. The difficulty lies entirely in identifying the correct class from the sequence, not in ambiguity among the options.


### Important caveats

- The UniProt entry I0AIT9 was first publicly released on 2025-04-09, and the underlying characterization paper (PubMed 35065074) was published in 2022. A model trained before mid-2025 would have no database exposure to this annotation.
- The identity of the protein (accession I0AIT9) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.
- The catalytic activity evidence is experimental (ECO:0000269, direct assay + crystallography), lending high confidence to the annotation, but this does not help a model answer from sequence alone.
- The sequence length (716 aa) and organism (Ignavibacterium album) are unusual; no standard textbook or well-known model organism context aids recognition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "None available from the supplied sequence. The protein is a recently characterized (2022) beta-1,2-glucosyltransferase from the obscure bacterium Ignavibacterium album, assigned the very specific EC number 2.4.1.391. No well-known glycosyltransferase family motif (e.g., GT-A/GT-B signature sequences) or other recognizable catalytic motif is apparent in the raw sequence that would allow a model to distinguish this enzyme from the three distractors (a phosphopantothenoylcysteine decarboxylase, an HMG-CoA dehydratase, and a nicotinate-ribonucleotide adenylyltransferase) through general biological reasoning. Distinguishing a glycosyltransferase from a nucleotidyltransferase (the two transferase options) would require knowledge of the specific active-site architecture and substrate-binding residues unique to this newly described enzyme class.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific annotation that this exact 716-aa sequence from Ignavibacterium album is a beta-1,2-glucosyltransferase (EC 2.4.1.391) characterized in 2022. Identifying the enzyme requires recognizing the sequence as I0AIT9 and recalling or looking up its UniProt annotation, or having memorized the 2022 JBC characterization. No general sequence-to-function heuristic in standard biochemistry training would yield this specific EC assignment.",
    "reason": "The enzyme was only characterized in 2022, the UniProt entry was first published in April 2025, and the organism is an obscure anaerobic bacterium. The sequence lacks recognizable motifs that would let a model assign it to a specific glycosyltransferase subfamily or distinguish it from the other three mechanistically unrelated enzymes. Selection of the correct answer depends on item-specific database knowledge or memorization of this particular entry."
  },
  "case_id": "catalytic_activity_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt I0AIT9 (B12GT_IGNAJ) from Ignavibacterium album (716 aa, sequence matched in both current and historical snapshots). The UniProt entry annotates the protein as Beta-1,2-glucosyltransferase (EC 2.4.1.391) with the catalytic activity exactly matching Choice D. The evidence code is ECO:0000269 (direct assay evidence) from PubMed:35065074 (Kobayashi et al., J. Biol. Chem. 2022), supported by X-ray crystallography of 11 PDB structures (7VKW–7VL6) in complexes with beta-D-glucose, sophorose, and alternative substrates. This is experimental, not merely computational, evidence."
  },
  "important_caveats": [
    "The UniProt entry I0AIT9 was first publicly released on 2025-04-09, and the underlying characterization paper (PubMed 35065074) was published in 2022. A model trained before mid-2025 would have no database exposure to this annotation.",
    "The identity of the protein (accession I0AIT9) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.",
    "The catalytic activity evidence is experimental (ECO:0000269, direct assay + crystallography), lending high confidence to the annotation, but this does not help a model answer from sequence alone.",
    "The sequence length (716 aa) and organism (Ignavibacterium album) are unusual; no standard textbook or well-known model organism context aids recognition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes (decarboxylase, dehydratase, nucleotidyltransferase, glycosyltransferase), so they are not confusable with one another once the correct class is identified. The difficulty lies entirely in identifying the correct class from the sequence, not in ambiguity among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt I0AIT9 (B12GT_IGNAJ) from Ignavibacterium album (716 aa, sequence matched in both current and historical snapshots). The UniProt entry annotates the protein as Beta-1,2-glucosyltransferase (EC 2.4.1.391) with the catalytic activity exactly matching Choice D. The evidence code is ECO:0000269 (direct assay evidence) from PubMed:35065074 (Kobayashi et al., J. Biol. Chem. 2022), supported by X-ray crystallography of 11 PDB structures (7VKW–7VL6) in complexes with beta-D-glucose, sophorose, and alternative substrates. This is experimental, not merely computational, evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "None available from the supplied sequence. The protein is a recently characterized (2022) beta-1,2-glucosyltransferase from the obscure bacterium Ignavibacterium album, assigned the very specific EC number 2.4.1.391. No well-known glycosyltransferase family motif (e.g., GT-A/GT-B signature sequences) or other recognizable catalytic motif is apparent in the raw sequence that would allow a model to distinguish this enzyme from the three distractors (a phosphopantothenoylcysteine decarboxylase, an HMG-CoA dehydratase, and a nicotinate-ribonucleotide adenylyltransferase) through general biological reasoning. Distinguishing a glycosyltransferase from a nucleotidyltransferase (the two transferase options) would require knowledge of the specific active-site architecture and substrate-binding residues unique to this newly described enzyme class.",
    "missing_item_specific_fact": "The specific annotation that this exact 716-aa sequence from Ignavibacterium album is a beta-1,2-glucosyltransferase (EC 2.4.1.391) characterized in 2022. Identifying the enzyme requires recognizing the sequence as I0AIT9 and recalling or looking up its UniProt annotation, or having memorized the 2022 JBC characterization. No general sequence-to-function heuristic in standard biochemistry training would yield this specific EC assignment.",
    "reason": "The enzyme was only characterized in 2022, the UniProt entry was first published in April 2025, and the organism is an obscure anaerobic bacterium. The sequence lacks recognizable motifs that would let a model assign it to a specific glycosyltransferase subfamily or distinguish it from the other three mechanistically unrelated enzymes. Selection of the correct answer depends on item-specific database knowledge or memorization of this particular entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes (decarboxylase, dehydratase, nucleotidyltransferase, glycosyltransferase), so they are not confusable with one another once the correct class is identified. The difficulty lies entirely in identifying the correct class from the sequence, not in ambiguity among the options."
  },
  "important_caveats": [
    "The UniProt entry I0AIT9 was first publicly released on 2025-04-09, and the underlying characterization paper (PubMed 35065074) was published in 2022. A model trained before mid-2025 would have no database exposure to this annotation.",
    "The identity of the protein (accession I0AIT9) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.",
    "The catalytic activity evidence is experimental (ECO:0000269, direct assay + crystallography), lending high confidence to the annotation, but this does not help a model answer from sequence alone.",
    "The sequence length (716 aa) and organism (Ignavibacterium album) are unusual; no standard textbook or well-known model organism context aids recognition."
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

**Accession:** `I0AIT9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 55. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
"I0AIT9"
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35065074","source":"PubMed"}],"value":"Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35065074","source":"PubMed"}],"value":"IaSGT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"value":"2.4.1.391"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35065074","source":"PubMed"}],"value":"Beta-1,2-glucosyltransferase"}}}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.4.1.391","evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"name":"a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78691"},{"database":"Rhea","id":"RHEA-COMP:11881"},{"database":"Rhea","id":"RHEA-COMP:11882"},{"database":"ChEBI","id":"CHEBI:27517"},{"database":"ChEBI","id":"CHEBI:35436"},{"database":"ChEBI","id":"CHEBI:229541"}]}}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"citation":{"authors":["Kobayashi K.","Shimizu H.","Tanaka N.","Kuramochi K.","Nakai H.","Nakajima M.","Taguchi H."],"citationCrossReferences":[{"database":"PubMed","id":"35065074"},{"database":"DOI","id":"10.1016/j.jbc.2022.101606"}],"citationType":"journal article","firstPage":"101606","id":"35065074","journal":"J. Biol. Chem.","lastPage":"101606","publicationDate":"2022","title":"Characterization and structural analyses of a novel glycosyltransferase acting on the beta-1,2-glucosidic linkages.","volume":"298"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7VKW","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKX","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKY","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL0","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL1","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL2","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL3","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL4","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL5","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL6","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE; SOPHOROSE AND ALTERNATIVE SUBSTRATES","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","ACTIVE SITE","MUTAGENESIS OF GLU-176 AND GLU-343"]}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
ID   B12GT_IGNAJ             Reviewed;         716 AA.
AC   I0AIT9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-JUN-2012, sequence version 1.
DT   28-JAN-2026, entry version 55.
DE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};
DE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};
DE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};
DE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};
GN   OrderedLocusNames=IALB_1185 {ECO:0000312|EMBL:AFH48896.1};
OS   Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 /
OS   Mat9-16).
OC   Bacteria; Pseudomonadati; Ignavibacteriota; Ignavibacteria;
OC   Ignavibacteriales; Ignavibacteriaceae; Ignavibacterium.
OX   NCBI_TaxID=945713;
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
DE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};
DE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};
DE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};
DE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 25-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
RN   [2] {ECO:0007744|PDB:7VKW, ECO:0007744|PDB:7VKX, ECO:0007744|PDB:7VKY, ECO:0007744|PDB:7VKZ, ECO:0007744|PDB:7VL0, ECO:0007744|PDB:7VL1, ECO:0007744|PDB:7VL2, ECO:0007744|PDB:7VL3, ECO:0007744|PDB:7VL4, ECO:0007744|PDB:7VL5, ECO:0007744|PDB:7VL6}
RP   X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE;
RP   SOPHOROSE AND ALTERNATIVE SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF
RP   GLU-176 AND GLU-343.
RC   STRAIN=DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16;
RX   PubMed=35065074; DOI=10.1016/j.jbc.2022.101606;
RA   Kobayashi K., Shimizu H., Tanaka N., Kuramochi K., Nakai H., Nakajima M.,
RA   Taguchi H.;
RT   "Characterization and structural analyses of a novel glycosyltransferase
RT   acting on the beta-1,2-glucosidic linkages.";
RL   J. Biol. Chem. 298:101606-101606(2022).
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 46-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-
CC         glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1);
CC         Xref=Rhea:RHEA:78691, Rhea:RHEA-COMP:11881, Rhea:RHEA-COMP:11882,
CC         ChEBI:CHEBI:27517, ChEBI:CHEBI:35436, ChEBI:CHEBI:229541;
CC         EC=2.4.1.391; Evidence={ECO:0000269|PubMed:35065074};
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 62. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
