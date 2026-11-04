# GO_cellular_component_0012

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0012.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **A** — phosphopantothenoylcysteine decarboxylase complex

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGSEPVSAEGESMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSSSGSLHFIDRASMPKDVILYTDEDEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWNNPFTERHFISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGRAVVTLR

[Multiple Choices]
A. phosphopantothenoylcysteine decarboxylase complex
B. cell tip
C. mannosyltransferase complex
D. nuclear pore
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

> The matched sequence has a phosphopantothenoylcysteine decarboxylase complex annotation (IBA, phylogenetic inference), so choice A is scientifically supported. This is not direct experimental evidence that the complex is the protein's exclusive or primary location; the record also reports nucleus and cell-membrane localization.

Citations as saved: [H4](#evidence-h4), [H2](#evidence-h2), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 214-aa sequence is consistent with the compact PPCDC/HAL3 enzyme family; transferable recognition of that family from homologous sequences links it to the PPCDC complex, the specifically offered option A. The other options describe a mannosyltransferase complex, a cell-tip region, or a nuclear pore, none of which fits that enzyme-family inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and the known association of eukaryotic PPCDC proteins with a PPCDC complex provide a meaningful distinction among these choices without needing the exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein has other reported localizations and 'primary' is not defined, those do not make the other offered terms equivalent to the specifically supported PPCDC-complex annotation; nucleus alone, for example, does not imply nuclear pore.


### Important caveats

- The complex annotation is IBA and therefore computationally inferred, not direct experimental proof of complex membership or exclusive localization.
- The source also reports nucleus and cell-membrane localization, so the question's wording about a single primary component simplifies a potentially multi-localized protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 214-aa sequence is consistent with the compact PPCDC/HAL3 enzyme family; transferable recognition of that family from homologous sequences links it to the PPCDC complex, the specifically offered option A. The other options describe a mannosyltransferase complex, a cell-tip region, or a nuclear pore, none of which fits that enzyme-family inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the known association of eukaryotic PPCDC proteins with a PPCDC complex provide a meaningful distinction among these choices without needing the exact protein's database entry."
  },
  "case_id": "GO_cellular_component_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H2",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a phosphopantothenoylcysteine decarboxylase complex annotation (IBA, phylogenetic inference), so choice A is scientifically supported. This is not direct experimental evidence that the complex is the protein's exclusive or primary location; the record also reports nucleus and cell-membrane localization."
  },
  "important_caveats": [
    "The complex annotation is IBA and therefore computationally inferred, not direct experimental proof of complex membership or exclusive localization.",
    "The source also reports nucleus and cell-membrane localization, so the question's wording about a single primary component simplifies a potentially multi-localized protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has other reported localizations and 'primary' is not defined, those do not make the other offered terms equivalent to the specifically supported PPCDC-complex annotation; nucleus alone, for example, does not imply nuclear pore."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a phosphopantothenoylcysteine decarboxylase complex annotation (IBA, phylogenetic inference), so choice A is scientifically supported. This is not direct experimental evidence that the complex is the protein's exclusive or primary location; the record also reports nucleus and cell-membrane localization.",
    "evidence_ids": ["H4", "H2", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 214-aa sequence is consistent with the compact PPCDC/HAL3 enzyme family; transferable recognition of that family from homologous sequences links it to the PPCDC complex, the specifically offered option A. The other options describe a mannosyltransferase complex, a cell-tip region, or a nuclear pore, none of which fits that enzyme-family inference.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the known association of eukaryotic PPCDC proteins with a PPCDC complex provide a meaningful distinction among these choices without needing the exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has other reported localizations and 'primary' is not defined, those do not make the other offered terms equivalent to the specifically supported PPCDC-complex annotation; nucleus alone, for example, does not imply nuclear pore."
  },
  "important_caveats": [
    "The complex annotation is IBA and therefore computationally inferred, not direct experimental proof of complex membership or exclusive localization.",
    "The source also reports nucleus and cell-membrane localization, so the question's wording about a single primary component simplifies a potentially multi-localized protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (C6TA59, HAL3b from Glycine max) carries the GO annotation GO:0071513 'phosphopantothenoylcysteine decarboxylase complex' with evidence code IBA:GO_Central (evidence C7/H4). The protein is annotated as Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36), and PPCDC is known to form a homotrimeric complex in eukaryotes (per GO term definition, evidence GO4). However, the strongest experimental evidence (IDA) for this protein's localization is nucleus and plasma membrane (evidence C5/C6/C8, H2/H3/H5), neither of which appears among the choices. The expected answer A is supported by the GO annotation, but the supporting evidence code is computational inference (IBA), not experimental (IDA). The annotation is present and matches the option text exactly.

Citations as saved: [C4](#evidence-c4), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish A from B, C, D through a combination of family recognition and elimination. (1) The sequence is 214 amino acids, consistent with the PPCDC/HAL3 enzyme family (~200–250 AA), and contains motifs (e.g., 'LCHCFSEW', 'GDSVLHIELRKWADIM') characteristic of the HAL3/PPCDC superfamily involved in CoA biosynthesis. PPCDC is well known to function as a homotrimeric complex in eukaryotes, directly supporting the 'complex' GO term. (2) Nuclear pore proteins (D) are typically hundreds to thousands of residues long and contain FG-repeat domains; a 214-AA protein without FG repeats is inconsistent with the nuclear pore. (3) Mannosyltransferase complexes (C) reside in the Golgi and involve transferase-specific motifs; nothing in this sequence resembles a glycosyltransferase fold or Golgi-retention signal. (4) Cell tip (B) is a highly specific localization for growth/polarity proteins (e.g., in fungi or root hairs); no targeting motifs for cell-tip accumulation are present. The process of elimination combined with PPCDC family recognition meaningfully distinguishes A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PPCDC/HAL3 family is well characterized in biochemistry (third step of CoA biosynthesis, EC 4.1.1.36). A model familiar with this family can recognize the ~214-AA length and catalytic motifs. Even without precise family recall, the other three options are strongly inconsistent with a small 214-AA enzyme lacking FG repeats, transferase motifs, or growth-polarity targeting signals. The combination of positive family-level inference and elimination of clearly mismatched alternatives provides a credible transferable reasoning path.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (B: cell tip, C: mannosyltransferase complex, D: nuclear pore) are each strongly inconsistent with a 214-AA soluble enzyme bearing PPCDC-family motifs. Nuclear pore proteins are far larger with FG repeats; mannosyltransferase complexes involve Golgi-localized transferases; cell tip is for polarity/growth proteins. No alternative among the offered choices is defensible for this sequence.


### Important caveats

- The GO annotation supporting choice A uses evidence code IBA (Inferred by Biological Aspect), a computational inference, not experimental data. The experimental (IDA) evidence for this protein points to nucleus and plasma membrane, neither of which is offered as a choice.
- The protein's actual experimental subcellular locations (nucleus, plasma membrane) are not among the options, so the question forces selection of the only annotated complex term despite the stronger experimental evidence pointing elsewhere.
- The GO term definition (GO4) states the PPCDC complex is 'part_of cytoplasm,' yet the protein's experimental localization is nucleus and membrane, creating a mild tension between the complex annotation and the protein's observed locations.
- The source is Glycine max (soybean), a plant; PPCDC complex annotation via IBA:GO_Central is propagated from other organisms and may not reflect the plant-specific complex architecture.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish A from B, C, D through a combination of family recognition and elimination. (1) The sequence is 214 amino acids, consistent with the PPCDC/HAL3 enzyme family (~200–250 AA), and contains motifs (e.g., 'LCHCFSEW', 'GDSVLHIELRKWADIM') characteristic of the HAL3/PPCDC superfamily involved in CoA biosynthesis. PPCDC is well known to function as a homotrimeric complex in eukaryotes, directly supporting the 'complex' GO term. (2) Nuclear pore proteins (D) are typically hundreds to thousands of residues long and contain FG-repeat domains; a 214-AA protein without FG repeats is inconsistent with the nuclear pore. (3) Mannosyltransferase complexes (C) reside in the Golgi and involve transferase-specific motifs; nothing in this sequence resembles a glycosyltransferase fold or Golgi-retention signal. (4) Cell tip (B) is a highly specific localization for growth/polarity proteins (e.g., in fungi or root hairs); no targeting motifs for cell-tip accumulation are present. The process of elimination combined with PPCDC family recognition meaningfully distinguishes A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PPCDC/HAL3 family is well characterized in biochemistry (third step of CoA biosynthesis, EC 4.1.1.36). A model familiar with this family can recognize the ~214-AA length and catalytic motifs. Even without precise family recall, the other three options are strongly inconsistent with a small 214-AA enzyme lacking FG repeats, transferase motifs, or growth-polarity targeting signals. The combination of positive family-level inference and elimination of clearly mismatched alternatives provides a credible transferable reasoning path."
  },
  "case_id": "GO_cellular_component_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C7",
      "H1",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (C6TA59, HAL3b from Glycine max) carries the GO annotation GO:0071513 'phosphopantothenoylcysteine decarboxylase complex' with evidence code IBA:GO_Central (evidence C7/H4). The protein is annotated as Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36), and PPCDC is known to form a homotrimeric complex in eukaryotes (per GO term definition, evidence GO4). However, the strongest experimental evidence (IDA) for this protein's localization is nucleus and plasma membrane (evidence C5/C6/C8, H2/H3/H5), neither of which appears among the choices. The expected answer A is supported by the GO annotation, but the supporting evidence code is computational inference (IBA), not experimental (IDA). The annotation is present and matches the option text exactly."
  },
  "important_caveats": [
    "The GO annotation supporting choice A uses evidence code IBA (Inferred by Biological Aspect), a computational inference, not experimental data. The experimental (IDA) evidence for this protein points to nucleus and plasma membrane, neither of which is offered as a choice.",
    "The protein's actual experimental subcellular locations (nucleus, plasma membrane) are not among the options, so the question forces selection of the only annotated complex term despite the stronger experimental evidence pointing elsewhere.",
    "The GO term definition (GO4) states the PPCDC complex is 'part_of cytoplasm,' yet the protein's experimental localization is nucleus and membrane, creating a mild tension between the complex annotation and the protein's observed locations.",
    "The source is Glycine max (soybean), a plant; PPCDC complex annotation via IBA:GO_Central is propagated from other organisms and may not reflect the plant-specific complex architecture."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (B: cell tip, C: mannosyltransferase complex, D: nuclear pore) are each strongly inconsistent with a 214-AA soluble enzyme bearing PPCDC-family motifs. Nuclear pore proteins are far larger with FG repeats; mannosyltransferase complexes involve Golgi-localized transferases; cell tip is for polarity/growth proteins. No alternative among the offered choices is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (C6TA59, HAL3b from Glycine max) carries the GO annotation GO:0071513 'phosphopantothenoylcysteine decarboxylase complex' with evidence code IBA:GO_Central (evidence C7/H4). The protein is annotated as Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36), and PPCDC is known to form a homotrimeric complex in eukaryotes (per GO term definition, evidence GO4). However, the strongest experimental evidence (IDA) for this protein's localization is nucleus and plasma membrane (evidence C5/C6/C8, H2/H3/H5), neither of which appears among the choices. The expected answer A is supported by the GO annotation, but the supporting evidence code is computational inference (IBA), not experimental (IDA). The annotation is present and matches the option text exactly.",
    "evidence_ids": ["C4", "C7", "H1", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish A from B, C, D through a combination of family recognition and elimination. (1) The sequence is 214 amino acids, consistent with the PPCDC/HAL3 enzyme family (~200–250 AA), and contains motifs (e.g., 'LCHCFSEW', 'GDSVLHIELRKWADIM') characteristic of the HAL3/PPCDC superfamily involved in CoA biosynthesis. PPCDC is well known to function as a homotrimeric complex in eukaryotes, directly supporting the 'complex' GO term. (2) Nuclear pore proteins (D) are typically hundreds to thousands of residues long and contain FG-repeat domains; a 214-AA protein without FG repeats is inconsistent with the nuclear pore. (3) Mannosyltransferase complexes (C) reside in the Golgi and involve transferase-specific motifs; nothing in this sequence resembles a glycosyltransferase fold or Golgi-retention signal. (4) Cell tip (B) is a highly specific localization for growth/polarity proteins (e.g., in fungi or root hairs); no targeting motifs for cell-tip accumulation are present. The process of elimination combined with PPCDC family recognition meaningfully distinguishes A.",
    "missing_item_specific_fact": "",
    "reason": "The PPCDC/HAL3 family is well characterized in biochemistry (third step of CoA biosynthesis, EC 4.1.1.36). A model familiar with this family can recognize the ~214-AA length and catalytic motifs. Even without precise family recall, the other three options are strongly inconsistent with a small 214-AA enzyme lacking FG repeats, transferase motifs, or growth-polarity targeting signals. The combination of positive family-level inference and elimination of clearly mismatched alternatives provides a credible transferable reasoning path."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (B: cell tip, C: mannosyltransferase complex, D: nuclear pore) are each strongly inconsistent with a 214-AA soluble enzyme bearing PPCDC-family motifs. Nuclear pore proteins are far larger with FG repeats; mannosyltransferase complexes involve Golgi-localized transferases; cell tip is for polarity/growth proteins. No alternative among the offered choices is defensible for this sequence."
  },
  "important_caveats": [
    "The GO annotation supporting choice A uses evidence code IBA (Inferred by Biological Aspect), a computational inference, not experimental data. The experimental (IDA) evidence for this protein points to nucleus and plasma membrane, neither of which is offered as a choice.",
    "The protein's actual experimental subcellular locations (nucleus, plasma membrane) are not among the options, so the question forces selection of the only annotated complex term despite the stronger experimental evidence pointing elsewhere.",
    "The GO term definition (GO4) states the PPCDC complex is 'part_of cytoplasm,' yet the protein's experimental localization is nucleus and membrane, creating a mild tension between the complex annotation and the protein's observed locations.",
    "The source is Glycine max (soybean), a plant; PPCDC complex annotation via IBA:GO_Central is propagated from other organisms and may not reflect the plant-specific complex architecture."
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
  "benchmark_sequence_length": 214,
  "benchmark_sequence_sha256": "dcaceed6f1d468598241beac0d585a8eb9ed9cdd0b98d0e7be38e1ae1801b687",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 214,
  "current_source_sequence_sha256": "dcaceed6f1d468598241beac0d585a8eb9ed9cdd0b98d0e7be38e1ae1801b687",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 84,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C6TA59",
  "selected_historical_entry_version": 84,
  "selected_historical_record_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "selected_historical_source_sequence_length": 214,
  "selected_historical_source_sequence_sha256": "dcaceed6f1d468598241beac0d585a8eb9ed9cdd0b98d0e7be38e1ae1801b687",
  "selected_historical_version": {
    "accession": "C6TA59",
    "database": "Swiss-Prot",
    "entryVersion": 84,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HAL3B_SOYBN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C6TA59\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soybean\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Fabales\",\"Fabaceae\",\"Papilionoideae\",\"50 kb inversion clade\",\"NPAAA clade\",\"indigoferoid/millettioid clade\",\"Phaseoleae\",\"Glycine\",\"Glycine subgen. Soja\"],\"scientificName\":\"Glycine max\",\"synonyms\":[\"Glycine hispida\"],\"taxonId\":3847}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"Halotolerance protein 3b\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"GmHAL3b\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"4.1.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Phosphopantothenoylcysteine decarboxylase HAL3b\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PPCDC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"id\":\"SL-0191\",\"value\":\"Nucleus\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005634\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleus\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/24",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0071513\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:phosphopantothenoylcysteine decarboxylase complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/25",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/26",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H1",
  "excerpt": "ID   HAL3B_SOYBN             Reviewed;         214 AA.\nAC   C6TA59;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 84.\nDE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3b {ECO:0000305};\nDE            Short=PPCDC {ECO:0000305};\nDE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};\nDE   AltName: Full=Halotolerance protein 3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nDE            Short=GmHAL3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   Name=HAL3B {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   OrderedLocusNames=Glyma07g082800 {ECO:0000312|EMBL:KRH48322.1};\nOS   Glycine max (Soybean) (Glycine hispida).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;\nOC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;\nOC   Glycine subgen. Soja.\nOX   NCBI_TaxID=3847;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H2",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|Ref.4}. Nucleus\nCC       {ECO:0000269|Ref.4}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0005634; C:nucleus; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0071513; C:phosphopantothenoylcysteine decarboxylase complex; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005643\nname: nuclear pore\nnamespace: cellular_component\nalt_id: GO:0005644\ndef: \"A protein complex providing a discrete opening in the nuclear envelope of a eukaryotic cell, where the inner and outer nuclear membranes are joined.\" [ISBN:0198547684]\nsubset: goslim_pir\nsynonym: \"NPC\" EXACT []\nsynonym: \"nuclear pore complex\" EXACT []\nsynonym: \"nuclear pore membrane protein\" NARROW []\nsynonym: \"nucleopore\" EXACT [GOC:al, PMID:7603572]\nxref: NIF_Subcellular:sao220861693\nxref: Wikipedia:Nuclear_pore\nis_a: GO:0140513 ! nuclear protein-containing complex\nrelationship: part_of GO:0005635 ! nuclear envelope\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005643",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58104-58119",
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
  "excerpt": "[Term]\nid: GO:0031501\nname: mannosyltransferase complex\nnamespace: cellular_component\ndef: \"A complex that possesses mannosyltransferase activity.\" [GOC:mah]\nsubset: goslim_pir\nis_a: GO:0140535 ! intracellular protein-containing complex\nis_a: GO:1990234 ! transferase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031501",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 177124-177132",
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
  "excerpt": "[Term]\nid: GO:0051286\nname: cell tip\nnamespace: cellular_component\ndef: \"The region at the end of the longest axis of a cylindrical or elongated cell.\" [GOC:ai, GOC:mah]\ncomment: Note that this term differs from 'cell pole ; GO:0060187' in that it is applicable to the thin ends of elongated cells, such as the ends of axons or dendrites.\nsynonym: \"cell end\" EXACT [GOC:mah]\nis_a: GO:0060187 ! cell pole\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051286",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 325114-325122",
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
  "excerpt": "[Term]\nid: GO:0071513\nname: phosphopantothenoylcysteine decarboxylase complex\nnamespace: cellular_component\ndef: \"A protein complex that catalyzes decarboxylation of 4'-phosphopantothenoylcysteine to yield 4'-phosphopantetheine; this is the third step in the biosynthesis of Coenzyme A. The complex is homotrimeric in many eukaryotes, but is a heterotrimer in Saccharomyces.\" [GOC:jh, PMID:19915539]\ncomment: See also the molecular function term 'acetolactate synthase activity ; GO:0003984'.\nis_a: GO:1902494 ! catalytic complex\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0071513",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 377848-377856",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
