# EC_number_0155

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0155.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 3.1.3.16

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
A. 3.1.3.112
B. 5.3.1.8
C. 2.7.7.80
D. 3.1.3.16
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

> The matched-sequence UniProt entry assigns EC 3.1.3.16 and describes dephosphorylation of protein serine and threonine residues. The annotation cites a characterization paper; this supports D, though the excerpts do not independently establish the experiments' details.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a protein phosphatase 5: an N-terminal alpha-helical repeat region followed by a conserved metal-dependent protein phosphatase catalytic domain, including characteristic catalytic-domain motifs. Family knowledge links this architecture to serine/threonine protein dephosphorylation, corresponding to EC 3.1.3.16 (D), rather than the isomerase or nucleotide-transferase alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the phosphatase family from transferable sequence and domain patterns meaningfully distinguishes D among these choices. This is a family-level inference, not proof of every substrate or activity detail for this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives classify substantially different reaction types, and the sequence-family inference favors only the protein serine/threonine phosphatase EC number.


### Important caveats

- The supporting database annotation is literature-cited and applies to a sequence-matched entry; the supplied excerpts do not provide the primary experimental data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a protein phosphatase 5: an N-terminal alpha-helical repeat region followed by a conserved metal-dependent protein phosphatase catalytic domain, including characteristic catalytic-domain motifs. Family knowledge links this architecture to serine/threonine protein dephosphorylation, corresponding to EC 3.1.3.16 (D), rather than the isomerase or nucleotide-transferase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the phosphatase family from transferable sequence and domain patterns meaningfully distinguishes D among these choices. This is a family-level inference, not proof of every substrate or activity detail for this particular protein."
  },
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt entry assigns EC 3.1.3.16 and describes dephosphorylation of protein serine and threonine residues. The annotation cites a characterization paper; this supports D, though the excerpts do not independently establish the experiments' details."
  },
  "important_caveats": [
    "The supporting database annotation is literature-cited and applies to a sequence-matched entry; the supplied excerpts do not provide the primary experimental data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives classify substantially different reaction types, and the sequence-family inference favors only the protein serine/threonine phosphatase EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt entry assigns EC 3.1.3.16 and describes dephosphorylation of protein serine and threonine residues. The annotation cites a characterization paper; this supports D, though the excerpts do not independently establish the experiments' details.",
    "evidence_ids": ["C4", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a protein phosphatase 5: an N-terminal alpha-helical repeat region followed by a conserved metal-dependent protein phosphatase catalytic domain, including characteristic catalytic-domain motifs. Family knowledge links this architecture to serine/threonine protein dephosphorylation, corresponding to EC 3.1.3.16 (D), rather than the isomerase or nucleotide-transferase alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the phosphatase family from transferable sequence and domain patterns meaningfully distinguishes D among these choices. This is a family-level inference, not proof of every substrate or activity detail for this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives classify substantially different reaction types, and the sequence-family inference favors only the protein serine/threonine phosphatase EC number."
  },
  "important_caveats": [
    "The supporting database annotation is literature-cited and applies to a sequence-matched entry; the supplied excerpts do not provide the primary experimental data."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q388N2 (sequence matched exactly) annotates this protein as Serine/threonine-protein phosphatase T (TbPP5) with EC 3.1.3.16, supported by experimental evidence (ECO:0000305, PubMed:11290414, Chaudhuri 2001). The catalytic activities listed are dephosphorylation of O-phospho-L-seryl-&#91;protein&#93; and O-phospho-L-threonyl-&#91;protein&#93;, both under EC 3.1.3.16. The evidence is from a primary characterization paper.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark GDxVHG-like motif of the PPP (phosphoprotein phosphatase) superfamily: 'GDFVDRGS' near the middle of the sequence and 'VVHGGL' further downstream, corresponding to the conserved GDxVHG catalytic motif. The PPP superfamily (PP1, PP2A, PP5, PP6, PP7) is specifically composed of serine/threonine protein phosphatases (EC 3.1.3.16) that use a binuclear metal center for catalysis. This distinguishes them from tyrosine phosphatases (which would correspond to EC 3.1.3.112), as PTP-family enzymes use a completely different cysteine-based catalytic mechanism with a CxxRxxG signature motif, which is absent here. Options B (EC 5.3.1.8, glucose-6-phosphate isomerase) and C (EC 2.7.7.80, nucleotidyltransferase) belong to entirely different EC classes (isomerase, transferase) and lack any phosphatase catalytic motifs. Thus, recognizing the PPP-family GDxVHG motif from general protein-family knowledge meaningfully distinguishes D (3.1.3.16) from A (3.1.3.112, tyrosine phosphatase) and eliminates B and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PPP superfamily GDxVHG motif is a well-established, transferable sequence signature shared across PP1, PP2A, PP5, and related Ser/Thr phosphatases. A knowledgeable model recognizing this motif can infer Ser/Thr phosphatase activity (EC 3.1.3.16) and exclude tyrosine phosphatases (different catalytic mechanism and motif), isomerases, and transferases without needing to recall this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (hydrolase, isomerase, transferase) and within hydrolases distinguish Ser/Thr vs. Tyr phosphatases. The PPP-family motif clearly points to Ser/Thr phosphatase, making D the uniquely defensible choice.


### Important caveats

- The GDxVHG motif in this sequence is a PP5-family variant (GDFVDRGS rather than the canonical GDxVHG of PP1/PP2A), but the key catalytic residues (G, D, V, H, G) are conserved, consistent with PPP superfamily membership.
- The evidence code ECO:0000305 indicates the EC assignment derives from the primary experimental paper (PubMed 11290414), not merely computational inference.
- EC 3.1.3.112 is a relatively obscure EC entry; its exact identity as a tyrosine phosphatase or other phosphatase subtype is assumed from general EC classification knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark GDxVHG-like motif of the PPP (phosphoprotein phosphatase) superfamily: 'GDFVDRGS' near the middle of the sequence and 'VVHGGL' further downstream, corresponding to the conserved GDxVHG catalytic motif. The PPP superfamily (PP1, PP2A, PP5, PP6, PP7) is specifically composed of serine/threonine protein phosphatases (EC 3.1.3.16) that use a binuclear metal center for catalysis. This distinguishes them from tyrosine phosphatases (which would correspond to EC 3.1.3.112), as PTP-family enzymes use a completely different cysteine-based catalytic mechanism with a CxxRxxG signature motif, which is absent here. Options B (EC 5.3.1.8, glucose-6-phosphate isomerase) and C (EC 2.7.7.80, nucleotidyltransferase) belong to entirely different EC classes (isomerase, transferase) and lack any phosphatase catalytic motifs. Thus, recognizing the PPP-family GDxVHG motif from general protein-family knowledge meaningfully distinguishes D (3.1.3.16) from A (3.1.3.112, tyrosine phosphatase) and eliminates B and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PPP superfamily GDxVHG motif is a well-established, transferable sequence signature shared across PP1, PP2A, PP5, and related Ser/Thr phosphatases. A knowledgeable model recognizing this motif can infer Ser/Thr phosphatase activity (EC 3.1.3.16) and exclude tyrosine phosphatases (different catalytic mechanism and motif), isomerases, and transferases without needing to recall this exact protein's database annotation."
  },
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q388N2 (sequence matched exactly) annotates this protein as Serine/threonine-protein phosphatase T (TbPP5) with EC 3.1.3.16, supported by experimental evidence (ECO:0000305, PubMed:11290414, Chaudhuri 2001). The catalytic activities listed are dephosphorylation of O-phospho-L-seryl-[protein] and O-phospho-L-threonyl-[protein], both under EC 3.1.3.16. The evidence is from a primary characterization paper."
  },
  "important_caveats": [
    "The GDxVHG motif in this sequence is a PP5-family variant (GDFVDRGS rather than the canonical GDxVHG of PP1/PP2A), but the key catalytic residues (G, D, V, H, G) are conserved, consistent with PPP superfamily membership.",
    "The evidence code ECO:0000305 indicates the EC assignment derives from the primary experimental paper (PubMed 11290414), not merely computational inference.",
    "EC 3.1.3.112 is a relatively obscure EC entry; its exact identity as a tyrosine phosphatase or other phosphatase subtype is assumed from general EC classification knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (hydrolase, isomerase, transferase) and within hydrolases distinguish Ser/Thr vs. Tyr phosphatases. The PPP-family motif clearly points to Ser/Thr phosphatase, making D the uniquely defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q388N2 (sequence matched exactly) annotates this protein as Serine/threonine-protein phosphatase T (TbPP5) with EC 3.1.3.16, supported by experimental evidence (ECO:0000305, PubMed:11290414, Chaudhuri 2001). The catalytic activities listed are dephosphorylation of O-phospho-L-seryl-[protein] and O-phospho-L-threonyl-[protein], both under EC 3.1.3.16. The evidence is from a primary characterization paper.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark GDxVHG-like motif of the PPP (phosphoprotein phosphatase) superfamily: 'GDFVDRGS' near the middle of the sequence and 'VVHGGL' further downstream, corresponding to the conserved GDxVHG catalytic motif. The PPP superfamily (PP1, PP2A, PP5, PP6, PP7) is specifically composed of serine/threonine protein phosphatases (EC 3.1.3.16) that use a binuclear metal center for catalysis. This distinguishes them from tyrosine phosphatases (which would correspond to EC 3.1.3.112), as PTP-family enzymes use a completely different cysteine-based catalytic mechanism with a CxxRxxG signature motif, which is absent here. Options B (EC 5.3.1.8, glucose-6-phosphate isomerase) and C (EC 2.7.7.80, nucleotidyltransferase) belong to entirely different EC classes (isomerase, transferase) and lack any phosphatase catalytic motifs. Thus, recognizing the PPP-family GDxVHG motif from general protein-family knowledge meaningfully distinguishes D (3.1.3.16) from A (3.1.3.112, tyrosine phosphatase) and eliminates B and C.",
    "missing_item_specific_fact": "",
    "reason": "The PPP superfamily GDxVHG motif is a well-established, transferable sequence signature shared across PP1, PP2A, PP5, and related Ser/Thr phosphatases. A knowledgeable model recognizing this motif can infer Ser/Thr phosphatase activity (EC 3.1.3.16) and exclude tyrosine phosphatases (different catalytic mechanism and motif), isomerases, and transferases without needing to recall this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (hydrolase, isomerase, transferase) and within hydrolases distinguish Ser/Thr vs. Tyr phosphatases. The PPP-family motif clearly points to Ser/Thr phosphatase, making D the uniquely defensible choice."
  },
  "important_caveats": [
    "The GDxVHG motif in this sequence is a PP5-family variant (GDFVDRGS rather than the canonical GDxVHG of PP1/PP2A), but the key catalytic residues (G, D, V, H, G) are conserved, consistent with PPP superfamily membership.",
    "The evidence code ECO:0000305 indicates the EC assignment derives from the primary experimental paper (PubMed 11290414), not merely computational inference.",
    "EC 3.1.3.112 is a relatively obscure EC entry; its exact identity as a tyrosine phosphatase or other phosphatase subtype is assumed from general EC classification knowledge."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:20630\"}}],\"reaction\":{\"ecNumber\":\"3.1.3.16\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"name\":\"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:20629\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9863\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11604\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:83421\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:47005\"}}],\"reaction\":{\"ecNumber\":\"3.1.3.16\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"name\":\"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:47004\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11605\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30013\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61977\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
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
  "excerpt": "DE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000305};\nDE            Short=PPT {ECO:0000305};\nDE            EC=3.1.3.16 {ECO:0000305|PubMed:11290414};\nDE   AltName: Full=TbPP5 {ECO:0000303|PubMed:11290414};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +\nCC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-\nCC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:83421; EC=3.1.3.16;\nCC         Evidence={ECO:0000305|PubMed:11290414};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;\nCC         Evidence={ECO:0000305|PubMed:11290414};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-58",
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
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +\nCC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-\nCC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:61977; EC=3.1.3.16;\nCC         Evidence={ECO:0000305|PubMed:11290414};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;\nCC         Evidence={ECO:0000305|PubMed:11290414};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 155. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
