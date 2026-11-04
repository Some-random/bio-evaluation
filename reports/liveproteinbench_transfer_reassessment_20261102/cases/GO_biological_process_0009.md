# GO_biological_process_0009

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0009.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — L-valine biosynthetic process

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
A. plasma membrane organization
B. L-valine biosynthetic process
C. dUDP biosynthetic process
D. indole alkaloid biosynthetic process
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

> The matched-sequence UniProt record reports that this enzyme catalyzes a step producing the penultimate precursor to valine and assigns it to the L-valine biosynthetic pathway. The functional annotation cites experimental evidence, while the GO annotation itself is IEA (computationally assigned).

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a long, mitochondrial-targeted dihydroxy-acid dehydratase: its conserved enzyme-family sequence features support recognition of a branched-chain amino-acid biosynthesis enzyme. DHAD catalyzes a shared pathway step that produces a valine precursor, making B meaningfully distinguishable from membrane organization, dUDP synthesis, and indole alkaloid synthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the known DHAD reaction provide a transferable basis for choosing B; recalling this exact protein’s database entry is not necessary. The sequence alone may not establish the exact organism or all of this enzyme’s roles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The enzyme also participates in isoleucine biosynthesis, but that is not an offered choice. Among the listed alternatives, valine biosynthesis is the defensible match.


### Important caveats

- The reviewer-only record matches the supplied sequence; its organism and annotations were not original inputs.
- The source reports experimental support for the functional annotation, but the GO term assignment is IEA rather than a direct experimental GO annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a long, mitochondrial-targeted dihydroxy-acid dehydratase: its conserved enzyme-family sequence features support recognition of a branched-chain amino-acid biosynthesis enzyme. DHAD catalyzes a shared pathway step that produces a valine precursor, making B meaningfully distinguishable from membrane organization, dUDP synthesis, and indole alkaloid synthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known DHAD reaction provide a transferable basis for choosing B; recalling this exact protein’s database entry is not necessary. The sequence alone may not establish the exact organism or all of this enzyme’s roles."
  },
  "case_id": "GO_biological_process_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record reports that this enzyme catalyzes a step producing the penultimate precursor to valine and assigns it to the L-valine biosynthetic pathway. The functional annotation cites experimental evidence, while the GO annotation itself is IEA (computationally assigned)."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence; its organism and annotations were not original inputs.",
    "The source reports experimental support for the functional annotation, but the GO term assignment is IEA rather than a direct experimental GO annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme also participates in isoleucine biosynthesis, but that is not an offered choice. Among the listed alternatives, valine biosynthesis is the defensible match."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record reports that this enzyme catalyzes a step producing the penultimate precursor to valine and assigns it to the L-valine biosynthetic pathway. The functional annotation cites experimental evidence, while the GO annotation itself is IEA (computationally assigned).",
    "evidence_ids": ["C5", "C7", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a long, mitochondrial-targeted dihydroxy-acid dehydratase: its conserved enzyme-family sequence features support recognition of a branched-chain amino-acid biosynthesis enzyme. DHAD catalyzes a shared pathway step that produces a valine precursor, making B meaningfully distinguishable from membrane organization, dUDP synthesis, and indole alkaloid synthesis.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known DHAD reaction provide a transferable basis for choosing B; recalling this exact protein’s database entry is not necessary. The sequence alone may not establish the exact organism or all of this enzyme’s roles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme also participates in isoleucine biosynthesis, but that is not an offered choice. Among the listed alternatives, valine biosynthesis is the defensible match."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence; its organism and annotations were not original inputs.",
    "The source reports experimental support for the functional annotation, but the GO term assignment is IEA rather than a direct experimental GO annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q0CPG9 (ASTD_ASPTN) is annotated as Dihydroxy-acid dehydratase astD (EC 4.2.1.9), which catalyzes the dehydration of 2,3-dihydroxyisovalerate to 2-oxoisovalerate, the penultimate step in L-valine biosynthesis. The pathway comment explicitly states 'L-valine biosynthesis; L-valine from pyruvate: step 3/4' (C7, H5), and GO:0009099 (L-valine biosynthetic process) is directly annotated (C8, H7). The protein also participates in isoleucine biosynthesis, but that term is not among the offered choices. The answer B is well-supported by experimental evidence (ECO:0000269, PubMed:29995859).

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple diagnostic features of the dihydroxy-acid dehydratase (DHAD/ILV3) family: (1) an N-terminal mitochondrial targeting presequence rich in Arg/Ser/Thr (fungal mitochondrial import signal); (2) two &#91;4Fe-4S&#93; cluster-binding motifs with the pattern CxxC...CPGRGACGG...SSSC (e.g., 'CPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKK'), which are hallmark iron-sulfur cluster ligands of DHAD; (3) a conserved catalytic domain with motifs like 'GAGLGQDVALLTDGRFSGGSHGFLIGH' and 'GKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEG' matching the DHAD active-site architecture. DHAD (ILV3) is a well-characterized enzyme across fungi, bacteria, and plants that catalyzes the third step of branched-chain amino acid biosynthesis, directly producing the penultimate precursor to L-valine (2-oxoisovalerate) and L-isoleucine. Among the four options, only B (L-valine biosynthetic process) is consistent with a DHAD enzyme. Option A (plasma membrane organization) is excluded by the absence of transmembrane segments and the presence of a soluble enzyme architecture with Fe-S clusters. Option C (dUDP biosynthetic process) is excluded by the absence of any nucleotide-metabolism motifs (no kinase, no ribonucleotide reductase, no pyrimidine pathway features). Option D (indole alkaloid biosynthetic process) is excluded by the absence of P450, terpene synthase, or tryptophan-derived alkaloid pathway motifs. The DHAD family is extensively characterized in many organisms, making this a transferable family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the DHAD/ILV3 family from conserved &#91;4Fe-4S&#93; cluster motifs, mitochondrial targeting sequence, and catalytic domain architecture. DHAD's role in branched-chain amino acid biosynthesis (specifically valine and isoleucine) is a well-established, transferable fact learned from characterization of ILV3 homologs in yeast, E. coli, plants, and other fungi. This directly selects option B over the three clearly unrelated alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein participates in both L-valine and L-isoleucine biosynthesis, only L-valine biosynthetic process is offered among the four choices. The other three options (plasma membrane organization, dUDP biosynthesis, indole alkaloid biosynthesis) are clearly incompatible with a DHAD enzyme. No ambiguity exists among the offered alternatives.


### Important caveats

- The protein is part of the aspterric acid biosynthesis gene cluster in Aspergillus terreus and also functions as a resistance protein against the DHAD inhibitor aspterric acid. However, its enzymatic/biological process role is BCAA biosynthesis, and aspterric acid biosynthesis is not offered as an option.
- The GO annotation for L-valine biosynthetic process carries evidence code IEA:UniProtKB-UniPathway (automatic assignment from pathway), while the experimental evidence (ECO:0000269) supports the enzymatic function and pathway membership.
- The protein equally participates in isoleucine biosynthesis (GO:0009097), but this term is not among the offered choices, so it does not create ambiguity.
- The mitochondrial targeting sequence and Fe-S cluster motifs are strongly indicative of DHAD but do not uniquely identify this specific fungal astD paralog versus other DHAD family members; however, the biological process (BCAA biosynthesis) is the same for all DHAD enzymes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple diagnostic features of the dihydroxy-acid dehydratase (DHAD/ILV3) family: (1) an N-terminal mitochondrial targeting presequence rich in Arg/Ser/Thr (fungal mitochondrial import signal); (2) two [4Fe-4S] cluster-binding motifs with the pattern CxxC...CPGRGACGG...SSSC (e.g., 'CPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKK'), which are hallmark iron-sulfur cluster ligands of DHAD; (3) a conserved catalytic domain with motifs like 'GAGLGQDVALLTDGRFSGGSHGFLIGH' and 'GKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEG' matching the DHAD active-site architecture. DHAD (ILV3) is a well-characterized enzyme across fungi, bacteria, and plants that catalyzes the third step of branched-chain amino acid biosynthesis, directly producing the penultimate precursor to L-valine (2-oxoisovalerate) and L-isoleucine. Among the four options, only B (L-valine biosynthetic process) is consistent with a DHAD enzyme. Option A (plasma membrane organization) is excluded by the absence of transmembrane segments and the presence of a soluble enzyme architecture with Fe-S clusters. Option C (dUDP biosynthetic process) is excluded by the absence of any nucleotide-metabolism motifs (no kinase, no ribonucleotide reductase, no pyrimidine pathway features). Option D (indole alkaloid biosynthetic process) is excluded by the absence of P450, terpene synthase, or tryptophan-derived alkaloid pathway motifs. The DHAD family is extensively characterized in many organisms, making this a transferable family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the DHAD/ILV3 family from conserved [4Fe-4S] cluster motifs, mitochondrial targeting sequence, and catalytic domain architecture. DHAD's role in branched-chain amino acid biosynthesis (specifically valine and isoleucine) is a well-established, transferable fact learned from characterization of ILV3 homologs in yeast, E. coli, plants, and other fungi. This directly selects option B over the three clearly unrelated alternatives."
  },
  "case_id": "GO_biological_process_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "H3",
      "H5",
      "H7",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG9 (ASTD_ASPTN) is annotated as Dihydroxy-acid dehydratase astD (EC 4.2.1.9), which catalyzes the dehydration of 2,3-dihydroxyisovalerate to 2-oxoisovalerate, the penultimate step in L-valine biosynthesis. The pathway comment explicitly states 'L-valine biosynthesis; L-valine from pyruvate: step 3/4' (C7, H5), and GO:0009099 (L-valine biosynthetic process) is directly annotated (C8, H7). The protein also participates in isoleucine biosynthesis, but that term is not among the offered choices. The answer B is well-supported by experimental evidence (ECO:0000269, PubMed:29995859)."
  },
  "important_caveats": [
    "The protein is part of the aspterric acid biosynthesis gene cluster in Aspergillus terreus and also functions as a resistance protein against the DHAD inhibitor aspterric acid. However, its enzymatic/biological process role is BCAA biosynthesis, and aspterric acid biosynthesis is not offered as an option.",
    "The GO annotation for L-valine biosynthetic process carries evidence code IEA:UniProtKB-UniPathway (automatic assignment from pathway), while the experimental evidence (ECO:0000269) supports the enzymatic function and pathway membership.",
    "The protein equally participates in isoleucine biosynthesis (GO:0009097), but this term is not among the offered choices, so it does not create ambiguity.",
    "The mitochondrial targeting sequence and Fe-S cluster motifs are strongly indicative of DHAD but do not uniquely identify this specific fungal astD paralog versus other DHAD family members; however, the biological process (BCAA biosynthesis) is the same for all DHAD enzymes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein participates in both L-valine and L-isoleucine biosynthesis, only L-valine biosynthetic process is offered among the four choices. The other three options (plasma membrane organization, dUDP biosynthesis, indole alkaloid biosynthesis) are clearly incompatible with a DHAD enzyme. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG9 (ASTD_ASPTN) is annotated as Dihydroxy-acid dehydratase astD (EC 4.2.1.9), which catalyzes the dehydration of 2,3-dihydroxyisovalerate to 2-oxoisovalerate, the penultimate step in L-valine biosynthesis. The pathway comment explicitly states 'L-valine biosynthesis; L-valine from pyruvate: step 3/4' (C7, H5), and GO:0009099 (L-valine biosynthetic process) is directly annotated (C8, H7). The protein also participates in isoleucine biosynthesis, but that term is not among the offered choices. The answer B is well-supported by experimental evidence (ECO:0000269, PubMed:29995859).",
    "evidence_ids": ["C5", "C7", "C8", "H3", "H5", "H7", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple diagnostic features of the dihydroxy-acid dehydratase (DHAD/ILV3) family: (1) an N-terminal mitochondrial targeting presequence rich in Arg/Ser/Thr (fungal mitochondrial import signal); (2) two [4Fe-4S] cluster-binding motifs with the pattern CxxC...CPGRGACGG...SSSC (e.g., 'CPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKK'), which are hallmark iron-sulfur cluster ligands of DHAD; (3) a conserved catalytic domain with motifs like 'GAGLGQDVALLTDGRFSGGSHGFLIGH' and 'GKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEG' matching the DHAD active-site architecture. DHAD (ILV3) is a well-characterized enzyme across fungi, bacteria, and plants that catalyzes the third step of branched-chain amino acid biosynthesis, directly producing the penultimate precursor to L-valine (2-oxoisovalerate) and L-isoleucine. Among the four options, only B (L-valine biosynthetic process) is consistent with a DHAD enzyme. Option A (plasma membrane organization) is excluded by the absence of transmembrane segments and the presence of a soluble enzyme architecture with Fe-S clusters. Option C (dUDP biosynthetic process) is excluded by the absence of any nucleotide-metabolism motifs (no kinase, no ribonucleotide reductase, no pyrimidine pathway features). Option D (indole alkaloid biosynthetic process) is excluded by the absence of P450, terpene synthase, or tryptophan-derived alkaloid pathway motifs. The DHAD family is extensively characterized in many organisms, making this a transferable family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the DHAD/ILV3 family from conserved [4Fe-4S] cluster motifs, mitochondrial targeting sequence, and catalytic domain architecture. DHAD's role in branched-chain amino acid biosynthesis (specifically valine and isoleucine) is a well-established, transferable fact learned from characterization of ILV3 homologs in yeast, E. coli, plants, and other fungi. This directly selects option B over the three clearly unrelated alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein participates in both L-valine and L-isoleucine biosynthesis, only L-valine biosynthetic process is offered among the four choices. The other three options (plasma membrane organization, dUDP biosynthesis, indole alkaloid biosynthesis) are clearly incompatible with a DHAD enzyme. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The protein is part of the aspterric acid biosynthesis gene cluster in Aspergillus terreus and also functions as a resistance protein against the DHAD inhibitor aspterric acid. However, its enzymatic/biological process role is BCAA biosynthesis, and aspterric acid biosynthesis is not offered as an option.",
    "The GO annotation for L-valine biosynthetic process carries evidence code IEA:UniProtKB-UniPathway (automatic assignment from pathway), while the experimental evidence (ECO:0000269) supports the enzymatic function and pathway membership.",
    "The protein equally participates in isoleucine biosynthesis (GO:0009097), but this term is not among the offered choices, so it does not create ambiguity.",
    "The mitochondrial targeting sequence and Fe-S cluster motifs are strongly indicative of DHAD but do not uniquely identify this specific fungal astD paralog versus other DHAD family members; however, the biological process (BCAA biosynthesis) is the same for all DHAD enzymes."
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/7",
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
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009099\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:L-valine biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniPathway\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
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
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-isoleucine biosynthesis; L-\nCC       isoleucine from 2-oxobutanoate: step 3/4.\nCC       {ECO:0000269|PubMed:29995859}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-79",
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
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-valine biosynthesis; L-valine from\nCC       pyruvate: step 3/4. {ECO:0000269|PubMed:29995859}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-81",
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
  "excerpt": "DR   GO; GO:0009097; P:isoleucine biosynthetic process; IEA:UniProtKB-UniPathway.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-117",
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
  "excerpt": "DR   GO; GO:0009099; P:L-valine biosynthetic process; IEA:UniProtKB-UniPathway.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-118",
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
  "excerpt": "[Term]\nid: GO:0006227\nname: dUDP biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of dUDP, deoxyuridine diphosphate (2'-deoxy-5'-uridylyl phosphate).\" [ISBN:0198506732]\nsynonym: \"dUDP anabolism\" EXACT []\nsynonym: \"dUDP biosynthesis\" EXACT []\nsynonym: \"dUDP formation\" EXACT []\nsynonym: \"dUDP synthesis\" EXACT []\nis_a: GO:0009189 ! deoxyribonucleoside diphosphate biosynthetic process\nis_a: GO:0009197 ! pyrimidine deoxyribonucleoside diphosphate biosynthetic process\nis_a: GO:0009221 ! pyrimidine deoxyribonucleotide biosynthetic process\nis_a: GO:0046077 ! dUDP metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006227",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 64156-64169",
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
  "excerpt": "[Term]\nid: GO:0007009\nname: plasma membrane organization\nnamespace: biological_process\ndef: \"A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of the plasma membrane.\" [GOC:dph, GOC:jl, GOC:mah]\nsubset: goslim_chembl\nsynonym: \"plasma membrane organisation\" EXACT []\nsynonym: \"plasma membrane organization and biogenesis\" RELATED [GOC:mah]\nis_a: GO:0061024 ! membrane organization\nrelationship: part_of GO:0010256 ! endomembrane system organization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007009",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 72411-72421",
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
  "excerpt": "[Term]\nid: GO:0009099\nname: L-valine biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of valine, 2-amino-3-methylbutanoic acid.\" [GOC:ai, MetaCyc:VALSYN-PWY]\nsynonym: \"valine anabolism\" EXACT []\nsynonym: \"valine biosynthesis\" EXACT []\nsynonym: \"valine formation\" EXACT []\nsynonym: \"valine synthesis\" EXACT []\nxref: MetaCyc:VALSYN-PWY\nis_a: GO:0009079 ! pyruvate family amino acid biosynthetic process\nis_a: GO:0009082 ! branched-chain amino acid biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009099",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 92766-92778",
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
  "excerpt": "[Term]\nid: GO:0035835\nname: indole alkaloid biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of an indole alkaloid, an alkaloid containing an indole skeleton.\" [GOC:yaf]\nsynonym: \"indole alkaloid anabolism\" EXACT [GOC:bf]\nsynonym: \"indole alkaloid biosynthesis\" EXACT [GOC:bf]\nsynonym: \"indole alkaloid formation\" EXACT [GOC:bf]\nsynonym: \"indole alkaloid synthesis\" EXACT [GOC:bf]\nis_a: GO:0009821 ! alkaloid biosynthetic process\nis_a: GO:0035834 ! indole alkaloid metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0035835",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 221717-221728",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
