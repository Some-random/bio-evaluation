# catalytic_activity_0088

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQPEFTRSIVGASFLLPVINGAMHIPPAVSATRVTLEDNQPRDAPILVLLFALSVLIDVMDKAADLPRQTRKTWLMTIVVFASPFVVLAVYGTMHCGLLALLRLLGVPLLAVVHAMPLIPVYSWKTGSISTVKLKYFLGPFKSLFGATCIGLMDVTAVVLYLRGTMLHPENASSAGHFRVLMYTITYDFLWESICDVRDIQEDEQNNITTLATAFGVRPTLIFLGGSTMMGDLSITLLGGGSAVLSVVRSTVFWGAFAALALHKPRSAVYPWGLATLFGLLPVWLASLGART

[Multiple Choices]
A. 2 5'-deoxyadenosin-5'-yl radical + 2 dAMP + A = 2 4'-phospho-dehydrooxetanocin + 2 5'-deoxyadenosine + AH2
B. (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate
C. peramine + 2-oxoglutarate + O2 = 8-hydroxyperamine + succinate + CO2
D. a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
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

> The exact supplied sequence matches the UniProt record, which annotates this protein's catalytic activity as the reaction in choice B and links the assertion to experimental evidence from PubMed 39310987. The historical record available by the stated cutoff also contains this annotation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is highly hydrophobic, and it does not show obvious hallmark motifs for the radical-SAM, 2-oxoglutarate-dependent oxygenase, or cytochrome-P450 alternatives. That may help eliminate distractors, but does not establish the specific prenylation reaction or its substrates and product.


**Missing item-specific fact**

> The protein-specific finding that this enzyme catalyzes the reaction of (S,S)-drim-8-en-11-yl diphosphate with D-mannitol to form sporulositol A; this requires an annotation or experimental result not provided in the question.


**Reason**

> Broad sequence features do not identify this exact catalytic transformation. Choosing B depends on the protein-specific functional annotation or experimental evidence, rather than a sufficiently discriminating argument from the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports B, and the supplied evidence does not support another listed reaction. The limitation is dependence on external protein-specific knowledge, not a demonstrated ambiguity among options.


### Important caveats

- The UniProt annotation is linked to experimental evidence, but the primary paper was not independently retrieved or validated here.
- The reviewer-only accession and annotation were not supplied to the evaluated model; the source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is highly hydrophobic, and it does not show obvious hallmark motifs for the radical-SAM, 2-oxoglutarate-dependent oxygenase, or cytochrome-P450 alternatives. That may help eliminate distractors, but does not establish the specific prenylation reaction or its substrates and product.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that this enzyme catalyzes the reaction of (S,S)-drim-8-en-11-yl diphosphate with D-mannitol to form sporulositol A; this requires an annotation or experimental result not provided in the question.",
    "reason": "Broad sequence features do not identify this exact catalytic transformation. Choosing B depends on the protein-specific functional annotation or experimental evidence, rather than a sufficiently discriminating argument from the supplied sequence."
  },
  "case_id": "catalytic_activity_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt record, which annotates this protein's catalytic activity as the reaction in choice B and links the assertion to experimental evidence from PubMed 39310987. The historical record available by the stated cutoff also contains this annotation."
  },
  "important_caveats": [
    "The UniProt annotation is linked to experimental evidence, but the primary paper was not independently retrieved or validated here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model; the source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports B, and the supplied evidence does not support another listed reaction. The limitation is dependence on external protein-specific knowledge, not a demonstrated ambiguity among options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt record, which annotates this protein's catalytic activity as the reaction in choice B and links the assertion to experimental evidence from PubMed 39310987. The historical record available by the stated cutoff also contains this annotation.",
    "evidence_ids": ["C1", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is highly hydrophobic, and it does not show obvious hallmark motifs for the radical-SAM, 2-oxoglutarate-dependent oxygenase, or cytochrome-P450 alternatives. That may help eliminate distractors, but does not establish the specific prenylation reaction or its substrates and product.",
    "missing_item_specific_fact": "The protein-specific finding that this enzyme catalyzes the reaction of (S,S)-drim-8-en-11-yl diphosphate with D-mannitol to form sporulositol A; this requires an annotation or experimental result not provided in the question.",
    "reason": "Broad sequence features do not identify this exact catalytic transformation. Choosing B depends on the protein-specific functional annotation or experimental evidence, rather than a sufficiently discriminating argument from the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports B, and the supplied evidence does not support another listed reaction. The limitation is dependence on external protein-specific knowledge, not a demonstrated ambiguity among options."
  },
  "important_caveats": [
    "The UniProt annotation is linked to experimental evidence, but the primary paper was not independently retrieved or validated here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model; the source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (293 aa, SHA256 matched) corresponds to UniProt A0A6A6H402, annotated as 'Prenyltransferase vviA' (EC 2.5.1.-) from Viridothelium virens. The catalytic activity is explicitly annotated as '(S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate' (Rhea:RHEA:82587) with experimental evidence (ECO:0000269, PubMed:39310987, Org. Lett. 2024). The sequence is identical in both current (v13) and historical (v12) entries.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a membrane-associated protein with multiple hydrophobic TM helices and aspartate-rich regions (e.g., 'GDLS' near residue 189, consistent with the mutagenesis data citing ASP-189/TRP-192), features characteristic of membrane-bound prenyltransferases (EC 2.5.1.-). Critically, the sequence lacks the diagnostic CX3CX2C motif of radical SAM enzymes (eliminating A), the HxD...H 2-oxoglutarate dioxygenase motif (eliminating C), and the FxxGxxxCxG heme-binding motif of cytochrome P450s (eliminating D). Among the four choices, only B describes a prenyltransferase reaction, making it the sole option compatible with the identified enzyme class.


**Missing item-specific fact**

> The specific substrates (drim-8-en-11-yl diphosphate, D-mannitol) and product (sporulositol A) cannot be predicted from sequence alone; however, since only one of the four choices is a prenyltransferase reaction, class-level identification suffices to select B.


**Reason**

> The model can distinguish the answer through general biological knowledge: recognizing membrane-bound prenyltransferase topology, identifying aspartate-rich catalytic motifs, and eliminating options A, C, D by absence of their diagnostic cofactor-binding motifs. The specific natural-product substrates are not predictable from sequence, but the question format (only one prenyltransferase reaction among four choices) makes class identification sufficient.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A, C, and D require specific cofactor-binding motifs (radical SAM &#91;4Fe-4S&#93;, 2OG dioxygenase Fe/2OG, P450 heme) that are absent from this sequence. Only B is consistent with a membrane-bound prenyltransferase, leaving no ambiguity among the provided options.


### Important caveats

- The specific substrates (drim-8-en-11-yl diphosphate + D-mannitol) and product (sporulositol A) represent an obscure fungal natural-product pathway; a model could identify the enzyme class but not the exact reaction from sequence alone.
- The annotation evidence is experimental (ECO:0000269) from a 2024 Org. Lett. paper, not computational prediction.
- The sequence has been in UniProt since 2020 (sequence version 1) but the functional annotation was only added in April 2025, so the specific reaction was not publicly annotated at the time the sequence was first deposited.
- The reasoning argument relies on motif absence (negative evidence) for eliminating A, C, D; this is valid but less definitive than positive motif identification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a membrane-associated protein with multiple hydrophobic TM helices and aspartate-rich regions (e.g., 'GDLS' near residue 189, consistent with the mutagenesis data citing ASP-189/TRP-192), features characteristic of membrane-bound prenyltransferases (EC 2.5.1.-). Critically, the sequence lacks the diagnostic CX3CX2C motif of radical SAM enzymes (eliminating A), the HxD...H 2-oxoglutarate dioxygenase motif (eliminating C), and the FxxGxxxCxG heme-binding motif of cytochrome P450s (eliminating D). Among the four choices, only B describes a prenyltransferase reaction, making it the sole option compatible with the identified enzyme class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrates (drim-8-en-11-yl diphosphate, D-mannitol) and product (sporulositol A) cannot be predicted from sequence alone; however, since only one of the four choices is a prenyltransferase reaction, class-level identification suffices to select B.",
    "reason": "The model can distinguish the answer through general biological knowledge: recognizing membrane-bound prenyltransferase topology, identifying aspartate-rich catalytic motifs, and eliminating options A, C, D by absence of their diagnostic cofactor-binding motifs. The specific natural-product substrates are not predictable from sequence, but the question format (only one prenyltransferase reaction among four choices) makes class identification sufficient."
  },
  "case_id": "catalytic_activity_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence (293 aa, SHA256 matched) corresponds to UniProt A0A6A6H402, annotated as 'Prenyltransferase vviA' (EC 2.5.1.-) from Viridothelium virens. The catalytic activity is explicitly annotated as '(S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate' (Rhea:RHEA:82587) with experimental evidence (ECO:0000269, PubMed:39310987, Org. Lett. 2024). The sequence is identical in both current (v13) and historical (v12) entries."
  },
  "important_caveats": [
    "The specific substrates (drim-8-en-11-yl diphosphate + D-mannitol) and product (sporulositol A) represent an obscure fungal natural-product pathway; a model could identify the enzyme class but not the exact reaction from sequence alone.",
    "The annotation evidence is experimental (ECO:0000269) from a 2024 Org. Lett. paper, not computational prediction.",
    "The sequence has been in UniProt since 2020 (sequence version 1) but the functional annotation was only added in April 2025, so the specific reaction was not publicly annotated at the time the sequence was first deposited.",
    "The reasoning argument relies on motif absence (negative evidence) for eliminating A, C, D; this is valid but less definitive than positive motif identification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D require specific cofactor-binding motifs (radical SAM [4Fe-4S], 2OG dioxygenase Fe/2OG, P450 heme) that are absent from this sequence. Only B is consistent with a membrane-bound prenyltransferase, leaving no ambiguity among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (293 aa, SHA256 matched) corresponds to UniProt A0A6A6H402, annotated as 'Prenyltransferase vviA' (EC 2.5.1.-) from Viridothelium virens. The catalytic activity is explicitly annotated as '(S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate' (Rhea:RHEA:82587) with experimental evidence (ECO:0000269, PubMed:39310987, Org. Lett. 2024). The sequence is identical in both current (v13) and historical (v12) entries.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence encodes a membrane-associated protein with multiple hydrophobic TM helices and aspartate-rich regions (e.g., 'GDLS' near residue 189, consistent with the mutagenesis data citing ASP-189/TRP-192), features characteristic of membrane-bound prenyltransferases (EC 2.5.1.-). Critically, the sequence lacks the diagnostic CX3CX2C motif of radical SAM enzymes (eliminating A), the HxD...H 2-oxoglutarate dioxygenase motif (eliminating C), and the FxxGxxxCxG heme-binding motif of cytochrome P450s (eliminating D). Among the four choices, only B describes a prenyltransferase reaction, making it the sole option compatible with the identified enzyme class.",
    "missing_item_specific_fact": "The specific substrates (drim-8-en-11-yl diphosphate, D-mannitol) and product (sporulositol A) cannot be predicted from sequence alone; however, since only one of the four choices is a prenyltransferase reaction, class-level identification suffices to select B.",
    "reason": "The model can distinguish the answer through general biological knowledge: recognizing membrane-bound prenyltransferase topology, identifying aspartate-rich catalytic motifs, and eliminating options A, C, D by absence of their diagnostic cofactor-binding motifs. The specific natural-product substrates are not predictable from sequence, but the question format (only one prenyltransferase reaction among four choices) makes class identification sufficient."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D require specific cofactor-binding motifs (radical SAM [4Fe-4S], 2OG dioxygenase Fe/2OG, P450 heme) that are absent from this sequence. Only B is consistent with a membrane-bound prenyltransferase, leaving no ambiguity among the provided options."
  },
  "important_caveats": [
    "The specific substrates (drim-8-en-11-yl diphosphate + D-mannitol) and product (sporulositol A) represent an obscure fungal natural-product pathway; a model could identify the enzyme class but not the exact reaction from sequence alone.",
    "The annotation evidence is experimental (ECO:0000269) from a 2024 Org. Lett. paper, not computational prediction.",
    "The sequence has been in UniProt since 2020 (sequence version 1) but the functional annotation was only added in April 2025, so the specific reaction was not publicly annotated at the time the sequence was first deposited.",
    "The reasoning argument relies on motif absence (negative evidence) for eliminating A, C, D; this is valid but less definitive than positive motif identification."
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

**Accession:** `A0A6A6H402` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
"A0A6A6H402"
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39310987","source":"PubMed"}],"value":"Sporulositol A biosynthesis cluster protein A"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39310987","source":"PubMed"}],"value":"2.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39310987","source":"PubMed"}],"value":"Prenyltransferase vviA"}}}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39310987","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:82588"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39310987","source":"PubMed"}],"name":"(S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:82587"},{"database":"ChEBI","id":"CHEBI:16899"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:206556"},{"database":"ChEBI","id":"CHEBI:231796"}]}}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"citation":{"authors":["Tang Y.J.","Zou Y."],"citationCrossReferences":[{"database":"PubMed","id":"39310987"},{"database":"DOI","id":"10.1021/acs.orglett.4c03154"}],"citationType":"journal article","firstPage":"8366","id":"39310987","journal":"Org. Lett.","lastPage":"8370","publicationDate":"2024","title":"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.","volume":"26"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","PATHWAY","MUTAGENESIS OF LEU-17; ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND THR-277"]}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
ID   VVIA_VIRVR              Reviewed;         293 AA.
AC   A0A6A6H402;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   17-JUN-2020, sequence version 1.
DT   28-JAN-2026, entry version 12.
DE   RecName: Full=Prenyltransferase vviA {ECO:0000303|PubMed:39310987};
DE            EC=2.5.1.- {ECO:0000269|PubMed:39310987};
DE   AltName: Full=Sporulositol A biosynthesis cluster protein A {ECO:0000303|PubMed:39310987};
GN   Name=vviA {ECO:0000303|PubMed:39310987}; ORFNames=EV356DRAFT_253807;
OS   Viridothelium virens (Speckled blister lichen) (Trypethelium virens).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetes incertae sedis; Trypetheliales; Trypetheliaceae;
OC   Viridothelium.
OX   NCBI_TaxID=1048519;
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
DE   RecName: Full=Prenyltransferase vviA {ECO:0000303|PubMed:39310987};
DE            EC=2.5.1.- {ECO:0000269|PubMed:39310987};
DE   AltName: Full=Sporulositol A biosynthesis cluster protein A {ECO:0000303|PubMed:39310987};
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 48-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol
CC         A + diphosphate; Xref=Rhea:RHEA:82587, ChEBI:CHEBI:16899,
CC         ChEBI:CHEBI:33019, ChEBI:CHEBI:206556, ChEBI:CHEBI:231796;
CC         Evidence={ECO:0000269|PubMed:39310987};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82588;
CC         Evidence={ECO:0000269|PubMed:39310987};
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 88. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
