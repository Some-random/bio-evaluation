# catalytic_activity_0183

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — beta-amyrin + 3 reduced &#91;NADPH--hemoprotein reductase&#93; + 3 O2 = oleanolate + 3 oxidized &#91;NADPH--hemoprotein reductase&#93; + 4 H2O + 4 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELFFICGLVLFSTLSLISLFLLHNHSSARGYRLPPGRMGWPFIGESYEFLANGWKGYPEKFIFSRLAKYKPNQVFKTSILGEKVAVMCGATCNKFLFSNEGKLVNAWWPNSVNKIFPSSTQTSSKEEAKKMRKLLPTFFKPEALQRYIPIMDEIAIRHMEDEWEGKSKIEVFPLAKRYTFWLACRLFLSIDDPVHVAKFADPFNDIASGIISIPIDLPGTPFNRGIKASNVVRQELKTIIKQRKLDLSDNKASPTQDILSHMLLTPDEDGRYMNELDIADKILGLLIGGHDTASAACTFVVKFLAELPHIYDGVYKEQMEIAKSKKEGERLNWEDIQKMKYSWNVACEVMRLAPPLQGAFREALSDFMYAGFQIPKGWKLYWSANSTHRNPECFPEPEKFDPARFDGSGPAPYTYVPFGGGPRMCPGKEYARLEILVFMHNIVKRFKWEKLIPDETIVVNPMPTPAKGLPVRLRPHSKPVTVSA

[Multiple Choices]
A. beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)
B. a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
C. L-proline betaine + NADH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NAD(+) + H2O
D. a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)
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

> The exact sequence matches a UniProt entry annotating this enzyme as beta-amyrin 28-monooxygenase and assigning the reaction in choice A. The catalytic-activity annotation is linked to a publication with experimental-evidence code ECO:0000269; the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a cytochrome P450, which supports oxidative chemistry, but that broad inference does not establish its particular substrate or product. In particular, it does not distinguish choice A from the other P450-type oxidation in choice B.


**Missing item-specific fact**

> The protein-specific finding that this sequence is CYP716A378 from soapwort and catalyzes beta-amyrin oxidation to oleanolate.


**Reason**

> Identifying the specific reaction requires substrate-specific functional annotation or experimental knowledge not supplied in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reaction options describe distinct transformations, and the sequence-matched annotation supports A. The question lacks input that enables the model to infer this enzyme's specific substrate activity, but that is a lookup dependence rather than multiple equally supported answers.


### Important caveats

- The source identity, exact sequence match, and catalytic-activity annotation come from reviewer-only evidence and were not provided to the evaluated model.
- The annotation cites experimental evidence, but the cited study was not independently examined; the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a cytochrome P450, which supports oxidative chemistry, but that broad inference does not establish its particular substrate or product. In particular, it does not distinguish choice A from the other P450-type oxidation in choice B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that this sequence is CYP716A378 from soapwort and catalyzes beta-amyrin oxidation to oleanolate.",
    "reason": "Identifying the specific reaction requires substrate-specific functional annotation or experimental knowledge not supplied in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "catalytic_activity_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating this enzyme as beta-amyrin 28-monooxygenase and assigning the reaction in choice A. The catalytic-activity annotation is linked to a publication with experimental-evidence code ECO:0000269; the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The source identity, exact sequence match, and catalytic-activity annotation come from reviewer-only evidence and were not provided to the evaluated model.",
    "The annotation cites experimental evidence, but the cited study was not independently examined; the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction options describe distinct transformations, and the sequence-matched annotation supports A. The question lacks input that enables the model to infer this enzyme's specific substrate activity, but that is a lookup dependence rather than multiple equally supported answers."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating this enzyme as beta-amyrin 28-monooxygenase and assigning the reaction in choice A. The catalytic-activity annotation is linked to a publication with experimental-evidence code ECO:0000269; the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a cytochrome P450, which supports oxidative chemistry, but that broad inference does not establish its particular substrate or product. In particular, it does not distinguish choice A from the other P450-type oxidation in choice B.",
    "missing_item_specific_fact": "The protein-specific finding that this sequence is CYP716A378 from soapwort and catalyzes beta-amyrin oxidation to oleanolate.",
    "reason": "Identifying the specific reaction requires substrate-specific functional annotation or experimental knowledge not supplied in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction options describe distinct transformations, and the sequence-matched annotation supports A. The question lacks input that enables the model to infer this enzyme's specific substrate activity, but that is a lookup dependence rather than multiple equally supported answers."
  },
  "important_caveats": [
    "The source identity, exact sequence match, and catalytic-activity annotation come from reviewer-only evidence and were not provided to the evaluated model.",
    "The annotation cites experimental evidence, but the cited study was not independently examined; the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1NEA3 (sequence matched, 485 AA, Saponaria officinalis) is annotated as 'Beta-amyrin 28-monooxygenase CYP716A378' (EC 1.14.14.126) with the catalytic reaction text exactly matching Choice A. The annotation carries evidence code ECO:0000269 (experimental) from PubMed:39043959 (Jo et al., Nat. Chem. Biol. 2025), indicating direct experimental characterization of the reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable P450 heme-binding motif (FGGGPRMCPGK region with the conserved cysteine ligand), an N-terminal signal peptide indicating ER localization, and overall architecture consistent with a plant microsomal P450. This allows elimination of Choice D (phospholipase hydrolysis, no P450 involvement) and Choice C (amine oxidase-type reaction using NADH, not NADPH-hemoprotein reductase). However, the critical distinction between Choice A (triterpenoid beta-amyrin → oleanolate) and Choice B (steroid 14α-hydroxymethyl → 14α-formyl) both involve identical cofactor chemistry (NADPH-hemoprotein reductase + O2) and cannot be resolved from sequence features alone.


**Missing item-specific fact**

> Identification of the specific CYP family (CYP716, associated with triterpenoid oxidation) versus other plant P450 families (e.g., CYP72/CYP88, associated with steroid oxidation) requires either exact sequence-to-database matching or memorization of CYP family-substrate specificity assignments. No general sequence motif distinguishes triterpenoid-oxidizing from steroid-oxidizing P450s.


**Reason**

> While P450 identity can be inferred from the heme-binding motif and cofactor requirements eliminate C and D, the A-vs-B distinction (triterpenoid vs steroid substrate) depends on knowing the CYP family assignment, which is an item-specific database fact not derivable from general biological reasoning applied to the raw sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A and B describe NADPH-hemoprotein reductase-dependent P450 oxidations of plant natural products. Without CYP family identification, a knowledgeable model could reasonably assign either a triterpenoid or steroid substrate to an unidentified plant P450. Choices C and D are clearly eliminable (wrong cofactor system and wrong enzyme class respectively).


### Important caveats

- The UniProt annotation is based on experimental evidence (ECO:0000269, PubMed:39043959), making the key scientifically well-supported.
- The sequence-to-entry match is confirmed at both current (v6) and historical (v5, released 2026-01-28) snapshots.
- The entry was first publicly released 2025-06-18; the author's source snapshot date is unknown but the sequence has been stable since 2024-11-27.
- The CYP716 family association with triterpenoid metabolism is well-established in plant biology literature, but this knowledge is essentially a database/family-level fact rather than a sequence-derivable property.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable P450 heme-binding motif (FGGGPRMCPGK region with the conserved cysteine ligand), an N-terminal signal peptide indicating ER localization, and overall architecture consistent with a plant microsomal P450. This allows elimination of Choice D (phospholipase hydrolysis, no P450 involvement) and Choice C (amine oxidase-type reaction using NADH, not NADPH-hemoprotein reductase). However, the critical distinction between Choice A (triterpenoid beta-amyrin → oleanolate) and Choice B (steroid 14α-hydroxymethyl → 14α-formyl) both involve identical cofactor chemistry (NADPH-hemoprotein reductase + O2) and cannot be resolved from sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identification of the specific CYP family (CYP716, associated with triterpenoid oxidation) versus other plant P450 families (e.g., CYP72/CYP88, associated with steroid oxidation) requires either exact sequence-to-database matching or memorization of CYP family-substrate specificity assignments. No general sequence motif distinguishes triterpenoid-oxidizing from steroid-oxidizing P450s.",
    "reason": "While P450 identity can be inferred from the heme-binding motif and cofactor requirements eliminate C and D, the A-vs-B distinction (triterpenoid vs steroid substrate) depends on knowing the CYP family assignment, which is an item-specific database fact not derivable from general biological reasoning applied to the raw sequence."
  },
  "case_id": "catalytic_activity_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1NEA3 (sequence matched, 485 AA, Saponaria officinalis) is annotated as 'Beta-amyrin 28-monooxygenase CYP716A378' (EC 1.14.14.126) with the catalytic reaction text exactly matching Choice A. The annotation carries evidence code ECO:0000269 (experimental) from PubMed:39043959 (Jo et al., Nat. Chem. Biol. 2025), indicating direct experimental characterization of the reaction."
  },
  "important_caveats": [
    "The UniProt annotation is based on experimental evidence (ECO:0000269, PubMed:39043959), making the key scientifically well-supported.",
    "The sequence-to-entry match is confirmed at both current (v6) and historical (v5, released 2026-01-28) snapshots.",
    "The entry was first publicly released 2025-06-18; the author's source snapshot date is unknown but the sequence has been stable since 2024-11-27.",
    "The CYP716 family association with triterpenoid metabolism is well-established in plant biology literature, but this knowledge is essentially a database/family-level fact rather than a sequence-derivable property."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A and B describe NADPH-hemoprotein reductase-dependent P450 oxidations of plant natural products. Without CYP family identification, a knowledgeable model could reasonably assign either a triterpenoid or steroid substrate to an unidentified plant P450. Choices C and D are clearly eliminable (wrong cofactor system and wrong enzyme class respectively)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1NEA3 (sequence matched, 485 AA, Saponaria officinalis) is annotated as 'Beta-amyrin 28-monooxygenase CYP716A378' (EC 1.14.14.126) with the catalytic reaction text exactly matching Choice A. The annotation carries evidence code ECO:0000269 (experimental) from PubMed:39043959 (Jo et al., Nat. Chem. Biol. 2025), indicating direct experimental characterization of the reaction.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable P450 heme-binding motif (FGGGPRMCPGK region with the conserved cysteine ligand), an N-terminal signal peptide indicating ER localization, and overall architecture consistent with a plant microsomal P450. This allows elimination of Choice D (phospholipase hydrolysis, no P450 involvement) and Choice C (amine oxidase-type reaction using NADH, not NADPH-hemoprotein reductase). However, the critical distinction between Choice A (triterpenoid beta-amyrin → oleanolate) and Choice B (steroid 14α-hydroxymethyl → 14α-formyl) both involve identical cofactor chemistry (NADPH-hemoprotein reductase + O2) and cannot be resolved from sequence features alone.",
    "missing_item_specific_fact": "Identification of the specific CYP family (CYP716, associated with triterpenoid oxidation) versus other plant P450 families (e.g., CYP72/CYP88, associated with steroid oxidation) requires either exact sequence-to-database matching or memorization of CYP family-substrate specificity assignments. No general sequence motif distinguishes triterpenoid-oxidizing from steroid-oxidizing P450s.",
    "reason": "While P450 identity can be inferred from the heme-binding motif and cofactor requirements eliminate C and D, the A-vs-B distinction (triterpenoid vs steroid substrate) depends on knowing the CYP family assignment, which is an item-specific database fact not derivable from general biological reasoning applied to the raw sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A and B describe NADPH-hemoprotein reductase-dependent P450 oxidations of plant natural products. Without CYP family identification, a knowledgeable model could reasonably assign either a triterpenoid or steroid substrate to an unidentified plant P450. Choices C and D are clearly eliminable (wrong cofactor system and wrong enzyme class respectively)."
  },
  "important_caveats": [
    "The UniProt annotation is based on experimental evidence (ECO:0000269, PubMed:39043959), making the key scientifically well-supported.",
    "The sequence-to-entry match is confirmed at both current (v6) and historical (v5, released 2026-01-28) snapshots.",
    "The entry was first publicly released 2025-06-18; the author's source snapshot date is unknown but the sequence has been stable since 2024-11-27.",
    "The CYP716 family association with triterpenoid metabolism is well-established in plant biology literature, but this knowledge is essentially a database/family-level fact rather than a sequence-derivable property."
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

**Accession:** `A0AAW1NEA3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
"A0AAW1NEA3"
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"Cytochrome P450 716A378"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoCYP716A378"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"1.14.14.126"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Beta-amyrin 28-monooxygenase CYP716A378"}}}
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:43069"}}],"reaction":{"ecNumber":"1.14.14.126","evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"name":"beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:43068"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:10352"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:82828"}]}}
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48148.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.561544+00:00.  

```text
DE   RecName: Full=Beta-amyrin 28-monooxygenase CYP716A378 {ECO:0000305};
DE            EC=1.14.14.126 {ECO:0000269|PubMed:39043959};
DE   AltName: Full=Cytochrome P450 716A378 {ECO:0000303|PubMed:39043959};
DE            Short=SoCYP716A378 {ECO:0000303|PubMed:39043959};
```

Source SHA-256: `8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)  
**Locator:** `lines 18-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.561544+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:WWM48148.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE
RP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.
RX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;
RA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,
RA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,
RA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,
RA   Leebens-Mack J., Osbourn A.;
RT   "Unlocking saponin biosynthesis in soapwort.";
RL   Nat. Chem. Biol. 21:215-226(2025).
```

Source SHA-256: `8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)  
**Locator:** `lines 42-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.561544+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2
CC         = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4
CC         H(+); Xref=Rhea:RHEA:43068, Rhea:RHEA-COMP:11964, Rhea:RHEA-
CC         COMP:11965, ChEBI:CHEBI:10352, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,
CC         ChEBI:CHEBI:82828; EC=1.14.14.126;
CC         Evidence={ECO:0000269|PubMed:39043959};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:43069;
CC         Evidence={ECO:0000269|PubMed:39043959};
```

Source SHA-256: `8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 183. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
