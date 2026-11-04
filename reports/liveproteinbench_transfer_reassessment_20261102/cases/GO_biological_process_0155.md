# GO_biological_process_0155

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0155.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — symbiont-mediated perturbation of host defenses

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKTILAVIFFGILAFAFADYPSIPKCTHPPAMANFNQKKFLEGKWYVTKAKHGSNSTVCREYRAKTKGNDQILVGDGYYSFNGGTFYFTVRCKRLPNKEVQKPLQFTCTQKSPDDPSKMFKFQLEVTILDTDYANYAVMYRCVQFPEELGSHFEDNTLLLHRKLDQLVDENLIERKLKLSLPSFKSRDDVVEGCRELPSKKKKTKP

[Multiple Choices]
A. sterol biosynthetic process
B. symbiont-mediated perturbation of host defenses
C. vascular endothelial growth factor signaling pathway
D. response to strigolactone
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

> The matched sequence has a GO annotation for symbiont-mediated perturbation of host defenses (IEA:InterPro), and experimental functional evidence reports suppression of the host kallikrein-kinin system and inhibition of intrinsic coagulation. These findings support choice B, while distinguishing the computational GO annotation from the experimental functional evidence.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus is strongly hydrophobic, consistent with a signal peptide, and the remainder is a small cysteine-containing protein, supporting a secreted-protein inference. Among the choices, a secreted protein acting on a host is more consistent with perturbing host defenses (B) than with sterol biosynthesis, VEGF signaling, or a response to a plant hormone. This is a transferable, probabilistic inference from sequence features and general protein biology, not proof of the exact activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal-peptide-like sequence and small secreted-protein character provide a meaningful basis for distinguishing B from the offered alternatives. The precise host target and biological activity are not independently established by sequence alone, but that degree of certainty is not required to make the comparative choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence features and broad biological context.


### Important caveats

- The original input does not identify the organism or provide experimental evidence; the sequence-based inference is probabilistic.
- The exact GO term is supported by a computational annotation, whereas the supplied functional evidence experimentally describes host coagulation-system inhibition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus is strongly hydrophobic, consistent with a signal peptide, and the remainder is a small cysteine-containing protein, supporting a secreted-protein inference. Among the choices, a secreted protein acting on a host is more consistent with perturbing host defenses (B) than with sterol biosynthesis, VEGF signaling, or a response to a plant hormone. This is a transferable, probabilistic inference from sequence features and general protein biology, not proof of the exact activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal-peptide-like sequence and small secreted-protein character provide a meaningful basis for distinguishing B from the offered alternatives. The precise host target and biological activity are not independently established by sequence alone, but that degree of certainty is not required to make the comparative choice."
  },
  "case_id": "GO_biological_process_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a GO annotation for symbiont-mediated perturbation of host defenses (IEA:InterPro), and experimental functional evidence reports suppression of the host kallikrein-kinin system and inhibition of intrinsic coagulation. These findings support choice B, while distinguishing the computational GO annotation from the experimental functional evidence."
  },
  "important_caveats": [
    "The original input does not identify the organism or provide experimental evidence; the sequence-based inference is probabilistic.",
    "The exact GO term is supported by a computational annotation, whereas the supplied functional evidence experimentally describes host coagulation-system inhibition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence features and broad biological context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a GO annotation for symbiont-mediated perturbation of host defenses (IEA:InterPro), and experimental functional evidence reports suppression of the host kallikrein-kinin system and inhibition of intrinsic coagulation. These findings support choice B, while distinguishing the computational GO annotation from the experimental functional evidence.",
    "evidence_ids": ["C5", "C7", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus is strongly hydrophobic, consistent with a signal peptide, and the remainder is a small cysteine-containing protein, supporting a secreted-protein inference. Among the choices, a secreted protein acting on a host is more consistent with perturbing host defenses (B) than with sterol biosynthesis, VEGF signaling, or a response to a plant hormone. This is a transferable, probabilistic inference from sequence features and general protein biology, not proof of the exact activity.",
    "missing_item_specific_fact": "",
    "reason": "The signal-peptide-like sequence and small secreted-protein character provide a meaningful basis for distinguishing B from the offered alternatives. The precise host target and biological activity are not independently established by sequence alone, but that degree of certainty is not required to make the comparative choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence features and broad biological context."
  },
  "important_caveats": [
    "The original input does not identify the organism or provide experimental evidence; the sequence-based inference is probabilistic.",
    "The exact GO term is supported by a computational annotation, whereas the supplied functional evidence experimentally describes host coagulation-system inhibition."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A7BJ45, Triafestin-1 from Triatoma infestans) carries GO:0030682 (symbiont-mediated perturbation of host defenses) as an IEA:InterPro annotation. The experimental evidence (PubMed:17645545) confirms the protein suppresses the host plasma kallikrein-kinin system, blocks coagulation factor XII and prekallikrein activation, and attenuates bradykinin generation—all clear perturbations of host defense. The GO term definition ('a process in which a symbiont alters or subverts the normal execution of a host organism's defense response') matches the experimentally observed function. Although the specific GO annotation is computational (IEA:InterPro), the underlying biology is experimentally verified (IDA:UniProtKB for the related GO:0140184). The answer B is a valid, supported description of the protein's biological process.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence shows: (1) a clear N-terminal hydrophobic signal peptide (MKTILAVIFFGILAFAFADY), indicating a secreted protein; (2) a small mature protein (~186 aa) with multiple cysteines forming disulfide bonds; (3) a compact domain with the Cys spacing and fold pattern characteristic of a Kunitz-type serine protease inhibitor. From general biology learned across many blood-feeding arthropods (ticks, mosquitoes, kissing bugs), small secreted Kunitz-type or similar protease-inhibitor domains from salivary glands overwhelmingly function to interfere with host coagulation, complement, and kallikrein-kinin cascades—i.e., perturbation of host defenses. This pattern directly supports option B. The other three options are eliminable from sequence features and domain knowledge: A (sterol biosynthetic process) requires large membrane-bound enzymes (e.g., squalene synthase ~412 aa, HMG-CoA reductase ~888 aa) with transmembrane segments, incompatible with a small secreted disulfide-bonded inhibitor; C (VEGF signaling pathway) requires receptor tyrosine kinase domains (~1000+ aa) or VEGF-specific ligand motifs absent here; D (response to strigolactone) is a plant-specific hormonal response pathway, irrelevant to an insect protein. Thus, family-level recognition of Kunitz-type inhibitors from blood-feeders plus elimination of the three clearly mismatched options provides a credible, concrete inference path to B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the signal peptide, small size, disulfide-rich Kunitz-like inhibitory fold, and secreted nature from the sequence alone. The well-documented pattern across dozens of blood-feeding arthropod salivary proteins (tick anticoagulant peptide, ixolaris, various Kunitz inhibitors from mosquitoes and bugs) that such small secreted inhibitors target host defense cascades provides strong transferable support for B. The three distractors are excluded by fundamental protein-class and kingdom mismatches visible from the sequence and general biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are each excluded by clear biological incompatibilities (wrong protein class, wrong pathway type, wrong kingdom respectively). Among the four offered choices, only B is consistent with a small secreted protease-inhibitor domain from an arthropod. No ambiguity among the offered alternatives.


### Important caveats

- The GO:0030682 annotation for this protein is IEA:InterPro (computational), not directly experimental. However, the underlying function (suppression of host kallikrein-kinin and coagulation systems) is experimentally confirmed via IDA annotations on related GO terms.
- The term 'symbiont' in GO:0030682 is used broadly in ontology practice to include parasites and blood-feeding organisms, though a strict biological definition of symbiosis might not encompass a transient blood-feeding interaction.
- The more specific experimentally-annotated GO term GO:0140184 (venom-mediated suppression of blood coagulation, intrinsic pathway) is not among the choices but is a narrower description of the same function.
- The reviewer-only evidence identifies the protein as Triafestin-1 from Triatoma infestans, but this organism/protein name was not provided to the evaluated model; the reasoning above relies only on sequence features and transferable knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence shows: (1) a clear N-terminal hydrophobic signal peptide (MKTILAVIFFGILAFAFADY), indicating a secreted protein; (2) a small mature protein (~186 aa) with multiple cysteines forming disulfide bonds; (3) a compact domain with the Cys spacing and fold pattern characteristic of a Kunitz-type serine protease inhibitor. From general biology learned across many blood-feeding arthropods (ticks, mosquitoes, kissing bugs), small secreted Kunitz-type or similar protease-inhibitor domains from salivary glands overwhelmingly function to interfere with host coagulation, complement, and kallikrein-kinin cascades—i.e., perturbation of host defenses. This pattern directly supports option B. The other three options are eliminable from sequence features and domain knowledge: A (sterol biosynthetic process) requires large membrane-bound enzymes (e.g., squalene synthase ~412 aa, HMG-CoA reductase ~888 aa) with transmembrane segments, incompatible with a small secreted disulfide-bonded inhibitor; C (VEGF signaling pathway) requires receptor tyrosine kinase domains (~1000+ aa) or VEGF-specific ligand motifs absent here; D (response to strigolactone) is a plant-specific hormonal response pathway, irrelevant to an insect protein. Thus, family-level recognition of Kunitz-type inhibitors from blood-feeders plus elimination of the three clearly mismatched options provides a credible, concrete inference path to B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the signal peptide, small size, disulfide-rich Kunitz-like inhibitory fold, and secreted nature from the sequence alone. The well-documented pattern across dozens of blood-feeding arthropod salivary proteins (tick anticoagulant peptide, ixolaris, various Kunitz inhibitors from mosquitoes and bugs) that such small secreted inhibitors target host defense cascades provides strong transferable support for B. The three distractors are excluded by fundamental protein-class and kingdom mismatches visible from the sequence and general biology."
  },
  "case_id": "GO_biological_process_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "H3",
      "H5",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A7BJ45, Triafestin-1 from Triatoma infestans) carries GO:0030682 (symbiont-mediated perturbation of host defenses) as an IEA:InterPro annotation. The experimental evidence (PubMed:17645545) confirms the protein suppresses the host plasma kallikrein-kinin system, blocks coagulation factor XII and prekallikrein activation, and attenuates bradykinin generation—all clear perturbations of host defense. The GO term definition ('a process in which a symbiont alters or subverts the normal execution of a host organism's defense response') matches the experimentally observed function. Although the specific GO annotation is computational (IEA:InterPro), the underlying biology is experimentally verified (IDA:UniProtKB for the related GO:0140184). The answer B is a valid, supported description of the protein's biological process."
  },
  "important_caveats": [
    "The GO:0030682 annotation for this protein is IEA:InterPro (computational), not directly experimental. However, the underlying function (suppression of host kallikrein-kinin and coagulation systems) is experimentally confirmed via IDA annotations on related GO terms.",
    "The term 'symbiont' in GO:0030682 is used broadly in ontology practice to include parasites and blood-feeding organisms, though a strict biological definition of symbiosis might not encompass a transient blood-feeding interaction.",
    "The more specific experimentally-annotated GO term GO:0140184 (venom-mediated suppression of blood coagulation, intrinsic pathway) is not among the choices but is a narrower description of the same function.",
    "The reviewer-only evidence identifies the protein as Triafestin-1 from Triatoma infestans, but this organism/protein name was not provided to the evaluated model; the reasoning above relies only on sequence features and transferable knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are each excluded by clear biological incompatibilities (wrong protein class, wrong pathway type, wrong kingdom respectively). Among the four offered choices, only B is consistent with a small secreted protease-inhibitor domain from an arthropod. No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A7BJ45, Triafestin-1 from Triatoma infestans) carries GO:0030682 (symbiont-mediated perturbation of host defenses) as an IEA:InterPro annotation. The experimental evidence (PubMed:17645545) confirms the protein suppresses the host plasma kallikrein-kinin system, blocks coagulation factor XII and prekallikrein activation, and attenuates bradykinin generation—all clear perturbations of host defense. The GO term definition ('a process in which a symbiont alters or subverts the normal execution of a host organism's defense response') matches the experimentally observed function. Although the specific GO annotation is computational (IEA:InterPro), the underlying biology is experimentally verified (IDA:UniProtKB for the related GO:0140184). The answer B is a valid, supported description of the protein's biological process.",
    "evidence_ids": ["C5", "C7", "C8", "H3", "H5", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence shows: (1) a clear N-terminal hydrophobic signal peptide (MKTILAVIFFGILAFAFADY), indicating a secreted protein; (2) a small mature protein (~186 aa) with multiple cysteines forming disulfide bonds; (3) a compact domain with the Cys spacing and fold pattern characteristic of a Kunitz-type serine protease inhibitor. From general biology learned across many blood-feeding arthropods (ticks, mosquitoes, kissing bugs), small secreted Kunitz-type or similar protease-inhibitor domains from salivary glands overwhelmingly function to interfere with host coagulation, complement, and kallikrein-kinin cascades—i.e., perturbation of host defenses. This pattern directly supports option B. The other three options are eliminable from sequence features and domain knowledge: A (sterol biosynthetic process) requires large membrane-bound enzymes (e.g., squalene synthase ~412 aa, HMG-CoA reductase ~888 aa) with transmembrane segments, incompatible with a small secreted disulfide-bonded inhibitor; C (VEGF signaling pathway) requires receptor tyrosine kinase domains (~1000+ aa) or VEGF-specific ligand motifs absent here; D (response to strigolactone) is a plant-specific hormonal response pathway, irrelevant to an insect protein. Thus, family-level recognition of Kunitz-type inhibitors from blood-feeders plus elimination of the three clearly mismatched options provides a credible, concrete inference path to B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the signal peptide, small size, disulfide-rich Kunitz-like inhibitory fold, and secreted nature from the sequence alone. The well-documented pattern across dozens of blood-feeding arthropod salivary proteins (tick anticoagulant peptide, ixolaris, various Kunitz inhibitors from mosquitoes and bugs) that such small secreted inhibitors target host defense cascades provides strong transferable support for B. The three distractors are excluded by fundamental protein-class and kingdom mismatches visible from the sequence and general biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are each excluded by clear biological incompatibilities (wrong protein class, wrong pathway type, wrong kingdom respectively). Among the four offered choices, only B is consistent with a small secreted protease-inhibitor domain from an arthropod. No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The GO:0030682 annotation for this protein is IEA:InterPro (computational), not directly experimental. However, the underlying function (suppression of host kallikrein-kinin and coagulation systems) is experimentally confirmed via IDA annotations on related GO terms.",
    "The term 'symbiont' in GO:0030682 is used broadly in ontology practice to include parasites and blood-feeding organisms, though a strict biological definition of symbiosis might not encompass a transient blood-feeding interaction.",
    "The more specific experimentally-annotated GO term GO:0140184 (venom-mediated suppression of blood coagulation, intrinsic pathway) is not among the choices but is a narrower description of the same function.",
    "The reviewer-only evidence identifies the protein as Triafestin-1 from Triatoma infestans, but this organism/protein name was not provided to the evaluated model; the reasoning above relies only on sequence features and transferable knowledge."
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
  "benchmark_sequence_length": 206,
  "benchmark_sequence_sha256": "d4e7707c323262208b48fc591ac398ecb437296b7ae5143354262910f5bfb2c8",
  "current_entry_audit": {
    "entryVersion": 32,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-09-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "18e5c8c634bfe4365c698be8b2fced90a0a7869d827b602398ee4b567cd7a661",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 206,
  "current_source_sequence_sha256": "d4e7707c323262208b48fc591ac398ecb437296b7ae5143354262910f5bfb2c8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A7BJ45",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "04f27e4d5411161dabb6346ae2c2052a56a94ea2d7a4db1bcbc6b4ec4dc185bf",
  "selected_historical_source_sequence_length": 206,
  "selected_historical_source_sequence_sha256": "d4e7707c323262208b48fc591ac398ecb437296b7ae5143354262910f5bfb2c8",
  "selected_historical_version": {
    "accession": "A7BJ45",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "TRIA1_TRIIF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ45.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A7BJ45\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:59.925039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e5c8c634bfe4365c698be8b2fced90a0a7869d827b602398ee4b567cd7a661",
  "url": "https://rest.uniprot.org/uniprotkb/A7BJ45.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ45.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":32,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-09-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:59.925039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e5c8c634bfe4365c698be8b2fced90a0a7869d827b602398ee4b567cd7a661",
  "url": "https://rest.uniprot.org/uniprotkb/A7BJ45.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ45.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Assassin bug\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAF75464.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Paraneoptera\",\"Hemiptera\",\"Heteroptera\",\"Panheteroptera\",\"Cimicomorpha\",\"Reduviidae\",\"Triatominae\",\"Triatoma\"],\"scientificName\":\"Triatoma infestans\",\"taxonId\":30076}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:59.925039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e5c8c634bfe4365c698be8b2fced90a0a7869d827b602398ee4b567cd7a661",
  "url": "https://rest.uniprot.org/uniprotkb/A7BJ45.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ45.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17645545\",\"source\":\"PubMed\"}],\"value\":\"Triafestin-1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:59.925039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e5c8c634bfe4365c698be8b2fced90a0a7869d827b602398ee4b567cd7a661",
  "url": "https://rest.uniprot.org/uniprotkb/A7BJ45.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ45.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17645545\",\"source\":\"PubMed\"}],\"value\":\"Suppresses activation of the host plasma kallikrein-kinin system, leading to inhibition of the intrinsic coagulation pathway (PubMed:17645545). Blocks host coagulation factor XII (F12) and prekallikrein (KLKB1) reciprocal activation without affecting their amidolytic activities (PubMed:17645545). Blocks binding of host F12 and high molecular weight kininogen (KNG1) to negatively charged surfaces (PubMed:17645545). Attenuates generation of bradykinin by interfering with activation of host kallikrein-kinin system (PubMed:17645545)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:59.925039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e5c8c634bfe4365c698be8b2fced90a0a7869d827b602398ee4b567cd7a661",
  "url": "https://rest.uniprot.org/uniprotkb/A7BJ45.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ45.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"17645545\",\"source\":\"PubMed\"}],\"id\":\"GO:0140106\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:hematophagy\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-01T06:24:59.925039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e5c8c634bfe4365c698be8b2fced90a0a7869d827b602398ee4b567cd7a661",
  "url": "https://rest.uniprot.org/uniprotkb/A7BJ45.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ45.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030682\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:symbiont-mediated perturbation of host defenses\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-01T06:24:59.925039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e5c8c634bfe4365c698be8b2fced90a0a7869d827b602398ee4b567cd7a661",
  "url": "https://rest.uniprot.org/uniprotkb/A7BJ45.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ45.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"17645545\",\"source\":\"PubMed\"}],\"id\":\"GO:0140184\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:venom-mediated suppression of blood coagulation, intrinsic pathway\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-01T06:24:59.925039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e5c8c634bfe4365c698be8b2fced90a0a7869d827b602398ee4b567cd7a661",
  "url": "https://rest.uniprot.org/uniprotkb/A7BJ45.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ45.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Isawa H.\",\"Orito Y.\",\"Jingushi N.\",\"Iwanaga S.\",\"Morita A.\",\"Chinzei Y.\",\"Yuda M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17645545\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1742-4658.2007.05958.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"4271\",\"id\":\"17645545\",\"journal\":\"FEBS J.\",\"lastPage\":\"4286\",\"publicationDate\":\"2007\",\"title\":\"Identification and characterization of plasma kallikrein-kinin system inhibitors from salivary glands of the blood-sucking insect Triatoma infestans.\",\"volume\":\"274\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAF75464.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"ACTIVITY REGULATION\",\"INTERACTION WITH HOST F12 AND KNG1\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:59.925039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e5c8c634bfe4365c698be8b2fced90a0a7869d827b602398ee4b567cd7a661",
  "url": "https://rest.uniprot.org/uniprotkb/A7BJ45.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   TRIA1_TRIIF             Reviewed;         206 AA.\nAC   A7BJ45;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-SEP-2007, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Triafestin-1 {ECO:0000303|PubMed:17645545};\nDE   Flags: Precursor;\nOS   Triatoma infestans (Assassin bug).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Paraneoptera; Hemiptera; Heteroptera; Panheteroptera;\nOC   Cimicomorpha; Reduviidae; Triatominae; Triatoma.\nOX   NCBI_TaxID=30076 {ECO:0000312|EMBL:BAF75464.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.778085+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04f27e4d5411161dabb6346ae2c2052a56a94ea2d7a4db1bcbc6b4ec4dc185bf",
  "url": "https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAF75464.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, ACTIVITY REGULATION, INTERACTION WITH\nRP   HOST F12 AND KNG1, AND TISSUE SPECIFICITY.\nRX   PubMed=17645545; DOI=10.1111/j.1742-4658.2007.05958.x;\nRA   Isawa H., Orito Y., Jingushi N., Iwanaga S., Morita A., Chinzei Y.,\nRA   Yuda M.;\nRT   \"Identification and characterization of plasma kallikrein-kinin system\nRT   inhibitors from salivary glands of the blood-sucking insect Triatoma\nRT   infestans.\";\nRL   FEBS J. 274:4271-4286(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.778085+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 13-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04f27e4d5411161dabb6346ae2c2052a56a94ea2d7a4db1bcbc6b4ec4dc185bf",
  "url": "https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Suppresses activation of the host plasma kallikrein-kinin\nCC       system, leading to inhibition of the intrinsic coagulation pathway\nCC       (PubMed:17645545). Blocks host coagulation factor XII (F12) and\nCC       prekallikrein (KLKB1) reciprocal activation without affecting their\nCC       amidolytic activities (PubMed:17645545). Blocks binding of host F12 and\nCC       high molecular weight kininogen (KNG1) to negatively charged surfaces\nCC       (PubMed:17645545). Attenuates generation of bradykinin by interfering\nCC       with activation of host kallikrein-kinin system (PubMed:17645545).\nCC       {ECO:0000269|PubMed:17645545}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.778085+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04f27e4d5411161dabb6346ae2c2052a56a94ea2d7a4db1bcbc6b4ec4dc185bf",
  "url": "https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0140106; P:hematophagy; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.778085+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04f27e4d5411161dabb6346ae2c2052a56a94ea2d7a4db1bcbc6b4ec4dc185bf",
  "url": "https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0030682; P:symbiont-mediated perturbation of host defenses; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.778085+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04f27e4d5411161dabb6346ae2c2052a56a94ea2d7a4db1bcbc6b4ec4dc185bf",
  "url": "https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0140184; P:venom-mediated suppression of blood coagulation, intrinsic pathway; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.778085+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04f27e4d5411161dabb6346ae2c2052a56a94ea2d7a4db1bcbc6b4ec4dc185bf",
  "url": "https://rest.uniprot.org/unisave/A7BJ45?format=txt&versions=31"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0016126\nname: sterol biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of sterols, steroids with one or more hydroxyl groups and a hydrocarbon side-chain in the molecule.\" [GOC:curators]\nsynonym: \"sterol anabolism\" EXACT []\nsynonym: \"sterol biosynthesis\" EXACT []\nsynonym: \"sterol formation\" EXACT []\nsynonym: \"sterol synthesis\" EXACT []\nxref: MetaCyc:PWY-2541\nis_a: GO:0006694 ! steroid biosynthetic process\nis_a: GO:0016125 ! sterol metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016126",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 123737-123749",
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
  "excerpt": "[Term]\nid: GO:0030682\nname: symbiont-mediated perturbation of host defenses\nnamespace: biological_process\nalt_id: GO:0044413\nalt_id: GO:0044415\nalt_id: GO:0051807\nalt_id: GO:0051832\nalt_id: GO:0051834\ndef: \"A process in which a symbiont alters or subverts the normal execution of a host organism's defense response. The host defense response is mounted by the host in response to the presence of the symbiont. The host is defined as the larger of the organisms involved in a symbiotic interaction.\" [GOC:mtg_pamgo_17jul06]\nsynonym: \"avoidance of defenses of other organism during symbiotic interaction\" RELATED [GOC:dph]\nsynonym: \"avoidance of defenses of other organism involved in symbiotic interaction\" NARROW []\nsynonym: \"avoidance of host defences\" NARROW []\nsynonym: \"avoidance of host defenses\" NARROW []\nsynonym: \"evasion of host defence response\" NARROW []\nsynonym: \"evasion of other organism defence response\" NARROW []\nsynonym: \"evasion or tolerance of defense response of other organism during symbiotic interaction\" RELATED [GOC:dph]\nsynonym: \"evasion or tolerance of defense response of other organism involved in symbiotic interaction\" BROAD []\nsynonym: \"evasion or tolerance of defenses of other organism\" RELATED []\nsynonym: \"evasion or tolerance of defenses of other organism during symbiotic interaction\" RELATED [GOC:dph]\nsynonym: \"evasion or tolerance of defenses of other organism involved in symbiotic interaction\" RELATED []\nsynonym: \"evasion or tolerance of host defense response\" NARROW []\nsynonym: \"evasion or tolerance of host defenses\" RELATED []\nsynonym: \"mitigation of host defenses by symbiont\" EXACT []\nsynonym: \"perturbation of host defenses by symbiont\" EXACT []\nis_a: GO:0052200 ! symbiont-mediated response to host defenses\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030682",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 168439-168465",
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
  "excerpt": "[Term]\nid: GO:0038084\nname: vascular endothelial growth factor signaling pathway\nnamespace: biological_process\ndef: \"The series of molecular signals initiated by vascular endothelial growth factor (VEGF) binding its receptor on the surface of the target cell, and ending with the regulation of a downstream cellular process, e.g. transcription.\" [GOC:signaling, PMID:17470632]\ncomment: In GO, a gene product with 'vascular endothelial growth factor-activated receptor activity ; GO:0005021' necessarily binds VEGF to transduce a signal. To represent cross-talk between ligands and receptors, signaling pathways in GO are starting to be named after the receptor and/or the signal. GO:0038084 is for annotation of any pathway in which the ligand VEGF binds and activates any cell surface receptor (VEGFR, PDGFR etc.). For annotation of signaling pathways where a VEGFR binds one of its physiological ligands (VEGF or an alternative growth factor), consider 'vascular endothelial growth factor receptor signaling pathway ; GO:0048010'.\nsynonym: \"vascular endothelial growth factor signalling pathway\" EXACT [GOC:bf]\nsynonym: \"VEGF signaling\" EXACT [GOC:bf]\nsynonym: \"VEGF-activated signaling pathway\" EXACT [GOC:bf]\nis_a: GO:0007169 ! cell surface receptor protein tyrosine kinase signaling pathway\nrelationship: part_of GO:0035924 ! cellular response to vascular endothelial growth factor stimulus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0038084",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 229528-229539",
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
  "excerpt": "[Term]\nid: GO:1902347\nname: response to strigolactone\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a strigolactone stimulus.\" [GOC:TermGenie, PMID:23893171]\nsynonym: \"response to strigolactone analog GR24\" RELATED [PMID:23893171]\nis_a: GO:0033993 ! response to lipid\nis_a: GO:1901700 ! response to oxygen-containing compound\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1902347",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 489432-489440",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 155. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
