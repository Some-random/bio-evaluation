# GO_biological_process_0064

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0064.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **D** — cytoplasmic translational elongation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPPKKSNARNASLLKEAVTNAGRSDTASTAREGSIAATFVSDSDSSTTASGPVDEKVAAVAELITTLTTNAASDKRQSAADDIAKFVEAEGVAQMVKTKILHGIATGLHNTKQPVAREGAITAIETLIKSPVSKQIEPYMITFIPVLLERLSDKAKTVCLAADSALKALITRLTPYATKQVLPLLLAGIEYSQKWQTKVGALELMQSLSKTAPRQMTTAVPDLVPPLSEVMHDTKAEAKNAGRQTMEAICELINNKDIEKFIPALIDTIANPEKVPDTVHLLGATTFVSEVLPPTLAIMVPLLSRGLNERQTAIKRKAAVIIINMCKLVEKPQIIAPFLPRLLPTLEKIQDDVADPECRQVCQNATKILTKVGIPAPGTVMDDSYEFKKLDDKALAYLKKAIGHQQITEIPEAYRPVLEYLEHIAAAMVADGNMDNDDWNGSIIPTLKAFIPTEGTVTNAVKEFRELSFGSNVKEAVAEEEEDDAEELCNCEFSLAYGARVLLNRTHLILKRGHRYGLTGANGSGKSTLMRAIANGQVEGFPPADQLKTVAVEHDLDGAHEHDNKEVQAFVLEDPVYAHLPKETVVNMLESVGFKGPMATRPVGQLSGGWRMKLALARAMLHNADILLLDEPTNHLDVINVAWLQDYLIGLKTVTSIIVSHDSSFLDIVCSDIIHLDNFKLKRYRGNLSKFVEAVPEAKAYYELGAAQQTFRFPEPGMLEGVKTKERAILKVQNAVFQYPGTDRRQLNGVTFQCSLGSRVAVVGPNGAGKSTLIKLLCGVIEPDNGVVWRHPNLRIAYVAQHAFEHIEKHTNLTPNQYIQWRYQTGEDREEMEKAARQISAEEEAAMKKVQVISGEKKVVDSVIGRRKLKNSYEYEVSWVGKLSNENSWLPRDTLIEMGFLKKVQEIDQAEAARQGLARPLTQKEIEKHLSDVGIDSEIGTHSHIRGLSGGQKVKVVIAGAMWQRPHLLVLDEPTNFLDRDSLGALKTAIDAYGGGVIMVTHSREFSEAICKEVWKVDNGELTPTGHNWVSGQGSGPRLEDKNKDEEVFDAFGNKIDVAKQKSKLSGKDLRKKRKEREARRKRGEEVSDDDE

[Multiple Choices]
A. response to amino acid
B. regulation of protein K48-linked ubiquitination
C. cellular response to tumor necrosis factor
D. cytoplasmic translational elongation
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence-matched record identifies the protein as elongation factor 3 and describes its role in cytoplasmic translation elongation. The cited function includes experimental evidence, while some mechanistic details and the GO annotation are supported by similarity or inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence contains tandem P-loop ATPase-like motifs, including the characteristic GxxxxGKT pattern, in an architecture consistent with eukaryotic elongation factor 3. Knowledge transferred from this protein family links eEF3 to ribosome-dependent translation elongation, distinguishing option D from the amino-acid response, ubiquitination regulation, and TNF response choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level sequence and architecture provide a meaningful basis for selecting D without needing this exact protein's database annotation. The motifs alone are not uniquely diagnostic, but their tandem arrangement in this large protein supports the family inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, cytoplasmic translational elongation is the clear match to the inferred protein family and annotated function.


### Important caveats

- The reviewer-only record matches the supplied sequence; its annotation draws on both experimental evidence and similarity-based inference.
- The precise historical source snapshot used by the benchmark author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence contains tandem P-loop ATPase-like motifs, including the characteristic GxxxxGKT pattern, in an architecture consistent with eukaryotic elongation factor 3. Knowledge transferred from this protein family links eEF3 to ribosome-dependent translation elongation, distinguishing option D from the amino-acid response, ubiquitination regulation, and TNF response choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level sequence and architecture provide a meaningful basis for selecting D without needing this exact protein's database annotation. The motifs alone are not uniquely diagnostic, but their tandem arrangement in this large protein supports the family inference."
  },
  "case_id": "GO_biological_process_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as elongation factor 3 and describes its role in cytoplasmic translation elongation. The cited function includes experimental evidence, while some mechanistic details and the GO annotation are supported by similarity or inference."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence; its annotation draws on both experimental evidence and similarity-based inference.",
    "The precise historical source snapshot used by the benchmark author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, cytoplasmic translational elongation is the clear match to the inferred protein family and annotated function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as elongation factor 3 and describes its role in cytoplasmic translation elongation. The cited function includes experimental evidence, while some mechanistic details and the GO annotation are supported by similarity or inference.",
    "evidence_ids": ["C4", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence contains tandem P-loop ATPase-like motifs, including the characteristic GxxxxGKT pattern, in an architecture consistent with eukaryotic elongation factor 3. Knowledge transferred from this protein family links eEF3 to ribosome-dependent translation elongation, distinguishing option D from the amino-acid response, ubiquitination regulation, and TNF response choices.",
    "missing_item_specific_fact": "",
    "reason": "The family-level sequence and architecture provide a meaningful basis for selecting D without needing this exact protein's database annotation. The motifs alone are not uniquely diagnostic, but their tandem arrangement in this large protein supports the family inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, cytoplasmic translational elongation is the clear match to the inferred protein family and annotated function."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence; its annotation draws on both experimental evidence and similarity-based inference.",
    "The precise historical source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A139AVY4 is annotated as Elongation factor 3 (eEF3), a ribosome-dependent ATPase functioning in cytoplasmic translation elongation. The GO annotation GO:0002182 (cytoplasmic translational elongation) is assigned with IGI evidence from PubMed:39247690. The pathway is 'Protein biosynthesis; polypeptide chain elongation.' The GO ontology definition of GO:0002182 matches option D exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two clearly identifiable tandem ABC-ATPase domains: Walker A motifs (GPPGTGKSTLMRAIANGQVEGFPPADQ and GPNGAGKSTLIKLLCGVIEPDNG), Walker B motifs (DEPTNHLDVINVAWLQDYLIGL and DEPTNFLDRDSLGALKTAIDAYGGG), and ABC signature motifs (LSGGQKVKVVIAGAMWQRPHLLVLDEPTNFLD). No transmembrane helices are present. This tandem-ABC-ATPase-without-TM architecture is the hallmark of the ABC-F subfamily (e.g., eEF3, ABCF1), which are translation factors rather than transporters or signaling proteins. Among the four choices, only D (cytoplasmic translational elongation) is mechanistically compatible with an ABC-ATPase translation factor. Options A (response to amino acid), B (regulation of K48-linked ubiquitination), and C (cellular response to TNF) describe signaling/stress-response processes carried out by receptors, kinases, E3 ligases, or transcription factors—none of which are ABC-ATPases. The family-level inference from tandem ABC-ATPase domains → translation factor → elongation is transferable knowledge about the ABC-F protein family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The tandem ABC-ATPase domain architecture (two Walker A/B pairs, ABC signature, no TM segments) is a sequence-level family signature recognizable without prior knowledge of this specific protein. This architecture is shared by eEF3 and related ABC-F translation factors across fungi and other eukaryotes. The inference that an ABC-ATPase without transmembrane domains participates in translation (rather than amino acid sensing, ubiquitination, or TNF signaling) is a well-established family-level pattern. The four options are mechanistically distinct enough that the ABC-ATPase feature meaningfully eliminates A, B, and C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The tandem ABC-ATPase architecture unambiguously points to a translation-related function. Options A, B, and C describe signaling/stress-response pathways mechanistically unrelated to ABC-ATPase enzymes. Only D is consistent with the observed domain architecture.


### Important caveats

- The GO annotation for this entry carries IGI evidence from a 2024 PubMed paper (39247690) plus by-similarity annotations from S. cerevisiae eEF3 (P16521). The experimental evidence is relatively recent.
- The protein is from a chytrid fungus (Gonapodya prolifera); eEF3 is fungal-specific (absent in animals), so a model familiar with eEF3 from yeast or Candida would recognize the architecture, but the exact organism is irrelevant to the family-level inference.
- The reviewer-only source identifies the protein as eEF3 via UniProt accession A0A139AVY4, but the model only receives the raw sequence and four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two clearly identifiable tandem ABC-ATPase domains: Walker A motifs (GPPGTGKSTLMRAIANGQVEGFPPADQ and GPNGAGKSTLIKLLCGVIEPDNG), Walker B motifs (DEPTNHLDVINVAWLQDYLIGL and DEPTNFLDRDSLGALKTAIDAYGGG), and ABC signature motifs (LSGGQKVKVVIAGAMWQRPHLLVLDEPTNFLD). No transmembrane helices are present. This tandem-ABC-ATPase-without-TM architecture is the hallmark of the ABC-F subfamily (e.g., eEF3, ABCF1), which are translation factors rather than transporters or signaling proteins. Among the four choices, only D (cytoplasmic translational elongation) is mechanistically compatible with an ABC-ATPase translation factor. Options A (response to amino acid), B (regulation of K48-linked ubiquitination), and C (cellular response to TNF) describe signaling/stress-response processes carried out by receptors, kinases, E3 ligases, or transcription factors—none of which are ABC-ATPases. The family-level inference from tandem ABC-ATPase domains → translation factor → elongation is transferable knowledge about the ABC-F protein family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The tandem ABC-ATPase domain architecture (two Walker A/B pairs, ABC signature, no TM segments) is a sequence-level family signature recognizable without prior knowledge of this specific protein. This architecture is shared by eEF3 and related ABC-F translation factors across fungi and other eukaryotes. The inference that an ABC-ATPase without transmembrane domains participates in translation (rather than amino acid sensing, ubiquitination, or TNF signaling) is a well-established family-level pattern. The four options are mechanistically distinct enough that the ABC-ATPase feature meaningfully eliminates A, B, and C."
  },
  "case_id": "GO_biological_process_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "GO1",
      "H1",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A139AVY4 is annotated as Elongation factor 3 (eEF3), a ribosome-dependent ATPase functioning in cytoplasmic translation elongation. The GO annotation GO:0002182 (cytoplasmic translational elongation) is assigned with IGI evidence from PubMed:39247690. The pathway is 'Protein biosynthesis; polypeptide chain elongation.' The GO ontology definition of GO:0002182 matches option D exactly."
  },
  "important_caveats": [
    "The GO annotation for this entry carries IGI evidence from a 2024 PubMed paper (39247690) plus by-similarity annotations from S. cerevisiae eEF3 (P16521). The experimental evidence is relatively recent.",
    "The protein is from a chytrid fungus (Gonapodya prolifera); eEF3 is fungal-specific (absent in animals), so a model familiar with eEF3 from yeast or Candida would recognize the architecture, but the exact organism is irrelevant to the family-level inference.",
    "The reviewer-only source identifies the protein as eEF3 via UniProt accession A0A139AVY4, but the model only receives the raw sequence and four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The tandem ABC-ATPase architecture unambiguously points to a translation-related function. Options A, B, and C describe signaling/stress-response pathways mechanistically unrelated to ABC-ATPase enzymes. Only D is consistent with the observed domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A139AVY4 is annotated as Elongation factor 3 (eEF3), a ribosome-dependent ATPase functioning in cytoplasmic translation elongation. The GO annotation GO:0002182 (cytoplasmic translational elongation) is assigned with IGI evidence from PubMed:39247690. The pathway is 'Protein biosynthesis; polypeptide chain elongation.' The GO ontology definition of GO:0002182 matches option D exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "GO1", "H1", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two clearly identifiable tandem ABC-ATPase domains: Walker A motifs (GPPGTGKSTLMRAIANGQVEGFPPADQ and GPNGAGKSTLIKLLCGVIEPDNG), Walker B motifs (DEPTNHLDVINVAWLQDYLIGL and DEPTNFLDRDSLGALKTAIDAYGGG), and ABC signature motifs (LSGGQKVKVVIAGAMWQRPHLLVLDEPTNFLD). No transmembrane helices are present. This tandem-ABC-ATPase-without-TM architecture is the hallmark of the ABC-F subfamily (e.g., eEF3, ABCF1), which are translation factors rather than transporters or signaling proteins. Among the four choices, only D (cytoplasmic translational elongation) is mechanistically compatible with an ABC-ATPase translation factor. Options A (response to amino acid), B (regulation of K48-linked ubiquitination), and C (cellular response to TNF) describe signaling/stress-response processes carried out by receptors, kinases, E3 ligases, or transcription factors—none of which are ABC-ATPases. The family-level inference from tandem ABC-ATPase domains → translation factor → elongation is transferable knowledge about the ABC-F protein family.",
    "missing_item_specific_fact": "",
    "reason": "The tandem ABC-ATPase domain architecture (two Walker A/B pairs, ABC signature, no TM segments) is a sequence-level family signature recognizable without prior knowledge of this specific protein. This architecture is shared by eEF3 and related ABC-F translation factors across fungi and other eukaryotes. The inference that an ABC-ATPase without transmembrane domains participates in translation (rather than amino acid sensing, ubiquitination, or TNF signaling) is a well-established family-level pattern. The four options are mechanistically distinct enough that the ABC-ATPase feature meaningfully eliminates A, B, and C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The tandem ABC-ATPase architecture unambiguously points to a translation-related function. Options A, B, and C describe signaling/stress-response pathways mechanistically unrelated to ABC-ATPase enzymes. Only D is consistent with the observed domain architecture."
  },
  "important_caveats": [
    "The GO annotation for this entry carries IGI evidence from a 2024 PubMed paper (39247690) plus by-similarity annotations from S. cerevisiae eEF3 (P16521). The experimental evidence is relatively recent.",
    "The protein is from a chytrid fungus (Gonapodya prolifera); eEF3 is fungal-specific (absent in animals), so a model familiar with eEF3 from yeast or Candida would recognize the architecture, but the exact organism is irrelevant to the family-level inference.",
    "The reviewer-only source identifies the protein as eEF3 via UniProt accession A0A139AVY4, but the model only receives the raw sequence and four choices."
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
  "benchmark_sequence_length": 1092,
  "benchmark_sequence_sha256": "690cad51db32e62963020d9c268f56c8eaff38f40a1b831856f47af766704754",
  "current_entry_audit": {
    "entryVersion": 48,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-05-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1092,
  "current_source_sequence_sha256": "690cad51db32e62963020d9c268f56c8eaff38f40a1b831856f47af766704754",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 47,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A139AVY4",
  "selected_historical_entry_version": 47,
  "selected_historical_record_sha256": "f5583d453bb640e57a634cad7f6f94f5135da55d2628b07b6202933300efe260",
  "selected_historical_source_sequence_length": 1092,
  "selected_historical_source_sequence_sha256": "690cad51db32e62963020d9c268f56c8eaff38f40a1b831856f47af766704754",
  "selected_historical_version": {
    "accession": "A0A139AVY4",
    "database": "Swiss-Prot",
    "entryVersion": 47,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "EF3_GONPJ",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A139AVY4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A139AVY4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:25.720658+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848",
  "url": "https://rest.uniprot.org/uniprotkb/A0A139AVY4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A139AVY4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":48,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-05-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:25.720658+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848",
  "url": "https://rest.uniprot.org/uniprotkb/A0A139AVY4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A139AVY4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Monoblepharis prolifera\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000070544\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Fungi incertae sedis\",\"chytridiomyceta\",\"Monoblepharomycota\",\"Monoblepharidomycetes\",\"Monoblepharidales\",\"Gonapodyaceae\",\"Gonapodya\"],\"scientificName\":\"Gonapodya prolifera (strain JEL478)\",\"taxonId\":1344416}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:25.720658+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848",
  "url": "https://rest.uniprot.org/uniprotkb/A0A139AVY4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A139AVY4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Eukaryotic elongation factor 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"eEF3\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P16521\",\"source\":\"UniProtKB\"}],\"value\":\"3.6.4.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Elongation factor 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"EF-3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:25.720658+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848",
  "url": "https://rest.uniprot.org/uniprotkb/A0A139AVY4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A139AVY4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P16521\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39247690\",\"source\":\"PubMed\"}],\"value\":\"Ribosome-dependent ATPase that functions in cytoplasmic translation elongation (PubMed:39247690). Required for the ATP-dependent release of deacylated tRNA from the ribosomal E-site during protein biosynthesis (By similarity). Stimulates the eEF1A-dependent binding of aminoacyl-tRNA to the ribosomal A-site, which has reduced affinity for tRNA as long as the E-site is occupied (By similarity). Assists translation termination by stimulating the release of nascent protein from the ribosome by release factors (By similarity)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:25.720658+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848",
  "url": "https://rest.uniprot.org/uniprotkb/A0A139AVY4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A139AVY4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93796\",\"source\":\"UniProtKB\"}],\"value\":\"Protein biosynthesis; polypeptide chain elongation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:25.720658+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848",
  "url": "https://rest.uniprot.org/uniprotkb/A0A139AVY4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A139AVY4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000316\",\"id\":\"39247690\",\"source\":\"PubMed\"}],\"id\":\"GO:0002182\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:cytoplasmic translational elongation\"},{\"key\":\"GoEvidenceType\",\"value\":\"IGI:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:24:25.720658+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848",
  "url": "https://rest.uniprot.org/uniprotkb/A0A139AVY4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A139AVY4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Maldonado G.\",\"Garcia A.\",\"Herrero S.\",\"Castano I.\",\"Altmann M.\",\"Fischer R.\",\"Hernandez G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39247690\"},{\"database\":\"DOI\",\"id\":\"10.3389/fmicb.2024.1438900\"}],\"citationType\":\"journal article\",\"firstPage\":\"1438900\",\"id\":\"39247690\",\"journal\":\"Front. Microbiol.\",\"lastPage\":\"1438900\",\"publicationDate\":\"2024\",\"title\":\"The gene YEF3 function encoding translation elongation factor eEF3 is partially conserved across fungi.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:25.720658+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848",
  "url": "https://rest.uniprot.org/uniprotkb/A0A139AVY4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47)

```json
{
  "entry_version": 47,
  "evidence_id": "H1",
  "excerpt": "ID   EF3_GONPJ               Reviewed;        1092 AA.\nAC   A0A139AVY4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-MAY-2016, sequence version 1.\nDT   28-JAN-2026, entry version 47.\nDE   RecName: Full=Elongation factor 3 {ECO:0000305};\nDE            Short=EF-3 {ECO:0000305};\nDE            EC=3.6.4.- {ECO:0000250|UniProtKB:P16521};\nDE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};\nDE            Short=eEF3 {ECO:0000305};\nGN   Name=TEF3 {ECO:0000305};\nGN   ORFNames=M427DRAFT_119444 {ECO:0000312|EMBL:KXS20890.1};\nOS   Gonapodya prolifera (strain JEL478) (Monoblepharis prolifera).\nOC   Eukaryota; Fungi; Fungi incertae sedis; Chytridiomycota;\nOC   Chytridiomycota incertae sedis; Monoblepharidomycetes; Monoblepharidales;\nOC   Gonapodyaceae; Gonapodya.\nOX   NCBI_TaxID=1344416 {ECO:0000312|Proteomes:UP000070544};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:29.778395+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f5583d453bb640e57a634cad7f6f94f5135da55d2628b07b6202933300efe260",
  "url": "https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47)

```json
{
  "entry_version": 47,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION.\nRX   PubMed=39247690; DOI=10.3389/fmicb.2024.1438900;\nRA   Maldonado G., Garcia A., Herrero S., Castano I., Altmann M., Fischer R.,\nRA   Hernandez G.;\nRT   \"The gene YEF3 function encoding translation elongation factor eEF3 is\nRT   partially conserved across fungi.\";\nRL   Front. Microbiol. 15:1438900-1438900(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:29.778395+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f5583d453bb640e57a634cad7f6f94f5135da55d2628b07b6202933300efe260",
  "url": "https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47)

```json
{
  "entry_version": 47,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Ribosome-dependent ATPase that functions in cytoplasmic\nCC       translation elongation (PubMed:39247690). Required for the ATP-\nCC       dependent release of deacylated tRNA from the ribosomal E-site during\nCC       protein biosynthesis (By similarity). Stimulates the eEF1A-dependent\nCC       binding of aminoacyl-tRNA to the ribosomal A-site, which has reduced\nCC       affinity for tRNA as long as the E-site is occupied (By similarity).\nCC       Assists translation termination by stimulating the release of nascent\nCC       protein from the ribosome by release factors (By similarity).\nCC       {ECO:0000250|UniProtKB:P16521, ECO:0000269|PubMed:39247690}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:29.778395+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f5583d453bb640e57a634cad7f6f94f5135da55d2628b07b6202933300efe260",
  "url": "https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47)

```json
{
  "entry_version": 47,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Protein biosynthesis; polypeptide chain elongation.\nCC       {ECO:0000250|UniProtKB:O93796}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:29.778395+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f5583d453bb640e57a634cad7f6f94f5135da55d2628b07b6202933300efe260",
  "url": "https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47)

```json
{
  "entry_version": 47,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0002182; P:cytoplasmic translational elongation; IGI:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:29.778395+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f5583d453bb640e57a634cad7f6f94f5135da55d2628b07b6202933300efe260",
  "url": "https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0002182\nname: cytoplasmic translational elongation\nnamespace: biological_process\ndef: \"The successive addition of amino acid residues to a nascent polypeptide chain during protein biosynthesis in the cytoplasm.\" [GOC:hjd]\nis_a: GO:0006414 ! translational elongation\nrelationship: part_of GO:0002181 ! cytoplasmic translation\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0002182",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 15691-15698",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0043200\nname: response to amino acid\nnamespace: biological_process\nalt_id: GO:0010237\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of an amino acid stimulus. An amino acid is a carboxylic acids containing one or more amino groups.\" [GOC:ef, GOC:mlg]\nsynonym: \"response to amino acid stimulus\" EXACT [GOC:dos]\nis_a: GO:0001101 ! response to acid chemical\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043200",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 244865-244873",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0061945\nname: regulation of protein K48-linked ubiquitination\nnamespace: biological_process\ndef: \"Any process that modulates the rate, frequency or extent of protein K-48-linked ubiquitination, a protein ubiquitination process in which a polymer of ubiquitin, formed by linkages between lysine residues at position 48 of the ubiquitin monomers, is added to a protein. K48-linked ubiquitination targets the substrate protein for degradation.\" [PMID:23460740]\nis_a: GO:1902914 ! regulation of protein polyubiquitination\nrelationship: regulates GO:0070936 ! protein K48-linked ubiquitination\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0061945",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 360905-360912",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0071356\nname: cellular response to tumor necrosis factor\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a tumor necrosis factor stimulus.\" [GOC:mah]\nsynonym: \"cellular response to TNF\" EXACT [GOC:mah]\nis_a: GO:0034612 ! response to tumor necrosis factor\nis_a: GO:0071345 ! cellular response to cytokine stimulus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0071356",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 376344-376352",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
