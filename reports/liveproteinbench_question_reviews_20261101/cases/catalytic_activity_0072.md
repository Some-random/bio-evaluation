# catalytic_activity_0072

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSVSPQSTMARIPERRVRTLDFAQFRHGEPSGSRGFCRELVDCLSSVGFVKIRNHGISGQEIENVFVMSQLFFSLPQAAKGKAAHPPEANPHRGYSYVGQEKLSRVKDYEKGKREITDVYDIKHYPIDRDARQESYDQGAAVDNLYPNRWPDEQDIPGFRVLMETFYERCHEVHQDILRAIAIGFDLSPSFLTDLCCQNTSELRLNHYPSVHPSSLRKGAKRISEHTDFGTVTLLFQDSVGGLEIEDQNTPGTYFPVLSERKSDIIVNIGDCIQRWTNDKIHSTSHRVVLPEDTDALTKDRYSVAYFGKPSRSQLVGSLREFVKEGEKPKYNDISAWQYNQEKLVLTY

[Multiple Choices]
A. dopamine + S-adenosyl-L-methionine = N-methyl-dopamine + S-adenosyl-L-homocysteine + H(+)
B. L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2
C. beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)
D. 2 3-amino-1,5-dihydropyridine-2,6-dione + O2 = indigoidine + 2 H2O
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

> The sequence-matched UniProt annotation assigns this protein the L-proline 2-oxoglutarate/O2 hydroxylation reaction in choice B and cites experimental evidence (ECO:0000269).

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an Fe(II)/2-oxoglutarate oxygenase, including histidine/aspartate-containing candidate metal-binding motifs. Of the choices, B alone is a 2-oxoglutarate- and O2-dependent hydroxylation reaction; the others describe methyl transfer, nucleotide adenylation, or indigoidine formation.


**Missing item-specific fact**

> The exact substrate and hydroxylation position are not explicitly supplied; the sequence-based family inference does not independently establish those details.


**Reason**

> A family-level sequence and reaction-chemistry match meaningfully distinguishes B from the alternatives, although exact reaction specificity is harder to infer from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B among the listed choices matches the annotated L-proline hydroxylation reaction.


### Important caveats

- The matched protein is also annotated with other proline hydroxylation activities, but those reactions are not among the choices.
- The cited experimental-evidence annotation supports the key, but the primary study was not independently reviewed here; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an Fe(II)/2-oxoglutarate oxygenase, including histidine/aspartate-containing candidate metal-binding motifs. Of the choices, B alone is a 2-oxoglutarate- and O2-dependent hydroxylation reaction; the others describe methyl transfer, nucleotide adenylation, or indigoidine formation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate and hydroxylation position are not explicitly supplied; the sequence-based family inference does not independently establish those details.",
    "reason": "A family-level sequence and reaction-chemistry match meaningfully distinguishes B from the alternatives, although exact reaction specificity is harder to infer from sequence alone."
  },
  "case_id": "catalytic_activity_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein the L-proline 2-oxoglutarate/O2 hydroxylation reaction in choice B and cites experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The matched protein is also annotated with other proline hydroxylation activities, but those reactions are not among the choices.",
    "The cited experimental-evidence annotation supports the key, but the primary study was not independently reviewed here; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B among the listed choices matches the annotated L-proline hydroxylation reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein the L-proline 2-oxoglutarate/O2 hydroxylation reaction in choice B and cites experimental evidence (ECO:0000269).",
    "evidence_ids": ["C5", "H5", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an Fe(II)/2-oxoglutarate oxygenase, including histidine/aspartate-containing candidate metal-binding motifs. Of the choices, B alone is a 2-oxoglutarate- and O2-dependent hydroxylation reaction; the others describe methyl transfer, nucleotide adenylation, or indigoidine formation.",
    "missing_item_specific_fact": "The exact substrate and hydroxylation position are not explicitly supplied; the sequence-based family inference does not independently establish those details.",
    "reason": "A family-level sequence and reaction-chemistry match meaningfully distinguishes B from the alternatives, although exact reaction specificity is harder to infer from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B among the listed choices matches the annotated L-proline hydroxylation reaction."
  },
  "important_caveats": [
    "The matched protein is also annotated with other proline hydroxylation activities, but those reactions are not among the choices.",
    "The cited experimental-evidence annotation supports the key, but the primary study was not independently reviewed here; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProt entry A0A455ZMR3 (PPZD_METMF, 2-oxoglutarate-Fe(II) type oxidoreductase ppzD from Metarhizium majus) with exact SHA256 match. The UniProt annotation lists the catalytic activity 'L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2' (EC 1.14.11.57) with experimental evidence (ECO:0000269, PubMed:38578094, a 2024 JACS paper reporting direct assay). Choice B exactly matches this annotated reaction. The annotation is based on experimental characterization, not mere computational transfer.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly argue that the absence of a Rossmann-like SAM-binding fold (ruling out A), a nucleotidyltransferase motif (ruling out C), and NRPS condensation-domain architecture (ruling out D) leaves B as the most plausible. Additionally, the 2-oxoglutarate/Fe(II) oxygenase superfamily has a loosely conserved 2-His-1-carboxylate facial triad (HxD/E...H) that might be discernible in the sequence. However, this superfamily encompasses hundreds of enzymes with vastly different substrates.


**Missing item-specific fact**

> Even if one identifies the protein as a member of the 2-oxoglutarate/Fe(II) oxygenase superfamily, specifying that this particular enzyme hydroxylates L-proline at the 4-position (trans-4-hydroxy-L-proline) rather than any of the dozens of other possible 2-OG oxygenase substrates requires knowledge of this specific protein's experimentally determined substrate specificity (ppzD from the pyrrolopyrazine biosynthetic cluster of Metarhizium majus). This item-specific functional annotation is not derivable from the linear 349-aa sequence alone.


**Reason**

> The four choices span four completely different enzyme classes (methyltransferase, 2-OG oxygenase, nucleotidyltransferase, oxidase). While elimination of three classes by absence of characteristic domains is possible, the positive identification of the specific substrate (L-proline) and product (trans-4-hydroxy-L-proline) for this particular 2-OG oxygenase requires the item-specific experimental characterization reported in PubMed:38578094. Recognizing the 2-OG oxygenase fold does not specify the substrate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt entry annotates three catalytic activities for ppzD (trans-4-hydroxy-L-proline, trans-3-hydroxy-L-proline, and cis-4-hydroxy-D-proline). However, only the trans-4-hydroxy-L-proline reaction appears among the four choices, so no ambiguity arises among the offered options. The other three choices (A, C, D) describe entirely different enzyme classes unrelated to this protein.


### Important caveats

- The UniProt entry lists multiple catalytic activities for ppzD; the question's phrasing 'the specific chemical reaction' slightly understates the enzyme's promiscuity, though only one of the annotated reactions appears as a choice.
- The experimental evidence (ECO:0000269, PubMed:38578094, 2024) postdates the 2019 sequence publication; the author's source snapshot date is unknown, so the annotation may or may not have been available at question-construction time.
- The protein is a specialized biosynthetic-cluster enzyme (ppzD) with no obvious commercial or textbook-level name, making sequence-based identification particularly challenging without database lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly argue that the absence of a Rossmann-like SAM-binding fold (ruling out A), a nucleotidyltransferase motif (ruling out C), and NRPS condensation-domain architecture (ruling out D) leaves B as the most plausible. Additionally, the 2-oxoglutarate/Fe(II) oxygenase superfamily has a loosely conserved 2-His-1-carboxylate facial triad (HxD/E...H) that might be discernible in the sequence. However, this superfamily encompasses hundreds of enzymes with vastly different substrates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Even if one identifies the protein as a member of the 2-oxoglutarate/Fe(II) oxygenase superfamily, specifying that this particular enzyme hydroxylates L-proline at the 4-position (trans-4-hydroxy-L-proline) rather than any of the dozens of other possible 2-OG oxygenase substrates requires knowledge of this specific protein's experimentally determined substrate specificity (ppzD from the pyrrolopyrazine biosynthetic cluster of Metarhizium majus). This item-specific functional annotation is not derivable from the linear 349-aa sequence alone.",
    "reason": "The four choices span four completely different enzyme classes (methyltransferase, 2-OG oxygenase, nucleotidyltransferase, oxidase). While elimination of three classes by absence of characteristic domains is possible, the positive identification of the specific substrate (L-proline) and product (trans-4-hydroxy-L-proline) for this particular 2-OG oxygenase requires the item-specific experimental characterization reported in PubMed:38578094. Recognizing the 2-OG oxygenase fold does not specify the substrate."
  },
  "case_id": "catalytic_activity_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C9",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt entry A0A455ZMR3 (PPZD_METMF, 2-oxoglutarate-Fe(II) type oxidoreductase ppzD from Metarhizium majus) with exact SHA256 match. The UniProt annotation lists the catalytic activity 'L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2' (EC 1.14.11.57) with experimental evidence (ECO:0000269, PubMed:38578094, a 2024 JACS paper reporting direct assay). Choice B exactly matches this annotated reaction. The annotation is based on experimental characterization, not mere computational transfer."
  },
  "important_caveats": [
    "The UniProt entry lists multiple catalytic activities for ppzD; the question's phrasing 'the specific chemical reaction' slightly understates the enzyme's promiscuity, though only one of the annotated reactions appears as a choice.",
    "The experimental evidence (ECO:0000269, PubMed:38578094, 2024) postdates the 2019 sequence publication; the author's source snapshot date is unknown, so the annotation may or may not have been available at question-construction time.",
    "The protein is a specialized biosynthetic-cluster enzyme (ppzD) with no obvious commercial or textbook-level name, making sequence-based identification particularly challenging without database lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry annotates three catalytic activities for ppzD (trans-4-hydroxy-L-proline, trans-3-hydroxy-L-proline, and cis-4-hydroxy-D-proline). However, only the trans-4-hydroxy-L-proline reaction appears among the four choices, so no ambiguity arises among the offered options. The other three choices (A, C, D) describe entirely different enzyme classes unrelated to this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt entry A0A455ZMR3 (PPZD_METMF, 2-oxoglutarate-Fe(II) type oxidoreductase ppzD from Metarhizium majus) with exact SHA256 match. The UniProt annotation lists the catalytic activity 'L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2' (EC 1.14.11.57) with experimental evidence (ECO:0000269, PubMed:38578094, a 2024 JACS paper reporting direct assay). Choice B exactly matches this annotated reaction. The annotation is based on experimental characterization, not mere computational transfer.",
    "evidence_ids": ["C1", "C4", "C5", "C9", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly argue that the absence of a Rossmann-like SAM-binding fold (ruling out A), a nucleotidyltransferase motif (ruling out C), and NRPS condensation-domain architecture (ruling out D) leaves B as the most plausible. Additionally, the 2-oxoglutarate/Fe(II) oxygenase superfamily has a loosely conserved 2-His-1-carboxylate facial triad (HxD/E...H) that might be discernible in the sequence. However, this superfamily encompasses hundreds of enzymes with vastly different substrates.",
    "missing_item_specific_fact": "Even if one identifies the protein as a member of the 2-oxoglutarate/Fe(II) oxygenase superfamily, specifying that this particular enzyme hydroxylates L-proline at the 4-position (trans-4-hydroxy-L-proline) rather than any of the dozens of other possible 2-OG oxygenase substrates requires knowledge of this specific protein's experimentally determined substrate specificity (ppzD from the pyrrolopyrazine biosynthetic cluster of Metarhizium majus). This item-specific functional annotation is not derivable from the linear 349-aa sequence alone.",
    "reason": "The four choices span four completely different enzyme classes (methyltransferase, 2-OG oxygenase, nucleotidyltransferase, oxidase). While elimination of three classes by absence of characteristic domains is possible, the positive identification of the specific substrate (L-proline) and product (trans-4-hydroxy-L-proline) for this particular 2-OG oxygenase requires the item-specific experimental characterization reported in PubMed:38578094. Recognizing the 2-OG oxygenase fold does not specify the substrate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry annotates three catalytic activities for ppzD (trans-4-hydroxy-L-proline, trans-3-hydroxy-L-proline, and cis-4-hydroxy-D-proline). However, only the trans-4-hydroxy-L-proline reaction appears among the four choices, so no ambiguity arises among the offered options. The other three choices (A, C, D) describe entirely different enzyme classes unrelated to this protein."
  },
  "important_caveats": [
    "The UniProt entry lists multiple catalytic activities for ppzD; the question's phrasing 'the specific chemical reaction' slightly understates the enzyme's promiscuity, though only one of the annotated reactions appears as a choice.",
    "The experimental evidence (ECO:0000269, PubMed:38578094, 2024) postdates the 2019 sequence publication; the author's source snapshot date is unknown, so the annotation may or may not have been available at question-construction time.",
    "The protein is a specialized biosynthetic-cluster enzyme (ppzD) with no obvious commercial or textbook-level name, making sequence-based identification particularly challenging without database lookup."
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

**Accession:** `A0A455ZMR3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 20. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:18.557115+00:00.  

```json
"A0A455ZMR3"
```

Source SHA-256: `598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:18.557115+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"Pyrrolopyrazine biosynthesis cluster protein D"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"value":"1.14.11.-"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"value":"1.14.11.57"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"2-oxoglutarate-Fe(II) type oxidoreductase ppzD"}}}
```

Source SHA-256: `598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:18.557115+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:51509"}}],"reaction":{"ecNumber":"1.14.11.57","evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"name":"L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:51508"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:16810"},{"database":"ChEBI","id":"CHEBI:30031"},{"database":"ChEBI","id":"CHEBI:58375"},{"database":"ChEBI","id":"CHEBI:60039"}]}}
```

Source SHA-256: `598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:18.557115+00:00.  

```json
{"citation":{"authors":["Rothchild K.W.","Hagar M.","Berry D.","Ryan K.S."],"citationCrossReferences":[{"database":"PubMed","id":"38578094"},{"database":"DOI","id":"10.1021/jacs.4c01419"}],"citationType":"journal article","firstPage":"10263","id":"38578094","journal":"J. Am. Chem. Soc.","lastPage":"10267","publicationDate":"2024","title":"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.","volume":"146"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:22.046089+00:00.  

```text
ID   PPZD_METMF              Reviewed;         349 AA.
AC   A0A455ZMR3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUN-2019, sequence version 1.
DT   28-JAN-2026, entry version 20.
DE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzD {ECO:0000303|PubMed:30452111};
DE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};
DE            EC=1.14.11.57 {ECO:0000269|PubMed:38578094};
DE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein D {ECO:0000303|PubMed:30452111};
GN   Name=ppzD;
OS   Metarhizium majus (strain ARSEF 297).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;
OC   Metarhizium majus.
OX   NCBI_TaxID=1276143;
```

Source SHA-256: `1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:22.046089+00:00.  

```text
DE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzD {ECO:0000303|PubMed:30452111};
DE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};
DE            EC=1.14.11.57 {ECO:0000269|PubMed:38578094};
DE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein D {ECO:0000303|PubMed:30452111};
```

Source SHA-256: `1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)  
**Locator:** `lines 25-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:22.046089+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RX   PubMed=38578094; DOI=10.1021/jacs.4c01419;
RA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;
RT   "Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ
RT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.";
RL   J. Am. Chem. Soc. 146:10263-10267(2024).
```

Source SHA-256: `1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)  
**Locator:** `lines 53-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:22.046089+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline +
CC         succinate + CO2; Xref=Rhea:RHEA:51508, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:16526, ChEBI:CHEBI:16810, ChEBI:CHEBI:30031,
CC         ChEBI:CHEBI:58375, ChEBI:CHEBI:60039; EC=1.14.11.57;
CC         Evidence={ECO:0000269|PubMed:38578094};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:51509;
CC         Evidence={ECO:0000269|PubMed:38578094};
```

Source SHA-256: `1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 72. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
