# catalytic_activity_0065

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKKRCLITGGAGFIGSHLAEELVKRGHPVTIVDNFYKGKSKYHEELTGNIPIIPISILDKNSMHELVNQHDVVFHLAAILGVKTTMEKSIELIETNFDGTRNILQAALKGKKKVIFASTSEVYGKGTPPFSEDDDRLYGATSKIRWSYAICKTLEETLCLGYALQGLPVTIVRYFNIYGPRAKDGPYAGVIPRFIRAALQGDDLLVYGDGKQTRCFTYVSDAVEATIAAMDEKVNGEIINIGSEDEKSIQEVAQDIHQLTHSSSKIVHVPFEKVYPHGFEEIPNRKPDVTKLKEMCQFHPNVSWEQGLKETIQWFREIEND

[Multiple Choices]
A. UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2
B. ajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)
C. L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2
D. 4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O
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

> The supplied sequence exactly matches the UniProt entry annotated as UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase, and that entry gives choice A as its catalytic reaction with an experimental evidence code citing a 2010 paper. This supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct, specialized enzyme activities, but the input provides no organism, pathway context, enzyme name, or other clear indication of which activity applies. The sequence alone does not provide a sufficiently specific argument in the supplied information to distinguish the exact reaction.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental characterization identifying this sequence as a UDP-sugar decarboxylase.


**Reason**

> Selecting A depends on knowing the particular function associated with this sequence. Recognizing the sequence or retrieving its annotation would supply that missing fact; it is not established by a general biological argument available from the prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe different reactions, and the matched protein annotation supports A rather than an alternative.


### Important caveats

- The current and historical UniProt records match the supplied sequence, but the benchmark author's exact source snapshot is unknown.
- The supporting UniProt annotation cites experimental evidence, but the primary paper was not independently validated in the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct, specialized enzyme activities, but the input provides no organism, pathway context, enzyme name, or other clear indication of which activity applies. The sequence alone does not provide a sufficiently specific argument in the supplied information to distinguish the exact reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization identifying this sequence as a UDP-sugar decarboxylase.",
    "reason": "Selecting A depends on knowing the particular function associated with this sequence. Recognizing the sequence or retrieving its annotation would supply that missing fact; it is not established by a general biological argument available from the prompt."
  },
  "case_id": "catalytic_activity_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase, and that entry gives choice A as its catalytic reaction with an experimental evidence code citing a 2010 paper. This supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The current and historical UniProt records match the supplied sequence, but the benchmark author's exact source snapshot is unknown.",
    "The supporting UniProt annotation cites experimental evidence, but the primary paper was not independently validated in the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe different reactions, and the matched protein annotation supports A rather than an alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase, and that entry gives choice A as its catalytic reaction with an experimental evidence code citing a 2010 paper. This supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct, specialized enzyme activities, but the input provides no organism, pathway context, enzyme name, or other clear indication of which activity applies. The sequence alone does not provide a sufficiently specific argument in the supplied information to distinguish the exact reaction.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization identifying this sequence as a UDP-sugar decarboxylase.",
    "reason": "Selecting A depends on knowing the particular function associated with this sequence. Recognizing the sequence or retrieving its annotation would supply that missing fact; it is not established by a general biological argument available from the prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe different reactions, and the matched protein annotation supports A rather than an alternative."
  },
  "important_caveats": [
    "The current and historical UniProt records match the supplied sequence, but the benchmark author's exact source snapshot is unknown.",
    "The supporting UniProt annotation cites experimental evidence, but the primary paper was not independently validated in the supplied evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt entry A7GKX7 (UXNAS_BACCN), which is annotated with experimental evidence (ECO:0000269, PubMed:20529859) as UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase (EC 4.1.1.128). The catalytic activity reaction 'UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2' is explicitly stated in the entry and matches Choice A verbatim. The evidence is from a 2010 JBC paper with direct biochemical characterization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> There is a weak elimination-based argument: the sequence lacks canonical SAM-binding motifs (e.g., VLDVGAG) expected for methyltransferases (argues against B), lacks the HxD/E...H iron-coordinating motifs of 2-oxoglutarate-dependent dioxygenases (argues against C), and while it contains a YGDG NAD(P)-binding-like motif, it lacks the specific FMN-binding residues of nitroreductases (weakly argues against D). However, these are negative arguments only. No positive sequence signature uniquely identifies this as a UDP-sugar decarboxylase (EC 4.1.1.128), an extremely rare activity.


**Missing item-specific fact**

> The specific identity of this protein as a member of the UDP-sugar decarboxylase family (EC 4.1.1.128) and the knowledge that its Rossmann-like fold (GGAGFIGS, YGDG motifs) in this context supports UDP-sugar binding and C4 decarboxylation rather than oxidoreductase activity. This enzyme family is exceedingly rare and not identifiable by standard motif-based reasoning.


**Reason**

> The GGAGFIGS and YGDG motifs present in the sequence are classically associated with NAD(P)-dependent oxidoreductases, which could mislead a model toward choices C or D. The correct answer (A) requires recognizing this as a rare UDP-sugar decarboxylase, a function not inferable from these motifs alone. The question effectively requires prior knowledge of this specific enzyme or its family rather than sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the sequence motifs could superficially suggest oxidoreductase activity (C or D), the absence of definitive 2-oxoglutarate dioxygenase motifs (HxD/E, H) and FMN-binding residues makes those choices less defensible. Choice B lacks SAM-binding motifs. Choice A, though not positively identifiable from motifs, is the only remaining option and is confirmed by experimental annotation. No truly ambiguous alternative exists given careful motif analysis, but the path to A is indirect.


### Important caveats

- The GGAGFIGS and YGDG motifs in this sequence are potentially misleading: they resemble NAD(P)-binding Rossmann-fold elements typically associated with dehydrogenases/reductases, not decarboxylases. A model relying on motif-based heuristics might incorrectly select C or D.
- The UniProt entry references a COFACTOR (mentioned in reference RP line), which is not reflected in the simplified reaction equation in Choice A. This does not invalidate the answer but adds context not available to the evaluated model.
- EC 4.1.1.128 is an extremely rare enzyme class with very few characterized members, making it essentially impossible to identify from sequence without prior database lookup or memorization.
- The sequence-to-function mapping for this protein relies on the specific structural/biochemical characterization in PubMed:20529859 (Gu et al., 2010 JBC), not on generalizable sequence motifs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "There is a weak elimination-based argument: the sequence lacks canonical SAM-binding motifs (e.g., VLDVGAG) expected for methyltransferases (argues against B), lacks the HxD/E...H iron-coordinating motifs of 2-oxoglutarate-dependent dioxygenases (argues against C), and while it contains a YGDG NAD(P)-binding-like motif, it lacks the specific FMN-binding residues of nitroreductases (weakly argues against D). However, these are negative arguments only. No positive sequence signature uniquely identifies this as a UDP-sugar decarboxylase (EC 4.1.1.128), an extremely rare activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as a member of the UDP-sugar decarboxylase family (EC 4.1.1.128) and the knowledge that its Rossmann-like fold (GGAGFIGS, YGDG motifs) in this context supports UDP-sugar binding and C4 decarboxylation rather than oxidoreductase activity. This enzyme family is exceedingly rare and not identifiable by standard motif-based reasoning.",
    "reason": "The GGAGFIGS and YGDG motifs present in the sequence are classically associated with NAD(P)-dependent oxidoreductases, which could mislead a model toward choices C or D. The correct answer (A) requires recognizing this as a rare UDP-sugar decarboxylase, a function not inferable from these motifs alone. The question effectively requires prior knowledge of this specific enzyme or its family rather than sequence-based reasoning."
  },
  "case_id": "catalytic_activity_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A7GKX7 (UXNAS_BACCN), which is annotated with experimental evidence (ECO:0000269, PubMed:20529859) as UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase (EC 4.1.1.128). The catalytic activity reaction 'UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2' is explicitly stated in the entry and matches Choice A verbatim. The evidence is from a 2010 JBC paper with direct biochemical characterization."
  },
  "important_caveats": [
    "The GGAGFIGS and YGDG motifs in this sequence are potentially misleading: they resemble NAD(P)-binding Rossmann-fold elements typically associated with dehydrogenases/reductases, not decarboxylases. A model relying on motif-based heuristics might incorrectly select C or D.",
    "The UniProt entry references a COFACTOR (mentioned in reference RP line), which is not reflected in the simplified reaction equation in Choice A. This does not invalidate the answer but adds context not available to the evaluated model.",
    "EC 4.1.1.128 is an extremely rare enzyme class with very few characterized members, making it essentially impossible to identify from sequence without prior database lookup or memorization.",
    "The sequence-to-function mapping for this protein relies on the specific structural/biochemical characterization in PubMed:20529859 (Gu et al., 2010 JBC), not on generalizable sequence motifs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the sequence motifs could superficially suggest oxidoreductase activity (C or D), the absence of definitive 2-oxoglutarate dioxygenase motifs (HxD/E, H) and FMN-binding residues makes those choices less defensible. Choice B lacks SAM-binding motifs. Choice A, though not positively identifiable from motifs, is the only remaining option and is confirmed by experimental annotation. No truly ambiguous alternative exists given careful motif analysis, but the path to A is indirect."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A7GKX7 (UXNAS_BACCN), which is annotated with experimental evidence (ECO:0000269, PubMed:20529859) as UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase (EC 4.1.1.128). The catalytic activity reaction 'UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2' is explicitly stated in the entry and matches Choice A verbatim. The evidence is from a 2010 JBC paper with direct biochemical characterization.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "There is a weak elimination-based argument: the sequence lacks canonical SAM-binding motifs (e.g., VLDVGAG) expected for methyltransferases (argues against B), lacks the HxD/E...H iron-coordinating motifs of 2-oxoglutarate-dependent dioxygenases (argues against C), and while it contains a YGDG NAD(P)-binding-like motif, it lacks the specific FMN-binding residues of nitroreductases (weakly argues against D). However, these are negative arguments only. No positive sequence signature uniquely identifies this as a UDP-sugar decarboxylase (EC 4.1.1.128), an extremely rare activity.",
    "missing_item_specific_fact": "The specific identity of this protein as a member of the UDP-sugar decarboxylase family (EC 4.1.1.128) and the knowledge that its Rossmann-like fold (GGAGFIGS, YGDG motifs) in this context supports UDP-sugar binding and C4 decarboxylation rather than oxidoreductase activity. This enzyme family is exceedingly rare and not identifiable by standard motif-based reasoning.",
    "reason": "The GGAGFIGS and YGDG motifs present in the sequence are classically associated with NAD(P)-dependent oxidoreductases, which could mislead a model toward choices C or D. The correct answer (A) requires recognizing this as a rare UDP-sugar decarboxylase, a function not inferable from these motifs alone. The question effectively requires prior knowledge of this specific enzyme or its family rather than sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the sequence motifs could superficially suggest oxidoreductase activity (C or D), the absence of definitive 2-oxoglutarate dioxygenase motifs (HxD/E, H) and FMN-binding residues makes those choices less defensible. Choice B lacks SAM-binding motifs. Choice A, though not positively identifiable from motifs, is the only remaining option and is confirmed by experimental annotation. No truly ambiguous alternative exists given careful motif analysis, but the path to A is indirect."
  },
  "important_caveats": [
    "The GGAGFIGS and YGDG motifs in this sequence are potentially misleading: they resemble NAD(P)-binding Rossmann-fold elements typically associated with dehydrogenases/reductases, not decarboxylases. A model relying on motif-based heuristics might incorrectly select C or D.",
    "The UniProt entry references a COFACTOR (mentioned in reference RP line), which is not reflected in the simplified reaction equation in Choice A. This does not invalidate the answer but adds context not available to the evaluated model.",
    "EC 4.1.1.128 is an extremely rare enzyme class with very few characterized members, making it essentially impossible to identify from sequence without prior database lookup or memorization.",
    "The sequence-to-function mapping for this protein relies on the specific structural/biochemical characterization in PubMed:20529859 (Gu et al., 2010 JBC), not on generalizable sequence motifs."
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

**Accession:** `A7GKX7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 94. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.082856+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-XylNAc synthase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"value":"4.1.1.128"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-GlcNAcA decarboxylase"}]}}
```

Source SHA-256: `e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.082856+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81488"}}],"reaction":{"ecNumber":"4.1.1.128","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"name":"UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81487"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:65040"},{"database":"ChEBI","id":"CHEBI:231888"}]}}
```

Source SHA-256: `e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.082856+00:00.  

```json
{"citation":{"authors":["Gu X.","Glushka J.","Lee S.G.","Bar-Peled M."],"citationCrossReferences":[{"database":"PubMed","id":"20529859"},{"database":"DOI","id":"10.1074/jbc.m110.125872"}],"citationType":"journal article","firstPage":"24825","id":"20529859","journal":"J. Biol. Chem.","lastPage":"24833","publicationDate":"2010","title":"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.","volume":"285"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ADE43880.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT"]}
```

Source SHA-256: `e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 94 / 1.  
**Retrieved:** 2026-11-01T06:27:51.337169+00:00.  

```text
ID   UXNAS_BACCN             Reviewed;         321 AA.
AC   A7GKX7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   11-SEP-2007, sequence version 1.
DT   28-JAN-2026, entry version 94.
DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase {ECO:0000305};
DE            Short=UDP-GlcNAcA decarboxylase {ECO:0000303|PubMed:20529859};
DE            EC=4.1.1.128 {ECO:0000269|PubMed:20529859};
DE   AltName: Full=UDP-XylNAc synthase {ECO:0000303|PubMed:20529859};
GN   Name=UXNAcS {ECO:0000303|PubMed:20529859};
GN   OrderedLocusNames=Bcer98_0430 {ECO:0000312|EMBL:ABS20785.1};
OS   Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98).
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus;
OC   Bacillus cereus group.
OX   NCBI_TaxID=315749;
```

Source SHA-256: `3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 94 / 1.  
**Retrieved:** 2026-11-01T06:27:51.337169+00:00.  

```text
DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase {ECO:0000305};
DE            Short=UDP-GlcNAcA decarboxylase {ECO:0000303|PubMed:20529859};
DE            EC=4.1.1.128 {ECO:0000269|PubMed:20529859};
DE   AltName: Full=UDP-XylNAc synthase {ECO:0000303|PubMed:20529859};
```

Source SHA-256: `3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)  
**Locator:** `lines 27-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 94 / 1.  
**Retrieved:** 2026-11-01T06:27:51.337169+00:00.  

```text
RN   [2] {ECO:0000312|EMBL:ADE43880.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
RP   ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.
RC   STRAIN=DSM 22905 / CIP 110041 / 391-98 / NVH 391-98;
RX   PubMed=20529859; DOI=10.1074/jbc.m110.125872;
RA   Gu X., Glushka J., Lee S.G., Bar-Peled M.;
RT   "Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the
RT   human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.";
RL   J. Biol. Chem. 285:24825-24833(2010).
```

Source SHA-256: `3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 94 / 1.  
**Retrieved:** 2026-11-01T06:27:51.337169+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-
CC         acetyl-alpha-D-xylosamine + CO2; Xref=Rhea:RHEA:81487,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:65040,
CC         ChEBI:CHEBI:231888; EC=4.1.1.128;
CC         Evidence={ECO:0000269|PubMed:20529859};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81488;
CC         Evidence={ECO:0000269|PubMed:20529859};
```

Source SHA-256: `3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 65. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
