# active_site_0106

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **A** — Position 237 (Proton donor)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| contradicted | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MTGFLPEPLRMLVTSPALLDFTSDGPLPYALRQKFTGKPPPVTSNLSLASQTVLVTGATSGVGLEAARQLAQLGPRLLILGVRNASKAEQIKSELERDTPNLTVQVAELDLESLLSVDRFVDELSANSIRLDLALLNAGFFAHDDRITDDGYSPLFQVNFLSTAYLTLKLLPLLHTTAPPHPPGTTTPPGPRLVLVTSEAHAWTTFPDVPRPTENRTQPILSVFQDKNTLGSADDQYARAKLLLALFGKELSRRLTAAENDTTVVITTPGFCASNFFPDGMMTRLIQLTSARSVQQGGALHVFAATAPGPEIHGAYLRDGKPTGLSKFAQGPQGQILQERLWGEMEEFFMQRGGSPLGM

[Multiple Choices]
A. Position 237 (Proton donor)
B. Position 154 (Acyl-thioester intermediate)
C. Position 458 (For beta-ketoacyl synthase activity)
D. Position 215 (Charge relay system)
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

## Luna’s full visible review

### Expected-answer support: contradicted

> The supplied sequence has leucine at position 237, whose side chain is not a plausible catalytic proton donor. UniProt annotates that position as a proton donor, but the feature is transferred by similarity from another protein, not direct experimental evidence for this sequence; the annotation conflicts with the residue identity.

Cited evidence: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a dehydrogenase, which makes a proton-donor role broadly plausible, but it does not provide a defensible basis for assigning that role to position 237; that residue is leucine.

**Missing item-specific fact**

> A reliable, sequence-specific experimental or validated annotation of the active-site residues is absent. The available position-237 annotation is homology-transferred and conflicts with the sequence residue.

**Reason**

> Identifying a precise active-site position requires protein-specific information not established by the prompt. Recognizing a broad enzyme family or using generic catalytic-residue patterns cannot justify the listed position.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The sequence does not support the keyed proton-donor assignment at position 237, and no other option is established by the supplied information. Position 458 also lies beyond the 359-residue sequence.

### Important caveats

- The database annotation explicitly labels position 237 as a proton donor, but its evidence is transferred from UniProtKB:O93868 rather than shown to be experimentally verified in this protein.
- The sequence match and annotation do not resolve the discrepancy between the annotated role and leucine at position 237.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "active_site_0106",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The supplied sequence has leucine at position 237, whose side chain is not a plausible catalytic proton donor. UniProt annotates that position as a proton donor, but the feature is transferred by similarity from another protein, not direct experimental evidence for this sequence; the annotation conflicts with the residue identity.",
    "evidence_ids": [
      "C5",
      "H3"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a dehydrogenase, which makes a proton-donor role broadly plausible, but it does not provide a defensible basis for assigning that role to position 237; that residue is leucine.",
    "missing_item_specific_fact": "A reliable, sequence-specific experimental or validated annotation of the active-site residues is absent. The available position-237 annotation is homology-transferred and conflicts with the sequence residue.",
    "reason": "Identifying a precise active-site position requires protein-specific information not established by the prompt. Recognizing a broad enzyme family or using generic catalytic-residue patterns cannot justify the listed position."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not support the keyed proton-donor assignment at position 237, and no other option is established by the supplied information. Position 458 also lies beyond the 359-residue sequence."
  },
  "important_caveats": [
    "The database annotation explicitly labels position 237 as a proton donor, but its evidence is transferred from UniProtKB:O93868 rather than shown to be experimentally verified in this protein.",
    "The sequence match and annotation do not resolve the discrepancy between the annotated role and leucine at position 237."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `model_residue_identity_error`.

> The original frozen sequence uses1-based Y237, not leucine. C5/H3 annotate237 as proton donor by similarity. The model contradiction argument relies on a false residue identity.

**Remaining uncertainty:** This invalidates that stated argument only; the similarity-transferred active-site annotation is not direct validation of the exact residue function.

**Direct check of the original sequence:**

```json
{
  "indexing": "1-based",
  "length": 359,
  "residues": {
    "237": "Y"
  },
  "sha256": "00a67859bfb5799f648543ed75c5168c3c4cc678d78363e0f961ad4cc8caaf9d"
}
```

Evidence checked: [C5](#evidence-c5), [H3](#evidence-h3).

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `P0DXW2`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 3. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:52.717483+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000250","id":"O93868","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":237},"start":{"modifier":"EXACT","value":237}},"type":"Active site"}
```

Source SHA-256: `49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)  
**Locator:** `lines 60-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:57.835506+00:00.  

```text
FT   ACT_SITE        237
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000250|UniProtKB:O93868"
```

Source SHA-256: `4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json) (zero-based source row 106). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
