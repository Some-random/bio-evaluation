# pathway_0149

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0149.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Cofactor biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MHYLDNLLLNTDSYKASHWLQYPPGTDASFFYVESRGGVYDQTAFFGLQSILKEAINRPVTHADIDDAKALLAAHGEPFNEAGWRDIVDRLGGQLPIRIRAVPEGCVVPTHNVLMTIESTDAKAFWVPSYLETLLLRVWYPVTVATVSWQVKQIVRDFLQRTSDDPEGQLPFKLHDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHTPVAGYSIPAAEHSTITSWGREREVDAYRNMLTQFARPGAIVAVVSDSYDIYRAIREHWGTTLREEIIASGATVVIRPDSGDPVDVVEQCLLLLDEAFGHQVNGKGYKVLNHVRVIQGDGINPQSLRAILERITAAGYAADNVAFGMGGALLQKVDRDTQKFALKCSAVRVDGAWIDVYKDPITDQGKQSKRGRLTLLRDRATGQYRSALLDEVATHAGDSDDALVTVWENGQMLREWTLEQVRAHADAARL

[Multiple Choices]
A. Antifungal biosynthesis. .
B. protein ubiquitination. .
C. IMP biosynthesis via de novo pathway
D. Cofactor biosynthesis
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies the protein as nicotinamide phosphoribosyltransferase and places it in NAD(+) cofactor biosynthesis via the nicotinamide salvage pathway. The pathway annotation cites experimental evidence, although the underlying study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 468-residue sequence is consistent with the NAMPT family. Transferable knowledge of this enzyme family connects nicotinamide phosphoribosyltransferase activity to NAD biosynthesis, a cofactor-biosynthesis pathway. That distinguishes D from protein ubiquitination and antifungal biosynthesis; it also distinguishes D from de novo IMP biosynthesis, which is a different nucleotide-synthesis route.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition from the sequence, together with the known role of NAMPT homologs in NAD cofactor biosynthesis, provides a meaningful basis for choosing among these options without recalling this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices distinguish cofactor biosynthesis from the other listed pathways, and the supported NAMPT-family inference points to D.


### Important caveats

- The source annotation is reviewer-only evidence, not an original input; the answerability judgment relies on transferable NAMPT-family knowledge.
- The cited experimental basis is represented in the supplied annotation, but the primary study was not independently evaluated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 468-residue sequence is consistent with the NAMPT family. Transferable knowledge of this enzyme family connects nicotinamide phosphoribosyltransferase activity to NAD biosynthesis, a cofactor-biosynthesis pathway. That distinguishes D from protein ubiquitination and antifungal biosynthesis; it also distinguishes D from de novo IMP biosynthesis, which is a different nucleotide-synthesis route.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition from the sequence, together with the known role of NAMPT homologs in NAD cofactor biosynthesis, provides a meaningful basis for choosing among these options without recalling this exact protein's database record."
  },
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as nicotinamide phosphoribosyltransferase and places it in NAD(+) cofactor biosynthesis via the nicotinamide salvage pathway. The pathway annotation cites experimental evidence, although the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The source annotation is reviewer-only evidence, not an original input; the answerability judgment relies on transferable NAMPT-family knowledge.",
    "The cited experimental basis is represented in the supplied annotation, but the primary study was not independently evaluated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish cofactor biosynthesis from the other listed pathways, and the supported NAMPT-family inference points to D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as nicotinamide phosphoribosyltransferase and places it in NAD(+) cofactor biosynthesis via the nicotinamide salvage pathway. The pathway annotation cites experimental evidence, although the underlying study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 468-residue sequence is consistent with the NAMPT family. Transferable knowledge of this enzyme family connects nicotinamide phosphoribosyltransferase activity to NAD biosynthesis, a cofactor-biosynthesis pathway. That distinguishes D from protein ubiquitination and antifungal biosynthesis; it also distinguishes D from de novo IMP biosynthesis, which is a different nucleotide-synthesis route.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition from the sequence, together with the known role of NAMPT homologs in NAD cofactor biosynthesis, provides a meaningful basis for choosing among these options without recalling this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish cofactor biosynthesis from the other listed pathways, and the supported NAMPT-family inference points to D."
  },
  "important_caveats": [
    "The source annotation is reviewer-only evidence, not an original input; the answerability judgment relies on transferable NAMPT-family knowledge.",
    "The cited experimental basis is represented in the supplied annotation, but the primary study was not independently evaluated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0H2X5R2) annotates this protein as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) with pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1,' supported by experimental evidence (ECO:0000269, PubMed:38429435) including X-ray crystallography and functional assays. The answer D (Cofactor biosynthesis) is directly confirmed.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'GEP' motif (around residue 70: 'AKALLAAHGEPFNEAGWRDIVDRLGG') and the 'GWR' motif immediately following, which are hallmark signatures of NAMPT identified across human, yeast, and bacterial NAMPT proteins. The overall ~468 aa length and PRTase (phosphoribosyltransferase) fold architecture (central β-sheet flanked by α-helices, with the characteristic GEP-GWR catalytic region) are consistent with NAMPT. The PRTase fold with GEP motif is associated with nucleotide/cofactor salvage enzymes (NAMPT, HGPRT, APRT, UPP, TrpD), not with de novo purine biosynthesis enzymes (PurF uses a glutamine amidotransferase fold; PurL/PurM/PurH use formyltransferase or synthetase folds). The sequence lacks RING/HECT/U-box motifs (ruling out ubiquitination), lacks polyketide synthase or NRPS domains (ruling out antifungal biosynthesis), and lacks the glutamine amidotransferase Cys-His catalytic dyad and large multi-domain architecture of Pur enzymes (ruling out IMP de novo biosynthesis). The GEP motif specifically identifies NAMPT among PRTases, pointing to NAD+ biosynthesis, which UniProt classifies under 'Cofactor biosynthesis.'


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GEP-GWR motif and PRTase fold are well-known transferable features from human NAMPT (P30431), yeast Pnc1, and other characterized NAMPT orthologs. A model familiar with these motifs can recognize the protein as a NAMPT-family phosphoribosyltransferase and, knowing that NAMPT catalyzes the rate-limiting step of NAD+ salvage (classified under cofactor biosynthesis), distinguish D from the other three options. The absence of purine-pathway enzyme features, ubiquitin-ligase domains, and antifungal biosynthetic machinery further eliminates alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct pathway categories with no overlap. The GEP motif and PRTase fold unambiguously point to NAMPT/NAD+ biosynthesis (cofactor biosynthesis) rather than ubiquitination, antifungal biosynthesis, or de novo IMP biosynthesis.


### Important caveats

- The N-terminal ~90 residues of this sequence are identical to human NAMPT (P30431), which is unusual for a bacterial protein; this may reflect extremely high conservation in this region or a database annotation artifact. The UniProt entry was only made public in February 2025.
- The reviewer-only evidence confirms the annotation via a 2024 crystallographic study (PDB 7YQO-7YQR, 8IGZ) with experimental evidence codes, but this information was not available to the evaluated model.
- The PRTase fold is shared among several enzyme families; the GEP motif is the key discriminator for NAMPT specifically within that fold.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GEP' motif (around residue 70: 'AKALLAAHGEPFNEAGWRDIVDRLGG') and the 'GWR' motif immediately following, which are hallmark signatures of NAMPT identified across human, yeast, and bacterial NAMPT proteins. The overall ~468 aa length and PRTase (phosphoribosyltransferase) fold architecture (central β-sheet flanked by α-helices, with the characteristic GEP-GWR catalytic region) are consistent with NAMPT. The PRTase fold with GEP motif is associated with nucleotide/cofactor salvage enzymes (NAMPT, HGPRT, APRT, UPP, TrpD), not with de novo purine biosynthesis enzymes (PurF uses a glutamine amidotransferase fold; PurL/PurM/PurH use formyltransferase or synthetase folds). The sequence lacks RING/HECT/U-box motifs (ruling out ubiquitination), lacks polyketide synthase or NRPS domains (ruling out antifungal biosynthesis), and lacks the glutamine amidotransferase Cys-His catalytic dyad and large multi-domain architecture of Pur enzymes (ruling out IMP de novo biosynthesis). The GEP motif specifically identifies NAMPT among PRTases, pointing to NAD+ biosynthesis, which UniProt classifies under 'Cofactor biosynthesis.'",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GEP-GWR motif and PRTase fold are well-known transferable features from human NAMPT (P30431), yeast Pnc1, and other characterized NAMPT orthologs. A model familiar with these motifs can recognize the protein as a NAMPT-family phosphoribosyltransferase and, knowing that NAMPT catalyzes the rate-limiting step of NAD+ salvage (classified under cofactor biosynthesis), distinguish D from the other three options. The absence of purine-pathway enzyme features, ubiquitin-ligase domains, and antifungal biosynthetic machinery further eliminates alternatives."
  },
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0H2X5R2) annotates this protein as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) with pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1,' supported by experimental evidence (ECO:0000269, PubMed:38429435) including X-ray crystallography and functional assays. The answer D (Cofactor biosynthesis) is directly confirmed."
  },
  "important_caveats": [
    "The N-terminal ~90 residues of this sequence are identical to human NAMPT (P30431), which is unusual for a bacterial protein; this may reflect extremely high conservation in this region or a database annotation artifact. The UniProt entry was only made public in February 2025.",
    "The reviewer-only evidence confirms the annotation via a 2024 crystallographic study (PDB 7YQO-7YQR, 8IGZ) with experimental evidence codes, but this information was not available to the evaluated model.",
    "The PRTase fold is shared among several enzyme families; the GEP motif is the key discriminator for NAMPT specifically within that fold."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct pathway categories with no overlap. The GEP motif and PRTase fold unambiguously point to NAMPT/NAD+ biosynthesis (cofactor biosynthesis) rather than ubiquitination, antifungal biosynthesis, or de novo IMP biosynthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0H2X5R2) annotates this protein as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) with pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1,' supported by experimental evidence (ECO:0000269, PubMed:38429435) including X-ray crystallography and functional assays. The answer D (Cofactor biosynthesis) is directly confirmed.",
    "evidence_ids": ["C5", "C4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GEP' motif (around residue 70: 'AKALLAAHGEPFNEAGWRDIVDRLGG') and the 'GWR' motif immediately following, which are hallmark signatures of NAMPT identified across human, yeast, and bacterial NAMPT proteins. The overall ~468 aa length and PRTase (phosphoribosyltransferase) fold architecture (central β-sheet flanked by α-helices, with the characteristic GEP-GWR catalytic region) are consistent with NAMPT. The PRTase fold with GEP motif is associated with nucleotide/cofactor salvage enzymes (NAMPT, HGPRT, APRT, UPP, TrpD), not with de novo purine biosynthesis enzymes (PurF uses a glutamine amidotransferase fold; PurL/PurM/PurH use formyltransferase or synthetase folds). The sequence lacks RING/HECT/U-box motifs (ruling out ubiquitination), lacks polyketide synthase or NRPS domains (ruling out antifungal biosynthesis), and lacks the glutamine amidotransferase Cys-His catalytic dyad and large multi-domain architecture of Pur enzymes (ruling out IMP de novo biosynthesis). The GEP motif specifically identifies NAMPT among PRTases, pointing to NAD+ biosynthesis, which UniProt classifies under 'Cofactor biosynthesis.'",
    "missing_item_specific_fact": "",
    "reason": "The GEP-GWR motif and PRTase fold are well-known transferable features from human NAMPT (P30431), yeast Pnc1, and other characterized NAMPT orthologs. A model familiar with these motifs can recognize the protein as a NAMPT-family phosphoribosyltransferase and, knowing that NAMPT catalyzes the rate-limiting step of NAD+ salvage (classified under cofactor biosynthesis), distinguish D from the other three options. The absence of purine-pathway enzyme features, ubiquitin-ligase domains, and antifungal biosynthetic machinery further eliminates alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct pathway categories with no overlap. The GEP motif and PRTase fold unambiguously point to NAMPT/NAD+ biosynthesis (cofactor biosynthesis) rather than ubiquitination, antifungal biosynthesis, or de novo IMP biosynthesis."
  },
  "important_caveats": [
    "The N-terminal ~90 residues of this sequence are identical to human NAMPT (P30431), which is unusual for a bacterial protein; this may reflect extremely high conservation in this region or a database annotation artifact. The UniProt entry was only made public in February 2025.",
    "The reviewer-only evidence confirms the annotation via a 2024 crystallographic study (PDB 7YQO-7YQR, 8IGZ) with experimental evidence codes, but this information was not available to the evaluated model.",
    "The PRTase fold is shared among several enzyme families; the GEP motif is the key discriminator for NAMPT specifically within that fold."
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
  "benchmark_sequence_length": 468,
  "benchmark_sequence_sha256": "c9ee286b6dffa262b90f67a1a22d051bc2b6beed528f7f4ef5e12e3af3684da3",
  "current_entry_audit": {
    "entryVersion": 47,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-09-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 468,
  "current_source_sequence_sha256": "c9ee286b6dffa262b90f67a1a22d051bc2b6beed528f7f4ef5e12e3af3684da3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 45,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0H2X5R2",
  "selected_historical_entry_version": 45,
  "selected_historical_record_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "selected_historical_source_sequence_length": 468,
  "selected_historical_source_sequence_sha256": "c9ee286b6dffa262b90f67a1a22d051bc2b6beed528f7f4ef5e12e3af3684da3",
  "selected_historical_version": {
    "accession": "A0A0H2X5R2",
    "database": "Swiss-Prot",
    "entryVersion": 45,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NAMPT_XANC8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0H2X5R2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":47,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-09-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Lysobacterales\",\"Lysobacteraceae\",\"Xanthomonas\"],\"scientificName\":\"Xanthomonas campestris pv. campestris (strain 8004)\",\"taxonId\":314565}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"2.4.2.12\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"Nicotinamide phosphoribosyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NAM phosphoribosyltransferase\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NAMPT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Xu G.\",\"Ma J.\",\"Fang Q.\",\"Peng Q.\",\"Jiao X.\",\"Hu W.\",\"Zhao Q.\",\"Kong Y.\",\"Liu F.\",\"Shi X.\",\"Tang D.J.\",\"Tang J.L.\",\"Ming Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38429435\"},{\"database\":\"DOI\",\"id\":\"10.1038/s42003-024-05921-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"255\",\"id\":\"38429435\",\"journal\":\"Commun. Biol.\",\"lastPage\":\"255\",\"publicationDate\":\"2024\",\"title\":\"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.\",\"volume\":\"7\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQO\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQP\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQQ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQR\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8IGZ\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"8004\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) OF APOENZYME; WILD-TYPE IN COMPLEXES WITH NICOTINAMIDE AND BETA-NICOTINAMIDE D-RIBONUCLEOTIDE AND QUADRUPLE MUTANT PHE-175/PHE-224/PHE-291/PHE-332\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\",\"DOMAIN\",\"PHOSPHORYLATION AT HIS-229\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-175; ARG-180; ASP-203; ILE-224; HIS-229; VAL-291; ARG-293; ILE-332; ASP-335 AND ARG-373\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H1",
  "excerpt": "ID   NAMPT_XANC8             Reviewed;         468 AA.\nAC   A0A0H2X5R2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-SEP-2015, sequence version 1.\nDT   28-JAN-2026, entry version 45.\nDE   RecName: Full=Nicotinamide phosphoribosyltransferase {ECO:0000303|PubMed:38429435};\nDE            Short=NAM phosphoribosyltransferase {ECO:0000303|PubMed:38429435};\nDE            Short=NAMPT {ECO:0000303|PubMed:38429435};\nDE            EC=2.4.2.12 {ECO:0000269|PubMed:38429435};\nGN   OrderedLocusNames=XC_0719 {ECO:0000312|EMBL:AAY47797.1};\nOS   Xanthomonas campestris pv. campestris (strain 8004).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Lysobacterales; Lysobacteraceae; Xanthomonas.\nOX   NCBI_TaxID=314565;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7YQO, ECO:0007744|PDB:7YQP, ECO:0007744|PDB:7YQQ, ECO:0007744|PDB:7YQR, ECO:0007744|PDB:8IGZ}\nRP   X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) OF APOENZYME; WILD-TYPE IN COMPLEXES\nRP   WITH NICOTINAMIDE AND BETA-NICOTINAMIDE D-RIBONUCLEOTIDE AND QUADRUPLE\nRP   MUTANT PHE-175/PHE-224/PHE-291/PHE-332, FUNCTION, CATALYTIC ACTIVITY,\nRP   ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBUNIT,\nRP   DOMAIN, PHOSPHORYLATION AT HIS-229, DISRUPTION PHENOTYPE, AND MUTAGENESIS\nRP   OF HIS-175; ARG-180; ASP-203; ILE-224; HIS-229; VAL-291; ARG-293; ILE-332;\nRP   ASP-335 AND ARG-373.\nRC   STRAIN=8004;\nRX   PubMed=38429435; DOI=10.1038/s42003-024-05921-3;\nRA   Xu G., Ma J., Fang Q., Peng Q., Jiao X., Hu W., Zhao Q., Kong Y., Liu F.,\nRA   Shi X., Tang D.J., Tang J.L., Ming Z.;\nRT   \"Structural insights into Xanthomonas campestris pv. campestris NAD+\nRT   biosynthesis via the NAM salvage pathway.\";\nRL   Commun. Biol. 7:255-255(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-\nCC       ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and\nCC       nicotinamide: step 1/1. {ECO:0000269|PubMed:38429435}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
