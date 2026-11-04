# GO_molecular_function_0128

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0128.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — endo-1,4-beta-xylanase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MITFSSLLVTFSAISTSLAIPGSILPKRSPMNFVLQRNESSLVRRATPNYEQDYTTGGDVIYTPSGSSFTVDWSTEDDFVVGLGWTTGSTNPINFSGTFGIGSGTALLSIYGWSENPLVEYYIVEDSASPPSFGTVKGSVTSDGSSYTIWENQRVNEPSIVGTATFNQYISVRSSPRKSGTVTVENHFQAWAALGMNLGTLNYQVLAVEGWGGEGAATQTVS

[Multiple Choices]
A. alpha-1,2-mannosyltransferase activity
B. calcium-dependent phospholipid binding
C. tubulin deacetylase activity
D. endo-1,4-beta-xylanase activity
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

> The sequence-matched record identifies the protein as an endo-1,4-beta-xylanase and gives the corresponding catalytic reaction and GO term. The annotation is supported by similarity and a computational PROSITE rule; this is not evidence of a direct activity assay on this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short sequence has an N-terminal hydrophobic signal-peptide-like region followed by a compact, enzyme-like domain, consistent with a secreted fungal polysaccharide hydrolase such as a xylanase. This meaningfully favors D over the other choices: mannosyltransferases are commonly membrane-associated, calcium-dependent phospholipid binding is not suggested by this enzyme-like sequence, and tubulin deacetylases belong to a different protein class.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of secreted fungal carbohydrate-active enzymes and the contrasting protein classes provides a credible, though not definitive, basis for choosing D without knowing this protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based enzyme-family inference distinguishes D from the offered alternatives.


### Important caveats

- The supplied sequence and family-level features support a likely function; they do not independently establish experimentally measured activity for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short sequence has an N-terminal hydrophobic signal-peptide-like region followed by a compact, enzyme-like domain, consistent with a secreted fungal polysaccharide hydrolase such as a xylanase. This meaningfully favors D over the other choices: mannosyltransferases are commonly membrane-associated, calcium-dependent phospholipid binding is not suggested by this enzyme-like sequence, and tubulin deacetylases belong to a different protein class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of secreted fungal carbohydrate-active enzymes and the contrasting protein classes provides a credible, though not definitive, basis for choosing D without knowing this protein's database annotation."
  },
  "case_id": "GO_molecular_function_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as an endo-1,4-beta-xylanase and gives the corresponding catalytic reaction and GO term. The annotation is supported by similarity and a computational PROSITE rule; this is not evidence of a direct activity assay on this exact protein."
  },
  "important_caveats": [
    "The supplied sequence and family-level features support a likely function; they do not independently establish experimentally measured activity for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based enzyme-family inference distinguishes D from the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as an endo-1,4-beta-xylanase and gives the corresponding catalytic reaction and GO term. The annotation is supported by similarity and a computational PROSITE rule; this is not evidence of a direct activity assay on this exact protein.",
    "evidence_ids": ["C4", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short sequence has an N-terminal hydrophobic signal-peptide-like region followed by a compact, enzyme-like domain, consistent with a secreted fungal polysaccharide hydrolase such as a xylanase. This meaningfully favors D over the other choices: mannosyltransferases are commonly membrane-associated, calcium-dependent phospholipid binding is not suggested by this enzyme-like sequence, and tubulin deacetylases belong to a different protein class.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of secreted fungal carbohydrate-active enzymes and the contrasting protein classes provides a credible, though not definitive, basis for choosing D without knowing this protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based enzyme-family inference distinguishes D from the offered alternatives."
  },
  "important_caveats": [
    "The supplied sequence and family-level features support a likely function; they do not independently establish experimentally measured activity for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A384K474, EIX2_BOTFB) is annotated with EC 3.2.1.8 (Endo-1,4-beta-xylanase) and GO:0031176 (endo-1,4-beta-xylanase activity). The catalytic activity is explicitly stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The EC assignment uses PROSITE-ProRule (ECO:0000255), and the function comment is supported by both similarity (ECO:0000250) and PubMed evidence (ECO:0000269, PMID:33205907). The sequence matches exactly (222 AA). The GO annotation is IEA:UniProtKB-EC, but the underlying EC assignment and functional description are well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish D from A, B, C using several transferable principles: (1) The N-terminal hydrophobic stretch (MITFSSLLVTFSAISTSLAIPG) is a classic secretion signal peptide, indicating a secreted protein. (2) The mature protein is only ~195 aa after signal cleavage. Alpha-1,2-mannosyltransferases (A) are typically 400-600+ aa membrane-bound Golgi enzymes with transmembrane anchors and DXD/HxxH motifs — incompatible with this small secreted protein. Tubulin deacetylases (C) are large cytoplasmic proteins (>300-1200 aa, e.g., HDAC6 >1200 aa) — far too large. Calcium-dependent phospholipid-binding C2 domains (B) are found in cytoplasmic proteins (synaptotagmins, PKCs), not secreted small enzymes, and have distinctive loop architectures absent here. (3) The remaining option D (endo-1,4-beta-xylanase) is the only glycoside hydrolase among the choices, and small secreted glycoside hydrolases (GH10, GH11 families) are among the most common fungal/bacterial secreted enzymes. (4) Positive features support GH11 xylanase identity: the beta-sheet-rich composition (high T, S, G, N content), the 'TTGG' motif, multiple 'GT'/'GS' loop patterns, and the conserved Glu residues in 'EDDF' near the catalytic cleft are consistent with the GH11 beta-jelly-roll fold. Fungal-type signal peptides (short, polar N-region) further support a fungal secreted hydrolase. Together, these features meaningfully eliminate A, B, C and positively support D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of alternatives A, B, C relies on well-established size, localization, and domain-architecture principles transferable across many proteins. The positive identification of D is supported by recognition of GH11-like sequence features (beta-sheet composition, GT/GS/TTGG motifs, catalytic Glu) common across the GH11 xylanase family. No fact specific to this exact protein is needed beyond general family-level knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives are mutually exclusive in terms of protein class, size, and localization. A 222-aa secreted protein with a signal peptide cannot be a membrane-bound mannosyltransferase, a C2-domain phospholipid-binding protein, or a tubulin deacetylase. Only D (a small secreted glycoside hydrolase) is compatible with the observed features.


### Important caveats

- The GO annotation for this protein is IEA (inferred from electronic annotation via EC number), not a direct experimental GO assignment, though the underlying EC assignment uses PROSITE-ProRule and the function is supported by PubMed evidence.
- Positive identification of GH11 family from sequence alone is probabilistic; a model might recognize 'small secreted glycoside hydrolase' without pinpointing the exact family, but among the four choices only D is a glycoside hydrolase, so family-level precision is not required to select D.
- The reviewer-only evidence confirms the protein is from Botrytis cinerea (a fungus), which the evaluated model would not know from the sequence alone, but the fungal-type signal peptide and GH11-like features are recognizable from the sequence itself.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish D from A, B, C using several transferable principles: (1) The N-terminal hydrophobic stretch (MITFSSLLVTFSAISTSLAIPG) is a classic secretion signal peptide, indicating a secreted protein. (2) The mature protein is only ~195 aa after signal cleavage. Alpha-1,2-mannosyltransferases (A) are typically 400-600+ aa membrane-bound Golgi enzymes with transmembrane anchors and DXD/HxxH motifs — incompatible with this small secreted protein. Tubulin deacetylases (C) are large cytoplasmic proteins (>300-1200 aa, e.g., HDAC6 >1200 aa) — far too large. Calcium-dependent phospholipid-binding C2 domains (B) are found in cytoplasmic proteins (synaptotagmins, PKCs), not secreted small enzymes, and have distinctive loop architectures absent here. (3) The remaining option D (endo-1,4-beta-xylanase) is the only glycoside hydrolase among the choices, and small secreted glycoside hydrolases (GH10, GH11 families) are among the most common fungal/bacterial secreted enzymes. (4) Positive features support GH11 xylanase identity: the beta-sheet-rich composition (high T, S, G, N content), the 'TTGG' motif, multiple 'GT'/'GS' loop patterns, and the conserved Glu residues in 'EDDF' near the catalytic cleft are consistent with the GH11 beta-jelly-roll fold. Fungal-type signal peptides (short, polar N-region) further support a fungal secreted hydrolase. Together, these features meaningfully eliminate A, B, C and positively support D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of alternatives A, B, C relies on well-established size, localization, and domain-architecture principles transferable across many proteins. The positive identification of D is supported by recognition of GH11-like sequence features (beta-sheet composition, GT/GS/TTGG motifs, catalytic Glu) common across the GH11 xylanase family. No fact specific to this exact protein is needed beyond general family-level knowledge."
  },
  "case_id": "GO_molecular_function_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384K474, EIX2_BOTFB) is annotated with EC 3.2.1.8 (Endo-1,4-beta-xylanase) and GO:0031176 (endo-1,4-beta-xylanase activity). The catalytic activity is explicitly stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The EC assignment uses PROSITE-ProRule (ECO:0000255), and the function comment is supported by both similarity (ECO:0000250) and PubMed evidence (ECO:0000269, PMID:33205907). The sequence matches exactly (222 AA). The GO annotation is IEA:UniProtKB-EC, but the underlying EC assignment and functional description are well-supported."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA (inferred from electronic annotation via EC number), not a direct experimental GO assignment, though the underlying EC assignment uses PROSITE-ProRule and the function is supported by PubMed evidence.",
    "Positive identification of GH11 family from sequence alone is probabilistic; a model might recognize 'small secreted glycoside hydrolase' without pinpointing the exact family, but among the four choices only D is a glycoside hydrolase, so family-level precision is not required to select D.",
    "The reviewer-only evidence confirms the protein is from Botrytis cinerea (a fungus), which the evaluated model would not know from the sequence alone, but the fungal-type signal peptide and GH11-like features are recognizable from the sequence itself."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are mutually exclusive in terms of protein class, size, and localization. A 222-aa secreted protein with a signal peptide cannot be a membrane-bound mannosyltransferase, a C2-domain phospholipid-binding protein, or a tubulin deacetylase. Only D (a small secreted glycoside hydrolase) is compatible with the observed features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384K474, EIX2_BOTFB) is annotated with EC 3.2.1.8 (Endo-1,4-beta-xylanase) and GO:0031176 (endo-1,4-beta-xylanase activity). The catalytic activity is explicitly stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The EC assignment uses PROSITE-ProRule (ECO:0000255), and the function comment is supported by both similarity (ECO:0000250) and PubMed evidence (ECO:0000269, PMID:33205907). The sequence matches exactly (222 AA). The GO annotation is IEA:UniProtKB-EC, but the underlying EC assignment and functional description are well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish D from A, B, C using several transferable principles: (1) The N-terminal hydrophobic stretch (MITFSSLLVTFSAISTSLAIPG) is a classic secretion signal peptide, indicating a secreted protein. (2) The mature protein is only ~195 aa after signal cleavage. Alpha-1,2-mannosyltransferases (A) are typically 400-600+ aa membrane-bound Golgi enzymes with transmembrane anchors and DXD/HxxH motifs — incompatible with this small secreted protein. Tubulin deacetylases (C) are large cytoplasmic proteins (>300-1200 aa, e.g., HDAC6 >1200 aa) — far too large. Calcium-dependent phospholipid-binding C2 domains (B) are found in cytoplasmic proteins (synaptotagmins, PKCs), not secreted small enzymes, and have distinctive loop architectures absent here. (3) The remaining option D (endo-1,4-beta-xylanase) is the only glycoside hydrolase among the choices, and small secreted glycoside hydrolases (GH10, GH11 families) are among the most common fungal/bacterial secreted enzymes. (4) Positive features support GH11 xylanase identity: the beta-sheet-rich composition (high T, S, G, N content), the 'TTGG' motif, multiple 'GT'/'GS' loop patterns, and the conserved Glu residues in 'EDDF' near the catalytic cleft are consistent with the GH11 beta-jelly-roll fold. Fungal-type signal peptides (short, polar N-region) further support a fungal secreted hydrolase. Together, these features meaningfully eliminate A, B, C and positively support D.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of alternatives A, B, C relies on well-established size, localization, and domain-architecture principles transferable across many proteins. The positive identification of D is supported by recognition of GH11-like sequence features (beta-sheet composition, GT/GS/TTGG motifs, catalytic Glu) common across the GH11 xylanase family. No fact specific to this exact protein is needed beyond general family-level knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are mutually exclusive in terms of protein class, size, and localization. A 222-aa secreted protein with a signal peptide cannot be a membrane-bound mannosyltransferase, a C2-domain phospholipid-binding protein, or a tubulin deacetylase. Only D (a small secreted glycoside hydrolase) is compatible with the observed features."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA (inferred from electronic annotation via EC number), not a direct experimental GO assignment, though the underlying EC assignment uses PROSITE-ProRule and the function is supported by PubMed evidence.",
    "Positive identification of GH11 family from sequence alone is probabilistic; a model might recognize 'small secreted glycoside hydrolase' without pinpointing the exact family, but among the four choices only D is a glycoside hydrolase, so family-level precision is not required to select D.",
    "The reviewer-only evidence confirms the protein is from Botrytis cinerea (a fungus), which the evaluated model would not know from the sequence alone, but the fungal-type signal peptide and GH11-like features are recognizable from the sequence itself."
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
  "benchmark_sequence_length": 222,
  "benchmark_sequence_sha256": "2265146ae5d59cb592dd036988cd6b2763b6251bd85f07a031b262ea02925786",
  "current_entry_audit": {
    "entryVersion": 27,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 222,
  "current_source_sequence_sha256": "2265146ae5d59cb592dd036988cd6b2763b6251bd85f07a031b262ea02925786",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 25,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384K474",
  "selected_historical_entry_version": 25,
  "selected_historical_record_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "selected_historical_source_sequence_length": 222,
  "selected_historical_source_sequence_sha256": "2265146ae5d59cb592dd036988cd6b2763b6251bd85f07a031b262ea02925786",
  "selected_historical_version": {
    "accession": "A0A384K474",
    "database": "Swiss-Prot",
    "entryVersion": 25,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX2_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384K474\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":27,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX2\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX21\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"B3VSG7\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (By similarity). May act as an elicitor of plant defense responses in certain plants but does not exhibit any cell death when transiently expressed in N.benthamiana (PubMed:33205907)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031176\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:endo-1,4-beta-xylanase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-EC\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H1",
  "excerpt": "ID   EIX2_BOTFB              Reviewed;         222 AA.\nAC   A0A384K474;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 25.\nDE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX21 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX2 {ECO:0000303|PubMed:33205907}; ORFNames=BCIN_15g01600;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a\nCC       major structural heterogeneous polysaccharide found in plant biomass\nCC       representing the second most abundant polysaccharide in the biosphere,\nCC       after cellulose (By similarity). May act as an elicitor of plant\nCC       defense responses in certain plants but does not exhibit any cell death\nCC       when transiently expressed in N.benthamiana (PubMed:33205907).\nCC       {ECO:0000250|UniProtKB:B3VSG7, ECO:0000269|PubMed:33205907}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0031176; F:endo-1,4-beta-xylanase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000026\nname: alpha-1,2-mannosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a mannose residue to an oligosaccharide, forming an alpha-(1->2) linkage.\" [GOC:mcc, PMID:10521541]\nxref: Reactome:R-HSA-446187 \"ALG11 transfers the fourth and fifth Man to the N-glycan precursor\"\nxref: Reactome:R-HSA-446215 \"ALG9 transfers Man to N-glycan precursor (GlcNAc)2 (Man)6 (PP-Dol)1\"\nxref: Reactome:R-HSA-446216 \"ALG9 transfers Man to N-glycan precursor (GlcNAc)2 (Man)8 (PP-Dol)1\"\nxref: Reactome:R-HSA-4551297 \"Defective ALG11 does not transfer Man to the N-glycan precursor\"\nxref: Reactome:R-HSA-4720478 \"Defective ALG9 does not add the seventh mannose to the N-glycan precursor\"\nxref: Reactome:R-HSA-9035514 \"Defective ALG9 does not add the last mannose to the N-glycan precursor\"\nis_a: GO:0000030 ! mannosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000026",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 282-294",
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
  "excerpt": "[Term]\nid: GO:0005544\nname: calcium-dependent phospholipid binding\nnamespace: molecular_function\ndef: \"Binding to a phospholipid, a class of lipids containing phosphoric acid as a mono- or diester, in the presence of calcium.\" [GOC:jl]\nis_a: GO:0005543 ! phospholipid binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005544",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 57197-57203",
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
  "excerpt": "[Term]\nid: GO:0031176\nname: endo-1,4-beta-xylanase activity\nnamespace: molecular_function\ndef: \"Catalysis of the endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\" [EC:3.2.1.8]\nsynonym: \"1,4-beta-D-xylan xylanohydrolase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"1,4-beta-xylan xylanohydrolase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"beta-1,4-xylan xylanohydrolase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"beta-1,4-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"beta-D-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"beta-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"endo-(1,4)-beta-xylanase(1,4)-beta-xylan 4-xylanohydrolase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"endo-(1->4)-beta-xylanase(1->4)-beta-xylan 4-xylanohydrolase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"endo-1,4-beta-D-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"endo-1,4-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"endo-beta-1,4-xylanase activity\" RELATED [EC:3.2.1.8]\nsynonym: \"xylanase\" BROAD [EC:3.2.1.8]\nxref: EC:3.2.1.8\nxref: MetaCyc:3.2.1.8-RXN\nis_a: GO:0097599 ! xylanase activity\nproperty_value: skos:exactMatch EC:3.2.1.8\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031176",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 173997-174018",
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
  "excerpt": "[Term]\nid: GO:0042903\nname: tubulin deacetylase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: N-acetyl(alpha-tubulin) + H2O = alpha-tubulin + acetate.\" [PMID:12024216, PMID:12486003]\nxref: Reactome:R-HSA-5618331 \"HDAC6 deacetylates microtubules\"\nis_a: GO:0016811 ! hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds, in linear amides\nis_a: GO:0033558 ! protein lysine deacetylase activity\nproperty_value: skos:broadMatch EC:3.5.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042903",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 242076-242085",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
