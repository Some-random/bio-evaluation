# EC_number_0154

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 1.1.1.440

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEKQVQIPEIELNSGHKMPLVGFGTCVPDPIPPLEELAGIFLEAIKVGYRHFDTASSYGTEEALGRAVAQAIETGLVNGREEFFISSKLWCEDADLDLILPALKKTLGNMGLDYLDLSMIHMPVRVRKGAEMFNYTKEDLLPFDIQGTWKAMEECNKLGLAKSIGVSNYSCEKLTKLLENATVPPAVNQVEMNVVWQQRKLLPFCKEKNIHVTAWSPLLSYGAVWGSNAVMENPILVEIAASKNKTVAQVALRWIYEQGASFIMRTFNKDRMFENVQIFDWELTKEELDKIQKIPQRRGTLGEDFIHPEGPIKSVEDLWDGDL

[Multiple Choices]
A. 1.1.1.195
B. 3.1.1.4
C. 1.1.1.440
D. 3.1.26.3
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry annotated as EC 1.1.1.440, with catalytic activity and EC number attributed to experimental evidence (ECO:0000269) from a cited publication. This supports choice C for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include oxidoreductases and enzymes from other broad classes, so general biological knowledge might suggest a broad class, but it does not identify the specific reaction or distinguish EC 1.1.1.440 from EC 1.1.1.195.


**Missing item-specific fact**

> The protein’s specific catalytic activity—rhazimol reduction/oxidation and its associated EC assignment—is not supplied in the sequence or prompt.


**Reason**

> Selecting the exact four-digit EC number requires protein-specific functional information not inferable with meaningful confidence from the provided sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Reviewer-only evidence supports choice C for the sequence-matched protein; no alternative listed EC number is supported by the supplied evidence.


### Important caveats

- The evidence is a database annotation tied to cited experimental evidence, not an independent review of the primary paper.
- The actual author source snapshot is unknown, although the historical sequence-matched entry also records EC 1.1.1.440.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include oxidoreductases and enzymes from other broad classes, so general biological knowledge might suggest a broad class, but it does not identify the specific reaction or distinguish EC 1.1.1.440 from EC 1.1.1.195.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein’s specific catalytic activity—rhazimol reduction/oxidation and its associated EC assignment—is not supplied in the sequence or prompt.",
    "reason": "Selecting the exact four-digit EC number requires protein-specific functional information not inferable with meaningful confidence from the provided sequence alone."
  },
  "case_id": "EC_number_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 1.1.1.440, with catalytic activity and EC number attributed to experimental evidence (ECO:0000269) from a cited publication. This supports choice C for this sequence."
  },
  "important_caveats": [
    "The evidence is a database annotation tied to cited experimental evidence, not an independent review of the primary paper.",
    "The actual author source snapshot is unknown, although the historical sequence-matched entry also records EC 1.1.1.440."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports choice C for the sequence-matched protein; no alternative listed EC number is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0154",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 1.1.1.440, with catalytic activity and EC number attributed to experimental evidence (ECO:0000269) from a cited publication. This supports choice C for this sequence.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include oxidoreductases and enzymes from other broad classes, so general biological knowledge might suggest a broad class, but it does not identify the specific reaction or distinguish EC 1.1.1.440 from EC 1.1.1.195.",
    "missing_item_specific_fact": "The protein’s specific catalytic activity—rhazimol reduction/oxidation and its associated EC assignment—is not supplied in the sequence or prompt.",
    "reason": "Selecting the exact four-digit EC number requires protein-specific functional information not inferable with meaningful confidence from the provided sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports choice C for the sequence-matched protein; no alternative listed EC number is supported by the supplied evidence."
  },
  "important_caveats": [
    "The evidence is a database annotation tied to cited experimental evidence, not an independent review of the primary paper.",
    "The actual author source snapshot is unknown, although the historical sequence-matched entry also records EC 1.1.1.440."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7S518 (sequence exactly matched, 323 aa) is annotated as Rhazimal reductase 1 (AsRHR1) with EC=1.1.1.440, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction 'rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)' is consistent with EC 1.1.1.440. The sequence in the question matches the UniProt sequence exactly (SHA-256 match confirmed in both current and historical records).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A partial reasoning pathway exists: the sequence contains Rossmann-fold-like motifs (e.g., 'VGFGT' near the N-terminus, 'TASSYG' resembling the SDR catalytic 'TGxxxYG' motif) and a length (~323 aa) consistent with the short-chain dehydrogenase/reductase (SDR) superfamily. This allows a knowledgeable model to eliminate the hydrolase options B (EC 3.1.1.4, carboxylesterase) and D (EC 3.1.26.3, ribonuclease), narrowing to two EC 1.1.1.x oxidoreductases. However, the final choice between A (1.1.1.195, secologanin synthase) and C (1.1.1.440, rhazimal reductase) requires knowing the specific substrate of this particular enzyme, which is not derivable from general sequence features shared by all SDRs.


**Missing item-specific fact**

> The specific substrate identity of this enzyme (rhazimal/rhazimol vs. secologanin) and the active-site residue configuration that confers monoterpene indole alkaloid vs. iridoid substrate specificity. The organism name (Alstonia scholaris) and its metabolic context are not provided in the question input.


**Reason**

> While the SDR-family motifs allow elimination of the two hydrolase distractors (a genuine reasoning step), distinguishing EC 1.1.1.195 from EC 1.1.1.440 requires knowing which specific alkaloid biosynthetic intermediate this particular SDR reduces. Both are plant SDRs with nearly identical folds and cofactor-binding motifs; substrate specificity is encoded in subtle active-site variations not identifiable by general biological reasoning from a raw sequence without structural modeling or database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt annotation with experimental evidence unambiguously supports EC 1.1.1.440. The hydrolase options (B, D) are clearly wrong for an SDR. Between A and C, only C is correct per the experimental data. No genuine ambiguity exists in the ground truth, though the reasoning pathway to select C over A is weak from sequence alone.


### Important caveats

- The organism name (Alstonia scholaris) and its well-known monoterpene indole alkaloid biosynthetic pathway are not provided in the model input, removing a potential contextual reasoning cue.
- EC 1.1.1.195 (secologanin synthase) and EC 1.1.1.440 (rhazimal reductase) are both plant SDRs with highly similar sequence architecture; their distinction is substrate-level, not fold-level.
- The annotation evidence code ECO:0000269 indicates direct experimental evidence (assay), strengthening the key's reliability.
- The sequence-to-accession match was confirmed by SHA-256 hash in both the current UniProt entry and the historical (entry version 12) record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A partial reasoning pathway exists: the sequence contains Rossmann-fold-like motifs (e.g., 'VGFGT' near the N-terminus, 'TASSYG' resembling the SDR catalytic 'TGxxxYG' motif) and a length (~323 aa) consistent with the short-chain dehydrogenase/reductase (SDR) superfamily. This allows a knowledgeable model to eliminate the hydrolase options B (EC 3.1.1.4, carboxylesterase) and D (EC 3.1.26.3, ribonuclease), narrowing to two EC 1.1.1.x oxidoreductases. However, the final choice between A (1.1.1.195, secologanin synthase) and C (1.1.1.440, rhazimal reductase) requires knowing the specific substrate of this particular enzyme, which is not derivable from general sequence features shared by all SDRs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity of this enzyme (rhazimal/rhazimol vs. secologanin) and the active-site residue configuration that confers monoterpene indole alkaloid vs. iridoid substrate specificity. The organism name (Alstonia scholaris) and its metabolic context are not provided in the question input.",
    "reason": "While the SDR-family motifs allow elimination of the two hydrolase distractors (a genuine reasoning step), distinguishing EC 1.1.1.195 from EC 1.1.1.440 requires knowing which specific alkaloid biosynthetic intermediate this particular SDR reduces. Both are plant SDRs with nearly identical folds and cofactor-binding motifs; substrate specificity is encoded in subtle active-site variations not identifiable by general biological reasoning from a raw sequence without structural modeling or database lookup."
  },
  "case_id": "EC_number_0154",
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
    "reason": "The UniProt entry A0A9E7S518 (sequence exactly matched, 323 aa) is annotated as Rhazimal reductase 1 (AsRHR1) with EC=1.1.1.440, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction 'rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)' is consistent with EC 1.1.1.440. The sequence in the question matches the UniProt sequence exactly (SHA-256 match confirmed in both current and historical records)."
  },
  "important_caveats": [
    "The organism name (Alstonia scholaris) and its well-known monoterpene indole alkaloid biosynthetic pathway are not provided in the model input, removing a potential contextual reasoning cue.",
    "EC 1.1.1.195 (secologanin synthase) and EC 1.1.1.440 (rhazimal reductase) are both plant SDRs with highly similar sequence architecture; their distinction is substrate-level, not fold-level.",
    "The annotation evidence code ECO:0000269 indicates direct experimental evidence (assay), strengthening the key's reliability.",
    "The sequence-to-accession match was confirmed by SHA-256 hash in both the current UniProt entry and the historical (entry version 12) record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt annotation with experimental evidence unambiguously supports EC 1.1.1.440. The hydrolase options (B, D) are clearly wrong for an SDR. Between A and C, only C is correct per the experimental data. No genuine ambiguity exists in the ground truth, though the reasoning pathway to select C over A is weak from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0154",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S518 (sequence exactly matched, 323 aa) is annotated as Rhazimal reductase 1 (AsRHR1) with EC=1.1.1.440, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction 'rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)' is consistent with EC 1.1.1.440. The sequence in the question matches the UniProt sequence exactly (SHA-256 match confirmed in both current and historical records).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A partial reasoning pathway exists: the sequence contains Rossmann-fold-like motifs (e.g., 'VGFGT' near the N-terminus, 'TASSYG' resembling the SDR catalytic 'TGxxxYG' motif) and a length (~323 aa) consistent with the short-chain dehydrogenase/reductase (SDR) superfamily. This allows a knowledgeable model to eliminate the hydrolase options B (EC 3.1.1.4, carboxylesterase) and D (EC 3.1.26.3, ribonuclease), narrowing to two EC 1.1.1.x oxidoreductases. However, the final choice between A (1.1.1.195, secologanin synthase) and C (1.1.1.440, rhazimal reductase) requires knowing the specific substrate of this particular enzyme, which is not derivable from general sequence features shared by all SDRs.",
    "missing_item_specific_fact": "The specific substrate identity of this enzyme (rhazimal/rhazimol vs. secologanin) and the active-site residue configuration that confers monoterpene indole alkaloid vs. iridoid substrate specificity. The organism name (Alstonia scholaris) and its metabolic context are not provided in the question input.",
    "reason": "While the SDR-family motifs allow elimination of the two hydrolase distractors (a genuine reasoning step), distinguishing EC 1.1.1.195 from EC 1.1.1.440 requires knowing which specific alkaloid biosynthetic intermediate this particular SDR reduces. Both are plant SDRs with nearly identical folds and cofactor-binding motifs; substrate specificity is encoded in subtle active-site variations not identifiable by general biological reasoning from a raw sequence without structural modeling or database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt annotation with experimental evidence unambiguously supports EC 1.1.1.440. The hydrolase options (B, D) are clearly wrong for an SDR. Between A and C, only C is correct per the experimental data. No genuine ambiguity exists in the ground truth, though the reasoning pathway to select C over A is weak from sequence alone."
  },
  "important_caveats": [
    "The organism name (Alstonia scholaris) and its well-known monoterpene indole alkaloid biosynthetic pathway are not provided in the model input, removing a potential contextual reasoning cue.",
    "EC 1.1.1.195 (secologanin synthase) and EC 1.1.1.440 (rhazimal reductase) are both plant SDRs with highly similar sequence architecture; their distinction is substrate-level, not fold-level.",
    "The annotation evidence code ECO:0000269 indicates direct experimental evidence (assay), strengthening the key's reliability.",
    "The sequence-to-accession match was confirmed by SHA-256 hash in both the current UniProt entry and the historical (entry version 12) record."
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

**Accession:** `A0A9E7S518` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
"A0A9E7S518"
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.1.1.440"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Rhazimal reductase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsRHR1"}]}}
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79617"}}],"reaction":{"ecNumber":"1.1.1.440","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"name":"rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79615"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:230473"},{"database":"ChEBI","id":"CHEBI:230474"}]}}
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65385.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:14.092631+00:00.  

```text
ID   RHR1_ALSSC              Reviewed;         323 AA.
AC   A0A9E7S518;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2023, sequence version 1.
DT   28-JAN-2026, entry version 12.
DE   RecName: Full=Rhazimal reductase 1 {ECO:0000303|PubMed:36349266};
DE            Short=AsRHR1 {ECO:0000303|PubMed:36349266};
DE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};
GN   Name=RHR1 {ECO:0000303|PubMed:36349266};
OS   Alstonia scholaris (Dogbane) (Echites scholaris).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;
OC   Alstonia.
OX   NCBI_TaxID=52822;
```

Source SHA-256: `9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:14.092631+00:00.  

```text
DE   RecName: Full=Rhazimal reductase 1 {ECO:0000303|PubMed:36349266};
DE            Short=AsRHR1 {ECO:0000303|PubMed:36349266};
DE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};
```

Source SHA-256: `9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)  
**Locator:** `lines 16-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:14.092631+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:URS65385.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=36349266; DOI=10.1039/d2sc03612f;
RA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;
RT   "Deciphering and reprogramming the cyclization regioselectivity in
RT   bifurcation of indole alkaloid biosynthesis.";
RL   Chem. Sci. 13:12389-12395(2022).
```

Source SHA-256: `9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)  
**Locator:** `lines 30-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:14.092631+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+);
CC         Xref=Rhea:RHEA:79615, ChEBI:CHEBI:15378, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:230473, ChEBI:CHEBI:230474;
CC         EC=1.1.1.440; Evidence={ECO:0000269|PubMed:36349266};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:79617;
CC         Evidence={ECO:0000269|PubMed:36349266};
```

Source SHA-256: `9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 154. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
