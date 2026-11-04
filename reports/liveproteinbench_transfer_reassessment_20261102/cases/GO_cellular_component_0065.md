# GO_cellular_component_0065

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0065.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **A** — fungal-type cell wall

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVGKSTLLSVLASASVAFAACSLDSHCPEETPCCSQYGECGTGAYCLGGCDPRMSFSLESCVPEPVCESASYTFTSMDGITSNTKYLGDASKSNWVYSGSPVIYNDNVLLTMSANSVGTVMASSTYMWYGNVKAKFKTSRGQGVITAFILFSDVKDEIDYEFVGSELTTAQSNYYFQGITNYDNELNITLSDTYANYHEYEIDWTPDEITWLVDGQVGRTKKRADTWNATANQWNFPQTPARVQLSLWPGGLASNGAGTIAWAGGEIDWNSEDIQNNGYYYAAFESVDISCYNAKSAPGTNSGKSYYYNSVLGTNNTVIDSKNATILSSLLATGTNMTAGESAAASGSTAASTAATVPGLTGSGGGGVGDNHSDDGSSSSDSSSGSATSSSSGSSSTGSSGFSQGDGSTSTSKSSADSLVANQERVLKGSLFAGIVAVVAMMAL

[Multiple Choices]
A. fungal-type cell wall
B. monoatomic ion channel complex
C. primosome complex
D. virus tail, tube
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

> The sequence-matched record annotates fungal-type cell wall (GO:0009277), including a historical TreeGrafter annotation and a current UniProtKB-ARBA annotation. These are computational annotations, not direct experimental localization evidence, but they support choice A.

Citations as saved: [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, and the C-terminal hydrophobic region is consistent with a GPI-anchor signal. Together with the extracellular enzyme-like sequence, this suggests a secreted, cell-surface fungal protein; transferable knowledge of fungal cell-wall remodeling proteins makes the fungal-type cell wall a meaningful choice over an ion-channel complex, primosome, or viral tail tube.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence features and protein-family-level biological pattern provide a credible distinction among the offered choices without needing the exact target's recorded annotation. They support a cell-wall association, though they do not establish localization experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence also supports membrane association, but plasma membrane is not an offered option; none of the other listed choices is comparably supported.


### Important caveats

- The supplied cell-wall annotations are computational; the evidence provided does not establish experimental localization.
- A membrane-associated localization is also annotated for this protein, so the wording “primary” is not fully resolved by the excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the C-terminal hydrophobic region is consistent with a GPI-anchor signal. Together with the extracellular enzyme-like sequence, this suggests a secreted, cell-surface fungal protein; transferable knowledge of fungal cell-wall remodeling proteins makes the fungal-type cell wall a meaningful choice over an ion-channel complex, primosome, or viral tail tube.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and protein-family-level biological pattern provide a credible distinction among the offered choices without needing the exact target's recorded annotation. They support a cell-wall association, though they do not establish localization experimentally."
  },
  "case_id": "GO_cellular_component_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates fungal-type cell wall (GO:0009277), including a historical TreeGrafter annotation and a current UniProtKB-ARBA annotation. These are computational annotations, not direct experimental localization evidence, but they support choice A."
  },
  "important_caveats": [
    "The supplied cell-wall annotations are computational; the evidence provided does not establish experimental localization.",
    "A membrane-associated localization is also annotated for this protein, so the wording “primary” is not fully resolved by the excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence also supports membrane association, but plasma membrane is not an offered option; none of the other listed choices is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates fungal-type cell wall (GO:0009277), including a historical TreeGrafter annotation and a current UniProtKB-ARBA annotation. These are computational annotations, not direct experimental localization evidence, but they support choice A.",
    "evidence_ids": ["H4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the C-terminal hydrophobic region is consistent with a GPI-anchor signal. Together with the extracellular enzyme-like sequence, this suggests a secreted, cell-surface fungal protein; transferable knowledge of fungal cell-wall remodeling proteins makes the fungal-type cell wall a meaningful choice over an ion-channel complex, primosome, or viral tail tube.",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and protein-family-level biological pattern provide a credible distinction among the offered choices without needing the exact target's recorded annotation. They support a cell-wall association, though they do not establish localization experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence also supports membrane association, but plasma membrane is not an offered option; none of the other listed choices is comparably supported."
  },
  "important_caveats": [
    "The supplied cell-wall annotations are computational; the evidence provided does not establish experimental localization.",
    "A membrane-associated localization is also annotated for this protein, so the wording “primary” is not fully resolved by the excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (A0A384K116, Crh-like protein 3 from Botrytis cinerea) carries GO:0009277 (fungal-type cell wall) as a cellular component annotation (evidence IEA:UniProtKB-ARBA). The protein is described as a GPI-anchored cell membrane protein with chitinase/chitin transglycosylase activity. The GO definition of fungal-type cell wall explicitly includes GPI-anchored glycoproteins as cell wall components. The annotation is computational (IEA), but the biological rationale (GPI-anchored chitinase involved in cell wall remodeling) is well-supported by the protein's known function and the 2021 experimental paper (PubMed:33846308) confirming Crh3 as a cell wall-associated transglycosylase. The answer is consistent with the database record.

Citations as saved: [C6](#evidence-c6), [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4), [H3](#evidence-h3), [H2](#evidence-h2), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains three strong transferable features that distinguish A from B, C, and D: (1) An N-terminal signal peptide (MVGKSTLLSVLASASVAFAACSLDSH) indicates a secreted or membrane-anchored protein, immediately ruling out C (primosome complex, a nuclear replication complex). (2) A C-terminal hydrophobic region (SLVANQERVLKGSLFAGIVAVVAMMAL) with a small polar residue at the omega site is a classic GPI-anchor signal sequence, indicating a cell-surface/cell-wall-anchored protein rather than a multi-pass ion channel (ruling out B) or a viral structural protein (ruling out D). (3) Multiple cysteine-rich motifs in the N-terminal region (CPEETPCCSQYGECGTGAYCLGGCDPRMSFSLESCVPEPVCES) are characteristic of chitin-binding domains, and the central region contains a GH18 chitinase catalytic domain. Fungal GPI-anchored chitinases and transglycosylases are textbook examples of cell wall-associated proteins involved in cell wall remodeling. This combination of signal peptide + chitin-binding domain + chitinase catalytic domain + GPI-anchor signal is a well-recognized pattern across fungal cell wall proteins (e.g., Crh1, CWP1, CWP2 in yeast), making A the only biologically coherent choice among the four options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the signal peptide, GPI-anchor signal, chitin-binding cysteine motifs, and GH18 catalytic domain to infer this is a secreted, GPI-anchored cell wall-remodeling enzyme. This family-level pattern (fungal GPI-anchored chitinases/transglycosylases as cell wall proteins) is well-established transferable knowledge. The distractors are clearly incompatible: ion channels require multiple transmembrane helices (absent), primosomes are nuclear complexes (inconsistent with a secreted protein), and virus tail tubes are bacteriophage structural proteins (inconsistent with a eukaryotic fungal sequence with a signal peptide).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only A (fungal-type cell wall) is consistent with the sequence features. B, C, and D are clearly incompatible with a secreted GPI-anchored chitinase. Although the UniProt entry also annotates plasma membrane (GO:0005886), that term is not among the choices, so no ambiguity exists among the provided options.


### Important caveats

- The GO:0009277 annotation is IEA (Inferred from Electronic Annotation) via ARBA, not direct experimental evidence. However, the biological rationale is well-supported by the protein's known enzymatic function and the 2021 experimental study.
- The protein's primary UniProt subcellular location comment is 'Cell membrane; GPI-anchor,' but among the offered GO cellular component choices, 'fungal-type cell wall' is the best match since the GO definition explicitly includes GPI-anchored glycoproteins as cell wall components.
- The source is a fungal organism (Botrytis cinerea), which is relevant context for the 'fungal-type' qualifier in the GO term, but this is inferable from the chitinase/chitin-binding domain biology and GPI-anchor pattern without knowing the exact organism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains three strong transferable features that distinguish A from B, C, and D: (1) An N-terminal signal peptide (MVGKSTLLSVLASASVAFAACSLDSH) indicates a secreted or membrane-anchored protein, immediately ruling out C (primosome complex, a nuclear replication complex). (2) A C-terminal hydrophobic region (SLVANQERVLKGSLFAGIVAVVAMMAL) with a small polar residue at the omega site is a classic GPI-anchor signal sequence, indicating a cell-surface/cell-wall-anchored protein rather than a multi-pass ion channel (ruling out B) or a viral structural protein (ruling out D). (3) Multiple cysteine-rich motifs in the N-terminal region (CPEETPCCSQYGECGTGAYCLGGCDPRMSFSLESCVPEPVCES) are characteristic of chitin-binding domains, and the central region contains a GH18 chitinase catalytic domain. Fungal GPI-anchored chitinases and transglycosylases are textbook examples of cell wall-associated proteins involved in cell wall remodeling. This combination of signal peptide + chitin-binding domain + chitinase catalytic domain + GPI-anchor signal is a well-recognized pattern across fungal cell wall proteins (e.g., Crh1, CWP1, CWP2 in yeast), making A the only biologically coherent choice among the four options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the signal peptide, GPI-anchor signal, chitin-binding cysteine motifs, and GH18 catalytic domain to infer this is a secreted, GPI-anchored cell wall-remodeling enzyme. This family-level pattern (fungal GPI-anchored chitinases/transglycosylases as cell wall proteins) is well-established transferable knowledge. The distractors are clearly incompatible: ion channels require multiple transmembrane helices (absent), primosomes are nuclear complexes (inconsistent with a secreted protein), and virus tail tubes are bacteriophage structural proteins (inconsistent with a eukaryotic fungal sequence with a signal peptide)."
  },
  "case_id": "GO_cellular_component_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C5",
      "C4",
      "H4",
      "H3",
      "H2",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A384K116, Crh-like protein 3 from Botrytis cinerea) carries GO:0009277 (fungal-type cell wall) as a cellular component annotation (evidence IEA:UniProtKB-ARBA). The protein is described as a GPI-anchored cell membrane protein with chitinase/chitin transglycosylase activity. The GO definition of fungal-type cell wall explicitly includes GPI-anchored glycoproteins as cell wall components. The annotation is computational (IEA), but the biological rationale (GPI-anchored chitinase involved in cell wall remodeling) is well-supported by the protein's known function and the 2021 experimental paper (PubMed:33846308) confirming Crh3 as a cell wall-associated transglycosylase. The answer is consistent with the database record."
  },
  "important_caveats": [
    "The GO:0009277 annotation is IEA (Inferred from Electronic Annotation) via ARBA, not direct experimental evidence. However, the biological rationale is well-supported by the protein's known enzymatic function and the 2021 experimental study.",
    "The protein's primary UniProt subcellular location comment is 'Cell membrane; GPI-anchor,' but among the offered GO cellular component choices, 'fungal-type cell wall' is the best match since the GO definition explicitly includes GPI-anchored glycoproteins as cell wall components.",
    "The source is a fungal organism (Botrytis cinerea), which is relevant context for the 'fungal-type' qualifier in the GO term, but this is inferable from the chitinase/chitin-binding domain biology and GPI-anchor pattern without knowing the exact organism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only A (fungal-type cell wall) is consistent with the sequence features. B, C, and D are clearly incompatible with a secreted GPI-anchored chitinase. Although the UniProt entry also annotates plasma membrane (GO:0005886), that term is not among the choices, so no ambiguity exists among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A384K116, Crh-like protein 3 from Botrytis cinerea) carries GO:0009277 (fungal-type cell wall) as a cellular component annotation (evidence IEA:UniProtKB-ARBA). The protein is described as a GPI-anchored cell membrane protein with chitinase/chitin transglycosylase activity. The GO definition of fungal-type cell wall explicitly includes GPI-anchored glycoproteins as cell wall components. The annotation is computational (IEA), but the biological rationale (GPI-anchored chitinase involved in cell wall remodeling) is well-supported by the protein's known function and the 2021 experimental paper (PubMed:33846308) confirming Crh3 as a cell wall-associated transglycosylase. The answer is consistent with the database record.",
    "evidence_ids": ["C6", "C5", "C4", "H4", "H3", "H2", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains three strong transferable features that distinguish A from B, C, and D: (1) An N-terminal signal peptide (MVGKSTLLSVLASASVAFAACSLDSH) indicates a secreted or membrane-anchored protein, immediately ruling out C (primosome complex, a nuclear replication complex). (2) A C-terminal hydrophobic region (SLVANQERVLKGSLFAGIVAVVAMMAL) with a small polar residue at the omega site is a classic GPI-anchor signal sequence, indicating a cell-surface/cell-wall-anchored protein rather than a multi-pass ion channel (ruling out B) or a viral structural protein (ruling out D). (3) Multiple cysteine-rich motifs in the N-terminal region (CPEETPCCSQYGECGTGAYCLGGCDPRMSFSLESCVPEPVCES) are characteristic of chitin-binding domains, and the central region contains a GH18 chitinase catalytic domain. Fungal GPI-anchored chitinases and transglycosylases are textbook examples of cell wall-associated proteins involved in cell wall remodeling. This combination of signal peptide + chitin-binding domain + chitinase catalytic domain + GPI-anchor signal is a well-recognized pattern across fungal cell wall proteins (e.g., Crh1, CWP1, CWP2 in yeast), making A the only biologically coherent choice among the four options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the signal peptide, GPI-anchor signal, chitin-binding cysteine motifs, and GH18 catalytic domain to infer this is a secreted, GPI-anchored cell wall-remodeling enzyme. This family-level pattern (fungal GPI-anchored chitinases/transglycosylases as cell wall proteins) is well-established transferable knowledge. The distractors are clearly incompatible: ion channels require multiple transmembrane helices (absent), primosomes are nuclear complexes (inconsistent with a secreted protein), and virus tail tubes are bacteriophage structural proteins (inconsistent with a eukaryotic fungal sequence with a signal peptide)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only A (fungal-type cell wall) is consistent with the sequence features. B, C, and D are clearly incompatible with a secreted GPI-anchored chitinase. Although the UniProt entry also annotates plasma membrane (GO:0005886), that term is not among the choices, so no ambiguity exists among the provided options."
  },
  "important_caveats": [
    "The GO:0009277 annotation is IEA (Inferred from Electronic Annotation) via ARBA, not direct experimental evidence. However, the biological rationale is well-supported by the protein's known enzymatic function and the 2021 experimental study.",
    "The protein's primary UniProt subcellular location comment is 'Cell membrane; GPI-anchor,' but among the offered GO cellular component choices, 'fungal-type cell wall' is the best match since the GO definition explicitly includes GPI-anchored glycoproteins as cell wall components.",
    "The source is a fungal organism (Botrytis cinerea), which is relevant context for the 'fungal-type' qualifier in the GO term, but this is inferable from the chitinase/chitin-binding domain biology and GPI-anchor pattern without knowing the exact organism."
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
  "benchmark_sequence_length": 444,
  "benchmark_sequence_sha256": "fb0633b17deb89eb19591d65a84515ea5ac98abe057826a49312d226bb2dc5e4",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 444,
  "current_source_sequence_sha256": "fb0633b17deb89eb19591d65a84515ea5ac98abe057826a49312d226bb2dc5e4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384K116",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "selected_historical_source_sequence_length": 444,
  "selected_historical_source_sequence_sha256": "fb0633b17deb89eb19591d65a84515ea5ac98abe057826a49312d226bb2dc5e4",
  "selected_historical_version": {
    "accession": "A0A384K116",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH3_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384K116\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitinase crh3\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitin transglycosylase crh3\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9902\",\"value\":\"Lipid-anchor, GPI-anchor\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009277\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:fungal-type cell wall\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-ARBA\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Bi K.\",\"Scalschi L.\",\"Jaiswal N.\",\"Mengiste T.\",\"Fried R.\",\"Sanz A.B.\",\"Arroyo J.\",\"Zhu W.\",\"Masrati G.\",\"Sharon A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33846308\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-021-22436-1\"}],\"citationType\":\"journal article\",\"firstPage\":\"2166\",\"id\":\"33846308\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2166\",\"publicationDate\":\"2021\",\"title\":\"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.\",\"volume\":\"12\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"INTERACTION WITH CRH1 AND CRH2\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   CRH3_BOTFB              Reviewed;         444 AA.\nAC   A0A384K116;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Crh-like protein 3 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh3 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh3 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\nGN   Name=crh3 {ECO:0000303|PubMed:33846308}; ORFNames=BCIN_13g03640;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.844205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "url": "https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, SUBUNIT, AND INTERACTION WITH CRH1 AND CRH2.\nRX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;\nRA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,\nRA   Arroyo J., Zhu W., Masrati G., Sharon A.;\nRT   \"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector\nRT   triggering plant cell death and defense response.\";\nRL   Nat. Commun. 12:2166-2166(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.844205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "url": "https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000255}; Lipid-anchor, GPI-\nCC       anchor {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.844205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "url": "https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0009277; C:fungal-type cell wall; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.844205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "url": "https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.844205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "url": "https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0098552; C:side of membrane; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.844205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "url": "https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0009277\nname: fungal-type cell wall\nnamespace: cellular_component\ndef: \"A rigid yet dynamic structure surrounding the plasma membrane that affords protection from stresses and contributes to cell morphogenesis, consisting of extensively cross-linked glycoproteins and carbohydrates. The glycoproteins may be modified with N- or O-linked carbohydrates, or glycosylphosphatidylinositol (GPI) anchors; the polysaccharides are primarily branched glucans, including beta-linked and alpha-linked glucans, and may also include chitin and other carbohydrate polymers, but not cellulose or pectin. Enzymes involved in cell wall biosynthesis are also found in the cell wall. Note that some forms of fungi develop a capsule outside of the cell wall under certain circumstances; this is considered a separate structure.\" [GOC:mcc, GOC:mtg_sensu, ISBN:3540601864, PMID:11283274, PMID:16927300, PMID:3319422, PMID:36266346]\nsynonym: \"beta-glucan-containing cell wall\" RELATED []\nsynonym: \"chitin- and beta-glucan-containing cell wall\" NARROW []\nsynonym: \"chitin-containing cell wall\" RELATED []\nis_a: GO:0005618 ! cell wall\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009277",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 94765-94774",
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
  "excerpt": "[Term]\nid: GO:0034702\nname: monoatomic ion channel complex\nnamespace: cellular_component\ndef: \"A protein complex that spans a membrane and forms a water-filled channel across the phospholipid bilayer allowing selective monoatomic ion transport down its electrochemical gradient.\" [GOC:mah, ISBN:071673706X]\nis_a: GO:1902495 ! transmembrane transporter complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0034702",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 211424-211430",
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

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:1990077\nname: primosome complex\nnamespace: cellular_component\ndef: \"Any of a family of protein complexes that form at the origin of replication or stalled replication forks and function in replication primer synthesis in all organisms. Early complexes initiate double-stranded DNA unwinding. The core unit consists of a replicative helicase and a primase. The helicase further unwinds the DNA and recruits the polymerase machinery. The primase synthesizes RNA primers that act as templates for complementary stand replication by the polymerase machinery. The primosome contains a number of associated proteins and protein complexes and contributes to the processes of replication initiation, lagging strand elongation, and replication restart.\" [GOC:bhm, GOC:mah, PMID:21856207]\nsynonym: \"primosome\" EXACT []\nis_a: GO:0032993 ! protein-DNA complex\nrelationship: part_of GO:0030894 ! replisome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990077",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 549032-549040",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 65. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
