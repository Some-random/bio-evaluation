# GO_cellular_component_0049

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0049.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — mitochondrial inner membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNELSVNDAFDDIEIESFDFIWEEWEEYKGDVPLWQHIFCGSIAGLMEHVFMYPLDTLKTYFQTNGHMKYNMIYDNCNTINNNNNNIYRGNNSSYKNTCDKNYKDMNNHRNMQTFKRNFCSSTNCDKCIINNFCKYKTNCYNVMAALHTKNNRYIHNIAEPLKNMANYKINTTNNNNVNNIINNNNNNNKKKSRNIFSYPSHTKQYRNVTYVVNKKMQQNLFNNYISNKCINDPFCCRTKTNVLNMKKDIHKFCHLSKEKYNNVFYQNDTYHPNIYGRKRKTLCRNKNNINLFKNHVHKKYCHSLDDQICHSKIKEDMRNLQNFKNYTCAKNMKRHLYSTVPFFNLKNKGNKNITLPYKEIRSKYILKNGYKSMYQRNAGYYKNLIKMQSAKKNRHQLLALRKCLMSEKKYTIIKNEPFIIRKKKNMRNEYFIGNMKGRCIINTSLNSYTLKRNCLDYHHFVNNLKNICYSIMNICYNIKNTILINPSLPINNNNNNNNNTKMDTFIKLINKCLYNNNAHKIDHKILLSNYLNLFKHTNYSYYYILNNFLKNNAPCTSRKNEWNIFSNFINVLKNKIITNNVDYIRNPNVRRNQILRNNYLYSFLRNYNKNLKRNTHMILNKLTSFKYSIPYIKNKYSNVLINNINTNNNTYSNRNVLNSIRYNNIYKNIMHPIFFPGYYNTIHFRYYNYFSRIIDDKDKGKNKNIINISTKRNNCSSIIRNNLSNLYKGVNVVVLGCIPAHALYFSTFEYSKKYFSRMTSNNSSLKMNNRNISTVSNDIKSEKSNFKLYDLNYFSIAVSGFLATLVHDLIITPIDTLKQRIQLGINKNSKDSLKLLKQNGIRSLYLSLPITLLMNIPYQIIMICTNEKMKKIYFEYICGLNTQNNKKNMENKVIDKVHDETRNQDNIGKDIKNDTYNMDKNGTFLRNQEMINKENRIYNSGALEKHVTSQEKEDKILQSVKQENVSSNNDIVNFYEGQSIYNNDAHNIIRDDINKMTHKNLENNIDNTINSNESDVNRIDNMTNDMNKECDIFSINKNNNSTVLYDQIMKRLEMNSSNKNFSLNFHDKIIRQESSPFEKENYNMNLKNIWIDNYKNDFFNKPFNHITSYFVCAGIGGGIAAVLTNPLDVIKTRIQTECFQTKGFNFFRIVSNIYYREGMRSFFKGSLARMALCIPASAVSWGTYETMKRFFKINFNTT

[Multiple Choices]
A. voltage-gated calcium channel complex
B. virus tail, tube
C. mitochondrial inner membrane
D. cellular bud neck septin ring
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched record reports mitochondrial membrane localization with experimental evidence and identifies the protein as a putative mitoferrin / mitochondrial carrier protein MRS3. Mitochondrial carrier proteins are characteristically inner-membrane proteins, supporting choice C. The supplied GO annotations themselves are broader (“mitochondrial membrane”), so the inner-membrane assignment is a family-based refinement rather than an explicit annotation in these excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple hydrophobic membrane-spanning regions, particularly toward its C-terminal portion, consistent with a multipass transporter rather than a septin-ring component or viral tail protein. Mitochondrial carrier proteins are multipass inner-membrane transporters; that family-level pattern makes the mitochondrial inner membrane a credible choice over the offered alternatives. The sequence alone does not establish the exact localization with certainty.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable inference from the membrane-transporter architecture and the known localization of mitochondrial carrier families meaningfully distinguishes C among these choices; recalling this exact protein’s database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed alternatives are sufficiently distinct, and the mitochondrial-carrier interpretation favors C over the other choices.


### Important caveats

- The supplied source annotations explicitly say mitochondrial membrane, not mitochondrial inner membrane; the finer localization is supported by the carrier-family interpretation.
- The current and historical records match the supplied sequence, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic membrane-spanning regions, particularly toward its C-terminal portion, consistent with a multipass transporter rather than a septin-ring component or viral tail protein. Mitochondrial carrier proteins are multipass inner-membrane transporters; that family-level pattern makes the mitochondrial inner membrane a credible choice over the offered alternatives. The sequence alone does not establish the exact localization with certainty.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from the membrane-transporter architecture and the known localization of mitochondrial carrier families meaningfully distinguishes C among these choices; recalling this exact protein’s database record is not necessary."
  },
  "case_id": "GO_cellular_component_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record reports mitochondrial membrane localization with experimental evidence and identifies the protein as a putative mitoferrin / mitochondrial carrier protein MRS3. Mitochondrial carrier proteins are characteristically inner-membrane proteins, supporting choice C. The supplied GO annotations themselves are broader (“mitochondrial membrane”), so the inner-membrane assignment is a family-based refinement rather than an explicit annotation in these excerpts."
  },
  "important_caveats": [
    "The supplied source annotations explicitly say mitochondrial membrane, not mitochondrial inner membrane; the finer localization is supported by the carrier-family interpretation.",
    "The current and historical records match the supplied sequence, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives are sufficiently distinct, and the mitochondrial-carrier interpretation favors C over the other choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record reports mitochondrial membrane localization with experimental evidence and identifies the protein as a putative mitoferrin / mitochondrial carrier protein MRS3. Mitochondrial carrier proteins are characteristically inner-membrane proteins, supporting choice C. The supplied GO annotations themselves are broader (“mitochondrial membrane”), so the inner-membrane assignment is a family-based refinement rather than an explicit annotation in these excerpts.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic membrane-spanning regions, particularly toward its C-terminal portion, consistent with a multipass transporter rather than a septin-ring component or viral tail protein. Mitochondrial carrier proteins are multipass inner-membrane transporters; that family-level pattern makes the mitochondrial inner membrane a credible choice over the offered alternatives. The sequence alone does not establish the exact localization with certainty.",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from the membrane-transporter architecture and the known localization of mitochondrial carrier families meaningfully distinguishes C among these choices; recalling this exact protein’s database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives are sufficiently distinct, and the mitochondrial-carrier interpretation favors C over the other choices."
  },
  "important_caveats": [
    "The supplied source annotations explicitly say mitochondrial membrane, not mitochondrial inner membrane; the finer localization is supported by the carrier-family interpretation.",
    "The current and historical records match the supplied sequence, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5/H3) records 'Mitochondrion membrane' with 'Multi-pass membrane protein' topology, mapping to GO:0031966 (mitochondrial membrane). The expected answer 'mitochondrial inner membrane' (GO:0005743) is a direct child of GO:0031966. The protein is annotated as a putative mitoferrin / mitochondrial carrier protein MRS3 (C4/H1). The mitochondrial carrier family (MCF) and mitoferrins are well-established inner membrane iron/substrate transporters, making 'mitochondrial inner membrane' the most specific correct compartment. The evidence supports mitochondrial membrane localization, and family-level knowledge confirms inner membrane specifically.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence contains the hallmark mitochondrial carrier family (MCF) signature: the conserved 'GGG' motif (visible in 'FVCAGIGGGIAAVLTNPLDVIKTRIQTECFQTKGFNFFRIVSNIYYREGMRSFFKGSLARMALCIPASAVSWGTYETMKRFFKINFNTT'), S/AXXK motifs, and the characteristic pattern of transmembrane helices arranged in the tripartite carrier fold. The MCF/mitoferrin family is one of the most universally recognized protein families in biology, and all members are definitively mitochondrial inner membrane carriers. This family-level signature directly and specifically distinguishes option C. Option A (voltage-gated calcium channel complex) requires a 24-TM topology with S4 voltage-sensor segments containing repeated arginines in a specific spacing, EF-hand domains, and a large pore-forming α1 subunit architecture—none of which are present. Option B (virus tail, tube) applies to bacteriophage structural proteins with entirely different composition and fold; the extreme Asn/Lys-rich composition is typical of AT-rich eukaryotic genomes (Plasmodium), not phage genes. Option D (cellular bud neck septin ring) requires a conserved GTPase/polymerization domain characteristic of septins, absent here. Thus, recognizing the MCF carrier signature—a feature shared across hundreds of characterized homologs in yeast, plants, and animals—sufficiently identifies the inner mitochondrial membrane localization and excludes all three distractors.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The mitochondrial carrier family signature (GGG motif, S/AXXK motifs, carrier topology) is a widely conserved, textbook-recognized sequence feature present in the original input. Transferable knowledge of the MCF/mitoferrin family (all members are inner membrane carriers) directly supports choice C. The other three options require entirely different structural architectures (voltage-sensor domains, phage tail folds, septin GTPase domains) that are clearly absent from the sequence. A knowledgeable model can make this distinction from sequence features and family-level biology without needing the specific UniProt annotation for this exact entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The MCF/mitoferrin signature is unambiguous and points specifically to mitochondrial inner membrane. The three distractors require fundamentally different protein architectures (voltage-sensor domains, phage structural folds, septin GTPase domains) that are clearly absent. The only minor imprecision is that UniProt annotates 'mitochondrion membrane' (GO:0031966) rather than the more specific 'mitochondrial inner membrane' (GO:0005743), but since GO:0005743 is a child of GO:0031966 and MCF proteins are definitively inner membrane, option C is the most specific correct answer with no competing defensible choice.


### Important caveats

- The UniProt annotation uses the broader term 'Mitochondrion membrane' (GO:0031966) rather than the more specific 'mitochondrial inner membrane' (GO:0005743). The inner membrane specificity is supported by MCF/mitoferrin family knowledge rather than a direct annotation of this exact residue-level topology.
- The sequence is from Plasmodium falciparum with extremely AT-rich amino acid composition (very high Asn, Lys, Ile, Tyr content), which makes the N-terminal region atypical for standard mitochondrial targeting signal prediction tools. However, the C-terminal MCF carrier domain remains recognizable.
- The mitoferrin annotation is marked 'Putative' (ECO:0000305) and the subcellular location evidence includes both experimental (ECO:0000269, PubMed:39575308) and computational (ECO:0000255, multi-pass membrane topology) components.
- The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark input and UniProt Q8I397, validating that the annotation applies to this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence contains the hallmark mitochondrial carrier family (MCF) signature: the conserved 'GGG' motif (visible in 'FVCAGIGGGIAAVLTNPLDVIKTRIQTECFQTKGFNFFRIVSNIYYREGMRSFFKGSLARMALCIPASAVSWGTYETMKRFFKINFNTT'), S/AXXK motifs, and the characteristic pattern of transmembrane helices arranged in the tripartite carrier fold. The MCF/mitoferrin family is one of the most universally recognized protein families in biology, and all members are definitively mitochondrial inner membrane carriers. This family-level signature directly and specifically distinguishes option C. Option A (voltage-gated calcium channel complex) requires a 24-TM topology with S4 voltage-sensor segments containing repeated arginines in a specific spacing, EF-hand domains, and a large pore-forming α1 subunit architecture—none of which are present. Option B (virus tail, tube) applies to bacteriophage structural proteins with entirely different composition and fold; the extreme Asn/Lys-rich composition is typical of AT-rich eukaryotic genomes (Plasmodium), not phage genes. Option D (cellular bud neck septin ring) requires a conserved GTPase/polymerization domain characteristic of septins, absent here. Thus, recognizing the MCF carrier signature—a feature shared across hundreds of characterized homologs in yeast, plants, and animals—sufficiently identifies the inner mitochondrial membrane localization and excludes all three distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The mitochondrial carrier family signature (GGG motif, S/AXXK motifs, carrier topology) is a widely conserved, textbook-recognized sequence feature present in the original input. Transferable knowledge of the MCF/mitoferrin family (all members are inner membrane carriers) directly supports choice C. The other three options require entirely different structural architectures (voltage-sensor domains, phage tail folds, septin GTPase domains) that are clearly absent from the sequence. A knowledgeable model can make this distinction from sequence features and family-level biology without needing the specific UniProt annotation for this exact entry."
  },
  "case_id": "GO_cellular_component_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H3) records 'Mitochondrion membrane' with 'Multi-pass membrane protein' topology, mapping to GO:0031966 (mitochondrial membrane). The expected answer 'mitochondrial inner membrane' (GO:0005743) is a direct child of GO:0031966. The protein is annotated as a putative mitoferrin / mitochondrial carrier protein MRS3 (C4/H1). The mitochondrial carrier family (MCF) and mitoferrins are well-established inner membrane iron/substrate transporters, making 'mitochondrial inner membrane' the most specific correct compartment. The evidence supports mitochondrial membrane localization, and family-level knowledge confirms inner membrane specifically."
  },
  "important_caveats": [
    "The UniProt annotation uses the broader term 'Mitochondrion membrane' (GO:0031966) rather than the more specific 'mitochondrial inner membrane' (GO:0005743). The inner membrane specificity is supported by MCF/mitoferrin family knowledge rather than a direct annotation of this exact residue-level topology.",
    "The sequence is from Plasmodium falciparum with extremely AT-rich amino acid composition (very high Asn, Lys, Ile, Tyr content), which makes the N-terminal region atypical for standard mitochondrial targeting signal prediction tools. However, the C-terminal MCF carrier domain remains recognizable.",
    "The mitoferrin annotation is marked 'Putative' (ECO:0000305) and the subcellular location evidence includes both experimental (ECO:0000269, PubMed:39575308) and computational (ECO:0000255, multi-pass membrane topology) components.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark input and UniProt Q8I397, validating that the annotation applies to this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The MCF/mitoferrin signature is unambiguous and points specifically to mitochondrial inner membrane. The three distractors require fundamentally different protein architectures (voltage-sensor domains, phage structural folds, septin GTPase domains) that are clearly absent. The only minor imprecision is that UniProt annotates 'mitochondrion membrane' (GO:0031966) rather than the more specific 'mitochondrial inner membrane' (GO:0005743), but since GO:0005743 is a child of GO:0031966 and MCF proteins are definitively inner membrane, option C is the most specific correct answer with no competing defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H3) records 'Mitochondrion membrane' with 'Multi-pass membrane protein' topology, mapping to GO:0031966 (mitochondrial membrane). The expected answer 'mitochondrial inner membrane' (GO:0005743) is a direct child of GO:0031966. The protein is annotated as a putative mitoferrin / mitochondrial carrier protein MRS3 (C4/H1). The mitochondrial carrier family (MCF) and mitoferrins are well-established inner membrane iron/substrate transporters, making 'mitochondrial inner membrane' the most specific correct compartment. The evidence supports mitochondrial membrane localization, and family-level knowledge confirms inner membrane specifically.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence contains the hallmark mitochondrial carrier family (MCF) signature: the conserved 'GGG' motif (visible in 'FVCAGIGGGIAAVLTNPLDVIKTRIQTECFQTKGFNFFRIVSNIYYREGMRSFFKGSLARMALCIPASAVSWGTYETMKRFFKINFNTT'), S/AXXK motifs, and the characteristic pattern of transmembrane helices arranged in the tripartite carrier fold. The MCF/mitoferrin family is one of the most universally recognized protein families in biology, and all members are definitively mitochondrial inner membrane carriers. This family-level signature directly and specifically distinguishes option C. Option A (voltage-gated calcium channel complex) requires a 24-TM topology with S4 voltage-sensor segments containing repeated arginines in a specific spacing, EF-hand domains, and a large pore-forming α1 subunit architecture—none of which are present. Option B (virus tail, tube) applies to bacteriophage structural proteins with entirely different composition and fold; the extreme Asn/Lys-rich composition is typical of AT-rich eukaryotic genomes (Plasmodium), not phage genes. Option D (cellular bud neck septin ring) requires a conserved GTPase/polymerization domain characteristic of septins, absent here. Thus, recognizing the MCF carrier signature—a feature shared across hundreds of characterized homologs in yeast, plants, and animals—sufficiently identifies the inner mitochondrial membrane localization and excludes all three distractors.",
    "missing_item_specific_fact": "",
    "reason": "The mitochondrial carrier family signature (GGG motif, S/AXXK motifs, carrier topology) is a widely conserved, textbook-recognized sequence feature present in the original input. Transferable knowledge of the MCF/mitoferrin family (all members are inner membrane carriers) directly supports choice C. The other three options require entirely different structural architectures (voltage-sensor domains, phage tail folds, septin GTPase domains) that are clearly absent from the sequence. A knowledgeable model can make this distinction from sequence features and family-level biology without needing the specific UniProt annotation for this exact entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The MCF/mitoferrin signature is unambiguous and points specifically to mitochondrial inner membrane. The three distractors require fundamentally different protein architectures (voltage-sensor domains, phage structural folds, septin GTPase domains) that are clearly absent. The only minor imprecision is that UniProt annotates 'mitochondrion membrane' (GO:0031966) rather than the more specific 'mitochondrial inner membrane' (GO:0005743), but since GO:0005743 is a child of GO:0031966 and MCF proteins are definitively inner membrane, option C is the most specific correct answer with no competing defensible choice."
  },
  "important_caveats": [
    "The UniProt annotation uses the broader term 'Mitochondrion membrane' (GO:0031966) rather than the more specific 'mitochondrial inner membrane' (GO:0005743). The inner membrane specificity is supported by MCF/mitoferrin family knowledge rather than a direct annotation of this exact residue-level topology.",
    "The sequence is from Plasmodium falciparum with extremely AT-rich amino acid composition (very high Asn, Lys, Ile, Tyr content), which makes the N-terminal region atypical for standard mitochondrial targeting signal prediction tools. However, the C-terminal MCF carrier domain remains recognizable.",
    "The mitoferrin annotation is marked 'Putative' (ECO:0000305) and the subcellular location evidence includes both experimental (ECO:0000269, PubMed:39575308) and computational (ECO:0000255, multi-pass membrane topology) components.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark input and UniProt Q8I397, validating that the annotation applies to this exact sequence."
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
  "benchmark_sequence_length": 1199,
  "benchmark_sequence_sha256": "0aec190e1890daaba4890c14f5ccf9dc2d066473eaed63c4598f14eb646271c7",
  "current_entry_audit": {
    "entryVersion": 137,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1199,
  "current_source_sequence_sha256": "0aec190e1890daaba4890c14f5ccf9dc2d066473eaed63c4598f14eb646271c7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 135,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8I397",
  "selected_historical_entry_version": 135,
  "selected_historical_record_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "selected_historical_source_sequence_length": 1199,
  "selected_historical_source_sequence_sha256": "0aec190e1890daaba4890c14f5ccf9dc2d066473eaed63c4598f14eb646271c7",
  "selected_historical_version": {
    "accession": "Q8I397",
    "database": "Swiss-Prot",
    "entryVersion": 135,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFRN_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8I397\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":137,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"Mitochondrial carrier protein MRS3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"PfMRS3\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Putative mitoferrin\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"PfMFRN\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"id\":\"SL-0171\",\"value\":\"Mitochondrion membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031966\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrial membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/16",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Wunderlich J.\",\"Kotov V.\",\"Votborg-Novel L.\",\"Ntalla C.\",\"Geffken M.\",\"Peine S.\",\"Portugal S.\",\"Strauss J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39575308\"},{\"database\":\"DOI\",\"id\":\"10.3389/fcimb.2024.1480076\"}],\"citationType\":\"journal article\",\"firstPage\":\"1480076\",\"id\":\"39575308\",\"journal\":\"Front. Cell. Infect. Microbiol.\",\"lastPage\":\"1480076\",\"publicationDate\":\"2024\",\"title\":\"Iron transport pathways in the human malaria parasite Plasmodium falciparum revealed by RNA-sequencing.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:03.528080+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I397.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H1",
  "excerpt": "ID   MFRN_PLAF7              Reviewed;        1199 AA.\nAC   Q8I397;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 135.\nDE   RecName: Full=Putative mitoferrin {ECO:0000305};\nDE            Short=PfMFRN {ECO:0000303|PubMed:39575308};\nDE   AltName: Full=Mitochondrial carrier protein MRS3 {ECO:0000303|PubMed:39575308};\nDE            Short=PfMRS3 {ECO:0000303|PubMed:39575308};\nGN   ORFNames=PF3D7_0905200 {ECO:0000312|EMBL:CAD51737.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, INDUCTION, AND\nRP   DISRUPTION PHENOTYPE.\nRX   PubMed=39575308; DOI=10.3389/fcimb.2024.1480076;\nRA   Wunderlich J., Kotov V., Votborg-Novel L., Ntalla C., Geffken M., Peine S.,\nRA   Portugal S., Strauss J.;\nRT   \"Iron transport pathways in the human malaria parasite Plasmodium\nRT   falciparum revealed by RNA-sequencing.\";\nRL   Front. Cell. Infect. Microbiol. 14:1480076-1480076(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Mitochondrion membrane\nCC       {ECO:0000269|PubMed:39575308}; Multi-pass membrane protein\nCC       {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)

```json
{
  "entry_version": 135,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0031966; C:mitochondrial membrane; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:05.771018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455",
  "url": "https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000144\nname: cellular bud neck septin ring\nnamespace: cellular_component\ndef: \"A ring-shaped structure that forms at the site of cytokinesis in the bud neck of a budding cell; composed of members of the conserved family of filament forming proteins called septins as well as septin-associated proteins. In S. cerevisiae, this structure forms at the time of bud emergence and the septins show a high rate of exchange.\" [GOC:krc, PMID:16009555]\nis_a: GO:0000399 ! cellular bud neck septin structure\nis_a: GO:0005940 ! septin ring\nis_a: GO:0032161 ! cleavage apparatus septin structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000144",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1412-1420",
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
  "excerpt": "[Term]\nid: GO:0005743\nname: mitochondrial inner membrane\nnamespace: cellular_component\ndef: \"The inner, i.e. lumen-facing, lipid bilayer of the mitochondrial envelope. It is highly folded to form cristae.\" [GOC:ai]\nsynonym: \"inner mitochondrial membrane\" EXACT []\nsynonym: \"inner mitochondrion membrane\" EXACT []\nsynonym: \"mitochondrion inner membrane\" EXACT []\nxref: NIF_Subcellular:sao1371347282\nxref: Wikipedia:Inner_mitochondrial_membrane\nis_a: GO:0019866 ! organelle inner membrane\nis_a: GO:0031966 ! mitochondrial membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005743",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59031-59043",
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
  "excerpt": "[Term]\nid: GO:0005891\nname: voltage-gated calcium channel complex\nnamespace: cellular_component\ndef: \"A protein complex that forms a transmembrane channel through which calcium ions may pass in response to changes in membrane potential.\" [GOC:mah]\nsubset: goslim_pir\nsynonym: \"voltage gated calcium channel complex\" EXACT []\nsynonym: \"voltage-dependent calcium channel complex\" EXACT []\nsynonym: \"voltage-sensitive calcium channel complex\" EXACT []\nis_a: GO:0034704 ! calcium channel complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005891",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60486-60497",
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
  "excerpt": "[Term]\nid: GO:0098026\nname: virus tail, tube\nnamespace: cellular_component\ndef: \"The internal tube of the tail of some viruses. The virus tail tube is the channel for DNA ejection into the host cytoplasm.\" [PMID:33188213, VZ:3960]\ncomment: Applies in particular the Myoviridae bacteriophages. Many bacteriophages with dsDNA genomes, or Caudovirales, have a tail. The viral tail can be short (Podoviridae), long and non-contractile (Siphoviridae) or long and contractile (Myoviridae). The tail is the channel through which the phage genome is injected into the host bacterial cell.\nsynonym: \"bacteriophage tail tube\" NARROW [GOC:bm]\nxref: VZ:3960 \"Viral tail tube protein\"\nis_a: GO:0044423 ! virion component\nrelationship: part_of GO:0098015 ! virus tail\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0098026",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 408367-408377",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
