# catalytic_activity_0166

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0166.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — L-lysyl-&#91;protein&#93; + acetyl-CoA = N(6)-acetyl-L-lysyl-&#91;protein&#93; + CoA + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASENNKRKASEEALSPDSQLQSKKARTDSPEREPKSEGGPLGKPPLRIVPFPEKPAVLEERRGEIEFRVVNNDGSRDSFVVLTGLKCIFQKQLPKMPKDYIARLVYDRSHLSIAIVKHPLEVVGGITYRPFNSRRFAEIVFCAISSDQQVKGYGAHLMSHLKDYVKATSPIMHFLTYADNYAIGYFKKQGFTKEITLDKSIWMGYIKDYEGGTIMQCTMLPKIRYLEIGRMLLKQKEAVHAKIRAFSRSHIIHAPPKEWKNGACKIDPLSIPAIKQSGWSPDMDELARQPRHGPNYNQLLHLLNDMQNHSAAWPFTQPVNRDEVPDYYEVIKEPMDLSTMEEKHEKDMYPTPQDFIKDAMLIFDNCRRYNNENTPYAKSANKLEKFMWQQIRNIPEWSVST

[Multiple Choices]
A. Hydrolyzes single-stranded DNA or mismatched double-stranded DNA and polynucleotides, releasing free uracil.
B. Cs(+)(in) = Cs(+)(out)
C. 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)
D. L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)
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

> The matched-sequence UniProt annotation lists the exact acetylation reaction in D and cites experimental evidence (ECO:0000269). This supports D for the supplied protein, while not independently verifying the cited study here.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a fungal Gcn5-like GNAT-family acetyltransferase: this family has a catalytic acetyl-CoA-binding domain and transfers acetyl groups to lysine residues on proteins. That family-level inference points to D, rather than DNA base excision, ion transport, or an alkaloid redox reaction. The sequence alone may not establish every detail of substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable protein-family inference meaningfully distinguishes the offered protein lysine acetylation reaction without relying on the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, D is the reaction consistent with a Gcn5-like protein acetyltransferase.


### Important caveats

- Reviewer-only evidence also annotates a benzoyl-transfer reaction for this protein; it is not one of the offered choices and does not contradict D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a fungal Gcn5-like GNAT-family acetyltransferase: this family has a catalytic acetyl-CoA-binding domain and transfers acetyl groups to lysine residues on proteins. That family-level inference points to D, rather than DNA base excision, ion transport, or an alkaloid redox reaction. The sequence alone may not establish every detail of substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable protein-family inference meaningfully distinguishes the offered protein lysine acetylation reaction without relying on the exact protein's database record."
  },
  "case_id": "catalytic_activity_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation lists the exact acetylation reaction in D and cites experimental evidence (ECO:0000269). This supports D for the supplied protein, while not independently verifying the cited study here."
  },
  "important_caveats": [
    "Reviewer-only evidence also annotates a benzoyl-transfer reaction for this protein; it is not one of the offered choices and does not contradict D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, D is the reaction consistent with a Gcn5-like protein acetyltransferase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation lists the exact acetylation reaction in D and cites experimental evidence (ECO:0000269). This supports D for the supplied protein, while not independently verifying the cited study here.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a fungal Gcn5-like GNAT-family acetyltransferase: this family has a catalytic acetyl-CoA-binding domain and transfers acetyl groups to lysine residues on proteins. That family-level inference points to D, rather than DNA base excision, ion transport, or an alkaloid redox reaction. The sequence alone may not establish every detail of substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "A transferable protein-family inference meaningfully distinguishes the offered protein lysine acetylation reaction without relying on the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, D is the reaction consistent with a Gcn5-like protein acetyltransferase."
  },
  "important_caveats": [
    "Reviewer-only evidence also annotates a benzoyl-transfer reaction for this protein; it is not one of the offered choices and does not contradict D."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7U2QYM2, GCNE_ASPFN) explicitly annotates the catalytic reaction 'L-lysyl-&#91;protein&#93; + acetyl-CoA = N(6)-acetyl-L-lysyl-&#91;protein&#93; + CoA + H(+)' under EC 2.3.1.48 with experimental evidence (ECO:0000269, PubMed:39601562). The recommended name is 'Histone acetyltransferase gcnE.' This matches option D verbatim. The evidence is experimental, not merely computational or transferred.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable-knowledge arguments distinguish D from the other choices. (1) Elimination of A: Uracil DNA glycosylases (UDGs) are compact (~270-350 AA) enzymes with a characteristic beta-sheet core and specific catalytic residues (Asp, His, Tyr); this 402-AA sequence lacks those features and is too long/complex for a typical UDG. (2) Elimination of B: A Cs+ transporter would require 10-14 hydrophobic transmembrane helices; this sequence shows no such pattern of extended hydrophobic segments. (3) Elimination of C: The ajmaline dehydrogenase (a Rauwolfia serpentina alkaloid biosynthesis enzyme) would require a Rossmann-fold NAD(P)-binding motif (GxGxxG) and specific catalytic residues; while scattered glycines exist, no canonical Rossmann motif or dehydrogenase catalytic architecture is apparent. (4) Positive support for D: The GNAT (Gcn5-related N-acetyltransferase) superfamily is characterized by a conserved 'Q/RxxGxG/A' P-loop motif and a glycine-rich acetyl-CoA binding region. The sequence contains 'GYGA' (consistent with the Q/RxxGxG/A variant) and 'GGT' (glycine-rich loop), and the overall length (~402 AA) is consistent with fungal Gcn5 homologs (yeast Gcn5 is ~454 AA). The charged N-terminal region and absence of TM segments are consistent with a soluble nuclear acetyltransferase. These features, combined with the elimination of alternatives, provide a credible transferable-knowledge pathway to select D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of (a) elimination of clearly mismatched options (transporter, DNA glycosylase, NAD-dependent dehydrogenase) based on general structural/sequence principles learned from other proteins, and (b) recognition of GNAT-superfamily sequence hallmarks (GYGA motif, GGT glycine-rich region, appropriate length, soluble-protein composition) provides a concrete, transferable inference that meaningfully distinguishes option D. The GNAT fold is one of the most extensively characterized acyltransferase families, and its sequence signatures are part of standard protein-family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent very different enzyme classes (DNA glycosylase, ion transporter, NAD-dependent dehydrogenase, acyltransferase). The sequence features and elimination logic make D clearly the most defensible choice. No other option is seriously competitive given the absence of TM helices, Rossmann motifs, or UDG catalytic architecture.


### Important caveats

- The GNAT fold is defined primarily by 3D structure; pure sequence-based identification without database search is possible but relies on recognizing conserved motifs (GYGA, GGT) that are suggestive rather than absolutely diagnostic.
- The UniProt entry also annotates a benzoyltransferase activity (benzoyl-CoA + L-lysyl-&#91;protein&#93;), but this alternative substrate reaction is not among the offered choices, so it does not create ambiguity within the provided options.
- The experimental evidence (PubMed:39601562, published 2025) postdates many training cutoffs, but the GNAT/HAT family knowledge and sequence-motif recognition used in the argument are well-established and do not depend on this specific publication.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable-knowledge arguments distinguish D from the other choices. (1) Elimination of A: Uracil DNA glycosylases (UDGs) are compact (~270-350 AA) enzymes with a characteristic beta-sheet core and specific catalytic residues (Asp, His, Tyr); this 402-AA sequence lacks those features and is too long/complex for a typical UDG. (2) Elimination of B: A Cs+ transporter would require 10-14 hydrophobic transmembrane helices; this sequence shows no such pattern of extended hydrophobic segments. (3) Elimination of C: The ajmaline dehydrogenase (a Rauwolfia serpentina alkaloid biosynthesis enzyme) would require a Rossmann-fold NAD(P)-binding motif (GxGxxG) and specific catalytic residues; while scattered glycines exist, no canonical Rossmann motif or dehydrogenase catalytic architecture is apparent. (4) Positive support for D: The GNAT (Gcn5-related N-acetyltransferase) superfamily is characterized by a conserved 'Q/RxxGxG/A' P-loop motif and a glycine-rich acetyl-CoA binding region. The sequence contains 'GYGA' (consistent with the Q/RxxGxG/A variant) and 'GGT' (glycine-rich loop), and the overall length (~402 AA) is consistent with fungal Gcn5 homologs (yeast Gcn5 is ~454 AA). The charged N-terminal region and absence of TM segments are consistent with a soluble nuclear acetyltransferase. These features, combined with the elimination of alternatives, provide a credible transferable-knowledge pathway to select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of (a) elimination of clearly mismatched options (transporter, DNA glycosylase, NAD-dependent dehydrogenase) based on general structural/sequence principles learned from other proteins, and (b) recognition of GNAT-superfamily sequence hallmarks (GYGA motif, GGT glycine-rich region, appropriate length, soluble-protein composition) provides a concrete, transferable inference that meaningfully distinguishes option D. The GNAT fold is one of the most extensively characterized acyltransferase families, and its sequence signatures are part of standard protein-family knowledge."
  },
  "case_id": "catalytic_activity_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7U2QYM2, GCNE_ASPFN) explicitly annotates the catalytic reaction 'L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)' under EC 2.3.1.48 with experimental evidence (ECO:0000269, PubMed:39601562). The recommended name is 'Histone acetyltransferase gcnE.' This matches option D verbatim. The evidence is experimental, not merely computational or transferred."
  },
  "important_caveats": [
    "The GNAT fold is defined primarily by 3D structure; pure sequence-based identification without database search is possible but relies on recognizing conserved motifs (GYGA, GGT) that are suggestive rather than absolutely diagnostic.",
    "The UniProt entry also annotates a benzoyltransferase activity (benzoyl-CoA + L-lysyl-[protein]), but this alternative substrate reaction is not among the offered choices, so it does not create ambiguity within the provided options.",
    "The experimental evidence (PubMed:39601562, published 2025) postdates many training cutoffs, but the GNAT/HAT family knowledge and sequence-motif recognition used in the argument are well-established and do not depend on this specific publication."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes (DNA glycosylase, ion transporter, NAD-dependent dehydrogenase, acyltransferase). The sequence features and elimination logic make D clearly the most defensible choice. No other option is seriously competitive given the absence of TM helices, Rossmann motifs, or UDG catalytic architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7U2QYM2, GCNE_ASPFN) explicitly annotates the catalytic reaction 'L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)' under EC 2.3.1.48 with experimental evidence (ECO:0000269, PubMed:39601562). The recommended name is 'Histone acetyltransferase gcnE.' This matches option D verbatim. The evidence is experimental, not merely computational or transferred.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable-knowledge arguments distinguish D from the other choices. (1) Elimination of A: Uracil DNA glycosylases (UDGs) are compact (~270-350 AA) enzymes with a characteristic beta-sheet core and specific catalytic residues (Asp, His, Tyr); this 402-AA sequence lacks those features and is too long/complex for a typical UDG. (2) Elimination of B: A Cs+ transporter would require 10-14 hydrophobic transmembrane helices; this sequence shows no such pattern of extended hydrophobic segments. (3) Elimination of C: The ajmaline dehydrogenase (a Rauwolfia serpentina alkaloid biosynthesis enzyme) would require a Rossmann-fold NAD(P)-binding motif (GxGxxG) and specific catalytic residues; while scattered glycines exist, no canonical Rossmann motif or dehydrogenase catalytic architecture is apparent. (4) Positive support for D: The GNAT (Gcn5-related N-acetyltransferase) superfamily is characterized by a conserved 'Q/RxxGxG/A' P-loop motif and a glycine-rich acetyl-CoA binding region. The sequence contains 'GYGA' (consistent with the Q/RxxGxG/A variant) and 'GGT' (glycine-rich loop), and the overall length (~402 AA) is consistent with fungal Gcn5 homologs (yeast Gcn5 is ~454 AA). The charged N-terminal region and absence of TM segments are consistent with a soluble nuclear acetyltransferase. These features, combined with the elimination of alternatives, provide a credible transferable-knowledge pathway to select D.",
    "missing_item_specific_fact": "",
    "reason": "The combination of (a) elimination of clearly mismatched options (transporter, DNA glycosylase, NAD-dependent dehydrogenase) based on general structural/sequence principles learned from other proteins, and (b) recognition of GNAT-superfamily sequence hallmarks (GYGA motif, GGT glycine-rich region, appropriate length, soluble-protein composition) provides a concrete, transferable inference that meaningfully distinguishes option D. The GNAT fold is one of the most extensively characterized acyltransferase families, and its sequence signatures are part of standard protein-family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes (DNA glycosylase, ion transporter, NAD-dependent dehydrogenase, acyltransferase). The sequence features and elimination logic make D clearly the most defensible choice. No other option is seriously competitive given the absence of TM helices, Rossmann motifs, or UDG catalytic architecture."
  },
  "important_caveats": [
    "The GNAT fold is defined primarily by 3D structure; pure sequence-based identification without database search is possible but relies on recognizing conserved motifs (GYGA, GGT) that are suggestive rather than absolutely diagnostic.",
    "The UniProt entry also annotates a benzoyltransferase activity (benzoyl-CoA + L-lysyl-[protein]), but this alternative substrate reaction is not among the offered choices, so it does not create ambiguity within the provided options.",
    "The experimental evidence (PubMed:39601562, published 2025) postdates many training cutoffs, but the GNAT/HAT family knowledge and sequence-motif recognition used in the argument are well-established and do not depend on this specific publication."
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
  "benchmark_sequence_length": 402,
  "benchmark_sequence_sha256": "98f104b9c1052647fe3ad81fec046783468f372eba17bee1bf0a42e9d10f7d90",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 402,
  "current_source_sequence_sha256": "98f104b9c1052647fe3ad81fec046783468f372eba17bee1bf0a42e9d10f7d90",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 21,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7U2QYM2",
  "selected_historical_entry_version": 21,
  "selected_historical_record_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "selected_historical_source_sequence_length": 402,
  "selected_historical_source_sequence_sha256": "98f104b9c1052647fe3ad81fec046783468f372eba17bee1bf0a42e9d10f7d90",
  "selected_historical_version": {
    "accession": "A0A7U2QYM2",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "GCNE_ASPFN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7U2QYM2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357 / JCM 12722 / SRRC 167)\",\"taxonId\":332952}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"value\":\"Benzoyltransferase gcnE\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.48\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q03330\",\"source\":\"UniProtKB\"}],\"value\":\"Histone acetyltransferase gcnE\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:45949\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.48\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"name\":\"L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:45948\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9752\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10731\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29969\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61930\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:83532\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"name\":\"benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-[protein] + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:83531\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9752\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:20154\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29969\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57369\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:233144\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Chen X.\",\"Wu L.\",\"Zhang Y.\",\"Wang S.\",\"Wang S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39601562\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.02665-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0266524\",\"id\":\"39601562\",\"journal\":\"MBio\",\"lastPage\":\"e0266524\",\"publicationDate\":\"2025\",\"title\":\"Importance of benzoyltransferase GcnE and lysine benzoylation of alcohol dehydrogenase AdhB in pathogenesis and aflatoxin production in Aspergillus flavus.\",\"volume\":\"16\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"CATALYTIC ACTIVITY\",\"DOMAIN\",\"ACTIVE SITE\",\"MUTAGENESIS OF GLU-139\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H1",
  "excerpt": "ID   GCNE_ASPFN              Reviewed;         402 AA.\nAC   A0A7U2QYM2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=Histone acetyltransferase gcnE {ECO:0000250|UniProtKB:Q03330};\nDE            EC=2.3.1.48 {ECO:0000269|PubMed:39601562};\nDE   AltName: Full=Benzoyltransferase gcnE {ECO:0000303|PubMed:39601562};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:39601562};\nGN   Name=gcnE {ECO:0000303|PubMed:39601562}; ORFNames=F9C07_11133;\nOS   Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357\nOS   / JCM 12722 / SRRC 167).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=332952;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Histone acetyltransferase gcnE {ECO:0000250|UniProtKB:Q03330};\nDE            EC=2.3.1.48 {ECO:0000269|PubMed:39601562};\nDE   AltName: Full=Benzoyltransferase gcnE {ECO:0000303|PubMed:39601562};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:39601562};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, CATALYTIC ACTIVITY, DOMAIN, ACTIVE SITE,\nRP   AND MUTAGENESIS OF GLU-139.\nRX   PubMed=39601562; DOI=10.1128/mbio.02665-24;\nRA   Chen X., Wu L., Zhang Y., Wang S., Wang S.;\nRT   \"Importance of benzoyltransferase GcnE and lysine benzoylation of alcohol\nRT   dehydrogenase AdhB in pathogenesis and aflatoxin production in Aspergillus\nRT   flavus.\";\nRL   MBio 16:e0266524-e0266524(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein]\nCC         + CoA + H(+); Xref=Rhea:RHEA:45948, Rhea:RHEA-COMP:9752, Rhea:RHEA-\nCC         COMP:10731, ChEBI:CHEBI:15378, ChEBI:CHEBI:29969, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57288, ChEBI:CHEBI:61930; EC=2.3.1.48;\nCC         Evidence={ECO:0000269|PubMed:39601562};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:45949;\nCC         Evidence={ECO:0000269|PubMed:39601562};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-\nCC         [protein] + CoA + H(+); Xref=Rhea:RHEA:83531, Rhea:RHEA-COMP:9752,\nCC         Rhea:RHEA-COMP:20154, ChEBI:CHEBI:15378, ChEBI:CHEBI:29969,\nCC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57369, ChEBI:CHEBI:233144;\nCC         Evidence={ECO:0000269|PubMed:39601562};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83532;\nCC         Evidence={ECO:0000269|PubMed:39601562};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 166. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
