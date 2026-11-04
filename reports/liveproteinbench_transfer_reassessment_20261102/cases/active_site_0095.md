# active_site_0095

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0095.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 112 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSFSSLFVAACAAVTAFALPSELEKRAITTSQQGTSNGYFYSFWTNGGGSVSYNNGASGEYSVSWSNCGSFTSGKGWATGSSRNINFSGSFKPSGNAYLAVYGWTTSPLVEYYIMENYGDYNPGRSMTFKGTVTSDGSVYDIYTHQQVNQPSISGTATFEQYWSIRRTKRSSGTVTTANHFKAWASHGMYLGSHNYQIVSTEGYQSSGSSDITVS

[Multiple Choices]
A. Position 122 (Nucleophile)
B. Position 213 (Proton acceptor)
C. Position 6593 (Proton acceptor; for dehydratase activity)
D. Position 112 (Nucleophile)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies position 112 as the nucleophile. This is computational annotation via PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short, signal-peptide-bearing, aromatic-rich sequence is consistent with a secreted fungal GH11 xylanase. GH11 xylanases use conserved catalytic glutamates; position 112 is Glu in the sequence, whereas position 122 is Tyr, making 112 the meaningful nucleophile candidate among those choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and the catalytic-glutamate pattern provide a transferable basis for choosing D over the alternatives, though they do not independently prove the exact annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered nucleophile positions are distinguishable from the sequence: position 112 is Glu, while position 122 is Tyr. The other choices do not provide a competing plausible nucleophile assignment.


### Important caveats

- The supporting active-site annotation is computational rather than experimental in the cited excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short, signal-peptide-bearing, aromatic-rich sequence is consistent with a secreted fungal GH11 xylanase. GH11 xylanases use conserved catalytic glutamates; position 112 is Glu in the sequence, whereas position 122 is Tyr, making 112 the meaningful nucleophile candidate among those choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the catalytic-glutamate pattern provide a transferable basis for choosing D over the alternatives, though they do not independently prove the exact annotation."
  },
  "case_id": "active_site_0095",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 112 as the nucleophile. This is computational annotation via PROSITE-ProRule, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The supporting active-site annotation is computational rather than experimental in the cited excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered nucleophile positions are distinguishable from the sequence: position 112 is Glu, while position 122 is Tyr. The other choices do not provide a competing plausible nucleophile assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0095",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 112 as the nucleophile. This is computational annotation via PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short, signal-peptide-bearing, aromatic-rich sequence is consistent with a secreted fungal GH11 xylanase. GH11 xylanases use conserved catalytic glutamates; position 112 is Glu in the sequence, whereas position 122 is Tyr, making 112 the meaningful nucleophile candidate among those choices.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the catalytic-glutamate pattern provide a transferable basis for choosing D over the alternatives, though they do not independently prove the exact annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered nucleophile positions are distinguishable from the sequence: position 112 is Glu, while position 122 is Tyr. The other choices do not provide a competing plausible nucleophile assignment."
  },
  "important_caveats": [
    "The supporting active-site annotation is computational rather than experimental in the cited excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry K9GHZ3 (Ethylene-inducing xylanase, EC 3.2.1.8) annotates position 112 as the catalytic nucleophile (ECO:0000255|PROSITE-ProRule:PRU01097). The residue at position 112 in the supplied 216-aa sequence is indeed Glu (E), which is the canonical nucleophile in glycoside hydrolase family 11 (GH11) xylanases. The annotation is computational (PROSITE-ProRule), not experimental, but it is well-supported by the sequence context and family-conserved catalytic motif. The second annotated active site (position 203, Proton donor) is not offered as a correct option, but D is the only option identifying a true annotated active-site residue.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can eliminate three options and confirm D using transferable biochemistry and protein-family knowledge without knowing this protein's specific annotation. (1) Option C (position 6593) is impossible for a 216-residue protein. (2) Option B (position 213, proton acceptor): residue 213 is Ile (I), a hydrophobic aliphatic side chain with no ionizable group capable of accepting a proton—this violates basic amino-acid chemistry. (3) Option A (position 122, nucleophile): residue 122 is Tyr (Y), which is not a nucleophile in glycosidases; the canonical nucleophiles in glycoside hydrolases are Glu or Asp. (4) Option D (position 112, nucleophile): residue 112 is Glu (E), the canonical nucleophile in GH11 and other glycoside hydrolase families. The small (~216 aa), cysteine-rich, N-terminal-signal-peptide-containing sequence is consistent with a secreted fungal glycoside hydrolase, reinforcing the expectation of a Glu/Asp catalytic nucleophile. Thus general knowledge of glycosidase catalytic mechanisms and amino-acid chemistry meaningfully distinguishes D from the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of C (position beyond sequence length), B (Ile cannot be a proton acceptor), and A (Tyr is not a glycosidase nucleophile) relies on general biochemistry and amino-acid properties. Confirming D as the nucleophile relies on the well-established fact that Glu is the canonical nucleophile in GH-family glycoside hydrolases, which is transferable knowledge from many homologous proteins. No target-specific annotation or memorized database entry is required to reach D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D identifies a residue (Glu at 112) that is chemically and mechanistically consistent with a glycosidase nucleophile. The other three options are eliminated by basic sequence-length constraints (C), amino-acid chemistry (B: Ile as proton acceptor), and catalytic-mechanism knowledge (A: Tyr as nucleophile). No ambiguity among the offered choices.


### Important caveats

- The active-site annotation is computational (PROSITE-ProRule PRU01097, ECO:0000255), not derived from site-directed mutagenesis or crystallography. However, PROSITE-ProRule annotations for GH11 catalytic residues are well-validated across many characterized xylanases.
- The protein is annotated as a precursor; the signal peptide (approx. residues 1–19) would be cleaved in the mature enzyme. The numbering 112 refers to the precursor coordinates, which is the standard UniProt convention and matches the supplied sequence.
- The question asks for the 'catalytic center' but the full catalytic dyad includes both position 112 (nucleophile) and position 203 (proton donor). Only position 112 appears among the correct options, so D is the best single choice despite not listing the complete dyad.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate three options and confirm D using transferable biochemistry and protein-family knowledge without knowing this protein's specific annotation. (1) Option C (position 6593) is impossible for a 216-residue protein. (2) Option B (position 213, proton acceptor): residue 213 is Ile (I), a hydrophobic aliphatic side chain with no ionizable group capable of accepting a proton—this violates basic amino-acid chemistry. (3) Option A (position 122, nucleophile): residue 122 is Tyr (Y), which is not a nucleophile in glycosidases; the canonical nucleophiles in glycoside hydrolases are Glu or Asp. (4) Option D (position 112, nucleophile): residue 112 is Glu (E), the canonical nucleophile in GH11 and other glycoside hydrolase families. The small (~216 aa), cysteine-rich, N-terminal-signal-peptide-containing sequence is consistent with a secreted fungal glycoside hydrolase, reinforcing the expectation of a Glu/Asp catalytic nucleophile. Thus general knowledge of glycosidase catalytic mechanisms and amino-acid chemistry meaningfully distinguishes D from the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of C (position beyond sequence length), B (Ile cannot be a proton acceptor), and A (Tyr is not a glycosidase nucleophile) relies on general biochemistry and amino-acid properties. Confirming D as the nucleophile relies on the well-established fact that Glu is the canonical nucleophile in GH-family glycoside hydrolases, which is transferable knowledge from many homologous proteins. No target-specific annotation or memorized database entry is required to reach D."
  },
  "case_id": "active_site_0095",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry K9GHZ3 (Ethylene-inducing xylanase, EC 3.2.1.8) annotates position 112 as the catalytic nucleophile (ECO:0000255|PROSITE-ProRule:PRU01097). The residue at position 112 in the supplied 216-aa sequence is indeed Glu (E), which is the canonical nucleophile in glycoside hydrolase family 11 (GH11) xylanases. The annotation is computational (PROSITE-ProRule), not experimental, but it is well-supported by the sequence context and family-conserved catalytic motif. The second annotated active site (position 203, Proton donor) is not offered as a correct option, but D is the only option identifying a true annotated active-site residue."
  },
  "important_caveats": [
    "The active-site annotation is computational (PROSITE-ProRule PRU01097, ECO:0000255), not derived from site-directed mutagenesis or crystallography. However, PROSITE-ProRule annotations for GH11 catalytic residues are well-validated across many characterized xylanases.",
    "The protein is annotated as a precursor; the signal peptide (approx. residues 1–19) would be cleaved in the mature enzyme. The numbering 112 refers to the precursor coordinates, which is the standard UniProt convention and matches the supplied sequence.",
    "The question asks for the 'catalytic center' but the full catalytic dyad includes both position 112 (nucleophile) and position 203 (proton donor). Only position 112 appears among the correct options, so D is the best single choice despite not listing the complete dyad."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D identifies a residue (Glu at 112) that is chemically and mechanistically consistent with a glycosidase nucleophile. The other three options are eliminated by basic sequence-length constraints (C), amino-acid chemistry (B: Ile as proton acceptor), and catalytic-mechanism knowledge (A: Tyr as nucleophile). No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0095",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry K9GHZ3 (Ethylene-inducing xylanase, EC 3.2.1.8) annotates position 112 as the catalytic nucleophile (ECO:0000255|PROSITE-ProRule:PRU01097). The residue at position 112 in the supplied 216-aa sequence is indeed Glu (E), which is the canonical nucleophile in glycoside hydrolase family 11 (GH11) xylanases. The annotation is computational (PROSITE-ProRule), not experimental, but it is well-supported by the sequence context and family-conserved catalytic motif. The second annotated active site (position 203, Proton donor) is not offered as a correct option, but D is the only option identifying a true annotated active-site residue.",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can eliminate three options and confirm D using transferable biochemistry and protein-family knowledge without knowing this protein's specific annotation. (1) Option C (position 6593) is impossible for a 216-residue protein. (2) Option B (position 213, proton acceptor): residue 213 is Ile (I), a hydrophobic aliphatic side chain with no ionizable group capable of accepting a proton—this violates basic amino-acid chemistry. (3) Option A (position 122, nucleophile): residue 122 is Tyr (Y), which is not a nucleophile in glycosidases; the canonical nucleophiles in glycoside hydrolases are Glu or Asp. (4) Option D (position 112, nucleophile): residue 112 is Glu (E), the canonical nucleophile in GH11 and other glycoside hydrolase families. The small (~216 aa), cysteine-rich, N-terminal-signal-peptide-containing sequence is consistent with a secreted fungal glycoside hydrolase, reinforcing the expectation of a Glu/Asp catalytic nucleophile. Thus general knowledge of glycosidase catalytic mechanisms and amino-acid chemistry meaningfully distinguishes D from the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of C (position beyond sequence length), B (Ile cannot be a proton acceptor), and A (Tyr is not a glycosidase nucleophile) relies on general biochemistry and amino-acid properties. Confirming D as the nucleophile relies on the well-established fact that Glu is the canonical nucleophile in GH-family glycoside hydrolases, which is transferable knowledge from many homologous proteins. No target-specific annotation or memorized database entry is required to reach D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D identifies a residue (Glu at 112) that is chemically and mechanistically consistent with a glycosidase nucleophile. The other three options are eliminated by basic sequence-length constraints (C), amino-acid chemistry (B: Ile as proton acceptor), and catalytic-mechanism knowledge (A: Tyr as nucleophile). No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The active-site annotation is computational (PROSITE-ProRule PRU01097, ECO:0000255), not derived from site-directed mutagenesis or crystallography. However, PROSITE-ProRule annotations for GH11 catalytic residues are well-validated across many characterized xylanases.",
    "The protein is annotated as a precursor; the signal peptide (approx. residues 1–19) would be cleaved in the mature enzyme. The numbering 112 refers to the precursor coordinates, which is the standard UniProt convention and matches the supplied sequence.",
    "The question asks for the 'catalytic center' but the full catalytic dyad includes both position 112 (nucleophile) and position 203 (proton donor). Only position 112 appears among the correct options, so D is the best single choice despite not listing the complete dyad."
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
  "benchmark_sequence_length": 216,
  "benchmark_sequence_sha256": "a43bc3a676b5d19b8e6508b04a2c94642fc3a180c24cd6d47e5e6705a113a73e",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-02-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 216,
  "current_source_sequence_sha256": "a43bc3a676b5d19b8e6508b04a2c94642fc3a180c24cd6d47e5e6705a113a73e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "K9GHZ3",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3",
  "selected_historical_source_sequence_length": 216,
  "selected_historical_source_sequence_sha256": "a43bc3a676b5d19b8e6508b04a2c94642fc3a180c24cd6d47e5e6705a113a73e",
  "selected_historical_version": {
    "accession": "K9GHZ3",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX_PEND1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"K9GHZ3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-02-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Green mold\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Penicillium\"],\"scientificName\":\"Penicillium digitatum (strain Pd1 / CECT 20795)\",\"taxonId\":1170230}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39718348\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39718348\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39718348\",\"source\":\"PubMed\"}],\"value\":\"EIX\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":112},\"start\":{\"modifier\":\"EXACT\",\"value\":112}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":203},\"start\":{\"modifier\":\"EXACT\",\"value\":203}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"He J.\",\"Li R.\",\"Xu C.\",\"Chen X.\",\"Yao J.\",\"Li Z.\",\"Cheng Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39718348\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.jafc.4c07212\"}],\"citationType\":\"journal article\",\"firstPage\":\"135\",\"id\":\"39718348\",\"journal\":\"J. Agric. Food Chem.\",\"lastPage\":\"146\",\"publicationDate\":\"2025\",\"title\":\"Enhancing Fruit Resistance against Fungal Pathogens Using a Pathogen-Associated Molecular Pattern PdEIX.\",\"volume\":\"73\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:58.976117+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde",
  "url": "https://rest.uniprot.org/uniprotkb/K9GHZ3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   EIX_PEND1               Reviewed;         216 AA.\nAC   K9GHZ3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-FEB-2013, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:39718348};\nDE            Short=EIX {ECO:0000303|PubMed:39718348};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:39718348};\nDE   Flags: Precursor;\nGN   Name=EIX {ECO:0000303|PubMed:39718348}; ORFNames=PDIP_02920;\nOS   Penicillium digitatum (strain Pd1 / CECT 20795) (Green mold).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.\nOX   NCBI_TaxID=1170230;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:01.625551+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3",
  "url": "https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND SUBCELLULAR LOCATION.\nRX   PubMed=39718348; DOI=10.1021/acs.jafc.4c07212;\nRA   He J., Li R., Xu C., Chen X., Yao J., Li Z., Cheng Y.;\nRT   \"Enhancing Fruit Resistance against Fungal Pathogens Using a Pathogen-\nRT   Associated Molecular Pattern PdEIX.\";\nRL   J. Agric. Food Chem. 73:135-146(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:01.625551+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3",
  "url": "https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        112\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:01.625551+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3",
  "url": "https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        203\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:01.625551+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3",
  "url": "https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 95. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
