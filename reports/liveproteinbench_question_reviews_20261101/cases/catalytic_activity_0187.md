# catalytic_activity_0187

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELNGIRRRLATAKEAERHRLLLELIRAAAAEALDRPGPLPLDPGRAFGAQGVRGRAAGRLRERLSEATGLPLPATVVFDYPTPGALAGRLCALLLDEPAGPGGANGQMEAEEPIAIVGMGCRLPGDVRSPEGLWRLVHNGTDAISEFPEDRGWTVQQHPDPDHLGTTVTRHAGFLYDAPDFDAGFFAISPGEAVTIDPQHRLLLETTWKAVEDARIDPTSLRGSRTGVFVGLMYSEYGARIRRVPPGAEGYRVVGSMPSVASGRLAYTFGFEGPAVTVDTACSSSLVAMHLAAQSLRKGECTLAVAGGATVMATPWGYIEFSRQRGLAPDGRCRSFSADAAGSSWSEGVGVLLLERLSDARRHGHRVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRQALAHAGLTTAEVDAVDAHGAGTRLGDPIEAQALLATYGQGRPAGRPLWLGSLKSNIGHTQAAAGAAGVIKMVMAMRHGVLPRSLHITEPTPHVDWTSGAVELLTEARDWPADGRPRRAAVSSFGVGGTNAHIILEQAAPEPERPHAPEADGEPRPLPWPVSGHGAAGLRAQARRLADFLRAGPAAPDADLAYSLATTRATLTDRAVVVAADRAEAIARLTALAEGDQGPRVARATAVPRDRLAFVFPGQGSQWPGMAAELMSCYPVFRESIKECGRSLAPHTDWSLAKVLRGESGAPTLDRVDVVQPALFAVMVSLAALWRSFGVEPSAVAGHSQGEIAAARVAGALSLEDAARVVALRSRALRVLSGRGGMVSVAAPAGQVLRTLERWGGAVSVAAVNGPRSLVISGDPGALGEALAAFEAEGIRARRIPVDYASHSAQVEEIRDTLLTELSGIRPRPATVPFYSTVSGEPLDTTALDTGYWVRNLRDTVQFDRTVRRLLADGHTTFLEMSPHPVLTPGIQETAEEAGADEVLTVESLRRNEGGPARLLTAVAEAHVHGVAVDWSPAFAPHRSPARRPAVLRLSSGAATGLRTRPRPPPMFTTAGLDGIDHPLLGAAIPLADGGGGTLFTGTLSLATHPWLADHAVADVLVVPGTALVEAALRAGAECTGRAMLEELVLQAPLILPEQGTVRIQLSVGGPDGTGRRALILSSRPEDAGADEPWTRHAEGTLAPGGGHPRQDPGPWPPTGAREIDLDDCYRQLAKTGLHYGPAFQGLKRLWRLADDLCLEAELPDSAGESGRYGLHPALFDAALHAAALAGPSGAEPLTRLPFSWSGVALYTAGATRLRARLSFTGPQSLTLTAMDPLGHPVLSVGTLGMRPVTAEALHRAAGTAGTALLRLEWRRQAPEHPAGPDLTGWAWVGAGAPPAQPPDGRPYRDLAALRAELDAGAAVPPVIVLAEPATPEGTDPFTAARAALHRTLAAIQDWAAEERLAGTRLVVLTQGAVAATPGALPDPALAAVWGLVRSAQAEYPDRIGLVDTDDPGRSRAAVAAAVHAGEAQAAVRDGALLVPRLARVTATDGPGGPAWPADGTVLVTGGLGTLGRLVVRHLVTTHGARRLVILSRSGGDSAEVREFVGELLAQGANVQVVKGDAADPAVLERVLDGIPQEHPLAAVAHLAGALDDGVLAAQTPQRLDRVLRPKAEAAWQLHRLTARARVPLLAFSSLSGVLGPAGQAGYAAANAFVDALVQRRRGTGLPGVSMGWGMWATRSGLTGALSDTDARLIARTGVRPLTDEEGLALFDQARATGEPVVFPLGLDITALNSGAPDGIPPLLRGLTARTPARRAGAAEAPEPAGEDLAARLAATPEAERDALLLGVVRGHIAAVLGYDDPRAVAERRPFSDIGFDSLRALQLRNRLGAATGRRLPATLVFDHPNPAALSRYLRTLLLPDPAPAPTAPDGQPGPDQADQVIERLNSASLEEVLDFIDHQLGE

[Multiple Choices]
A. UTP + H2O = UDP + phosphate + H(+)
B. 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O
C. n ATP + n H2O + a microtubule = n ADP + n phosphate + (n+1) alpha/beta tubulin heterodimers.
D. UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)
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

> The exact sequence matches the NorA entry, whose catalytic-activity annotation gives reaction B. That annotation cites PubMed 17763486; it supports the key, though the cited primary study was not independently checked here.

Citations as saved: [H4](#evidence-h4), [H3](#evidence-h3), [C5](#evidence-c5), [C1](#evidence-c1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The unusually long sequence is compatible with a multidomain biosynthetic enzyme, and B is the only polyketide-assembly reaction among the choices. This may suggest B’s broad enzyme class, but does not establish the specific substrates or product.


**Missing item-specific fact**

> The protein-specific NorA annotation linking this sequence to formation of demethyldeoxyspectinabilin from the listed CoA substrates.


**Reason**

> Choosing the precise named reaction requires an item-specific functional assignment not supplied in the question. Broad sequence architecture alone does not determine this reaction’s substrates, product, or stoichiometry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotated reaction matches B; the other choices describe unrelated reaction classes.


### Important caveats

- The cited database catalytic-activity annotation is literature-supported, but the evidence provided does not independently establish the underlying experimental details.
- The exact sequence match establishes applicability of the annotation to this sequence, not that the evaluated model was given the accession or annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The unusually long sequence is compatible with a multidomain biosynthetic enzyme, and B is the only polyketide-assembly reaction among the choices. This may suggest B’s broad enzyme class, but does not establish the specific substrates or product.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific NorA annotation linking this sequence to formation of demethyldeoxyspectinabilin from the listed CoA substrates.",
    "reason": "Choosing the precise named reaction requires an item-specific functional assignment not supplied in the question. Broad sequence architecture alone does not determine this reaction’s substrates, product, or stoichiometry."
  },
  "case_id": "catalytic_activity_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H3",
      "C5",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the NorA entry, whose catalytic-activity annotation gives reaction B. That annotation cites PubMed 17763486; it supports the key, though the cited primary study was not independently checked here."
  },
  "important_caveats": [
    "The cited database catalytic-activity annotation is literature-supported, but the evidence provided does not independently establish the underlying experimental details.",
    "The exact sequence match establishes applicability of the annotation to this sequence, not that the evaluated model was given the accession or annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated reaction matches B; the other choices describe unrelated reaction classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the NorA entry, whose catalytic-activity annotation gives reaction B. That annotation cites PubMed 17763486; it supports the key, though the cited primary study was not independently checked here.",
    "evidence_ids": ["H4", "H3", "C5", "C1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The unusually long sequence is compatible with a multidomain biosynthetic enzyme, and B is the only polyketide-assembly reaction among the choices. This may suggest B’s broad enzyme class, but does not establish the specific substrates or product.",
    "missing_item_specific_fact": "The protein-specific NorA annotation linking this sequence to formation of demethyldeoxyspectinabilin from the listed CoA substrates.",
    "reason": "Choosing the precise named reaction requires an item-specific functional assignment not supplied in the question. Broad sequence architecture alone does not determine this reaction’s substrates, product, or stoichiometry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated reaction matches B; the other choices describe unrelated reaction classes."
  },
  "important_caveats": [
    "The cited database catalytic-activity annotation is literature-supported, but the evidence provided does not independently establish the underlying experimental details.",
    "The exact sequence match establishes applicability of the annotation to this sequence, not that the evaluated model was given the accession or annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER92 (NORA_STRON, sequence matched exactly at 1897 AA) lists the exact reaction in Choice B as the CATALYTIC ACTIVITY for this protein, with EC 2.3.1.290. The evidence code is ECO:0000305 (curator inference) citing PubMed:17763486 (Traitcheva et al., ChemBioChem 2007), which characterized the spectinabilin/aureothin PKS pathway. The reaction is annotated as physiologically left-to-right (RHEA:58945). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence is 1897 amino acids, far exceeding the size of any enzyme catalyzing Choices A (nucleotide phosphodiesterase, ~300-500 AA), C (tubulin, ~440 AA), or D (UDP-GlcNAc hydrolase, small enzyme). The sequence contains recognizable modular PKS domain signatures: a ketosynthase motif (Cys-His-His triad region 'GGMGCRLPGDVRSPEGLWRLVHNG'), an acyltransferase-like segment ('GSMPSVASGRL'), an acyl-carrier protein serine region ('GSAVNQDG'), a dehydratase motif ('GQGSQWPG'), and a long C-terminal reductase/thioesterase region. This multi-domain architecture of a very large enzyme is characteristic of a modular polyketide synthase. Among the four choices, only B describes a PKS-type condensation/reduction reaction. The other choices can be eliminated by protein size and domain architecture alone.


**Missing item-specific fact**

> The exact substrate identity (4-nitrobenzoyl-CoA) and product name (demethyldeoxyspectinabilin) cannot be deduced from sequence without database lookup or AT-domain specificity prediction. However, among the given choices, only B is a PKS reaction, so the specific product name is not needed to select the correct option.


**Reason**

> A trained biologist can recognize that a ~1900 AA multi-domain protein with KS/AT/ACP/DH/KR/TE-like motifs is a modular PKS, and among the four options only B represents a PKS reaction. The elimination of A, C, and D relies on general protein-size and domain-architecture reasoning. The exact chemical names in B are not independently derivable from sequence, but they are not needed to distinguish B from the clearly non-PKS alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A, C, and D describe reactions catalyzed by small, single-domain enzymes (phosphodiesterase, tubulin GTPase, UDP-sugar hydrolase) that are incompatible with a 1897 AA multi-domain protein. Choice C additionally contains a factual error (ATP instead of GTP for tubulin). Only B is consistent with the observed protein architecture.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by curator from PubMed:17763486), meaning the reaction assignment is based on pathway characterization in the cited paper rather than direct in vitro kinetics of the isolated NorA protein alone.
- The specific substrate/product names in Choice B (4-nitrobenzoyl-CoA, demethyldeoxyspectinabilin) are pathway-level assignments; recognizing the protein as a PKS narrows the answer to B among the choices, but the exact chemical identities require specialized PKS biology knowledge or database lookup.
- Reviewer-only evidence (UniProt accession, annotation) was absent from the evaluated model input; the reasoning argument relies solely on sequence-derived domain inference and elimination of incompatible choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence is 1897 amino acids, far exceeding the size of any enzyme catalyzing Choices A (nucleotide phosphodiesterase, ~300-500 AA), C (tubulin, ~440 AA), or D (UDP-GlcNAc hydrolase, small enzyme). The sequence contains recognizable modular PKS domain signatures: a ketosynthase motif (Cys-His-His triad region 'GGMGCRLPGDVRSPEGLWRLVHNG'), an acyltransferase-like segment ('GSMPSVASGRL'), an acyl-carrier protein serine region ('GSAVNQDG'), a dehydratase motif ('GQGSQWPG'), and a long C-terminal reductase/thioesterase region. This multi-domain architecture of a very large enzyme is characteristic of a modular polyketide synthase. Among the four choices, only B describes a PKS-type condensation/reduction reaction. The other choices can be eliminated by protein size and domain architecture alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate identity (4-nitrobenzoyl-CoA) and product name (demethyldeoxyspectinabilin) cannot be deduced from sequence without database lookup or AT-domain specificity prediction. However, among the given choices, only B is a PKS reaction, so the specific product name is not needed to select the correct option.",
    "reason": "A trained biologist can recognize that a ~1900 AA multi-domain protein with KS/AT/ACP/DH/KR/TE-like motifs is a modular PKS, and among the four options only B represents a PKS reaction. The elimination of A, C, and D relies on general protein-size and domain-architecture reasoning. The exact chemical names in B are not independently derivable from sequence, but they are not needed to distinguish B from the clearly non-PKS alternatives."
  },
  "case_id": "catalytic_activity_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (NORA_STRON, sequence matched exactly at 1897 AA) lists the exact reaction in Choice B as the CATALYTIC ACTIVITY for this protein, with EC 2.3.1.290. The evidence code is ECO:0000305 (curator inference) citing PubMed:17763486 (Traitcheva et al., ChemBioChem 2007), which characterized the spectinabilin/aureothin PKS pathway. The reaction is annotated as physiologically left-to-right (RHEA:58945). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by curator from PubMed:17763486), meaning the reaction assignment is based on pathway characterization in the cited paper rather than direct in vitro kinetics of the isolated NorA protein alone.",
    "The specific substrate/product names in Choice B (4-nitrobenzoyl-CoA, demethyldeoxyspectinabilin) are pathway-level assignments; recognizing the protein as a PKS narrows the answer to B among the choices, but the exact chemical identities require specialized PKS biology knowledge or database lookup.",
    "Reviewer-only evidence (UniProt accession, annotation) was absent from the evaluated model input; the reasoning argument relies solely on sequence-derived domain inference and elimination of incompatible choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D describe reactions catalyzed by small, single-domain enzymes (phosphodiesterase, tubulin GTPase, UDP-sugar hydrolase) that are incompatible with a 1897 AA multi-domain protein. Choice C additionally contains a factual error (ATP instead of GTP for tubulin). Only B is consistent with the observed protein architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (NORA_STRON, sequence matched exactly at 1897 AA) lists the exact reaction in Choice B as the CATALYTIC ACTIVITY for this protein, with EC 2.3.1.290. The evidence code is ECO:0000305 (curator inference) citing PubMed:17763486 (Traitcheva et al., ChemBioChem 2007), which characterized the spectinabilin/aureothin PKS pathway. The reaction is annotated as physiologically left-to-right (RHEA:58945). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed).",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence is 1897 amino acids, far exceeding the size of any enzyme catalyzing Choices A (nucleotide phosphodiesterase, ~300-500 AA), C (tubulin, ~440 AA), or D (UDP-GlcNAc hydrolase, small enzyme). The sequence contains recognizable modular PKS domain signatures: a ketosynthase motif (Cys-His-His triad region 'GGMGCRLPGDVRSPEGLWRLVHNG'), an acyltransferase-like segment ('GSMPSVASGRL'), an acyl-carrier protein serine region ('GSAVNQDG'), a dehydratase motif ('GQGSQWPG'), and a long C-terminal reductase/thioesterase region. This multi-domain architecture of a very large enzyme is characteristic of a modular polyketide synthase. Among the four choices, only B describes a PKS-type condensation/reduction reaction. The other choices can be eliminated by protein size and domain architecture alone.",
    "missing_item_specific_fact": "The exact substrate identity (4-nitrobenzoyl-CoA) and product name (demethyldeoxyspectinabilin) cannot be deduced from sequence without database lookup or AT-domain specificity prediction. However, among the given choices, only B is a PKS reaction, so the specific product name is not needed to select the correct option.",
    "reason": "A trained biologist can recognize that a ~1900 AA multi-domain protein with KS/AT/ACP/DH/KR/TE-like motifs is a modular PKS, and among the four options only B represents a PKS reaction. The elimination of A, C, and D relies on general protein-size and domain-architecture reasoning. The exact chemical names in B are not independently derivable from sequence, but they are not needed to distinguish B from the clearly non-PKS alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D describe reactions catalyzed by small, single-domain enzymes (phosphodiesterase, tubulin GTPase, UDP-sugar hydrolase) that are incompatible with a 1897 AA multi-domain protein. Choice C additionally contains a factual error (ATP instead of GTP for tubulin). Only B is consistent with the observed protein architecture."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by curator from PubMed:17763486), meaning the reaction assignment is based on pathway characterization in the cited paper rather than direct in vitro kinetics of the isolated NorA protein alone.",
    "The specific substrate/product names in Choice B (4-nitrobenzoyl-CoA, demethyldeoxyspectinabilin) are pathway-level assignments; recognizing the protein as a PKS narrows the answer to B among the choices, but the exact chemical identities require specialized PKS biology knowledge or database lookup.",
    "Reviewer-only evidence (UniProt accession, annotation) was absent from the evaluated model input; the reasoning argument relies solely on sequence-derived domain inference and elimination of incompatible choices."
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)  
**Locator:** `lines 15-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:27:51.676658+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:CAO85893.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND SUBUNIT.
RC   STRAIN=HKI-0260;
RX   PubMed=17763486; DOI=10.1002/cbic.200700309;
RA   Traitcheva N., Jenke-Kodama H., He J., Dittmann E., Hertweck C.;
RT   "Non-colinear polyketide biosynthesis in the aureothin and neoaureothin
RT   pathways: an evolutionary perspective.";
RL   ChemBioChem 8:1841-1849(2007).
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 187. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
