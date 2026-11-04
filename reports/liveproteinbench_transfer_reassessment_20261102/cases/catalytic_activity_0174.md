# catalytic_activity_0174

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0174.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATPSKKRCGVLGATGAVGTRFILLLSQHPLLELVAVGASDRSSGKKYRDAVRWKQSAPMPAKVADLTVRCCDPAEFSDCDIIFSGLDPDAAGEIEMAFLKANFAVFSNAKNYRLDPMVPLVVPLVNAGHIDVIPAQRKHFGLDKGMLVCNSNCAVVGLVVPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPYIPGEEGKISSEARKILGDLNSDLAGFSDQKPLQISVACNRVPVLDGHTVCASLRFVNRPPPTASQVREALREYKPEVQTLGCPSAPKMSIHVMDEVDRPQPRLDRETEGGYACTVGRIREDDSDVFDIQFVALSHNTVLGASGSSILNAESAILKGFV

[Multiple Choices]
A. L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)
B. L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)
C. 2-hydroxyspheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. a 14alpha-methyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence matches the source record, which annotates it as aspartate-semialdehyde dehydrogenase and gives the reaction in choice B. The catalytic-activity annotation carries experimental evidence code ECO:0000269 citing a publication; this supports the key, though the cited paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 362-residue sequence has an N-terminal glycine-rich dinucleotide-binding-like region and is consistent with the soluble NAD(P)-dependent dehydrogenase family that includes aspartate-semialdehyde dehydrogenases. Family-level recognition supports the NADP-dependent substrate transformation in B. The other choices describe distinct activities—a tyrosine/ATP reaction, carotenoid hydroxylation, or steroid hydroxylation—and do not fit this sequence-family pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable family-level inference from sequence features meaningfully distinguishes B from the offered alternatives; the exact target's database annotation is not necessary to make that choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe clearly different reactions, and the sequence-family inference supports B over the alternatives.


### Important caveats

- The source annotation cites experimental evidence, but the primary publication was not independently assessed.
- Sequence-family recognition supports the choice without proving every detail of the exact protein's catalytic behavior.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 362-residue sequence has an N-terminal glycine-rich dinucleotide-binding-like region and is consistent with the soluble NAD(P)-dependent dehydrogenase family that includes aspartate-semialdehyde dehydrogenases. Family-level recognition supports the NADP-dependent substrate transformation in B. The other choices describe distinct activities—a tyrosine/ATP reaction, carotenoid hydroxylation, or steroid hydroxylation—and do not fit this sequence-family pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level inference from sequence features meaningfully distinguishes B from the offered alternatives; the exact target's database annotation is not necessary to make that choice."
  },
  "case_id": "catalytic_activity_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the source record, which annotates it as aspartate-semialdehyde dehydrogenase and gives the reaction in choice B. The catalytic-activity annotation carries experimental evidence code ECO:0000269 citing a publication; this supports the key, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The source annotation cites experimental evidence, but the primary publication was not independently assessed.",
    "Sequence-family recognition supports the choice without proving every detail of the exact protein's catalytic behavior."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe clearly different reactions, and the sequence-family inference supports B over the alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the source record, which annotates it as aspartate-semialdehyde dehydrogenase and gives the reaction in choice B. The catalytic-activity annotation carries experimental evidence code ECO:0000269 citing a publication; this supports the key, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 362-residue sequence has an N-terminal glycine-rich dinucleotide-binding-like region and is consistent with the soluble NAD(P)-dependent dehydrogenase family that includes aspartate-semialdehyde dehydrogenases. Family-level recognition supports the NADP-dependent substrate transformation in B. The other choices describe distinct activities—a tyrosine/ATP reaction, carotenoid hydroxylation, or steroid hydroxylation—and do not fit this sequence-family pattern.",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level inference from sequence features meaningfully distinguishes B from the offered alternatives; the exact target's database annotation is not necessary to make that choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe clearly different reactions, and the sequence-family inference supports B over the alternatives."
  },
  "important_caveats": [
    "The source annotation cites experimental evidence, but the primary publication was not independently assessed.",
    "Sequence-family recognition supports the choice without proving every detail of the exact protein's catalytic behavior."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A080WMA9 (sequence matched) annotates this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from Trichophyton rubrum, with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)' supported by experimental evidence (ECO:0000269, PubMed:26869335, X-ray crystallography at 2.55 Å in complex with NADP+). This exactly matches option B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD(P)-binding motif near the N-terminus (GVLGATGAVGTR, a GxxGxxG-like pattern), indicating an NAD(P)-dependent dehydrogenase/oxidoreductase. This immediately disfavors options C (ferredoxin-dependent monooxygenase requiring &#91;2Fe-2S&#93; clusters and O2) and D (cytochrome P450 requiring a heme-binding FxxGxxxCxxxG motif, neither of which is present). Option A (tyrosinal reductase/aminotransferase) would require a PLP-binding lysine or a completely different fold architecture, also absent. The remaining candidate B (aspartate-semialdehyde dehydrogenase, EC 1.2.1.11) is a well-known NADP+-dependent dehydrogenase with a catalytic cysteine forming a thioacyl intermediate. The sequence contains multiple cysteines in positions consistent with the ASADH catalytic Cys-Asp dyad (e.g., in 'GHTVCASLRFV' and 'CNSNCAVVGLVVPAK'), and the overall length (~362 aa) and architecture match the conserved ASADH family fold. The N-terminal extension (MATPSKKRCGVLGATGAVGTRFILLLSQHPLLELVAVGAS...) is consistent with a mitochondrial targeting sequence, as fungal ASADHs are mitochondrial. A model familiar with the ASADH family (a central enzyme in the aspartate/lysine/methionine/threonine biosynthesis pathway, extensively characterized in bacteria and fungi) can recognize these combined features—Rossmann fold, catalytic cysteine, NADP+ specificity, absence of heme/ferredoxin/PLP motifs, and mitochondrial targeting—to select B over the other three structurally unrelated enzyme classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question is answerable through family-level recognition: the Rossmann fold eliminates ferredoxin- and P450-dependent options (C, D), the absence of PLP motifs eliminates the aminotransferase option (A), and the catalytic cysteine pattern plus overall architecture match the well-characterized ASADH family. This is transferable knowledge about enzyme families, not a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent structurally and mechanistically distinct enzyme classes (NADP+-dependent dehydrogenase, ferredoxin-dependent monooxygenase, P450 monooxygenase, and a tyrosinal-related reductase). The sequence features clearly favor one class over the others.


### Important caveats

- The Rossmann fold motif GxxGxxG is shared across many dehydrogenases; the specific assignment to ASADH relies on the combination of catalytic cysteine positions, overall fold architecture, and absence of competing motifs rather than a single unique sequence tag.
- The mitochondrial targeting sequence inference is consistent with fungal ASADH biology but is not strictly required to answer the question.
- The experimental evidence (X-ray crystallography, PubMed:26869335) confirms the annotation, but the model must rely on sequence-level family recognition without access to this evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif near the N-terminus (GVLGATGAVGTR, a GxxGxxG-like pattern), indicating an NAD(P)-dependent dehydrogenase/oxidoreductase. This immediately disfavors options C (ferredoxin-dependent monooxygenase requiring [2Fe-2S] clusters and O2) and D (cytochrome P450 requiring a heme-binding FxxGxxxCxxxG motif, neither of which is present). Option A (tyrosinal reductase/aminotransferase) would require a PLP-binding lysine or a completely different fold architecture, also absent. The remaining candidate B (aspartate-semialdehyde dehydrogenase, EC 1.2.1.11) is a well-known NADP+-dependent dehydrogenase with a catalytic cysteine forming a thioacyl intermediate. The sequence contains multiple cysteines in positions consistent with the ASADH catalytic Cys-Asp dyad (e.g., in 'GHTVCASLRFV' and 'CNSNCAVVGLVVPAK'), and the overall length (~362 aa) and architecture match the conserved ASADH family fold. The N-terminal extension (MATPSKKRCGVLGATGAVGTRFILLLSQHPLLELVAVGAS...) is consistent with a mitochondrial targeting sequence, as fungal ASADHs are mitochondrial. A model familiar with the ASADH family (a central enzyme in the aspartate/lysine/methionine/threonine biosynthesis pathway, extensively characterized in bacteria and fungi) can recognize these combined features—Rossmann fold, catalytic cysteine, NADP+ specificity, absence of heme/ferredoxin/PLP motifs, and mitochondrial targeting—to select B over the other three structurally unrelated enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through family-level recognition: the Rossmann fold eliminates ferredoxin- and P450-dependent options (C, D), the absence of PLP motifs eliminates the aminotransferase option (A), and the catalytic cysteine pattern plus overall architecture match the well-characterized ASADH family. This is transferable knowledge about enzyme families, not a lookup of this specific protein's record."
  },
  "case_id": "catalytic_activity_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A080WMA9 (sequence matched) annotates this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from Trichophyton rubrum, with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)' supported by experimental evidence (ECO:0000269, PubMed:26869335, X-ray crystallography at 2.55 Å in complex with NADP+). This exactly matches option B."
  },
  "important_caveats": [
    "The Rossmann fold motif GxxGxxG is shared across many dehydrogenases; the specific assignment to ASADH relies on the combination of catalytic cysteine positions, overall fold architecture, and absence of competing motifs rather than a single unique sequence tag.",
    "The mitochondrial targeting sequence inference is consistent with fungal ASADH biology but is not strictly required to answer the question.",
    "The experimental evidence (X-ray crystallography, PubMed:26869335) confirms the annotation, but the model must rely on sequence-level family recognition without access to this evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and mechanistically distinct enzyme classes (NADP+-dependent dehydrogenase, ferredoxin-dependent monooxygenase, P450 monooxygenase, and a tyrosinal-related reductase). The sequence features clearly favor one class over the others."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A080WMA9 (sequence matched) annotates this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from Trichophyton rubrum, with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)' supported by experimental evidence (ECO:0000269, PubMed:26869335, X-ray crystallography at 2.55 Å in complex with NADP+). This exactly matches option B.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif near the N-terminus (GVLGATGAVGTR, a GxxGxxG-like pattern), indicating an NAD(P)-dependent dehydrogenase/oxidoreductase. This immediately disfavors options C (ferredoxin-dependent monooxygenase requiring [2Fe-2S] clusters and O2) and D (cytochrome P450 requiring a heme-binding FxxGxxxCxxxG motif, neither of which is present). Option A (tyrosinal reductase/aminotransferase) would require a PLP-binding lysine or a completely different fold architecture, also absent. The remaining candidate B (aspartate-semialdehyde dehydrogenase, EC 1.2.1.11) is a well-known NADP+-dependent dehydrogenase with a catalytic cysteine forming a thioacyl intermediate. The sequence contains multiple cysteines in positions consistent with the ASADH catalytic Cys-Asp dyad (e.g., in 'GHTVCASLRFV' and 'CNSNCAVVGLVVPAK'), and the overall length (~362 aa) and architecture match the conserved ASADH family fold. The N-terminal extension (MATPSKKRCGVLGATGAVGTRFILLLSQHPLLELVAVGAS...) is consistent with a mitochondrial targeting sequence, as fungal ASADHs are mitochondrial. A model familiar with the ASADH family (a central enzyme in the aspartate/lysine/methionine/threonine biosynthesis pathway, extensively characterized in bacteria and fungi) can recognize these combined features—Rossmann fold, catalytic cysteine, NADP+ specificity, absence of heme/ferredoxin/PLP motifs, and mitochondrial targeting—to select B over the other three structurally unrelated enzyme classes.",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through family-level recognition: the Rossmann fold eliminates ferredoxin- and P450-dependent options (C, D), the absence of PLP motifs eliminates the aminotransferase option (A), and the catalytic cysteine pattern plus overall architecture match the well-characterized ASADH family. This is transferable knowledge about enzyme families, not a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and mechanistically distinct enzyme classes (NADP+-dependent dehydrogenase, ferredoxin-dependent monooxygenase, P450 monooxygenase, and a tyrosinal-related reductase). The sequence features clearly favor one class over the others."
  },
  "important_caveats": [
    "The Rossmann fold motif GxxGxxG is shared across many dehydrogenases; the specific assignment to ASADH relies on the combination of catalytic cysteine positions, overall fold architecture, and absence of competing motifs rather than a single unique sequence tag.",
    "The mitochondrial targeting sequence inference is consistent with fungal ASADH biology but is not strictly required to answer the question.",
    "The experimental evidence (X-ray crystallography, PubMed:26869335) confirms the annotation, but the model must rely on sequence-level family recognition without access to this evidence."
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
  "benchmark_sequence_length": 362,
  "benchmark_sequence_sha256": "ecc9f93bab233675495553ca0dc99c02862199248d190fa6418b0eaf45c3d7b5",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 362,
  "current_source_sequence_sha256": "ecc9f93bab233675495553ca0dc99c02862199248d190fa6418b0eaf45c3d7b5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A080WMA9",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "selected_historical_source_sequence_length": 362,
  "selected_historical_source_sequence_sha256": "ecc9f93bab233675495553ca0dc99c02862199248d190fa6418b0eaf45c3d7b5",
  "selected_historical_version": {
    "accession": "A0A080WMA9",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_TRIRC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A080WMA9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Athlete's foot fungus\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008864\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Onygenales\",\"Arthrodermataceae\",\"Trichophyton\"],\"scientificName\":\"Trichophyton rubrum (strain ATCC MYA-4607 / CBS 118892)\",\"taxonId\":559305}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26869335\",\"source\":\"PubMed\"}],\"value\":\"TrASADH\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24286\"}}],\"reaction\":{\"ecNumber\":\"1.2.1.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"}],\"name\":\"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24284\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:537519\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Li Q.\",\"Mu Z.\",\"Zhao R.\",\"Dahal G.\",\"Viola R.E.\",\"Liu T.\",\"Jin Q.\",\"Cui S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26869335\"},{\"database\":\"DOI\",\"id\":\"10.1038/srep21067\"}],\"citationType\":\"journal article\",\"firstPage\":\"21067\",\"id\":\"26869335\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"21067\",\"publicationDate\":\"2016\",\"title\":\"Structural Insights into the Tetrameric State of Aspartate-beta-semialdehyde Dehydrogenases from Fungal Species.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4ZHS\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4ZIC\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26869335\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"BMU01672\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.55 ANGSTROMS) IN COMPLEX WITH NADP(+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\",\"MUTAGENESIS OF 196-ASP--PHE-198 AND ARG-309\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_TRIRC              Reviewed;         362 AA.\nAC   A0A080WMA9; A0A140UHG6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   18-JUN-2025, entry version 38.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:26869335};\nDE   AltName: Full=TrASADH {ECO:0000303|PubMed:26869335};\nGN   ORFNames=TERG_03598 {ECO:0000312|EMBL:KFL61260.1};\nOS   Trichophyton rubrum (strain ATCC MYA-4607 / CBS 118892) (Athlete's foot\nOS   fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Onygenales; Arthrodermataceae; Trichophyton.\nOX   NCBI_TaxID=559305 {ECO:0000312|Proteomes:UP000008864};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:26869335};\nDE   AltName: Full=TrASADH {ECO:0000303|PubMed:26869335};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:4ZHS, ECO:0007744|PDB:4ZIC}\nRP   X-RAY CRYSTALLOGRAPHY (2.55 ANGSTROMS) IN COMPLEX WITH NADP(+), FUNCTION,\nRP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBUNIT, AND\nRP   MUTAGENESIS OF 196-ASP--PHE-198 AND ARG-309.\nRC   STRAIN=BMU01672 {ECO:0000303|PubMed:26869335};\nRX   PubMed=26869335; DOI=10.1038/srep21067;\nRA   Li Q., Mu Z., Zhao R., Dahal G., Viola R.E., Liu T., Jin Q., Cui S.;\nRT   \"Structural Insights into the Tetrameric State of Aspartate-beta-\nRT   semialdehyde Dehydrogenases from Fungal Species.\";\nRL   Sci. Rep. 6:21067-21067(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-\nCC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;\nCC         Evidence={ECO:0000269|PubMed:26869335};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;\nCC         Evidence={ECO:0000269|PubMed:26869335};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 174. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
