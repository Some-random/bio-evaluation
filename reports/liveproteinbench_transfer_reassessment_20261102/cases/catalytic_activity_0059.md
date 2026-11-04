# catalytic_activity_0059

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0059.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKKILFITGTRADYSKIKSLMYRVQNSSEFELCIFATGMHLSKNFGYTVKELYKNGFKNIYEFINYDKYYQTDKALATTIDGFSRYVNELKPDLIVVHGDRIEPLAAAIVGALNNILVAHIEGGEISGTIDDSLRHAISKLAHIHLVNDEFAKKRLMQLGEDEKSIFIIGSPDLELLNDNKISLNEAKKYYDINYENYALLMFHPVTTEITSIKNQADNLVKALIQSNKNYIVIYPNNDLGFELILQSYEELKNNPRFKLFPSLRFEYFITLLKNADFIIGNSSCILKEALYLKTAGILVGSRQNGRLGNENTLKVNANSDEILKAINTIHKKQDLFSAKLEILDSSKLFFEYLQSGEFFKLSTQKVFKDIII

[Multiple Choices]
A. L-dopa + H(+) = dopamine + CO2
B. D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)
C. 2 5'-deoxyadenosin-5'-yl radical + 2 dAMP + A = 2 4'-phospho-dehydrooxetanocin + 2 5'-deoxyadenosine + AH2
D. UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)
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

> The sequence-matched UniProt record gives this reaction and cites experimental evidence (ECO:0000269, PubMed 38382015). This supports D for the supplied sequence, though the primary paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 373-aa sequence is consistent with a bacterial UDP-N-acetylglucosamine 2-epimerase-like enzyme. Transferable family-level knowledge points to UDP-linked N-acetylhexosamine chemistry, distinguishing D from the unrelated aromatic amino-acid decarboxylation, acetyltransferase, and radical-SAM reactions. The sequence also lacks the characteristic CxxxCxxC motif expected for a radical-SAM enzyme.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the strong contrast among the offered reaction classes provide a meaningful, probabilistic basis for D without relying on the exact protein's database annotation. The unusual hydrolytic product may not be predictable with certainty from family recognition alone, but the alternatives do not require that degree of discrimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered reaction is comparably supported by the sequence and transferable family-level inference.


### Important caveats

- The source annotation is supported by cited experimental evidence, but the cited primary study was not independently assessed.
- The exact hydrolytic reaction is less directly inferable from family-level knowledge than the broad UDP-sugar reaction class.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 373-aa sequence is consistent with a bacterial UDP-N-acetylglucosamine 2-epimerase-like enzyme. Transferable family-level knowledge points to UDP-linked N-acetylhexosamine chemistry, distinguishing D from the unrelated aromatic amino-acid decarboxylation, acetyltransferase, and radical-SAM reactions. The sequence also lacks the characteristic CxxxCxxC motif expected for a radical-SAM enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the strong contrast among the offered reaction classes provide a meaningful, probabilistic basis for D without relying on the exact protein's database annotation. The unusual hydrolytic product may not be predictable with certainty from family recognition alone, but the alternatives do not require that degree of discrimination."
  },
  "case_id": "catalytic_activity_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record gives this reaction and cites experimental evidence (ECO:0000269, PubMed 38382015). This supports D for the supplied sequence, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The source annotation is supported by cited experimental evidence, but the cited primary study was not independently assessed.",
    "The exact hydrolytic reaction is less directly inferable from family-level knowledge than the broad UDP-sugar reaction class."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction is comparably supported by the sequence and transferable family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record gives this reaction and cites experimental evidence (ECO:0000269, PubMed 38382015). This supports D for the supplied sequence, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 373-aa sequence is consistent with a bacterial UDP-N-acetylglucosamine 2-epimerase-like enzyme. Transferable family-level knowledge points to UDP-linked N-acetylhexosamine chemistry, distinguishing D from the unrelated aromatic amino-acid decarboxylation, acetyltransferase, and radical-SAM reactions. The sequence also lacks the characteristic CxxxCxxC motif expected for a radical-SAM enzyme.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the strong contrast among the offered reaction classes provide a meaningful, probabilistic basis for D without relying on the exact protein's database annotation. The unusual hydrolytic product may not be predictable with certainty from family recognition alone, but the alternatives do not require that degree of discrimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction is comparably supported by the sequence and transferable family-level inference."
  },
  "important_caveats": [
    "The source annotation is supported by cited experimental evidence, but the cited primary study was not independently assessed.",
    "The exact hydrolytic reaction is less directly inferable from family-level knowledge than the broad UDP-sugar reaction class."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DY05 (UAEPH_CAMJ8) matches the supplied 373-aa sequence exactly (SHA256 confirmed). The catalytic activity is annotated as EC 3.2.1.183: UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+), matching choice D verbatim. The annotation carries experimental evidence (ECO:0000269) from PubMed 38382015 (Ghosh & Raushel, Biochemistry 2024), confirming this is experimentally validated, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can eliminate options through family-level sequence reasoning: (1) Option C (radical SAM) requires a conserved CX3CX2C motif for &#91;4Fe-4S&#93; cluster binding, which is entirely absent from this sequence. (2) Option A (aromatic L-amino acid decarboxylase) requires PLP-binding motifs (e.g., conserved Lys for Schiff base, 'GGR' region) and is typically 470-500 aa; this 373-aa protein lacks these features. (3) Option B (N-acetylglutamate synthase) requires a GNAT (GCN5-related N-acetyltransferase) domain with a characteristic PxxxG motif and acetyl-CoA binding features, which are not evident here. (4) The sequence contains 'HGDRIE' embedded in a nucleotide-sugar-processing context and 'NNDLG' (reminiscent of NDP-binding motifs), along with glycine-rich loops ('GSPDLELL'), collectively suggesting a nucleotide sugar-processing enzyme. Among the four choices, only D involves a nucleotide sugar substrate (UDP-GlcNAc). Thus, recognizing the protein as a nucleotide sugar enzyme from these conserved motifs and eliminating the three non-nucleotide-sugar options meaningfully distinguishes D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of A (no PLP motifs, wrong size), C (no radical SAM motif), and B (no GNAT domain) is well-supported by general biochemistry. The positive identification of nucleotide sugar processing via HGDRIE/NNDLG motifs and the fact that D is the sole nucleotide-sugar option among the choices provides a credible transferable inference. The specific distinction between EC 3.2.1.183 (hydrolyzing) and EC 5.1.3.7 (classical NAD-dependent) is not needed because only one nucleotide sugar option is offered.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mechanistically and structurally distinct enzyme classes (PLP-decarboxylase, GNAT acetyltransferase, radical SAM, nucleotide sugar hydrolase/epimerase). Sequence features clearly eliminate A and C, and the absence of GNAT features plus presence of nucleotide-sugar motifs distinguishes D from B. No two options are genuinely ambiguous given the available sequence evidence.


### Important caveats

- The hydrolyzing UDP-GlcNAc 2-epimerase (EC 3.2.1.183) is a very recently characterized enzyme (2024, Ghosh & Raushel). The 'HGDRIE' motif association with nucleotide sugar processing is suggestive but not as universally well-known as, e.g., the Rossmann fold of classical epimerases.
- The argument relies on recognizing the protein as a nucleotide sugar enzyme broadly, then noting D is the only such option. A model that fails to recognize HGDRIE/NNDLG as nucleotide-sugar features might struggle to distinguish D from B.
- The experimental evidence (ECO:0000269) confirms the annotation, but the enzyme was only characterized in 2024, so family-level training data for this specific enzyme may be sparse.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate options through family-level sequence reasoning: (1) Option C (radical SAM) requires a conserved CX3CX2C motif for [4Fe-4S] cluster binding, which is entirely absent from this sequence. (2) Option A (aromatic L-amino acid decarboxylase) requires PLP-binding motifs (e.g., conserved Lys for Schiff base, 'GGR' region) and is typically 470-500 aa; this 373-aa protein lacks these features. (3) Option B (N-acetylglutamate synthase) requires a GNAT (GCN5-related N-acetyltransferase) domain with a characteristic PxxxG motif and acetyl-CoA binding features, which are not evident here. (4) The sequence contains 'HGDRIE' embedded in a nucleotide-sugar-processing context and 'NNDLG' (reminiscent of NDP-binding motifs), along with glycine-rich loops ('GSPDLELL'), collectively suggesting a nucleotide sugar-processing enzyme. Among the four choices, only D involves a nucleotide sugar substrate (UDP-GlcNAc). Thus, recognizing the protein as a nucleotide sugar enzyme from these conserved motifs and eliminating the three non-nucleotide-sugar options meaningfully distinguishes D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A (no PLP motifs, wrong size), C (no radical SAM motif), and B (no GNAT domain) is well-supported by general biochemistry. The positive identification of nucleotide sugar processing via HGDRIE/NNDLG motifs and the fact that D is the sole nucleotide-sugar option among the choices provides a credible transferable inference. The specific distinction between EC 3.2.1.183 (hydrolyzing) and EC 5.1.3.7 (classical NAD-dependent) is not needed because only one nucleotide sugar option is offered."
  },
  "case_id": "catalytic_activity_0059",
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
    "reason": "The UniProt entry P0DY05 (UAEPH_CAMJ8) matches the supplied 373-aa sequence exactly (SHA256 confirmed). The catalytic activity is annotated as EC 3.2.1.183: UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+), matching choice D verbatim. The annotation carries experimental evidence (ECO:0000269) from PubMed 38382015 (Ghosh & Raushel, Biochemistry 2024), confirming this is experimentally validated, not merely computational."
  },
  "important_caveats": [
    "The hydrolyzing UDP-GlcNAc 2-epimerase (EC 3.2.1.183) is a very recently characterized enzyme (2024, Ghosh & Raushel). The 'HGDRIE' motif association with nucleotide sugar processing is suggestive but not as universally well-known as, e.g., the Rossmann fold of classical epimerases.",
    "The argument relies on recognizing the protein as a nucleotide sugar enzyme broadly, then noting D is the only such option. A model that fails to recognize HGDRIE/NNDLG as nucleotide-sugar features might struggle to distinguish D from B.",
    "The experimental evidence (ECO:0000269) confirms the annotation, but the enzyme was only characterized in 2024, so family-level training data for this specific enzyme may be sparse."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically and structurally distinct enzyme classes (PLP-decarboxylase, GNAT acetyltransferase, radical SAM, nucleotide sugar hydrolase/epimerase). Sequence features clearly eliminate A and C, and the absence of GNAT features plus presence of nucleotide-sugar motifs distinguishes D from B. No two options are genuinely ambiguous given the available sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DY05 (UAEPH_CAMJ8) matches the supplied 373-aa sequence exactly (SHA256 confirmed). The catalytic activity is annotated as EC 3.2.1.183: UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+), matching choice D verbatim. The annotation carries experimental evidence (ECO:0000269) from PubMed 38382015 (Ghosh & Raushel, Biochemistry 2024), confirming this is experimentally validated, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can eliminate options through family-level sequence reasoning: (1) Option C (radical SAM) requires a conserved CX3CX2C motif for [4Fe-4S] cluster binding, which is entirely absent from this sequence. (2) Option A (aromatic L-amino acid decarboxylase) requires PLP-binding motifs (e.g., conserved Lys for Schiff base, 'GGR' region) and is typically 470-500 aa; this 373-aa protein lacks these features. (3) Option B (N-acetylglutamate synthase) requires a GNAT (GCN5-related N-acetyltransferase) domain with a characteristic PxxxG motif and acetyl-CoA binding features, which are not evident here. (4) The sequence contains 'HGDRIE' embedded in a nucleotide-sugar-processing context and 'NNDLG' (reminiscent of NDP-binding motifs), along with glycine-rich loops ('GSPDLELL'), collectively suggesting a nucleotide sugar-processing enzyme. Among the four choices, only D involves a nucleotide sugar substrate (UDP-GlcNAc). Thus, recognizing the protein as a nucleotide sugar enzyme from these conserved motifs and eliminating the three non-nucleotide-sugar options meaningfully distinguishes D.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A (no PLP motifs, wrong size), C (no radical SAM motif), and B (no GNAT domain) is well-supported by general biochemistry. The positive identification of nucleotide sugar processing via HGDRIE/NNDLG motifs and the fact that D is the sole nucleotide-sugar option among the choices provides a credible transferable inference. The specific distinction between EC 3.2.1.183 (hydrolyzing) and EC 5.1.3.7 (classical NAD-dependent) is not needed because only one nucleotide sugar option is offered."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically and structurally distinct enzyme classes (PLP-decarboxylase, GNAT acetyltransferase, radical SAM, nucleotide sugar hydrolase/epimerase). Sequence features clearly eliminate A and C, and the absence of GNAT features plus presence of nucleotide-sugar motifs distinguishes D from B. No two options are genuinely ambiguous given the available sequence evidence."
  },
  "important_caveats": [
    "The hydrolyzing UDP-GlcNAc 2-epimerase (EC 3.2.1.183) is a very recently characterized enzyme (2024, Ghosh & Raushel). The 'HGDRIE' motif association with nucleotide sugar processing is suggestive but not as universally well-known as, e.g., the Rossmann fold of classical epimerases.",
    "The argument relies on recognizing the protein as a nucleotide sugar enzyme broadly, then noting D is the only such option. A model that fails to recognize HGDRIE/NNDLG as nucleotide-sugar features might struggle to distinguish D from B.",
    "The experimental evidence (ECO:0000269) confirms the annotation, but the enzyme was only characterized in 2024, so family-level training data for this specific enzyme may be sparse."
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
  "benchmark_sequence_length": 373,
  "benchmark_sequence_sha256": "e7bbdfb124fa6a1f8e0776ef9cfe10605110b022d22f31aa7d87fd2dc63013ef",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 373,
  "current_source_sequence_sha256": "e7bbdfb124fa6a1f8e0776ef9cfe10605110b022d22f31aa7d87fd2dc63013ef",
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
  "requested_accession": "P0DY05",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "selected_historical_source_sequence_length": 373,
  "selected_historical_source_sequence_sha256": "e7bbdfb124fa6a1f8e0776ef9cfe10605110b022d22f31aa7d87fd2dc63013ef",
  "selected_historical_version": {
    "accession": "P0DY05",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UAEPH_CAMJ8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DY05\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC 11828)\",\"taxonId\":407148}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Hydrolyzing UDP-GlcNAc 2-epimerase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.183\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetylglucosamine 2-epimerase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:30684\"}}],\"reaction\":{\"ecNumber\":\"3.2.1.183\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:30683\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17122\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"81116 / NCTC 11828\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   UAEPH_CAMJ8             Reviewed;         373 AA.\nAC   P0DY05;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};\nDE            EC=3.2.1.183 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=Hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};\nGN   Name=HS6.10 {ECO:0000303|PubMed:38382015};\nGN   OrderedLocusNames=C8J_1338 {ECO:0000312|EMBL:ABV52936.1};\nOS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC\nOS   11828).\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=407148;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};\nDE            EC=3.2.1.183 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=Hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=81116 / NCTC 11828;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-\nCC         mannosamine + UDP + H(+); Xref=Rhea:RHEA:30683, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17122, ChEBI:CHEBI:57705,\nCC         ChEBI:CHEBI:58223; EC=3.2.1.183;\nCC         Evidence={ECO:0000269|PubMed:38382015};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:30684;\nCC         Evidence={ECO:0000269|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 59. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
