# active_site_0121

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0121.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 279 (Proton donor/acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGVEEADKLKQLGNAAFSERKWHLAIDMYTKAIELTKTPTLFCNRALAELRAELPGAALADADAALGIEPTFAKAYYHKASAYLSLGKHKQALTNYKKVVDLAPQNSDAQAKVEFCKKEIRRINFENAIMTPDEAPLSQTIKLGSVRADYDGPRIENETVTVEFVEAMKEHFRLEKLIDRHDVIFILLEVQKILKKCPNFVSINVPVGEEITVCGDTHGQYYDLLNIFKLNGNPLETNRYLFNGDFVDRGSYSFENIMTLFAYKVLYPDHFFLSRGNHEGVSMNRMYGFEGEVTQKYNSEMFRLFTEVFNSLPIGHIINNEVFVVHGGLYSSDKVTLDDLQHPNRFRDIPESGLICESLWSDPQPMPGRAPSKRGVSCLSFGPDVTETFLNNNNLKLLVRSHEVKDEGYEIEHGGKCITVFSAPNYCDQMGNKGAFIRFTGGDMKPRFTTFTHVPHPGKRPMHYATGFGLF

[Multiple Choices]
A. Position 380 (For beta-ketoacyl synthase activity)
B. Position 341 (For beta-ketoacyl synthase 1 activity)
C. Position 166 (Proton acceptor)
D. Position 279 (Proton donor/acceptor)
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

> The sequence-matched UniProt annotation identifies residue 279 as an active-site proton donor/acceptor. This is computational annotation evidence (ECO:0000255, including a PIRSR rule), not direct experimental validation, but it supports the keyed claim.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the conserved catalytic-domain features of a PPP-family serine/threonine phosphatase. Transferable knowledge of this family and alignment to homologous phosphatases supports residue 279, an Asp in the catalytic domain, as a catalytic acid/base residue. That distinguishes D from the beta-ketoacyl-synthase options; position 166 is not in the corresponding conserved catalytic motif.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level sequence signature and conserved catalytic-residue pattern provide a meaningful basis to favor D without relying on the exact protein's database record. The residue-level role is an inference from homologous phosphatases, not something established solely by the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives identify different residues or incompatible enzyme activities; the conserved phosphatase catalytic-site inference favors D.


### Important caveats

- The supplied reviewer evidence supports the key through computational annotation; it does not establish experimental confirmation of residue 279's role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the conserved catalytic-domain features of a PPP-family serine/threonine phosphatase. Transferable knowledge of this family and alignment to homologous phosphatases supports residue 279, an Asp in the catalytic domain, as a catalytic acid/base residue. That distinguishes D from the beta-ketoacyl-synthase options; position 166 is not in the corresponding conserved catalytic motif.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level sequence signature and conserved catalytic-residue pattern provide a meaningful basis to favor D without relying on the exact protein's database record. The residue-level role is an inference from homologous phosphatases, not something established solely by the sequence."
  },
  "case_id": "active_site_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 279 as an active-site proton donor/acceptor. This is computational annotation evidence (ECO:0000255, including a PIRSR rule), not direct experimental validation, but it supports the keyed claim."
  },
  "important_caveats": [
    "The supplied reviewer evidence supports the key through computational annotation; it does not establish experimental confirmation of residue 279's role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives identify different residues or incompatible enzyme activities; the conserved phosphatase catalytic-site inference favors D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0121",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 279 as an active-site proton donor/acceptor. This is computational annotation evidence (ECO:0000255, including a PIRSR rule), not direct experimental validation, but it supports the keyed claim.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the conserved catalytic-domain features of a PPP-family serine/threonine phosphatase. Transferable knowledge of this family and alignment to homologous phosphatases supports residue 279, an Asp in the catalytic domain, as a catalytic acid/base residue. That distinguishes D from the beta-ketoacyl-synthase options; position 166 is not in the corresponding conserved catalytic motif.",
    "missing_item_specific_fact": "",
    "reason": "The family-level sequence signature and conserved catalytic-residue pattern provide a meaningful basis to favor D without relying on the exact protein's database record. The residue-level role is an inference from homologous phosphatases, not something established solely by the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives identify different residues or incompatible enzyme activities; the conserved phosphatase catalytic-site inference favors D."
  },
  "important_caveats": [
    "The supplied reviewer evidence supports the key through computational annotation; it does not establish experimental confirmation of residue 279's role."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q388N2 (PPP5_TRYB2, Serine/threonine-protein phosphatase T, EC 3.1.3.16) annotates position 279 as 'Proton donor/acceptor' (Active site), supported by evidence codes ECO:0000255 and ECO:0000255|PIRSR:PIRSR033096-1. The sequence at position 279 is indeed Histidine (H), consistent with the PPP-family catalytic mechanism. The annotation is computational (PIRSF pattern-based, not direct experimental measurement for this protein), but it is consistent with well-established PPP-phosphatase catalysis and the sequence match is confirmed.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmarks of PPP-family phosphatases: GDxVxG-like metal-binding motifs (CGDTHG at ~215-220, NGDFVDR at ~245-250), multiple Mn2+-coordinating residues, and the overall ~470-aa catalytic domain architecture. This immediately eliminates options A and B, which reference beta-ketoacyl synthase (a completely unrelated enzyme family in fatty-acid synthesis). Position 166 is Valine (V), a hydrophobic residue incapable of proton transfer, eliminating option C. Position 279 is Histidine (H), situated in the 'HEG' context (H279-E280-G281) within the metal-binding region. In PPP-family phosphatases (PP1, PP2A, PP5), the catalytic proton donor/acceptor is a conserved His in this region, acting as general acid/base during phosphoryl transfer. Recognizing the PPP family from sequence motifs and knowing that His is the canonical proton donor/acceptor in this family meaningfully distinguishes D from all other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the protein as a PPP-family phosphatase from conserved sequence motifs (GDxVxG-like, metal-binding clusters, domain length), eliminate A and B as referring to an unrelated enzyme class, eliminate C because position 166 is Valine (chemically impossible as proton acceptor), and select D because position 279 is Histidine in the expected catalytic context for PPP phosphatases. This relies on transferable family knowledge and basic amino-acid chemistry, not on memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B reference beta-ketoacyl synthase, an entirely different enzyme class, making them clearly inapplicable. Option C places a proton acceptor at a Valine residue, which is chemically infeasible. Option D (His at 279) is the only choice consistent with both the amino acid identity and the known PPP-phosphatase catalytic mechanism. No ambiguity exists among the offered alternatives.


### Important caveats

- The active-site annotation at position 279 is computational (PIRSF pattern ECO:0000255), not a direct experimental measurement on this Trypanosoma protein. However, the mechanism is well-established across the PPP family and the His is in the structurally expected context.
- The model would need to count to position 279 in a 472-aa sequence to verify the residue identity; errors in counting could lead to selecting a different option, though the elimination logic for A, B, and C is robust regardless of exact counting.
- The UniProt annotation was transferred from human PP5 (P53041) by similarity (ECO:0000250) for metal-binding sites; the active-site annotation uses PIRSF pattern matching rather than direct mutagenesis data on this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmarks of PPP-family phosphatases: GDxVxG-like metal-binding motifs (CGDTHG at ~215-220, NGDFVDR at ~245-250), multiple Mn2+-coordinating residues, and the overall ~470-aa catalytic domain architecture. This immediately eliminates options A and B, which reference beta-ketoacyl synthase (a completely unrelated enzyme family in fatty-acid synthesis). Position 166 is Valine (V), a hydrophobic residue incapable of proton transfer, eliminating option C. Position 279 is Histidine (H), situated in the 'HEG' context (H279-E280-G281) within the metal-binding region. In PPP-family phosphatases (PP1, PP2A, PP5), the catalytic proton donor/acceptor is a conserved His in this region, acting as general acid/base during phosphoryl transfer. Recognizing the PPP family from sequence motifs and knowing that His is the canonical proton donor/acceptor in this family meaningfully distinguishes D from all other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the protein as a PPP-family phosphatase from conserved sequence motifs (GDxVxG-like, metal-binding clusters, domain length), eliminate A and B as referring to an unrelated enzyme class, eliminate C because position 166 is Valine (chemically impossible as proton acceptor), and select D because position 279 is Histidine in the expected catalytic context for PPP phosphatases. This relies on transferable family knowledge and basic amino-acid chemistry, not on memorizing this specific protein's annotation."
  },
  "case_id": "active_site_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q388N2 (PPP5_TRYB2, Serine/threonine-protein phosphatase T, EC 3.1.3.16) annotates position 279 as 'Proton donor/acceptor' (Active site), supported by evidence codes ECO:0000255 and ECO:0000255|PIRSR:PIRSR033096-1. The sequence at position 279 is indeed Histidine (H), consistent with the PPP-family catalytic mechanism. The annotation is computational (PIRSF pattern-based, not direct experimental measurement for this protein), but it is consistent with well-established PPP-phosphatase catalysis and the sequence match is confirmed."
  },
  "important_caveats": [
    "The active-site annotation at position 279 is computational (PIRSF pattern ECO:0000255), not a direct experimental measurement on this Trypanosoma protein. However, the mechanism is well-established across the PPP family and the His is in the structurally expected context.",
    "The model would need to count to position 279 in a 472-aa sequence to verify the residue identity; errors in counting could lead to selecting a different option, though the elimination logic for A, B, and C is robust regardless of exact counting.",
    "The UniProt annotation was transferred from human PP5 (P53041) by similarity (ECO:0000250) for metal-binding sites; the active-site annotation uses PIRSF pattern matching rather than direct mutagenesis data on this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B reference beta-ketoacyl synthase, an entirely different enzyme class, making them clearly inapplicable. Option C places a proton acceptor at a Valine residue, which is chemically infeasible. Option D (His at 279) is the only choice consistent with both the amino acid identity and the known PPP-phosphatase catalytic mechanism. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0121",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q388N2 (PPP5_TRYB2, Serine/threonine-protein phosphatase T, EC 3.1.3.16) annotates position 279 as 'Proton donor/acceptor' (Active site), supported by evidence codes ECO:0000255 and ECO:0000255|PIRSR:PIRSR033096-1. The sequence at position 279 is indeed Histidine (H), consistent with the PPP-family catalytic mechanism. The annotation is computational (PIRSF pattern-based, not direct experimental measurement for this protein), but it is consistent with well-established PPP-phosphatase catalysis and the sequence match is confirmed.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmarks of PPP-family phosphatases: GDxVxG-like metal-binding motifs (CGDTHG at ~215-220, NGDFVDR at ~245-250), multiple Mn2+-coordinating residues, and the overall ~470-aa catalytic domain architecture. This immediately eliminates options A and B, which reference beta-ketoacyl synthase (a completely unrelated enzyme family in fatty-acid synthesis). Position 166 is Valine (V), a hydrophobic residue incapable of proton transfer, eliminating option C. Position 279 is Histidine (H), situated in the 'HEG' context (H279-E280-G281) within the metal-binding region. In PPP-family phosphatases (PP1, PP2A, PP5), the catalytic proton donor/acceptor is a conserved His in this region, acting as general acid/base during phosphoryl transfer. Recognizing the PPP family from sequence motifs and knowing that His is the canonical proton donor/acceptor in this family meaningfully distinguishes D from all other choices.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the protein as a PPP-family phosphatase from conserved sequence motifs (GDxVxG-like, metal-binding clusters, domain length), eliminate A and B as referring to an unrelated enzyme class, eliminate C because position 166 is Valine (chemically impossible as proton acceptor), and select D because position 279 is Histidine in the expected catalytic context for PPP phosphatases. This relies on transferable family knowledge and basic amino-acid chemistry, not on memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B reference beta-ketoacyl synthase, an entirely different enzyme class, making them clearly inapplicable. Option C places a proton acceptor at a Valine residue, which is chemically infeasible. Option D (His at 279) is the only choice consistent with both the amino acid identity and the known PPP-phosphatase catalytic mechanism. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The active-site annotation at position 279 is computational (PIRSF pattern ECO:0000255), not a direct experimental measurement on this Trypanosoma protein. However, the mechanism is well-established across the PPP family and the His is in the structurally expected context.",
    "The model would need to count to position 279 in a 472-aa sequence to verify the residue identity; errors in counting could lead to selecting a different option, though the elimination logic for A, B, and C is robust regardless of exact counting.",
    "The UniProt annotation was transferred from human PP5 (P53041) by similarity (ECO:0000250) for metal-binding sites; the active-site annotation uses PIRSF pattern matching rather than direct mutagenesis data on this specific protein."
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
  "benchmark_sequence_length": 472,
  "benchmark_sequence_sha256": "cc9358577e82c28a804de40071ec7b0e03104416e51a61cdb314664011a043f5",
  "current_entry_audit": {
    "entryVersion": 116,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-11-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 472,
  "current_source_sequence_sha256": "cc9358577e82c28a804de40071ec7b0e03104416e51a61cdb314664011a043f5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 114,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q388N2",
  "selected_historical_entry_version": 114,
  "selected_historical_record_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "selected_historical_source_sequence_length": 472,
  "selected_historical_source_sequence_sha256": "cc9358577e82c28a804de40071ec7b0e03104416e51a61cdb314664011a043f5",
  "selected_historical_version": {
    "accession": "Q388N2",
    "database": "Swiss-Prot",
    "entryVersion": 114,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PPP5_TRYB2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q388N2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":116,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-11-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008524\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Trypanosoma\"],\"scientificName\":\"Trypanosoma brucei brucei (strain 927/4 GUTat10.1)\",\"taxonId\":185431}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"value\":\"TbPP5\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"value\":\"3.1.3.16\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Serine/threonine-protein phosphatase T\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PPT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor/acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR033096-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":279},\"start\":{\"modifier\":\"EXACT\",\"value\":279}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53041\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29035\",\"label\":\"1\",\"name\":\"Mn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":217},\"start\":{\"modifier\":\"EXACT\",\"value\":217}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53041\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29035\",\"label\":\"1\",\"name\":\"Mn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":219},\"start\":{\"modifier\":\"EXACT\",\"value\":219}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53041\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29035\",\"label\":\"1\",\"name\":\"Mn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":246},\"start\":{\"modifier\":\"EXACT\",\"value\":246}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53041\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29035\",\"label\":\"2\",\"name\":\"Mn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":246},\"start\":{\"modifier\":\"EXACT\",\"value\":246}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53041\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29035\",\"label\":\"2\",\"name\":\"Mn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":278},\"start\":{\"modifier\":\"EXACT\",\"value\":278}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53041\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29035\",\"label\":\"2\",\"name\":\"Mn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":327},\"start\":{\"modifier\":\"EXACT\",\"value\":327}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53041\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29035\",\"label\":\"2\",\"name\":\"Mn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":403},\"start\":{\"modifier\":\"EXACT\",\"value\":403}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Chaudhuri M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11290414\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0378-1119(01)00367-5\"}],\"citationType\":\"journal article\",\"firstPage\":\"1\",\"id\":\"11290414\",\"journal\":\"Gene\",\"lastPage\":\"13\",\"publicationDate\":\"2001\",\"title\":\"Cloning and characterization of a novel serine/threonine protein phosphatase type 5 from Trypanosoma brucei.\",\"volume\":\"266\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"LUMP 1026\"}],\"referenceNumber\":2,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H1",
  "excerpt": "ID   PPP5_TRYB2              Reviewed;         472 AA.\nAC   Q388N2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-NOV-2005, sequence version 1.\nDT   28-JAN-2026, entry version 114.\nDE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000305};\nDE            Short=PPT {ECO:0000305};\nDE            EC=3.1.3.16 {ECO:0000305|PubMed:11290414};\nDE   AltName: Full=TbPP5 {ECO:0000303|PubMed:11290414};\nGN   Name=PPT1 {ECO:0000305};\nGN   ORFNames=Tb10.05.0110 {ECO:0000312|EMBL:EAN78738.1};\nOS   Trypanosoma brucei brucei (strain 927/4 GUTat10.1).\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Trypanosoma.\nOX   NCBI_TaxID=185431 {ECO:0000312|Proteomes:UP000008524};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   SUBCELLULAR LOCATION.\nRC   STRAIN=LUMP 1026 {ECO:0000303|PubMed:11290414};\nRX   PubMed=11290414; DOI=10.1016/s0378-1119(01)00367-5;\nRA   Chaudhuri M.;\nRT   \"Cloning and characterization of a novel serine/threonine protein\nRT   phosphatase type 5 from Trypanosoma brucei.\";\nRL   Gene 266:1-13(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        279\nFT                   /note=\"Proton donor/acceptor\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PIRSR:PIRSR033096-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 157-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         217\nFT                   /ligand=\"Mn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29035\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P53041\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-164",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         219\nFT                   /ligand=\"Mn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29035\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P53041\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 165-169",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         246\nFT                   /ligand=\"Mn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29035\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P53041\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 170-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         246\nFT                   /ligand=\"Mn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29035\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P53041\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 175-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         278\nFT                   /ligand=\"Mn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29035\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P53041\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 180-184",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         327\nFT                   /ligand=\"Mn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29035\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P53041\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 185-189",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         403\nFT                   /ligand=\"Mn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29035\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P53041\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 190-194",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 121. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
