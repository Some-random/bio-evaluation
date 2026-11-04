# active_site_0066

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0066.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 283 (For beta-ketoacyl synthase activity)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | Unusable review | Unusable review |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

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
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry annotates position 283 as active for beta-ketoacyl synthase activity, both in the current record and in the historical record. This is computational PROSITE-ProRule evidence, not direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a large modular polyketide synthase, whose ketosynthase domains use a conserved catalytic cysteine. Position 283 is cysteine in the sequence (in the local TACSSS motif), supporting option A; position 381 is glycine, not the corresponding catalytic cysteine. Position 2723 is beyond the 1897-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of polyketide synthase ketosynthase domains and their catalytic cysteine provides a meaningful way to distinguish the offered positions without knowing this protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, only A matches the sequence's plausible ketosynthase catalytic cysteine. The other annotated ketosynthase sites are not offered as choices.


### Important caveats

- The supporting annotation is computational and does not by itself establish experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large modular polyketide synthase, whose ketosynthase domains use a conserved catalytic cysteine. Position 283 is cysteine in the sequence (in the local TACSSS motif), supporting option A; position 381 is glycine, not the corresponding catalytic cysteine. Position 2723 is beyond the 1897-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of polyketide synthase ketosynthase domains and their catalytic cysteine provides a meaningful way to distinguish the offered positions without knowing this protein's recorded annotation."
  },
  "case_id": "active_site_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates position 283 as active for beta-ketoacyl synthase activity, both in the current record and in the historical record. This is computational PROSITE-ProRule evidence, not direct experimental confirmation."
  },
  "important_caveats": [
    "The supporting annotation is computational and does not by itself establish experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only A matches the sequence's plausible ketosynthase catalytic cysteine. The other annotated ketosynthase sites are not offered as choices."
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
    "reason": "The sequence-matched UniProt entry annotates position 283 as active for beta-ketoacyl synthase activity, both in the current record and in the historical record. This is computational PROSITE-ProRule evidence, not direct experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a large modular polyketide synthase, whose ketosynthase domains use a conserved catalytic cysteine. Position 283 is cysteine in the sequence (in the local TACSSS motif), supporting option A; position 381 is glycine, not the corresponding catalytic cysteine. Position 2723 is beyond the 1897-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of polyketide synthase ketosynthase domains and their catalytic cysteine provides a meaningful way to distinguish the offered positions without knowing this protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only A matches the sequence's plausible ketosynthase catalytic cysteine. The other annotated ketosynthase sites are not offered as choices."
  },
  "important_caveats": [
    "The supporting annotation is computational and does not by itself establish experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

No visible final review text was saved. Internal model reasoning is not a substitute for a visible review and is not published. The final-content extraction failed because the saved final content was not text.

**Saved parsed visible review:** `null`.

**Saved visible final text:** empty string (`""`).

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
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":283},\"start\":{\"modifier\":\"EXACT\",\"value\":283}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
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
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":418},\"start\":{\"modifier\":\"EXACT\",\"value\":418}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
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
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":458},\"start\":{\"modifier\":\"EXACT\",\"value\":458}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Proton acceptor; for dehydratase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01363\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1045},\"start\":{\"modifier\":\"EXACT\",\"value\":1045}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Proton donor; for dehydratase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01363\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1211},\"start\":{\"modifier\":\"EXACT\",\"value\":1211}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C10",
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
  "excerpt": "FT   ACT_SITE        283\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 171-173",
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
  "excerpt": "FT   ACT_SITE        418\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 174-176",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        458\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 177-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H6",
  "excerpt": "FT   ACT_SITE        1045\nFT                   /note=\"Proton acceptor; for dehydratase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01363\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 180-182",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H7",
  "excerpt": "FT   ACT_SITE        1211\nFT                   /note=\"Proton donor; for dehydratase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01363\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 183-185",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 66. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
