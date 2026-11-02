# catalytic_activity_0047

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — ATP + H2O = ADP + phosphate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDSQQSVEVLNQLLARLSVATPDNRDEVATEVSSFVNGNIIEHDAPEHFFNGLAKAIKDKKSAVNALAAVSHVASTSGLAPSVEPYVVALVPAILEQTGSKDKDVQSAANAALHAVVTAVNPVAVKAVLPHLTKSLSETNKWQEKVAVLSAISALVDQAKSQISLRMTELIPVLSEAMWDTKKEVKNAATATMTKATETVENKDIERFIPKLIECIANPSEVPETVHLLGATTFVAEVTPATLSIMTPLLSRGLAERETPIKRKSAVIIDNMCKLVEDPQIVAPFLNKLLPGLKNNFSVIADPEAREVTLRGLKTLRRVGAVGEGDVLPEISHAGDPATTLGVLDSLLKTENIAKKFRPAVEYISCIGGDLIDERIIDQQTWFTHVLPYMTIFLHQNQAKEILDEFRKRAVDNIPEPPKFDDEEEEGEDLCNCEFSLAYGAKILLNRTQLRLKRGRRYGLCGPNGSGKSTLMRAIANGQVDGFPSQEECRTVYVEHDIDGTHAETSVLDFVFQGDVGTKEAISAKLKEFGFDDEMIVMPIAALSGGWKMKLALARAVLKNADILLLDEPTNHLDTVNVAWLTNYLITCGITSIVVSHDSGFLDNICQYIIHYEGLKLRKYKGNLSALVERVPSAKSYYELGASDLEFRFPEPGYLEGVKTKQKAIVKVSNMTFQYPGTSKPQISDVSFQCSLSSRIAVIGPNGAGKSTLINVLTGELLPTTGEVYTHENIRIAYIKQHAFAHIESHLDKTPSEYIQWRFQTGEDRETMDRANRQINEDDAQAMNKIFKIDGTPRRIAGIHSRRKFKNSYEYECSFLLGENIGMKSERWVPMMSVDNAWLPRGEVIESHGKMVAEVDMKEALASGQFRPLTRKEIEEHCAMLGLDAELVSHSRIRGLSGGQKVKLVLAAGTWQRPHLIVLDEPTNYLDRDSLGALSKALKEFEGGVIIITHSAEFTKDLTEEVWAVRDGLMTPSGHNWVSGQGSGPRLEKKEDEEDKFDAMGNKISSGTKKTKLSSAELRKKKKERMKKKKELGDAYVSDDDADF

[Multiple Choices]
A. (2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O
B. ATP + H2O = ADP + phosphate + H(+)
C. beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)
D. L-leucine(in) = L-leucine(out)
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

> The exact sequence matches UniProt entry C5E4D9, annotated as elongation factor 3 with ATP + H2O = ADP + phosphate + H(+). The catalytic-activity annotation is transferred by similarity from UniProtKB:P16521 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two P-loop NTPase-like motifs, GPNGSGKST and GPNGAGKST, consistent with ATP-binding domains and supporting an ATP-hydrolyzing protein. The long soluble sequence lacks the transmembrane features expected for leucine transport and does not suggest the specialized chemistry in A or C; among these choices, ATP hydrolysis is the meaningful fit.


**Missing item-specific fact**

> No item-specific fact is necessary to distinguish these broad choices. Identifying the exact protein as elongation factor 3 or establishing its experimentally measured activity would require information not supplied.


**Reason**

> The sequence motifs and overall protein character provide a concrete biological basis for selecting the ATP-hydrolysis reaction over the alternatives, without needing to recognize the exact database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed reactions, ATP hydrolysis is the only one coherently supported by the sequence's repeated P-loop NTPase-like motifs.


### Important caveats

- The reviewer-only UniProt record matches the supplied sequence, but its catalytic-activity evidence is transferred from a homolog rather than presented as direct experimental evidence for this exact protein.
- The sequence-based argument supports distinguishing these choices; it does not independently establish every mechanistic detail of the protein's activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two P-loop NTPase-like motifs, GPNGSGKST and GPNGAGKST, consistent with ATP-binding domains and supporting an ATP-hydrolyzing protein. The long soluble sequence lacks the transmembrane features expected for leucine transport and does not suggest the specialized chemistry in A or C; among these choices, ATP hydrolysis is the meaningful fit.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is necessary to distinguish these broad choices. Identifying the exact protein as elongation factor 3 or establishing its experimentally measured activity would require information not supplied.",
    "reason": "The sequence motifs and overall protein character provide a concrete biological basis for selecting the ATP-hydrolysis reaction over the alternatives, without needing to recognize the exact database entry."
  },
  "case_id": "catalytic_activity_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry C5E4D9, annotated as elongation factor 3 with ATP + H2O = ADP + phosphate + H(+). The catalytic-activity annotation is transferred by similarity from UniProtKB:P16521 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact sequence."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the supplied sequence, but its catalytic-activity evidence is transferred from a homolog rather than presented as direct experimental evidence for this exact protein.",
    "The sequence-based argument supports distinguishing these choices; it does not independently establish every mechanistic detail of the protein's activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, ATP hydrolysis is the only one coherently supported by the sequence's repeated P-loop NTPase-like motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry C5E4D9, annotated as elongation factor 3 with ATP + H2O = ADP + phosphate + H(+). The catalytic-activity annotation is transferred by similarity from UniProtKB:P16521 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two P-loop NTPase-like motifs, GPNGSGKST and GPNGAGKST, consistent with ATP-binding domains and supporting an ATP-hydrolyzing protein. The long soluble sequence lacks the transmembrane features expected for leucine transport and does not suggest the specialized chemistry in A or C; among these choices, ATP hydrolysis is the meaningful fit.",
    "missing_item_specific_fact": "No item-specific fact is necessary to distinguish these broad choices. Identifying the exact protein as elongation factor 3 or establishing its experimentally measured activity would require information not supplied.",
    "reason": "The sequence motifs and overall protein character provide a concrete biological basis for selecting the ATP-hydrolysis reaction over the alternatives, without needing to recognize the exact database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, ATP hydrolysis is the only one coherently supported by the sequence's repeated P-loop NTPase-like motifs."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the supplied sequence, but its catalytic-activity evidence is transferred from a homolog rather than presented as direct experimental evidence for this exact protein.",
    "The sequence-based argument supports distinguishing these choices; it does not independently establish every mechanistic detail of the protein's activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C5, H3) confirms UniProt C5E4D9 (EF-3 from Zygosaccharomyces rouxii) is annotated with catalytic activity 'ATP + H2O = ADP + phosphate + H(+)' (EC 3.6.4.-). The evidence code is ECO:0000250 (inferred by similarity from P16521, S. cerevisiae EF-3), a computational transfer rather than direct experimental measurement. However, the sequence itself contains two canonical Walker A motifs (GLCGPNGSGKSTLMRAI and IGPNGAGKSTLINVLTG) and multiple Walker B motifs (DEPTNHLDT, DEPTNYLDR, DEEDK), which are hallmark P-loop NTPase signatures consistent with ATP hydrolysis. The EC class 3.6.4.- (ATPases acting on other compounds) is appropriate for EF-3's role in translation elongation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two textbook Walker A (P-loop) motifs with the consensus GxGxxGKST (GSGKST and GAGKST) and multiple Walker B motifs (hhhhDE: DEPTNHLDT, DEPTNYLDR, DEEDK), which are universal structural signatures of P-loop NTPases/ATPases. These motifs are directly identifiable from the sequence and indicate ATP hydrolysis capability. Additionally, the absence of cytochrome P450 heme-binding motifs (FxxGxRxCxG) rules out option C; the absence of dihydroxy-acid dehydratase catalytic residues rules out option A; and critically, the absence of transmembrane helices (no long hydrophobic stretches typical of membrane-spanning domains) rules out option D (a membrane amino acid transporter), even though the NBD architecture superficially resembles ABC transporters. EF-3 is an ABC-superfamily member lacking a TMD, functioning as a translation factor that hydrolyzes ATP.


**Missing item-specific fact**

> None critical. The Walker A/B motif recognition and the absence of TMDs are general biochemical knowledge. The specific identity as EF-3 would require database lookup, but the functional class (ATPase) is inferable from sequence features alone.


**Reason**

> A model with knowledge of P-loop NTPase structural signatures can identify the Walker A and Walker B motifs directly in the sequence, concluding ATPase activity (option B). The absence of transmembrane domains distinguishes it from a transporter (option D), and the absence of heme-binding or dehydratase motifs eliminates options C and A. This constitutes a concrete, sequence-grounded biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While option D (leucine transport) might initially seem plausible due to the ABC-transporter-like NBD architecture, the absence of transmembrane domains and the presence of two tandem NBDs (characteristic of translation factors like EF-3 rather than membrane transporters) provide a clear discriminator. Options A and C lack any supporting sequence features. Only B is consistent with the identifiable P-loop NTPase motifs.


### Important caveats

- The UniProt annotation uses ECO:0000250 (inferred by similarity from P16521), not direct experimental evidence. However, the sequence features (Walker A/B motifs) independently support the ATPase assignment.
- The EC number 3.6.4.- is incomplete (no final digit assigned), reflecting that EF-3's precise mechanism within the ABC superfamily is still being characterized.
- The protein is a fungal-specific translation factor (EF-3), absent from animals and plants, making it less familiar to general-trained models, but the sequence motifs remain identifiable.
- The sequence-match is exact (SHA256 confirmed) between the benchmark input and the UniProt entry C5E4D9.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two textbook Walker A (P-loop) motifs with the consensus GxGxxGKST (GSGKST and GAGKST) and multiple Walker B motifs (hhhhDE: DEPTNHLDT, DEPTNYLDR, DEEDK), which are universal structural signatures of P-loop NTPases/ATPases. These motifs are directly identifiable from the sequence and indicate ATP hydrolysis capability. Additionally, the absence of cytochrome P450 heme-binding motifs (FxxGxRxCxG) rules out option C; the absence of dihydroxy-acid dehydratase catalytic residues rules out option A; and critically, the absence of transmembrane helices (no long hydrophobic stretches typical of membrane-spanning domains) rules out option D (a membrane amino acid transporter), even though the NBD architecture superficially resembles ABC transporters. EF-3 is an ABC-superfamily member lacking a TMD, functioning as a translation factor that hydrolyzes ATP.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The Walker A/B motif recognition and the absence of TMDs are general biochemical knowledge. The specific identity as EF-3 would require database lookup, but the functional class (ATPase) is inferable from sequence features alone.",
    "reason": "A model with knowledge of P-loop NTPase structural signatures can identify the Walker A and Walker B motifs directly in the sequence, concluding ATPase activity (option B). The absence of transmembrane domains distinguishes it from a transporter (option D), and the absence of heme-binding or dehydratase motifs eliminates options C and A. This constitutes a concrete, sequence-grounded biological argument."
  },
  "case_id": "catalytic_activity_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, H3) confirms UniProt C5E4D9 (EF-3 from Zygosaccharomyces rouxii) is annotated with catalytic activity 'ATP + H2O = ADP + phosphate + H(+)' (EC 3.6.4.-). The evidence code is ECO:0000250 (inferred by similarity from P16521, S. cerevisiae EF-3), a computational transfer rather than direct experimental measurement. However, the sequence itself contains two canonical Walker A motifs (GLCGPNGSGKSTLMRAI and IGPNGAGKSTLINVLTG) and multiple Walker B motifs (DEPTNHLDT, DEPTNYLDR, DEEDK), which are hallmark P-loop NTPase signatures consistent with ATP hydrolysis. The EC class 3.6.4.- (ATPases acting on other compounds) is appropriate for EF-3's role in translation elongation."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000250 (inferred by similarity from P16521), not direct experimental evidence. However, the sequence features (Walker A/B motifs) independently support the ATPase assignment.",
    "The EC number 3.6.4.- is incomplete (no final digit assigned), reflecting that EF-3's precise mechanism within the ABC superfamily is still being characterized.",
    "The protein is a fungal-specific translation factor (EF-3), absent from animals and plants, making it less familiar to general-trained models, but the sequence motifs remain identifiable.",
    "The sequence-match is exact (SHA256 confirmed) between the benchmark input and the UniProt entry C5E4D9."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option D (leucine transport) might initially seem plausible due to the ABC-transporter-like NBD architecture, the absence of transmembrane domains and the presence of two tandem NBDs (characteristic of translation factors like EF-3 rather than membrane transporters) provide a clear discriminator. Options A and C lack any supporting sequence features. Only B is consistent with the identifiable P-loop NTPase motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, H3) confirms UniProt C5E4D9 (EF-3 from Zygosaccharomyces rouxii) is annotated with catalytic activity 'ATP + H2O = ADP + phosphate + H(+)' (EC 3.6.4.-). The evidence code is ECO:0000250 (inferred by similarity from P16521, S. cerevisiae EF-3), a computational transfer rather than direct experimental measurement. However, the sequence itself contains two canonical Walker A motifs (GLCGPNGSGKSTLMRAI and IGPNGAGKSTLINVLTG) and multiple Walker B motifs (DEPTNHLDT, DEPTNYLDR, DEEDK), which are hallmark P-loop NTPase signatures consistent with ATP hydrolysis. The EC class 3.6.4.- (ATPases acting on other compounds) is appropriate for EF-3's role in translation elongation.",
    "evidence_ids": ["C5", "H3", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two textbook Walker A (P-loop) motifs with the consensus GxGxxGKST (GSGKST and GAGKST) and multiple Walker B motifs (hhhhDE: DEPTNHLDT, DEPTNYLDR, DEEDK), which are universal structural signatures of P-loop NTPases/ATPases. These motifs are directly identifiable from the sequence and indicate ATP hydrolysis capability. Additionally, the absence of cytochrome P450 heme-binding motifs (FxxGxRxCxG) rules out option C; the absence of dihydroxy-acid dehydratase catalytic residues rules out option A; and critically, the absence of transmembrane helices (no long hydrophobic stretches typical of membrane-spanning domains) rules out option D (a membrane amino acid transporter), even though the NBD architecture superficially resembles ABC transporters. EF-3 is an ABC-superfamily member lacking a TMD, functioning as a translation factor that hydrolyzes ATP.",
    "missing_item_specific_fact": "None critical. The Walker A/B motif recognition and the absence of TMDs are general biochemical knowledge. The specific identity as EF-3 would require database lookup, but the functional class (ATPase) is inferable from sequence features alone.",
    "reason": "A model with knowledge of P-loop NTPase structural signatures can identify the Walker A and Walker B motifs directly in the sequence, concluding ATPase activity (option B). The absence of transmembrane domains distinguishes it from a transporter (option D), and the absence of heme-binding or dehydratase motifs eliminates options C and A. This constitutes a concrete, sequence-grounded biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option D (leucine transport) might initially seem plausible due to the ABC-transporter-like NBD architecture, the absence of transmembrane domains and the presence of two tandem NBDs (characteristic of translation factors like EF-3 rather than membrane transporters) provide a clear discriminator. Options A and C lack any supporting sequence features. Only B is consistent with the identifiable P-loop NTPase motifs."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000250 (inferred by similarity from P16521), not direct experimental evidence. However, the sequence features (Walker A/B motifs) independently support the ATPase assignment.",
    "The EC number 3.6.4.- is incomplete (no final digit assigned), reflecting that EF-3's precise mechanism within the ABC superfamily is still being characterized.",
    "The protein is a fungal-specific translation factor (EF-3), absent from animals and plants, making it less familiar to general-trained models, but the sequence motifs remain identifiable.",
    "The sequence-match is exact (SHA256 confirmed) between the benchmark input and the UniProt entry C5E4D9."
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

**Accession:** `C5E4D9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 92. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:30.729914+00:00.  

```json
"C5E4D9"
```

Source SHA-256: `78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:30.729914+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Eukaryotic elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"eEF3"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P16521","source":"UniProtKB"}],"value":"3.6.4.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"EF-3"}]}}
```

Source SHA-256: `78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:30.729914+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P16521","source":"UniProtKB"}],"name":"ATP + H2O = ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13065"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5E4D9?format=txt&versions=92)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:35.219574+00:00.  

```text
DE   RecName: Full=Elongation factor 3 {ECO:0000305};
DE            Short=EF-3 {ECO:0000305};
DE            EC=3.6.4.- {ECO:0000250|UniProtKB:P16521};
DE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};
DE            Short=eEF3 {ECO:0000305};
```

Source SHA-256: `24912b3780dfdc2175cd526300f2f38c8d113474ab82078ce32761e3bafbca36`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5E4D9?format=txt&versions=92)  
**Locator:** `lines 53-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:35.219574+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP + H2O = ADP + phosphate + H(+); Xref=Rhea:RHEA:13065,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000250|UniProtKB:P16521};
```

Source SHA-256: `24912b3780dfdc2175cd526300f2f38c8d113474ab82078ce32761e3bafbca36`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 47. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
