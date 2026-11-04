# EC_number_0087

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0087.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.3.1.290

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:58945\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.290\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"name\":\"4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:58944\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57327\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57384\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142871\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142872\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "DE   RecName: Full=Spectinabilin polyketide synthase system protein NorA {ECO:0000305};\nDE            Short=Spectinabilin PKS system protein NorA {ECO:0000305};\nDE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};\nDE   AltName: Full=Modular polyketide synthase NorA {ECO:0000312|EMBL:CAO85893.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6\nCC         NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8\nCC         CoA + 5 H2O; Xref=Rhea:RHEA:58944, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57327, ChEBI:CHEBI:57384, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:142871, ChEBI:CHEBI:142872;\nCC         EC=2.3.1.290; Evidence={ECO:0000305|PubMed:17763486};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:58945;\nCC         Evidence={ECO:0000305|PubMed:17763486};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
