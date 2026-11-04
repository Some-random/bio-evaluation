# pathway_0027

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0027.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFSNLHLPLNPIDKVNQPPVYYLQVQDGLIICSGLCWTTAYILYIRQAYRDKSYGMPLVCLCANIAWEFLFGAAIPESAAQVVSFFPWFVIDIGIVYTTWKFGREQWKHAPLVAQNLGWILLGGIAGMLVMFWAFLKTYDNRYEAGFYLAWTDQIIVSTTSVAQLMSRNNTSGHSWGIWFTRWIGSVFAELIFVWRYWNYPESYPVAATHVTIFLFIVTEVADLTYPFVYASLDKKEKKKLK

[Multiple Choices]
A. Secondary metabolite biosynthesis
B. fatty acid beta-oxidation. .
C. Carbohydrate degradation
D. iron-sulfur cluster biosynthesis. .
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

> The sequence-matched UniProt record assigns this protein to secondary metabolite and terpenoid biosynthesis, citing a publication with experimental evidence code ECO:0000269. This supports choice A, though the excerpts do not independently establish the experiments' details.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 242-residue sequence is exceptionally hydrophobic and has a compact, multi-pass membrane-protein architecture. That pattern is consistent with the unusual membrane-associated terpene-cyclase family, whose transferable family-level function is terpene/secondary-metabolite biosynthesis. It is a better fit to A than to the typically soluble enzyme machinery for carbohydrate degradation or beta-oxidation, or iron-sulfur cluster assembly. This is a probabilistic family-pattern inference, not a pathway assignment proved by hydrophobicity alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence/architecture inference can meaningfully favor A among these choices without using the exact protein's recorded annotation. The sequence alone does not make that inference certain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative is comparably supported by the supplied sequence and offered choices.


### Important caveats

- The multi-pass architecture is not by itself diagnostic of terpene cyclase function.
- The organism and pathway annotation in the reviewer-only evidence were not part of the original input and are not used as transferable evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 242-residue sequence is exceptionally hydrophobic and has a compact, multi-pass membrane-protein architecture. That pattern is consistent with the unusual membrane-associated terpene-cyclase family, whose transferable family-level function is terpene/secondary-metabolite biosynthesis. It is a better fit to A than to the typically soluble enzyme machinery for carbohydrate degradation or beta-oxidation, or iron-sulfur cluster assembly. This is a probabilistic family-pattern inference, not a pathway assignment proved by hydrophobicity alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence/architecture inference can meaningfully favor A among these choices without using the exact protein's recorded annotation. The sequence alone does not make that inference certain."
  },
  "case_id": "pathway_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein to secondary metabolite and terpenoid biosynthesis, citing a publication with experimental evidence code ECO:0000269. This supports choice A, though the excerpts do not independently establish the experiments' details."
  },
  "important_caveats": [
    "The multi-pass architecture is not by itself diagnostic of terpene cyclase function.",
    "The organism and pathway annotation in the reviewer-only evidence were not part of the original input and are not used as transferable evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the supplied sequence and offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein to secondary metabolite and terpenoid biosynthesis, citing a publication with experimental evidence code ECO:0000269. This supports choice A, though the excerpts do not independently establish the experiments' details.",
    "evidence_ids": ["C5", "H3", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 242-residue sequence is exceptionally hydrophobic and has a compact, multi-pass membrane-protein architecture. That pattern is consistent with the unusual membrane-associated terpene-cyclase family, whose transferable family-level function is terpene/secondary-metabolite biosynthesis. It is a better fit to A than to the typically soluble enzyme machinery for carbohydrate degradation or beta-oxidation, or iron-sulfur cluster assembly. This is a probabilistic family-pattern inference, not a pathway assignment proved by hydrophobicity alone.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence/architecture inference can meaningfully favor A among these choices without using the exact protein's recorded annotation. The sequence alone does not make that inference certain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the supplied sequence and offered choices."
  },
  "important_caveats": [
    "The multi-pass architecture is not by itself diagnostic of terpene cyclase function.",
    "The organism and pathway annotation in the reviewer-only evidence were not part of the original input and are not used as transferable evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DY23 (Pyr4-family terpene cyclase mfmH from Annulohypoxylon moriforme) is explicitly annotated with PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269|PubMed:38404388). The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). Choice A is directly supported.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmark terpene cyclase features transferable from knowledge of other fungal terpene cyclases: (1) Extremely high tryptophan density (~12 W residues in 242 aa, ~5% vs ~1.3% average), characteristic of the aromatic-lined hydrophobic cavity in terpene cyclases (e.g., trichodiene synthase, 5-epi-aristolochene synthase). (2) An NSE-like motif variant ('NNT' near position 170) and degenerate DDxxD-like residues near the C-terminus ('VADL...SLD'), consistent with Pyr4-family terpene cyclase motif degeneracy. (3) Size (~242 aa) matches fungal terpene cyclases. Conversely, the sequence lacks FAD/NAD-binding motifs (GGxGxxG) expected for fatty acid beta-oxidation (B), lacks glycosidase catalytic motifs (DxWxH, etc.) for carbohydrate degradation (C), and lacks CxxC/CP motifs for iron-sulfur cluster biosynthesis (D). A model familiar with terpene cyclase signatures from other fungal proteins could reasonably select A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The aromatic residue density and terpene cyclase motif architecture are well-established, transferable features learned from numerous other terpene cyclases. The absence of motifs diagnostic for the three distractor options further narrows the choice. While exact motif positions are degenerate in the Pyr4 subfamily, the overall compositional signature (extreme W content, NSE variant, size) provides a credible probabilistic inference distinguishing A from B, C, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (fatty acid beta-oxidation, carbohydrate degradation, iron-sulfur cluster biosynthesis) require distinct catalytic motifs and domain architectures entirely absent from this sequence. Only secondary metabolite biosynthesis (via terpene cyclase) is consistent with the observed sequence features.


### Important caveats

- The Pyr4-family terpene cyclase motifs (NSE, DDxxD) are degenerate compared to classical terpene cyclases, making motif-based recognition less straightforward than for canonical examples.
- The extremely high tryptophan content is the strongest single transferable feature, but a model not trained on terpene cyclase composition statistics might miss this signal.
- The UniProt annotation is based on experimental characterization (ECO:0000269) from a 2024 paper, providing high confidence in the pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmark terpene cyclase features transferable from knowledge of other fungal terpene cyclases: (1) Extremely high tryptophan density (~12 W residues in 242 aa, ~5% vs ~1.3% average), characteristic of the aromatic-lined hydrophobic cavity in terpene cyclases (e.g., trichodiene synthase, 5-epi-aristolochene synthase). (2) An NSE-like motif variant ('NNT' near position 170) and degenerate DDxxD-like residues near the C-terminus ('VADL...SLD'), consistent with Pyr4-family terpene cyclase motif degeneracy. (3) Size (~242 aa) matches fungal terpene cyclases. Conversely, the sequence lacks FAD/NAD-binding motifs (GGxGxxG) expected for fatty acid beta-oxidation (B), lacks glycosidase catalytic motifs (DxWxH, etc.) for carbohydrate degradation (C), and lacks CxxC/CP motifs for iron-sulfur cluster biosynthesis (D). A model familiar with terpene cyclase signatures from other fungal proteins could reasonably select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The aromatic residue density and terpene cyclase motif architecture are well-established, transferable features learned from numerous other terpene cyclases. The absence of motifs diagnostic for the three distractor options further narrows the choice. While exact motif positions are degenerate in the Pyr4 subfamily, the overall compositional signature (extreme W content, NSE variant, size) provides a credible probabilistic inference distinguishing A from B, C, and D."
  },
  "case_id": "pathway_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DY23 (Pyr4-family terpene cyclase mfmH from Annulohypoxylon moriforme) is explicitly annotated with PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269|PubMed:38404388). The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). Choice A is directly supported."
  },
  "important_caveats": [
    "The Pyr4-family terpene cyclase motifs (NSE, DDxxD) are degenerate compared to classical terpene cyclases, making motif-based recognition less straightforward than for canonical examples.",
    "The extremely high tryptophan content is the strongest single transferable feature, but a model not trained on terpene cyclase composition statistics might miss this signal.",
    "The UniProt annotation is based on experimental characterization (ECO:0000269) from a 2024 paper, providing high confidence in the pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (fatty acid beta-oxidation, carbohydrate degradation, iron-sulfur cluster biosynthesis) require distinct catalytic motifs and domain architectures entirely absent from this sequence. Only secondary metabolite biosynthesis (via terpene cyclase) is consistent with the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DY23 (Pyr4-family terpene cyclase mfmH from Annulohypoxylon moriforme) is explicitly annotated with PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269|PubMed:38404388). The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). Choice A is directly supported.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmark terpene cyclase features transferable from knowledge of other fungal terpene cyclases: (1) Extremely high tryptophan density (~12 W residues in 242 aa, ~5% vs ~1.3% average), characteristic of the aromatic-lined hydrophobic cavity in terpene cyclases (e.g., trichodiene synthase, 5-epi-aristolochene synthase). (2) An NSE-like motif variant ('NNT' near position 170) and degenerate DDxxD-like residues near the C-terminus ('VADL...SLD'), consistent with Pyr4-family terpene cyclase motif degeneracy. (3) Size (~242 aa) matches fungal terpene cyclases. Conversely, the sequence lacks FAD/NAD-binding motifs (GGxGxxG) expected for fatty acid beta-oxidation (B), lacks glycosidase catalytic motifs (DxWxH, etc.) for carbohydrate degradation (C), and lacks CxxC/CP motifs for iron-sulfur cluster biosynthesis (D). A model familiar with terpene cyclase signatures from other fungal proteins could reasonably select A.",
    "missing_item_specific_fact": "",
    "reason": "The aromatic residue density and terpene cyclase motif architecture are well-established, transferable features learned from numerous other terpene cyclases. The absence of motifs diagnostic for the three distractor options further narrows the choice. While exact motif positions are degenerate in the Pyr4 subfamily, the overall compositional signature (extreme W content, NSE variant, size) provides a credible probabilistic inference distinguishing A from B, C, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (fatty acid beta-oxidation, carbohydrate degradation, iron-sulfur cluster biosynthesis) require distinct catalytic motifs and domain architectures entirely absent from this sequence. Only secondary metabolite biosynthesis (via terpene cyclase) is consistent with the observed sequence features."
  },
  "important_caveats": [
    "The Pyr4-family terpene cyclase motifs (NSE, DDxxD) are degenerate compared to classical terpene cyclases, making motif-based recognition less straightforward than for canonical examples.",
    "The extremely high tryptophan content is the strongest single transferable feature, but a model not trained on terpene cyclase composition statistics might miss this signal.",
    "The UniProt annotation is based on experimental characterization (ECO:0000269) from a 2024 paper, providing high confidence in the pathway assignment."
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
  "benchmark_sequence_length": 242,
  "benchmark_sequence_sha256": "21b53f15e3037e7e885ad6e3d7ba7c3588e5eb84f99f8a961e2047b78215bf8f",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 242,
  "current_source_sequence_sha256": "21b53f15e3037e7e885ad6e3d7ba7c3588e5eb84f99f8a961e2047b78215bf8f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DY23",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d",
  "selected_historical_source_sequence_length": 242,
  "selected_historical_source_sequence_sha256": "21b53f15e3037e7e885ad6e3d7ba7c3588e5eb84f99f8a961e2047b78215bf8f",
  "selected_historical_version": {
    "accession": "P0DY23",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFMH_ANNMO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DY23\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:06.355655+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY23.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:06.355655+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY23.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Xylariomycetidae\",\"Xylariales\",\"Hypoxylaceae\",\"Annulohypoxylon\"],\"scientificName\":\"Annulohypoxylon moriforme\",\"synonyms\":[\"Hypoxylon moriforme\"],\"taxonId\":326622}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:06.355655+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY23.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"11'-O-desmethylfendlerol biosynthesis cluster protein H\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Pyr4-family terpene cyclase mfmH\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:06.355655+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY23.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:06.355655+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY23.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan D.\",\"Matsuda Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38404388\"},{\"database\":\"DOI\",\"id\":\"10.1039/d3sc06001b\"}],\"citationType\":\"journal article\",\"firstPage\":\"3011\",\"id\":\"38404388\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"3017\",\"publicationDate\":\"2024\",\"title\":\"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CBS 123579\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:06.355655+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY23.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   MFMH_ANNMO              Reviewed;         242 AA.\nAC   P0DY23;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Pyr4-family terpene cyclase mfmH {ECO:0000303|PubMed:38404388};\nDE            EC=4.2.3.- {ECO:0000269|PubMed:38404388};\nDE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein H {ECO:0000303|PubMed:38404388};\nGN   Name=mfmH {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_30178;\nOS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.\nOX   NCBI_TaxID=326622;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:08.630908+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d",
  "url": "https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   STRAIN=CBS 123579;\nRX   PubMed=38404388; DOI=10.1039/d3sc06001b;\nRA   Yan D., Matsuda Y.;\nRT   \"Global genome mining-driven discovery of an unusual biosynthetic logic for\nRT   fungal polyketide-terpenoid hybrids.\";\nRL   Chem. Sci. 15:3011-3017(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:08.630908+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d",
  "url": "https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:38404388}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:08.630908+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d",
  "url": "https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
