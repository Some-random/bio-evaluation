# catalytic_activity_0053

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSKIFGIVNITTDSFSDGGLYLDTDKAIEHALHLVEDGADVIDLGAASSNPDTTEVGVVEEIKRLKPVIKALKEKGISISVDTFKPEVQSFCIEQKVDFINDIQGFPYPEIYSGLAKSDCKLVLMHSVQRIGAATKVETNPEEVFTSMMEFFKERIAALVEAGVKRERIILDPGMGFFLGSNPETSILVLKRFPEIQEAFNLQVMIAVSRKSFLGKITGTDVKSRLAPTLAAEMYAYKKGADYLRTHDVKSLSDALKISKALG

[Multiple Choices]
A. lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol
B. (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate
C. (2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)
D. (S)-norprotosinomenine + S-adenosyl-L-methionine = (S)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)
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

> The supplied sequence exactly matches the 263-aa protein annotated as dihydropteroate synthase type-3, and the matching entry assigns it the reaction in choice B. The catalytic-activity annotation cites experimental evidence, although the available excerpts do not independently validate the underlying study.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme reactions, but the input gives only a sequence and no organism, pathway, enzyme name, or recognizable reaction context that meaningfully identifies which reaction applies.


**Missing item-specific fact**

> The protein-specific identity or experimentally established catalytic activity linking this sequence to dihydropteroate synthase and reaction B.


**Reason**

> The sequence-to-function association is item-specific; recalling or externally identifying this exact protein would be lookup or memorization, not reasoning from information supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched annotation supports B, and the options state different reactions; no evidence here supports another listed reaction for this sequence.


### Important caveats

- Reviewer-only database evidence supports the key but was not available to the evaluated model.
- UniProt identifies the sequence as E. coli dihydropteroate synthase type-3; its annotation cites experimental evidence, but the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct enzyme reactions, but the input gives only a sequence and no organism, pathway, enzyme name, or recognizable reaction context that meaningfully identifies which reaction applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity or experimentally established catalytic activity linking this sequence to dihydropteroate synthase and reaction B.",
    "reason": "The sequence-to-function association is item-specific; recalling or externally identifying this exact protein would be lookup or memorization, not reasoning from information supplied in the question."
  },
  "case_id": "catalytic_activity_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 263-aa protein annotated as dihydropteroate synthase type-3, and the matching entry assigns it the reaction in choice B. The catalytic-activity annotation cites experimental evidence, although the available excerpts do not independently validate the underlying study."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "UniProt identifies the sequence as E. coli dihydropteroate synthase type-3; its annotation cites experimental evidence, but the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation supports B, and the options state different reactions; no evidence here supports another listed reaction for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 263-aa protein annotated as dihydropteroate synthase type-3, and the matching entry assigns it the reaction in choice B. The catalytic-activity annotation cites experimental evidence, although the available excerpts do not independently validate the underlying study.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme reactions, but the input gives only a sequence and no organism, pathway, enzyme name, or recognizable reaction context that meaningfully identifies which reaction applies.",
    "missing_item_specific_fact": "The protein-specific identity or experimentally established catalytic activity linking this sequence to dihydropteroate synthase and reaction B.",
    "reason": "The sequence-to-function association is item-specific; recalling or externally identifying this exact protein would be lookup or memorization, not reasoning from information supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation supports B, and the options state different reactions; no evidence here supports another listed reaction for this sequence."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "UniProt identifies the sequence as E. coli dihydropteroate synthase type-3; its annotation cites experimental evidence, but the primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt C0HMD9 (DHP3_ECOLX, sul3 gene product) exactly. The UniProt entry annotates the catalytic activity as EC 2.5.1.15: (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate, supported by experimental evidence (ECO:0000269, PubMed:37419898, X-ray crystallography in complexes with substrates). This matches Choice B verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence lacks a classic NAD(P)-binding Rossmann fold (argues weakly against C), lacks a canonical SAM-binding MTase motif (argues weakly against D), and lacks transmembrane helices (argues weakly against A). However, these are only negative eliminations. The sequence does not display the conserved folP motifs (e.g., the DHPS signature 'GGN' loop, the conserved 'QxxQ' and 'HxxxN' residues) because sul3 is a highly divergent type III DHPS with low sequence identity to chromosomal folP. Positive identification requires knowing that this sequence corresponds to the plasmid-borne sulfonamide-resistance protein sul3, which is a DHPS variant.


**Missing item-specific fact**

> Recognition that this 263-aa sequence is the sul3 (sulfonamide resistance) protein, a divergent type III dihydropteroate synthase, rather than a canonical folP. The sequence provides no strong positive DHPS motif that would allow general reasoning to select B over C or D without prior knowledge of sul3's identity.


**Reason**

> Distinguishing B from C and D requires knowing the specific identity of this plasmid-borne resistance gene product. The sequence lacks the canonical DHPS conserved motifs due to its divergence, and the remaining choices (vomilenine reductase, O-methyltransferase) cannot be confidently excluded by motif scanning alone. The answer depends on recognizing or memorizing that sul3 = DHPS type III.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the protein is correctly identified as DHPS type III, only B is correct. The four choices span entirely different enzyme classes and pathways, so there is no genuine ambiguity among the options for a correctly identified protein.


### Important caveats

- The UniProt annotation for EC 2.5.1.15 is supported by both RuleBase (ECO:0000255) and experimental evidence from X-ray crystallography with substrates (ECO:0000269, PubMed:37419898, PDB 7S2L/7S2M/8SCD), so the annotation is experimentally grounded.
- The sul3 protein is a plasmid-borne, highly divergent DHPS variant; it shares the TIM-barrel fold with canonical folP but has low sequence identity, making motif-based identification from sequence alone unreliable.
- The reviewer-only evidence was absent from the evaluated model's input; the model saw only the raw sequence and four reaction choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks a classic NAD(P)-binding Rossmann fold (argues weakly against C), lacks a canonical SAM-binding MTase motif (argues weakly against D), and lacks transmembrane helices (argues weakly against A). However, these are only negative eliminations. The sequence does not display the conserved folP motifs (e.g., the DHPS signature 'GGN' loop, the conserved 'QxxQ' and 'HxxxN' residues) because sul3 is a highly divergent type III DHPS with low sequence identity to chromosomal folP. Positive identification requires knowing that this sequence corresponds to the plasmid-borne sulfonamide-resistance protein sul3, which is a DHPS variant.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this 263-aa sequence is the sul3 (sulfonamide resistance) protein, a divergent type III dihydropteroate synthase, rather than a canonical folP. The sequence provides no strong positive DHPS motif that would allow general reasoning to select B over C or D without prior knowledge of sul3's identity.",
    "reason": "Distinguishing B from C and D requires knowing the specific identity of this plasmid-borne resistance gene product. The sequence lacks the canonical DHPS conserved motifs due to its divergence, and the remaining choices (vomilenine reductase, O-methyltransferase) cannot be confidently excluded by motif scanning alone. The answer depends on recognizing or memorizing that sul3 = DHPS type III."
  },
  "case_id": "catalytic_activity_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt C0HMD9 (DHP3_ECOLX, sul3 gene product) exactly. The UniProt entry annotates the catalytic activity as EC 2.5.1.15: (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate, supported by experimental evidence (ECO:0000269, PubMed:37419898, X-ray crystallography in complexes with substrates). This matches Choice B verbatim."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.5.1.15 is supported by both RuleBase (ECO:0000255) and experimental evidence from X-ray crystallography with substrates (ECO:0000269, PubMed:37419898, PDB 7S2L/7S2M/8SCD), so the annotation is experimentally grounded.",
    "The sul3 protein is a plasmid-borne, highly divergent DHPS variant; it shares the TIM-barrel fold with canonical folP but has low sequence identity, making motif-based identification from sequence alone unreliable.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model saw only the raw sequence and four reaction choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is correctly identified as DHPS type III, only B is correct. The four choices span entirely different enzyme classes and pathways, so there is no genuine ambiguity among the options for a correctly identified protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt C0HMD9 (DHP3_ECOLX, sul3 gene product) exactly. The UniProt entry annotates the catalytic activity as EC 2.5.1.15: (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate, supported by experimental evidence (ECO:0000269, PubMed:37419898, X-ray crystallography in complexes with substrates). This matches Choice B verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence lacks a classic NAD(P)-binding Rossmann fold (argues weakly against C), lacks a canonical SAM-binding MTase motif (argues weakly against D), and lacks transmembrane helices (argues weakly against A). However, these are only negative eliminations. The sequence does not display the conserved folP motifs (e.g., the DHPS signature 'GGN' loop, the conserved 'QxxQ' and 'HxxxN' residues) because sul3 is a highly divergent type III DHPS with low sequence identity to chromosomal folP. Positive identification requires knowing that this sequence corresponds to the plasmid-borne sulfonamide-resistance protein sul3, which is a DHPS variant.",
    "missing_item_specific_fact": "Recognition that this 263-aa sequence is the sul3 (sulfonamide resistance) protein, a divergent type III dihydropteroate synthase, rather than a canonical folP. The sequence provides no strong positive DHPS motif that would allow general reasoning to select B over C or D without prior knowledge of sul3's identity.",
    "reason": "Distinguishing B from C and D requires knowing the specific identity of this plasmid-borne resistance gene product. The sequence lacks the canonical DHPS conserved motifs due to its divergence, and the remaining choices (vomilenine reductase, O-methyltransferase) cannot be confidently excluded by motif scanning alone. The answer depends on recognizing or memorizing that sul3 = DHPS type III."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is correctly identified as DHPS type III, only B is correct. The four choices span entirely different enzyme classes and pathways, so there is no genuine ambiguity among the options for a correctly identified protein."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.5.1.15 is supported by both RuleBase (ECO:0000255) and experimental evidence from X-ray crystallography with substrates (ECO:0000269, PubMed:37419898, PDB 7S2L/7S2M/8SCD), so the annotation is experimentally grounded.",
    "The sul3 protein is a plasmid-borne, highly divergent DHPS variant; it shares the TIM-barrel fold with canonical folP but has low sequence identity, making motif-based identification from sequence alone unreliable.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model saw only the raw sequence and four reaction choices."
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

**Accession:** `C0HMD9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:26.472274+00:00.  

```json
"C0HMD9"
```

Source SHA-256: `ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:26.472274+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P0C002","source":"UniProtKB"}],"value":"Dihydropteroate pyrophosphorylase type III"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P0C002","source":"UniProtKB"}],"value":"Dihydropteroate synthase type III"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361205","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"37419898","source":"PubMed"}],"value":"2.5.1.15"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361205","source":"RuleBase"},{"evidenceCode":"ECO:0000303","id":"37419898","source":"PubMed"}],"value":"Dihydropteroate synthase type-3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361205","source":"RuleBase"},{"evidenceCode":"ECO:0000303","id":"37419898","source":"PubMed"}],"value":"DHPS"}]}}
```

Source SHA-256: `ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:26.472274+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.5.1.15","evidences":[{"evidenceCode":"ECO:0000269","id":"37419898","source":"PubMed"}],"name":"(7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19949"},{"database":"ChEBI","id":"CHEBI:17836"},{"database":"ChEBI","id":"CHEBI:17839"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:72950"}]}}
```

Source SHA-256: `ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:26.472274+00:00.  

```json
{"citation":{"authors":["Venkatesan M.","Fruci M.","Verellen L.A.","Skarina T.","Mesa N.","Flick R.","Pham C.","Mahadevan R.","Stogios P.J.","Savchenko A."],"citationCrossReferences":[{"database":"PubMed","id":"37419898"},{"database":"DOI","id":"10.1038/s41467-023-39778-7"}],"citationType":"journal article","firstPage":"4031","id":"37419898","journal":"Nat. Commun.","lastPage":"4031","publicationDate":"2023","title":"Molecular mechanism of plasmid-borne resistance to sulfonamide antibiotics.","volume":"14"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7S2L","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7S2M","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8SCD","source":"PDB"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.06 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH MG(2+) AND WITH SUBSTRATES","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF PHE-177 AND LEU-179"]}
```

Source SHA-256: `ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:27:30.074117+00:00.  

```text
DE   RecName: Full=Dihydropteroate synthase type-3 {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};
DE            Short=DHPS {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};
DE            EC=2.5.1.15 {ECO:0000255|RuleBase:RU361205, ECO:0000269|PubMed:37419898};
DE   AltName: Full=Dihydropteroate pyrophosphorylase type III {ECO:0000250|UniProtKB:P0C002};
DE   AltName: Full=Dihydropteroate synthase type III {ECO:0000250|UniProtKB:P0C002};
```

Source SHA-256: `471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)  
**Locator:** `lines 26-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:27:30.074117+00:00.  

```text
RN   [2] {ECO:0007744|PDB:7S2L, ECO:0007744|PDB:7S2M, ECO:0007744|PDB:8SCD}
RP   X-RAY CRYSTALLOGRAPHY (2.06 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH
RP   MG(2+) AND WITH SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, AND MUTAGENESIS OF PHE-177 AND LEU-179.
RX   PubMed=37419898; DOI=10.1038/s41467-023-39778-7;
RA   Venkatesan M., Fruci M., Verellen L.A., Skarina T., Mesa N., Flick R.,
RA   Pham C., Mahadevan R., Stogios P.J., Savchenko A.;
RT   "Molecular mechanism of plasmid-borne resistance to sulfonamide
RT   antibiotics.";
RL   Nat. Commun. 14:4031-4031(2023).
```

Source SHA-256: `471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)  
**Locator:** `lines 44-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:27:30.074117+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate =
CC         7,8-dihydropteroate + diphosphate; Xref=Rhea:RHEA:19949,
CC         ChEBI:CHEBI:17836, ChEBI:CHEBI:17839, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:72950; EC=2.5.1.15;
CC         Evidence={ECO:0000269|PubMed:37419898};
```

Source SHA-256: `471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 53. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
