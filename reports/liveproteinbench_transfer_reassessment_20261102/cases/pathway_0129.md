# pathway_0129

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0129.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGRNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAINSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPESYSNFFGVAYDTPPKAHALKASRLLVPTTVARPSKPVRVFASTADPGTTTADQVYKVGHNLLLAHAAAIQVYRDKFQNTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQLLGPRLREFTPDQKKLLIGSYDYVGVNYYTATYVSSAQPPHDKKKAVFHTDGNFYTTDSKDGVLIGPLAGPAWLNIVPEGIYHVLHDIKENYEDPVIYITENGVYEVNDTAKTLSEARVDTTRLHYLQDHLSKVLEARHQGVRVQGYLVWSLMDNWELRAGYTSRFGLIHVDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKARPQEDDGAFDTPRKRLRKY

[Multiple Choices]
A. L-homoserine from L-aspartate: step 1/3. .
B. tetrahydrofolate biosynthesis
C. coenzyme A biosynthesis
D. Alkaloid biosynthesis. .
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

> The sequence-matched UniProt record annotates the protein to alkaloid biosynthesis, with experimental-evidence coding and a cited study that addresses its function and pathway. This supports choice D, though the cited paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a large plant beta-glucosidase: it contains features characteristic of glycoside-hydrolase enzymes, which cleave sugar groups from glycosides. Such enzymes can participate in specialized plant-metabolite processing, making alkaloid biosynthesis a credible choice among these alternatives. The other options name pathways whose characteristic enzymes are not beta-glucosidases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and transferable knowledge about plant beta-glucosidases provide a meaningful, though not conclusive, basis for distinguishing D from the offered alternatives. The sequence alone would not establish the exact substrate or pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based inference favors D over the alternatives; no other offered option is comparably supported by the apparent enzyme family.


### Important caveats

- A beta-glucosidase family assignment does not by itself prove involvement in alkaloid biosynthesis; the pathway connection is supported by the sequence-matched database annotation and cited study.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large plant beta-glucosidase: it contains features characteristic of glycoside-hydrolase enzymes, which cleave sugar groups from glycosides. Such enzymes can participate in specialized plant-metabolite processing, making alkaloid biosynthesis a credible choice among these alternatives. The other options name pathways whose characteristic enzymes are not beta-glucosidases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and transferable knowledge about plant beta-glucosidases provide a meaningful, though not conclusive, basis for distinguishing D from the offered alternatives. The sequence alone would not establish the exact substrate or pathway."
  },
  "case_id": "pathway_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to alkaloid biosynthesis, with experimental-evidence coding and a cited study that addresses its function and pathway. This supports choice D, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "A beta-glucosidase family assignment does not by itself prove involvement in alkaloid biosynthesis; the pathway connection is supported by the sequence-matched database annotation and cited study."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference favors D over the alternatives; no other offered option is comparably supported by the apparent enzyme family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to alkaloid biosynthesis, with experimental-evidence coding and a cited study that addresses its function and pathway. This supports choice D, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a large plant beta-glucosidase: it contains features characteristic of glycoside-hydrolase enzymes, which cleave sugar groups from glycosides. Such enzymes can participate in specialized plant-metabolite processing, making alkaloid biosynthesis a credible choice among these alternatives. The other options name pathways whose characteristic enzymes are not beta-glucosidases.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and transferable knowledge about plant beta-glucosidases provide a meaningful, though not conclusive, basis for distinguishing D from the offered alternatives. The sequence alone would not establish the exact substrate or pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference favors D over the alternatives; no other offered option is comparably supported by the apparent enzyme family."
  },
  "important_caveats": [
    "A beta-glucosidase family assignment does not by itself prove involvement in alkaloid biosynthesis; the pathway connection is supported by the sequence-matched database annotation and cited study."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B6ZKM4 annotates this protein as 'Ipecac alkaloid beta-glucosidase 2' (IpeGLU2) from Carapichea ipecacuanha, with pathway annotation 'Alkaloid biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:18927081). The protein functions in terpenoid-isoquinoline alkaloid biosynthesis by hydrolyzing glycosylated alkaloid intermediates. The sequence matches the reviewed entry (543 AA, SHA256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark GH1 beta-glucosidase motifs: 'WDTFTHTHPE' (catalytic acid/base region), 'FHWD' (classic GH1 signature), 'WEFGDRVKNW' (substrate-binding region), and 'NEPESYSNFFG' (conserved GH1 segment). A knowledgeable model can identify this as a glycoside hydrolase family 1 enzyme. Among the four choices: (A) L-homoserine from L-aspartate step 1/3 is catalyzed by aspartate kinase (EC 2.7.2.4), a kinase with ACT regulatory domains—completely inconsistent with a GH1 glucosidase; (B) tetrahydrofolate biosynthesis involves GTP cyclohydrolase I, dihydroneopterin aldolase, etc.—no glycosidase step exists; (C) coenzyme A biosynthesis involves pantothenate kinase, phosphopantothenoylcysteine synthetase/decarboxylase, phosphopantetheine adenylyltransferase—again no glycosidase. (D) Alkaloid biosynthesis in plants frequently involves beta-glucosidases that hydrolyze glycosylated alkaloid intermediates (e.g., terpenoid-isoquinoline, indole, and other alkaloid pathways). Thus, recognizing the enzyme as a GH1 beta-glucosidase and applying pathway biochemistry knowledge that only alkaloid biosynthesis among the listed options involves a glycosidase step allows a meaningful discrimination favoring D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The discrimination relies on identifying the protein family (GH1 beta-glucosidase) from conserved sequence motifs and then applying general pathway biochemistry: the other three pathways (aspartate kinase, folate biosynthesis, CoA biosynthesis) are well-defined and do not involve glycosidase-catalyzed steps. This is transferable knowledge about enzyme families and pathway architecture, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe pathways whose enzymatic steps are well-characterized and do not include beta-glucosidase activity. Option D (alkaloid biosynthesis) is the only listed pathway in which a beta-glucosidase plays a recognized role (hydrolysis of glycosylated alkaloid intermediates). No ambiguity exists among the offered choices given the clear GH1 identification.


### Important caveats

- Beta-glucosidases participate in many pathways not listed (flavonoid metabolism, cyanogenic glycoside catabolism, hormone conjugate hydrolysis, glucosinolate metabolism). The question's answerability depends on the constrained option set; with a broader set of choices, distinguishing alkaloid-specific from other glucosidase functions would require additional information.
- The experimental evidence (ECO:0000269) confirms the alkaloid pathway role for this specific enzyme, but the sequence-based reasoning only establishes that D is the only viable option among the four given, not that this particular glucosidase has alkaloid specificity over, say, flavonoid glycoside specificity.
- The GH1 family assignment is based on well-known conserved motifs visible in the sequence; this is standard bioinformatics inference and does not require species or organism knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark GH1 beta-glucosidase motifs: 'WDTFTHTHPE' (catalytic acid/base region), 'FHWD' (classic GH1 signature), 'WEFGDRVKNW' (substrate-binding region), and 'NEPESYSNFFG' (conserved GH1 segment). A knowledgeable model can identify this as a glycoside hydrolase family 1 enzyme. Among the four choices: (A) L-homoserine from L-aspartate step 1/3 is catalyzed by aspartate kinase (EC 2.7.2.4), a kinase with ACT regulatory domains—completely inconsistent with a GH1 glucosidase; (B) tetrahydrofolate biosynthesis involves GTP cyclohydrolase I, dihydroneopterin aldolase, etc.—no glycosidase step exists; (C) coenzyme A biosynthesis involves pantothenate kinase, phosphopantothenoylcysteine synthetase/decarboxylase, phosphopantetheine adenylyltransferase—again no glycosidase. (D) Alkaloid biosynthesis in plants frequently involves beta-glucosidases that hydrolyze glycosylated alkaloid intermediates (e.g., terpenoid-isoquinoline, indole, and other alkaloid pathways). Thus, recognizing the enzyme as a GH1 beta-glucosidase and applying pathway biochemistry knowledge that only alkaloid biosynthesis among the listed options involves a glycosidase step allows a meaningful discrimination favoring D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The discrimination relies on identifying the protein family (GH1 beta-glucosidase) from conserved sequence motifs and then applying general pathway biochemistry: the other three pathways (aspartate kinase, folate biosynthesis, CoA biosynthesis) are well-defined and do not involve glycosidase-catalyzed steps. This is transferable knowledge about enzyme families and pathway architecture, not a lookup of this specific protein's annotation."
  },
  "case_id": "pathway_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKM4 annotates this protein as 'Ipecac alkaloid beta-glucosidase 2' (IpeGLU2) from Carapichea ipecacuanha, with pathway annotation 'Alkaloid biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:18927081). The protein functions in terpenoid-isoquinoline alkaloid biosynthesis by hydrolyzing glycosylated alkaloid intermediates. The sequence matches the reviewed entry (543 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "Beta-glucosidases participate in many pathways not listed (flavonoid metabolism, cyanogenic glycoside catabolism, hormone conjugate hydrolysis, glucosinolate metabolism). The question's answerability depends on the constrained option set; with a broader set of choices, distinguishing alkaloid-specific from other glucosidase functions would require additional information.",
    "The experimental evidence (ECO:0000269) confirms the alkaloid pathway role for this specific enzyme, but the sequence-based reasoning only establishes that D is the only viable option among the four given, not that this particular glucosidase has alkaloid specificity over, say, flavonoid glycoside specificity.",
    "The GH1 family assignment is based on well-known conserved motifs visible in the sequence; this is standard bioinformatics inference and does not require species or organism knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe pathways whose enzymatic steps are well-characterized and do not include beta-glucosidase activity. Option D (alkaloid biosynthesis) is the only listed pathway in which a beta-glucosidase plays a recognized role (hydrolysis of glycosylated alkaloid intermediates). No ambiguity exists among the offered choices given the clear GH1 identification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKM4 annotates this protein as 'Ipecac alkaloid beta-glucosidase 2' (IpeGLU2) from Carapichea ipecacuanha, with pathway annotation 'Alkaloid biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:18927081). The protein functions in terpenoid-isoquinoline alkaloid biosynthesis by hydrolyzing glycosylated alkaloid intermediates. The sequence matches the reviewed entry (543 AA, SHA256 confirmed).",
    "evidence_ids": ["C5", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark GH1 beta-glucosidase motifs: 'WDTFTHTHPE' (catalytic acid/base region), 'FHWD' (classic GH1 signature), 'WEFGDRVKNW' (substrate-binding region), and 'NEPESYSNFFG' (conserved GH1 segment). A knowledgeable model can identify this as a glycoside hydrolase family 1 enzyme. Among the four choices: (A) L-homoserine from L-aspartate step 1/3 is catalyzed by aspartate kinase (EC 2.7.2.4), a kinase with ACT regulatory domains—completely inconsistent with a GH1 glucosidase; (B) tetrahydrofolate biosynthesis involves GTP cyclohydrolase I, dihydroneopterin aldolase, etc.—no glycosidase step exists; (C) coenzyme A biosynthesis involves pantothenate kinase, phosphopantothenoylcysteine synthetase/decarboxylase, phosphopantetheine adenylyltransferase—again no glycosidase. (D) Alkaloid biosynthesis in plants frequently involves beta-glucosidases that hydrolyze glycosylated alkaloid intermediates (e.g., terpenoid-isoquinoline, indole, and other alkaloid pathways). Thus, recognizing the enzyme as a GH1 beta-glucosidase and applying pathway biochemistry knowledge that only alkaloid biosynthesis among the listed options involves a glycosidase step allows a meaningful discrimination favoring D.",
    "missing_item_specific_fact": "",
    "reason": "The discrimination relies on identifying the protein family (GH1 beta-glucosidase) from conserved sequence motifs and then applying general pathway biochemistry: the other three pathways (aspartate kinase, folate biosynthesis, CoA biosynthesis) are well-defined and do not involve glycosidase-catalyzed steps. This is transferable knowledge about enzyme families and pathway architecture, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe pathways whose enzymatic steps are well-characterized and do not include beta-glucosidase activity. Option D (alkaloid biosynthesis) is the only listed pathway in which a beta-glucosidase plays a recognized role (hydrolysis of glycosylated alkaloid intermediates). No ambiguity exists among the offered choices given the clear GH1 identification."
  },
  "important_caveats": [
    "Beta-glucosidases participate in many pathways not listed (flavonoid metabolism, cyanogenic glycoside catabolism, hormone conjugate hydrolysis, glucosinolate metabolism). The question's answerability depends on the constrained option set; with a broader set of choices, distinguishing alkaloid-specific from other glucosidase functions would require additional information.",
    "The experimental evidence (ECO:0000269) confirms the alkaloid pathway role for this specific enzyme, but the sequence-based reasoning only establishes that D is the only viable option among the four given, not that this particular glucosidase has alkaloid specificity over, say, flavonoid glycoside specificity.",
    "The GH1 family assignment is based on well-known conserved motifs visible in the sequence; this is standard bioinformatics inference and does not require species or organism knowledge."
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
  "benchmark_sequence_length": 543,
  "benchmark_sequence_sha256": "a20dbd3decfa410fc38311f3c3bcb6b26c3d96d9e163353b0574db565e428c8f",
  "current_entry_audit": {
    "entryVersion": 46,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-02-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 543,
  "current_source_sequence_sha256": "a20dbd3decfa410fc38311f3c3bcb6b26c3d96d9e163353b0574db565e428c8f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 44,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B6ZKM4",
  "selected_historical_entry_version": 44,
  "selected_historical_record_sha256": "dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1",
  "selected_historical_source_sequence_length": 543,
  "selected_historical_source_sequence_sha256": "a20dbd3decfa410fc38311f3c3bcb6b26c3d96d9e163353b0574db565e428c8f",
  "selected_historical_version": {
    "accession": "B6ZKM4",
    "database": "Swiss-Prot",
    "entryVersion": 44,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GLU2_CARIP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B6ZKM4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:01.131375+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":46,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-02-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:01.131375+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ipecac\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Rubiaceae\",\"Rubioideae\",\"Palicoureeae\",\"Carapichea\"],\"scientificName\":\"Carapichea ipecacuanha\",\"synonyms\":[\"Callicocca ipecacuanha\"],\"taxonId\":77880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:01.131375+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Ipecac alkaloid beta-glucosidase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"IpeGLU2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:01.131375+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:01.131375+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Nomura T.\",\"Quesada A.L.\",\"Kutchan T.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18927081\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m806953200\"}],\"citationType\":\"journal article\",\"firstPage\":\"34650\",\"id\":\"18927081\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"34659\",\"publicationDate\":\"2008\",\"title\":\"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.\",\"volume\":\"283\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAH02545.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Root\"},{\"type\":\"TISSUE\",\"value\":\"Shoot\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:01.131375+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H1",
  "excerpt": "ID   GLU2_CARIP              Reviewed;         543 AA.\nAC   B6ZKM4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-FEB-2009, sequence version 1.\nDT   28-JAN-2026, entry version 44.\nDE   RecName: Full=Ipecac alkaloid beta-glucosidase 2 {ECO:0000303|PubMed:18927081};\nDE            Short=IpeGLU2 {ECO:0000303|PubMed:18927081};\nDE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};\nGN   Name=GLU2 {ECO:0000303|PubMed:18927081};\nOS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;\nOC   Carapichea.\nOX   NCBI_TaxID=77880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:55.242337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1",
  "url": "https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAH02545.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   TISSUE=Root, and Shoot;\nRX   PubMed=18927081; DOI=10.1074/jbc.m806953200;\nRA   Nomura T., Quesada A.L., Kutchan T.M.;\nRT   \"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis\nRT   in Psychotria ipecacuanha.\";\nRL   J. Biol. Chem. 283:34650-34659(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:55.242337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1",
  "url": "https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:18927081}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:55.242337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1",
  "url": "https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
