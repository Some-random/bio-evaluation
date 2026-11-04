# EC_number_0118

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0118.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 3.6.1.5

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKSLIGTLGLYCLFILTNNVVSSYGDDLYPLTIMHTNDFHARFEETNVKGNPCKSGEKCIGGLARVLHTIKKIIKEQEKKNIESLYINAGDNFQGTIWYNIGRWNVTSELMNIQPPDVMVLGNHEFDHGIDGLLPFLNNMDKTEIVVANMDARDEPQVAKKIKPFTIIKKKYRNIGVIGVVVEEVPDLANTGKLKFRNESEAILEAARNLKKEDPSVNIIIVVSHVGFDVDKIIAERTGSEVDIIVGGHSHTVLYTGTPPGPEKPEDNYPYVYNHPSGNKVLVVQAVCHAKYVGNLTVFFDKKGKVVTYEGAPIYMDTKVEQDKDVLEAMKPWRKLIDEKTKLVVGRTNVDLPRDICRSEECALGNLYTDSMIYAFGGKENCKSGSTWTTAPIAFVHAGAMRSSLHQGDILYSDALLLSPFTNMVVAYDLPGAQLKAALEFSAAPKNEDEKRRFLQMSGLKVTYNMSRAANNRIVDLKVRTNVCPYDQYENLDEKKTYRVVSPSFLQGGGDGFKMLRDYAKNIQNQKIDLDALVDYLKKFSPLAPKAEGRITIIH

[Multiple Choices]
A. 3.4.21.62
B. 3.6.1.5
C. 5.3.1.8
D. 5.6.2.1
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

> The sequence-matched UniProt entry assigns EC 3.6.1.5 and gives the corresponding ribonucleoside-triphosphate hydrolysis reaction with ECO:0000269 evidence citing a publication. This supports choice B, although the cited primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-peptide-like region and conserved motifs consistent with the extracellular apyrase/NTPDase family, including the histidine-containing regions around “SHVGFD” and “GGHSHT.” Transferable knowledge of this family supports nucleotide-triphosphate hydrolysis (EC 3.6.1.5), distinguishing B from the offered protease and isomerase alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features provide a meaningful basis to choose among these alternatives without recalling this protein’s database record. They support the EC class, though the precise activity assignment is a prediction rather than a certainty from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives represent substantially different enzyme activities, and the sequence features favor the nucleotide-triphosphatase option.


### Important caveats

- The reviewer-only annotation supports the key but was not available as original input.
- The sequence-based family inference is probabilistic and does not independently establish every detail of substrate specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region and conserved motifs consistent with the extracellular apyrase/NTPDase family, including the histidine-containing regions around “SHVGFD” and “GGHSHT.” Transferable knowledge of this family supports nucleotide-triphosphate hydrolysis (EC 3.6.1.5), distinguishing B from the offered protease and isomerase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features provide a meaningful basis to choose among these alternatives without recalling this protein’s database record. They support the EC class, though the precise activity assignment is a prediction rather than a certainty from sequence alone."
  },
  "case_id": "EC_number_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.6.1.5 and gives the corresponding ribonucleoside-triphosphate hydrolysis reaction with ECO:0000269 evidence citing a publication. This supports choice B, although the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not available as original input.",
    "The sequence-based family inference is probabilistic and does not independently establish every detail of substrate specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives represent substantially different enzyme activities, and the sequence features favor the nucleotide-triphosphatase option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.6.1.5 and gives the corresponding ribonucleoside-triphosphate hydrolysis reaction with ECO:0000269 evidence citing a publication. This supports choice B, although the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region and conserved motifs consistent with the extracellular apyrase/NTPDase family, including the histidine-containing regions around “SHVGFD” and “GGHSHT.” Transferable knowledge of this family supports nucleotide-triphosphate hydrolysis (EC 3.6.1.5), distinguishing B from the offered protease and isomerase alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features provide a meaningful basis to choose among these alternatives without recalling this protein’s database record. They support the EC class, though the precise activity assignment is a prediction rather than a certainty from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives represent substantially different enzyme activities, and the sequence features favor the nucleotide-triphosphatase option."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not available as original input.",
    "The sequence-based family inference is probabilistic and does not independently establish every detail of substrate specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q95P65 (APY_GLOMM) is annotated with EC=3.6.1.5, supported by experimental evidence (ECO:0000269, PubMed:20351782). The catalytic reaction is: a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+). The benchmark sequence (555 AA, sha256 match) is identical to the annotated entry. The annotation is experimental, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'MKSLIGTLGLYCLFILTNNVVSSYGDD' is a classic hydrophobic signal peptide indicating a secreted protein. This strongly disfavors EC 5.3.1.8 (triose-phosphate isomerase, a cytoplasmic glycolytic enzyme with a canonical TIM-barrel fold and highly conserved catalytic residues) and EC 5.6.2.1 (protein chaperone, a cytoplasmic/nuclear ATP-dependent folding machine). Between the remaining hydrolase options, EC 3.4.21.62 (a serine endopeptidase) requires a well-known catalytic triad (His-Asp-Ser) embedded in a trypsin/chymotrypsin-like fold with motifs such as GDSGGP; the supplied sequence lacks these hallmarks. By elimination of C, D (wrong cellular compartment / wrong fold class) and A (absent serine-protease catalytic architecture), option B (EC 3.6.1.5, a secreted apyrase/nucleotidase acting on ribonucleoside triphosphates) is the only remaining viable choice. The inference uses transferable knowledge of signal-peptide biology, enzyme-class localization, and serine-protease sequence signatures learned from many other proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate options C and D via the signal peptide (secreted vs. cytoplasmic), eliminate A via absence of serine-protease catalytic motifs, and arrive at B by elimination. This is a concrete, transferable chain of reasoning that does not require prior knowledge of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (3, 5) and very different enzyme types (serine protease, nucleotidase, TIM, chaperone). The signal peptide and absence of protease motifs provide a clear discrimination path. No two options are genuinely indistinguishable from the sequence.


### Important caveats

- The positive identification of EC 3.6.1.5 (as opposed to, say, EC 3.6.1.3 or another nucleotidase EC) relies primarily on elimination of the other three offered choices rather than on a unique sequence signature for 3.6.1.5 specifically.
- The UniProt name '5'-nucleotidase-related protein' hints at structural relation to 5'-nucleotidases, but the actual EC assignment (3.6.1.5, apyrase-type) was determined experimentally; a model might confuse this with a true 5'-nucleotidase (EC 3.1.3.5) if that were an option, but it is not among the four choices.
- EC 5.6.2.1 is an unusual/rare EC number; its plausibility as a distractor is low for a secreted protein, making elimination straightforward.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MKSLIGTLGLYCLFILTNNVVSSYGDD' is a classic hydrophobic signal peptide indicating a secreted protein. This strongly disfavors EC 5.3.1.8 (triose-phosphate isomerase, a cytoplasmic glycolytic enzyme with a canonical TIM-barrel fold and highly conserved catalytic residues) and EC 5.6.2.1 (protein chaperone, a cytoplasmic/nuclear ATP-dependent folding machine). Between the remaining hydrolase options, EC 3.4.21.62 (a serine endopeptidase) requires a well-known catalytic triad (His-Asp-Ser) embedded in a trypsin/chymotrypsin-like fold with motifs such as GDSGGP; the supplied sequence lacks these hallmarks. By elimination of C, D (wrong cellular compartment / wrong fold class) and A (absent serine-protease catalytic architecture), option B (EC 3.6.1.5, a secreted apyrase/nucleotidase acting on ribonucleoside triphosphates) is the only remaining viable choice. The inference uses transferable knowledge of signal-peptide biology, enzyme-class localization, and serine-protease sequence signatures learned from many other proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate options C and D via the signal peptide (secreted vs. cytoplasmic), eliminate A via absence of serine-protease catalytic motifs, and arrive at B by elimination. This is a concrete, transferable chain of reasoning that does not require prior knowledge of this specific protein's database annotation."
  },
  "case_id": "EC_number_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q95P65 (APY_GLOMM) is annotated with EC=3.6.1.5, supported by experimental evidence (ECO:0000269, PubMed:20351782). The catalytic reaction is: a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+). The benchmark sequence (555 AA, sha256 match) is identical to the annotated entry. The annotation is experimental, not merely computational."
  },
  "important_caveats": [
    "The positive identification of EC 3.6.1.5 (as opposed to, say, EC 3.6.1.3 or another nucleotidase EC) relies primarily on elimination of the other three offered choices rather than on a unique sequence signature for 3.6.1.5 specifically.",
    "The UniProt name '5'-nucleotidase-related protein' hints at structural relation to 5'-nucleotidases, but the actual EC assignment (3.6.1.5, apyrase-type) was determined experimentally; a model might confuse this with a true 5'-nucleotidase (EC 3.1.3.5) if that were an option, but it is not among the four choices.",
    "EC 5.6.2.1 is an unusual/rare EC number; its plausibility as a distractor is low for a secreted protein, making elimination straightforward."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (3, 5) and very different enzyme types (serine protease, nucleotidase, TIM, chaperone). The signal peptide and absence of protease motifs provide a clear discrimination path. No two options are genuinely indistinguishable from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q95P65 (APY_GLOMM) is annotated with EC=3.6.1.5, supported by experimental evidence (ECO:0000269, PubMed:20351782). The catalytic reaction is: a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+). The benchmark sequence (555 AA, sha256 match) is identical to the annotated entry. The annotation is experimental, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'MKSLIGTLGLYCLFILTNNVVSSYGDD' is a classic hydrophobic signal peptide indicating a secreted protein. This strongly disfavors EC 5.3.1.8 (triose-phosphate isomerase, a cytoplasmic glycolytic enzyme with a canonical TIM-barrel fold and highly conserved catalytic residues) and EC 5.6.2.1 (protein chaperone, a cytoplasmic/nuclear ATP-dependent folding machine). Between the remaining hydrolase options, EC 3.4.21.62 (a serine endopeptidase) requires a well-known catalytic triad (His-Asp-Ser) embedded in a trypsin/chymotrypsin-like fold with motifs such as GDSGGP; the supplied sequence lacks these hallmarks. By elimination of C, D (wrong cellular compartment / wrong fold class) and A (absent serine-protease catalytic architecture), option B (EC 3.6.1.5, a secreted apyrase/nucleotidase acting on ribonucleoside triphosphates) is the only remaining viable choice. The inference uses transferable knowledge of signal-peptide biology, enzyme-class localization, and serine-protease sequence signatures learned from many other proteins.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate options C and D via the signal peptide (secreted vs. cytoplasmic), eliminate A via absence of serine-protease catalytic motifs, and arrive at B by elimination. This is a concrete, transferable chain of reasoning that does not require prior knowledge of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (3, 5) and very different enzyme types (serine protease, nucleotidase, TIM, chaperone). The signal peptide and absence of protease motifs provide a clear discrimination path. No two options are genuinely indistinguishable from the sequence."
  },
  "important_caveats": [
    "The positive identification of EC 3.6.1.5 (as opposed to, say, EC 3.6.1.3 or another nucleotidase EC) relies primarily on elimination of the other three offered choices rather than on a unique sequence signature for 3.6.1.5 specifically.",
    "The UniProt name '5'-nucleotidase-related protein' hints at structural relation to 5'-nucleotidases, but the actual EC assignment (3.6.1.5, apyrase-type) was determined experimentally; a model might confuse this with a true 5'-nucleotidase (EC 3.1.3.5) if that were an option, but it is not among the four choices.",
    "EC 5.6.2.1 is an unusual/rare EC number; its plausibility as a distractor is low for a secreted protein, making elimination straightforward."
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
  "benchmark_sequence_length": 555,
  "benchmark_sequence_sha256": "881429cdee022e789feb0de1032bd5397cddc0acbccdc7813dfdf72b98b7d5e1",
  "current_entry_audit": {
    "entryVersion": 84,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-12-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 555,
  "current_source_sequence_sha256": "881429cdee022e789feb0de1032bd5397cddc0acbccdc7813dfdf72b98b7d5e1",
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
  "requested_accession": "Q95P65",
  "selected_historical_entry_version": 83,
  "selected_historical_record_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "selected_historical_source_sequence_length": 555,
  "selected_historical_source_sequence_sha256": "881429cdee022e789feb0de1032bd5397cddc0acbccdc7813dfdf72b98b7d5e1",
  "selected_historical_version": {
    "accession": "Q95P65",
    "database": "Swiss-Prot",
    "entryVersion": 83,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "APY_GLOMM",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q95P65\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":84,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-12-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Savannah tsetse fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAK63848.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Hippoboscoidea\",\"Glossinidae\",\"Glossina\"],\"scientificName\":\"Glossina morsitans morsitans\",\"taxonId\":37546}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"3.6.1.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"5'-nucleotidase-related protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"5'Nuc\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.6.1.5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"name\":\"a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:36795\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58043\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61557\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Caljon G.\",\"De Ridder K.\",\"De Baetselier P.\",\"Coosemans M.\",\"Van Den Abbeele J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20351782\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0009671\"}],\"citationType\":\"journal article\",\"firstPage\":\"e9671\",\"id\":\"20351782\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e9671\",\"publicationDate\":\"2010\",\"title\":\"Identification of a tsetse fly salivary protein with dual inhibitory action on human platelet aggregation.\",\"volume\":\"5\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H1",
  "excerpt": "ID   APY_GLOMM               Reviewed;         555 AA.\nAC   Q95P65; D3TRV7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-DEC-2001, sequence version 1.\nDT   28-JAN-2026, entry version 83.\nDE   RecName: Full=5'-nucleotidase-related protein {ECO:0000303|PubMed:20351782};\nDE            Short=5'Nuc {ECO:0000303|PubMed:20351782};\nDE            EC=3.6.1.5 {ECO:0000269|PubMed:20351782};\nDE   Flags: Precursor;\nOS   Glossina morsitans morsitans (Savannah tsetse fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Hippoboscoidea;\nOC   Glossinidae; Glossina.\nOX   NCBI_TaxID=37546 {ECO:0000312|EMBL:AAK63848.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=5'-nucleotidase-related protein {ECO:0000303|PubMed:20351782};\nDE            Short=5'Nuc {ECO:0000303|PubMed:20351782};\nDE            EC=3.6.1.5 {ECO:0000269|PubMed:20351782};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR LOCATION, TISSUE SPECIFICITY,\nRP   AND DISRUPTION PHENOTYPE.\nRX   PubMed=20351782; DOI=10.1371/journal.pone.0009671;\nRA   Caljon G., De Ridder K., De Baetselier P., Coosemans M.,\nRA   Van Den Abbeele J.;\nRT   \"Identification of a tsetse fly salivary protein with dual inhibitory\nRT   action on human platelet aggregation.\";\nRL   PLoS ONE 5:e9671-e9671(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside\nCC         5'-phosphate + 2 phosphate + 2 H(+); Xref=Rhea:RHEA:36795,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:58043, ChEBI:CHEBI:61557; EC=3.6.1.5;\nCC         Evidence={ECO:0000269|PubMed:20351782};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
