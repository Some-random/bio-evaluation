# EC_number_0087: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0087.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **D** — 2.3.1.290

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MELNGIRRRLATAKEAERHRLLLELIRAAAAEALDRPGPLPLDPGRAFGAQGVRGRAAGRLRERLSEATGLPLPATVVFDYPTPGALAGRLCALLLDEPAGPGGANGQMEAEEPIAIVGMGCRLPGDVRSPEGLWRLVHNGTDAISEFPEDRGWTVQQHPDPDHLGTTVTRHAGFLYDAPDFDAGFFAISPGEAVTIDPQHRLLLETTWKAVEDARIDPTSLRGSRTGVFVGLMYSEYGARIRRVPPGAEGYRVVGSMPSVASGRLAYTFGFEGPAVTVDTACSSSLVAMHLAAQSLRKGECTLAVAGGATVMATPWGYIEFSRQRGLAPDGRCRSFSADAAGSSWSEGVGVLLLERLSDARRHGHRVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRQALAHAGLTTAEVDAVDAHGAGTRLGDPIEAQALLATYGQGRPAGRPLWLGSLKSNIGHTQAAAGAAGVIKMVMAMRHGVLPRSLHITEPTPHVDWTSGAVELLTEARDWPADGRPRRAAVSSFGVGGTNAHIILEQAAPEPERPHAPEADGEPRPLPWPVSGHGAAGLRAQARRLADFLRAGPAAPDADLAYSLATTRATLTDRAVVVAADRAEAIARLTALAEGDQGPRVARATAVPRDRLAFVFPGQGSQWPGMAAELMSCYPVFRESIKECGRSLAPHTDWSLAKVLRGESGAPTLDRVDVVQPALFAVMVSLAALWRSFGVEPSAVAGHSQGEIAAARVAGALSLEDAARVVALRSRALRVLSGRGGMVSVAAPAGQVLRTLERWGGAVSVAAVNGPRSLVISGDPGALGEALAAFEAEGIRARRIPVDYASHSAQVEEIRDTLLTELSGIRPRPATVPFYSTVSGEPLDTTALDTGYWVRNLRDTVQFDRTVRRLLADGHTTFLEMSPHPVLTPGIQETAEEAGADEVLTVESLRRNEGGPARLLTAVAEAHVHGVAVDWSPAFAPHRSPARRPAVLRLSSGAATGLRTRPRPPPMFTTAGLDGIDHPLLGAAIPLADGGGGTLFTGTLSLATHPWLADHAVADVLVVPGTALVEAALRAGAECTGRAMLEELVLQAPLILPEQGTVRIQLSVGGPDGTGRRALILSSRPEDAGADEPWTRHAEGTLAPGGGHPRQDPGPWPPTGAREIDLDDCYRQLAKTGLHYGPAFQGLKRLWRLADDLCLEAELPDSAGESGRYGLHPALFDAALHAAALAGPSGAEPLTRLPFSWSGVALYTAGATRLRARLSFTGPQSLTLTAMDPLGHPVLSVGTLGMRPVTAEALHRAAGTAGTALLRLEWRRQAPEHPAGPDLTGWAWVGAGAPPAQPPDGRPYRDLAALRAELDAGAAVPPVIVLAEPATPEGTDPFTAARAALHRTLAAIQDWAAEERLAGTRLVVLTQGAVAATPGALPDPALAAVWGLVRSAQAEYPDRIGLVDTDDPGRSRAAVAAAVHAGEAQAAVRDGALLVPRLARVTATDGPGGPAWPADGTVLVTGGLGTLGRLVVRHLVTTHGARRLVILSRSGGDSAEVREFVGELLAQGANVQVVKGDAADPAVLERVLDGIPQEHPLAAVAHLAGALDDGVLAAQTPQRLDRVLRPKAEAAWQLHRLTARARVPLLAFSSLSGVLGPAGQAGYAAANAFVDALVQRRRGTGLPGVSMGWGMWATRSGLTGALSDTDARLIARTGVRPLTDEEGLALFDQARATGEPVVFPLGLDITALNSGAPDGIPPLLRGLTARTPARRAGAAEAPEPAGEDLAARLAATPEAERDALLLGVVRGHIAAVLGYDDPRAVAERRPFSDIGFDSLRALQLRNRLGAATGRRLPATLVFDHPNPAALSRYLRTLLLPDPAPAPTAPDGQPGPDQADQVIERLNSASLEEVLDFIDHQLGE

[Multiple Choices]
A. 2.3.1.319
B. 3.2.1.31
C. 5.4.99.14
D. 2.3.1.290
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the UniProt entry for NorA, whose curated annotation assigns EC 2.3.1.290 and describes the associated catalytic reaction. The annotation cites a publication, but the supplied excerpts do not independently establish that the reaction was experimentally measured on this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence is compatible with a modular polyketide synthase, which could suggest a broad enzyme class, but that does not distinguish the exact EC number among the options.


**Missing item-specific fact**

> The protein-specific identification as NorA in the spectinabilin biosynthetic system and its annotated catalytic reaction are needed to select EC 2.3.1.290.


**Reason**

> The sequence and choices do not provide enough biological context to infer the specific reaction or distinguish the closely related EC assignments. Doing so requires the protein-specific functional annotation or equivalent external evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports D for the sequence-matched protein; no other choice is supported by the supplied evidence. The limitation is lookup dependence, not evidence that multiple EC numbers apply.


### Important caveats

- The sequence match applies to UniProt accession B4ER92, but that accession was inferred from reviewer-only metadata and was not supplied to the evaluated model.
- The cited UniProt annotation is literature-supported curation; the excerpts alone do not establish direct experimental characterization of the exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is compatible with a modular polyketide synthase, which could suggest a broad enzyme class, but that does not distinguish the exact EC number among the options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as NorA in the spectinabilin biosynthetic system and its annotated catalytic reaction are needed to select EC 2.3.1.290.",
    "reason": "The sequence and choices do not provide enough biological context to infer the specific reaction or distinguish the closely related EC assignments. Doing so requires the protein-specific functional annotation or equivalent external evidence."
  },
  "case_id": "EC_number_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for NorA, whose curated annotation assigns EC 2.3.1.290 and describes the associated catalytic reaction. The annotation cites a publication, but the supplied excerpts do not independently establish that the reaction was experimentally measured on this exact protein."
  },
  "important_caveats": [
    "The sequence match applies to UniProt accession B4ER92, but that accession was inferred from reviewer-only metadata and was not supplied to the evaluated model.",
    "The cited UniProt annotation is literature-supported curation; the excerpts alone do not establish direct experimental characterization of the exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D for the sequence-matched protein; no other choice is supported by the supplied evidence. The limitation is lookup dependence, not evidence that multiple EC numbers apply."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for NorA, whose curated annotation assigns EC 2.3.1.290 and describes the associated catalytic reaction. The annotation cites a publication, but the supplied excerpts do not independently establish that the reaction was experimentally measured on this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence is compatible with a modular polyketide synthase, which could suggest a broad enzyme class, but that does not distinguish the exact EC number among the options.",
    "missing_item_specific_fact": "The protein-specific identification as NorA in the spectinabilin biosynthetic system and its annotated catalytic reaction are needed to select EC 2.3.1.290.",
    "reason": "The sequence and choices do not provide enough biological context to infer the specific reaction or distinguish the closely related EC assignments. Doing so requires the protein-specific functional annotation or equivalent external evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D for the sequence-matched protein; no other choice is supported by the supplied evidence. The limitation is lookup dependence, not evidence that multiple EC numbers apply."
  },
  "important_caveats": [
    "The sequence match applies to UniProt accession B4ER92, but that accession was inferred from reviewer-only metadata and was not supplied to the evaluated model.",
    "The cited UniProt annotation is literature-supported curation; the excerpts alone do not establish direct experimental characterization of the exact sequence."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER92 (sequence SHA256 matched) is annotated with EC=2.3.1.290 for 'Spectinabilin polyketide synthase system protein NorA' from Streptomyces orinoci. The catalytic activity (4-nitrobenzoyl-CoA + 6 methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12H+ → demethyldeoxyspectinabilin + 7CO2 + 6NADP+ + 8CoA + 5H2O) is supported by evidence code ECO:0000305 (curator inference) citing PubMed:17763486. The annotation is database-curated based on published literature, not purely computational prediction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The 1897-aa sequence displays a modular polyketide synthase (PKS) architecture with identifiable KS, AT (GHSQGE motif), ACP, KR, DH, and ER domains arranged in iterative modules. This multi-domain transferase architecture eliminates B (3.2.1.31, a glycosidase/hydrolase) and C (5.4.99.14, an isomerase) through general biological reasoning about enzyme class. However, distinguishing EC 2.3.1.290 (spectinabilin PKS using 4-nitrobenzoyl-CoA starter) from EC 2.3.1.319 (another type I PKS) requires knowledge of the specific starter-unit specificity and product identity, which is not derivable from sequence motifs alone.


**Missing item-specific fact**

> The specific substrate specificity of this NorA module—namely that it accepts 4-nitrobenzoyl-CoA as a starter unit and produces demethyldeoxyspectinabilin—is an item-specific experimental/literature fact (PubMed:17763486) not encoded in recognizable sequence motifs. Without prior knowledge of the spectinabilin biosynthetic pathway or the specific organism's gene cluster, a model cannot distinguish 2.3.1.290 from 2.3.1.319 by sequence reasoning alone.


**Reason**

> While the PKS domain architecture narrows the answer to the 2.3.1.x class and eliminates hydrolase/isomerase distractors, the critical A-vs-D distinction hinges on the specific nitroaromatic starter-unit chemistry unique to spectinabilin biosynthesis. This is a protein-specific annotation fact, not a generalizable sequence-to-function inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B and C are clearly eliminable by enzyme-class reasoning (PKS is a transferase, not a hydrolase or isomerase). Between A and D, only one (D) matches the actual annotation; however, a model lacking specific pathway knowledge could plausibly select A (2.3.1.319) as another type I PKS EC number. The question is not ambiguous in the strict sense (only one correct answer exists), but the A-vs-D distinction is not resolvable by reasoning alone.


### Important caveats

- The UniProt annotation uses ECO:0000305 (curator inference from literature), not direct experimental characterization of this specific protein's kinetics. The underlying evidence is a 2007 ChemBioChem paper on aureothin/neoaureothin pathways.
- EC 2.3.1.319 validity and exact definition were not independently verified from the supplied evidence; if it is a recently assigned or rarely used EC number, it may be a less plausible distractor.
- The sequence-to-EC-number mapping for modular PKS systems is inherently ambiguous at the 4th-digit level without substrate/product information.
- The accession B4ER92 was inferred from dataset metadata (reviewer-only); the evaluated model saw only the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1897-aa sequence displays a modular polyketide synthase (PKS) architecture with identifiable KS, AT (GHSQGE motif), ACP, KR, DH, and ER domains arranged in iterative modules. This multi-domain transferase architecture eliminates B (3.2.1.31, a glycosidase/hydrolase) and C (5.4.99.14, an isomerase) through general biological reasoning about enzyme class. However, distinguishing EC 2.3.1.290 (spectinabilin PKS using 4-nitrobenzoyl-CoA starter) from EC 2.3.1.319 (another type I PKS) requires knowledge of the specific starter-unit specificity and product identity, which is not derivable from sequence motifs alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this NorA module—namely that it accepts 4-nitrobenzoyl-CoA as a starter unit and produces demethyldeoxyspectinabilin—is an item-specific experimental/literature fact (PubMed:17763486) not encoded in recognizable sequence motifs. Without prior knowledge of the spectinabilin biosynthetic pathway or the specific organism's gene cluster, a model cannot distinguish 2.3.1.290 from 2.3.1.319 by sequence reasoning alone.",
    "reason": "While the PKS domain architecture narrows the answer to the 2.3.1.x class and eliminates hydrolase/isomerase distractors, the critical A-vs-D distinction hinges on the specific nitroaromatic starter-unit chemistry unique to spectinabilin biosynthesis. This is a protein-specific annotation fact, not a generalizable sequence-to-function inference."
  },
  "case_id": "EC_number_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (sequence SHA256 matched) is annotated with EC=2.3.1.290 for 'Spectinabilin polyketide synthase system protein NorA' from Streptomyces orinoci. The catalytic activity (4-nitrobenzoyl-CoA + 6 methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12H+ → demethyldeoxyspectinabilin + 7CO2 + 6NADP+ + 8CoA + 5H2O) is supported by evidence code ECO:0000305 (curator inference) citing PubMed:17763486. The annotation is database-curated based on published literature, not purely computational prediction."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (curator inference from literature), not direct experimental characterization of this specific protein's kinetics. The underlying evidence is a 2007 ChemBioChem paper on aureothin/neoaureothin pathways.",
    "EC 2.3.1.319 validity and exact definition were not independently verified from the supplied evidence; if it is a recently assigned or rarely used EC number, it may be a less plausible distractor.",
    "The sequence-to-EC-number mapping for modular PKS systems is inherently ambiguous at the 4th-digit level without substrate/product information.",
    "The accession B4ER92 was inferred from dataset metadata (reviewer-only); the evaluated model saw only the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and C are clearly eliminable by enzyme-class reasoning (PKS is a transferase, not a hydrolase or isomerase). Between A and D, only one (D) matches the actual annotation; however, a model lacking specific pathway knowledge could plausibly select A (2.3.1.319) as another type I PKS EC number. The question is not ambiguous in the strict sense (only one correct answer exists), but the A-vs-D distinction is not resolvable by reasoning alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"EC_number_0087","expected_answer_check":{"judgment":"supported","reason":"UniProt entry B4ER92 (sequence SHA256 matched) is annotated with EC=2.3.1.290 for 'Spectinabilin polyketide synthase system protein NorA' from Streptomyces orinoci. The catalytic activity (4-nitrobenzoyl-CoA + 6 methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12H+ → demethyldeoxyspectinabilin + 7CO2 + 6NADP+ + 8CoA + 5H2O) is supported by evidence code ECO:0000305 (curator inference) citing PubMed:17763486. The annotation is database-curated based on published literature, not purely computational prediction.","evidence_ids":["C4","C5","H1","H2","H4"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"The 1897-aa sequence displays a modular polyketide synthase (PKS) architecture with identifiable KS, AT (GHSQGE motif), ACP, KR, DH, and ER domains arranged in iterative modules. This multi-domain transferase architecture eliminates B (3.2.1.31, a glycosidase/hydrolase) and C (5.4.99.14, an isomerase) through general biological reasoning about enzyme class. However, distinguishing EC 2.3.1.290 (spectinabilin PKS using 4-nitrobenzoyl-CoA starter) from EC 2.3.1.319 (another type I PKS) requires knowledge of the specific starter-unit specificity and product identity, which is not derivable from sequence motifs alone.","missing_item_specific_fact":"The specific substrate specificity of this NorA module—namely that it accepts 4-nitrobenzoyl-CoA as a starter unit and produces demethyldeoxyspectinabilin—is an item-specific experimental/literature fact (PubMed:17763486) not encoded in recognizable sequence motifs. Without prior knowledge of the spectinabilin biosynthetic pathway or the specific organism's gene cluster, a model cannot distinguish 2.3.1.290 from 2.3.1.319 by sequence reasoning alone.","reason":"While the PKS domain architecture narrows the answer to the 2.3.1.x class and eliminates hydrolase/isomerase distractors, the critical A-vs-D distinction hinges on the specific nitroaromatic starter-unit chemistry unique to spectinabilin biosynthesis. This is a protein-specific annotation fact, not a generalizable sequence-to-function inference."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"B and C are clearly eliminable by enzyme-class reasoning (PKS is a transferase, not a hydrolase or isomerase). Between A and D, only one (D) matches the actual annotation; however, a model lacking specific pathway knowledge could plausibly select A (2.3.1.319) as another type I PKS EC number. The question is not ambiguous in the strict sense (only one correct answer exists), but the A-vs-D distinction is not resolvable by reasoning alone."},"important_caveats":["The UniProt annotation uses ECO:0000305 (curator inference from literature), not direct experimental characterization of this specific protein's kinetics. The underlying evidence is a 2007 ChemBioChem paper on aureothin/neoaureothin pathways.","EC 2.3.1.319 validity and exact definition were not independently verified from the supplied evidence; if it is a recently assigned or rarely used EC number, it may be a less plausible distractor.","The sequence-to-EC-number mapping for modular PKS systems is inherently ambiguous at the 4th-digit level without substrate/product information.","The accession B4ER92 was inferred from dataset metadata (reviewer-only); the evaluated model saw only the raw sequence."]}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches the 1897-aa UniProt entry for NorA, whose reviewed annotation assigns EC 2.3.1.290 and gives the corresponding catalytic reaction. The annotation cites PubMed 17763486; this supports the key, though the excerpts do not independently establish the underlying experimental methods.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long, multidomain sequence is consistent with a modular polyketide synthase, which makes the polyketide-related EC 2.3.1 choices more plausible than the glycosidase or isomerase options. But choices A and D share that broad EC class, and the general PKS architecture does not identify the particular product-forming pathway needed to distinguish their complete EC numbers.


**Missing item-specific fact**

> The protein's specific pathway or product identity, or a sufficiently informative homolog/family assignment linking it to the reaction classified as EC 2.3.1.290 rather than EC 2.3.1.319.


**Reason**

> Transferable knowledge supports a broad PKS inference but does not meaningfully distinguish the two offered acyltransferase EC numbers. The exact reaction assignment therefore requires more specific protein or pathway information not supplied in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports D; the original choices alone are insufficient to determine the exact EC number, but that does not establish another option as scientifically defensible for this protein.


### Important caveats

- The cited UniProt annotation is sequence-matched and refers to a PubMed source, but the supplied excerpts do not independently validate the experimental evidence.
- The actual author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, multidomain sequence is consistent with a modular polyketide synthase, which makes the polyketide-related EC 2.3.1 choices more plausible than the glycosidase or isomerase options. But choices A and D share that broad EC class, and the general PKS architecture does not identify the particular product-forming pathway needed to distinguish their complete EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific pathway or product identity, or a sufficiently informative homolog/family assignment linking it to the reaction classified as EC 2.3.1.290 rather than EC 2.3.1.319.",
    "reason": "Transferable knowledge supports a broad PKS inference but does not meaningfully distinguish the two offered acyltransferase EC numbers. The exact reaction assignment therefore requires more specific protein or pathway information not supplied in the original input."
  },
  "case_id": "EC_number_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the 1897-aa UniProt entry for NorA, whose reviewed annotation assigns EC 2.3.1.290 and gives the corresponding catalytic reaction. The annotation cites PubMed 17763486; this supports the key, though the excerpts do not independently establish the underlying experimental methods."
  },
  "important_caveats": [
    "The cited UniProt annotation is sequence-matched and refers to a PubMed source, but the supplied excerpts do not independently validate the experimental evidence.",
    "The actual author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D; the original choices alone are insufficient to determine the exact EC number, but that does not establish another option as scientifically defensible for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the 1897-aa UniProt entry for NorA, whose reviewed annotation assigns EC 2.3.1.290 and gives the corresponding catalytic reaction. The annotation cites PubMed 17763486; this supports the key, though the excerpts do not independently establish the underlying experimental methods.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long, multidomain sequence is consistent with a modular polyketide synthase, which makes the polyketide-related EC 2.3.1 choices more plausible than the glycosidase or isomerase options. But choices A and D share that broad EC class, and the general PKS architecture does not identify the particular product-forming pathway needed to distinguish their complete EC numbers.",
    "missing_item_specific_fact": "The protein's specific pathway or product identity, or a sufficiently informative homolog/family assignment linking it to the reaction classified as EC 2.3.1.290 rather than EC 2.3.1.319.",
    "reason": "Transferable knowledge supports a broad PKS inference but does not meaningfully distinguish the two offered acyltransferase EC numbers. The exact reaction assignment therefore requires more specific protein or pathway information not supplied in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D; the original choices alone are insufficient to determine the exact EC number, but that does not establish another option as scientifically defensible for this protein."
  },
  "important_caveats": [
    "The cited UniProt annotation is sequence-matched and refers to a PubMed source, but the supplied excerpts do not independently validate the experimental evidence.",
    "The actual author source snapshot is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER92 (sequence sha256 matched) annotates this protein as Spectinabilin polyketide synthase system protein NorA with EC 2.3.1.290, supported by evidence code ECO:0000305 (curator inference) citing PubMed:17763486. The catalytic activity reaction (4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H+ = demethyldeoxyspectinabilin + ...) is explicitly listed. Both current and historical (entry version 83) records confirm EC 2.3.1.290.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model can recognize the ~1897-residue protein as a modular polyketide synthase (PKS) from domain architecture: acyltransferase (AT) motifs (GxSxG), ketoreductase (KR), dehydratase (DH), enoylreductase (ER), acyl carrier protein (ACP) with GDMG motifs, and a C-terminal thioesterase (TE). This confidently eliminates option B (EC 3.2.1.31, beta-glucuronidase, a glycosidase) and option C (EC 5.4.99.14, a mutase/isomerase). However, both remaining options A (EC 2.3.1.319) and D (EC 2.3.1.290) are specific EC numbers assigned to particular modular PKS systems in the acyltransferase class (2.3.1). Distinguishing between two specific PKS EC numbers requires knowing the exact product/substrate chemistry of each enzyme. While AT domain specificity codes can indicate extender-unit preferences (methylmalonyl vs malonyl), mapping the complete domain architecture and starter-unit specificity to a particular named natural product (spectinabilin vs whatever product EC 2.3.1.319 describes) is a database-level annotation, not a derivable inference from general PKS family knowledge.


**Missing item-specific fact**

> The specific EC number assignment (2.3.1.290 vs 2.3.1.319) for this exact protein depends on knowing which particular natural product pathway (spectinabilin vs the product of EC 2.3.1.319) this sequence belongs to. This product-level identity is a database annotation not recoverable from sequence features alone without already knowing the answer.


**Reason**

> The sequence clearly identifies a modular PKS, eliminating B and C. But both A and D are valid PKS EC numbers in the 2.3.1.x range. No transferable family-level or mechanistic knowledge distinguishes between two specific PKS product EC numbers without the database record for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both EC 2.3.1.319 and EC 2.3.1.290 are specific EC numbers for modular polyketide synthase systems. From the sequence alone, a model can confirm the protein is a modular PKS but cannot determine which specific natural product pathway it belongs to, making both A and D defensible without the database annotation.


### Important caveats

- The UniProt annotation for EC 2.3.1.290 uses evidence code ECO:0000305 (curator inference based on PubMed:17763486), not direct experimental determination of the full reaction in isolation.
- EC 2.3.1.290 is a very recently assigned and niche EC number specific to the spectinabilin biosynthetic pathway; its existence in the EC list itself is relatively new.
- The identity of EC 2.3.1.319 as a competing option was not independently verified; if it is not a valid EC number or corresponds to a clearly different enzyme class, the ambiguity between A and D would be reduced.
- The reviewer-only evidence confirms sequence match (sha256) between the benchmark input and UniProt B4ER92, but the accession and organism identity were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can recognize the ~1897-residue protein as a modular polyketide synthase (PKS) from domain architecture: acyltransferase (AT) motifs (GxSxG), ketoreductase (KR), dehydratase (DH), enoylreductase (ER), acyl carrier protein (ACP) with GDMG motifs, and a C-terminal thioesterase (TE). This confidently eliminates option B (EC 3.2.1.31, beta-glucuronidase, a glycosidase) and option C (EC 5.4.99.14, a mutase/isomerase). However, both remaining options A (EC 2.3.1.319) and D (EC 2.3.1.290) are specific EC numbers assigned to particular modular PKS systems in the acyltransferase class (2.3.1). Distinguishing between two specific PKS EC numbers requires knowing the exact product/substrate chemistry of each enzyme. While AT domain specificity codes can indicate extender-unit preferences (methylmalonyl vs malonyl), mapping the complete domain architecture and starter-unit specificity to a particular named natural product (spectinabilin vs whatever product EC 2.3.1.319 describes) is a database-level annotation, not a derivable inference from general PKS family knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific EC number assignment (2.3.1.290 vs 2.3.1.319) for this exact protein depends on knowing which particular natural product pathway (spectinabilin vs the product of EC 2.3.1.319) this sequence belongs to. This product-level identity is a database annotation not recoverable from sequence features alone without already knowing the answer.",
    "reason": "The sequence clearly identifies a modular PKS, eliminating B and C. But both A and D are valid PKS EC numbers in the 2.3.1.x range. No transferable family-level or mechanistic knowledge distinguishes between two specific PKS product EC numbers without the database record for this exact protein."
  },
  "case_id": "EC_number_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (sequence sha256 matched) annotates this protein as Spectinabilin polyketide synthase system protein NorA with EC 2.3.1.290, supported by evidence code ECO:0000305 (curator inference) citing PubMed:17763486. The catalytic activity reaction (4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H+ = demethyldeoxyspectinabilin + ...) is explicitly listed. Both current and historical (entry version 83) records confirm EC 2.3.1.290."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.3.1.290 uses evidence code ECO:0000305 (curator inference based on PubMed:17763486), not direct experimental determination of the full reaction in isolation.",
    "EC 2.3.1.290 is a very recently assigned and niche EC number specific to the spectinabilin biosynthetic pathway; its existence in the EC list itself is relatively new.",
    "The identity of EC 2.3.1.319 as a competing option was not independently verified; if it is not a valid EC number or corresponds to a clearly different enzyme class, the ambiguity between A and D would be reduced.",
    "The reviewer-only evidence confirms sequence match (sha256) between the benchmark input and UniProt B4ER92, but the accession and organism identity were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both EC 2.3.1.319 and EC 2.3.1.290 are specific EC numbers for modular polyketide synthase systems. From the sequence alone, a model can confirm the protein is a modular PKS but cannot determine which specific natural product pathway it belongs to, making both A and D defensible without the database annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (sequence sha256 matched) annotates this protein as Spectinabilin polyketide synthase system protein NorA with EC 2.3.1.290, supported by evidence code ECO:0000305 (curator inference) citing PubMed:17763486. The catalytic activity reaction (4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H+ = demethyldeoxyspectinabilin + ...) is explicitly listed. Both current and historical (entry version 83) records confirm EC 2.3.1.290.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable model can recognize the ~1897-residue protein as a modular polyketide synthase (PKS) from domain architecture: acyltransferase (AT) motifs (GxSxG), ketoreductase (KR), dehydratase (DH), enoylreductase (ER), acyl carrier protein (ACP) with GDMG motifs, and a C-terminal thioesterase (TE). This confidently eliminates option B (EC 3.2.1.31, beta-glucuronidase, a glycosidase) and option C (EC 5.4.99.14, a mutase/isomerase). However, both remaining options A (EC 2.3.1.319) and D (EC 2.3.1.290) are specific EC numbers assigned to particular modular PKS systems in the acyltransferase class (2.3.1). Distinguishing between two specific PKS EC numbers requires knowing the exact product/substrate chemistry of each enzyme. While AT domain specificity codes can indicate extender-unit preferences (methylmalonyl vs malonyl), mapping the complete domain architecture and starter-unit specificity to a particular named natural product (spectinabilin vs whatever product EC 2.3.1.319 describes) is a database-level annotation, not a derivable inference from general PKS family knowledge.",
    "missing_item_specific_fact": "The specific EC number assignment (2.3.1.290 vs 2.3.1.319) for this exact protein depends on knowing which particular natural product pathway (spectinabilin vs the product of EC 2.3.1.319) this sequence belongs to. This product-level identity is a database annotation not recoverable from sequence features alone without already knowing the answer.",
    "reason": "The sequence clearly identifies a modular PKS, eliminating B and C. But both A and D are valid PKS EC numbers in the 2.3.1.x range. No transferable family-level or mechanistic knowledge distinguishes between two specific PKS product EC numbers without the database record for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both EC 2.3.1.319 and EC 2.3.1.290 are specific EC numbers for modular polyketide synthase systems. From the sequence alone, a model can confirm the protein is a modular PKS but cannot determine which specific natural product pathway it belongs to, making both A and D defensible without the database annotation."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.3.1.290 uses evidence code ECO:0000305 (curator inference based on PubMed:17763486), not direct experimental determination of the full reaction in isolation.",
    "EC 2.3.1.290 is a very recently assigned and niche EC number specific to the spectinabilin biosynthetic pathway; its existence in the EC list itself is relatively new.",
    "The identity of EC 2.3.1.319 as a competing option was not independently verified; if it is not a valid EC number or corresponds to a clearly different enzyme class, the ambiguity between A and D would be reduced.",
    "The reviewer-only evidence confirms sequence match (sha256) between the benchmark input and UniProt B4ER92, but the accession and organism identity were not provided to the evaluated model."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "B4ER92",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "7a2b43eb4693bca9c8e214b8ce966e5161f55926389724de9065d4baf60d4ff1",
  "benchmark_sequence_length": 1897,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 85,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-09-23",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "current_source_sequence_sha256": "7a2b43eb4693bca9c8e214b8ce966e5161f55926389724de9065d4baf60d4ff1",
  "current_source_sequence_length": 1897,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 83,
  "selected_historical_version": {
    "accession": "B4ER92",
    "database": "Swiss-Prot",
    "entryVersion": 83,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NORA_STRON",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "selected_historical_source_sequence_sha256": "7a2b43eb4693bca9c8e214b8ce966e5161f55926389724de9065d4baf60d4ff1",
  "selected_historical_source_sequence_length": 1897,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 83,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"B4ER92\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":85,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-09-23\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Streptoverticillium orinoci\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces orinoci\",\"taxonId\":67339}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAO85893.1\",\"source\":\"EMBL\"}],\"value\":\"Modular polyketide synthase NorA\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.290\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Spectinabilin polyketide synthase system protein NorA\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Spectinabilin PKS system protein NorA\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:58945\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.290\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"name\":\"4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:58944\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57327\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57384\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142871\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142872\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Traitcheva N.\",\"Jenke-Kodama H.\",\"He J.\",\"Dittmann E.\",\"Hertweck C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17763486\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.200700309\"}],\"citationType\":\"journal article\",\"firstPage\":\"1841\",\"id\":\"17763486\",\"journal\":\"ChemBioChem\",\"lastPage\":\"1849\",\"publicationDate\":\"2007\",\"title\":\"Non-colinear polyketide biosynthesis in the aureothin and neoaureothin pathways: an evolutionary perspective.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAO85893.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"HKI-0260\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   NORA_STRON              Reviewed;        1897 AA.\nAC   B4ER92;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   23-SEP-2008, sequence version 1.\nDT   28-JAN-2026, entry version 83.\nDE   RecName: Full=Spectinabilin polyketide synthase system protein NorA {ECO:0000305};\nDE            Short=Spectinabilin PKS system protein NorA {ECO:0000305};\nDE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};\nDE   AltName: Full=Modular polyketide synthase NorA {ECO:0000312|EMBL:CAO85893.1};\nGN   Name=norA {ECO:0000303|PubMed:17763486};\nOS   Streptomyces orinoci (Streptoverticillium orinoci).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=67339;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 83,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Spectinabilin polyketide synthase system protein NorA {ECO:0000305};\nDE            Short=Spectinabilin PKS system protein NorA {ECO:0000305};\nDE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};\nDE   AltName: Full=Modular polyketide synthase NorA {ECO:0000312|EMBL:CAO85893.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 83,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "source_locator": "lines 15-22",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAO85893.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND SUBUNIT.\nRC   STRAIN=HKI-0260;\nRX   PubMed=17763486; DOI=10.1002/cbic.200700309;\nRA   Traitcheva N., Jenke-Kodama H., He J., Dittmann E., Hertweck C.;\nRT   \"Non-colinear polyketide biosynthesis in the aureothin and neoaureothin\nRT   pathways: an evolutionary perspective.\";\nRL   ChemBioChem 8:1841-1849(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 83,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "source_locator": "lines 31-40",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6\nCC         NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8\nCC         CoA + 5 H2O; Xref=Rhea:RHEA:58944, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57327, ChEBI:CHEBI:57384, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:142871, ChEBI:CHEBI:142872;\nCC         EC=2.3.1.290; Evidence={ECO:0000305|PubMed:17763486};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:58945;\nCC         Evidence={ECO:0000305|PubMed:17763486};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 83,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
