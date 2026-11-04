# active_site_0079

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0079.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 205 (For beta-ketoacyl synthase activity)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | Unusable review | Unusable review |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTDEAKLLSYLKRVTADLDRTTRRLREAEEQRYEAIAIVGMACRYPGGVRSPEELWRLVADEADAVSHFPQNRGWDLDTLFDPERAGGTSLTQEGGFLYDADQFDAGFFGIGPREATAMDPQQRLLLETSWEALERAGIDPATLRGSATGVFAGVMYHDYGARVVEVPEEVEGYLGNGNAGSIASGRVAFTFGFEGPAVTLDTACSSSLVALHLAAQALRQGECSLALAGGVTVMATPGVFTEFTRQGGLAADGRCKSFSTTADGTGWSEGAGMLLLERLSDAERNGHLVLAVVRGSAVNQDGASSGLTAPNGPAQQRVIRQALANARLSASEVDVVEAHGTGTKLGDPIEAQALLATYGQDRAEDRPLWLGSVKSNLGHTQAAAGVAGIIKSVMAMRHGVLPATLHVDEPTSEVDWSAGAVELLTKSRSWPETGRPRRAAVSGFGVSGTNAHVILEQAADLDVPDAAPVPEGVPVPWVVSARSADALRAQARRLRGHMAAEPGAAVVDVGHSLATARSCFEHRAVVIGRTTDDLLAGLEALAEGRGDSRVRVGAGLAGGRTGFVFAGQGSQRLGMGGRLREMFPVFGEAWDEVVAELDGRLGRPLGEVVFAEEGSEQASLVDRTEFTQPALFAFEVALFRLLESWGVVPDVVAGHSIGELAAAYVAGVLSLSDACALVVARGRLMQALPAGGAMVAVQVTEAEARRLVEGEPSGAVDIAAVNGPESVVIAGDEDVVLRVQEIVRGRGRKTKRLTVSHAFHSPRMEPMLDEFRRVAETVTYHEPRIAVVSAVSGEVAGAELRSAEYWTRHVREAVRFYDAVRCLRSEGVSTFVEVGPDGALSALGQDCLVGEEARGTEFVSTVRAGRDEAESVVAAVGAAHVRGVPVDWAAYYAPYGPRRAGLPTYAFEHQRYWLDASVRTVGDLAGLGLGSAEHPLLGAAVALADGDGVLLTGRLSLATHPWLADHRVQGAVLFPGTAFVELALRAGEQVGADCVEELTLEVPLVLPERGGVQVQVVVGAADEQGGRPVTVYSRPDEDVEDEPWARHAIGMLVPFAASAAVPAEDADFAVWPPQDAVAVDTDGMYDRLAEGGLEYGPVFQGLRSVWRRGSEVFAEVALDDTHRDGAEHDVSAVSAPETTAPVWRLEATGGGTLDALALVAYEETDRPLRANEVRVEVHAAGLNFRDVLITLGMLETKDKLGWELSGVVLETGPDVTGLAPGDRVMGVALGSFAQQAVADHRMLAKIPDGWSYAEAASVPLVFLTAYYSLVDLADLRAGQSVLIHAAAGGVGMAAVQLARHLGAEVFGTASTGKWDALRAQGLDETHIASSRDLEFEPRVLEATDGRGVDVVLDALAGEFVDASLRTLTHGGRFIEMGKTDIRDAEEVAARYPGVHYRAFDLIEAGPERVGQMLAEVLRLFDDGALTVLPVTTWDLLSAPDAFRHLSQARHIGKVVLTVPRTIDPYDTELAVVTRSRSRWRTGRSSARLTANPNSAGEFGLHPALLDAALHAIGFGEFVSDGGAGVLPFSWSGVRLLASGADALRVRVSGVGVGANEVALVVADGSGRPVASVDSLALRPVSADGIGAGRSGASRQSLFRVGWRQVAVPDQAGAGEWVALDRGAGWAQGEGCEVLPDLAALGSAVSAGRSVPRLVVAHFAADREVPVTAGVRGVTAEGLELIQSWLADERFADSRLVIMTRQAVAVDAGEGVFDLGAAALWGLVRTAQSEQPGRVVLVDVDDLDAVSRVVGIGDEPQLAVRDGRVFVPRLMRAEAIDGVPVWDPEGTLLITGASGALGGVVARHVVREWGVRHLVLASRRGAEAPGMTELVAELGELGASAAPVACDVADRDALAAVLAGIPAVHRLAGVVHAAGVLDDGVVGSLTPERLETVLAPKADAAWHLHELAAELDLSVFVLFSSAASVFGGAGQGNYAAANAFLDALAARRRADGLVATSLSWGLWDQAGGMTGQLGEADVARMSRSGVLPISVGEALPLLDAGVTGGDAWLAPVRLDLAALRQQAIATGGVPALLRDLVRVPNRRKAETGGSGAGSRSSLTDKLAGLPQEERAQELLDFVCEHTAAVLGHSGAGMVDPGRNFRELGIDSLAAVELRNRIGGVLGIRLSATLVFDYPSPVLLAGHIGEQLALDEPAPRLPVVAELERLEAAVSAARFDEDSRDDVAARLRKLLSHLDALAASPKREADDGELASASVEELFALVDQELEDL

[Multiple Choices]
A. Position 458 (For beta-ketoacyl synthase activity)
B. Position 315 (For beta-ketoacyl synthase activity)
C. Position 205 (For beta-ketoacyl synthase activity)
D. Position 93 (Proton donor)
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

> The sequence-matched UniProt annotation identifies position 205 as an active site for beta-ketoacyl synthase activity. This is a PROSITE-ProRule computational annotation, not evidence of direct experimental validation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a large modular polyketide synthase, and position 205 is a cysteine in the local sequence LDTACSSS. Ketosynthase domains in polyketide synthases commonly use a conserved catalytic cysteine, making option C a meaningful family-level inference. The other offered positions do not present the same evident catalytic-cysteine clue; position 93 is glutamine, not a likely proton-donating catalytic residue.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable ketosynthase-family feature connects the sequence at position 205 to the offered beta-ketoacyl synthase activity. The inference is credible without recalling this exact protein's database record, though sequence motifs alone do not experimentally prove the residue's role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied annotation also lists positions 340 and 380 for beta-ketoacyl synthase activity, but neither is offered. Of the actual choices, only position 205 is supported by the annotation and the catalytic-cysteine inference.


### Important caveats

- The supporting active-site annotation is computationally assigned by PROSITE-ProRule; it should not be presented as direct experimental evidence.
- The sequence match supports applying the annotation to this supplied sequence, but does not establish the exact source snapshot used by the question author.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large modular polyketide synthase, and position 205 is a cysteine in the local sequence LDTACSSS. Ketosynthase domains in polyketide synthases commonly use a conserved catalytic cysteine, making option C a meaningful family-level inference. The other offered positions do not present the same evident catalytic-cysteine clue; position 93 is glutamine, not a likely proton-donating catalytic residue.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable ketosynthase-family feature connects the sequence at position 205 to the offered beta-ketoacyl synthase activity. The inference is credible without recalling this exact protein's database record, though sequence motifs alone do not experimentally prove the residue's role."
  },
  "case_id": "active_site_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 205 as an active site for beta-ketoacyl synthase activity. This is a PROSITE-ProRule computational annotation, not evidence of direct experimental validation."
  },
  "important_caveats": [
    "The supporting active-site annotation is computationally assigned by PROSITE-ProRule; it should not be presented as direct experimental evidence.",
    "The sequence match supports applying the annotation to this supplied sequence, but does not establish the exact source snapshot used by the question author."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation also lists positions 340 and 380 for beta-ketoacyl synthase activity, but neither is offered. Of the actual choices, only position 205 is supported by the annotation and the catalytic-cysteine inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 205 as an active site for beta-ketoacyl synthase activity. This is a PROSITE-ProRule computational annotation, not evidence of direct experimental validation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a large modular polyketide synthase, and position 205 is a cysteine in the local sequence LDTACSSS. Ketosynthase domains in polyketide synthases commonly use a conserved catalytic cysteine, making option C a meaningful family-level inference. The other offered positions do not present the same evident catalytic-cysteine clue; position 93 is glutamine, not a likely proton-donating catalytic residue.",
    "missing_item_specific_fact": "",
    "reason": "A transferable ketosynthase-family feature connects the sequence at position 205 to the offered beta-ketoacyl synthase activity. The inference is credible without recalling this exact protein's database record, though sequence motifs alone do not experimentally prove the residue's role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation also lists positions 340 and 380 for beta-ketoacyl synthase activity, but neither is offered. Of the actual choices, only position 205 is supported by the annotation and the catalytic-cysteine inference."
  },
  "important_caveats": [
    "The supporting active-site annotation is computationally assigned by PROSITE-ProRule; it should not be presented as direct experimental evidence.",
    "The sequence match supports applying the annotation to this supplied sequence, but does not establish the exact source snapshot used by the question author."
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
  "benchmark_sequence_length": 2228,
  "benchmark_sequence_sha256": "01fb6bd38a5a614dfe14b817b2aa96ddb08f64e1d47b6084691f5e8a441f86b8",
  "current_entry_audit": {
    "entryVersion": 71,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 2228,
  "current_source_sequence_sha256": "01fb6bd38a5a614dfe14b817b2aa96ddb08f64e1d47b6084691f5e8a441f86b8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 69,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E0D204",
  "selected_historical_entry_version": 69,
  "selected_historical_record_sha256": "d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd",
  "selected_historical_source_sequence_length": 2228,
  "selected_historical_source_sequence_sha256": "01fb6bd38a5a614dfe14b817b2aa96ddb08f64e1d47b6084691f5e8a441f86b8",
  "selected_historical_version": {
    "accession": "E0D204",
    "database": "Swiss-Prot",
    "entryVersion": 69,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GFSC_STRHA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E0D204\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:54.215687+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11",
  "url": "https://rest.uniprot.org/uniprotkb/E0D204.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":71,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:54.215687+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11",
  "url": "https://rest.uniprot.org/uniprotkb/E0D204.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces halstedii\",\"taxonId\":1944}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:54.215687+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11",
  "url": "https://rest.uniprot.org/uniprotkb/E0D204.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"FD-891 synthase GfsC, module 8\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"I6XD69\",\"source\":\"UniProtKB\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Polyketide synthase GfsC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:54.215687+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11",
  "url": "https://rest.uniprot.org/uniprotkb/E0D204.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":205},\"start\":{\"modifier\":\"EXACT\",\"value\":205}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:27:54.215687+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11",
  "url": "https://rest.uniprot.org/uniprotkb/E0D204.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":340},\"start\":{\"modifier\":\"EXACT\",\"value\":340}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:27:54.215687+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11",
  "url": "https://rest.uniprot.org/uniprotkb/E0D204.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":380},\"start\":{\"modifier\":\"EXACT\",\"value\":380}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:27:54.215687+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11",
  "url": "https://rest.uniprot.org/uniprotkb/E0D204.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H1",
  "excerpt": "ID   GFSC_STRHA              Reviewed;        2228 AA.\nAC   E0D204;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2010, sequence version 1.\nDT   28-JAN-2026, entry version 69.\nDE   RecName: Full=Polyketide synthase GfsC {ECO:0000305};\nDE            EC=2.3.1.- {ECO:0000250|UniProtKB:I6XD69};\nDE   AltName: Full=FD-891 synthase GfsC, module 8;\nGN   Name=gfsC {ECO:0000303|PubMed:20589823};\nOS   Streptomyces halstedii.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=1944;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:56.450911+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd",
  "url": "https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAJ16469.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], PATHWAY, AND DOMAIN.\nRC   STRAIN=A-8890;\nRX   PubMed=20589823; DOI=10.1002/cbic.201000214;\nRA   Kudo F., Motegi A., Mizoue K., Eguchi T.;\nRT   \"Cloning and characterization of the biosynthetic gene cluster of 16-\nRT   membered macrolide antibiotic FD-891: involvement of a dual functional\nRT   cytochrome P450 monooxygenase catalyzing epoxidation and hydroxylation.\";\nRL   ChemBioChem 11:1574-1582(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:56.450911+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd",
  "url": "https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        205\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:56.450911+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 200-202",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd",
  "url": "https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        340\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:56.450911+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 203-205",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd",
  "url": "https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)

```json
{
  "entry_version": 69,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        380\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:56.450911+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 206-208",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd",
  "url": "https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 79. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
