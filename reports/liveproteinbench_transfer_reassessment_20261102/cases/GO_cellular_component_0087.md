# GO_cellular_component_0087

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0087.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAVMKFTWRSIIPRCSKGIEEPEAEAEAEPETKKQDSKQGSFSRLAMIDLSYPSSRFTEDLSTSLAGSNLYVFTLEELKVITQCFSSANFLGEGGFGPVHKGFIDDNLRPGLEAQPVAVKLLDLEGLQGHREWLTEVVFLAQLSHPHLVKLIGYCCEDEHRLLVYEYMPRGSLENQLFAKYSVPLPWSTRMKIALGAAKGLAYLHEAEKPVIYRDFKASNILLDSDYSAKLSDFGLAKDGPEGDKTHVSTRVMGTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRSLDKSRSPREQNLAEWARPMLNESRRLARIMDPKLEGQYSETGARKAAALAYQCLSHRAKQRPKMSDVVNILEPLLDYEETSVGTFVYTVPTHQNGGSPPKDDTDTKECEAKTELKKENGDHHNRHHHRRSHKSRDGHRHRNKSSSQSSVHSENYTSKQTLENGSNEECNID

[Multiple Choices]
A. synapse
B. SAGA complex
C. plasma membrane
D. vitelline envelope
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

> The matched-sequence UniProt record annotates cell membrane based on evidence transferred from a homolog, and assigns plasma membrane by ISS. These support the keyed choice, but are computational/transfer annotations rather than direct experimental localization evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a recognizable protein kinase domain, including conserved catalytic motifs, consistent with an intracellular signaling kinase rather than a SAGA structural or enzymatic subunit, a synaptic component, or a vitelline-envelope protein. Kinases in signaling pathways can associate with the plasma membrane, making that choice a credible best fit among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable kinase-family and signaling knowledge gives a meaningful, though probabilistic, basis for preferring plasma membrane among the offered choices. The sequence does not itself establish that localization: it lacks an obvious transmembrane segment, and kinase-domain recognition alone cannot distinguish membrane-associated from other intracellular kinases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice has comparable support from the sequence and general protein biology, although the precise localization is not determined with certainty.


### Important caveats

- The source annotation is sequence-matched, but the supplied localization evidence is transferred or computational; direct experimental confirmation is not established here.
- Reviewer-only organism and protein identity information was not used as an original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a recognizable protein kinase domain, including conserved catalytic motifs, consistent with an intracellular signaling kinase rather than a SAGA structural or enzymatic subunit, a synaptic component, or a vitelline-envelope protein. Kinases in signaling pathways can associate with the plasma membrane, making that choice a credible best fit among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase-family and signaling knowledge gives a meaningful, though probabilistic, basis for preferring plasma membrane among the offered choices. The sequence does not itself establish that localization: it lacks an obvious transmembrane segment, and kinase-domain recognition alone cannot distinguish membrane-associated from other intracellular kinases."
  },
  "case_id": "GO_cellular_component_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates cell membrane based on evidence transferred from a homolog, and assigns plasma membrane by ISS. These support the keyed choice, but are computational/transfer annotations rather than direct experimental localization evidence."
  },
  "important_caveats": [
    "The source annotation is sequence-matched, but the supplied localization evidence is transferred or computational; direct experimental confirmation is not established here.",
    "Reviewer-only organism and protein identity information was not used as an original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice has comparable support from the sequence and general protein biology, although the precise localization is not determined with certainty."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates cell membrane based on evidence transferred from a homolog, and assigns plasma membrane by ISS. These support the keyed choice, but are computational/transfer annotations rather than direct experimental localization evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a recognizable protein kinase domain, including conserved catalytic motifs, consistent with an intracellular signaling kinase rather than a SAGA structural or enzymatic subunit, a synaptic component, or a vitelline-envelope protein. Kinases in signaling pathways can associate with the plasma membrane, making that choice a credible best fit among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Transferable kinase-family and signaling knowledge gives a meaningful, though probabilistic, basis for preferring plasma membrane among the offered choices. The sequence does not itself establish that localization: it lacks an obvious transmembrane segment, and kinase-domain recognition alone cannot distinguish membrane-associated from other intracellular kinases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice has comparable support from the sequence and general protein biology, although the precise localization is not determined with certainty."
  },
  "important_caveats": [
    "The source annotation is sequence-matched, but the supplied localization evidence is transferred or computational; direct experimental confirmation is not established here.",
    "Reviewer-only organism and protein identity information was not used as an original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates the protein's subcellular location as 'Cell membrane' (SL-0039) with evidence code ECO:0000250 (inferred by similarity from Q9ZUF4), and the GO cross-reference is GO:0005886 (plasma membrane, ISS:UniProtKB). The GO ontology confirms 'cell membrane' as an EXACT synonym of GO:0005886 'plasma membrane.' The protein name 'EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5A' is consistent with plasma membrane association (RLCKs are membrane-associated without spanning). However, the evidence is computational (ISS), not direct experimental localization.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains clear serine/threonine kinase domain motifs: glycine-rich loop (GEGGFG at ~residues 108-113), catalytic HRD-like loop (HRLLVYEYMPRGS), DFG motif (SDFGLAK), and APE motif (GTRGYAAPEYIMTG). This identifies the protein as a protein kinase. Among the four choices: (A) Synapse requires synaptic targeting domains (SNARE, SH3, PDZ, C2) and is an animal neuronal structure—absent here. (B) SAGA complex components have HAT, DUB, or TAF domains, not kinase domains—clearly incompatible. (D) Vitelline envelope is an animal egg coat glycoprotein structure—no egg coat motifs present. (C) Plasma membrane is the only viable option: the protein lacks a transmembrane domain (no 20+ residue hydrophobic stretch), consistent with a receptor-like cytoplasmic kinase (RLCK) family, which associates with the plasma membrane via lipid modifications or protein interactions. A knowledgeable model can eliminate A, B, and D by domain content and biological context, leaving C as the only plausible membrane-associated location for a kinase.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The kinase domain is unambiguously identifiable from conserved sequence motifs. Eliminating the three distractors requires only general knowledge: SAGA complex proteins are chromatin factors (not kinases), synapses are animal neuronal structures requiring specific domains, and vitelline envelopes are animal egg structures. The remaining option (plasma membrane) is the only compartment where a membrane-associated kinase would reside. Plant RLCK family knowledge provides additional confirmation but the elimination logic works without it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are highly distinct in biological context and protein type. A kinase domain clearly excludes SAGA complex membership. Synapse and vitelline envelope are animal-specific structures with incompatible protein compositions. Only plasma membrane is consistent with a membrane-associated kinase lacking a transmembrane domain.


### Important caveats

- The UniProt localization annotation is inferred by similarity (ECO:0000250/ISS), not direct experimental evidence. The actual membrane association of this specific protein may rely on the functional study (PubMed:39488762) but the subcellular location annotation itself is transferred.
- The protein name contains 'cytoplasmic,' which could cause confusion with a cytoplasmic location. However, RLCKs are a well-defined family that associates with the plasma membrane despite lacking transmembrane domains; 'cytoplasmic' here refers to the kinase domain being on the cytoplasmic face, not to a soluble cytoplasmic location.
- The model cannot determine the organism (Gossypium barbadense) from the sequence alone, but the elimination of synapse and vitelline envelope does not require organism knowledge—it follows from domain content and protein type.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains clear serine/threonine kinase domain motifs: glycine-rich loop (GEGGFG at ~residues 108-113), catalytic HRD-like loop (HRLLVYEYMPRGS), DFG motif (SDFGLAK), and APE motif (GTRGYAAPEYIMTG). This identifies the protein as a protein kinase. Among the four choices: (A) Synapse requires synaptic targeting domains (SNARE, SH3, PDZ, C2) and is an animal neuronal structure—absent here. (B) SAGA complex components have HAT, DUB, or TAF domains, not kinase domains—clearly incompatible. (D) Vitelline envelope is an animal egg coat glycoprotein structure—no egg coat motifs present. (C) Plasma membrane is the only viable option: the protein lacks a transmembrane domain (no 20+ residue hydrophobic stretch), consistent with a receptor-like cytoplasmic kinase (RLCK) family, which associates with the plasma membrane via lipid modifications or protein interactions. A knowledgeable model can eliminate A, B, and D by domain content and biological context, leaving C as the only plausible membrane-associated location for a kinase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The kinase domain is unambiguously identifiable from conserved sequence motifs. Eliminating the three distractors requires only general knowledge: SAGA complex proteins are chromatin factors (not kinases), synapses are animal neuronal structures requiring specific domains, and vitelline envelopes are animal egg structures. The remaining option (plasma membrane) is the only compartment where a membrane-associated kinase would reside. Plant RLCK family knowledge provides additional confirmation but the elimination logic works without it."
  },
  "case_id": "GO_cellular_component_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates the protein's subcellular location as 'Cell membrane' (SL-0039) with evidence code ECO:0000250 (inferred by similarity from Q9ZUF4), and the GO cross-reference is GO:0005886 (plasma membrane, ISS:UniProtKB). The GO ontology confirms 'cell membrane' as an EXACT synonym of GO:0005886 'plasma membrane.' The protein name 'EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5A' is consistent with plasma membrane association (RLCKs are membrane-associated without spanning). However, the evidence is computational (ISS), not direct experimental localization."
  },
  "important_caveats": [
    "The UniProt localization annotation is inferred by similarity (ECO:0000250/ISS), not direct experimental evidence. The actual membrane association of this specific protein may rely on the functional study (PubMed:39488762) but the subcellular location annotation itself is transferred.",
    "The protein name contains 'cytoplasmic,' which could cause confusion with a cytoplasmic location. However, RLCKs are a well-defined family that associates with the plasma membrane despite lacking transmembrane domains; 'cytoplasmic' here refers to the kinase domain being on the cytoplasmic face, not to a soluble cytoplasmic location.",
    "The model cannot determine the organism (Gossypium barbadense) from the sequence alone, but the elimination of synapse and vitelline envelope does not require organism knowledge—it follows from domain content and protein type."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are highly distinct in biological context and protein type. A kinase domain clearly excludes SAGA complex membership. Synapse and vitelline envelope are animal-specific structures with incompatible protein compositions. Only plasma membrane is consistent with a membrane-associated kinase lacking a transmembrane domain."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates the protein's subcellular location as 'Cell membrane' (SL-0039) with evidence code ECO:0000250 (inferred by similarity from Q9ZUF4), and the GO cross-reference is GO:0005886 (plasma membrane, ISS:UniProtKB). The GO ontology confirms 'cell membrane' as an EXACT synonym of GO:0005886 'plasma membrane.' The protein name 'EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5A' is consistent with plasma membrane association (RLCKs are membrane-associated without spanning). However, the evidence is computational (ISS), not direct experimental localization.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains clear serine/threonine kinase domain motifs: glycine-rich loop (GEGGFG at ~residues 108-113), catalytic HRD-like loop (HRLLVYEYMPRGS), DFG motif (SDFGLAK), and APE motif (GTRGYAAPEYIMTG). This identifies the protein as a protein kinase. Among the four choices: (A) Synapse requires synaptic targeting domains (SNARE, SH3, PDZ, C2) and is an animal neuronal structure—absent here. (B) SAGA complex components have HAT, DUB, or TAF domains, not kinase domains—clearly incompatible. (D) Vitelline envelope is an animal egg coat glycoprotein structure—no egg coat motifs present. (C) Plasma membrane is the only viable option: the protein lacks a transmembrane domain (no 20+ residue hydrophobic stretch), consistent with a receptor-like cytoplasmic kinase (RLCK) family, which associates with the plasma membrane via lipid modifications or protein interactions. A knowledgeable model can eliminate A, B, and D by domain content and biological context, leaving C as the only plausible membrane-associated location for a kinase.",
    "missing_item_specific_fact": "",
    "reason": "The kinase domain is unambiguously identifiable from conserved sequence motifs. Eliminating the three distractors requires only general knowledge: SAGA complex proteins are chromatin factors (not kinases), synapses are animal neuronal structures requiring specific domains, and vitelline envelopes are animal egg structures. The remaining option (plasma membrane) is the only compartment where a membrane-associated kinase would reside. Plant RLCK family knowledge provides additional confirmation but the elimination logic works without it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are highly distinct in biological context and protein type. A kinase domain clearly excludes SAGA complex membership. Synapse and vitelline envelope are animal-specific structures with incompatible protein compositions. Only plasma membrane is consistent with a membrane-associated kinase lacking a transmembrane domain."
  },
  "important_caveats": [
    "The UniProt localization annotation is inferred by similarity (ECO:0000250/ISS), not direct experimental evidence. The actual membrane association of this specific protein may rely on the functional study (PubMed:39488762) but the subcellular location annotation itself is transferred.",
    "The protein name contains 'cytoplasmic,' which could cause confusion with a cytoplasmic location. However, RLCKs are a well-defined family that associates with the plasma membrane despite lacking transmembrane domains; 'cytoplasmic' here refers to the kinase domain being on the cytoplasmic face, not to a soluble cytoplasmic location.",
    "The model cannot determine the organism (Gossypium barbadense) from the sequence alone, but the elimination of synapse and vitelline envelope does not require organism knowledge—it follows from domain content and protein type."
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
  "benchmark_sequence_length": 462,
  "benchmark_sequence_sha256": "42162c00b0c88b29ae0a2c6b6adef777a99920387ab33bc301c1b0921d93ed86",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-12-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 462,
  "current_source_sequence_sha256": "42162c00b0c88b29ae0a2c6b6adef777a99920387ab33bc301c1b0921d93ed86",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 17,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A5J5T2N2",
  "selected_historical_entry_version": 17,
  "selected_historical_record_sha256": "a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633",
  "selected_historical_source_sequence_length": 462,
  "selected_historical_source_sequence_sha256": "42162c00b0c88b29ae0a2c6b6adef777a99920387ab33bc301c1b0921d93ed86",
  "selected_historical_version": {
    "accession": "A0A5J5T2N2",
    "database": "Swiss-Prot",
    "entryVersion": 17,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIR5A_GOSBA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A5J5T2N2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:28.786512+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-12-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:28.786512+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Sea Island cotton\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"malvids\",\"Malvales\",\"Malvaceae\",\"Malvoideae\",\"Gossypium\"],\"scientificName\":\"Gossypium barbadense\",\"synonyms\":[\"Hibiscus barbadensis\"],\"taxonId\":3634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:28.786512+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10027\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"2.7.11.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39488762\",\"source\":\"PubMed\"}],\"value\":\"EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5A\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39488762\",\"source\":\"PubMed\"}],\"value\":\"GbEIR5A\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:28.786512+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9ZUF4\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:25:28.786512+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:25:28.786512+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Sun L.\",\"Li X.\",\"Zhong J.\",\"Wang Y.\",\"Li B.\",\"Ye Z.\",\"Zhang J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39488762\"},{\"database\":\"DOI\",\"id\":\"10.1002/advs.202407787\"}],\"citationType\":\"journal article\",\"firstPage\":\"e2407787\",\"id\":\"39488762\",\"journal\":\"Adv. Sci.\",\"lastPage\":\"e2407787\",\"publicationDate\":\"2025\",\"title\":\"Recognition of a fungal effector potentiates pathogen-associated molecular pattern-triggered immunity in cotton.\",\"volume\":\"12\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Hai7124\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"INTERACTION WITH V.DAHLIAE EPD1\",\"INDUCTION BY V.DAHLIAE EPD1\",\"TISSUE SPECIFICITY\",\"PHOSPHORYLATION AT TYR-165 AND TYR-167\",\"MUTAGENESIS OF TYR-165; TYR-167; SER-172; SER-219; SER-225; SER-291 AND SER-421\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:28.786512+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H1",
  "excerpt": "ID   EIR5A_GOSBA             Reviewed;         462 AA.\nAC   A0A5J5T2N2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-DEC-2019, sequence version 1.\nDT   28-JAN-2026, entry version 17.\nDE   RecName: Full=EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5A {ECO:0000303|PubMed:39488762};\nDE            Short=GbEIR5A {ECO:0000303|PubMed:39488762};\nDE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};\nGN   Name=EIR5A {ECO:0000303|PubMed:39488762};\nGN   ORFNames=ES319_A13G211700v1 {ECO:0000312|EMBL:KAB2049947.1};\nOS   Gossypium barbadense (Sea Island cotton) (Hibiscus barbadensis).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; malvids; Malvales; Malvaceae; Malvoideae; Gossypium.\nOX   NCBI_TaxID=3634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:31.043989+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633",
  "url": "https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, INTERACTION WITH V.DAHLIAE EPD1, INDUCTION\nRP   BY V.DAHLIAE EPD1, TISSUE SPECIFICITY, PHOSPHORYLATION AT TYR-165 AND\nRP   TYR-167, AND MUTAGENESIS OF TYR-165; TYR-167; SER-172; SER-219; SER-225;\nRP   SER-291 AND SER-421.\nRC   STRAIN=cv. Hai7124;\nRX   PubMed=39488762; DOI=10.1002/advs.202407787;\nRA   Sun L., Li X., Zhong J., Wang Y., Li B., Ye Z., Zhang J.;\nRT   \"Recognition of a fungal effector potentiates pathogen-associated molecular\nRT   pattern-triggered immunity in cotton.\";\nRL   Adv. Sci. 12:e2407787-e2407787(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:31.043989+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633",
  "url": "https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:Q9ZUF4}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:31.043989+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633",
  "url": "https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:31.043989+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633",
  "url": "https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000124\nname: SAGA complex\nnamespace: cellular_component\nalt_id: GO:0000125\nalt_id: GO:0030914\ndef: \"A SAGA-type histone acetyltransferase complex that deubiquitinates H2A and/or H2B. This complex is organized into several functional submodules: a structural core including the activator binding module and consisting of ADA1 or a homolog, members of the SPT and TAF protein families as well as promotor recruitment factor TRRAP/TRA1, a histone acetyltransferase (HAT) module consisting of GCN5/KAT2A or PCAF/KAT2B, ADA2, ADA3/NGG1, and SGF29 or homologues thereof, a histone deubiquitinase (DUB) module consisting of ATXN7/SGF73, ATXN7L3/SGF11, ENY2/SUS1 and USP22/UBP8 or homologues thereof, and in some taxa a splicing module consisting of SF3B3 and SF3B5 or homologues thereof (not in fungi). In budding yeast also contains Spt8 which distinguishes it from SAGA-like (SLIK) complex (GO:0046695).\" [PMID:10637607, PMID:17337012, PMID:19056896, PMID:20838651, PMID:33004486]\nsynonym: \"PCAF complex\" NARROW []\nsynonym: \"PCAF histone acetylase-associated complex\" NARROW []\nsynonym: \"Spt-Ada-Gcn5-acetyltransferase complex\" EXACT []\nsynonym: \"SPT3-TAF9-GCN5 acetylase complex\" RELATED [GOC:rl, PMID:18838386]\nsynonym: \"SPT3-TAF9-PCAF acetylase complex\" NARROW [PMID:18838386]\nsynonym: \"STAGA coactivator complex\" RELATED []\nsynonym: \"STAGA complex\" RELATED [PMID:32616828, PMID:33004486, PMID:34112237]\nis_a: GO:0070461 ! SAGA-type complex\nis_a: GO:1905368 ! peptidase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000124",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1252-1268",
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
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60420-60454",
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
  "excerpt": "[Term]\nid: GO:0045202\nname: synapse\nnamespace: cellular_component\ndef: \"The junction between an axon of one neuron and a dendrite of another neuron, a muscle fiber or a glial cell. As the axon approaches the synapse it enlarges into a specialized structure, the presynaptic terminal bouton, which contains mitochondria and synaptic vesicles. At the tip of the terminal bouton is the presynaptic membrane; facing it, and separated from it by a minute cleft (the synaptic cleft) is a specialized area of membrane on the receiving cell, known as the postsynaptic membrane. In response to the arrival of nerve impulses, the presynaptic terminal bouton secretes molecules of neurotransmitters into the synaptic cleft. These diffuse across the cleft and transmit the signal to the postsynaptic membrane.\" [GOC:aruk, ISBN:0198506732, PMID:24619342, PMID:29383328, PMID:31998110]\nsubset: goslim_agr\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_synapse\nsynonym: \"electrotonic synapse\" RELATED [NIF_Subcellular:sao1311109124]\nsynonym: \"mixed synapse\" NARROW [NIF_Subcellular:sao1506103497]\nsynonym: \"synaptic junction\" EXACT []\nxref: NIF_Subcellular:sao914572699\nxref: Wikipedia:Chemical_synapse\nis_a: GO:0030054 ! cell junction\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0045202",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 262894-262912",
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
  "excerpt": "[Term]\nid: GO:0060388\nname: vitelline envelope\nnamespace: cellular_component\ndef: \"A glycoprotein-based structure that lies outside the plasma membrane and surrounds the egg before fertilization.\" [GOC:dph, ISBN:0878932437]\nsynonym: \"fertilization membrane\" RELATED []\nis_a: GO:0035805 ! egg coat\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0060388",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 347268-347275",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
