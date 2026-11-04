# cofactor_0173

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0173.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — a divalent metal cation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSIIGSFPPGGPRVEVQETRVQTDRVLTIPNILSMARLAGVPLFLWLILRPEFGGPQSDGWALLVLALSGVSDYLDGKLARRWNQISSLGRLLDPAADRLYILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRRHGYPPPQVNFLGKAATFNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD

[Multiple Choices]
A. cob(II)alamin
B. [2Fe-2S] cluster
C. a divalent metal cation
D. Fe cation
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation reports a divalent metal cation as the cofactor, with experimental evidence cited from a publication. It notes highest activity with Co(2+) and lower activity with Mn(2+), supporting choice C.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a short, strongly hydrophobic multipass membrane protein, consistent with a membrane lipid-synthesis enzyme rather than a soluble cobalamin- or Fe-S-binding enzyme. Transferable knowledge that lipid-phosphate transfer reactions commonly use divalent cations to support catalysis favors the broad divalent-metal choice over a specific iron cofactor; the sequence does not show an obvious iron-specific binding feature.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and choices support a meaningful family-level, probabilistic inference for a divalent metal. They do not independently establish which divalent ion gives the greatest activity, so the precise Co/Mn profile remains target-specific.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports a divalent-metal cofactor and identifies Co(2+) and Mn(2+) as supporting activity; it does not identify Fe as the cofactor.


### Important caveats

- The reviewer-only, sequence-matched annotation cites experimental evidence, but the primary study was not independently reviewed here.
- The sequence architecture alone does not prove the enzyme family or its metal dependence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a short, strongly hydrophobic multipass membrane protein, consistent with a membrane lipid-synthesis enzyme rather than a soluble cobalamin- or Fe-S-binding enzyme. Transferable knowledge that lipid-phosphate transfer reactions commonly use divalent cations to support catalysis favors the broad divalent-metal choice over a specific iron cofactor; the sequence does not show an obvious iron-specific binding feature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices support a meaningful family-level, probabilistic inference for a divalent metal. They do not independently establish which divalent ion gives the greatest activity, so the precise Co/Mn profile remains target-specific."
  },
  "case_id": "cofactor_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports a divalent metal cation as the cofactor, with experimental evidence cited from a publication. It notes highest activity with Co(2+) and lower activity with Mn(2+), supporting choice C."
  },
  "important_caveats": [
    "The reviewer-only, sequence-matched annotation cites experimental evidence, but the primary study was not independently reviewed here.",
    "The sequence architecture alone does not prove the enzyme family or its metal dependence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports a divalent-metal cofactor and identifies Co(2+) and Mn(2+) as supporting activity; it does not identify Fe as the cofactor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports a divalent metal cation as the cofactor, with experimental evidence cited from a publication. It notes highest activity with Co(2+) and lower activity with Mn(2+), supporting choice C.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a short, strongly hydrophobic multipass membrane protein, consistent with a membrane lipid-synthesis enzyme rather than a soluble cobalamin- or Fe-S-binding enzyme. Transferable knowledge that lipid-phosphate transfer reactions commonly use divalent cations to support catalysis favors the broad divalent-metal choice over a specific iron cofactor; the sequence does not show an obvious iron-specific binding feature.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices support a meaningful family-level, probabilistic inference for a divalent metal. They do not independently establish which divalent ion gives the greatest activity, so the precise Co/Mn profile remains target-specific."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports a divalent-metal cofactor and identifies Co(2+) and Mn(2+) as supporting activity; it does not identify Fe as the cofactor."
  },
  "important_caveats": [
    "The reviewer-only, sequence-matched annotation cites experimental evidence, but the primary study was not independently reviewed here.",
    "The sequence architecture alone does not prove the enzyme family or its metal dependence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, EC 2.7.8.41, Streptomyces coelicolor) explicitly annotates the cofactor as 'a divalent metal cation' (ChEBI:CHEBI:60240) with experimental evidence (ECO:0000269, PubMed:19439403). The note specifies highest activity with Co(2+), lower with Mn(2+), and no activity with Ni(2+), Ca(2+), or Mg(2+). The sequence matches exactly (215 aa, SHA-256 confirmed). The author key 'a divalent metal cation' is directly and experimentally supported.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two conserved 'DD' (aspartate-aspartate) motifs: one in 'LDPAADRLYIL' (~residues 89-90) and one at the C-terminus 'ADVAAD' (~residues 213-214). These DD motifs are the hallmark of the CDP-alcohol phosphatidyltransferase superfamily (PF01126), which includes CDP-diacylglycerol synthase, phosphatidylserine synthase, phosphatidylethanolamine synthase, and cardiolipin synthase. Family-level knowledge established across many characterized members (e.g., E. coli CdsA, yeast CDS1, human CRLS1) is that these enzymes coordinate a divalent metal cation (typically Mg2+ or Mn2+) via the DD pair to activate the phosphate group for nucleophilic attack. This distinguishes option C from the alternatives: (A) cob(II)alamin requires a B12-binding domain with conserved 'DXHXX' and 'HXXXH' motifs and a characteristic α/β fold, absent here; (B) a &#91;2Fe-2S&#93; cluster requires a cysteine-rich motif (e.g., C-X2-C-X2-C-X2-C), which this hydrophobic membrane sequence lacks; (D) a specific Fe cation as a prosthetic group is characteristic of oxidoreductases or certain hydrolases, not the phosphatidyltransferase mechanism. The overall architecture—multiple TM helices, ~215 aa, DD motifs—is consistent with a membrane-bound phosphatidyltransferase requiring a divalent metal cation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DD motifs are directly observable in the supplied sequence and are a well-characterized family-level signature of the phosphatidyltransferase superfamily. The divalent metal cation requirement is a transferable property learned from multiple characterized members of this family. The absence of B12-binding motifs, Fe-S cluster cysteine motifs, and iron-prosthetic-group features further excludes options A, B, and D. This constitutes a concrete, family-level inference from the sequence to the correct choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mechanistically distinct cofactor classes (organometallic B12, iron-sulfur cluster, general divalent cation, specific iron cation). The DD motifs and phosphatidyltransferase family context clearly point to a divalent metal cation and exclude the other three. No ambiguity among the offered choices is identified.


### Important caveats

- The specific divalent cation preference (Co2+ > Mn2+, with no activity for Mg2+) is a protein-specific experimental finding not derivable from family-level knowledge alone, but the question only asks for the general class 'a divalent metal cation,' which is the family-level property.
- The sequence is highly hydrophobic and could superficially resemble other membrane proteins; recognition of the DD motifs as phosphatidyltransferase signatures requires familiarity with this superfamily.
- Option D ('Fe cation') could in principle overlap with 'divalent metal cation' if Fe2+ were considered, but in standard biochemical cofactor classification these are treated as distinct categories (specific prosthetic-group iron vs. general divalent cation activator).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two conserved 'DD' (aspartate-aspartate) motifs: one in 'LDPAADRLYIL' (~residues 89-90) and one at the C-terminus 'ADVAAD' (~residues 213-214). These DD motifs are the hallmark of the CDP-alcohol phosphatidyltransferase superfamily (PF01126), which includes CDP-diacylglycerol synthase, phosphatidylserine synthase, phosphatidylethanolamine synthase, and cardiolipin synthase. Family-level knowledge established across many characterized members (e.g., E. coli CdsA, yeast CDS1, human CRLS1) is that these enzymes coordinate a divalent metal cation (typically Mg2+ or Mn2+) via the DD pair to activate the phosphate group for nucleophilic attack. This distinguishes option C from the alternatives: (A) cob(II)alamin requires a B12-binding domain with conserved 'DXHXX' and 'HXXXH' motifs and a characteristic α/β fold, absent here; (B) a [2Fe-2S] cluster requires a cysteine-rich motif (e.g., C-X2-C-X2-C-X2-C), which this hydrophobic membrane sequence lacks; (D) a specific Fe cation as a prosthetic group is characteristic of oxidoreductases or certain hydrolases, not the phosphatidyltransferase mechanism. The overall architecture—multiple TM helices, ~215 aa, DD motifs—is consistent with a membrane-bound phosphatidyltransferase requiring a divalent metal cation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DD motifs are directly observable in the supplied sequence and are a well-characterized family-level signature of the phosphatidyltransferase superfamily. The divalent metal cation requirement is a transferable property learned from multiple characterized members of this family. The absence of B12-binding motifs, Fe-S cluster cysteine motifs, and iron-prosthetic-group features further excludes options A, B, and D. This constitutes a concrete, family-level inference from the sequence to the correct choice."
  },
  "case_id": "cofactor_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, EC 2.7.8.41, Streptomyces coelicolor) explicitly annotates the cofactor as 'a divalent metal cation' (ChEBI:CHEBI:60240) with experimental evidence (ECO:0000269, PubMed:19439403). The note specifies highest activity with Co(2+), lower with Mn(2+), and no activity with Ni(2+), Ca(2+), or Mg(2+). The sequence matches exactly (215 aa, SHA-256 confirmed). The author key 'a divalent metal cation' is directly and experimentally supported."
  },
  "important_caveats": [
    "The specific divalent cation preference (Co2+ > Mn2+, with no activity for Mg2+) is a protein-specific experimental finding not derivable from family-level knowledge alone, but the question only asks for the general class 'a divalent metal cation,' which is the family-level property.",
    "The sequence is highly hydrophobic and could superficially resemble other membrane proteins; recognition of the DD motifs as phosphatidyltransferase signatures requires familiarity with this superfamily.",
    "Option D ('Fe cation') could in principle overlap with 'divalent metal cation' if Fe2+ were considered, but in standard biochemical cofactor classification these are treated as distinct categories (specific prosthetic-group iron vs. general divalent cation activator)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct cofactor classes (organometallic B12, iron-sulfur cluster, general divalent cation, specific iron cation). The DD motifs and phosphatidyltransferase family context clearly point to a divalent metal cation and exclude the other three. No ambiguity among the offered choices is identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, EC 2.7.8.41, Streptomyces coelicolor) explicitly annotates the cofactor as 'a divalent metal cation' (ChEBI:CHEBI:60240) with experimental evidence (ECO:0000269, PubMed:19439403). The note specifies highest activity with Co(2+), lower with Mn(2+), and no activity with Ni(2+), Ca(2+), or Mg(2+). The sequence matches exactly (215 aa, SHA-256 confirmed). The author key 'a divalent metal cation' is directly and experimentally supported.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two conserved 'DD' (aspartate-aspartate) motifs: one in 'LDPAADRLYIL' (~residues 89-90) and one at the C-terminus 'ADVAAD' (~residues 213-214). These DD motifs are the hallmark of the CDP-alcohol phosphatidyltransferase superfamily (PF01126), which includes CDP-diacylglycerol synthase, phosphatidylserine synthase, phosphatidylethanolamine synthase, and cardiolipin synthase. Family-level knowledge established across many characterized members (e.g., E. coli CdsA, yeast CDS1, human CRLS1) is that these enzymes coordinate a divalent metal cation (typically Mg2+ or Mn2+) via the DD pair to activate the phosphate group for nucleophilic attack. This distinguishes option C from the alternatives: (A) cob(II)alamin requires a B12-binding domain with conserved 'DXHXX' and 'HXXXH' motifs and a characteristic α/β fold, absent here; (B) a [2Fe-2S] cluster requires a cysteine-rich motif (e.g., C-X2-C-X2-C-X2-C), which this hydrophobic membrane sequence lacks; (D) a specific Fe cation as a prosthetic group is characteristic of oxidoreductases or certain hydrolases, not the phosphatidyltransferase mechanism. The overall architecture—multiple TM helices, ~215 aa, DD motifs—is consistent with a membrane-bound phosphatidyltransferase requiring a divalent metal cation.",
    "missing_item_specific_fact": "",
    "reason": "The DD motifs are directly observable in the supplied sequence and are a well-characterized family-level signature of the phosphatidyltransferase superfamily. The divalent metal cation requirement is a transferable property learned from multiple characterized members of this family. The absence of B12-binding motifs, Fe-S cluster cysteine motifs, and iron-prosthetic-group features further excludes options A, B, and D. This constitutes a concrete, family-level inference from the sequence to the correct choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct cofactor classes (organometallic B12, iron-sulfur cluster, general divalent cation, specific iron cation). The DD motifs and phosphatidyltransferase family context clearly point to a divalent metal cation and exclude the other three. No ambiguity among the offered choices is identified."
  },
  "important_caveats": [
    "The specific divalent cation preference (Co2+ > Mn2+, with no activity for Mg2+) is a protein-specific experimental finding not derivable from family-level knowledge alone, but the question only asks for the general class 'a divalent metal cation,' which is the family-level property.",
    "The sequence is highly hydrophobic and could superficially resemble other membrane proteins; recognition of the DD motifs as phosphatidyltransferase signatures requires familiarity with this superfamily.",
    "Option D ('Fe cation') could in principle overlap with 'divalent metal cation' if Fe2+ were considered, but in standard biochemical cofactor classification these are treated as distinct categories (specific prosthetic-group iron vs. general divalent cation activator)."
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
  "benchmark_sequence_length": 215,
  "benchmark_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "current_entry_audit": {
    "entryVersion": 120,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 215,
  "current_source_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 118,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9KZP3",
  "selected_historical_entry_version": 118,
  "selected_historical_record_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "selected_historical_source_sequence_length": 215,
  "selected_historical_source_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "selected_historical_version": {
    "accession": "Q9KZP3",
    "database": "Swiss-Prot",
    "entryVersion": 118,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRLS1_STRCO",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9KZP3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":120,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001973\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\",\"Streptomyces albidoflavus group\"],\"scientificName\":\"Streptomyces coelicolor (strain ATCC BAA-471 / A3(2) / M145)\",\"taxonId\":100226}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19439403\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.41\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthase (CMP-forming)\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"CLS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:60240\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19439403\",\"source\":\"PubMed\"}],\"name\":\"a divalent metal cation\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19439403\",\"source\":\"PubMed\"}],\"value\":\"Highest activity found with Co(2+) whereas Mn(2+) supports a lower activity; no activity detected with Ni(2+), Ca(2+) or Mg(2+).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Sandoval-Calderon M.\",\"Geiger O.\",\"Guan Z.\",\"Barona-Gomez F.\",\"Sohlenkamp C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19439403\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.006072\"}],\"citationType\":\"journal article\",\"firstPage\":\"17383\",\"id\":\"19439403\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"17390\",\"publicationDate\":\"2009\",\"title\":\"A eukaryote-like cardiolipin synthase is present in Streptomyces coelicolor and in most actinobacteria.\",\"volume\":\"284\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H1",
  "excerpt": "ID   CRLS1_STRCO             Reviewed;         215 AA.\nAC   Q9KZP3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 118.\nDE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS {ECO:0000305};\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:19439403};\nGN   Name=clsA {ECO:0000303|PubMed:22409773};\nGN   OrderedLocusNames=SCO1389 {ECO:0000312|EMBL:CAB88885.1};\nGN   ORFNames=SC1A8A.09c {ECO:0000312|EMBL:CAB88885.1};\nOS   Streptomyces coelicolor (strain ATCC BAA-471 / A3(2) / M145).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces; Streptomyces albidoflavus group.\nOX   NCBI_TaxID=100226 {ECO:0000312|Proteomes:UP000001973};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS {ECO:0000305};\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:19439403};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   SUBCELLULAR LOCATION.\nRX   PubMed=19439403; DOI=10.1074/jbc.m109.006072;\nRA   Sandoval-Calderon M., Geiger O., Guan Z., Barona-Gomez F., Sohlenkamp C.;\nRT   \"A eukaryote-like cardiolipin synthase is present in Streptomyces\nRT   coelicolor and in most actinobacteria.\";\nRL   J. Biol. Chem. 284:17383-17390(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H4",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=22409773; DOI=10.1111/j.1365-2958.2012.08018.x;\nRA   Jyothikumar V., Klanbut K., Tiong J., Roxburgh J.S., Hunter I.S.,\nRA   Smith T.K., Herron P.R.;\nRT   \"Cardiolipin synthase is required for Streptomyces coelicolor\nRT   morphogenesis.\";\nRL   Mol. Microbiol. 84:181-197(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=a divalent metal cation; Xref=ChEBI:CHEBI:60240;\nCC         Evidence={ECO:0000269|PubMed:19439403};\nCC       Note=Highest activity found with Co(2+) whereas Mn(2+) supports a lower\nCC       activity; no activity detected with Ni(2+), Ca(2+) or Mg(2+).\nCC       {ECO:0000269|PubMed:19439403};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 173. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
