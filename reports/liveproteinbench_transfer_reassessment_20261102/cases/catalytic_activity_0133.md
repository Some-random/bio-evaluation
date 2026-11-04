# catalytic_activity_0133

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0133.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1-&gt;4)-beta-linkages in chitin and chitodextrins.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSLLYLVALFVASICSVTAQTWTSCNPLTTTCPPDQALGINTTFTFNKTLDDTIWNVTNGVLSHTDEGTEFTITGENQSPTMQSNFYIFFGIVESHVKMAKGAGIISSIVLQSDDLDEIDWEWVGYNTSEVQSNYFGKGNNETFNRGGYHYVPNADTEFHNYTTYWTQEKLEWWIDGKLARTLTYEDSQGAGKYYPQTPCNIRYGIWPAGIKGNAQGTIEWAGGLVDYSKAPFTMVLQSVRVHDFHTGKEYNYTDHSGSWQSIDVIAGNSTIANAIQNPPKSLSEKWAELPTGAKAGVYIGAGCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN

[Multiple Choices]
A. Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides.
B. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
C. 2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O
D. Fe(2+)(in) = Fe(2+)(out)
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

> The sequence-matched UniProt entry annotates this protein with the reaction in B (EC 3.2.1.14), citing a literature source. This is curated annotation evidence, not an independent validation of the underlying experiment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal signal-peptide-like region, a large extracellular enzyme region, and a hydrophobic C-terminal membrane-anchor-like segment, consistent with a fungal cell-wall enzyme. Its acidic motif around QSDDLDE is compatible with a chitinase-family catalytic site. Transferable knowledge of fungal chitin-remodeling enzymes therefore supports B over the unrelated indigoidine synthesis and iron transport choices, and over the distinct arabinofuranosidase reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable knowledge of secreted fungal glycosidases and chitinase catalytic motifs provide a meaningful basis for selecting B among these alternatives; the exact database annotation is not necessary for that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the only offered reaction consistent with the sequence-based chitinase inference. The annotated transglycosylase activity is not among the choices.


### Important caveats

- The source also annotates a chitin transglycosylase activity; this does not make another offered option defensible.
- The catalytic-activity annotation cites literature, but the supplied excerpts do not independently establish the details of the experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like region, a large extracellular enzyme region, and a hydrophobic C-terminal membrane-anchor-like segment, consistent with a fungal cell-wall enzyme. Its acidic motif around QSDDLDE is compatible with a chitinase-family catalytic site. Transferable knowledge of fungal chitin-remodeling enzymes therefore supports B over the unrelated indigoidine synthesis and iron transport choices, and over the distinct arabinofuranosidase reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of secreted fungal glycosidases and chitinase catalytic motifs provide a meaningful basis for selecting B among these alternatives; the exact database annotation is not necessary for that distinction."
  },
  "case_id": "catalytic_activity_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein with the reaction in B (EC 3.2.1.14), citing a literature source. This is curated annotation evidence, not an independent validation of the underlying experiment."
  },
  "important_caveats": [
    "The source also annotates a chitin transglycosylase activity; this does not make another offered option defensible.",
    "The catalytic-activity annotation cites literature, but the supplied excerpts do not independently establish the details of the experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only offered reaction consistent with the sequence-based chitinase inference. The annotated transglycosylase activity is not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein with the reaction in B (EC 3.2.1.14), citing a literature source. This is curated annotation evidence, not an independent validation of the underlying experiment.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like region, a large extracellular enzyme region, and a hydrophobic C-terminal membrane-anchor-like segment, consistent with a fungal cell-wall enzyme. Its acidic motif around QSDDLDE is compatible with a chitinase-family catalytic site. Transferable knowledge of fungal chitin-remodeling enzymes therefore supports B over the unrelated indigoidine synthesis and iron transport choices, and over the distinct arabinofuranosidase reaction.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of secreted fungal glycosidases and chitinase catalytic motifs provide a meaningful basis for selecting B among these alternatives; the exact database annotation is not necessary for that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only offered reaction consistent with the sequence-based chitinase inference. The annotated transglycosylase activity is not among the choices."
  },
  "important_caveats": [
    "The source also annotates a chitin transglycosylase activity; this does not make another offered option defensible.",
    "The catalytic-activity annotation cites literature, but the supplied excerpts do not independently establish the details of the experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4WXE6 (CRH3_ASPFU) explicitly lists EC 3.2.1.14 with the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins,' matching option B verbatim. The evidence code is ECO:0000305 (inferred by similarity), indicating the chitinase annotation is based on similarity rather than direct experimentation, but the annotation is clearly present in the database record. The protein also has an experimentally supported transglycosylase activity (EC 2.4.-.-, ECO:0000269), but among the four offered choices, B is the directly stated catalytic activity.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a tripartite architecture diagnostic of fungal Crh (Chitin Remodeling) proteins: (1) an N-terminal secretion signal peptide (MSLLYLVALFVASICSVT), (2) a large catalytic domain with features consistent with glycoside hydrolase family 18 (GH18) chitinases, and (3) a C-terminal transmembrane anchor (GCVGAALLAGFIFFFIAQRKKGR) with flanking charged residues. This SP+GH18+TM architecture is a well-known family-level signature of fungal chitinases/chitin transglycosylases. Against the alternatives: Option C (indigoidine synthase, an NRPS) requires a multi-domain protein >100 kDa with adenylation/condensation/thiolation modules, incompatible with a 363-aa protein. Option D (iron transporter, e.g., Nramp) requires a 10-12 pass transmembrane topology, incompatible with a single C-terminal TM and a large soluble catalytic domain. Option A (alpha-L-arabinofuranosidase) belongs to GH43/GH51 families with beta-propeller or (beta/alpha)8 folds and lacks the DXXDXDXE-type catalytic motif and the C-terminal TM anchor characteristic of GH18 chitinases. The GH18 TIM-barrel fold with its conserved DXXDXDXE catalytic motif (visible as a degenerate variant in the central region) and the distinctive Crh-type C-terminal membrane anchor together provide a concrete family-level inference pointing to chitinase activity (option B).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model trained on protein families can recognize the GH18 catalytic domain fold, the DXXDXDXE-type motif, and the C-terminal transmembrane anchor as hallmarks of fungal chitinases/Crh proteins. These are transferable family-level features learned from many related proteins. The protein size and domain architecture independently eliminate options C and D, while the fold and motif distinguish B from A. No target-specific database lookup is strictly required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different enzyme classes (GH43/51 arabinofuranosidase, GH18 chitinase, NRPS, membrane transporter) with incompatible sequence architectures. Only option B is consistent with the observed domain organization and family signatures.


### Important caveats

- The chitinase EC annotation (3.2.1.14) carries evidence code ECO:0000305 (inferred by similarity), meaning it is not directly experimentally demonstrated for this exact protein; the experimentally supported activity is the transglycosylase function (EC 2.4.-.-, ECO:0000269).
- The Crh proteins are primarily characterized as chitin transglycosylases rather than classical endo-chitinases, but UniProt lists both activities and the question's option B text matches the database annotation verbatim.
- The GH18 catalytic motif (DXXDXDXE) appears in a somewhat degenerate form in this sequence; recognition relies on overall fold similarity and family-level pattern matching rather than a perfect canonical motif match.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a tripartite architecture diagnostic of fungal Crh (Chitin Remodeling) proteins: (1) an N-terminal secretion signal peptide (MSLLYLVALFVASICSVT), (2) a large catalytic domain with features consistent with glycoside hydrolase family 18 (GH18) chitinases, and (3) a C-terminal transmembrane anchor (GCVGAALLAGFIFFFIAQRKKGR) with flanking charged residues. This SP+GH18+TM architecture is a well-known family-level signature of fungal chitinases/chitin transglycosylases. Against the alternatives: Option C (indigoidine synthase, an NRPS) requires a multi-domain protein >100 kDa with adenylation/condensation/thiolation modules, incompatible with a 363-aa protein. Option D (iron transporter, e.g., Nramp) requires a 10-12 pass transmembrane topology, incompatible with a single C-terminal TM and a large soluble catalytic domain. Option A (alpha-L-arabinofuranosidase) belongs to GH43/GH51 families with beta-propeller or (beta/alpha)8 folds and lacks the DXXDXDXE-type catalytic motif and the C-terminal TM anchor characteristic of GH18 chitinases. The GH18 TIM-barrel fold with its conserved DXXDXDXE catalytic motif (visible as a degenerate variant in the central region) and the distinctive Crh-type C-terminal membrane anchor together provide a concrete family-level inference pointing to chitinase activity (option B).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model trained on protein families can recognize the GH18 catalytic domain fold, the DXXDXDXE-type motif, and the C-terminal transmembrane anchor as hallmarks of fungal chitinases/Crh proteins. These are transferable family-level features learned from many related proteins. The protein size and domain architecture independently eliminate options C and D, while the fold and motif distinguish B from A. No target-specific database lookup is strictly required."
  },
  "case_id": "catalytic_activity_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXE6 (CRH3_ASPFU) explicitly lists EC 3.2.1.14 with the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins,' matching option B verbatim. The evidence code is ECO:0000305 (inferred by similarity), indicating the chitinase annotation is based on similarity rather than direct experimentation, but the annotation is clearly present in the database record. The protein also has an experimentally supported transglycosylase activity (EC 2.4.-.-, ECO:0000269), but among the four offered choices, B is the directly stated catalytic activity."
  },
  "important_caveats": [
    "The chitinase EC annotation (3.2.1.14) carries evidence code ECO:0000305 (inferred by similarity), meaning it is not directly experimentally demonstrated for this exact protein; the experimentally supported activity is the transglycosylase function (EC 2.4.-.-, ECO:0000269).",
    "The Crh proteins are primarily characterized as chitin transglycosylases rather than classical endo-chitinases, but UniProt lists both activities and the question's option B text matches the database annotation verbatim.",
    "The GH18 catalytic motif (DXXDXDXE) appears in a somewhat degenerate form in this sequence; recognition relies on overall fold similarity and family-level pattern matching rather than a perfect canonical motif match."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (GH43/51 arabinofuranosidase, GH18 chitinase, NRPS, membrane transporter) with incompatible sequence architectures. Only option B is consistent with the observed domain organization and family signatures."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXE6 (CRH3_ASPFU) explicitly lists EC 3.2.1.14 with the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins,' matching option B verbatim. The evidence code is ECO:0000305 (inferred by similarity), indicating the chitinase annotation is based on similarity rather than direct experimentation, but the annotation is clearly present in the database record. The protein also has an experimentally supported transglycosylase activity (EC 2.4.-.-, ECO:0000269), but among the four offered choices, B is the directly stated catalytic activity.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a tripartite architecture diagnostic of fungal Crh (Chitin Remodeling) proteins: (1) an N-terminal secretion signal peptide (MSLLYLVALFVASICSVT), (2) a large catalytic domain with features consistent with glycoside hydrolase family 18 (GH18) chitinases, and (3) a C-terminal transmembrane anchor (GCVGAALLAGFIFFFIAQRKKGR) with flanking charged residues. This SP+GH18+TM architecture is a well-known family-level signature of fungal chitinases/chitin transglycosylases. Against the alternatives: Option C (indigoidine synthase, an NRPS) requires a multi-domain protein >100 kDa with adenylation/condensation/thiolation modules, incompatible with a 363-aa protein. Option D (iron transporter, e.g., Nramp) requires a 10-12 pass transmembrane topology, incompatible with a single C-terminal TM and a large soluble catalytic domain. Option A (alpha-L-arabinofuranosidase) belongs to GH43/GH51 families with beta-propeller or (beta/alpha)8 folds and lacks the DXXDXDXE-type catalytic motif and the C-terminal TM anchor characteristic of GH18 chitinases. The GH18 TIM-barrel fold with its conserved DXXDXDXE catalytic motif (visible as a degenerate variant in the central region) and the distinctive Crh-type C-terminal membrane anchor together provide a concrete family-level inference pointing to chitinase activity (option B).",
    "missing_item_specific_fact": "",
    "reason": "A model trained on protein families can recognize the GH18 catalytic domain fold, the DXXDXDXE-type motif, and the C-terminal transmembrane anchor as hallmarks of fungal chitinases/Crh proteins. These are transferable family-level features learned from many related proteins. The protein size and domain architecture independently eliminate options C and D, while the fold and motif distinguish B from A. No target-specific database lookup is strictly required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (GH43/51 arabinofuranosidase, GH18 chitinase, NRPS, membrane transporter) with incompatible sequence architectures. Only option B is consistent with the observed domain organization and family signatures."
  },
  "important_caveats": [
    "The chitinase EC annotation (3.2.1.14) carries evidence code ECO:0000305 (inferred by similarity), meaning it is not directly experimentally demonstrated for this exact protein; the experimentally supported activity is the transglycosylase function (EC 2.4.-.-, ECO:0000269).",
    "The Crh proteins are primarily characterized as chitin transglycosylases rather than classical endo-chitinases, but UniProt lists both activities and the question's option B text matches the database annotation verbatim.",
    "The GH18 catalytic motif (DXXDXDXE) appears in a somewhat degenerate form in this sequence; recognition relies on overall fold similarity and family-level pattern matching rather than a perfect canonical motif match."
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
  "benchmark_sequence_length": 363,
  "benchmark_sequence_sha256": "3deb859056a8160d9cec48ee8776946ad4066ac14f699364c29390fefc1dc15d",
  "current_entry_audit": {
    "entryVersion": 100,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-04-17",
    "sequenceVersion": 2
  },
  "current_record_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 363,
  "current_source_sequence_sha256": "3deb859056a8160d9cec48ee8776946ad4066ac14f699364c29390fefc1dc15d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 98,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q4WXE6",
  "selected_historical_entry_version": 98,
  "selected_historical_record_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "selected_historical_source_sequence_length": 363,
  "selected_historical_source_sequence_sha256": "3deb859056a8160d9cec48ee8776946ad4066ac14f699364c29390fefc1dc15d",
  "selected_historical_version": {
    "accession": "Q4WXE6",
    "database": "Swiss-Prot",
    "entryVersion": 98,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH3_ASPFU",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4WXE6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":100,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-04-17\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitinase crh3\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitin transglycosylase crh3\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"name\":\"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Fang W.\",\"Sanz A.B.\",\"Bartual S.G.\",\"Wang B.\",\"Ferenbach A.T.\",\"Farkas V.\",\"Hurtado-Guerrero R.\",\"Arroyo J.\",\"van Aalten D.M.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30971696\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-019-09674-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"1669\",\"id\":\"30971696\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"1669\",\"publicationDate\":\"2019\",\"title\":\"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh transglycosylases.\",\"volume\":\"10\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H1",
  "excerpt": "ID   CRH3_ASPFU              Reviewed;         363 AA.\nAC   Q4WXE6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-APR-2007, sequence version 2.\nDT   28-JAN-2026, entry version 98.\nDE   RecName: Full=Crh-like protein 3 {ECO:0000303|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitinase crh3 {ECO:0000303|PubMed:30971696};\nDE              EC=3.2.1.14 {ECO:0000305|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh3 {ECO:0000303|PubMed:30971696};\nDE              EC=2.4.-.- {ECO:0000269|PubMed:30971696};\nDE   Flags: Precursor;\nGN   Name=crh3 {ECO:0000303|PubMed:30971696}; ORFNames=AFUA_3G09250;\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Crh-like protein 3 {ECO:0000303|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitinase crh3 {ECO:0000303|PubMed:30971696};\nDE              EC=3.2.1.14 {ECO:0000305|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh3 {ECO:0000303|PubMed:30971696};\nDE              EC=2.4.-.- {ECO:0000269|PubMed:30971696};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30971696; DOI=10.1038/s41467-019-09674-0;\nRA   Fang W., Sanz A.B., Bartual S.G., Wang B., Ferenbach A.T., Farkas V.,\nRA   Hurtado-Guerrero R., Arroyo J., van Aalten D.M.F.;\nRT   \"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh\nRT   transglycosylases.\";\nRL   Nat. Commun. 10:1669-1669(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide\nCC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;\nCC         Evidence={ECO:0000305|PubMed:30971696};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
