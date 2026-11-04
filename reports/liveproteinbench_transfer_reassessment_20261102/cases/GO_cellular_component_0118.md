# GO_cellular_component_0118

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0118.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — side of membrane

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
A. host cell plasma membrane
B. endocytic vesicle
C. side of membrane
D. host cell nucleolus
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

> The sequence-matched UniProt record annotates the protein as cell membrane-associated with a GPI anchor and assigns GO:0098552, “side of membrane.” These annotations support C, though the GO assignments are computational and do not establish experimental localization.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secretion signal, while the C-terminal hydrophobic segment followed by a short charged tail is characteristic of a GPI-anchor signal. Transferable knowledge of secreted, GPI-anchored fungal proteins supports membrane association and therefore C (“side of membrane”). This is a better fit than an endocytic vesicle or nucleolus; “host cell plasma membrane” is also a poor fit for a secreted fungal protein rather than a protein of a host cell.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence contains recognizable secretion and GPI-anchor signal patterns that meaningfully distinguish membrane association from the other offered locations. The inference is probabilistic, and the sequence alone does not establish the exact membrane or leaflet.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is the best-supported offered choice. The sequence does not specify the precise membrane, but no other option is comparably supported by the targeting signals.


### Important caveats

- The reviewer evidence reports computational subcellular-location and GO annotations; it does not provide direct experimental proof of localization.
- The record also describes the protein as secreted and cell-wall-associated, which is compatible with membrane association via a GPI anchor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretion signal, while the C-terminal hydrophobic segment followed by a short charged tail is characteristic of a GPI-anchor signal. Transferable knowledge of secreted, GPI-anchored fungal proteins supports membrane association and therefore C (“side of membrane”). This is a better fit than an endocytic vesicle or nucleolus; “host cell plasma membrane” is also a poor fit for a secreted fungal protein rather than a protein of a host cell.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains recognizable secretion and GPI-anchor signal patterns that meaningfully distinguish membrane association from the other offered locations. The inference is probabilistic, and the sequence alone does not establish the exact membrane or leaflet."
  },
  "case_id": "GO_cellular_component_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as cell membrane-associated with a GPI anchor and assigns GO:0098552, “side of membrane.” These annotations support C, though the GO assignments are computational and do not establish experimental localization."
  },
  "important_caveats": [
    "The reviewer evidence reports computational subcellular-location and GO annotations; it does not provide direct experimental proof of localization.",
    "The record also describes the protein as secreted and cell-wall-associated, which is compatible with membrane association via a GPI anchor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the best-supported offered choice. The sequence does not specify the precise membrane, but no other option is comparably supported by the targeting signals."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as cell membrane-associated with a GPI anchor and assigns GO:0098552, “side of membrane.” These annotations support C, though the GO assignments are computational and do not establish experimental localization.",
    "evidence_ids": ["C5", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretion signal, while the C-terminal hydrophobic segment followed by a short charged tail is characteristic of a GPI-anchor signal. Transferable knowledge of secreted, GPI-anchored fungal proteins supports membrane association and therefore C (“side of membrane”). This is a better fit than an endocytic vesicle or nucleolus; “host cell plasma membrane” is also a poor fit for a secreted fungal protein rather than a protein of a host cell.",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains recognizable secretion and GPI-anchor signal patterns that meaningfully distinguish membrane association from the other offered locations. The inference is probabilistic, and the sequence alone does not establish the exact membrane or leaflet."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the best-supported offered choice. The sequence does not specify the precise membrane, but no other option is comparably supported by the targeting signals."
  },
  "important_caveats": [
    "The reviewer evidence reports computational subcellular-location and GO annotations; it does not provide direct experimental proof of localization.",
    "The record also describes the protein as secreted and cell-wall-associated, which is compatible with membrane association via a GPI anchor."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q4WXE6) annotates GO:0098552 'side of membrane' (IEA:UniProtKB-KW) alongside GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The subcellular location comment states 'Cell membrane; Lipid-anchor, GPI-anchor' and 'Secreted, cell wall.' A GPI-anchored protein resides on one leaflet/surface of the membrane, which matches the GO definition of 'side of membrane': 'one leaflet of a membrane bilayer and any protein embedded or anchored in it or attached to its surface.' The annotation is IEA (inferred from keyword), not experimentally verified, but it is the recorded database annotation consistent with the protein's GPI-anchor topology.

Citations as saved: [H5](#evidence-h5), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features distinguish the choices: (1) The N-terminal sequence 'MSLLYLVALFVASICSVTA' is a classic signal peptide, indicating secretion/membrane targeting, which eliminates D (nucleolus). (2) The central domain contains a GH18 chitinase signature (e.g., 'GAGIISSIVLQSDDLDEIDWEWVGYNTSEVQSNYFGKGNNETFNRGGYHYVPNADTEFHNYTTYWTQEKLEWWIDGKLARTLTYEDSQGAGKYYPQTPCNIRYGIWPAGIKGNAQGTIEWAGGLVDYSKAPFTMVLQSVRVHDFHTGKEYNYTDHSGSWQSIDVIAGNSTIANAIQNPPKSLSEKWAELPTGAKAGVYIGAGCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN'), consistent with a cell-wall remodeling enzyme, not an endocytic vesicle protein, eliminating B. (3) Options A and D carry the 'host cell' prefix, which in GO ontology specifically denotes the membrane/nucleolus of a host cell in a viral/pathogen interaction context (goslim_virus subset). A fungal protein's own membrane would be annotated 'plasma membrane,' not 'host cell plasma membrane,' eliminating A. (4) Near the C-terminus, the hydrophobic stretch 'GCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN' resembles a GPI-anchor signal (hydrophobic region followed by charged residues), indicating attachment to the outer leaflet surface. The GO definition of 'side of membrane' explicitly includes proteins 'anchored in it or attached to its surface,' making C the most precise match for a GPI-anchored protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of signal-peptide recognition, chitinase-family knowledge, GO ontology naming conventions ('host cell' prefix for pathogen context), and GPI-anchor signal identification provides a concrete, transferable reasoning chain that meaningfully distinguishes C from the other three options without requiring recall of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is eliminated by the 'host cell' prefix (inappropriate for a fungal protein's own membrane). Option B is eliminated by the chitinase domain and signal peptide. Option D is eliminated by both the 'host cell' prefix and the secretory signal. Option C is uniquely supported by the GPI-anchor topology and the GO definition. No other option is defensible.


### Important caveats

- The GO:0098552 annotation is IEA:UniProtKB-KW (inferred from keyword), not experimentally determined. The protein's membrane association is inferred from sequence features (GPI anchor) rather than direct experimental localization.
- The protein is also annotated as 'Secreted, cell wall' (ECO:0000305), so 'side of membrane' captures only the membrane-anchored fraction; the full picture includes a secreted cell-wall pool.
- The 'host cell' prefix in options A and D is a strong structural discriminator within the GO ontology, but a model unfamiliar with this convention might still consider A plausible for a membrane protein.
- The GPI-anchor signal recognition from sequence is probabilistic; not all hydrophobic C-terminal stretches are GPI anchors, though the pattern here is consistent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features distinguish the choices: (1) The N-terminal sequence 'MSLLYLVALFVASICSVTA' is a classic signal peptide, indicating secretion/membrane targeting, which eliminates D (nucleolus). (2) The central domain contains a GH18 chitinase signature (e.g., 'GAGIISSIVLQSDDLDEIDWEWVGYNTSEVQSNYFGKGNNETFNRGGYHYVPNADTEFHNYTTYWTQEKLEWWIDGKLARTLTYEDSQGAGKYYPQTPCNIRYGIWPAGIKGNAQGTIEWAGGLVDYSKAPFTMVLQSVRVHDFHTGKEYNYTDHSGSWQSIDVIAGNSTIANAIQNPPKSLSEKWAELPTGAKAGVYIGAGCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN'), consistent with a cell-wall remodeling enzyme, not an endocytic vesicle protein, eliminating B. (3) Options A and D carry the 'host cell' prefix, which in GO ontology specifically denotes the membrane/nucleolus of a host cell in a viral/pathogen interaction context (goslim_virus subset). A fungal protein's own membrane would be annotated 'plasma membrane,' not 'host cell plasma membrane,' eliminating A. (4) Near the C-terminus, the hydrophobic stretch 'GCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN' resembles a GPI-anchor signal (hydrophobic region followed by charged residues), indicating attachment to the outer leaflet surface. The GO definition of 'side of membrane' explicitly includes proteins 'anchored in it or attached to its surface,' making C the most precise match for a GPI-anchored protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of signal-peptide recognition, chitinase-family knowledge, GO ontology naming conventions ('host cell' prefix for pathogen context), and GPI-anchor signal identification provides a concrete, transferable reasoning chain that meaningfully distinguishes C from the other three options without requiring recall of this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q4WXE6) annotates GO:0098552 'side of membrane' (IEA:UniProtKB-KW) alongside GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The subcellular location comment states 'Cell membrane; Lipid-anchor, GPI-anchor' and 'Secreted, cell wall.' A GPI-anchored protein resides on one leaflet/surface of the membrane, which matches the GO definition of 'side of membrane': 'one leaflet of a membrane bilayer and any protein embedded or anchored in it or attached to its surface.' The annotation is IEA (inferred from keyword), not experimentally verified, but it is the recorded database annotation consistent with the protein's GPI-anchor topology."
  },
  "important_caveats": [
    "The GO:0098552 annotation is IEA:UniProtKB-KW (inferred from keyword), not experimentally determined. The protein's membrane association is inferred from sequence features (GPI anchor) rather than direct experimental localization.",
    "The protein is also annotated as 'Secreted, cell wall' (ECO:0000305), so 'side of membrane' captures only the membrane-anchored fraction; the full picture includes a secreted cell-wall pool.",
    "The 'host cell' prefix in options A and D is a strong structural discriminator within the GO ontology, but a model unfamiliar with this convention might still consider A plausible for a membrane protein.",
    "The GPI-anchor signal recognition from sequence is probabilistic; not all hydrophobic C-terminal stretches are GPI anchors, though the pattern here is consistent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by the 'host cell' prefix (inappropriate for a fungal protein's own membrane). Option B is eliminated by the chitinase domain and signal peptide. Option D is eliminated by both the 'host cell' prefix and the secretory signal. Option C is uniquely supported by the GPI-anchor topology and the GO definition. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q4WXE6) annotates GO:0098552 'side of membrane' (IEA:UniProtKB-KW) alongside GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The subcellular location comment states 'Cell membrane; Lipid-anchor, GPI-anchor' and 'Secreted, cell wall.' A GPI-anchored protein resides on one leaflet/surface of the membrane, which matches the GO definition of 'side of membrane': 'one leaflet of a membrane bilayer and any protein embedded or anchored in it or attached to its surface.' The annotation is IEA (inferred from keyword), not experimentally verified, but it is the recorded database annotation consistent with the protein's GPI-anchor topology.",
    "evidence_ids": ["H5", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features distinguish the choices: (1) The N-terminal sequence 'MSLLYLVALFVASICSVTA' is a classic signal peptide, indicating secretion/membrane targeting, which eliminates D (nucleolus). (2) The central domain contains a GH18 chitinase signature (e.g., 'GAGIISSIVLQSDDLDEIDWEWVGYNTSEVQSNYFGKGNNETFNRGGYHYVPNADTEFHNYTTYWTQEKLEWWIDGKLARTLTYEDSQGAGKYYPQTPCNIRYGIWPAGIKGNAQGTIEWAGGLVDYSKAPFTMVLQSVRVHDFHTGKEYNYTDHSGSWQSIDVIAGNSTIANAIQNPPKSLSEKWAELPTGAKAGVYIGAGCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN'), consistent with a cell-wall remodeling enzyme, not an endocytic vesicle protein, eliminating B. (3) Options A and D carry the 'host cell' prefix, which in GO ontology specifically denotes the membrane/nucleolus of a host cell in a viral/pathogen interaction context (goslim_virus subset). A fungal protein's own membrane would be annotated 'plasma membrane,' not 'host cell plasma membrane,' eliminating A. (4) Near the C-terminus, the hydrophobic stretch 'GCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN' resembles a GPI-anchor signal (hydrophobic region followed by charged residues), indicating attachment to the outer leaflet surface. The GO definition of 'side of membrane' explicitly includes proteins 'anchored in it or attached to its surface,' making C the most precise match for a GPI-anchored protein.",
    "missing_item_specific_fact": "",
    "reason": "The combination of signal-peptide recognition, chitinase-family knowledge, GO ontology naming conventions ('host cell' prefix for pathogen context), and GPI-anchor signal identification provides a concrete, transferable reasoning chain that meaningfully distinguishes C from the other three options without requiring recall of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by the 'host cell' prefix (inappropriate for a fungal protein's own membrane). Option B is eliminated by the chitinase domain and signal peptide. Option D is eliminated by both the 'host cell' prefix and the secretory signal. Option C is uniquely supported by the GPI-anchor topology and the GO definition. No other option is defensible."
  },
  "important_caveats": [
    "The GO:0098552 annotation is IEA:UniProtKB-KW (inferred from keyword), not experimentally determined. The protein's membrane association is inferred from sequence features (GPI anchor) rather than direct experimental localization.",
    "The protein is also annotated as 'Secreted, cell wall' (ECO:0000305), so 'side of membrane' captures only the membrane-anchored fraction; the full picture includes a secreted cell-wall pool.",
    "The 'host cell' prefix in options A and D is a strong structural discriminator within the GO ontology, but a model unfamiliar with this convention might still consider A plausible for a membrane protein.",
    "The GPI-anchor signal recognition from sequence is probabilistic; not all hydrophobic C-terminal stretches are GPI anchors, though the pattern here is consistent."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9902\",\"value\":\"Lipid-anchor, GPI-anchor\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"id\":\"SL-0041\",\"value\":\"Secreted, cell wall\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
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
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C7",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000255}; Lipid-anchor, GPI-\nCC       anchor {ECO:0000255}. Secreted, cell wall {ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-66",
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
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0098552; C:side of membrane; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0020002\nname: host cell plasma membrane\nnamespace: cellular_component\ndef: \"The plasma membrane surrounding a host cell.\" [GOC:mb]\nsubset: goslim_virus\nis_a: GO:0033644 ! host cell membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020002",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155120-155127",
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
  "excerpt": "[Term]\nid: GO:0030139\nname: endocytic vesicle\nnamespace: cellular_component\ndef: \"A membrane-bounded intracellular vesicle formed by invagination of the plasma membrane around an extracellular substance. Endocytic vesicles fuse with early endosomes to deliver the cargo for further sorting.\" [GOC:curators, PMID:19696797]\nsynonym: \"endocytotic transport vesicle\" EXACT []\nsynonym: \"endocytotic vesicle\" EXACT []\nxref: NIF_Subcellular:sao1362520468\nis_a: GO:0031410 ! cytoplasmic vesicle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030139",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 163117-163126",
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
  "excerpt": "[Term]\nid: GO:0044196\nname: host cell nucleolus\nnamespace: cellular_component\ndef: \"A small, dense body one or more of which are present in the nucleus of eukaryotic host cells.\" [GOC:jl]\nis_a: GO:0044094 ! host cell nuclear part\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044196",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 255128-255134",
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
  "excerpt": "[Term]\nid: GO:0098552\nname: side of membrane\nnamespace: cellular_component\ndef: \"A cellular component consisting of one leaflet of a membrane bilayer and any protein embedded or anchored in it or attached to its surface.\" [GOC:dos]\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0016020 ! membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0098552",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 408943-408950",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
