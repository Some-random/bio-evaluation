# catalytic_activity_0076

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — a ribonucleoside 5&#x27;-triphosphate + 2 H2O = a ribonucleoside 5&#x27;-phosphate + 2 phosphate + 2 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MALVRFATIITVLCHLAIQDGAAKSFPHGEKAPFPLTLIHINDLHARFDETNQKSSTCTNSKECIAGIARVYHTIKQLKSEYKTKNPLYLNAGDNFQGTLWYNLLRWNVTAYFIKELPPDAMTLGNHEFDHSPKGLAPYLAELEKMKIPTVVANLEKNGEPALKDSKIARSIVLKVGNRKVGVIGALYDKTHLVAQTGMVTLTNSIEAVRKEAQELKKKNVNIIVVLSHCGLDGDKQLAEEAGDLIDVIVGAHSHSLLLNKDAKVPYDTKYDTIEGDYPLVVKKSNNHTVLITQARSFGKYVGRLTVNFDCEGEVQSWEGYPIYMNNSVKQDEEVLRELEPWRAEVKRLGTQVIGTTEVFLDRESCRWCECTLGDLIADAYADQYTNSTVQPVAFVQAGNFRNPIEKGDITNGLAIEAAPYGSSVDMIKLSGADLWSAIDHSFTLDDEFRYNTAQVSGMAVVADLSKKPYERVQSIDIVGANGAKTALKKDQIYYVVVPSYLADGKDGFAMLKKGTNRVTGPLDSDVLIEYVRKRQTIAKTMFQEKRVVIENHTNGTCSWDLDSQRYKPK

[Multiple Choices]
A. Cd(2+)(in) = Cd(2+)(out)
B. vinorine + reduced [NADPH--hemoprotein reductase] + O2 = vomilenine + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
C. UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2
D. a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+)
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

> The supplied sequence exactly matches the 570-aa sequence in the cited UniProt records. Those records annotate it as an apyrase and give reaction D as its catalytic activity, with experimental-evidence code ECO:0000269 linked to PubMed 39294191. This supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted or membrane-targeted protein, but that does not establish its substrate or the specific nucleotide-hydrolysis reaction in D.


**Missing item-specific fact**

> The protein-specific identification or functional evidence that this sequence is an apyrase catalyzing the reaction in D.


**Reason**

> The prompt supplies only the sequence and choices. No general biological inference from the provided context meaningfully establishes this precise catalytic activity; selecting D depends on protein-specific functional knowledge absent from the prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reactions, and the matched protein annotation specifically supports D.


### Important caveats

- The annotation cites experimental evidence, but the underlying paper and assay details were not independently examined.
- The exact author source snapshot is unknown; the sequence matches both the retrieved current record and the historical record checked.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted or membrane-targeted protein, but that does not establish its substrate or the specific nucleotide-hydrolysis reaction in D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification or functional evidence that this sequence is an apyrase catalyzing the reaction in D.",
    "reason": "The prompt supplies only the sequence and choices. No general biological inference from the provided context meaningfully establishes this precise catalytic activity; selecting D depends on protein-specific functional knowledge absent from the prompt."
  },
  "case_id": "catalytic_activity_0076",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 570-aa sequence in the cited UniProt records. Those records annotate it as an apyrase and give reaction D as its catalytic activity, with experimental-evidence code ECO:0000269 linked to PubMed 39294191. This supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The annotation cites experimental evidence, but the underlying paper and assay details were not independently examined.",
    "The exact author source snapshot is unknown; the sequence matches both the retrieved current record and the historical record checked."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the matched protein annotation specifically supports D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 570-aa sequence in the cited UniProt records. Those records annotate it as an apyrase and give reaction D as its catalytic activity, with experimental-evidence code ECO:0000269 linked to PubMed 39294191. This supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted or membrane-targeted protein, but that does not establish its substrate or the specific nucleotide-hydrolysis reaction in D.",
    "missing_item_specific_fact": "The protein-specific identification or functional evidence that this sequence is an apyrase catalyzing the reaction in D.",
    "reason": "The prompt supplies only the sequence and choices. No general biological inference from the provided context meaningfully establishes this precise catalytic activity; selecting D depends on protein-specific functional knowledge absent from the prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the matched protein annotation specifically supports D."
  },
  "important_caveats": [
    "The annotation cites experimental evidence, but the underlying paper and assay details were not independently examined.",
    "The exact author source snapshot is unknown; the sequence matches both the retrieved current record and the historical record checked."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q5TVM9 (APY_ANOGA, Anopheles gambiae apyrase) exactly (570 aa, SHA-256 match). The UniProt entry annotates EC 3.6.1.5 with the catalytic reaction 'a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+)' (evidence C5, H5), supported by ECO:0000269 (direct experimental evidence from PubMed:39294191, Nat. Commun. 2024). The expected answer D is an exact textual match to the annotated reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several structural and size-based arguments allow elimination of distractors: (1) Option A (Cd2+ transporter) requires multiple transmembrane helices; the sequence shows only an N-terminal signal peptide (MALVRFATIITVLCHLAIQD) and no polytopic TM architecture. (2) Option B (cytochrome P450) requires the highly conserved heme-binding motif FxxGxRxCxG, which is absent from the sequence. (3) Option C (UDP-glucuronate decarboxylase, EC 4.1.1.35) is typically a ~200-250 aa cytosolic enzyme; the 570-aa secreted protein is far too large and has a signal peptide inconsistent with cytosolic nucleotide-sugar metabolism. (4) The remaining option D corresponds to NTPDase/apyrase (EC 3.6.1.5), a well-characterized enzyme class (~500-600 aa, secreted or membrane-bound) that hydrolyzes NTPs to NMPs + 2 Pi. The signal peptide, protein length, and overall domain architecture are consistent with a secreted NTPDase. The stoichiometry (triphosphate → monophosphate + 2 Pi) is standard textbook knowledge for EC 3.6.1.5.


**Missing item-specific fact**

> Positive identification of the NTPDase family from sequence motifs (e.g., PROSITE PS51061 conserved regions) would strengthen the argument, but the elimination-based reasoning path is sufficient to distinguish D from A, B, and C without exact database lookup.


**Reason**

> The question can be answered through structural elimination (TM topology, P450 heme motif, enzyme size) combined with general knowledge of NTPDase reaction stoichiometry. The signal peptide and ~570-aa length are inconsistent with options A, B, and C, leaving D as the only viable choice. This does not require memorizing the specific UniProt entry for Q5TVM9.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different enzyme classes (ion transporter, P450 monooxygenase, decarboxylase, NTPDase) with distinct structural signatures. The elimination arguments are robust enough that no alternative option is defensible given the sequence features.


### Important caveats

- The experimental evidence (ECO:0000269) supporting the apyrase annotation comes from PubMed:39294191 (2024), which post-dates the original sequence submission (2007). The historical entry version 120 (2026-01) already includes this annotation, so the key was available at the benchmark construction time.
- The positive identification of NTPDase family motifs from raw sequence is non-trivial; the reasoning path here relies more heavily on elimination of clearly incompatible options than on direct motif recognition.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must work from the sequence and general knowledge alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several structural and size-based arguments allow elimination of distractors: (1) Option A (Cd2+ transporter) requires multiple transmembrane helices; the sequence shows only an N-terminal signal peptide (MALVRFATIITVLCHLAIQD) and no polytopic TM architecture. (2) Option B (cytochrome P450) requires the highly conserved heme-binding motif FxxGxRxCxG, which is absent from the sequence. (3) Option C (UDP-glucuronate decarboxylase, EC 4.1.1.35) is typically a ~200-250 aa cytosolic enzyme; the 570-aa secreted protein is far too large and has a signal peptide inconsistent with cytosolic nucleotide-sugar metabolism. (4) The remaining option D corresponds to NTPDase/apyrase (EC 3.6.1.5), a well-characterized enzyme class (~500-600 aa, secreted or membrane-bound) that hydrolyzes NTPs to NMPs + 2 Pi. The signal peptide, protein length, and overall domain architecture are consistent with a secreted NTPDase. The stoichiometry (triphosphate → monophosphate + 2 Pi) is standard textbook knowledge for EC 3.6.1.5.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of the NTPDase family from sequence motifs (e.g., PROSITE PS51061 conserved regions) would strengthen the argument, but the elimination-based reasoning path is sufficient to distinguish D from A, B, and C without exact database lookup.",
    "reason": "The question can be answered through structural elimination (TM topology, P450 heme motif, enzyme size) combined with general knowledge of NTPDase reaction stoichiometry. The signal peptide and ~570-aa length are inconsistent with options A, B, and C, leaving D as the only viable choice. This does not require memorizing the specific UniProt entry for Q5TVM9."
  },
  "case_id": "catalytic_activity_0076",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5TVM9 (APY_ANOGA, Anopheles gambiae apyrase) exactly (570 aa, SHA-256 match). The UniProt entry annotates EC 3.6.1.5 with the catalytic reaction 'a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+)' (evidence C5, H5), supported by ECO:0000269 (direct experimental evidence from PubMed:39294191, Nat. Commun. 2024). The expected answer D is an exact textual match to the annotated reaction."
  },
  "important_caveats": [
    "The experimental evidence (ECO:0000269) supporting the apyrase annotation comes from PubMed:39294191 (2024), which post-dates the original sequence submission (2007). The historical entry version 120 (2026-01) already includes this annotation, so the key was available at the benchmark construction time.",
    "The positive identification of NTPDase family motifs from raw sequence is non-trivial; the reasoning path here relies more heavily on elimination of clearly incompatible options than on direct motif recognition.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must work from the sequence and general knowledge alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (ion transporter, P450 monooxygenase, decarboxylase, NTPDase) with distinct structural signatures. The elimination arguments are robust enough that no alternative option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5TVM9 (APY_ANOGA, Anopheles gambiae apyrase) exactly (570 aa, SHA-256 match). The UniProt entry annotates EC 3.6.1.5 with the catalytic reaction 'a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+)' (evidence C5, H5), supported by ECO:0000269 (direct experimental evidence from PubMed:39294191, Nat. Commun. 2024). The expected answer D is an exact textual match to the annotated reaction.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several structural and size-based arguments allow elimination of distractors: (1) Option A (Cd2+ transporter) requires multiple transmembrane helices; the sequence shows only an N-terminal signal peptide (MALVRFATIITVLCHLAIQD) and no polytopic TM architecture. (2) Option B (cytochrome P450) requires the highly conserved heme-binding motif FxxGxRxCxG, which is absent from the sequence. (3) Option C (UDP-glucuronate decarboxylase, EC 4.1.1.35) is typically a ~200-250 aa cytosolic enzyme; the 570-aa secreted protein is far too large and has a signal peptide inconsistent with cytosolic nucleotide-sugar metabolism. (4) The remaining option D corresponds to NTPDase/apyrase (EC 3.6.1.5), a well-characterized enzyme class (~500-600 aa, secreted or membrane-bound) that hydrolyzes NTPs to NMPs + 2 Pi. The signal peptide, protein length, and overall domain architecture are consistent with a secreted NTPDase. The stoichiometry (triphosphate → monophosphate + 2 Pi) is standard textbook knowledge for EC 3.6.1.5.",
    "missing_item_specific_fact": "Positive identification of the NTPDase family from sequence motifs (e.g., PROSITE PS51061 conserved regions) would strengthen the argument, but the elimination-based reasoning path is sufficient to distinguish D from A, B, and C without exact database lookup.",
    "reason": "The question can be answered through structural elimination (TM topology, P450 heme motif, enzyme size) combined with general knowledge of NTPDase reaction stoichiometry. The signal peptide and ~570-aa length are inconsistent with options A, B, and C, leaving D as the only viable choice. This does not require memorizing the specific UniProt entry for Q5TVM9."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (ion transporter, P450 monooxygenase, decarboxylase, NTPDase) with distinct structural signatures. The elimination arguments are robust enough that no alternative option is defensible given the sequence features."
  },
  "important_caveats": [
    "The experimental evidence (ECO:0000269) supporting the apyrase annotation comes from PubMed:39294191 (2024), which post-dates the original sequence submission (2007). The historical entry version 120 (2026-01) already includes this annotation, so the key was available at the benchmark construction time.",
    "The positive identification of NTPDase family motifs from raw sequence is non-trivial; the reasoning path here relies more heavily on elimination of clearly incompatible options than on direct motif recognition.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must work from the sequence and general knowledge alone."
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

**Accession:** `Q5TVM9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 120. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:23.238423+00:00.  

```json
"Q5TVM9"
```

Source SHA-256: `d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:23.238423+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39294191","source":"PubMed"}],"value":"5' nucleotidase ecto"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39294191","source":"PubMed"}],"value":"Ag5'NTE"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10801886","source":"PubMed"}],"value":"Apyrase-like 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"10801886","source":"PubMed"}],"value":"AgApyL1"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39294191","source":"PubMed"}],"value":"3.6.1.5"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39294191","source":"PubMed"}],"value":"Apyrase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39294191","source":"PubMed"}],"value":"AgApy"}]}}
```

Source SHA-256: `d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:23.238423+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.6.1.5","evidences":[{"evidenceCode":"ECO:0000269","id":"39294191","source":"PubMed"}],"name":"a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:36795"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:58043"},{"database":"ChEBI","id":"CHEBI:61557"}]}}
```

Source SHA-256: `d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-01T06:28:38.028811+00:00.  

```text
ID   APY_ANOGA               Reviewed;         570 AA.
AC   Q5TVM9; Q9UB34;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-JAN-2007, sequence version 1.
DT   28-JAN-2026, entry version 120.
DE   RecName: Full=Apyrase {ECO:0000303|PubMed:39294191};
DE            Short=AgApy {ECO:0000303|PubMed:39294191};
DE            EC=3.6.1.5 {ECO:0000269|PubMed:39294191};
DE   AltName: Full=5' nucleotidase ecto {ECO:0000303|PubMed:39294191};
DE            Short=Ag5'NTE {ECO:0000303|PubMed:39294191};
DE   AltName: Full=Apyrase-like 1 {ECO:0000303|PubMed:10801886};
DE            Short=AgApyL1 {ECO:0000303|PubMed:10801886};
DE   Flags: Precursor;
GN   ORFNames=AgaP_AGAP011026 {ECO:0000312|EMBL:EAA05427.2};
OS   Anopheles gambiae (African malaria mosquito).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;
OC   Anophelinae; Anopheles.
OX   NCBI_TaxID=7165 {ECO:0000312|Proteomes:UP000007062};
```

Source SHA-256: `dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)  
**Locator:** `lines 6-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-01T06:28:38.028811+00:00.  

```text
DE   RecName: Full=Apyrase {ECO:0000303|PubMed:39294191};
DE            Short=AgApy {ECO:0000303|PubMed:39294191};
DE            EC=3.6.1.5 {ECO:0000269|PubMed:39294191};
DE   AltName: Full=5' nucleotidase ecto {ECO:0000303|PubMed:39294191};
DE            Short=Ag5'NTE {ECO:0000303|PubMed:39294191};
DE   AltName: Full=Apyrase-like 1 {ECO:0000303|PubMed:10801886};
DE            Short=AgApyL1 {ECO:0000303|PubMed:10801886};
DE   Flags: Precursor;
```

Source SHA-256: `dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)  
**Locator:** `lines 102-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-01T06:28:38.028811+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside
CC         5'-phosphate + 2 phosphate + 2 H(+); Xref=Rhea:RHEA:36795,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:58043, ChEBI:CHEBI:61557; EC=3.6.1.5;
CC         Evidence={ECO:0000269|PubMed:39294191};
```

Source SHA-256: `dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 76. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
