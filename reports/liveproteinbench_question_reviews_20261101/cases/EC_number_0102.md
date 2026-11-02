# EC_number_0102

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFSSLFVAACAAVTAFALPSELEKRAITTSQQGTSNGYFYSFWTNGGGSVSYNNGASGEYSVSWSNCGSFTSGKGWATGSSRNINFSGSFKPSGNAYLAVYGWTTSPLVEYYIMENYGDYNPGRSMTFKGTVTSDGSVYDIYTHQQVNQPSISGTATFEQYWSIRRTKRSSGTVTTANHFKAWASHGMYLGSHNYQIVSTEGYQSSGSSDITVS

[Multiple Choices]
A. 3.2.1.105
B. 1.1.1.195
C. 3.6.1.74
D. 3.2.1.8
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

> The exact sequence matches a UniProt entry annotated as endo-1,4-beta-xylanase with EC 3.2.1.8. The EC assignment and reaction are supported by a PROSITE-ProRule computational annotation, not by the cited experimental evidence; the available evidence therefore supports the key as an annotation but does not independently establish experimental confirmation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal signal peptide and sequence composition are compatible with a secreted fungal carbohydrate-active enzyme, making a hydrolase more plausible than the oxidoreductase or ATPase choices. Those broad features do not establish the specific substrate or EC subclass.


**Missing item-specific fact**

> The protein-specific identification as an endo-1,4-beta-xylanase, or equivalent family/homology or functional annotation linking this sequence to EC 3.2.1.8, is absent from the input.


**Reason**

> Choosing the precise EC requires protein-specific functional or family knowledge not established by the sequence's general features alone. Remembering the exact sequence's database annotation would be lookup or memorization, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence features alone do not confidently distinguish the exact EC, but the sequence-matched annotation supports D; no other option is supported by the supplied reviewer evidence.


### Important caveats

- Reviewer-only accession and database annotations were not supplied to the evaluated model.
- The EC evidence is computationally assigned by a PROSITE rule; cited publication evidence supports the protein name, not necessarily direct experimental verification of the catalytic classification.
- The exact author data snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal signal peptide and sequence composition are compatible with a secreted fungal carbohydrate-active enzyme, making a hydrolase more plausible than the oxidoreductase or ATPase choices. Those broad features do not establish the specific substrate or EC subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as an endo-1,4-beta-xylanase, or equivalent family/homology or functional annotation linking this sequence to EC 3.2.1.8, is absent from the input.",
    "reason": "Choosing the precise EC requires protein-specific functional or family knowledge not established by the sequence's general features alone. Remembering the exact sequence's database annotation would be lookup or memorization, not reasoning from supplied context."
  },
  "case_id": "EC_number_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as endo-1,4-beta-xylanase with EC 3.2.1.8. The EC assignment and reaction are supported by a PROSITE-ProRule computational annotation, not by the cited experimental evidence; the available evidence therefore supports the key as an annotation but does not independently establish experimental confirmation."
  },
  "important_caveats": [
    "Reviewer-only accession and database annotations were not supplied to the evaluated model.",
    "The EC evidence is computationally assigned by a PROSITE rule; cited publication evidence supports the protein name, not necessarily direct experimental verification of the catalytic classification.",
    "The exact author data snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features alone do not confidently distinguish the exact EC, but the sequence-matched annotation supports D; no other option is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as endo-1,4-beta-xylanase with EC 3.2.1.8. The EC assignment and reaction are supported by a PROSITE-ProRule computational annotation, not by the cited experimental evidence; the available evidence therefore supports the key as an annotation but does not independently establish experimental confirmation.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal signal peptide and sequence composition are compatible with a secreted fungal carbohydrate-active enzyme, making a hydrolase more plausible than the oxidoreductase or ATPase choices. Those broad features do not establish the specific substrate or EC subclass.",
    "missing_item_specific_fact": "The protein-specific identification as an endo-1,4-beta-xylanase, or equivalent family/homology or functional annotation linking this sequence to EC 3.2.1.8, is absent from the input.",
    "reason": "Choosing the precise EC requires protein-specific functional or family knowledge not established by the sequence's general features alone. Remembering the exact sequence's database annotation would be lookup or memorization, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features alone do not confidently distinguish the exact EC, but the sequence-matched annotation supports D; no other option is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "Reviewer-only accession and database annotations were not supplied to the evaluated model.",
    "The EC evidence is computationally assigned by a PROSITE rule; cited publication evidence supports the protein name, not necessarily direct experimental verification of the catalytic classification.",
    "The exact author data snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry K9GHZ3 (sequence exactly matched, 216 aa) annotates this protein as EC 3.2.1.8 (Endo-1,4-beta-xylanase) under the name 'Ethylene-inducing xylanase' (EIX) from Penicillium digitatum. The EC annotation carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097 (computational/PROSITE-ProRule annotation), and the catalytic activity is stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' Both current and historical (v51) records confirm EC 3.2.1.8.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 216-aa length is the strongest reasoning-based discriminator. GH11 endo-1,4-beta-xylanases (EC 3.2.1.8) are characteristically small (~200–250 aa) with a β-jelly-roll fold, whereas GH10 xylanases (EC 3.2.1.105) are typically 400+ aa with a (β/α)₈ TIM-barrel fold. The sequence also shows features consistent with a small fungal secreted glycoside hydrolase: an N-terminal signal peptide, high Ser/Thr/Gly/Asn/Trp content, and motifs (e.g., 'TATFEQ' and 'STEGY') plausibly corresponding to the two catalytic glutamates of a GH11 xylanase. Options B (oxidoreductase, EC 1.1.1.195) and C (nucleotide pyrophosphatase, EC 3.6.1.74) belong to entirely different enzyme classes and can be excluded by the glycoside-hydrolase-like composition and the absence of redox or nucleotide-binding motifs.


**Missing item-specific fact**

> Precise confirmation of the GH11 fold and catalytic mechanism would require structural data or site-directed mutagenesis; the PROSITE-ProRule annotation (PRU01097) is computational. However, the size-based and compositional arguments provide a defensible general-knowledge pathway to D.


**Reason**

> A knowledgeable model can use the small protein length (216 aa) to exclude GH10 (EC 3.2.1.105, typically 400+ aa), use the secreted fungal glycoside-hydrolase-like composition to exclude the oxidoreductase and nucleotide-hydrolase options, and arrive at EC 3.2.1.8. This constitutes a concrete biological argument grounded in general enzymology and structural biology, not mere memorization of this specific entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While A (3.2.1.105) and D (3.2.1.8) both describe endo-1,4-beta-xylanases, the 216-aa length strongly favors GH11 (D) over GH10 (A). B and C are different enzyme classes entirely. No other option is defensible given the sequence length and composition.


### Important caveats

- The EC 3.2.1.8 annotation is based on PROSITE-ProRule (ECO:0000255), a computational/pattern-based evidence code, not direct experimental characterization of this specific protein. The PubMed reference (39718348) supports the ethylene-inducing function and subcellular location but the EC assignment itself is rule-based.
- The protein is also known as 'Ethylene-inducing xylanase' (EIX), a pathogen-associated molecular pattern (PAMP) in Penicillium digitatum; its xylanase activity and its elicitor function are related but distinct biological roles.
- The distinction between EC 3.2.1.8 and EC 3.2.1.105 is purely structural (GH11 vs GH10 fold); both catalyze the same chemical reaction. A model relying solely on reaction chemistry could not distinguish them—only size/fold reasoning can.
- Reviewer-only UniProt evidence was not available to the evaluated model; the reasoning argument must be reconstructed from the raw sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 216-aa length is the strongest reasoning-based discriminator. GH11 endo-1,4-beta-xylanases (EC 3.2.1.8) are characteristically small (~200–250 aa) with a β-jelly-roll fold, whereas GH10 xylanases (EC 3.2.1.105) are typically 400+ aa with a (β/α)₈ TIM-barrel fold. The sequence also shows features consistent with a small fungal secreted glycoside hydrolase: an N-terminal signal peptide, high Ser/Thr/Gly/Asn/Trp content, and motifs (e.g., 'TATFEQ' and 'STEGY') plausibly corresponding to the two catalytic glutamates of a GH11 xylanase. Options B (oxidoreductase, EC 1.1.1.195) and C (nucleotide pyrophosphatase, EC 3.6.1.74) belong to entirely different enzyme classes and can be excluded by the glycoside-hydrolase-like composition and the absence of redox or nucleotide-binding motifs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise confirmation of the GH11 fold and catalytic mechanism would require structural data or site-directed mutagenesis; the PROSITE-ProRule annotation (PRU01097) is computational. However, the size-based and compositional arguments provide a defensible general-knowledge pathway to D.",
    "reason": "A knowledgeable model can use the small protein length (216 aa) to exclude GH10 (EC 3.2.1.105, typically 400+ aa), use the secreted fungal glycoside-hydrolase-like composition to exclude the oxidoreductase and nucleotide-hydrolase options, and arrive at EC 3.2.1.8. This constitutes a concrete biological argument grounded in general enzymology and structural biology, not mere memorization of this specific entry."
  },
  "case_id": "EC_number_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry K9GHZ3 (sequence exactly matched, 216 aa) annotates this protein as EC 3.2.1.8 (Endo-1,4-beta-xylanase) under the name 'Ethylene-inducing xylanase' (EIX) from Penicillium digitatum. The EC annotation carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097 (computational/PROSITE-ProRule annotation), and the catalytic activity is stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' Both current and historical (v51) records confirm EC 3.2.1.8."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation is based on PROSITE-ProRule (ECO:0000255), a computational/pattern-based evidence code, not direct experimental characterization of this specific protein. The PubMed reference (39718348) supports the ethylene-inducing function and subcellular location but the EC assignment itself is rule-based.",
    "The protein is also known as 'Ethylene-inducing xylanase' (EIX), a pathogen-associated molecular pattern (PAMP) in Penicillium digitatum; its xylanase activity and its elicitor function are related but distinct biological roles.",
    "The distinction between EC 3.2.1.8 and EC 3.2.1.105 is purely structural (GH11 vs GH10 fold); both catalyze the same chemical reaction. A model relying solely on reaction chemistry could not distinguish them—only size/fold reasoning can.",
    "Reviewer-only UniProt evidence was not available to the evaluated model; the reasoning argument must be reconstructed from the raw sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A (3.2.1.105) and D (3.2.1.8) both describe endo-1,4-beta-xylanases, the 216-aa length strongly favors GH11 (D) over GH10 (A). B and C are different enzyme classes entirely. No other option is defensible given the sequence length and composition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry K9GHZ3 (sequence exactly matched, 216 aa) annotates this protein as EC 3.2.1.8 (Endo-1,4-beta-xylanase) under the name 'Ethylene-inducing xylanase' (EIX) from Penicillium digitatum. The EC annotation carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097 (computational/PROSITE-ProRule annotation), and the catalytic activity is stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' Both current and historical (v51) records confirm EC 3.2.1.8.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 216-aa length is the strongest reasoning-based discriminator. GH11 endo-1,4-beta-xylanases (EC 3.2.1.8) are characteristically small (~200–250 aa) with a β-jelly-roll fold, whereas GH10 xylanases (EC 3.2.1.105) are typically 400+ aa with a (β/α)₈ TIM-barrel fold. The sequence also shows features consistent with a small fungal secreted glycoside hydrolase: an N-terminal signal peptide, high Ser/Thr/Gly/Asn/Trp content, and motifs (e.g., 'TATFEQ' and 'STEGY') plausibly corresponding to the two catalytic glutamates of a GH11 xylanase. Options B (oxidoreductase, EC 1.1.1.195) and C (nucleotide pyrophosphatase, EC 3.6.1.74) belong to entirely different enzyme classes and can be excluded by the glycoside-hydrolase-like composition and the absence of redox or nucleotide-binding motifs.",
    "missing_item_specific_fact": "Precise confirmation of the GH11 fold and catalytic mechanism would require structural data or site-directed mutagenesis; the PROSITE-ProRule annotation (PRU01097) is computational. However, the size-based and compositional arguments provide a defensible general-knowledge pathway to D.",
    "reason": "A knowledgeable model can use the small protein length (216 aa) to exclude GH10 (EC 3.2.1.105, typically 400+ aa), use the secreted fungal glycoside-hydrolase-like composition to exclude the oxidoreductase and nucleotide-hydrolase options, and arrive at EC 3.2.1.8. This constitutes a concrete biological argument grounded in general enzymology and structural biology, not mere memorization of this specific entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A (3.2.1.105) and D (3.2.1.8) both describe endo-1,4-beta-xylanases, the 216-aa length strongly favors GH11 (D) over GH10 (A). B and C are different enzyme classes entirely. No other option is defensible given the sequence length and composition."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation is based on PROSITE-ProRule (ECO:0000255), a computational/pattern-based evidence code, not direct experimental characterization of this specific protein. The PubMed reference (39718348) supports the ethylene-inducing function and subcellular location but the EC assignment itself is rule-based.",
    "The protein is also known as 'Ethylene-inducing xylanase' (EIX), a pathogen-associated molecular pattern (PAMP) in Penicillium digitatum; its xylanase activity and its elicitor function are related but distinct biological roles.",
    "The distinction between EC 3.2.1.8 and EC 3.2.1.105 is purely structural (GH11 vs GH10 fold); both catalyze the same chemical reaction. A model relying solely on reaction chemistry could not distinguish them—only size/fold reasoning can.",
    "Reviewer-only UniProt evidence was not available to the evaluated model; the reasoning argument must be reconstructed from the raw sequence and general biological knowledge."
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

**Accession:** `K9GHZ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"Ethylene-inducing xylanase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"EIX"}]}}
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:29:01.625551+00:00.  

```text
ID   EIX_PEND1               Reviewed;         216 AA.
AC   K9GHZ3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   06-FEB-2013, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:39718348};
DE            Short=EIX {ECO:0000303|PubMed:39718348};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:39718348};
DE   Flags: Precursor;
GN   Name=EIX {ECO:0000303|PubMed:39718348}; ORFNames=PDIP_02920;
OS   Penicillium digitatum (strain Pd1 / CECT 20795) (Green mold).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=1170230;
```

Source SHA-256: `c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:29:01.625551+00:00.  

```text
DE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:39718348};
DE            Short=EIX {ECO:0000303|PubMed:39718348};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:39718348};
DE   Flags: Precursor;
```

Source SHA-256: `c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)  
**Locator:** `lines 41-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:29:01.625551+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};
```

Source SHA-256: `c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 102. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
