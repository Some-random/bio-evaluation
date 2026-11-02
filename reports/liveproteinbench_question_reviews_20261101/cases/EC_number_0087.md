# EC_number_0087

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.3.1.290

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `B4ER92` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 83. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
"B4ER92"
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"CAO85893.1","source":"EMBL"}],"value":"Modular polyketide synthase NorA"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"value":"2.3.1.290"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Spectinabilin polyketide synthase system protein NorA"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Spectinabilin PKS system protein NorA"}]}}
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:58945"}}],"reaction":{"ecNumber":"2.3.1.290","evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"name":"4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58944"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57327"},{"database":"ChEBI","id":"CHEBI:57384"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:142871"},{"database":"ChEBI","id":"CHEBI:142872"}]}}
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:27:51.676658+00:00.  

```text
ID   NORA_STRON              Reviewed;        1897 AA.
AC   B4ER92;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   23-SEP-2008, sequence version 1.
DT   28-JAN-2026, entry version 83.
DE   RecName: Full=Spectinabilin polyketide synthase system protein NorA {ECO:0000305};
DE            Short=Spectinabilin PKS system protein NorA {ECO:0000305};
DE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};
DE   AltName: Full=Modular polyketide synthase NorA {ECO:0000312|EMBL:CAO85893.1};
GN   Name=norA {ECO:0000303|PubMed:17763486};
OS   Streptomyces orinoci (Streptoverticillium orinoci).
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=67339;
```

Source SHA-256: `3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:27:51.676658+00:00.  

```text
DE   RecName: Full=Spectinabilin polyketide synthase system protein NorA {ECO:0000305};
DE            Short=Spectinabilin PKS system protein NorA {ECO:0000305};
DE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};
DE   AltName: Full=Modular polyketide synthase NorA {ECO:0000312|EMBL:CAO85893.1};
```

Source SHA-256: `3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)  
**Locator:** `lines 31-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:27:51.676658+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6
CC         NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8
CC         CoA + 5 H2O; Xref=Rhea:RHEA:58944, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:57287,
CC         ChEBI:CHEBI:57327, ChEBI:CHEBI:57384, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:142871, ChEBI:CHEBI:142872;
CC         EC=2.3.1.290; Evidence={ECO:0000305|PubMed:17763486};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:58945;
CC         Evidence={ECO:0000305|PubMed:17763486};
```

Source SHA-256: `3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
