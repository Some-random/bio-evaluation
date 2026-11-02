# active_site_0016

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 159 (Proton donor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPISIPKGEKLMDLLSMKGKVTIVTGASGPRGMGIEAARGIAEMGGNVALTYAGRKEGGEKNAAALEKEYGIKAKAYKLDVANYESCCQLVKDVIADFGQIDAFVANAGKTADSGVLDGEISAFEEVIQTDLLGVAYCAKAVGHHFKERQTGSFVITASMSGHIANFPQEQTSYNVAKAGCIHMARSLANEWRDFARVNSISPGYIDTGLSDFVDKETQKLWHSMIPMGRDGDAKELKAAYVYFCSDASTYTTGSDLVIDGGYCAR

[Multiple Choices]
A. Position 64 (Nucleophile (Probable))
B. Position 159 (Proton donor)
C. Position 153 (catalytic acid/base residue)
D. Position 342 (Charge relay system)
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

> For the exact supplied sequence, UniProt annotates position 159 as the proton donor. This supports choice B, but the annotation is transferred by similarity from UniProtKB:P0C0Y5 (ECO:0000250), not established here as a direct experiment on this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a 266-residue enzyme, so position 342 is out of range; however, general sequence reasoning does not identify position 159 as its proton donor or distinguish it reliably from the other in-range residue claims.


**Missing item-specific fact**

> The protein-specific active-site annotation assigning the proton-donor role to residue 159, or equivalent validated homolog or structural evidence.


**Reason**

> The key is supported by reviewer-only annotation, but that annotation and the protein identity are absent from the evaluated input. Exact residue-role assignment therefore depends on an item-specific external fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports B; it does not support the different residue-role claims in A or C, and D names a position beyond the sequence length.


### Important caveats

- The sequence matches the 266-residue UniProt entry, but the actual source snapshot used by the author is unknown.
- The position-159 annotation is similarity-based, transferred from P0C0Y5; it should not be represented as direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a 266-residue enzyme, so position 342 is out of range; however, general sequence reasoning does not identify position 159 as its proton donor or distinguish it reliably from the other in-range residue claims.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning the proton-donor role to residue 159, or equivalent validated homolog or structural evidence.",
    "reason": "The key is supported by reviewer-only annotation, but that annotation and the protein identity are absent from the evaluated input. Exact residue-role assignment therefore depends on an item-specific external fact."
  },
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "For the exact supplied sequence, UniProt annotates position 159 as the proton donor. This supports choice B, but the annotation is transferred by similarity from UniProtKB:P0C0Y5 (ECO:0000250), not established here as a direct experiment on this protein."
  },
  "important_caveats": [
    "The sequence matches the 266-residue UniProt entry, but the actual source snapshot used by the author is unknown.",
    "The position-159 annotation is similarity-based, transferred from P0C0Y5; it should not be represented as direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; it does not support the different residue-role claims in A or C, and D names a position beyond the sequence length."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "For the exact supplied sequence, UniProt annotates position 159 as the proton donor. This supports choice B, but the annotation is transferred by similarity from UniProtKB:P0C0Y5 (ECO:0000250), not established here as a direct experiment on this protein.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a 266-residue enzyme, so position 342 is out of range; however, general sequence reasoning does not identify position 159 as its proton donor or distinguish it reliably from the other in-range residue claims.",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning the proton-donor role to residue 159, or equivalent validated homolog or structural evidence.",
    "reason": "The key is supported by reviewer-only annotation, but that annotation and the protein identity are absent from the evaluated input. Exact residue-role assignment therefore depends on an item-specific external fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; it does not support the different residue-role claims in A or C, and D names a position beyond the sequence length."
  },
  "important_caveats": [
    "The sequence matches the 266-residue UniProt entry, but the actual source snapshot used by the author is unknown.",
    "The position-159 annotation is similarity-based, transferred from P0C0Y5; it should not be represented as direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A223HDI5 (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) annotates position 159 as 'Proton donor' (Active site), matching choice B exactly. The sequence in the question matches the entry (266 aa, SHA-256 match). However, the evidence code is ECO:0000250 (inferred by similarity to P0C0Y5), making this a computational/transfer annotation rather than direct experimental evidence for this specific protein. The annotation is nonetheless the authoritative database claim and is consistent with the SDR-family catalytic mechanism (Ser as proton donor in the Ser-Tyr-Lys catalytic triad).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several reasoning steps distinguish B from the distractors using general biochemistry: (1) The N-terminal region contains a Rossmann-fold-like NAD(P)-binding motif (GASGPR at ~26-31), identifying this as an NAD(P)-dependent dehydrogenase. (2) The YxxxK motif at positions 174-178 (Y-N-V-A-K) is the hallmark SDR (short-chain dehydrogenase/reductase) catalytic Tyr-Lys dyad. (3) In the SDR catalytic mechanism, the catalytic Ser acts specifically as a proton donor (donating H+ to the substrate carbonyl oxygen), the Tyr as proton acceptor, and the Lys lowers the Tyr pKa. The functional label 'Proton donor' in choice B matches this mechanism precisely. (4) Choice D (position 342) is impossible in a 266-residue protein. (5) Choice A (position 64, Alanine) cannot serve as a nucleophile. (6) Choice C labels Ser153 as 'catalytic acid/base residue,' which is not the standard SDR terminology for the catalytic Ser (it is specifically a proton donor, not a general acid/base). The Ser at 159 is ~15 residues upstream of the catalytic Tyr(174), consistent with typical SDR catalytic-tetrad spacing, while Ser(153) is ~21 residues upstream.


**Missing item-specific fact**

> Distinguishing Ser159 from Ser153 as the catalytic proton donor relies on the specific spacing (~15 residues) between the catalytic Ser and the YxxxK dyad in SDR enzymes, which is a family-specific structural detail. A model without SDR-family knowledge would struggle to choose between the two Ser residues purely from the sequence.


**Reason**

> The SDR catalytic mechanism (Ser = proton donor, Tyr = proton acceptor, Lys = pKa modulator), the identifiable YxxxK motif, and the functional labels in the choices provide a concrete biological argument for B over the other options. The elimination of D (impossible position) and A (Ala cannot be nucleophile) is straightforward. The B-vs-C distinction is supported by the correct SDR functional terminology ('Proton donor' vs. non-standard 'acid/base'). The residual difficulty in pinpointing Ser159 over Ser153 is a matter of SDR-specific structural spacing, which is specialized but defensible general biochemistry knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A, C, and D are clearly eliminable: A assigns nucleophile function to Alanine (position 64), C uses non-standard terminology ('acid/base') for a Ser that in SDR enzymes is specifically a proton donor, and D references position 342 in a 266-residue protein. Only B corresponds to an annotated active-site residue with a mechanistically accurate functional label. While positions 174 (Proton acceptor) and 178 (Lowers pKa of Tyr) are also active-site residues, they do not appear among the choices, so there is no competing correct option.


### Important caveats

- The UniProt annotation for position 159 uses evidence code ECO:0000250 (inferred by similarity to P0C0Y5), meaning it is a computational transfer annotation, not direct experimental evidence (e.g., site-directed mutagenesis or crystallography) for this specific Aureobasidium enzyme.
- The protein is 266 residues long; choice D (position 342) is trivially impossible, making it an unusually easy distractor.
- The question stem asks to identify 'the enzyme's catalytic center' (singular), but the SDR catalytic center comprises multiple residues (Ser159, Tyr174, Lys178). Only Ser159 appears among the choices, so the question is effectively asking which single annotated active-site residue is correctly described.
- The entry was first public on 2025-02-05 with annotation updates through 2026-01-28; the author's source snapshot date is unknown, but the sequence has been stable since 2017-10-25 (sequence version 1).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several reasoning steps distinguish B from the distractors using general biochemistry: (1) The N-terminal region contains a Rossmann-fold-like NAD(P)-binding motif (GASGPR at ~26-31), identifying this as an NAD(P)-dependent dehydrogenase. (2) The YxxxK motif at positions 174-178 (Y-N-V-A-K) is the hallmark SDR (short-chain dehydrogenase/reductase) catalytic Tyr-Lys dyad. (3) In the SDR catalytic mechanism, the catalytic Ser acts specifically as a proton donor (donating H+ to the substrate carbonyl oxygen), the Tyr as proton acceptor, and the Lys lowers the Tyr pKa. The functional label 'Proton donor' in choice B matches this mechanism precisely. (4) Choice D (position 342) is impossible in a 266-residue protein. (5) Choice A (position 64, Alanine) cannot serve as a nucleophile. (6) Choice C labels Ser153 as 'catalytic acid/base residue,' which is not the standard SDR terminology for the catalytic Ser (it is specifically a proton donor, not a general acid/base). The Ser at 159 is ~15 residues upstream of the catalytic Tyr(174), consistent with typical SDR catalytic-tetrad spacing, while Ser(153) is ~21 residues upstream.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Distinguishing Ser159 from Ser153 as the catalytic proton donor relies on the specific spacing (~15 residues) between the catalytic Ser and the YxxxK dyad in SDR enzymes, which is a family-specific structural detail. A model without SDR-family knowledge would struggle to choose between the two Ser residues purely from the sequence.",
    "reason": "The SDR catalytic mechanism (Ser = proton donor, Tyr = proton acceptor, Lys = pKa modulator), the identifiable YxxxK motif, and the functional labels in the choices provide a concrete biological argument for B over the other options. The elimination of D (impossible position) and A (Ala cannot be nucleophile) is straightforward. The B-vs-C distinction is supported by the correct SDR functional terminology ('Proton donor' vs. non-standard 'acid/base'). The residual difficulty in pinpointing Ser159 over Ser153 is a matter of SDR-specific structural spacing, which is specialized but defensible general biochemistry knowledge."
  },
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A223HDI5 (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) annotates position 159 as 'Proton donor' (Active site), matching choice B exactly. The sequence in the question matches the entry (266 aa, SHA-256 match). However, the evidence code is ECO:0000250 (inferred by similarity to P0C0Y5), making this a computational/transfer annotation rather than direct experimental evidence for this specific protein. The annotation is nonetheless the authoritative database claim and is consistent with the SDR-family catalytic mechanism (Ser as proton donor in the Ser-Tyr-Lys catalytic triad)."
  },
  "important_caveats": [
    "The UniProt annotation for position 159 uses evidence code ECO:0000250 (inferred by similarity to P0C0Y5), meaning it is a computational transfer annotation, not direct experimental evidence (e.g., site-directed mutagenesis or crystallography) for this specific Aureobasidium enzyme.",
    "The protein is 266 residues long; choice D (position 342) is trivially impossible, making it an unusually easy distractor.",
    "The question stem asks to identify 'the enzyme's catalytic center' (singular), but the SDR catalytic center comprises multiple residues (Ser159, Tyr174, Lys178). Only Ser159 appears among the choices, so the question is effectively asking which single annotated active-site residue is correctly described.",
    "The entry was first public on 2025-02-05 with annotation updates through 2026-01-28; the author's source snapshot date is unknown, but the sequence has been stable since 2017-10-25 (sequence version 1)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D are clearly eliminable: A assigns nucleophile function to Alanine (position 64), C uses non-standard terminology ('acid/base') for a Ser that in SDR enzymes is specifically a proton donor, and D references position 342 in a 266-residue protein. Only B corresponds to an annotated active-site residue with a mechanistically accurate functional label. While positions 174 (Proton acceptor) and 178 (Lowers pKa of Tyr) are also active-site residues, they do not appear among the choices, so there is no competing correct option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A223HDI5 (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) annotates position 159 as 'Proton donor' (Active site), matching choice B exactly. The sequence in the question matches the entry (266 aa, SHA-256 match). However, the evidence code is ECO:0000250 (inferred by similarity to P0C0Y5), making this a computational/transfer annotation rather than direct experimental evidence for this specific protein. The annotation is nonetheless the authoritative database claim and is consistent with the SDR-family catalytic mechanism (Ser as proton donor in the Ser-Tyr-Lys catalytic triad).",
    "evidence_ids": ["C5", "H3", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several reasoning steps distinguish B from the distractors using general biochemistry: (1) The N-terminal region contains a Rossmann-fold-like NAD(P)-binding motif (GASGPR at ~26-31), identifying this as an NAD(P)-dependent dehydrogenase. (2) The YxxxK motif at positions 174-178 (Y-N-V-A-K) is the hallmark SDR (short-chain dehydrogenase/reductase) catalytic Tyr-Lys dyad. (3) In the SDR catalytic mechanism, the catalytic Ser acts specifically as a proton donor (donating H+ to the substrate carbonyl oxygen), the Tyr as proton acceptor, and the Lys lowers the Tyr pKa. The functional label 'Proton donor' in choice B matches this mechanism precisely. (4) Choice D (position 342) is impossible in a 266-residue protein. (5) Choice A (position 64, Alanine) cannot serve as a nucleophile. (6) Choice C labels Ser153 as 'catalytic acid/base residue,' which is not the standard SDR terminology for the catalytic Ser (it is specifically a proton donor, not a general acid/base). The Ser at 159 is ~15 residues upstream of the catalytic Tyr(174), consistent with typical SDR catalytic-tetrad spacing, while Ser(153) is ~21 residues upstream.",
    "missing_item_specific_fact": "Distinguishing Ser159 from Ser153 as the catalytic proton donor relies on the specific spacing (~15 residues) between the catalytic Ser and the YxxxK dyad in SDR enzymes, which is a family-specific structural detail. A model without SDR-family knowledge would struggle to choose between the two Ser residues purely from the sequence.",
    "reason": "The SDR catalytic mechanism (Ser = proton donor, Tyr = proton acceptor, Lys = pKa modulator), the identifiable YxxxK motif, and the functional labels in the choices provide a concrete biological argument for B over the other options. The elimination of D (impossible position) and A (Ala cannot be nucleophile) is straightforward. The B-vs-C distinction is supported by the correct SDR functional terminology ('Proton donor' vs. non-standard 'acid/base'). The residual difficulty in pinpointing Ser159 over Ser153 is a matter of SDR-specific structural spacing, which is specialized but defensible general biochemistry knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D are clearly eliminable: A assigns nucleophile function to Alanine (position 64), C uses non-standard terminology ('acid/base') for a Ser that in SDR enzymes is specifically a proton donor, and D references position 342 in a 266-residue protein. Only B corresponds to an annotated active-site residue with a mechanistically accurate functional label. While positions 174 (Proton acceptor) and 178 (Lowers pKa of Tyr) are also active-site residues, they do not appear among the choices, so there is no competing correct option."
  },
  "important_caveats": [
    "The UniProt annotation for position 159 uses evidence code ECO:0000250 (inferred by similarity to P0C0Y5), meaning it is a computational transfer annotation, not direct experimental evidence (e.g., site-directed mutagenesis or crystallography) for this specific Aureobasidium enzyme.",
    "The protein is 266 residues long; choice D (position 342) is trivially impossible, making it an unusually easy distractor.",
    "The question stem asks to identify 'the enzyme's catalytic center' (singular), but the SDR catalytic center comprises multiple residues (Ser159, Tyr174, Lys178). Only Ser159 appears among the choices, so the question is effectively asking which single annotated active-site residue is correctly described.",
    "The entry was first public on 2025-02-05 with annotation updates through 2026-01-28; the author's source snapshot date is unknown, but the sequence has been stable since 2017-10-25 (sequence version 1)."
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

**Accession:** `A0A223HDI5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 15. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
"A0A223HDI5"
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32003433","source":"PubMed"}],"value":"1.1.1.138"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"NADP-dependent mannitol dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"MtDH"}]}}
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000250","id":"P0C0Y5","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":159},"start":{"modifier":"EXACT","value":159}},"type":"Active site"}
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)  
**Locator:** `lines 101-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.627063+00:00.  

```text
FT   ACT_SITE        159
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000250|UniProtKB:P0C0Y5"
```

Source SHA-256: `cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 16. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
