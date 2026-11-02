# GO_biological_process_0085

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — carbohydrate metabolic process

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
A. carbohydrate metabolic process
B. regulation of macromolecule metabolic process
C. response to insulin
D. regulation of angiogenesis
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

> The sequence matches the annotated protein. Its experimentally supported function is a glycosyltransferase that transfers glucosyl residues between carbohydrate substrates, supporting carbohydrate metabolic process. The GO annotation itself is computational (IEA:InterPro), while the protein-function annotation cites experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a large globular protein with no obvious signal peptide or membrane-spanning regions, but those generic features do not identify its biological process or distinguish carbohydrate metabolism from the broad regulatory option.


**Missing item-specific fact**

> The protein-specific fact needed is that this sequence encodes a beta-1,2-glucosyltransferase acting on glucooligosaccharides.


**Reason**

> That catalytic identity is not established by the supplied context or a decisive, self-evident sequence feature; selecting A depends on identifying or looking up the particular protein's function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein's reported catalytic activity supports A; the other choices do not describe that activity.


### Important caveats

- The GO term annotation is computational, whereas the cited catalytic-function annotation is experimentally supported.
- The sequence match is established for the reviewed current and historical records, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a large globular protein with no obvious signal peptide or membrane-spanning regions, but those generic features do not identify its biological process or distinguish carbohydrate metabolism from the broad regulatory option.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact needed is that this sequence encodes a beta-1,2-glucosyltransferase acting on glucooligosaccharides.",
    "reason": "That catalytic identity is not established by the supplied context or a decisive, self-evident sequence feature; selecting A depends on identifying or looking up the particular protein's function."
  },
  "case_id": "GO_biological_process_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein. Its experimentally supported function is a glycosyltransferase that transfers glucosyl residues between carbohydrate substrates, supporting carbohydrate metabolic process. The GO annotation itself is computational (IEA:InterPro), while the protein-function annotation cites experimental evidence."
  },
  "important_caveats": [
    "The GO term annotation is computational, whereas the cited catalytic-function annotation is experimentally supported.",
    "The sequence match is established for the reviewed current and historical records, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's reported catalytic activity supports A; the other choices do not describe that activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein. Its experimentally supported function is a glycosyltransferase that transfers glucosyl residues between carbohydrate substrates, supporting carbohydrate metabolic process. The GO annotation itself is computational (IEA:InterPro), while the protein-function annotation cites experimental evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a large globular protein with no obvious signal peptide or membrane-spanning regions, but those generic features do not identify its biological process or distinguish carbohydrate metabolism from the broad regulatory option.",
    "missing_item_specific_fact": "The protein-specific fact needed is that this sequence encodes a beta-1,2-glucosyltransferase acting on glucooligosaccharides.",
    "reason": "That catalytic identity is not established by the supplied context or a decisive, self-evident sequence feature; selecting A depends on identifying or looking up the particular protein's function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's reported catalytic activity supports A; the other choices do not describe that activity."
  },
  "important_caveats": [
    "The GO term annotation is computational, whereas the cited catalytic-function annotation is experimentally supported.",
    "The sequence match is established for the reviewed current and historical records, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (UniProt I0AIT9, B12GT_IGNAJ from Ignavibacterium album) is experimentally characterized as a Beta-1,2-glucosyltransferase (EC 2.4.1.391) that catalyzes transfer of glucosyl residues between carbohydrate acceptors, confirmed by X-ray crystallography and enzymatic assays (PubMed:35065074). This activity is squarely within GO:0005975 'carbohydrate metabolic process' (chemical reactions and pathways involving carbohydrates). The UniProt GO annotation is IEA:InterPro (computational), but the underlying experimental evidence (ECO:0000269) confirms the glycosyltransferase function on glucose/oligosaccharide substrates, which is a carbohydrate metabolic reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General biological reasoning allows elimination of options C (response to insulin) and D (regulation of angiogenesis) as eukaryotic/mammalian-specific processes inapplicable to a bacterial protein. However, distinguishing A (carbohydrate metabolic process) from B (regulation of macromolecule metabolic process) requires identifying the protein's specific enzymatic function—namely, that it is a glycosyltransferase directly catalyzing a carbohydrate reaction rather than a regulatory factor modulating metabolic rate. This identification from a 716-aa sequence of a 'novel' enzyme from an obscure bacterium (Ignavibacterium album) is not achievable through general biological reasoning alone.


**Missing item-specific fact**

> The specific identity of this protein as a Beta-1,2-glucosyltransferase (EC 2.4.1.391) acting on beta-1,2-glucooligosaccharides, which was established through experimental characterization (crystallography, enzymatic assays) and is not inferable from the raw sequence without database comparison or memorization of this specific enzyme.


**Reason**

> While elimination of eukaryotic-specific distractors (C, D) is possible via general knowledge, the critical A-vs-B discrimination requires knowing this particular protein is a direct metabolic enzyme (glycosyltransferase) rather than a regulatory protein. The protein is from an obscure organism, described as 'novel,' and its GO annotation is IEA:InterPro (computational pattern match). Recognizing glycosyltransferase motifs in a novel enzyme sequence without database lookup is not general biological reasoning but specialized pattern recognition bordering on memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the protein's identity as a glycosyltransferase is known, A is clearly correct and B is wrong (a direct catalytic enzyme is not a 'regulation' factor). C and D are inapplicable to a bacterium. No genuine ambiguity exists in the answer key itself.


### Important caveats

- The GO annotation for this protein is IEA:InterPro (Inferred from Electronic Annotation), not a direct experimental GO assignment. However, the underlying experimental evidence (ECO:0000269, PubMed:35065074) confirms the enzymatic function.
- The protein is from Ignavibacterium album, a relatively obscure anaerobic bacterium, making sequence-based identification without database access extremely difficult.
- GO:0060255 (option B) carries the 'gocheck_do_not_annotate' subset tag, indicating it is a deprecated/discouraged annotation term, further weakening it as a distractor.
- The sequence-match is confirmed (SHA256 match between benchmark sequence and UniProt I0AIT9), so the reviewer evidence applies to the exact protein presented.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General biological reasoning allows elimination of options C (response to insulin) and D (regulation of angiogenesis) as eukaryotic/mammalian-specific processes inapplicable to a bacterial protein. However, distinguishing A (carbohydrate metabolic process) from B (regulation of macromolecule metabolic process) requires identifying the protein's specific enzymatic function—namely, that it is a glycosyltransferase directly catalyzing a carbohydrate reaction rather than a regulatory factor modulating metabolic rate. This identification from a 716-aa sequence of a 'novel' enzyme from an obscure bacterium (Ignavibacterium album) is not achievable through general biological reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as a Beta-1,2-glucosyltransferase (EC 2.4.1.391) acting on beta-1,2-glucooligosaccharides, which was established through experimental characterization (crystallography, enzymatic assays) and is not inferable from the raw sequence without database comparison or memorization of this specific enzyme.",
    "reason": "While elimination of eukaryotic-specific distractors (C, D) is possible via general knowledge, the critical A-vs-B discrimination requires knowing this particular protein is a direct metabolic enzyme (glycosyltransferase) rather than a regulatory protein. The protein is from an obscure organism, described as 'novel,' and its GO annotation is IEA:InterPro (computational pattern match). Recognizing glycosyltransferase motifs in a novel enzyme sequence without database lookup is not general biological reasoning but specialized pattern recognition bordering on memorization."
  },
  "case_id": "GO_biological_process_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein (UniProt I0AIT9, B12GT_IGNAJ from Ignavibacterium album) is experimentally characterized as a Beta-1,2-glucosyltransferase (EC 2.4.1.391) that catalyzes transfer of glucosyl residues between carbohydrate acceptors, confirmed by X-ray crystallography and enzymatic assays (PubMed:35065074). This activity is squarely within GO:0005975 'carbohydrate metabolic process' (chemical reactions and pathways involving carbohydrates). The UniProt GO annotation is IEA:InterPro (computational), but the underlying experimental evidence (ECO:0000269) confirms the glycosyltransferase function on glucose/oligosaccharide substrates, which is a carbohydrate metabolic reaction."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA:InterPro (Inferred from Electronic Annotation), not a direct experimental GO assignment. However, the underlying experimental evidence (ECO:0000269, PubMed:35065074) confirms the enzymatic function.",
    "The protein is from Ignavibacterium album, a relatively obscure anaerobic bacterium, making sequence-based identification without database access extremely difficult.",
    "GO:0060255 (option B) carries the 'gocheck_do_not_annotate' subset tag, indicating it is a deprecated/discouraged annotation term, further weakening it as a distractor.",
    "The sequence-match is confirmed (SHA256 match between benchmark sequence and UniProt I0AIT9), so the reviewer evidence applies to the exact protein presented."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein's identity as a glycosyltransferase is known, A is clearly correct and B is wrong (a direct catalytic enzyme is not a 'regulation' factor). C and D are inapplicable to a bacterium. No genuine ambiguity exists in the answer key itself."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (UniProt I0AIT9, B12GT_IGNAJ from Ignavibacterium album) is experimentally characterized as a Beta-1,2-glucosyltransferase (EC 2.4.1.391) that catalyzes transfer of glucosyl residues between carbohydrate acceptors, confirmed by X-ray crystallography and enzymatic assays (PubMed:35065074). This activity is squarely within GO:0005975 'carbohydrate metabolic process' (chemical reactions and pathways involving carbohydrates). The UniProt GO annotation is IEA:InterPro (computational), but the underlying experimental evidence (ECO:0000269) confirms the glycosyltransferase function on glucose/oligosaccharide substrates, which is a carbohydrate metabolic reaction.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General biological reasoning allows elimination of options C (response to insulin) and D (regulation of angiogenesis) as eukaryotic/mammalian-specific processes inapplicable to a bacterial protein. However, distinguishing A (carbohydrate metabolic process) from B (regulation of macromolecule metabolic process) requires identifying the protein's specific enzymatic function—namely, that it is a glycosyltransferase directly catalyzing a carbohydrate reaction rather than a regulatory factor modulating metabolic rate. This identification from a 716-aa sequence of a 'novel' enzyme from an obscure bacterium (Ignavibacterium album) is not achievable through general biological reasoning alone.",
    "missing_item_specific_fact": "The specific identity of this protein as a Beta-1,2-glucosyltransferase (EC 2.4.1.391) acting on beta-1,2-glucooligosaccharides, which was established through experimental characterization (crystallography, enzymatic assays) and is not inferable from the raw sequence without database comparison or memorization of this specific enzyme.",
    "reason": "While elimination of eukaryotic-specific distractors (C, D) is possible via general knowledge, the critical A-vs-B discrimination requires knowing this particular protein is a direct metabolic enzyme (glycosyltransferase) rather than a regulatory protein. The protein is from an obscure organism, described as 'novel,' and its GO annotation is IEA:InterPro (computational pattern match). Recognizing glycosyltransferase motifs in a novel enzyme sequence without database lookup is not general biological reasoning but specialized pattern recognition bordering on memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein's identity as a glycosyltransferase is known, A is clearly correct and B is wrong (a direct catalytic enzyme is not a 'regulation' factor). C and D are inapplicable to a bacterium. No genuine ambiguity exists in the answer key itself."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA:InterPro (Inferred from Electronic Annotation), not a direct experimental GO assignment. However, the underlying experimental evidence (ECO:0000269, PubMed:35065074) confirms the enzymatic function.",
    "The protein is from Ignavibacterium album, a relatively obscure anaerobic bacterium, making sequence-based identification without database access extremely difficult.",
    "GO:0060255 (option B) carries the 'gocheck_do_not_annotate' subset tag, indicating it is a deprecated/discouraged annotation term, further weakening it as a distractor.",
    "The sequence-match is confirmed (SHA256 match between benchmark sequence and UniProt I0AIT9), so the reviewer evidence applies to the exact protein presented."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"value":"Glycosyltransferase acting on beta-1,2-glucooligosaccharides (PubMed:35065074). Catalyzes the transfer of a glucosyl residue from the non-reducing end of a 1,2-beta-D-glucan to a glucose residue of an acceptor molecule, forming a beta-1,2-glucosidic bond (PubMed:35065074). The beta-1,2-linked glucose dimer sophorose is the preferred donor in vitro (PubMed:35065074). Has a very broad specificity for the acceptor and can act on various aryl- and alkyl-glucosides (PubMed:35065074). Does not show any hydrolytic activity (PubMed:35065074)"}]}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/uniProtKBCrossReferences/41`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"database":"GO","id":"GO:0005975","properties":[{"key":"GoTerm","value":"P:carbohydrate metabolic process"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"citation":{"authors":["Kobayashi K.","Shimizu H.","Tanaka N.","Kuramochi K.","Nakai H.","Nakajima M.","Taguchi H."],"citationCrossReferences":[{"database":"PubMed","id":"35065074"},{"database":"DOI","id":"10.1016/j.jbc.2022.101606"}],"citationType":"journal article","firstPage":"101606","id":"35065074","journal":"J. Biol. Chem.","lastPage":"101606","publicationDate":"2022","title":"Characterization and structural analyses of a novel glycosyltransferase acting on the beta-1,2-glucosidic linkages.","volume":"298"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7VKW","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKX","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKY","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL0","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL1","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL2","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL3","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL4","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL5","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL6","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE; SOPHOROSE AND ALTERNATIVE SUBSTRATES","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","ACTIVE SITE","MUTAGENESIS OF GLU-176 AND GLU-343"]}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 37-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
CC   -!- FUNCTION: Glycosyltransferase acting on beta-1,2-glucooligosaccharides
CC       (PubMed:35065074). Catalyzes the transfer of a glucosyl residue from
CC       the non-reducing end of a 1,2-beta-D-glucan to a glucose residue of an
CC       acceptor molecule, forming a beta-1,2-glucosidic bond
CC       (PubMed:35065074). The beta-1,2-linked glucose dimer sophorose is the
CC       preferred donor in vitro (PubMed:35065074). Has a very broad
CC       specificity for the acceptor and can act on various aryl- and alkyl-
CC       glucosides (PubMed:35065074). Does not show any hydrolytic activity
CC       (PubMed:35065074). {ECO:0000269|PubMed:35065074}.
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 140-140`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
DR   GO; GO:0005975; P:carbohydrate metabolic process; IEA:InterPro.
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 61261-61283`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005975
name: carbohydrate metabolic process
namespace: biological_process
alt_id: GO:0044261
alt_id: GO:0044723
def: "The chemical reactions and pathways involving carbohydrates, any of a group of organic compounds based of the general formula Cx(H2O)y." [GOC:mah, ISBN:0198506732]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_pombe
subset: goslim_prokaryote
subset: goslim_yeast
synonym: "carbohydrate metabolism" EXACT []
xref: Wikipedia:Carbohydrate_metabolism
is_a: GO:0044238 ! primary metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
