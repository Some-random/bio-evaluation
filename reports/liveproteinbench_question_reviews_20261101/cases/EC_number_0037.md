# EC_number_0037

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 7.6.2.2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGKEQKEKKDGNLSIKEEVEKELNKKSTAELFRKIKNEKISFFLPFKCLPAQHRKLLFISFVCAVLSGGTLPFFISVFGVILKNMNLGDDINPIILSLVSIGLVQFILSMISSYCMDVITSKILKTLKLEYLRSVFYQDGQFHDNNPGSKLRSDLDFYLEQVSSGIGTKFITIFTYASSFLGLYIWSLIKNARLTLCITCVFPLIYVCGVICNKKVKLNKKTSLLYNNNTMSIIEEALMGIRTVASYCGEKTILNKFNLSETFYSKYILKANFVEALHIGLINGLILVSYAFGFWYGTRIIINSATNQYPNNDFNGASVISILLGVLISMFMLTIILPNITEYMKALEATNSLYEIINRKPLVENNDDGETLPNIKKIEFKNVRFHYDTRKDVEIYKDLSFTLKEGKTYAFVGESGCGKSTILKLIERLYDPTEGDIIVNDSHNLKDINLKWWRSKIGVVSQDPLLFSNSIKNNIKYSLYSLKDLEAMENYYEENTNDTYENKNFSLISNSMTSNELLEMKKEYQTIKDSDVVDVSKKVLIHDFVSSLPDKYDTLVGSNASKLSGGQKQRISIARAIMRNPKILILDEATSSLDNKSEYLVQKTINNLKGNENRITIIIAHRLSTIRYANTIFVLSNRERSDNNNNNNNDDNNNNNNNNNNKINNEGSYIIEQGTHDSLMKNKNGIYHLMINNQKISSNKSSNNGNDNGSDNKSSAYKDSDTGNDADNMNSLSIHENENISNNRNCKNTAENEKEEKVPFFKRMFRRKKKAPNNLRIIYKEIFSYKKDVTIIFFSILVAGGLYPVFALLYARYVSTLFDFANLEYNSNKYSIYILLIAIAMFISETLKNYYNNKIGEKVEKTMKRRLFENILYQEMSFFDQDKNTPGVLSAHINRDVHLLKTGLVNNIVIFSHFIMLFLVSMVMSFYFCPIVAAVLTFIYFINMRVFAVRARLTKSKEIEKKENMSSGVFAFSSDDEMFKDPSFLIQEAFYNMHTVINYGLEDYFCNLIEKAIDYKNKGQKRRIIVNAALWGFSQSAQLFINSFAYWFGSFLIKRGTILVDDFMKSLFTFIFTGSYAGKLMSLKGDSENAKLSFEKYYPLMIRKSNIDVRDDGGIRINKNLIKGKVDIKDVNFRYISRPNVPIYKNLSFTCDSKKTTAIVGETGSGKSTFMNLLLRFYDLKNDHIILKNDMTNFQDYQNNNNNSLVLKNVNEFSNQSGSAEDYTVFNNNGEILLDDINICDYNLRDLRNLFSIVSQEPMLFNMSIYENIKFGREDATLEDVKRVSKFAAIDEFIESLPNKYDTNVGPYGKSLSGGQKQRIAIARALLREPKILLLDEATSSLDSNSEKLIEKTIVDIKDKADKTIITIAHRIASIKRSDKIVVFNNPDRNGTFVQSHGTHDELLSAQDGIYKKYVKLAK

[Multiple Choices]
A. 7.6.2.2
B. 6.3.5.1
C. 1.14.13.247
D. 3.1.1.4
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

> The sequence matches the UniProt entry for PfMDR1, whose EC 7.6.2.2 annotation is linked to experimental evidence codes and a catalytic reaction describing ATP-driven xenobiotic transport.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple transmembrane regions and two ABC nucleotide-binding domains with ATP-binding motifs, supporting an ATP-powered membrane transporter. That architecture meaningfully favors the transporter option over the ligase, oxidoreductase, and hydrolase choices.


**Missing item-specific fact**

> The exact transported substrate range and protein-specific EC assignment are not stated in the input; the sequence architecture supports the transporter class but does not independently establish every detail of its annotation.


**Reason**

> The supplied sequence provides strong biological grounds to distinguish the ATP-dependent transporter choice among these options, even though its exact substrate specificity is protein-specific.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The two-transmembrane-domain ABC transporter architecture is inconsistent with the broad enzyme classes represented by the other choices.


### Important caveats

- The supporting UniProt annotation is reviewer-only and was not supplied to the model.
- The experimental support cited in the annotation supports the expected EC assignment, but the underlying primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple transmembrane regions and two ABC nucleotide-binding domains with ATP-binding motifs, supporting an ATP-powered membrane transporter. That architecture meaningfully favors the transporter option over the ligase, oxidoreductase, and hydrolase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact transported substrate range and protein-specific EC assignment are not stated in the input; the sequence architecture supports the transporter class but does not independently establish every detail of its annotation.",
    "reason": "The supplied sequence provides strong biological grounds to distinguish the ATP-dependent transporter choice among these options, even though its exact substrate specificity is protein-specific."
  },
  "case_id": "EC_number_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for PfMDR1, whose EC 7.6.2.2 annotation is linked to experimental evidence codes and a catalytic reaction describing ATP-driven xenobiotic transport."
  },
  "important_caveats": [
    "The supporting UniProt annotation is reviewer-only and was not supplied to the model.",
    "The experimental support cited in the annotation supports the expected EC assignment, but the underlying primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The two-transmembrane-domain ABC transporter architecture is inconsistent with the broad enzyme classes represented by the other choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for PfMDR1, whose EC 7.6.2.2 annotation is linked to experimental evidence codes and a catalytic reaction describing ATP-driven xenobiotic transport.",
    "evidence_ids": ["C1", "C4", "C5", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple transmembrane regions and two ABC nucleotide-binding domains with ATP-binding motifs, supporting an ATP-powered membrane transporter. That architecture meaningfully favors the transporter option over the ligase, oxidoreductase, and hydrolase choices.",
    "missing_item_specific_fact": "The exact transported substrate range and protein-specific EC assignment are not stated in the input; the sequence architecture supports the transporter class but does not independently establish every detail of its annotation.",
    "reason": "The supplied sequence provides strong biological grounds to distinguish the ATP-dependent transporter choice among these options, even though its exact substrate specificity is protein-specific."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The two-transmembrane-domain ABC transporter architecture is inconsistent with the broad enzyme classes represented by the other choices."
  },
  "important_caveats": [
    "The supporting UniProt annotation is reviewer-only and was not supplied to the model.",
    "The experimental support cited in the annotation supports the expected EC assignment, but the underlying primary studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q7K6A5 (sequence matched exactly, 1419 AA) annotates this protein (Plasmodium falciparum Multidrug Resistance Protein 1 / P-glycoprotein homolog) with EC 7.6.2.2, supported by experimental evidence codes ECO:0000269 from PubMed:35507548 and PubMed:37527341. The catalytic activity (ATP + H2O + xenobiotic&#91;Side 1&#93; = ADP + phosphate + xenobiotic&#91;Side 2&#93;) is consistent with P-type xenobiotic transporter activity. Both current and historical (entry version 159) records confirm this annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two nucleotide-binding domains with Walker A motifs (GESGCGKST, GETGSGKST), Walker B motifs (DEATSS), and ABC signature motifs (LSGGQKQR), plus multiple transmembrane helices — the canonical architecture of a full-type ABC transporter. Among the four choices, only EC 7.6.2.2 (P-type xenobiotic transporter) belongs to the ABC transporter / translocase class (EC 7). The other options are glutamine synthase (EC 6.3.5.1, ligase), a monooxygenase (EC 1.14.13.247, oxidoreductase), and phospholipase A2 (EC 3.1.1.4, hydrolase) — none of which share the two-NBD/two-TMD architecture. Recognizing ABC transporter features from sequence motifs and mapping to the EC 7 translocase class is achievable through general enzymology knowledge.


**Missing item-specific fact**

> None critical. Distinguishing 7.6.2.2 from other EC 7.6.2.x sub-numbers would require knowing the substrate class (xenobiotic vs. phospholipid vs. peptide), but the distractors are from entirely different EC top-level classes, so that finer distinction is not needed here.


**Reason**

> The sequence provides clear ABC transporter hallmarks (paired NBDs with Walker A/B and signature motifs, multiple TMDs). A model with general enzyme-class knowledge can identify the protein as an ABC-type translocase and select the only EC 7 option, eliminating the ligase, oxidoreductase, and hydrolase distractors without needing to memorize the specific PfMDR1 entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors belong to completely different EC top-level classes (6, 1, 3) and catalyze mechanistically unrelated reactions. The sequence unambiguously encodes an ABC transporter, so only EC 7.6.2.2 is defensible.


### Important caveats

- EC 7.6.2.2 is a relatively recent reclassification (2018 EC revision moved P-glycoprotein-type transporters from EC 3.6.3.44 to EC 7.6.2.2). A model trained on older EC numbering might not associate the translocase class with '7.'
- The specific assignment to 7.6.2.2 (xenobiotic) rather than 7.6.2.1 (phospholipid) or 7.6.2.3 relies on substrate specificity data not derivable from sequence alone, but this distinction is not tested by the given distractors.
- The evidence is from UniProt annotation backed by experimental studies (cryo-EM structures, ATPase assays), not purely computational inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two nucleotide-binding domains with Walker A motifs (GESGCGKST, GETGSGKST), Walker B motifs (DEATSS), and ABC signature motifs (LSGGQKQR), plus multiple transmembrane helices — the canonical architecture of a full-type ABC transporter. Among the four choices, only EC 7.6.2.2 (P-type xenobiotic transporter) belongs to the ABC transporter / translocase class (EC 7). The other options are glutamine synthase (EC 6.3.5.1, ligase), a monooxygenase (EC 1.14.13.247, oxidoreductase), and phospholipase A2 (EC 3.1.1.4, hydrolase) — none of which share the two-NBD/two-TMD architecture. Recognizing ABC transporter features from sequence motifs and mapping to the EC 7 translocase class is achievable through general enzymology knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Distinguishing 7.6.2.2 from other EC 7.6.2.x sub-numbers would require knowing the substrate class (xenobiotic vs. phospholipid vs. peptide), but the distractors are from entirely different EC top-level classes, so that finer distinction is not needed here.",
    "reason": "The sequence provides clear ABC transporter hallmarks (paired NBDs with Walker A/B and signature motifs, multiple TMDs). A model with general enzyme-class knowledge can identify the protein as an ABC-type translocase and select the only EC 7 option, eliminating the ligase, oxidoreductase, and hydrolase distractors without needing to memorize the specific PfMDR1 entry."
  },
  "case_id": "EC_number_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q7K6A5 (sequence matched exactly, 1419 AA) annotates this protein (Plasmodium falciparum Multidrug Resistance Protein 1 / P-glycoprotein homolog) with EC 7.6.2.2, supported by experimental evidence codes ECO:0000269 from PubMed:35507548 and PubMed:37527341. The catalytic activity (ATP + H2O + xenobiotic[Side 1] = ADP + phosphate + xenobiotic[Side 2]) is consistent with P-type xenobiotic transporter activity. Both current and historical (entry version 159) records confirm this annotation."
  },
  "important_caveats": [
    "EC 7.6.2.2 is a relatively recent reclassification (2018 EC revision moved P-glycoprotein-type transporters from EC 3.6.3.44 to EC 7.6.2.2). A model trained on older EC numbering might not associate the translocase class with '7.'",
    "The specific assignment to 7.6.2.2 (xenobiotic) rather than 7.6.2.1 (phospholipid) or 7.6.2.3 relies on substrate specificity data not derivable from sequence alone, but this distinction is not tested by the given distractors.",
    "The evidence is from UniProt annotation backed by experimental studies (cryo-EM structures, ATPase assays), not purely computational inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors belong to completely different EC top-level classes (6, 1, 3) and catalyze mechanistically unrelated reactions. The sequence unambiguously encodes an ABC transporter, so only EC 7.6.2.2 is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q7K6A5 (sequence matched exactly, 1419 AA) annotates this protein (Plasmodium falciparum Multidrug Resistance Protein 1 / P-glycoprotein homolog) with EC 7.6.2.2, supported by experimental evidence codes ECO:0000269 from PubMed:35507548 and PubMed:37527341. The catalytic activity (ATP + H2O + xenobiotic[Side 1] = ADP + phosphate + xenobiotic[Side 2]) is consistent with P-type xenobiotic transporter activity. Both current and historical (entry version 159) records confirm this annotation.",
    "evidence_ids": ["C4", "C5", "H2", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two nucleotide-binding domains with Walker A motifs (GESGCGKST, GETGSGKST), Walker B motifs (DEATSS), and ABC signature motifs (LSGGQKQR), plus multiple transmembrane helices — the canonical architecture of a full-type ABC transporter. Among the four choices, only EC 7.6.2.2 (P-type xenobiotic transporter) belongs to the ABC transporter / translocase class (EC 7). The other options are glutamine synthase (EC 6.3.5.1, ligase), a monooxygenase (EC 1.14.13.247, oxidoreductase), and phospholipase A2 (EC 3.1.1.4, hydrolase) — none of which share the two-NBD/two-TMD architecture. Recognizing ABC transporter features from sequence motifs and mapping to the EC 7 translocase class is achievable through general enzymology knowledge.",
    "missing_item_specific_fact": "None critical. Distinguishing 7.6.2.2 from other EC 7.6.2.x sub-numbers would require knowing the substrate class (xenobiotic vs. phospholipid vs. peptide), but the distractors are from entirely different EC top-level classes, so that finer distinction is not needed here.",
    "reason": "The sequence provides clear ABC transporter hallmarks (paired NBDs with Walker A/B and signature motifs, multiple TMDs). A model with general enzyme-class knowledge can identify the protein as an ABC-type translocase and select the only EC 7 option, eliminating the ligase, oxidoreductase, and hydrolase distractors without needing to memorize the specific PfMDR1 entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors belong to completely different EC top-level classes (6, 1, 3) and catalyze mechanistically unrelated reactions. The sequence unambiguously encodes an ABC transporter, so only EC 7.6.2.2 is defensible."
  },
  "important_caveats": [
    "EC 7.6.2.2 is a relatively recent reclassification (2018 EC revision moved P-glycoprotein-type transporters from EC 3.6.3.44 to EC 7.6.2.2). A model trained on older EC numbering might not associate the translocase class with '7.'",
    "The specific assignment to 7.6.2.2 (xenobiotic) rather than 7.6.2.1 (phospholipid) or 7.6.2.3 relies on substrate specificity data not derivable from sequence alone, but this distinction is not tested by the given distractors.",
    "The evidence is from UniProt annotation backed by experimental studies (cryo-EM structures, ATPase assays), not purely computational inference."
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

**Accession:** `Q7K6A5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 159. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
"Q7K6A5"
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"1674943","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"8097560","source":"PubMed"}],"value":"P-glycoprotein homolog"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"1674943","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"8097560","source":"PubMed"}],"value":"PGH1"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"37527341","source":"PubMed"}],"value":"7.6.2.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"1674943","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"37527341","source":"PubMed"}],"value":"Multidrug resistance protein 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"1674943","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"37527341","source":"PubMed"}],"value":"PfMDR1"}]}}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"7.6.2.2","evidences":[{"evidenceCode":"ECO:0000269","id":"35507548","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"37527341","source":"PubMed"}],"name":"ATP + H2O + xenobioticSide 1 = ADP + phosphate + xenobioticSide 2."}}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
DE   RecName: Full=Multidrug resistance protein 1 {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:37527341};
DE            Short=PfMDR1 {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:37527341};
DE            EC=7.6.2.2 {ECO:0000269|PubMed:37527341};
DE   AltName: Full=P-glycoprotein homolog {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:8097560};
DE            Short=PGH1 {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:8097560};
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 89-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP + H2O + xenobioticSide 1 = ADP + phosphate +
CC         xenobioticSide 2.; EC=7.6.2.2; Evidence={ECO:0000269|PubMed:35507548,
CC         ECO:0000269|PubMed:37527341};
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
