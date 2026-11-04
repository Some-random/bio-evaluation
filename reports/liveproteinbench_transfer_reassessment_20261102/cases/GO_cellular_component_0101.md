# GO_cellular_component_0101

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0101.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — ATP-binding cassette (ABC) transporter complex

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTTSPGTVESTTPVSGQLRTVLSAGERPARATAVSATLTHLWRAMMAFKHFPVQLIDIVLMPLIFLLMFTYLFGGAFADSTEEYLQFYLPGVTVQAVVMMTVYTGTSLNTDIHKGVFDRFRTLPFWQPATLAGSLLGDVLRYVVALATTVFLGLLLGFRADGGFLGVVGAMLVLIVFGFSVSWIFAALGVVASEPERVSGTSMIVLYPLLFMSNIFVMPETMPGWMQAIVDANPMSHAATASRELMHGTAGFWDVGLVLCVSAGLVAVFAPLTMRLYRNKNAH

[Multiple Choices]
A. cytoplasmic vesicle
B. host cell plasma membrane
C. ATP-binding cassette (ABC) transporter complex
D. histone acetyltransferase complex
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

> The sequence-matched UniProt record annotates this protein to the ATP-binding cassette (ABC) transporter complex (GO:0043190), with evidence type IEA:InterPro. This supports the keyed GO annotation, though it is computational rather than direct experimental evidence. The record also describes a multipass cell-membrane permease, consistent with a transporter component.

Citations as saved: [H4](#evidence-h4), [C6](#evidence-c6), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly hydrophobic in multiple stretches, consistent with a multipass membrane transport protein rather than a soluble histone acetyltransferase complex component. Given the choices, the ABC transporter complex is the plausible transporter-associated option; a cytoplasmic vesicle is not a natural fit for this bacterial-looking membrane protein, and a host cell plasma membrane is not an appropriate localization for a bacterial protein. This is a probabilistic inference: the sequence alone does not uniquely establish ABC family membership.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about multipass membrane proteins and the biological context meaningfully favors C among these alternatives. The lack of a sequence feature uniquely identifying an ABC permease limits certainty but does not make target-specific lookup necessary to choose among the offered options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives do not offer a competing bacterial membrane-transporter complex; the multipass transporter inference favors C over the other listed choices.


### Important caveats

- The exact ABC-complex annotation is computational (IEA:InterPro); the supplied evidence does not establish it by direct experiment.
- The sequence supports a multipass membrane protein more clearly than it establishes the ABC transporter family specifically.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic in multiple stretches, consistent with a multipass membrane transport protein rather than a soluble histone acetyltransferase complex component. Given the choices, the ABC transporter complex is the plausible transporter-associated option; a cytoplasmic vesicle is not a natural fit for this bacterial-looking membrane protein, and a host cell plasma membrane is not an appropriate localization for a bacterial protein. This is a probabilistic inference: the sequence alone does not uniquely establish ABC family membership.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about multipass membrane proteins and the biological context meaningfully favors C among these alternatives. The lack of a sequence feature uniquely identifying an ABC permease limits certainty but does not make target-specific lookup necessary to choose among the offered options."
  },
  "case_id": "GO_cellular_component_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C6",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein to the ATP-binding cassette (ABC) transporter complex (GO:0043190), with evidence type IEA:InterPro. This supports the keyed GO annotation, though it is computational rather than direct experimental evidence. The record also describes a multipass cell-membrane permease, consistent with a transporter component."
  },
  "important_caveats": [
    "The exact ABC-complex annotation is computational (IEA:InterPro); the supplied evidence does not establish it by direct experiment.",
    "The sequence supports a multipass membrane protein more clearly than it establishes the ABC transporter family specifically."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives do not offer a competing bacterial membrane-transporter complex; the multipass transporter inference favors C over the other listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein to the ATP-binding cassette (ABC) transporter complex (GO:0043190), with evidence type IEA:InterPro. This supports the keyed GO annotation, though it is computational rather than direct experimental evidence. The record also describes a multipass cell-membrane permease, consistent with a transporter component.",
    "evidence_ids": ["H4", "C6", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic in multiple stretches, consistent with a multipass membrane transport protein rather than a soluble histone acetyltransferase complex component. Given the choices, the ABC transporter complex is the plausible transporter-associated option; a cytoplasmic vesicle is not a natural fit for this bacterial-looking membrane protein, and a host cell plasma membrane is not an appropriate localization for a bacterial protein. This is a probabilistic inference: the sequence alone does not uniquely establish ABC family membership.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about multipass membrane proteins and the biological context meaningfully favors C among these alternatives. The lack of a sequence feature uniquely identifying an ABC permease limits certainty but does not make target-specific lookup necessary to choose among the offered options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives do not offer a competing bacterial membrane-transporter complex; the multipass transporter inference favors C over the other listed choices."
  },
  "important_caveats": [
    "The exact ABC-complex annotation is computational (IEA:InterPro); the supplied evidence does not establish it by direct experiment.",
    "The sequence supports a multipass membrane protein more clearly than it establishes the ABC transporter family specifically."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU4 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB1' (C4), a multi-pass membrane protein at the cell membrane (C5/H3), and carries GO:0043190 (ABC transporter complex) with IEA:InterPro evidence (C6/H4). The GO annotation is computational (InterPro domain match) rather than directly experimental, but the protein name, topology annotation, and the GO term definition (GO:0043190 includes 'ABC-type efflux permease complex' as a NARROW synonym) are all consistent with the expected answer. The permease is a structural component of the ABC transporter complex.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~283 aa) contains approximately 6-8 long hydrophobic stretches (e.g., 'LIDIVLMPLIFLLMFTYLFGGAFADS', 'VVMMTVYTGTSLNTDIHKGVFDRFRTLPFWQPATLAGSLLGDVLRYVVALATTVFLGLLLG', 'VGAMLVLIVFGFSVSWIFAALGVVASEPER', 'IVLYPLLFMSNIFVMPETMPGWMQAIVDANPMSH', 'WDVGLVLCVSAGLVAVFAPLTMRLYRNKNAH') characteristic of a multi-pass membrane protein. This immediately eliminates D (histone acetyltransferase complex — a eukaryotic nuclear/chromatin complex with no relevance to a hydrophobic bacterial membrane protein) and A (cytoplasmic vesicle — a eukaryotic intracellular compartment; bacteria lack such vesicles, and the protein is clearly membrane-integrated, not soluble). Option B, 'host cell plasma membrane' (GO:0020002), is a GO term specifically defined for viral proteins localizing to the host cell membrane (goslim_virus subset per the ontology); a bacterial protein is never annotated with this term. This leaves C: a multi-pass membrane protein in a bacterium with no soluble enzymatic domain is most parsimoniously classified as a permease component of an ABC transporter complex, which is one of the most abundant multi-pass membrane protein families in bacteria. The absence of nucleotide-binding domains (Walker A/B motifs) is consistent with being the transmembrane permease subunit rather than the cytoplasmic ATPase subunit.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use (1) hydrophobicity analysis to identify multiple TM helices → membrane protein, (2) recognition that the protein is bacterial (no eukaryotic targeting signals, no nuclear localization signals) to eliminate D and A, (3) knowledge that GO:0020002 'host cell plasma membrane' is a viral-specific term to eliminate B, and (4) the general pattern that multi-pass membrane proteins in bacteria with no cytoplasmic enzymatic domains are frequently ABC transporter permeases. This chain of reasoning meaningfully distinguishes C from the other three options without requiring recall of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor is eliminated by a clear biological argument: A (eukaryotic vesicle, incompatible with bacterial membrane protein), B (viral-specific GO term, incompatible with a bacterial protein), D (eukaryotic nuclear chromatin complex, incompatible with a hydrophobic bacterial membrane protein). Only C remains consistent with a multi-pass membrane protein from a bacterium.


### Important caveats

- The GO:0043190 annotation in UniProt carries IEA:InterPro evidence (computational domain match), not direct experimental evidence. However, the protein name 'ABC transporter permease' and the InterPro domain assignment provide reasonable support.
- The UniProt entry also carries GO:0005886 (plasma membrane, ISS:UniProtKB), but this is a different term from option B's GO:0020002 (host cell plasma membrane), so there is no conflict with the expected answer.
- The protein was first released in Swiss-Prot in January 2026; the benchmark's exact source snapshot is unknown, but sequence match is confirmed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~283 aa) contains approximately 6-8 long hydrophobic stretches (e.g., 'LIDIVLMPLIFLLMFTYLFGGAFADS', 'VVMMTVYTGTSLNTDIHKGVFDRFRTLPFWQPATLAGSLLGDVLRYVVALATTVFLGLLLG', 'VGAMLVLIVFGFSVSWIFAALGVVASEPER', 'IVLYPLLFMSNIFVMPETMPGWMQAIVDANPMSH', 'WDVGLVLCVSAGLVAVFAPLTMRLYRNKNAH') characteristic of a multi-pass membrane protein. This immediately eliminates D (histone acetyltransferase complex — a eukaryotic nuclear/chromatin complex with no relevance to a hydrophobic bacterial membrane protein) and A (cytoplasmic vesicle — a eukaryotic intracellular compartment; bacteria lack such vesicles, and the protein is clearly membrane-integrated, not soluble). Option B, 'host cell plasma membrane' (GO:0020002), is a GO term specifically defined for viral proteins localizing to the host cell membrane (goslim_virus subset per the ontology); a bacterial protein is never annotated with this term. This leaves C: a multi-pass membrane protein in a bacterium with no soluble enzymatic domain is most parsimoniously classified as a permease component of an ABC transporter complex, which is one of the most abundant multi-pass membrane protein families in bacteria. The absence of nucleotide-binding domains (Walker A/B motifs) is consistent with being the transmembrane permease subunit rather than the cytoplasmic ATPase subunit.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use (1) hydrophobicity analysis to identify multiple TM helices → membrane protein, (2) recognition that the protein is bacterial (no eukaryotic targeting signals, no nuclear localization signals) to eliminate D and A, (3) knowledge that GO:0020002 'host cell plasma membrane' is a viral-specific term to eliminate B, and (4) the general pattern that multi-pass membrane proteins in bacteria with no cytoplasmic enzymatic domains are frequently ABC transporter permeases. This chain of reasoning meaningfully distinguishes C from the other three options without requiring recall of this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU4 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB1' (C4), a multi-pass membrane protein at the cell membrane (C5/H3), and carries GO:0043190 (ABC transporter complex) with IEA:InterPro evidence (C6/H4). The GO annotation is computational (InterPro domain match) rather than directly experimental, but the protein name, topology annotation, and the GO term definition (GO:0043190 includes 'ABC-type efflux permease complex' as a NARROW synonym) are all consistent with the expected answer. The permease is a structural component of the ABC transporter complex."
  },
  "important_caveats": [
    "The GO:0043190 annotation in UniProt carries IEA:InterPro evidence (computational domain match), not direct experimental evidence. However, the protein name 'ABC transporter permease' and the InterPro domain assignment provide reasonable support.",
    "The UniProt entry also carries GO:0005886 (plasma membrane, ISS:UniProtKB), but this is a different term from option B's GO:0020002 (host cell plasma membrane), so there is no conflict with the expected answer.",
    "The protein was first released in Swiss-Prot in January 2026; the benchmark's exact source snapshot is unknown, but sequence match is confirmed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor is eliminated by a clear biological argument: A (eukaryotic vesicle, incompatible with bacterial membrane protein), B (viral-specific GO term, incompatible with a bacterial protein), D (eukaryotic nuclear chromatin complex, incompatible with a hydrophobic bacterial membrane protein). Only C remains consistent with a multi-pass membrane protein from a bacterium."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU4 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB1' (C4), a multi-pass membrane protein at the cell membrane (C5/H3), and carries GO:0043190 (ABC transporter complex) with IEA:InterPro evidence (C6/H4). The GO annotation is computational (InterPro domain match) rather than directly experimental, but the protein name, topology annotation, and the GO term definition (GO:0043190 includes 'ABC-type efflux permease complex' as a NARROW synonym) are all consistent with the expected answer. The permease is a structural component of the ABC transporter complex.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~283 aa) contains approximately 6-8 long hydrophobic stretches (e.g., 'LIDIVLMPLIFLLMFTYLFGGAFADS', 'VVMMTVYTGTSLNTDIHKGVFDRFRTLPFWQPATLAGSLLGDVLRYVVALATTVFLGLLLG', 'VGAMLVLIVFGFSVSWIFAALGVVASEPER', 'IVLYPLLFMSNIFVMPETMPGWMQAIVDANPMSH', 'WDVGLVLCVSAGLVAVFAPLTMRLYRNKNAH') characteristic of a multi-pass membrane protein. This immediately eliminates D (histone acetyltransferase complex — a eukaryotic nuclear/chromatin complex with no relevance to a hydrophobic bacterial membrane protein) and A (cytoplasmic vesicle — a eukaryotic intracellular compartment; bacteria lack such vesicles, and the protein is clearly membrane-integrated, not soluble). Option B, 'host cell plasma membrane' (GO:0020002), is a GO term specifically defined for viral proteins localizing to the host cell membrane (goslim_virus subset per the ontology); a bacterial protein is never annotated with this term. This leaves C: a multi-pass membrane protein in a bacterium with no soluble enzymatic domain is most parsimoniously classified as a permease component of an ABC transporter complex, which is one of the most abundant multi-pass membrane protein families in bacteria. The absence of nucleotide-binding domains (Walker A/B motifs) is consistent with being the transmembrane permease subunit rather than the cytoplasmic ATPase subunit.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use (1) hydrophobicity analysis to identify multiple TM helices → membrane protein, (2) recognition that the protein is bacterial (no eukaryotic targeting signals, no nuclear localization signals) to eliminate D and A, (3) knowledge that GO:0020002 'host cell plasma membrane' is a viral-specific term to eliminate B, and (4) the general pattern that multi-pass membrane proteins in bacteria with no cytoplasmic enzymatic domains are frequently ABC transporter permeases. This chain of reasoning meaningfully distinguishes C from the other three options without requiring recall of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor is eliminated by a clear biological argument: A (eukaryotic vesicle, incompatible with bacterial membrane protein), B (viral-specific GO term, incompatible with a bacterial protein), D (eukaryotic nuclear chromatin complex, incompatible with a hydrophobic bacterial membrane protein). Only C remains consistent with a multi-pass membrane protein from a bacterium."
  },
  "important_caveats": [
    "The GO:0043190 annotation in UniProt carries IEA:InterPro evidence (computational domain match), not direct experimental evidence. However, the protein name 'ABC transporter permease' and the InterPro domain assignment provide reasonable support.",
    "The UniProt entry also carries GO:0005886 (plasma membrane, ISS:UniProtKB), but this is a different term from option B's GO:0020002 (host cell plasma membrane), so there is no conflict with the expected answer.",
    "The protein was first released in Swiss-Prot in January 2026; the benchmark's exact source snapshot is unknown, but sequence match is confirmed."
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
  "benchmark_sequence_length": 283,
  "benchmark_sequence_sha256": "044fc3aafdd7290b8ba81d7a359f1000702344148420b3b5202673cb2206cc44",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 283,
  "current_source_sequence_sha256": "044fc3aafdd7290b8ba81d7a359f1000702344148420b3b5202673cb2206cc44",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXU4",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "selected_historical_source_sequence_length": 283,
  "selected_historical_source_sequence_sha256": "044fc3aafdd7290b8ba81d7a359f1000702344148420b3b5202673cb2206cc44",
  "selected_historical_version": {
    "accession": "P0DXU4",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRB1_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ABC transporter permease protein DrrB1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32011\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0043190\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:ATP-binding cassette (ABC) transporter complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRB1_STRC4             Reviewed;         283 AA.\nAC   P0DXU4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ABC transporter permease protein DrrB1 {ECO:0000305};\nGN   Name=drrB1 {ECO:0000303|PubMed:39375957};\nGN   Synonyms=drrB {ECO:0000312|EMBL:WOT33551.1};\nGN   ORFNames=R5U08_05030 {ECO:0000312|EMBL:WOT33551.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P32011};\nCC       Multi-pass membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0043190; C:ATP-binding cassette (ABC) transporter complex; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000123\nname: histone acetyltransferase complex\nnamespace: cellular_component\ndef: \"A protein complex that possesses histone acetyltransferase activity.\" [GOC:mah]\ncomment: Note that this term represents a protein complex, not a function; the activity possessed by this complex is mentioned in the definition for the purpose of describing and distinguishing the complex. The function of this complex is represented by the molecular function term 'histone acetyltransferase activity ; GO:0004402'.\nsynonym: \"histone acetylase complex\" EXACT []\nis_a: GO:0031248 ! protein acetyltransferase complex\nrelationship: part_of GO:0000785 ! chromatin\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000123",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1242-1251",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0031410\nname: cytoplasmic vesicle\nnamespace: cellular_component\nalt_id: GO:0016023\ndef: \"A vesicle found in the cytoplasm of a cell.\" [GOC:ai, GOC:mah, GOC:vesicles]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_yeast\nsynonym: \"cytoplasmic membrane bounded vesicle\" RELATED []\nsynonym: \"cytoplasmic membrane-enclosed vesicle\" RELATED []\nsynonym: \"cytoplasmic, membrane-bounded vesicle\" RELATED []\nxref: NIF_Subcellular:sao180601769\nis_a: GO:0097708 ! intracellular vesicle\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031410",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 176239-176257",
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
  "excerpt": "[Term]\nid: GO:0043190\nname: ATP-binding cassette (ABC) transporter complex\nnamespace: cellular_component\nalt_id: GO:0043191\nalt_id: GO:0043192\ndef: \"A complex for the transport of metabolites into and out of the cell, typically comprised of four domains; two membrane-associated domains and two ATP-binding domains at the intracellular face of the membrane, that form a central pore through the plasma membrane. Each of the four core domains may be encoded as a separate polypeptide or the domains can be fused in any one of a number of ways into multidomain polypeptides. In Bacteria and Archaebacteria, ABC transporters also include substrate binding proteins to bind substrate external to the cytoplasm and deliver it to the transporter.\" [GOC:jl, GOC:mtg_sensu, PMID:11421269, PMID:15111107]\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"ABC-type efflux permease complex\" NARROW []\nsynonym: \"ABC-type efflux porter complex\" NARROW []\nsynonym: \"ABC-type uptake permease complex\" NARROW []\nsynonym: \"mating pheromone exporter\" NARROW []\nis_a: GO:0098533 ! ATPase dependent transmembrane transport complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043190",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 244782-244797",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 101. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
