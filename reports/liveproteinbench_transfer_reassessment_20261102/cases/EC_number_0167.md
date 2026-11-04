# EC_number_0167

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0167.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 1.5.1.32

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAISPEVEHPNKAFGFAARDPSGLLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSQDLENYCPDQILTYSATYTDGTTTYGGYSSLMVADEHFVIRWPENLPMDIGAPLLCAGITTYSPLRHFGLDKPGTHVGIVGLGGLGHVAVKFAKAFGAKVTVISTSEGKKQEAVEKLGADAFLVSRDPEQMQAAAATLDGIIDTVSAVHPILPLVNLLKSQGKLIMVGAPEKPIELPVFPLLLGRKIVAGSAIGGLKETQDMIDFAAKHNILPDVELIPMDYVNTAMERLLKADVKYRFVIDICNTLKSA

[Multiple Choices]
A. 1.5.1.32
B. 1.6.5.2
C. 1.14.18.1
D. 4.1.1.25
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

> The supplied sequence exactly matches the annotated protein sequence. Its UniProt annotation assigns EC 1.5.1.32 and cites experimental evidence for the catalytic activity and reaction, rather than relying only on a computational or similarity-based assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble, NAD(P)-dependent reductase, with features compatible with a zinc-containing medium-chain dehydrogenase/reductase-like protein. That provides a transferable basis for choosing A over the clearly different tyrosinase and decarboxylase options; its soluble reductase character also weighs against B, a quinone-linked NADH dehydrogenase. This supports the offered choice without establishing the exact substrate-specific EC number from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choices include substantially different enzyme types, and sequence-level enzyme-family and cofactor clues offer a meaningful way to distinguish the reductase answer. Exact reaction specificity would be harder to establish independently, but is not needed to distinguish A from these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported by the sequence-level reductase inference.


### Important caveats

- The experimental support is reported in the matched database annotation and cites publications; the primary studies were not independently reviewed here.
- The precise EC assignment is more specific than the family-level inference available from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble, NAD(P)-dependent reductase, with features compatible with a zinc-containing medium-chain dehydrogenase/reductase-like protein. That provides a transferable basis for choosing A over the clearly different tyrosinase and decarboxylase options; its soluble reductase character also weighs against B, a quinone-linked NADH dehydrogenase. This supports the offered choice without establishing the exact substrate-specific EC number from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choices include substantially different enzyme types, and sequence-level enzyme-family and cofactor clues offer a meaningful way to distinguish the reductase answer. Exact reaction specificity would be harder to establish independently, but is not needed to distinguish A from these alternatives."
  },
  "case_id": "EC_number_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein sequence. Its UniProt annotation assigns EC 1.5.1.32 and cites experimental evidence for the catalytic activity and reaction, rather than relying only on a computational or similarity-based assignment."
  },
  "important_caveats": [
    "The experimental support is reported in the matched database annotation and cites publications; the primary studies were not independently reviewed here.",
    "The precise EC assignment is more specific than the family-level inference available from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence-level reductase inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein sequence. Its UniProt annotation assigns EC 1.5.1.32 and cites experimental evidence for the catalytic activity and reaction, rather than relying only on a computational or similarity-based assignment.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble, NAD(P)-dependent reductase, with features compatible with a zinc-containing medium-chain dehydrogenase/reductase-like protein. That provides a transferable basis for choosing A over the clearly different tyrosinase and decarboxylase options; its soluble reductase character also weighs against B, a quinone-linked NADH dehydrogenase. This supports the offered choice without establishing the exact substrate-specific EC number from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "The choices include substantially different enzyme types, and sequence-level enzyme-family and cofactor clues offer a meaningful way to distinguish the reductase answer. Exact reaction specificity would be harder to establish independently, but is not needed to distinguish A from these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence-level reductase inference."
  },
  "important_caveats": [
    "The experimental support is reported in the matched database annotation and cites publications; the primary studies were not independently reviewed here.",
    "The precise EC assignment is more specific than the family-level inference available from sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ3 (sequence exactly matched, 360 aa) annotates EC 1.5.1.32 (Vomilenine reductase) with experimental evidence codes ECO:0000269 from two independent PubMed publications (11937349, 38212296). The catalytic reaction (2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+) is confirmed experimentally. The expected answer is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GIVGLGGLGH, a GxGxxG-type glycine-rich loop) characteristic of classic NAD(P)-dependent dehydrogenases/reductases. This immediately identifies the protein as an EC 1.x.x.x oxidoreductase, eliminating option D (EC 4.1.1.25, oxaloacetate decarboxylase, a lyase with no NAD-binding fold). At 360 amino acids with no multi-copper-binding domains (no HCH or HCH-type motifs), the protein is far too small and structurally wrong for a laccase (EC 1.14.18.1, typically 500–700 aa with four copper centers), eliminating option C. The presence of a canonical Rossmann NAD(P)-binding site without flavin-binding motifs or the structural architecture of NAD(P)H:quinone oxidoreductase (EC 1.6.5.2, a flavoprotein with FAD cofactor and distinct dimeric architecture) argues against option B. The remaining option A (EC 1.5.1.32, an NAD(P)-dependent reductase acting on a CH-NH group) is the only choice consistent with a ~360-aa Rossmann-fold NAD(P)-dependent reductase. A knowledgeable model can reach this conclusion using general structural biology of oxidoreductase families without knowing this specific protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold NAD-binding motif, protein size, and absence of copper or flavin cofactor motifs provide a concrete transferable inference that eliminates B, C, and D, leaving A as the only consistent choice. This relies on general knowledge of oxidoreductase structural classes (Rossmann fold, laccase copper domains, NQO1 flavoprotein architecture) learned from many other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span distinct enzyme classes (NAD-dependent reductase, flavoprotein quinone reductase, copper oxidase, lyase). The sequence features (Rossmann fold, 360 aa, no copper/flavin motifs) cleanly eliminate B, C, and D, leaving A as the unique defensible answer.


### Important caveats

- The specific 4th digit (32) of EC 1.5.1.32 cannot be deduced from sequence alone; however, since A is the only EC 1.5.1.x option among the four choices, the question is answerable by class-level elimination.
- The protein is annotated as a CAD2-homolog (EC 1.1.1.95 family), but its actual EC assignment is 1.5.1.32 (CH-NH group). EC 1.1.x.x is not among the choices, so this does not create ambiguity.
- The UniProt entry was first released in June 2025; the author's source snapshot is unknown but the sequence matches exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GIVGLGGLGH, a GxGxxG-type glycine-rich loop) characteristic of classic NAD(P)-dependent dehydrogenases/reductases. This immediately identifies the protein as an EC 1.x.x.x oxidoreductase, eliminating option D (EC 4.1.1.25, oxaloacetate decarboxylase, a lyase with no NAD-binding fold). At 360 amino acids with no multi-copper-binding domains (no HCH or HCH-type motifs), the protein is far too small and structurally wrong for a laccase (EC 1.14.18.1, typically 500–700 aa with four copper centers), eliminating option C. The presence of a canonical Rossmann NAD(P)-binding site without flavin-binding motifs or the structural architecture of NAD(P)H:quinone oxidoreductase (EC 1.6.5.2, a flavoprotein with FAD cofactor and distinct dimeric architecture) argues against option B. The remaining option A (EC 1.5.1.32, an NAD(P)-dependent reductase acting on a CH-NH group) is the only choice consistent with a ~360-aa Rossmann-fold NAD(P)-dependent reductase. A knowledgeable model can reach this conclusion using general structural biology of oxidoreductase families without knowing this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold NAD-binding motif, protein size, and absence of copper or flavin cofactor motifs provide a concrete transferable inference that eliminates B, C, and D, leaving A as the only consistent choice. This relies on general knowledge of oxidoreductase structural classes (Rossmann fold, laccase copper domains, NQO1 flavoprotein architecture) learned from many other proteins."
  },
  "case_id": "EC_number_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ3 (sequence exactly matched, 360 aa) annotates EC 1.5.1.32 (Vomilenine reductase) with experimental evidence codes ECO:0000269 from two independent PubMed publications (11937349, 38212296). The catalytic reaction (2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+) is confirmed experimentally. The expected answer is well-supported."
  },
  "important_caveats": [
    "The specific 4th digit (32) of EC 1.5.1.32 cannot be deduced from sequence alone; however, since A is the only EC 1.5.1.x option among the four choices, the question is answerable by class-level elimination.",
    "The protein is annotated as a CAD2-homolog (EC 1.1.1.95 family), but its actual EC assignment is 1.5.1.32 (CH-NH group). EC 1.1.x.x is not among the choices, so this does not create ambiguity.",
    "The UniProt entry was first released in June 2025; the author's source snapshot is unknown but the sequence matches exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span distinct enzyme classes (NAD-dependent reductase, flavoprotein quinone reductase, copper oxidase, lyase). The sequence features (Rossmann fold, 360 aa, no copper/flavin motifs) cleanly eliminate B, C, and D, leaving A as the unique defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ3 (sequence exactly matched, 360 aa) annotates EC 1.5.1.32 (Vomilenine reductase) with experimental evidence codes ECO:0000269 from two independent PubMed publications (11937349, 38212296). The catalytic reaction (2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+) is confirmed experimentally. The expected answer is well-supported.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GIVGLGGLGH, a GxGxxG-type glycine-rich loop) characteristic of classic NAD(P)-dependent dehydrogenases/reductases. This immediately identifies the protein as an EC 1.x.x.x oxidoreductase, eliminating option D (EC 4.1.1.25, oxaloacetate decarboxylase, a lyase with no NAD-binding fold). At 360 amino acids with no multi-copper-binding domains (no HCH or HCH-type motifs), the protein is far too small and structurally wrong for a laccase (EC 1.14.18.1, typically 500–700 aa with four copper centers), eliminating option C. The presence of a canonical Rossmann NAD(P)-binding site without flavin-binding motifs or the structural architecture of NAD(P)H:quinone oxidoreductase (EC 1.6.5.2, a flavoprotein with FAD cofactor and distinct dimeric architecture) argues against option B. The remaining option A (EC 1.5.1.32, an NAD(P)-dependent reductase acting on a CH-NH group) is the only choice consistent with a ~360-aa Rossmann-fold NAD(P)-dependent reductase. A knowledgeable model can reach this conclusion using general structural biology of oxidoreductase families without knowing this specific protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold NAD-binding motif, protein size, and absence of copper or flavin cofactor motifs provide a concrete transferable inference that eliminates B, C, and D, leaving A as the only consistent choice. This relies on general knowledge of oxidoreductase structural classes (Rossmann fold, laccase copper domains, NQO1 flavoprotein architecture) learned from many other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span distinct enzyme classes (NAD-dependent reductase, flavoprotein quinone reductase, copper oxidase, lyase). The sequence features (Rossmann fold, 360 aa, no copper/flavin motifs) cleanly eliminate B, C, and D, leaving A as the unique defensible answer."
  },
  "important_caveats": [
    "The specific 4th digit (32) of EC 1.5.1.32 cannot be deduced from sequence alone; however, since A is the only EC 1.5.1.x option among the four choices, the question is answerable by class-level elimination.",
    "The protein is annotated as a CAD2-homolog (EC 1.1.1.95 family), but its actual EC assignment is 1.5.1.32 (CH-NH group). EC 1.1.x.x is not among the choices, so this does not create ambiguity.",
    "The UniProt entry was first released in June 2025; the author's source snapshot is unknown but the sequence matches exactly."
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
  "benchmark_sequence_length": 360,
  "benchmark_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 360,
  "current_source_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXJ3",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "selected_historical_source_sequence_length": 360,
  "selected_historical_source_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "selected_historical_version": {
    "accession": "P0DXJ3",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "VOR1_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"CAD2-homolog protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Protein RR6-2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsRR6-2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11937349\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.32\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsVR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11937349\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:16411\"}}],\"reaction\":{\"ecNumber\":\"1.5.1.32\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11937349\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"name\":\"(2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:16409\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16408\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17372\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61927.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"von Schumann G.\",\"Gao S.\",\"Stoeckigt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11937349\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0968-0896(01)00435-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"1913\",\"id\":\"11937349\",\"journal\":\"Bioorg. Med. Chem.\",\"lastPage\":\"1918\",\"publicationDate\":\"2002\",\"title\":\"Vomilenine reductase--a novel enzyme catalyzing a crucial step in the biosynthesis of the therapeutically applied antiarrhythmic alkaloid ajmaline.\",\"volume\":\"10\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"ACTIVITY REGULATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   VOR1_RAUSE              Reviewed;         360 AA.\nAC   P0DXJ3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};\nDE            Short=RsVR {ECO:0000305|PubMed:38212296};\nDE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};\nDE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};\nGN   Name=VR {ECO:0000305|PubMed:38212296};\nGN   Synonyms=RR6-2 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};\nDE            Short=RsVR {ECO:0000305|PubMed:38212296};\nDE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};\nDE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WKU61927.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY,\nRP   ACTIVITY REGULATION, AND TISSUE SPECIFICITY.\nRX   PubMed=11937349; DOI=10.1016/s0968-0896(01)00435-7;\nRA   von Schumann G., Gao S., Stoeckigt J.;\nRT   \"Vomilenine reductase--a novel enzyme catalyzing a crucial step in the\nRT   biosynthesis of the therapeutically applied antiarrhythmic alkaloid\nRT   ajmaline.\";\nRL   Bioorg. Med. Chem. 10:1913-1918(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH +\nCC         H(+); Xref=Rhea:RHEA:16409, ChEBI:CHEBI:15378, ChEBI:CHEBI:16408,\nCC         ChEBI:CHEBI:17372, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349; EC=1.5.1.32;\nCC         Evidence={ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:16411;\nCC         Evidence={ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 167. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
