# EC_number_0189

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0189.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.7.8.7

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTDSNLLGLTCWLIDTRTLWPGQHIKDAASDILHLLSNDERNAVLRKIFIADARMSLASALLKRLYISRALNIPWRDVKIARKGDPTHGKPCAVLPDGSFAPIDFNVSHQAGLVSLVGWNPPPGQSQSALVGTDIVCVNERDDYRTIDQEGFDAWIDIYEDVFSEAERWDMKYNVDYITLLDGRIIQGNSLGRVDRCVRRNKDLSITLPTGETHSFNSDLLIDAKLRRFYSFFCYKEAYIKLAGEALLAPWLKELEFQNVKSPKPGTVARCSTHGTWGEKVSDVEVVLHGEKVEDVKMTLQAFEENFMLATAVQGLRDLEAPPFTKLNLENDVVAFAS

[Multiple Choices]
A. 2.7.8.41
B. 2.7.8.7
C. 3.2.1.183
D. 1.16.1.10
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation assigns EC 2.7.8.7 and describes the reaction as conversion of apo-ACP to holo-ACP. This supports B, although the cited evidence is transferred from a homolog (ECO:0000250), not direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble phosphopantetheinyl-transferase family protein. Transferable knowledge of that family connects its role—adding a 4′-phosphopantetheine group to ACP—to EC 2.7.8.7 (B). The other choices represent different reaction classes; in particular, the membrane-associated character expected of many phospholipid-transfer enzymes is not suggested by this sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and the known reaction of phosphopantetheinyl transferases provide a meaningful basis to distinguish B without knowing this protein's specific database entry. This is a credible inference, not proof of the exact protein's measured activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered options, only B corresponds to the phosphopantetheinyl-transferase reaction suggested by the sequence.


### Important caveats

- The supporting database EC annotation is explicitly homolog-transferred; the supplied evidence does not establish direct experimental characterization of this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble phosphopantetheinyl-transferase family protein. Transferable knowledge of that family connects its role—adding a 4′-phosphopantetheine group to ACP—to EC 2.7.8.7 (B). The other choices represent different reaction classes; in particular, the membrane-associated character expected of many phospholipid-transfer enzymes is not suggested by this sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the known reaction of phosphopantetheinyl transferases provide a meaningful basis to distinguish B without knowing this protein's specific database entry. This is a credible inference, not proof of the exact protein's measured activity."
  },
  "case_id": "EC_number_0189",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.7.8.7 and describes the reaction as conversion of apo-ACP to holo-ACP. This supports B, although the cited evidence is transferred from a homolog (ECO:0000250), not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supporting database EC annotation is explicitly homolog-transferred; the supplied evidence does not establish direct experimental characterization of this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, only B corresponds to the phosphopantetheinyl-transferase reaction suggested by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0189",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.7.8.7 and describes the reaction as conversion of apo-ACP to holo-ACP. This supports B, although the cited evidence is transferred from a homolog (ECO:0000250), not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble phosphopantetheinyl-transferase family protein. Transferable knowledge of that family connects its role—adding a 4′-phosphopantetheine group to ACP—to EC 2.7.8.7 (B). The other choices represent different reaction classes; in particular, the membrane-associated character expected of many phospholipid-transfer enzymes is not suggested by this sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the known reaction of phosphopantetheinyl transferases provide a meaningful basis to distinguish B without knowing this protein's specific database entry. This is a credible inference, not proof of the exact protein's measured activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, only B corresponds to the phosphopantetheinyl-transferase reaction suggested by the sequence."
  },
  "important_caveats": [
    "The supporting database EC annotation is explicitly homolog-transferred; the supplied evidence does not establish direct experimental characterization of this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A223GB52 annotates this 338-aa protein as 4'-phosphopantetheinyl transferase (EC 2.7.8.7). The annotation is based on similarity inference (ECO:0000250) from Q4X1W0, a characterized PPTase, rather than direct experimental kinetics. The catalytic reaction (apo-&#91;ACP&#93; + CoA → holo-&#91;ACP&#93; + adenosine 3',5'-bisphosphate + H+) is recorded. The annotation is consistent with the expected answer, though it is computational/transferred rather than experimentally validated for this exact sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable 'HGTWGEK' motif near the C-terminal region (~residue 295), which matches the HxxGxG/HxxGxxG nucleotide-binding signature characteristic of the Sfp/AcpH phosphopantetheinyl transferase family. This motif is a well-known, transferable feature learned from extensively characterized bacterial PPTases (e.g., Sfp from B. subtilis, AcpH from M. tuberculosis). The overall 338-aa length and mixed α/β architecture are consistent with the PPTase fold. Options C (EC 3.2.1.183, a glycosidase) and D (EC 1.16.1.10, a multicopper oxidase/ferroxidase) can be eliminated because the sequence lacks glycosidase catalytic residues (Asp/Glu pairs, β-propeller/TIM-barrel signatures) and multicopper-oxidase copper-binding motifs (H-x-H, H-x-x-H). Between A (2.7.8.41) and B (2.7.8.7), the HxxGxG-family motif and the overall PPTase-like sequence architecture point specifically to 2.7.8.7. EC 2.7.8.41 is an obscure transferase without the Sfp/AcpH motif signature.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PPTase family is one of the most thoroughly characterized enzyme families in enzymology. The HxxGxG motif, overall fold, and length are transferable knowledge from dozens of characterized PPTases across bacteria and fungi. A knowledgeable model can recognize the 'HGTWGEK' motif as a PPTase signature and eliminate non-transferase options by EC-class reasoning, then distinguish 2.7.8.7 from the obscure 2.7.8.41 by the specific family motif.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are eliminated by EC-class mismatch (hydrolase, oxidoreductase vs. transferase). Option A (2.7.8.41) lacks the Sfp/AcpH HxxGxG motif and is a very obscure entry, making B the clearly supported choice given the recognizable PPTase signature.


### Important caveats

- The UniProt annotation is based on similarity inference (ECO:0000250) from Q4X1W0, not direct experimental characterization of this exact protein.
- The 'HGTWGEK' motif is a variant of the canonical HxxGxG PPTase motif; fungal PPTases may show slight motif deviations compared to well-studied bacterial homologs.
- EC 2.7.8.41 is an extremely obscure entry; its non-PPTase nature is inferred from the absence of the Sfp/AcpH signature in the target sequence rather than from positive identification of 2.7.8.41-specific features.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable 'HGTWGEK' motif near the C-terminal region (~residue 295), which matches the HxxGxG/HxxGxxG nucleotide-binding signature characteristic of the Sfp/AcpH phosphopantetheinyl transferase family. This motif is a well-known, transferable feature learned from extensively characterized bacterial PPTases (e.g., Sfp from B. subtilis, AcpH from M. tuberculosis). The overall 338-aa length and mixed α/β architecture are consistent with the PPTase fold. Options C (EC 3.2.1.183, a glycosidase) and D (EC 1.16.1.10, a multicopper oxidase/ferroxidase) can be eliminated because the sequence lacks glycosidase catalytic residues (Asp/Glu pairs, β-propeller/TIM-barrel signatures) and multicopper-oxidase copper-binding motifs (H-x-H, H-x-x-H). Between A (2.7.8.41) and B (2.7.8.7), the HxxGxG-family motif and the overall PPTase-like sequence architecture point specifically to 2.7.8.7. EC 2.7.8.41 is an obscure transferase without the Sfp/AcpH motif signature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PPTase family is one of the most thoroughly characterized enzyme families in enzymology. The HxxGxG motif, overall fold, and length are transferable knowledge from dozens of characterized PPTases across bacteria and fungi. A knowledgeable model can recognize the 'HGTWGEK' motif as a PPTase signature and eliminate non-transferase options by EC-class reasoning, then distinguish 2.7.8.7 from the obscure 2.7.8.41 by the specific family motif."
  },
  "case_id": "EC_number_0189",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A223GB52 annotates this 338-aa protein as 4'-phosphopantetheinyl transferase (EC 2.7.8.7). The annotation is based on similarity inference (ECO:0000250) from Q4X1W0, a characterized PPTase, rather than direct experimental kinetics. The catalytic reaction (apo-[ACP] + CoA → holo-[ACP] + adenosine 3',5'-bisphosphate + H+) is recorded. The annotation is consistent with the expected answer, though it is computational/transferred rather than experimentally validated for this exact sequence."
  },
  "important_caveats": [
    "The UniProt annotation is based on similarity inference (ECO:0000250) from Q4X1W0, not direct experimental characterization of this exact protein.",
    "The 'HGTWGEK' motif is a variant of the canonical HxxGxG PPTase motif; fungal PPTases may show slight motif deviations compared to well-studied bacterial homologs.",
    "EC 2.7.8.41 is an extremely obscure entry; its non-PPTase nature is inferred from the absence of the Sfp/AcpH signature in the target sequence rather than from positive identification of 2.7.8.41-specific features."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are eliminated by EC-class mismatch (hydrolase, oxidoreductase vs. transferase). Option A (2.7.8.41) lacks the Sfp/AcpH HxxGxG motif and is a very obscure entry, making B the clearly supported choice given the recognizable PPTase signature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0189",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A223GB52 annotates this 338-aa protein as 4'-phosphopantetheinyl transferase (EC 2.7.8.7). The annotation is based on similarity inference (ECO:0000250) from Q4X1W0, a characterized PPTase, rather than direct experimental kinetics. The catalytic reaction (apo-[ACP] + CoA → holo-[ACP] + adenosine 3',5'-bisphosphate + H+) is recorded. The annotation is consistent with the expected answer, though it is computational/transferred rather than experimentally validated for this exact sequence.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable 'HGTWGEK' motif near the C-terminal region (~residue 295), which matches the HxxGxG/HxxGxxG nucleotide-binding signature characteristic of the Sfp/AcpH phosphopantetheinyl transferase family. This motif is a well-known, transferable feature learned from extensively characterized bacterial PPTases (e.g., Sfp from B. subtilis, AcpH from M. tuberculosis). The overall 338-aa length and mixed α/β architecture are consistent with the PPTase fold. Options C (EC 3.2.1.183, a glycosidase) and D (EC 1.16.1.10, a multicopper oxidase/ferroxidase) can be eliminated because the sequence lacks glycosidase catalytic residues (Asp/Glu pairs, β-propeller/TIM-barrel signatures) and multicopper-oxidase copper-binding motifs (H-x-H, H-x-x-H). Between A (2.7.8.41) and B (2.7.8.7), the HxxGxG-family motif and the overall PPTase-like sequence architecture point specifically to 2.7.8.7. EC 2.7.8.41 is an obscure transferase without the Sfp/AcpH motif signature.",
    "missing_item_specific_fact": "",
    "reason": "The PPTase family is one of the most thoroughly characterized enzyme families in enzymology. The HxxGxG motif, overall fold, and length are transferable knowledge from dozens of characterized PPTases across bacteria and fungi. A knowledgeable model can recognize the 'HGTWGEK' motif as a PPTase signature and eliminate non-transferase options by EC-class reasoning, then distinguish 2.7.8.7 from the obscure 2.7.8.41 by the specific family motif."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are eliminated by EC-class mismatch (hydrolase, oxidoreductase vs. transferase). Option A (2.7.8.41) lacks the Sfp/AcpH HxxGxG motif and is a very obscure entry, making B the clearly supported choice given the recognizable PPTase signature."
  },
  "important_caveats": [
    "The UniProt annotation is based on similarity inference (ECO:0000250) from Q4X1W0, not direct experimental characterization of this exact protein.",
    "The 'HGTWGEK' motif is a variant of the canonical HxxGxG PPTase motif; fungal PPTases may show slight motif deviations compared to well-studied bacterial homologs.",
    "EC 2.7.8.41 is an extremely obscure entry; its non-PPTase nature is inferred from the absence of the Sfp/AcpH signature in the target sequence rather than from positive identification of 2.7.8.41-specific features."
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
  "benchmark_sequence_length": 338,
  "benchmark_sequence_sha256": "99855a22c8c6713370da447a442e50fb925d79b1af9649603cf5c916be789205",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-10-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 338,
  "current_source_sequence_sha256": "99855a22c8c6713370da447a442e50fb925d79b1af9649603cf5c916be789205",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A223GB52",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0",
  "selected_historical_source_sequence_length": 338,
  "selected_historical_source_sequence_sha256": "99855a22c8c6713370da447a442e50fb925d79b1af9649603cf5c916be789205",
  "selected_historical_version": {
    "accession": "A0A223GB52",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PPTA_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A223GB52\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:40.730186+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GB52.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-10-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:40.730186+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GB52.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:40.730186+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GB52.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1W0\",\"source\":\"UniProtKB\"}],\"value\":\"Acyl-carrier-protein synthase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1W0\",\"source\":\"UniProtKB\"}],\"value\":\"Phosphopantetheine:protein transferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1W0\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.8.7\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.2\",\"source\":\"Reference\"}],\"value\":\"4'-phosphopantetheinyl transferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.2\",\"source\":\"Reference\"}],\"value\":\"PPTase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:40.730186+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GB52.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.8.7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1W0\",\"source\":\"UniProtKB\"}],\"name\":\"apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:12068\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9685\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9690\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58343\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64479\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:40.730186+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GB52.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   PPTA_AURME              Reviewed;         338 AA.\nAC   A0A223GB52;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-OCT-2017, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=4'-phosphopantetheinyl transferase {ECO:0000303|Ref.2};\nDE            Short=PPTase {ECO:0000303|Ref.2};\nDE            EC=2.7.8.7 {ECO:0000250|UniProtKB:Q4X1W0};\nDE   AltName: Full=Acyl-carrier-protein synthase {ECO:0000250|UniProtKB:Q4X1W0};\nDE   AltName: Full=Phosphopantetheine:protein transferase {ECO:0000250|UniProtKB:Q4X1W0};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:42.924113+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0",
  "url": "https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4'-phosphopantetheinyl transferase {ECO:0000303|Ref.2};\nDE            Short=PPTase {ECO:0000303|Ref.2};\nDE            EC=2.7.8.7 {ECO:0000250|UniProtKB:Q4X1W0};\nDE   AltName: Full=Acyl-carrier-protein synthase {ECO:0000250|UniProtKB:Q4X1W0};\nDE   AltName: Full=Phosphopantetheine:protein transferase {ECO:0000250|UniProtKB:Q4X1W0};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:42.924113+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0",
  "url": "https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate +\nCC         H(+); Xref=Rhea:RHEA:12068, Rhea:RHEA-COMP:9685, Rhea:RHEA-COMP:9690,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:58343, ChEBI:CHEBI:64479; EC=2.7.8.7;\nCC         Evidence={ECO:0000250|UniProtKB:Q4X1W0};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:42.924113+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0",
  "url": "https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 189. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
