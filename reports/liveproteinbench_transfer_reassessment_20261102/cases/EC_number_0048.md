# EC_number_0048

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0048.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 1.5.1.38

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSYGESHGKAIGCVIDGFLSNIEINFDLIQKQLDRRRPNQSKLTSNRNEKDKLVILSGFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQVSKELENKNPPSRDLVDSYGTVRYNEKEKIFMDCFNRIYDMNASMLKTDEYNKNTLTIPSIDNTYINVKTNECNINQVDNNHNNYINDKDNTFNNSEKSDEWIYLQTRCPHPYTAVQICSYILKLKNKGDSVGGIATCIIQNPPIGIGEPIFDKLEAELAKMILSIPAVKGIEFGSGFNGTYMFGSMHNDIFIPVENMSTKKESDLLYDDKGECKNMSYHSTIQNNEDQILNSTKGFMPPKNDKNFNNIDDYNVTFNNNEEKLLITKTNNCGGILAGISTGNNIVFRSAIKPVSSIQIEKETSDFYGNMCNLKVQGRHDSCILPRLPPIIEASSSMVIGDLILRQISKYGDKKLPTLFRNM

[Multiple Choices]
A. 1.5.1.32
B. 1.5.1.38
C. 5.6.2.4
D. 3.2.2.5
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

> The supplied sequence matches the UniProt entry, which assigns EC 1.5.1.38 to the FMNH2/NADP+ reaction with experimental evidence. The same protein is also annotated with EC 4.2.3.5 for chorismate synthase activity; that code is not among the choices.

Citations as saved: [C6](#evidence-c6), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has features consistent with the chorismate-synthase family. Transferable knowledge of related parasite chorismate synthases can support the inference that this family may also catalyze FMN reduction, distinguishing the offered EC 1.5.1.38 (B) from the other choices. This is a specialized family-level inference, not a consequence of chorismate-synthase identity alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could use sequence-family recognition and learned functional patterns from related proteins to favor B without recalling this exact protein's annotation. The unusual additional activity makes the inference less certain than identifying the usual chorismate-synthase activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein has another supported EC annotation, 4.2.3.5, but it is not offered. Among the listed choices, the supplied evidence supports B.


### Important caveats

- The evidence supports B as one activity of a bifunctional enzyme; the prompt's singular wording could obscure that the protein has another EC number.
- The sequence-family inference is probabilistic: generic chorismate-synthase features alone do not establish the additional FMN-reductase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with the chorismate-synthase family. Transferable knowledge of related parasite chorismate synthases can support the inference that this family may also catalyze FMN reduction, distinguishing the offered EC 1.5.1.38 (B) from the other choices. This is a specialized family-level inference, not a consequence of chorismate-synthase identity alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use sequence-family recognition and learned functional patterns from related proteins to favor B without recalling this exact protein's annotation. The unusual additional activity makes the inference less certain than identifying the usual chorismate-synthase activity."
  },
  "case_id": "EC_number_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt entry, which assigns EC 1.5.1.38 to the FMNH2/NADP+ reaction with experimental evidence. The same protein is also annotated with EC 4.2.3.5 for chorismate synthase activity; that code is not among the choices."
  },
  "important_caveats": [
    "The evidence supports B as one activity of a bifunctional enzyme; the prompt's singular wording could obscure that the protein has another EC number.",
    "The sequence-family inference is probabilistic: generic chorismate-synthase features alone do not establish the additional FMN-reductase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has another supported EC annotation, 4.2.3.5, but it is not offered. Among the listed choices, the supplied evidence supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt entry, which assigns EC 1.5.1.38 to the FMNH2/NADP+ reaction with experimental evidence. The same protein is also annotated with EC 4.2.3.5 for chorismate synthase activity; that code is not among the choices.",
    "evidence_ids": ["C6", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has features consistent with the chorismate-synthase family. Transferable knowledge of related parasite chorismate synthases can support the inference that this family may also catalyze FMN reduction, distinguishing the offered EC 1.5.1.38 (B) from the other choices. This is a specialized family-level inference, not a consequence of chorismate-synthase identity alone.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use sequence-family recognition and learned functional patterns from related proteins to favor B without recalling this exact protein's annotation. The unusual additional activity makes the inference less certain than identifying the usual chorismate-synthase activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has another supported EC annotation, 4.2.3.5, but it is not offered. Among the listed choices, the supplied evidence supports B."
  },
  "important_caveats": [
    "The evidence supports B as one activity of a bifunctional enzyme; the prompt's singular wording could obscure that the protein has another EC number.",
    "The sequence-family inference is probabilistic: generic chorismate-synthase features alone do not establish the additional FMN-reductase activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6KT66 (AROC_PLAF7) annotates EC 1.5.1.38 (FMNH2 + NADP+ = FMN + NADPH + 2H+) with experimental evidence (ECO:0000269, PubMed:31381947) as one of two catalytic activities of this bifunctional chorismate synthase from Plasmodium falciparum. The sequence in the question matches the source entry (SHA256 confirmed). The expected answer B (1.5.1.38) is directly supported by the database annotation with experimental evidence codes.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable FMN-binding motifs (e.g., GFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQ and GSGFNGTYMFGSMHNDIFIP regions) characteristic of the chorismate synthase family, a well-known FMN-dependent enzyme in the shikimate pathway. Recognition of this flavoprotein family allows elimination of EC 5.6.2.4 (chaperone-like ATPase, requires AAA+ fold absent here) and EC 3.2.2.5 (glycosylase, requires sugar-binding motifs absent here). Between the two remaining oxidoreductase options, EC 1.5.1.38 is specifically FMNH2:NADP+ oxidoreductase — the canonical reoxidation reaction for FMN-dependent enzymes — whereas EC 1.5.1.32 involves a different CH-NH substrate. A model recognizing the FMN-binding character of the protein can infer that the relevant oxidoreductase activity involves FMNH2 as the electron donor, pointing to 1.5.1.38 rather than 1.5.1.32.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The FMN-binding motifs in the sequence are transferable family-level features shared with other chorismate synthases and flavoproteins. The knowledge that FMNH2:NADP+ oxidoreductase is EC 1.5.1.38 is general enzymology. The elimination of 5.6.2.4 and 3.2.2.5 relies on fold recognition. The distinction between 1.5.1.32 and 1.5.1.38, while specific, is addressable by recognizing the FMN cofactor in the sequence and knowing that 1.5.1.38 specifically denotes FMNH2 oxidation by NADP+.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is bifunctional (EC 4.2.3.5 and EC 1.5.1.38), but EC 4.2.3.5 is not among the offered choices. Among the four options, only 1.5.1.38 is annotated for this protein. The other three options (1.5.1.32, 5.6.2.4, 3.2.2.5) are not supported by any annotation or by the sequence's structural features. No multiple defensible options exist among the given choices.


### Important caveats

- The protein is primarily known as chorismate synthase (EC 4.2.3.5, lyase); the oxidoreductase activity (EC 1.5.1.38) is a secondary bifunctional activity discovered in 2019 (PubMed:31381947). The question does not specify which catalytic activity to predict, but since 4.2.3.5 is absent from the choices, this does not create practical ambiguity.
- EC 1.5.1.38 is annotated with evidence code ECO:0000305 (curator inference from literature) for the EC number assignment, while the underlying catalytic activity has ECO:0000269 (direct assay evidence). The distinction between 1.5.1.32 and 1.5.1.38 is highly specific and relies on knowing the exact substrate (FMNH2) for 1.5.1.38.
- The reviewer-only evidence was not available to the evaluated model; the reasoning argument relies solely on sequence motifs and general flavoprotein/chorismate synthase family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable FMN-binding motifs (e.g., GFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQ and GSGFNGTYMFGSMHNDIFIP regions) characteristic of the chorismate synthase family, a well-known FMN-dependent enzyme in the shikimate pathway. Recognition of this flavoprotein family allows elimination of EC 5.6.2.4 (chaperone-like ATPase, requires AAA+ fold absent here) and EC 3.2.2.5 (glycosylase, requires sugar-binding motifs absent here). Between the two remaining oxidoreductase options, EC 1.5.1.38 is specifically FMNH2:NADP+ oxidoreductase — the canonical reoxidation reaction for FMN-dependent enzymes — whereas EC 1.5.1.32 involves a different CH-NH substrate. A model recognizing the FMN-binding character of the protein can infer that the relevant oxidoreductase activity involves FMNH2 as the electron donor, pointing to 1.5.1.38 rather than 1.5.1.32.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The FMN-binding motifs in the sequence are transferable family-level features shared with other chorismate synthases and flavoproteins. The knowledge that FMNH2:NADP+ oxidoreductase is EC 1.5.1.38 is general enzymology. The elimination of 5.6.2.4 and 3.2.2.5 relies on fold recognition. The distinction between 1.5.1.32 and 1.5.1.38, while specific, is addressable by recognizing the FMN cofactor in the sequence and knowing that 1.5.1.38 specifically denotes FMNH2 oxidation by NADP+."
  },
  "case_id": "EC_number_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "H1",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6KT66 (AROC_PLAF7) annotates EC 1.5.1.38 (FMNH2 + NADP+ = FMN + NADPH + 2H+) with experimental evidence (ECO:0000269, PubMed:31381947) as one of two catalytic activities of this bifunctional chorismate synthase from Plasmodium falciparum. The sequence in the question matches the source entry (SHA256 confirmed). The expected answer B (1.5.1.38) is directly supported by the database annotation with experimental evidence codes."
  },
  "important_caveats": [
    "The protein is primarily known as chorismate synthase (EC 4.2.3.5, lyase); the oxidoreductase activity (EC 1.5.1.38) is a secondary bifunctional activity discovered in 2019 (PubMed:31381947). The question does not specify which catalytic activity to predict, but since 4.2.3.5 is absent from the choices, this does not create practical ambiguity.",
    "EC 1.5.1.38 is annotated with evidence code ECO:0000305 (curator inference from literature) for the EC number assignment, while the underlying catalytic activity has ECO:0000269 (direct assay evidence). The distinction between 1.5.1.32 and 1.5.1.38 is highly specific and relies on knowing the exact substrate (FMNH2) for 1.5.1.38.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning argument relies solely on sequence motifs and general flavoprotein/chorismate synthase family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is bifunctional (EC 4.2.3.5 and EC 1.5.1.38), but EC 4.2.3.5 is not among the offered choices. Among the four options, only 1.5.1.38 is annotated for this protein. The other three options (1.5.1.32, 5.6.2.4, 3.2.2.5) are not supported by any annotation or by the sequence's structural features. No multiple defensible options exist among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6KT66 (AROC_PLAF7) annotates EC 1.5.1.38 (FMNH2 + NADP+ = FMN + NADPH + 2H+) with experimental evidence (ECO:0000269, PubMed:31381947) as one of two catalytic activities of this bifunctional chorismate synthase from Plasmodium falciparum. The sequence in the question matches the source entry (SHA256 confirmed). The expected answer B (1.5.1.38) is directly supported by the database annotation with experimental evidence codes.",
    "evidence_ids": ["C4", "C6", "H1", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable FMN-binding motifs (e.g., GFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQ and GSGFNGTYMFGSMHNDIFIP regions) characteristic of the chorismate synthase family, a well-known FMN-dependent enzyme in the shikimate pathway. Recognition of this flavoprotein family allows elimination of EC 5.6.2.4 (chaperone-like ATPase, requires AAA+ fold absent here) and EC 3.2.2.5 (glycosylase, requires sugar-binding motifs absent here). Between the two remaining oxidoreductase options, EC 1.5.1.38 is specifically FMNH2:NADP+ oxidoreductase — the canonical reoxidation reaction for FMN-dependent enzymes — whereas EC 1.5.1.32 involves a different CH-NH substrate. A model recognizing the FMN-binding character of the protein can infer that the relevant oxidoreductase activity involves FMNH2 as the electron donor, pointing to 1.5.1.38 rather than 1.5.1.32.",
    "missing_item_specific_fact": "",
    "reason": "The FMN-binding motifs in the sequence are transferable family-level features shared with other chorismate synthases and flavoproteins. The knowledge that FMNH2:NADP+ oxidoreductase is EC 1.5.1.38 is general enzymology. The elimination of 5.6.2.4 and 3.2.2.5 relies on fold recognition. The distinction between 1.5.1.32 and 1.5.1.38, while specific, is addressable by recognizing the FMN cofactor in the sequence and knowing that 1.5.1.38 specifically denotes FMNH2 oxidation by NADP+."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is bifunctional (EC 4.2.3.5 and EC 1.5.1.38), but EC 4.2.3.5 is not among the offered choices. Among the four options, only 1.5.1.38 is annotated for this protein. The other three options (1.5.1.32, 5.6.2.4, 3.2.2.5) are not supported by any annotation or by the sequence's structural features. No multiple defensible options exist among the given choices."
  },
  "important_caveats": [
    "The protein is primarily known as chorismate synthase (EC 4.2.3.5, lyase); the oxidoreductase activity (EC 1.5.1.38) is a secondary bifunctional activity discovered in 2019 (PubMed:31381947). The question does not specify which catalytic activity to predict, but since 4.2.3.5 is absent from the choices, this does not create practical ambiguity.",
    "EC 1.5.1.38 is annotated with evidence code ECO:0000305 (curator inference from literature) for the EC number assignment, while the underlying catalytic activity has ECO:0000269 (direct assay evidence). The distinction between 1.5.1.32 and 1.5.1.38 is highly specific and relies on knowing the exact substrate (FMNH2) for 1.5.1.38.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning argument relies solely on sequence motifs and general flavoprotein/chorismate synthase family knowledge."
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
  "benchmark_sequence_length": 527,
  "benchmark_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "current_entry_audit": {
    "entryVersion": 91,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 527,
  "current_source_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 89,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C6KT66",
  "selected_historical_entry_version": 89,
  "selected_historical_record_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "selected_historical_source_sequence_length": 527,
  "selected_historical_source_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "selected_historical_version": {
    "accession": "C6KT66",
    "database": "Swiss-Prot",
    "entryVersion": 89,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AROC_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C6KT66\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":91,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.38\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"Chorismate synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"value\":\"PfCS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:21021\"}}],\"reaction\":{\"ecNumber\":\"4.2.3.5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"name\":\"5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:21020\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57701\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:21626\"}}],\"reaction\":{\"ecNumber\":\"1.5.1.38\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"name\":\"FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:21624\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Fitzpatrick T.\",\"Ricken S.\",\"Lanzer M.\",\"Amrhein N.\",\"Macheroux P.\",\"Kappes B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11298276\"},{\"database\":\"DOI\",\"id\":\"10.1046/j.1365-2958.2001.02366.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"65\",\"id\":\"11298276\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"75\",\"publicationDate\":\"2001\",\"title\":\"Subcellular localization and characterization of chorismate synthase in the apicomplexan Plasmodium falciparum.\",\"volume\":\"40\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"DD2\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Khera H.K.\",\"Singh S.K.\",\"Singh S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31381947\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2019.111202\"}],\"citationType\":\"journal article\",\"firstPage\":\"111202\",\"id\":\"31381947\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"111202\",\"publicationDate\":\"2019\",\"title\":\"Chorismate synthase from malaria parasites is bifunctional enzyme.\",\"volume\":\"233\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H1",
  "excerpt": "ID   AROC_PLAF7              Reviewed;         527 AA.\nAC   C6KT66;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 89.\nDE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:11298276, ECO:0000303|PubMed:31381947};\nDE            Short=PfCS {ECO:0000303|PubMed:11298276};\nDE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};\nDE            EC=4.2.3.5 {ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};\nGN   Name=CS {ECO:0000305}; Synonyms=AROC {ECO:0000303|PubMed:11298276};\nGN   ORFNames=PF3D7_0623000 {ECO:0000312|EMBL:CAG25042.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:11298276, ECO:0000303|PubMed:31381947};\nDE            Short=PfCS {ECO:0000303|PubMed:11298276};\nDE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};\nDE            EC=4.2.3.5 {ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, AND DEVELOPMENTAL\nRP   STAGE.\nRC   STRAIN=DD2 {ECO:0000303|PubMed:11298276};\nRX   PubMed=11298276; DOI=10.1046/j.1365-2958.2001.02366.x;\nRA   Fitzpatrick T., Ricken S., Lanzer M., Amrhein N., Macheroux P., Kappes B.;\nRT   \"Subcellular localization and characterization of chorismate synthase in\nRT   the apicomplexan Plasmodium falciparum.\";\nRL   Mol. Microbiol. 40:65-75(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=31381947; DOI=10.1016/j.molbiopara.2019.111202;\nRA   Khera H.K., Singh S.K., Singh S.;\nRT   \"Chorismate synthase from malaria parasites is bifunctional enzyme.\";\nRL   Mol. Biochem. Parasitol. 233:111202-111202(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate +\nCC         phosphate; Xref=Rhea:RHEA:21020, ChEBI:CHEBI:29748,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57701; EC=4.2.3.5;\nCC         Evidence={ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:21021;\nCC         Evidence={ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=FMNH2 + NADP(+) = FMN + NADPH + 2 H(+); Xref=Rhea:RHEA:21624,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57618, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:58349; EC=1.5.1.38;\nCC         Evidence={ECO:0000269|PubMed:31381947};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:21626;\nCC         Evidence={ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 48. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
