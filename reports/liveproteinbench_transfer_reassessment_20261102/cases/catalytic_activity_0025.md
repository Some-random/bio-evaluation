# catalytic_activity_0025

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0025.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose

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
A. adenosine(in) + H(+)(in) = adenosine(out) + H(+)(out)
B. deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose
C. Co(2+)(in) = Co(2+)(out)
D. 3-desmethyl okaramine B + S-adenosyl-L-methionine = okaramine B + S-adenosyl-L-homocysteine + H(+)
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record lists the reaction in choice B as catalytic activity and cites ECO:0000269 evidence linked to a publication. This supports the key, though the excerpts report the annotation and its evidence attribution rather than independently presenting experimental results.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the NEP and ITENG motifs characteristic of GH1-family beta-glucosidases, which catalyze glycoside hydrolysis. That family-level inference strongly favors the glucoside hydrolysis in B over the adenosine and cobalt transport options or the SAM-dependent methylation in D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The motifs provide a transferable, meaningful basis for distinguishing the offered reaction types. They do not alone establish the precise natural substrate, deacetylipecoside, but that finer identification is not needed to distinguish B among these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B is a glycoside hydrolysis reaction, consistent with the sequence-based GH1 beta-glucosidase inference.


### Important caveats

- The sequence motifs support enzyme-family and reaction-class inference, not independent proof of activity on deacetylipecoside specifically.
- The source annotation also reports hydrolysis of deacetylisoipecoside, a reaction not offered as a separate choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the NEP and ITENG motifs characteristic of GH1-family beta-glucosidases, which catalyze glycoside hydrolysis. That family-level inference strongly favors the glucoside hydrolysis in B over the adenosine and cobalt transport options or the SAM-dependent methylation in D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The motifs provide a transferable, meaningful basis for distinguishing the offered reaction types. They do not alone establish the precise natural substrate, deacetylipecoside, but that finer identification is not needed to distinguish B among these choices."
  },
  "case_id": "catalytic_activity_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record lists the reaction in choice B as catalytic activity and cites ECO:0000269 evidence linked to a publication. This supports the key, though the excerpts report the annotation and its evidence attribution rather than independently presenting experimental results."
  },
  "important_caveats": [
    "The sequence motifs support enzyme-family and reaction-class inference, not independent proof of activity on deacetylipecoside specifically.",
    "The source annotation also reports hydrolysis of deacetylisoipecoside, a reaction not offered as a separate choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B is a glycoside hydrolysis reaction, consistent with the sequence-based GH1 beta-glucosidase inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record lists the reaction in choice B as catalytic activity and cites ECO:0000269 evidence linked to a publication. This supports the key, though the excerpts report the annotation and its evidence attribution rather than independently presenting experimental results.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the NEP and ITENG motifs characteristic of GH1-family beta-glucosidases, which catalyze glycoside hydrolysis. That family-level inference strongly favors the glucoside hydrolysis in B over the adenosine and cobalt transport options or the SAM-dependent methylation in D.",
    "missing_item_specific_fact": "",
    "reason": "The motifs provide a transferable, meaningful basis for distinguishing the offered reaction types. They do not alone establish the precise natural substrate, deacetylipecoside, but that finer identification is not needed to distinguish B among these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B is a glycoside hydrolysis reaction, consistent with the sequence-based GH1 beta-glucosidase inference."
  },
  "important_caveats": [
    "The sequence motifs support enzyme-family and reaction-class inference, not independent proof of activity on deacetylipecoside specifically.",
    "The source annotation also reports hydrolysis of deacetylisoipecoside, a reaction not offered as a separate choice."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B6ZKM4 (sequence matched, 543 AA) explicitly annotates the catalytic activity as 'deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose' with experimental evidence (ECO:0000269, PubMed:18927081). The protein is named 'Ipecac alkaloid beta-glucosidase 2' (EC 3.2.1.-). The expected answer B matches the annotated reaction verbatim.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple well-characterized motifs of glycoside hydrolase family 1 (GH1): the 'NEP' catalytic nucleophile motif (visible in 'WITINEPESYSNFF'), the 'FHWD' motif in the catalytic pocket ('VTLFHWDVPQAL'), the 'GHNLLL' conserved segment ('VYKVGHNLLLAHAAAIQVYRDK'), and the acid/base 'ND' pair in 'VYEVND'. The ~543-residue length is consistent with GH1 beta-glucosidases. These are textbook family-level features transferable from knowledge of many GH1 members (e.g., plant beta-glucosidases, bacterial beta-galactosidases). Among the four choices, only B describes hydrolysis of a glycosidic bond releasing D-glucose (a beta-glucosidase reaction). Choice A is a nucleoside transporter reaction, C is a cobalt-ion transporter reaction, and D is a SAM-dependent methyltransferase reaction. None of these alternative enzyme classes (transporters with TM helices, methyltransferases with VIGXG/Rossmann motifs) are consistent with the observed GH1 motifs. Thus family recognition of GH1 beta-glucosidase meaningfully and uniquely selects B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH1 family motifs (NEP, FHWD, GHNLLL, ND acid/base) are extensively documented across hundreds of characterized GH1 enzymes and constitute standard transferable knowledge. Recognizing these motifs identifies the enzyme as a beta-glucosidase, which eliminates the transporter (A, C) and methyltransferase (D) alternatives. The specific substrate name 'deacetylipecoside' is part of the answer text but is not needed to distinguish the choices; the reaction TYPE (glycosidic bond hydrolysis releasing glucose) is the discriminating feature.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four distinct enzyme classes (nucleoside transporter, beta-glucosidase, metal transporter, methyltransferase). The GH1 motifs in the sequence unambiguously point to the glycosidase class, leaving only B as defensible.


### Important caveats

- The specific substrate 'deacetylipecoside' is a plant alkaloid glycoside whose name cannot be deduced from sequence alone; however, the question is answerable because only one choice is a glycosidase reaction, making the exact substrate name irrelevant to the selection.
- The UniProt annotation also lists a second activity (deacetylisoipecoside hydrolysis, C6/H5), but this is not among the choices and does not create ambiguity.
- Evidence is experimental (ECO:0000269, PubMed:18927081, J. Biol. Chem. 2008), not merely computational prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple well-characterized motifs of glycoside hydrolase family 1 (GH1): the 'NEP' catalytic nucleophile motif (visible in 'WITINEPESYSNFF'), the 'FHWD' motif in the catalytic pocket ('VTLFHWDVPQAL'), the 'GHNLLL' conserved segment ('VYKVGHNLLLAHAAAIQVYRDK'), and the acid/base 'ND' pair in 'VYEVND'. The ~543-residue length is consistent with GH1 beta-glucosidases. These are textbook family-level features transferable from knowledge of many GH1 members (e.g., plant beta-glucosidases, bacterial beta-galactosidases). Among the four choices, only B describes hydrolysis of a glycosidic bond releasing D-glucose (a beta-glucosidase reaction). Choice A is a nucleoside transporter reaction, C is a cobalt-ion transporter reaction, and D is a SAM-dependent methyltransferase reaction. None of these alternative enzyme classes (transporters with TM helices, methyltransferases with VIGXG/Rossmann motifs) are consistent with the observed GH1 motifs. Thus family recognition of GH1 beta-glucosidase meaningfully and uniquely selects B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH1 family motifs (NEP, FHWD, GHNLLL, ND acid/base) are extensively documented across hundreds of characterized GH1 enzymes and constitute standard transferable knowledge. Recognizing these motifs identifies the enzyme as a beta-glucosidase, which eliminates the transporter (A, C) and methyltransferase (D) alternatives. The specific substrate name 'deacetylipecoside' is part of the answer text but is not needed to distinguish the choices; the reaction TYPE (glycosidic bond hydrolysis releasing glucose) is the discriminating feature."
  },
  "case_id": "catalytic_activity_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKM4 (sequence matched, 543 AA) explicitly annotates the catalytic activity as 'deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose' with experimental evidence (ECO:0000269, PubMed:18927081). The protein is named 'Ipecac alkaloid beta-glucosidase 2' (EC 3.2.1.-). The expected answer B matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The specific substrate 'deacetylipecoside' is a plant alkaloid glycoside whose name cannot be deduced from sequence alone; however, the question is answerable because only one choice is a glycosidase reaction, making the exact substrate name irrelevant to the selection.",
    "The UniProt annotation also lists a second activity (deacetylisoipecoside hydrolysis, C6/H5), but this is not among the choices and does not create ambiguity.",
    "Evidence is experimental (ECO:0000269, PubMed:18927081, J. Biol. Chem. 2008), not merely computational prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (nucleoside transporter, beta-glucosidase, metal transporter, methyltransferase). The GH1 motifs in the sequence unambiguously point to the glycosidase class, leaving only B as defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKM4 (sequence matched, 543 AA) explicitly annotates the catalytic activity as 'deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose' with experimental evidence (ECO:0000269, PubMed:18927081). The protein is named 'Ipecac alkaloid beta-glucosidase 2' (EC 3.2.1.-). The expected answer B matches the annotated reaction verbatim.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple well-characterized motifs of glycoside hydrolase family 1 (GH1): the 'NEP' catalytic nucleophile motif (visible in 'WITINEPESYSNFF'), the 'FHWD' motif in the catalytic pocket ('VTLFHWDVPQAL'), the 'GHNLLL' conserved segment ('VYKVGHNLLLAHAAAIQVYRDK'), and the acid/base 'ND' pair in 'VYEVND'. The ~543-residue length is consistent with GH1 beta-glucosidases. These are textbook family-level features transferable from knowledge of many GH1 members (e.g., plant beta-glucosidases, bacterial beta-galactosidases). Among the four choices, only B describes hydrolysis of a glycosidic bond releasing D-glucose (a beta-glucosidase reaction). Choice A is a nucleoside transporter reaction, C is a cobalt-ion transporter reaction, and D is a SAM-dependent methyltransferase reaction. None of these alternative enzyme classes (transporters with TM helices, methyltransferases with VIGXG/Rossmann motifs) are consistent with the observed GH1 motifs. Thus family recognition of GH1 beta-glucosidase meaningfully and uniquely selects B.",
    "missing_item_specific_fact": "",
    "reason": "The GH1 family motifs (NEP, FHWD, GHNLLL, ND acid/base) are extensively documented across hundreds of characterized GH1 enzymes and constitute standard transferable knowledge. Recognizing these motifs identifies the enzyme as a beta-glucosidase, which eliminates the transporter (A, C) and methyltransferase (D) alternatives. The specific substrate name 'deacetylipecoside' is part of the answer text but is not needed to distinguish the choices; the reaction TYPE (glycosidic bond hydrolysis releasing glucose) is the discriminating feature."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (nucleoside transporter, beta-glucosidase, metal transporter, methyltransferase). The GH1 motifs in the sequence unambiguously point to the glycosidase class, leaving only B as defensible."
  },
  "important_caveats": [
    "The specific substrate 'deacetylipecoside' is a plant alkaloid glycoside whose name cannot be deduced from sequence alone; however, the question is answerable because only one choice is a glycosidase reaction, making the exact substrate name irrelevant to the selection.",
    "The UniProt annotation also lists a second activity (deacetylisoipecoside hydrolysis, C6/H5), but this is not among the choices and does not create ambiguity.",
    "Evidence is experimental (ECO:0000269, PubMed:18927081, J. Biol. Chem. 2008), not merely computational prediction."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:78764\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"name\":\"deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:78763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:4167\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229554\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:78888\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"name\":\"deacetylisoipecoside + H2O = deacetylisoipecoside aglycone + D-glucose\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:78887\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:4167\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58091\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229557\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:01.131375+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)

```json
{
  "evidence_id": "C7",
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
  "excerpt": "DE   RecName: Full=Ipecac alkaloid beta-glucosidase 2 {ECO:0000303|PubMed:18927081};\nDE            Short=IpeGLU2 {ECO:0000303|PubMed:18927081};\nDE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:55.242337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=deacetylipecoside + H2O = deacetylipecoside aglycone + D-\nCC         glucose; Xref=Rhea:RHEA:78763, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:58379, ChEBI:CHEBI:229554;\nCC         Evidence={ECO:0000269|PubMed:18927081};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78764;\nCC         Evidence={ECO:0000269|PubMed:18927081};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:55.242337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1",
  "url": "https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=deacetylisoipecoside + H2O = deacetylisoipecoside aglycone +\nCC         D-glucose; Xref=Rhea:RHEA:78887, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:58091, ChEBI:CHEBI:229557;\nCC         Evidence={ECO:0000269|PubMed:18927081};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78888;\nCC         Evidence={ECO:0000269|PubMed:18927081};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:55.242337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1",
  "url": "https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
