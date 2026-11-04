# GO_molecular_function_0059

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0059.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — 2 iron, 2 sulfur cluster binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. collagen binding
B. D-alanine-D-alanine ligase activity
C. 2 iron, 2 sulfur cluster binding
D. trichodiene synthase activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record assigns 2 iron, 2 sulfur cluster binding, though as a keyword-based inferred annotation rather than direct experimental evidence. The record also identifies the protein as a dihydroxy-acid dehydratase, consistent with an iron-sulfur-dependent enzyme.

Citations as saved: [H6](#evidence-h6), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the dihydroxy-acid dehydratase family, whose members use an iron-sulfur cluster and have conserved cysteine features associated with cluster coordination. That family-level knowledge makes cluster binding (C) a meaningful choice over collagen binding, D-alanine-D-alanine ligase activity, or trichodiene synthase activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition and the sequence's cysteine-containing features provide a transferable basis for selecting C; the inference does not require recalling this exact protein's database entry. The family-level inference is strong but is not a direct measurement of cluster binding in this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the iron-sulfur cluster-binding activity is the one consistent with the inferred dihydroxy-acid dehydratase family.


### Important caveats

- The direct database annotation for cluster binding is computational (IEA: UniProtKB-KW), whereas the cited experimental evidence establishes the enzyme's dehydratase activity, not direct cluster binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the dihydroxy-acid dehydratase family, whose members use an iron-sulfur cluster and have conserved cysteine features associated with cluster coordination. That family-level knowledge makes cluster binding (C) a meaningful choice over collagen binding, D-alanine-D-alanine ligase activity, or trichodiene synthase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and the sequence's cysteine-containing features provide a transferable basis for selecting C; the inference does not require recalling this exact protein's database entry. The family-level inference is strong but is not a direct measurement of cluster binding in this particular protein."
  },
  "case_id": "GO_molecular_function_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns 2 iron, 2 sulfur cluster binding, though as a keyword-based inferred annotation rather than direct experimental evidence. The record also identifies the protein as a dihydroxy-acid dehydratase, consistent with an iron-sulfur-dependent enzyme."
  },
  "important_caveats": [
    "The direct database annotation for cluster binding is computational (IEA: UniProtKB-KW), whereas the cited experimental evidence establishes the enzyme's dehydratase activity, not direct cluster binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the iron-sulfur cluster-binding activity is the one consistent with the inferred dihydroxy-acid dehydratase family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns 2 iron, 2 sulfur cluster binding, though as a keyword-based inferred annotation rather than direct experimental evidence. The record also identifies the protein as a dihydroxy-acid dehydratase, consistent with an iron-sulfur-dependent enzyme.",
    "evidence_ids": ["H6", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the dihydroxy-acid dehydratase family, whose members use an iron-sulfur cluster and have conserved cysteine features associated with cluster coordination. That family-level knowledge makes cluster binding (C) a meaningful choice over collagen binding, D-alanine-D-alanine ligase activity, or trichodiene synthase activity.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and the sequence's cysteine-containing features provide a transferable basis for selecting C; the inference does not require recalling this exact protein's database entry. The family-level inference is strong but is not a direct measurement of cluster binding in this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the iron-sulfur cluster-binding activity is the one consistent with the inferred dihydroxy-acid dehydratase family."
  },
  "important_caveats": [
    "The direct database annotation for cluster binding is computational (IEA: UniProtKB-KW), whereas the cited experimental evidence establishes the enzyme's dehydratase activity, not direct cluster binding."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (Q0CPG9, dihydroxy-acid dehydratase astD from Aspergillus terreus) carries the GO annotation GO:0051537 '2 iron, 2 sulfur cluster binding' (evidence code IEA:UniProtKB-KW, excerpt H6). This is a valid molecular-function annotation for the protein. The protein's primary catalytic function is dihydroxy-acid dehydratase activity (GO:0004160, ECO:0000269|PubMed:29995859, excerpts C5/C8/H3/H7), which is NOT among the four options. Among the four offered choices, C is the only one that is an actual molecular-function annotation for this protein. The &#91;2Fe-2S&#93; cluster is a well-known essential cofactor of DHAD enzymes, and the annotation is consistent with the protein's biochemistry. The annotation is IEA (keyword-based, inferred from electronic annotation) rather than experimentally verified, but it is a recognized database annotation and is mechanistically consistent with the DHAD family.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H6](#evidence-h6), [H7](#evidence-h7), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~598 aa) contains multiple cysteines in patterns suggestive of metal-cluster coordination (e.g., 'PGCDKNMPG', 'PGCSAKG', 'NACPGRGACGG', 'PGSSSCPADDPKKLVECENIG', 'KCYDYED', 'YCTLVSDASHGCVTDGPI'). The DHAD (dihydroxy-acid dehydratase, EC 4.2.1.9) enzyme family is well characterized in biochemistry as containing a &#91;2Fe-2S&#93; cluster essential for catalysis; this is textbook-level family knowledge across bacteria (IlvD), plants, and fungi. Recognizing the cysteine-rich pattern and the ~600-residue length as consistent with a DHAD-family enzyme allows a knowledgeable model to infer &#91;2Fe-2S&#93; cluster binding. The other three options are eliminable by absence of their hallmark sequence features: (A) collagen binding requires specific domains (integrin-binding, discoidin, vWA, etc.) absent here; (B) D-alanine-D-alanine ligase requires an ATP-binding P-loop and specific substrate-binding architecture absent here; (D) trichodiene synthase requires the DDXXD aspartate-rich motif and terpene-cyclase fold features absent here. The combination of positive evidence (cysteine patterns + DHAD family knowledge) and elimination of the three clearly incompatible options provides a credible, transferable inference path to C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of the DHAD enzyme family and its well-established &#91;2Fe-2S&#93; cofactor, combined with visible cysteine patterns in the sequence and elimination of the three structurally incompatible alternatives, can meaningfully distinguish C from A, B, and D without recalling the specific database entry for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the question asks for the 'primary molecular function' and the protein's actual primary catalytic function (dihydroxy-acid dehydratase activity, GO:0004160) is not among the options, only option C is a valid molecular-function annotation for this protein. The other three options (collagen binding, D-alanine-D-alanine ligase, trichodiene synthase) have no sequence or functional basis for this protein. There is no genuine ambiguity among the four offered choices.


### Important caveats

- The GO:0051537 annotation is IEA (Inferred from Electronic Annotation, keyword-based), not experimentally verified for this specific protein. The experimentally verified primary function is dihydroxy-acid dehydratase catalytic activity (GO:0004160, ECO:0000269).
- The question asks for 'primary molecular function' but the actual primary catalytic function is not offered as a choice; C is the only valid annotation among the four options, though it represents a cofactor-binding sub-function rather than the catalytic activity itself.
- The protein is a fungal mitochondrial DHAD (astD) involved in aspterric acid biosynthesis and branched-chain amino acid biosynthesis; the &#91;2Fe-2S&#93; cluster annotation is consistent with the DHAD family biochemistry but is keyword-inferred rather than directly measured for this specific enzyme.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~598 aa) contains multiple cysteines in patterns suggestive of metal-cluster coordination (e.g., 'PGCDKNMPG', 'PGCSAKG', 'NACPGRGACGG', 'PGSSSCPADDPKKLVECENIG', 'KCYDYED', 'YCTLVSDASHGCVTDGPI'). The DHAD (dihydroxy-acid dehydratase, EC 4.2.1.9) enzyme family is well characterized in biochemistry as containing a [2Fe-2S] cluster essential for catalysis; this is textbook-level family knowledge across bacteria (IlvD), plants, and fungi. Recognizing the cysteine-rich pattern and the ~600-residue length as consistent with a DHAD-family enzyme allows a knowledgeable model to infer [2Fe-2S] cluster binding. The other three options are eliminable by absence of their hallmark sequence features: (A) collagen binding requires specific domains (integrin-binding, discoidin, vWA, etc.) absent here; (B) D-alanine-D-alanine ligase requires an ATP-binding P-loop and specific substrate-binding architecture absent here; (D) trichodiene synthase requires the DDXXD aspartate-rich motif and terpene-cyclase fold features absent here. The combination of positive evidence (cysteine patterns + DHAD family knowledge) and elimination of the three clearly incompatible options provides a credible, transferable inference path to C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the DHAD enzyme family and its well-established [2Fe-2S] cofactor, combined with visible cysteine patterns in the sequence and elimination of the three structurally incompatible alternatives, can meaningfully distinguish C from A, B, and D without recalling the specific database entry for this exact protein."
  },
  "case_id": "GO_molecular_function_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H6",
      "H7",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Q0CPG9, dihydroxy-acid dehydratase astD from Aspergillus terreus) carries the GO annotation GO:0051537 '2 iron, 2 sulfur cluster binding' (evidence code IEA:UniProtKB-KW, excerpt H6). This is a valid molecular-function annotation for the protein. The protein's primary catalytic function is dihydroxy-acid dehydratase activity (GO:0004160, ECO:0000269|PubMed:29995859, excerpts C5/C8/H3/H7), which is NOT among the four options. Among the four offered choices, C is the only one that is an actual molecular-function annotation for this protein. The [2Fe-2S] cluster is a well-known essential cofactor of DHAD enzymes, and the annotation is consistent with the protein's biochemistry. The annotation is IEA (keyword-based, inferred from electronic annotation) rather than experimentally verified, but it is a recognized database annotation and is mechanistically consistent with the DHAD family."
  },
  "important_caveats": [
    "The GO:0051537 annotation is IEA (Inferred from Electronic Annotation, keyword-based), not experimentally verified for this specific protein. The experimentally verified primary function is dihydroxy-acid dehydratase catalytic activity (GO:0004160, ECO:0000269).",
    "The question asks for 'primary molecular function' but the actual primary catalytic function is not offered as a choice; C is the only valid annotation among the four options, though it represents a cofactor-binding sub-function rather than the catalytic activity itself.",
    "The protein is a fungal mitochondrial DHAD (astD) involved in aspterric acid biosynthesis and branched-chain amino acid biosynthesis; the [2Fe-2S] cluster annotation is consistent with the DHAD family biochemistry but is keyword-inferred rather than directly measured for this specific enzyme."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for the 'primary molecular function' and the protein's actual primary catalytic function (dihydroxy-acid dehydratase activity, GO:0004160) is not among the options, only option C is a valid molecular-function annotation for this protein. The other three options (collagen binding, D-alanine-D-alanine ligase, trichodiene synthase) have no sequence or functional basis for this protein. There is no genuine ambiguity among the four offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Q0CPG9, dihydroxy-acid dehydratase astD from Aspergillus terreus) carries the GO annotation GO:0051537 '2 iron, 2 sulfur cluster binding' (evidence code IEA:UniProtKB-KW, excerpt H6). This is a valid molecular-function annotation for the protein. The protein's primary catalytic function is dihydroxy-acid dehydratase activity (GO:0004160, ECO:0000269|PubMed:29995859, excerpts C5/C8/H3/H7), which is NOT among the four options. Among the four offered choices, C is the only one that is an actual molecular-function annotation for this protein. The [2Fe-2S] cluster is a well-known essential cofactor of DHAD enzymes, and the annotation is consistent with the protein's biochemistry. The annotation is IEA (keyword-based, inferred from electronic annotation) rather than experimentally verified, but it is a recognized database annotation and is mechanistically consistent with the DHAD family.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H6", "H7", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~598 aa) contains multiple cysteines in patterns suggestive of metal-cluster coordination (e.g., 'PGCDKNMPG', 'PGCSAKG', 'NACPGRGACGG', 'PGSSSCPADDPKKLVECENIG', 'KCYDYED', 'YCTLVSDASHGCVTDGPI'). The DHAD (dihydroxy-acid dehydratase, EC 4.2.1.9) enzyme family is well characterized in biochemistry as containing a [2Fe-2S] cluster essential for catalysis; this is textbook-level family knowledge across bacteria (IlvD), plants, and fungi. Recognizing the cysteine-rich pattern and the ~600-residue length as consistent with a DHAD-family enzyme allows a knowledgeable model to infer [2Fe-2S] cluster binding. The other three options are eliminable by absence of their hallmark sequence features: (A) collagen binding requires specific domains (integrin-binding, discoidin, vWA, etc.) absent here; (B) D-alanine-D-alanine ligase requires an ATP-binding P-loop and specific substrate-binding architecture absent here; (D) trichodiene synthase requires the DDXXD aspartate-rich motif and terpene-cyclase fold features absent here. The combination of positive evidence (cysteine patterns + DHAD family knowledge) and elimination of the three clearly incompatible options provides a credible, transferable inference path to C.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the DHAD enzyme family and its well-established [2Fe-2S] cofactor, combined with visible cysteine patterns in the sequence and elimination of the three structurally incompatible alternatives, can meaningfully distinguish C from A, B, and D without recalling the specific database entry for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for the 'primary molecular function' and the protein's actual primary catalytic function (dihydroxy-acid dehydratase activity, GO:0004160) is not among the options, only option C is a valid molecular-function annotation for this protein. The other three options (collagen binding, D-alanine-D-alanine ligase, trichodiene synthase) have no sequence or functional basis for this protein. There is no genuine ambiguity among the four offered choices."
  },
  "important_caveats": [
    "The GO:0051537 annotation is IEA (Inferred from Electronic Annotation, keyword-based), not experimentally verified for this specific protein. The experimentally verified primary function is dihydroxy-acid dehydratase catalytic activity (GO:0004160, ECO:0000269).",
    "The question asks for 'primary molecular function' but the actual primary catalytic function is not offered as a choice; C is the only valid annotation among the four options, though it represents a cofactor-binding sub-function rather than the catalytic activity itself.",
    "The protein is a fungal mitochondrial DHAD (astD) involved in aspterric acid biosynthesis and branched-chain amino acid biosynthesis; the [2Fe-2S] cluster annotation is consistent with the DHAD family biochemistry but is keyword-inferred rather than directly measured for this specific enzyme."
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
  "benchmark_sequence_length": 598,
  "benchmark_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 598,
  "current_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0CPG9",
  "selected_historical_entry_version": 90,
  "selected_historical_record_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "selected_historical_source_sequence_length": 598,
  "selected_historical_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "selected_historical_version": {
    "accession": "Q0CPG9",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTD_ASPTN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0CPG9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase astD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxyacid dehydratase; part of the gene cluster that mediates the biosynthesis of the sesquiterpenoid aspterric acid (AA), an inhibitor of dihydroxy-acid dehydratase (DHAD) effective as an herbicide (PubMed:29995859). Performs the third step in the common pathway leading to biosynthesis of branched-chain amino acids (PubMed:29995859). Catalyzes the dehydration of (2R,3R)-2,3-dihydroxy-3-methylpentanoate (2,3-dihydroxy-3-methylvalerate) into 2-oxo-3-methylpentanoate (2-oxo-3-methylvalerate) and of (2R)-2,3-dihydroxy-3-methylbutanoate (2,3-dihydroxyisovalerate) into 2-oxo-3-methylbutanoate (2-oxoisovalerate), the penultimate precursor to L-isoleucine and L-valine, respectively (PubMed:29995859). AstD confers self-resistance in the presence of the dihydroxyacid dehydratase inhibitor aspterric acid (AA) produced by the ast cluster (PubMed:29995859)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24810\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"name\":\"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24809\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:11851\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49072\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:27695\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"name\":\"(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:27694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49258\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"id\":\"GO:0004160\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:dihydroxy-acid dehydratase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DOMAIN\",\"ACTIVITY REGULATION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H1",
  "excerpt": "ID   ASTD_ASPTN              Reviewed;         598 AA.\nAC   Q0CPG9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\nGN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, DOMAIN,\nRP   ACTIVITY REGULATION, AND PATHWAY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Dihydroxyacid dehydratase; part of the gene cluster that\nCC       mediates the biosynthesis of the sesquiterpenoid aspterric acid (AA),\nCC       an inhibitor of dihydroxy-acid dehydratase (DHAD) effective as an\nCC       herbicide (PubMed:29995859). Performs the third step in the common\nCC       pathway leading to biosynthesis of branched-chain amino acids\nCC       (PubMed:29995859). Catalyzes the dehydration of (2R,3R)-2,3-dihydroxy-\nCC       3-methylpentanoate (2,3-dihydroxy-3-methylvalerate) into 2-oxo-3-\nCC       methylpentanoate (2-oxo-3-methylvalerate) and of (2R)-2,3-dihydroxy-3-\nCC       methylbutanoate (2,3-dihydroxyisovalerate) into 2-oxo-3-methylbutanoate\nCC       (2-oxoisovalerate), the penultimate precursor to L-isoleucine and L-\nCC       valine, respectively (PubMed:29995859). AstD confers self-resistance in\nCC       the presence of the dihydroxyacid dehydratase inhibitor aspterric acid\nCC       (AA) produced by the ast cluster (PubMed:29995859).\nCC       {ECO:0000269|PubMed:29995859}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate\nCC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:49072; EC=4.2.1.9;\nCC         Evidence={ECO:0000269|PubMed:29995859};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;\nCC         Evidence={ECO:0000269|PubMed:29995859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-\nCC         oxopentanoate + H2O; Xref=Rhea:RHEA:27694, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:35146, ChEBI:CHEBI:49258; EC=4.2.1.9;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:27695;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0051537; F:2 iron, 2 sulfur cluster binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0004160; F:dihydroxy-acid dehydratase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 115-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005518\nname: collagen binding\nnamespace: molecular_function\ndef: \"Binding to collagen, a group of fibrous proteins of very high tensile strength that form the main component of connective tissue in animals. Collagen is highly enriched in glycine (some regions are 33% glycine) and proline, occurring predominantly as 3-hydroxyproline (about 20%).\" [GOC:ai, ISBN:0198506732]\nis_a: GO:0044877 ! protein-containing complex binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005518",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 56996-57002",
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
  "excerpt": "[Term]\nid: GO:0008716\nname: D-alanine-D-alanine ligase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 2 D-alanine + ATP = D-alanyl-D-alanine + ADP + 2 H+ + phosphate.\" [EC:6.3.2.4, RHEA:11224]\nsynonym: \"alanine:alanine ligase (ADP-forming) activity\" RELATED [EC:6.3.2.4]\nsynonym: \"alanylalanine synthetase activity\" RELATED [EC:6.3.2.4]\nsynonym: \"D-Ala-D-Ala synthetase activity\" RELATED [EC:6.3.2.4]\nsynonym: \"D-alanine:D-alanine ligase (ADP-forming)\" RELATED [EC:6.3.2.4]\nsynonym: \"D-alanyl-D-alanine synthetase activity\" RELATED [EC:6.3.2.4]\nsynonym: \"D-alanylalanine synthetase activity\" RELATED [EC:6.3.2.4]\nxref: EC:6.3.2.4\nxref: KEGG_REACTION:R01150\nxref: MetaCyc:DALADALALIG-RXN\nxref: RHEA:11224\nis_a: GO:0016881 ! acid-amino acid ligase activity\nproperty_value: skos:exactMatch EC:6.3.2.4\nproperty_value: skos:exactMatch RHEA:11224\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008716",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 86836-86854",
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
  "excerpt": "[Term]\nid: GO:0045482\nname: trichodiene synthase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 2-trans,6-trans-farnesyl diphosphate = diphosphate + trichodiene.\" [EC:4.2.3.6, RHEA:12052]\nsynonym: \"sesquiterpene cyclase activity\" BROAD [EC:4.2.3.6]\nsynonym: \"trans,trans-farnesyl-diphosphate diphosphate-lyase (cyclizing, trichodiene-forming)\" RELATED [EC:4.2.3.6]\nsynonym: \"trans,trans-farnesyl-diphosphate sesquiterpenoid-lyase activity\" RELATED [EC:4.2.3.6]\nsynonym: \"trichodiene synthetase activity\" RELATED [EC:4.2.3.6]\nxref: EC:4.2.3.6\nxref: KEGG_REACTION:R02306\nxref: MetaCyc:TRICHODIENE-SYNTHASE-RXN\nxref: RHEA:12052\nis_a: GO:0010334 ! sesquiterpene synthase activity\nproperty_value: skos:exactMatch EC:4.2.3.6\nproperty_value: skos:exactMatch RHEA:12052\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0045482",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 265002-265018",
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
  "excerpt": "[Term]\nid: GO:0051537\nname: 2 iron, 2 sulfur cluster binding\nnamespace: molecular_function\ndef: \"Binding to a 2 iron, 2 sulfur (2Fe-2S) cluster; this cluster consists of two iron atoms, with two inorganic sulfur atoms found between the irons and acting as bridging ligands.\" [GOC:ai, PMID:15952888, Wikipedia:Iron-sulfur_cluster]\nsynonym: \"2 Fe 2 S cluster binding\" EXACT []\nsynonym: \"2 iron, 2 sulphur cluster binding\" EXACT []\nsynonym: \"2Fe-2S cluster binding\" EXACT []\nsynonym: \"diiron disulfide cluster binding\" EXACT []\nsynonym: \"diiron disulphide cluster binding\" EXACT []\nsynonym: \"iron-sulfur cluster 2Fe-2S binding\" EXACT []\nsynonym: \"iron-sulphur cluster 2Fe-2S binding\" EXACT []\nis_a: GO:0051536 ! iron-sulfur cluster binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051537",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 327878-327891",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 59. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
