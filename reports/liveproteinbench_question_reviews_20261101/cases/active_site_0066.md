# active_site_0066

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **A** — Position 283 (For beta-ketoacyl synthase activity)

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
A. Position 283 (For beta-ketoacyl synthase activity)
B. Position 381 (For beta-ketoacyl synthase activity)
C. Position 2723 (Proton acceptor; for dehydratase activity 2)
D. Position 549 (Charge relay system)
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

> The supplied sequence exactly matches the UniProt NorA sequence, and its archived annotation lists position 283 as an active site for beta-ketoacyl synthase activity. The annotation is based on a PROSITE-ProRule computational rule, not direct experimental evidence in the excerpts.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5), [C1](#evidence-c1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a concrete way to infer the exact catalytic residue coordinate. Recognizing a polyketide synthase or its domains would not establish that position 283, rather than another coordinate, is annotated as an active site.


**Missing item-specific fact**

> The protein-specific active-site annotation assigning beta-ketoacyl synthase activity to residue 283.


**Reason**

> Selecting the keyed coordinate requires protein-specific annotation or equivalent residue-level evidence absent from the input; general biological reasoning does not distinguish it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice A is supported by the matched archived annotation among the listed choices. The task description asks for residue type as well as position, but the options give a position and functional label rather than the amino-acid type.


### Important caveats

- The historical archived record also annotates positions 418 and 458 for beta-ketoacyl synthase activity; neither is offered as a choice.
- The listed annotation is computationally assigned by PROSITE-ProRule, so it supports the expected answer as an annotation claim but does not establish experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a concrete way to infer the exact catalytic residue coordinate. Recognizing a polyketide synthase or its domains would not establish that position 283, rather than another coordinate, is annotated as an active site.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning beta-ketoacyl synthase activity to residue 283.",
    "reason": "Selecting the keyed coordinate requires protein-specific annotation or equivalent residue-level evidence absent from the input; general biological reasoning does not distinguish it."
  },
  "case_id": "active_site_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt NorA sequence, and its archived annotation lists position 283 as an active site for beta-ketoacyl synthase activity. The annotation is based on a PROSITE-ProRule computational rule, not direct experimental evidence in the excerpts."
  },
  "important_caveats": [
    "The historical archived record also annotates positions 418 and 458 for beta-ketoacyl synthase activity; neither is offered as a choice.",
    "The listed annotation is computationally assigned by PROSITE-ProRule, so it supports the expected answer as an annotation claim but does not establish experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice A is supported by the matched archived annotation among the listed choices. The task description asks for residue type as well as position, but the options give a position and functional label rather than the amino-acid type."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt NorA sequence, and its archived annotation lists position 283 as an active site for beta-ketoacyl synthase activity. The annotation is based on a PROSITE-ProRule computational rule, not direct experimental evidence in the excerpts.",
    "evidence_ids": ["H3", "C5", "C1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a concrete way to infer the exact catalytic residue coordinate. Recognizing a polyketide synthase or its domains would not establish that position 283, rather than another coordinate, is annotated as an active site.",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning beta-ketoacyl synthase activity to residue 283.",
    "reason": "Selecting the keyed coordinate requires protein-specific annotation or equivalent residue-level evidence absent from the input; general biological reasoning does not distinguish it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice A is supported by the matched archived annotation among the listed choices. The task description asks for residue type as well as position, but the options give a position and functional label rather than the amino-acid type."
  },
  "important_caveats": [
    "The historical archived record also annotates positions 418 and 458 for beta-ketoacyl synthase activity; neither is offered as a choice.",
    "The listed annotation is computationally assigned by PROSITE-ProRule, so it supports the expected answer as an annotation claim but does not establish experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER92 (NorA, Spectinabilin PKS system protein, Streptomyces orinoci) annotates position 283 as an Active site 'For beta-ketoacyl synthase activity' (evidence ECO:0000255|PROSITE-ProRule:PRU01348). The benchmark sequence (1897 aa) matches the UniProt sequence exactly. The annotation is computational (PROSITE-ProRule pattern match) rather than experimentally validated, but it is a recognized database annotation. The other options are not supported: position 381 is not annotated as a KS active site (the three KS sites are 283, 418, 458); position 2723 exceeds the sequence length of 1897; no 'charge relay system' annotation exists in this entry.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choices C and D can be eliminated by general reasoning: C cites position 2723 in a 1897-aa protein (impossible), and D invokes a 'charge relay system,' which is a serine-protease mechanism (Asp-His-Ser triad) irrelevant to polyketide synthase catalysis. However, distinguishing A (position 283) from B (position 381) — both labeled 'For beta-ketoacyl synthase activity' — requires knowing the exact domain boundaries and catalytic-cysteine positions within NorA's multiple KS domains. Identifying the GHSxG catalytic motif by manual character-counting across 1897 residues is impractical without tools, and the relative positions of the three KS catalytic Cys residues (283, 418, 458) are protein-specific facts.


**Missing item-specific fact**

> The precise domain architecture of NorA (which region of the 1897-aa sequence corresponds to the first KS domain and where its catalytic Cys falls) is a protein-specific annotation not derivable from general PKS biology alone. Without knowing that the first KS catalytic Cys is at position 283 rather than 381, a model cannot distinguish A from B through reasoning.


**Reason**

> While two distractors (C, D) are eliminable by general biological knowledge, the critical A-vs-B discrimination depends on the specific domain map of NorA, which is an item-specific database annotation (PROSITE-ProRule pattern match). A model must either recognize this exact protein or know its domain boundaries to select 283 over 381.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although NorA has multiple annotated active sites (three KS sites, two DH sites), only one of the four listed positions (283) corresponds to an actual annotated active site. Position 381 is not a KS site, position 2723 is beyond the sequence, and 'charge relay system' is not a PKS mechanism. Thus only A is defensible, and the question is effectively unambiguous despite the multi-domain nature of the enzyme.


### Important caveats

- The active-site annotation at position 283 is computational (PROSITE-ProRule PRU01348 pattern match, ECO:0000255), not experimentally validated. It reflects pattern-based inference from conserved KS motifs.
- The question asks for 'the enzyme's catalytic center' (singular) but NorA is a multi-domain enzyme with at least five annotated active sites. The question implicitly asks which listed option is correct rather than asking for all active sites.
- The UniProt accession B4ER92 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model sees only the raw sequence and choices.
- The historical UniProt entry (version 83, released 28-Jan-2026) already contains the position-283 annotation, so the key was available at the approximate benchmark construction date.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choices C and D can be eliminated by general reasoning: C cites position 2723 in a 1897-aa protein (impossible), and D invokes a 'charge relay system,' which is a serine-protease mechanism (Asp-His-Ser triad) irrelevant to polyketide synthase catalysis. However, distinguishing A (position 283) from B (position 381) — both labeled 'For beta-ketoacyl synthase activity' — requires knowing the exact domain boundaries and catalytic-cysteine positions within NorA's multiple KS domains. Identifying the GHSxG catalytic motif by manual character-counting across 1897 residues is impractical without tools, and the relative positions of the three KS catalytic Cys residues (283, 418, 458) are protein-specific facts.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise domain architecture of NorA (which region of the 1897-aa sequence corresponds to the first KS domain and where its catalytic Cys falls) is a protein-specific annotation not derivable from general PKS biology alone. Without knowing that the first KS catalytic Cys is at position 283 rather than 381, a model cannot distinguish A from B through reasoning.",
    "reason": "While two distractors (C, D) are eliminable by general biological knowledge, the critical A-vs-B discrimination depends on the specific domain map of NorA, which is an item-specific database annotation (PROSITE-ProRule pattern match). A model must either recognize this exact protein or know its domain boundaries to select 283 over 381."
  },
  "case_id": "active_site_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "C7",
      "C8",
      "C9",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (NorA, Spectinabilin PKS system protein, Streptomyces orinoci) annotates position 283 as an Active site 'For beta-ketoacyl synthase activity' (evidence ECO:0000255|PROSITE-ProRule:PRU01348). The benchmark sequence (1897 aa) matches the UniProt sequence exactly. The annotation is computational (PROSITE-ProRule pattern match) rather than experimentally validated, but it is a recognized database annotation. The other options are not supported: position 381 is not annotated as a KS active site (the three KS sites are 283, 418, 458); position 2723 exceeds the sequence length of 1897; no 'charge relay system' annotation exists in this entry."
  },
  "important_caveats": [
    "The active-site annotation at position 283 is computational (PROSITE-ProRule PRU01348 pattern match, ECO:0000255), not experimentally validated. It reflects pattern-based inference from conserved KS motifs.",
    "The question asks for 'the enzyme's catalytic center' (singular) but NorA is a multi-domain enzyme with at least five annotated active sites. The question implicitly asks which listed option is correct rather than asking for all active sites.",
    "The UniProt accession B4ER92 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model sees only the raw sequence and choices.",
    "The historical UniProt entry (version 83, released 28-Jan-2026) already contains the position-283 annotation, so the key was available at the approximate benchmark construction date."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although NorA has multiple annotated active sites (three KS sites, two DH sites), only one of the four listed positions (283) corresponds to an actual annotated active site. Position 381 is not a KS site, position 2723 is beyond the sequence, and 'charge relay system' is not a PKS mechanism. Thus only A is defensible, and the question is effectively unambiguous despite the multi-domain nature of the enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (NorA, Spectinabilin PKS system protein, Streptomyces orinoci) annotates position 283 as an Active site 'For beta-ketoacyl synthase activity' (evidence ECO:0000255|PROSITE-ProRule:PRU01348). The benchmark sequence (1897 aa) matches the UniProt sequence exactly. The annotation is computational (PROSITE-ProRule pattern match) rather than experimentally validated, but it is a recognized database annotation. The other options are not supported: position 381 is not annotated as a KS active site (the three KS sites are 283, 418, 458); position 2723 exceeds the sequence length of 1897; no 'charge relay system' annotation exists in this entry.",
    "evidence_ids": ["C5", "H3", "C6", "C7", "C8", "C9", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choices C and D can be eliminated by general reasoning: C cites position 2723 in a 1897-aa protein (impossible), and D invokes a 'charge relay system,' which is a serine-protease mechanism (Asp-His-Ser triad) irrelevant to polyketide synthase catalysis. However, distinguishing A (position 283) from B (position 381) — both labeled 'For beta-ketoacyl synthase activity' — requires knowing the exact domain boundaries and catalytic-cysteine positions within NorA's multiple KS domains. Identifying the GHSxG catalytic motif by manual character-counting across 1897 residues is impractical without tools, and the relative positions of the three KS catalytic Cys residues (283, 418, 458) are protein-specific facts.",
    "missing_item_specific_fact": "The precise domain architecture of NorA (which region of the 1897-aa sequence corresponds to the first KS domain and where its catalytic Cys falls) is a protein-specific annotation not derivable from general PKS biology alone. Without knowing that the first KS catalytic Cys is at position 283 rather than 381, a model cannot distinguish A from B through reasoning.",
    "reason": "While two distractors (C, D) are eliminable by general biological knowledge, the critical A-vs-B discrimination depends on the specific domain map of NorA, which is an item-specific database annotation (PROSITE-ProRule pattern match). A model must either recognize this exact protein or know its domain boundaries to select 283 over 381."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although NorA has multiple annotated active sites (three KS sites, two DH sites), only one of the four listed positions (283) corresponds to an actual annotated active site. Position 381 is not a KS site, position 2723 is beyond the sequence, and 'charge relay system' is not a PKS mechanism. Thus only A is defensible, and the question is effectively unambiguous despite the multi-domain nature of the enzyme."
  },
  "important_caveats": [
    "The active-site annotation at position 283 is computational (PROSITE-ProRule PRU01348 pattern match, ECO:0000255), not experimentally validated. It reflects pattern-based inference from conserved KS motifs.",
    "The question asks for 'the enzyme's catalytic center' (singular) but NorA is a multi-domain enzyme with at least five annotated active sites. The question implicitly asks which listed option is correct rather than asking for all active sites.",
    "The UniProt accession B4ER92 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model sees only the raw sequence and choices.",
    "The historical UniProt entry (version 83, released 28-Jan-2026) already contains the position-283 annotation, so the key was available at the approximate benchmark construction date."
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
**Locator:** `/features/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
{"description":"For beta-ketoacyl synthase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01348","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":283},"start":{"modifier":"EXACT","value":283}},"type":"Active site"}
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
{"description":"For beta-ketoacyl synthase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01348","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":418},"start":{"modifier":"EXACT","value":418}},"type":"Active site"}
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)  
**Locator:** `/features/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
{"description":"For beta-ketoacyl synthase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01348","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":458},"start":{"modifier":"EXACT","value":458}},"type":"Active site"}
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
{"description":"Proton acceptor; for dehydratase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01363","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":1045},"start":{"modifier":"EXACT","value":1045}},"type":"Active site"}
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)  
**Locator:** `/features/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
{"description":"Proton donor; for dehydratase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01363","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":1211},"start":{"modifier":"EXACT","value":1211}},"type":"Active site"}
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)  
**Locator:** `lines 171-173`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:27:51.676658+00:00.  

```text
FT   ACT_SITE        283
FT                   /note="For beta-ketoacyl synthase activity"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01348"
```

Source SHA-256: `3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 66. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
