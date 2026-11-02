# active_site_0020

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **D** — Position 120 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSSTISASAVVLLSGLASAQTFTDCNPTEKTCPSDPAIGGLQVTDFTAGKSSYWEVEDGTTMSYDGTLGAQFVISTATDAPTIKNIGYIMFGRIETWVRASAGTGIVSSFILESDDLDEIDWEWLGANNAEAENNFFGKGNTTTYDRAQYPAVATPIDTFHNYTIDWTAKSTIWYIDGVAVRTLLYDDKQTVGGKNYPQTPMLVKMGSWIGCASKAAETDSATAGTCSWAGGAVDLTQGPFTMYVKNVTIQDYGCATEYTYGDLTGDYTSIKATGGCSADGSAASPSASSSSAASGSSSSTKSSSGSSTLSTVTGTTSAIAVGTATGTATLSAGEKATAAAISGSTTSSSTIAKVTTTSDANSLKKPKHEYGMIDLGVMVLGLGLGYLVM

[Multiple Choices]
A. Position 250 (Proton acceptor)
B. Position 95 (Nucleophile)
C. Position 1045 (Proton acceptor; for dehydratase activity)
D. Position 120 (Nucleophile)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The matched UniProt entry annotates position 120 as the nucleophile, consistent with choice D. This is a literature-supported database annotation; the supplied excerpts do not independently validate the underlying experiment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a sufficiently specific general biological basis for identifying residue 120 as the nucleophile rather than the other candidate positions.


**Missing item-specific fact**

> The protein-specific assignment of position 120 as the nucleophile, supported by the cited literature and recorded in UniProt, is absent from the model input.


**Reason**

> The exact residue position and catalytic role require protein-specific functional annotation or experimental knowledge. Recognizing the sequence or using a generic predictor would not make this a reasoning-supported distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the matched annotation supports D. The entry also annotates position 124 as a proton donor, but that role and position are not offered as a competing choice.


### Important caveats

- The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.
- The database annotation is linked to a publication; the provided evidence does not include the primary experimental results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific general biological basis for identifying residue 120 as the nucleophile rather than the other candidate positions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of position 120 as the nucleophile, supported by the cited literature and recorded in UniProt, is absent from the model input.",
    "reason": "The exact residue position and catalytic role require protein-specific functional annotation or experimental knowledge. Recognizing the sequence or using a generic predictor would not make this a reasoning-supported distinction."
  },
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates position 120 as the nucleophile, consistent with choice D. This is a literature-supported database annotation; the supplied excerpts do not independently validate the underlying experiment."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The database annotation is linked to a publication; the provided evidence does not include the primary experimental results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the matched annotation supports D. The entry also annotates position 124 as a proton donor, but that role and position are not offered as a competing choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates position 120 as the nucleophile, consistent with choice D. This is a literature-supported database annotation; the supplied excerpts do not independently validate the underlying experiment.",
    "evidence_ids": ["C5", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific general biological basis for identifying residue 120 as the nucleophile rather than the other candidate positions.",
    "missing_item_specific_fact": "The protein-specific assignment of position 120 as the nucleophile, supported by the cited literature and recorded in UniProt, is absent from the model input.",
    "reason": "The exact residue position and catalytic role require protein-specific functional annotation or experimental knowledge. Recognizing the sequence or using a generic predictor would not make this a reasoning-supported distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the matched annotation supports D. The entry also annotates position 124 as a proton donor, but that role and position are not offered as a competing choice."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The database annotation is linked to a publication; the provided evidence does not include the primary experimental results."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A384J6C4 annotates ACT_SITE at position 120 as 'Nucleophile' with evidence code ECO:0000305 (inferred by direct assay) from PubMed:33846308 (Bi et al., Nat. Commun. 2021), indicating experimental support. The sequence at position 120 is Glu (E), chemically consistent with a nucleophile in a glycoside hydrolase/transglycosylase. The protein is 391 AA, so choice C (position 1045) is impossible. Position 95 is Ile (not a nucleophile), and position 250 is Thr (not a typical proton acceptor in this enzyme class). The expected answer D is directly confirmed by the database annotation with experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [C11](#evidence-c11), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is a Crh-like chitin transglycosylase (GH18-related). A model recognizing glycoside hydrolase/transglycosylase function can identify the DxxDxxxE-like catalytic motif in the region ~116–124 (D-D-L-D-E-I-D-W-E). Among the four choices: (C) position 1045 is impossible for a 391-AA protein; (B) position 95 is Ile, not a viable nucleophile; (A) position 250 is Thr, not a typical proton acceptor in glycosidases. Only choice D (Glu at 120, nucleophile) presents a chemically plausible catalytic residue within the identified motif region. Glu is the canonical nucleophile in GH18-family glycosidases, and its position within the DxxDxxxE-like cluster provides a concrete biochemical argument favoring D over the other options.


**Missing item-specific fact**

> The precise mechanistic distinction between E(120) as nucleophile versus E(124) as proton donor (or vice versa) in this Crh-like subfamily is not trivially derivable from the canonical GH18 DxxDxxxE motif alone, since the canonical motif would predict the terminal E (124) as nucleophile. The exact role assignment for E(120) benefits from knowledge of Crh-specific mechanism reported in PubMed:33846308.


**Reason**

> Although the exact nucleophile-vs-proton-donor assignment for this non-canonical Crh variant requires some specific mechanistic knowledge, the multiple-choice format allows elimination of three clearly implausible options (out-of-range position, non-catalytic residues) leaving only the chemically sensible Glu-in-motif answer. This elimination plus recognition of the GH18 catalytic motif provides meaningful reasoning grounds to select D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one choice (D) presents a chemically plausible catalytic residue (Glu) at a position within the identified active-site motif. The other three options are eliminated by basic constraints: C is out of range, B is an isoleucine, A is a threonine not typically serving as proton acceptor in this enzyme class. No genuine ambiguity exists among the options.


### Important caveats

- The EC-number assignments (chitinase, transglycosylase) for this entry are by similarity (ECO:0000250|UniProtKB:Q8J0P4), not direct experiment; however, the active-site annotations at 120 and 124 carry experimental evidence (ECO:0000305).
- The canonical GH18 DxxDxxxE motif would nominally predict the terminal Glu (position 124) as nucleophile, whereas the experimental annotation assigns nucleophile role to Glu-120 in this Crh-like protein. A model relying solely on the canonical motif template might misassign the nucleophile position, but the multiple-choice format still permits correct selection by elimination.
- The UniProt entry was first public in June 2025; the author's construction date is unknown, so the annotation may not have existed when the benchmark was built.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a Crh-like chitin transglycosylase (GH18-related). A model recognizing glycoside hydrolase/transglycosylase function can identify the DxxDxxxE-like catalytic motif in the region ~116–124 (D-D-L-D-E-I-D-W-E). Among the four choices: (C) position 1045 is impossible for a 391-AA protein; (B) position 95 is Ile, not a viable nucleophile; (A) position 250 is Thr, not a typical proton acceptor in glycosidases. Only choice D (Glu at 120, nucleophile) presents a chemically plausible catalytic residue within the identified motif region. Glu is the canonical nucleophile in GH18-family glycosidases, and its position within the DxxDxxxE-like cluster provides a concrete biochemical argument favoring D over the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise mechanistic distinction between E(120) as nucleophile versus E(124) as proton donor (or vice versa) in this Crh-like subfamily is not trivially derivable from the canonical GH18 DxxDxxxE motif alone, since the canonical motif would predict the terminal E (124) as nucleophile. The exact role assignment for E(120) benefits from knowledge of Crh-specific mechanism reported in PubMed:33846308.",
    "reason": "Although the exact nucleophile-vs-proton-donor assignment for this non-canonical Crh variant requires some specific mechanistic knowledge, the multiple-choice format allows elimination of three clearly implausible options (out-of-range position, non-catalytic residues) leaving only the chemically sensible Glu-in-motif answer. This elimination plus recognition of the GH18 catalytic motif provides meaningful reasoning grounds to select D."
  },
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4",
      "C11",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A384J6C4 annotates ACT_SITE at position 120 as 'Nucleophile' with evidence code ECO:0000305 (inferred by direct assay) from PubMed:33846308 (Bi et al., Nat. Commun. 2021), indicating experimental support. The sequence at position 120 is Glu (E), chemically consistent with a nucleophile in a glycoside hydrolase/transglycosylase. The protein is 391 AA, so choice C (position 1045) is impossible. Position 95 is Ile (not a nucleophile), and position 250 is Thr (not a typical proton acceptor in this enzyme class). The expected answer D is directly confirmed by the database annotation with experimental evidence."
  },
  "important_caveats": [
    "The EC-number assignments (chitinase, transglycosylase) for this entry are by similarity (ECO:0000250|UniProtKB:Q8J0P4), not direct experiment; however, the active-site annotations at 120 and 124 carry experimental evidence (ECO:0000305).",
    "The canonical GH18 DxxDxxxE motif would nominally predict the terminal Glu (position 124) as nucleophile, whereas the experimental annotation assigns nucleophile role to Glu-120 in this Crh-like protein. A model relying solely on the canonical motif template might misassign the nucleophile position, but the multiple-choice format still permits correct selection by elimination.",
    "The UniProt entry was first public in June 2025; the author's construction date is unknown, so the annotation may not have existed when the benchmark was built."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one choice (D) presents a chemically plausible catalytic residue (Glu) at a position within the identified active-site motif. The other three options are eliminated by basic constraints: C is out of range, B is an isoleucine, A is a threonine not typically serving as proton acceptor in this enzyme class. No genuine ambiguity exists among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A384J6C4 annotates ACT_SITE at position 120 as 'Nucleophile' with evidence code ECO:0000305 (inferred by direct assay) from PubMed:33846308 (Bi et al., Nat. Commun. 2021), indicating experimental support. The sequence at position 120 is Glu (E), chemically consistent with a nucleophile in a glycoside hydrolase/transglycosylase. The protein is 391 AA, so choice C (position 1045) is impossible. Position 95 is Ile (not a nucleophile), and position 250 is Thr (not a typical proton acceptor in this enzyme class). The expected answer D is directly confirmed by the database annotation with experimental evidence.",
    "evidence_ids": ["C5", "H3", "C6", "H4", "C11", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is a Crh-like chitin transglycosylase (GH18-related). A model recognizing glycoside hydrolase/transglycosylase function can identify the DxxDxxxE-like catalytic motif in the region ~116–124 (D-D-L-D-E-I-D-W-E). Among the four choices: (C) position 1045 is impossible for a 391-AA protein; (B) position 95 is Ile, not a viable nucleophile; (A) position 250 is Thr, not a typical proton acceptor in glycosidases. Only choice D (Glu at 120, nucleophile) presents a chemically plausible catalytic residue within the identified motif region. Glu is the canonical nucleophile in GH18-family glycosidases, and its position within the DxxDxxxE-like cluster provides a concrete biochemical argument favoring D over the other options.",
    "missing_item_specific_fact": "The precise mechanistic distinction between E(120) as nucleophile versus E(124) as proton donor (or vice versa) in this Crh-like subfamily is not trivially derivable from the canonical GH18 DxxDxxxE motif alone, since the canonical motif would predict the terminal E (124) as nucleophile. The exact role assignment for E(120) benefits from knowledge of Crh-specific mechanism reported in PubMed:33846308.",
    "reason": "Although the exact nucleophile-vs-proton-donor assignment for this non-canonical Crh variant requires some specific mechanistic knowledge, the multiple-choice format allows elimination of three clearly implausible options (out-of-range position, non-catalytic residues) leaving only the chemically sensible Glu-in-motif answer. This elimination plus recognition of the GH18 catalytic motif provides meaningful reasoning grounds to select D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one choice (D) presents a chemically plausible catalytic residue (Glu) at a position within the identified active-site motif. The other three options are eliminated by basic constraints: C is out of range, B is an isoleucine, A is a threonine not typically serving as proton acceptor in this enzyme class. No genuine ambiguity exists among the options."
  },
  "important_caveats": [
    "The EC-number assignments (chitinase, transglycosylase) for this entry are by similarity (ECO:0000250|UniProtKB:Q8J0P4), not direct experiment; however, the active-site annotations at 120 and 124 carry experimental evidence (ECO:0000305).",
    "The canonical GH18 DxxDxxxE motif would nominally predict the terminal Glu (position 124) as nucleophile, whereas the experimental annotation assigns nucleophile role to Glu-120 in this Crh-like protein. A model relying solely on the canonical motif template might misassign the nucleophile position, but the multiple-choice format still permits correct selection by elimination.",
    "The UniProt entry was first public in June 2025; the author's construction date is unknown, so the annotation may not have existed when the benchmark was built."
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

**Accession:** `A0A384J6C4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:56.188291+00:00.  

```json
{"description":"Nucleophile","evidences":[{"evidenceCode":"ECO:0000305","id":"33846308","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":120},"start":{"modifier":"EXACT","value":120}},"type":"Active site"}
```

Source SHA-256: `1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:56.188291+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000305","id":"33846308","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":124},"start":{"modifier":"EXACT","value":124}},"type":"Active site"}
```

Source SHA-256: `1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:56.188291+00:00.  

```json
{"citation":{"authors":["Bi K.","Scalschi L.","Jaiswal N.","Mengiste T.","Fried R.","Sanz A.B.","Arroyo J.","Zhu W.","Masrati G.","Sharon A."],"citationCrossReferences":[{"database":"PubMed","id":"33846308"},{"database":"DOI","id":"10.1038/s41467-021-22436-1"}],"citationType":"journal article","firstPage":"2166","id":"33846308","journal":"Nat. Commun.","lastPage":"2166","publicationDate":"2021","title":"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.","volume":"12"},"referenceNumber":4,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE","DOMAIN","MUTAGENESIS OF CYS-33; GLU-120; ASP-122 AND GLU-124","SUBUNIT","INTERACTION WITH CRH2 AND CRH3"]}
```

Source SHA-256: `1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)  
**Locator:** `lines 56-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:58.365606+00:00.  

```text
RN   [4]
RP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, DOMAIN, MUTAGENESIS
RP   OF CYS-33; GLU-120; ASP-122 AND GLU-124, SUBUNIT, AND INTERACTION WITH CRH2
RP   AND CRH3.
RX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;
RA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,
RA   Arroyo J., Zhu W., Masrati G., Sharon A.;
RT   "The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector
RT   triggering plant cell death and defense response.";
RL   Nat. Commun. 12:2166-2166(2021).
```

Source SHA-256: `47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)  
**Locator:** `lines 169-171`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:58.365606+00:00.  

```text
FT   ACT_SITE        120
FT                   /note="Nucleophile"
FT                   /evidence="ECO:0000305|PubMed:33846308"
```

Source SHA-256: `47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)  
**Locator:** `lines 172-174`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:58.365606+00:00.  

```text
FT   ACT_SITE        124
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000305|PubMed:33846308"
```

Source SHA-256: `47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
