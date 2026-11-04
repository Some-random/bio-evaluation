# pathway_0045

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0045.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Antibiotic biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MELNGIRRRLATAKEAERHRLLLELIRAAAAEALDRPGPLPLDPGRAFGAQGVRGRAAGRLRERLSEATGLPLPATVVFDYPTPGALAGRLCALLLDEPAGPGGANGQMEAEEPIAIVGMGCRLPGDVRSPEGLWRLVHNGTDAISEFPEDRGWTVQQHPDPDHLGTTVTRHAGFLYDAPDFDAGFFAISPGEAVTIDPQHRLLLETTWKAVEDARIDPTSLRGSRTGVFVGLMYSEYGARIRRVPPGAEGYRVVGSMPSVASGRLAYTFGFEGPAVTVDTACSSSLVAMHLAAQSLRKGECTLAVAGGATVMATPWGYIEFSRQRGLAPDGRCRSFSADAAGSSWSEGVGVLLLERLSDARRHGHRVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRQALAHAGLTTAEVDAVDAHGAGTRLGDPIEAQALLATYGQGRPAGRPLWLGSLKSNIGHTQAAAGAAGVIKMVMAMRHGVLPRSLHITEPTPHVDWTSGAVELLTEARDWPADGRPRRAAVSSFGVGGTNAHIILEQAAPEPERPHAPEADGEPRPLPWPVSGHGAAGLRAQARRLADFLRAGPAAPDADLAYSLATTRATLTDRAVVVAADRAEAIARLTALAEGDQGPRVARATAVPRDRLAFVFPGQGSQWPGMAAELMSCYPVFRESIKECGRSLAPHTDWSLAKVLRGESGAPTLDRVDVVQPALFAVMVSLAALWRSFGVEPSAVAGHSQGEIAAARVAGALSLEDAARVVALRSRALRVLSGRGGMVSVAAPAGQVLRTLERWGGAVSVAAVNGPRSLVISGDPGALGEALAAFEAEGIRARRIPVDYASHSAQVEEIRDTLLTELSGIRPRPATVPFYSTVSGEPLDTTALDTGYWVRNLRDTVQFDRTVRRLLADGHTTFLEMSPHPVLTPGIQETAEEAGADEVLTVESLRRNEGGPARLLTAVAEAHVHGVAVDWSPAFAPHRSPARRPAVLRLSSGAATGLRTRPRPPPMFTTAGLDGIDHPLLGAAIPLADGGGGTLFTGTLSLATHPWLADHAVADVLVVPGTALVEAALRAGAECTGRAMLEELVLQAPLILPEQGTVRIQLSVGGPDGTGRRALILSSRPEDAGADEPWTRHAEGTLAPGGGHPRQDPGPWPPTGAREIDLDDCYRQLAKTGLHYGPAFQGLKRLWRLADDLCLEAELPDSAGESGRYGLHPALFDAALHAAALAGPSGAEPLTRLPFSWSGVALYTAGATRLRARLSFTGPQSLTLTAMDPLGHPVLSVGTLGMRPVTAEALHRAAGTAGTALLRLEWRRQAPEHPAGPDLTGWAWVGAGAPPAQPPDGRPYRDLAALRAELDAGAAVPPVIVLAEPATPEGTDPFTAARAALHRTLAAIQDWAAEERLAGTRLVVLTQGAVAATPGALPDPALAAVWGLVRSAQAEYPDRIGLVDTDDPGRSRAAVAAAVHAGEAQAAVRDGALLVPRLARVTATDGPGGPAWPADGTVLVTGGLGTLGRLVVRHLVTTHGARRLVILSRSGGDSAEVREFVGELLAQGANVQVVKGDAADPAVLERVLDGIPQEHPLAAVAHLAGALDDGVLAAQTPQRLDRVLRPKAEAAWQLHRLTARARVPLLAFSSLSGVLGPAGQAGYAAANAFVDALVQRRRGTGLPGVSMGWGMWATRSGLTGALSDTDARLIARTGVRPLTDEEGLALFDQARATGEPVVFPLGLDITALNSGAPDGIPPLLRGLTARTPARRAGAAEAPEPAGEDLAARLAATPEAERDALLLGVVRGHIAAVLGYDDPRAVAERRPFSDIGFDSLRALQLRNRLGAATGRRLPATLVFDHPNPAALSRYLRTLLLPDPAPAPTAPDGQPGPDQADQVIERLNSASLEEVLDFIDHQLGE

[Multiple Choices]
A. One-carbon metabolism
B. Antibiotic biosynthesis. .
C. peptidoglycan degradation. .
D. 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates this protein in antibiotic biosynthesis, both in the current record and in a historical record. The annotation cites a publication, though the excerpts alone do not independently establish the experimental basis for that annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1,897-residue sequence has the scale and repeated catalytic-domain pattern characteristic of a modular polyketide synthase assembly-line protein. Such synthases build specialized polyketide natural products, making antibiotic biosynthesis a meaningful fit among these choices; the other options concern folate metabolism or peptidoglycan degradation and do not fit this large assembly-line architecture.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the transferable modular-PKS pattern provides a credible distinction among the offered alternatives. Sequence-level recognition does not by itself identify the specific product or prove that every polyketide made by such machinery is an antibiotic, but that finer distinction is not needed to favor B over these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives are sufficiently distinct for the modular-polyketide-synthase inference to favor B; no competing option is comparably supported by the sequence.


### Important caveats

- The pathway evidence is a database annotation supported by a cited publication; the supplied excerpts do not independently establish the precise experimental evidence.
- A modular polyketide synthase pattern supports the pathway choice but does not, by itself, establish the identity or therapeutic use of the product.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1,897-residue sequence has the scale and repeated catalytic-domain pattern characteristic of a modular polyketide synthase assembly-line protein. Such synthases build specialized polyketide natural products, making antibiotic biosynthesis a meaningful fit among these choices; the other options concern folate metabolism or peptidoglycan degradation and do not fit this large assembly-line architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the transferable modular-PKS pattern provides a credible distinction among the offered alternatives. Sequence-level recognition does not by itself identify the specific product or prove that every polyketide made by such machinery is an antibiotic, but that finer distinction is not needed to favor B over these choices."
  },
  "case_id": "pathway_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein in antibiotic biosynthesis, both in the current record and in a historical record. The annotation cites a publication, though the excerpts alone do not independently establish the experimental basis for that annotation."
  },
  "important_caveats": [
    "The pathway evidence is a database annotation supported by a cited publication; the supplied excerpts do not independently establish the precise experimental evidence.",
    "A modular polyketide synthase pattern supports the pathway choice but does not, by itself, establish the identity or therapeutic use of the product."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives are sufficiently distinct for the modular-polyketide-synthase inference to favor B; no competing option is comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein in antibiotic biosynthesis, both in the current record and in a historical record. The annotation cites a publication, though the excerpts alone do not independently establish the experimental basis for that annotation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1,897-residue sequence has the scale and repeated catalytic-domain pattern characteristic of a modular polyketide synthase assembly-line protein. Such synthases build specialized polyketide natural products, making antibiotic biosynthesis a meaningful fit among these choices; the other options concern folate metabolism or peptidoglycan degradation and do not fit this large assembly-line architecture.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the transferable modular-PKS pattern provides a credible distinction among the offered alternatives. Sequence-level recognition does not by itself identify the specific product or prove that every polyketide made by such machinery is an antibiotic, but that finer distinction is not needed to favor B over these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives are sufficiently distinct for the modular-polyketide-synthase inference to favor B; no competing option is comparably supported by the sequence."
  },
  "important_caveats": [
    "The pathway evidence is a database annotation supported by a cited publication; the supplied excerpts do not independently establish the precise experimental evidence.",
    "A modular polyketide synthase pattern supports the pathway choice but does not, by itself, establish the identity or therapeutic use of the product."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B4ER92 (Spectinabilin polyketide synthase system protein NorA) is explicitly annotated with PATHWAY: Antibiotic biosynthesis (ECO:0000305|PubMed:17763486). The protein is a modular polyketide synthase (PKS) producing spectinabilin, a polyketide antibiotic. The annotation is based on experimental evidence from the primary publication. Polyketide biosynthesis is also listed, but among the offered choices, 'Antibiotic biosynthesis' is the correct and directly supported answer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C4](#evidence-c4), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1897-amino-acid sequence exhibits the hallmark architecture of a modular Type I polyketide synthase (PKS): multiple catalytic domain motifs arranged in tandem, including AT domain signatures (GHSQGE, GGMVSVAAPAGQ), KR domain NADPH-binding motifs (GGLGTLGRL), and other iterative catalytic elements. This multi-domain modular organization is diagnostic of Type I PKS systems, which are well-known for synthesizing polyketide natural products. A knowledgeable model can (1) recognize the PKS domain architecture from sequence motifs and the extraordinary protein length, (2) recall that modular PKS enzymes are the biosynthetic workhorses for polyketide natural products, (3) know from extensive literature (erythromycin PKS, tetracycline PKS, actinorhodin PKS, etc.) that a large fraction of polyketide products are antibiotics, especially from Actinomycetes. Meanwhile, options A (one-carbon metabolism), C (peptidoglycan degradation), and D (dihydrofolate synthesis) involve small enzymes (typically 200-400 AA) with entirely different catalytic folds (e.g., DHPS is ~250 AA; peptidoglycan hydrolases are lysozyme/amidase folds; one-carbon enzymes are folate-binding or methyltransferase folds). The 1897-AA multi-domain PKS architecture is incompatible with any of these, leaving B as the only viable choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of modular PKS domain architecture from sequence motifs (AT: GHSxG, KR: GxGxxG, etc.) and the very large protein size is a well-established transferable skill. The association of PKS products with antibiotic biosynthesis is broad, well-documented general knowledge across many characterized PKS systems. The elimination of options A, C, and D follows straightforwardly from their incompatibility with a 1897-AA multi-domain enzyme. No target-specific annotation is needed to make this distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D describe pathways involving small, single-domain enzymes (folate-cycle enzymes, peptidoglycan hydrolases, DHPS) that are structurally and functionally incompatible with a 1897-AA modular PKS. Only option B (Antibiotic biosynthesis) is consistent with the PKS architecture. Although UniProt also annotates 'Polyketide biosynthesis,' that option is not offered, so there is no ambiguity among the given choices.


### Important caveats

- The UniProt entry also lists 'Polyketide biosynthesis' as a pathway; this is not among the choices but is a more specific description. The offered answer 'Antibiotic biosynthesis' is the broader UniProt pathway category and is correct among the given options.
- The sequence-based PKS domain recognition relies on motif-level pattern matching; a model without explicit PKS training might miss some motifs, but the overall size and multi-domain architecture remain strongly diagnostic.
- The protein is from Streptomyces orinoci, a genus renowned for antibiotic production, which further supports the antibiotic biosynthesis pathway assignment, though this organism-level inference requires recognizing Actinomycetota/Streptomycetaceae context from sequence composition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1897-amino-acid sequence exhibits the hallmark architecture of a modular Type I polyketide synthase (PKS): multiple catalytic domain motifs arranged in tandem, including AT domain signatures (GHSQGE, GGMVSVAAPAGQ), KR domain NADPH-binding motifs (GGLGTLGRL), and other iterative catalytic elements. This multi-domain modular organization is diagnostic of Type I PKS systems, which are well-known for synthesizing polyketide natural products. A knowledgeable model can (1) recognize the PKS domain architecture from sequence motifs and the extraordinary protein length, (2) recall that modular PKS enzymes are the biosynthetic workhorses for polyketide natural products, (3) know from extensive literature (erythromycin PKS, tetracycline PKS, actinorhodin PKS, etc.) that a large fraction of polyketide products are antibiotics, especially from Actinomycetes. Meanwhile, options A (one-carbon metabolism), C (peptidoglycan degradation), and D (dihydrofolate synthesis) involve small enzymes (typically 200-400 AA) with entirely different catalytic folds (e.g., DHPS is ~250 AA; peptidoglycan hydrolases are lysozyme/amidase folds; one-carbon enzymes are folate-binding or methyltransferase folds). The 1897-AA multi-domain PKS architecture is incompatible with any of these, leaving B as the only viable choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of modular PKS domain architecture from sequence motifs (AT: GHSxG, KR: GxGxxG, etc.) and the very large protein size is a well-established transferable skill. The association of PKS products with antibiotic biosynthesis is broad, well-documented general knowledge across many characterized PKS systems. The elimination of options A, C, and D follows straightforwardly from their incompatibility with a 1897-AA multi-domain enzyme. No target-specific annotation is needed to make this distinction."
  },
  "case_id": "pathway_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C4",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B4ER92 (Spectinabilin polyketide synthase system protein NorA) is explicitly annotated with PATHWAY: Antibiotic biosynthesis (ECO:0000305|PubMed:17763486). The protein is a modular polyketide synthase (PKS) producing spectinabilin, a polyketide antibiotic. The annotation is based on experimental evidence from the primary publication. Polyketide biosynthesis is also listed, but among the offered choices, 'Antibiotic biosynthesis' is the correct and directly supported answer."
  },
  "important_caveats": [
    "The UniProt entry also lists 'Polyketide biosynthesis' as a pathway; this is not among the choices but is a more specific description. The offered answer 'Antibiotic biosynthesis' is the broader UniProt pathway category and is correct among the given options.",
    "The sequence-based PKS domain recognition relies on motif-level pattern matching; a model without explicit PKS training might miss some motifs, but the overall size and multi-domain architecture remain strongly diagnostic.",
    "The protein is from Streptomyces orinoci, a genus renowned for antibiotic production, which further supports the antibiotic biosynthesis pathway assignment, though this organism-level inference requires recognizing Actinomycetota/Streptomycetaceae context from sequence composition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D describe pathways involving small, single-domain enzymes (folate-cycle enzymes, peptidoglycan hydrolases, DHPS) that are structurally and functionally incompatible with a 1897-AA modular PKS. Only option B (Antibiotic biosynthesis) is consistent with the PKS architecture. Although UniProt also annotates 'Polyketide biosynthesis,' that option is not offered, so there is no ambiguity among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B4ER92 (Spectinabilin polyketide synthase system protein NorA) is explicitly annotated with PATHWAY: Antibiotic biosynthesis (ECO:0000305|PubMed:17763486). The protein is a modular polyketide synthase (PKS) producing spectinabilin, a polyketide antibiotic. The annotation is based on experimental evidence from the primary publication. Polyketide biosynthesis is also listed, but among the offered choices, 'Antibiotic biosynthesis' is the correct and directly supported answer.",
    "evidence_ids": ["C5", "C6", "C4", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1897-amino-acid sequence exhibits the hallmark architecture of a modular Type I polyketide synthase (PKS): multiple catalytic domain motifs arranged in tandem, including AT domain signatures (GHSQGE, GGMVSVAAPAGQ), KR domain NADPH-binding motifs (GGLGTLGRL), and other iterative catalytic elements. This multi-domain modular organization is diagnostic of Type I PKS systems, which are well-known for synthesizing polyketide natural products. A knowledgeable model can (1) recognize the PKS domain architecture from sequence motifs and the extraordinary protein length, (2) recall that modular PKS enzymes are the biosynthetic workhorses for polyketide natural products, (3) know from extensive literature (erythromycin PKS, tetracycline PKS, actinorhodin PKS, etc.) that a large fraction of polyketide products are antibiotics, especially from Actinomycetes. Meanwhile, options A (one-carbon metabolism), C (peptidoglycan degradation), and D (dihydrofolate synthesis) involve small enzymes (typically 200-400 AA) with entirely different catalytic folds (e.g., DHPS is ~250 AA; peptidoglycan hydrolases are lysozyme/amidase folds; one-carbon enzymes are folate-binding or methyltransferase folds). The 1897-AA multi-domain PKS architecture is incompatible with any of these, leaving B as the only viable choice.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of modular PKS domain architecture from sequence motifs (AT: GHSxG, KR: GxGxxG, etc.) and the very large protein size is a well-established transferable skill. The association of PKS products with antibiotic biosynthesis is broad, well-documented general knowledge across many characterized PKS systems. The elimination of options A, C, and D follows straightforwardly from their incompatibility with a 1897-AA multi-domain enzyme. No target-specific annotation is needed to make this distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D describe pathways involving small, single-domain enzymes (folate-cycle enzymes, peptidoglycan hydrolases, DHPS) that are structurally and functionally incompatible with a 1897-AA modular PKS. Only option B (Antibiotic biosynthesis) is consistent with the PKS architecture. Although UniProt also annotates 'Polyketide biosynthesis,' that option is not offered, so there is no ambiguity among the given choices."
  },
  "important_caveats": [
    "The UniProt entry also lists 'Polyketide biosynthesis' as a pathway; this is not among the choices but is a more specific description. The offered answer 'Antibiotic biosynthesis' is the broader UniProt pathway category and is correct among the given options.",
    "The sequence-based PKS domain recognition relies on motif-level pattern matching; a model without explicit PKS training might miss some motifs, but the overall size and multi-domain architecture remain strongly diagnostic.",
    "The protein is from Streptomyces orinoci, a genus renowned for antibiotic production, which further supports the antibiotic biosynthesis pathway assignment, though this organism-level inference requires recognizing Actinomycetota/Streptomycetaceae context from sequence composition."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 1897,
  "benchmark_sequence_sha256": "7a2b43eb4693bca9c8e214b8ce966e5161f55926389724de9065d4baf60d4ff1",
  "current_entry_audit": {
    "entryVersion": 85,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-09-23",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1897,
  "current_source_sequence_sha256": "7a2b43eb4693bca9c8e214b8ce966e5161f55926389724de9065d4baf60d4ff1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 83,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B4ER92",
  "selected_historical_entry_version": 83,
  "selected_historical_record_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "selected_historical_source_sequence_length": 1897,
  "selected_historical_source_sequence_sha256": "7a2b43eb4693bca9c8e214b8ce966e5161f55926389724de9065d4baf60d4ff1",
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
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B4ER92\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":85,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-09-23\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Streptoverticillium orinoci\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces orinoci\",\"taxonId\":67339}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAO85893.1\",\"source\":\"EMBL\"}],\"value\":\"Modular polyketide synthase NorA\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.290\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Spectinabilin polyketide synthase system protein NorA\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Spectinabilin PKS system protein NorA\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"value\":\"Antibiotic biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"value\":\"Polyketide biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Traitcheva N.\",\"Jenke-Kodama H.\",\"He J.\",\"Dittmann E.\",\"Hertweck C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17763486\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.200700309\"}],\"citationType\":\"journal article\",\"firstPage\":\"1841\",\"id\":\"17763486\",\"journal\":\"ChemBioChem\",\"lastPage\":\"1849\",\"publicationDate\":\"2007\",\"title\":\"Non-colinear polyketide biosynthesis in the aureothin and neoaureothin pathways: an evolutionary perspective.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAO85893.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"HKI-0260\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H1",
  "excerpt": "ID   NORA_STRON              Reviewed;        1897 AA.\nAC   B4ER92;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   23-SEP-2008, sequence version 1.\nDT   28-JAN-2026, entry version 83.\nDE   RecName: Full=Spectinabilin polyketide synthase system protein NorA {ECO:0000305};\nDE            Short=Spectinabilin PKS system protein NorA {ECO:0000305};\nDE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};\nDE   AltName: Full=Modular polyketide synthase NorA {ECO:0000312|EMBL:CAO85893.1};\nGN   Name=norA {ECO:0000303|PubMed:17763486};\nOS   Streptomyces orinoci (Streptoverticillium orinoci).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=67339;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAO85893.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND SUBUNIT.\nRC   STRAIN=HKI-0260;\nRX   PubMed=17763486; DOI=10.1002/cbic.200700309;\nRA   Traitcheva N., Jenke-Kodama H., He J., Dittmann E., Hertweck C.;\nRT   \"Non-colinear polyketide biosynthesis in the aureothin and neoaureothin\nRT   pathways: an evolutionary perspective.\";\nRL   ChemBioChem 8:1841-1849(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Antibiotic biosynthesis. {ECO:0000305|PubMed:17763486}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Polyketide biosynthesis. {ECO:0000305|PubMed:17763486}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
