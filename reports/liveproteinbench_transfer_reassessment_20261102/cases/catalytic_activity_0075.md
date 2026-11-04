# catalytic_activity_0075

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0075.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTVKVKFPKDIREYARKEKVKDSLIKLTETALAEAISKFHRRMIVLQGDTLNKAKLAGILAGGAARILSEYIPEMLERKLRDTEQIEVLYATDALGEDTYGRKRFEEFRKHFSLLAPTAELTSVTFKHSRDILGRTFDILVIDLSYDYSPNDLGRIIETVRGGGLIFVLTNPFEKWKDMWTGFHKSLVTPPYTIEDVKKRFNRRLIRKFTEHKGIYIVNTDRMSIERKPGKYRSQATLPEREKVEIPKNIRFPRELYELCLTRGQVEVLKTLEELIEKEGMVVLTADRGRGKSVSIGIASVGLAVSSKKKRFRIVVTAPEPENVQSLMKFAKKSLEVLGYKTKVITDNGLIKEVYAKGIGIRYYPPTKGYRQRAELYIVDEAAGIHVPILHRYLEKERVVFSSTIHGYEGAGRGFSVKFLKKAKEKREYKEVHLSTPIRYAEGDPIEKWLFDVLLLDAEPVELTEEDYELIRKMEVYLEEPDLDDWFENDREDLRHFVGIYVLAHYRNRPSDVALLADAPHHEARVLRLKNGKIVTAIQIAKEGGIPKAVIDKMAKGYKPPGNIIPDMMVKHHYAKEFARLKGYRVVRIATHPDAMDMGLGSKALELLIKEAEEKGLDWVGSGFGASPELIRFWVRNGFAVVHLSPTRNPVSGEYTAIVIKPISEKAKEIVKKANEEFRIRLTEWLGDTHRDLEPEIARWLFESPFGEAVNYPIYLTKTQKRRLEMFIKRILTYDTVVDAVKPLVKLYFLDGWMRPYLDERQIMLLIHRVLQAHDWKETAKLLNRTEMYTMVELRDIVRGLWYYYKHLIKDEEGEK

[Multiple Choices]
A. cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)
B. 5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O
C. L-aspartate + ATP = 4-phospho-L-aspartate + ADP
D. uridine(out) = uridine(in)
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

> The sequence-matched UniProt annotation assigns this protein to TmcA and gives choice A as its catalytic activity, based on a HAMAP computational rule (C4, C5, H4). A cited publication also supports the broader reaction of RNA cytidine N4-acetylation, though the supplied excerpts do not establish direct experimental verification of the specific tRNA(Met) position for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence is compatible with the multidomain TmcA-type tRNA-modification enzyme family, whose transferable family-level function is ATP-dependent cytidine acetylation in tRNA. That points to A over B, a phosphoribosyltransferase reaction, C, an aspartate-phosphorylation reaction, and D, uridine transport. The inference is family-based rather than a deduction of every substrate detail from first principles.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could use sequence-based family recognition and the known function of related TmcA proteins to meaningfully distinguish A among these markedly different alternatives; it need not know this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reactions, and the TmcA-family inference favors A; no other listed option is comparably defensible.


### Important caveats

- The exact tRNA(Met) C34 reaction annotation is attributed to a computational HAMAP rule; the cited publication evidence in the excerpts supports broader RNA cytidine acetylation.
- Reviewer-only annotations support assessment of the key but are not original model inputs and are not used as the basis for the answerability inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is compatible with the multidomain TmcA-type tRNA-modification enzyme family, whose transferable family-level function is ATP-dependent cytidine acetylation in tRNA. That points to A over B, a phosphoribosyltransferase reaction, C, an aspartate-phosphorylation reaction, and D, uridine transport. The inference is family-based rather than a deduction of every substrate detail from first principles.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use sequence-based family recognition and the known function of related TmcA proteins to meaningfully distinguish A among these markedly different alternatives; it need not know this exact protein's database annotation."
  },
  "case_id": "catalytic_activity_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein to TmcA and gives choice A as its catalytic activity, based on a HAMAP computational rule (C4, C5, H4). A cited publication also supports the broader reaction of RNA cytidine N4-acetylation, though the supplied excerpts do not establish direct experimental verification of the specific tRNA(Met) position for this protein."
  },
  "important_caveats": [
    "The exact tRNA(Met) C34 reaction annotation is attributed to a computational HAMAP rule; the cited publication evidence in the excerpts supports broader RNA cytidine acetylation.",
    "Reviewer-only annotations support assessment of the key but are not original model inputs and are not used as the basis for the answerability inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the TmcA-family inference favors A; no other listed option is comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein to TmcA and gives choice A as its catalytic activity, based on a HAMAP computational rule (C4, C5, H4). A cited publication also supports the broader reaction of RNA cytidine N4-acetylation, though the supplied excerpts do not establish direct experimental verification of the specific tRNA(Met) position for this protein.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence is compatible with the multidomain TmcA-type tRNA-modification enzyme family, whose transferable family-level function is ATP-dependent cytidine acetylation in tRNA. That points to A over B, a phosphoribosyltransferase reaction, C, an aspartate-phosphorylation reaction, and D, uridine transport. The inference is family-based rather than a deduction of every substrate detail from first principles.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use sequence-based family recognition and the known function of related TmcA proteins to meaningfully distinguish A among these markedly different alternatives; it need not know this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the TmcA-family inference favors A; no other listed option is comparably defensible."
  },
  "important_caveats": [
    "The exact tRNA(Met) C34 reaction annotation is attributed to a computational HAMAP rule; the cited publication evidence in the excerpts supports broader RNA cytidine acetylation.",
    "Reviewer-only annotations support assessment of the key but are not original model inputs and are not used as the basis for the answerability inference."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8U3G4 (TMCA_PYRFU) for the 816-aa sequence from Pyrococcus furiosus is annotated as tRNA(Met) cytidine acetyltransferase TmcA, EC 2.3.1.193, with the exact catalytic reaction in option A listed as the primary annotated activity (evidence code ECO:0000255, HAMAP-Rule MF_01886). Additional broader RNA acetylation activities are annotated with partial experimental support (ECO:0000305, PubMed:32555463). The sequence matches the source record exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 816-aa sequence exhibits a bipartite domain architecture: an N-terminal Rossmann-like fold (recognizable by the glycine-rich 'GDTLNKAKLAGILAGG' motif and the β-α-β-α-β topology typical of nucleotide-binding domains) and a C-terminal GNAT (GCN5-related N-acetyltransferase) fold (indicated by motifs such as 'ATHPD', 'GSGFGASPE', and the overall α/β arrangement in the C-terminal ~200 residues). This combination of an ATP-binding Rossmann domain fused to a GNAT acetyltransferase domain in a single ~800-residue polypeptide is the hallmark of the TmcA/TrmO/NAT10 family of RNA acetyltransferases. Among the four options, only A involves acetyl-CoA as a co-substrate, consistent with a GNAT-fold acetyltransferase. Option B (PRPP synthetase) would be ~300-400 aa with a distinct PRPP-synthetase fold and no GNAT domain. Option C (aspartate kinase) would be ~450-500 aa with ACT regulatory domains and a kinase fold, lacking any acetyltransferase motif. Option D (uridine transporter) would be a membrane protein with multiple transmembrane helices and NCS/MFS motifs, entirely absent here. Thus, recognition of the GNAT fold and the bipartite ATP+acetyl-CoA architecture from general knowledge of acetyltransferase families meaningfully selects A over B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use transferable knowledge of GNAT-fold acetyltransferases, Rossmann-fold nucleotide-binding domains, and the distinctive bipartite architecture of the TmcA/TrmO/NAT10 family (shared across bacteria, archaea, and eukaryotes) to identify the acetyltransferase activity. The protein length (~816 aa), the presence of both ATP- and acetyl-CoA-binding motifs, and the absence of transmembrane helices or kinase/ACT domains collectively distinguish option A from the three non-acetyltransferase distractors without requiring recall of this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different enzyme classes (acetyltransferase, synthetase, kinase, transporter). The sequence features clearly favor an acetyltransferase with RNA substrate specificity. No other option is defensible given the domain architecture.


### Important caveats

- The primary annotation evidence is ECO:0000255 (HAMAP-Rule), a computational/probabilistic annotation rather than direct experimental characterization of this specific archaeal protein. The broader RNA acetylation activities carry additional experimental evidence (PubMed:32555463, 2020 Nature paper on NAT10/TmcA).
- The specific substrate detail 'cytidine(34) in elongator tRNA(Met)' is the canonical EC 2.3.1.193 reaction; the same enzyme also acetylates cytidine in other RNA contexts (tRNA, mRNA, general RNA) per additional UniProt annotations, but only option A is offered as the acetyltransferase choice.
- GNAT-fold recognition from raw sequence is a probabilistic inference; not all GNAT domains are equally obvious from sequence alone, though the bipartite architecture here is quite distinctive.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 816-aa sequence exhibits a bipartite domain architecture: an N-terminal Rossmann-like fold (recognizable by the glycine-rich 'GDTLNKAKLAGILAGG' motif and the β-α-β-α-β topology typical of nucleotide-binding domains) and a C-terminal GNAT (GCN5-related N-acetyltransferase) fold (indicated by motifs such as 'ATHPD', 'GSGFGASPE', and the overall α/β arrangement in the C-terminal ~200 residues). This combination of an ATP-binding Rossmann domain fused to a GNAT acetyltransferase domain in a single ~800-residue polypeptide is the hallmark of the TmcA/TrmO/NAT10 family of RNA acetyltransferases. Among the four options, only A involves acetyl-CoA as a co-substrate, consistent with a GNAT-fold acetyltransferase. Option B (PRPP synthetase) would be ~300-400 aa with a distinct PRPP-synthetase fold and no GNAT domain. Option C (aspartate kinase) would be ~450-500 aa with ACT regulatory domains and a kinase fold, lacking any acetyltransferase motif. Option D (uridine transporter) would be a membrane protein with multiple transmembrane helices and NCS/MFS motifs, entirely absent here. Thus, recognition of the GNAT fold and the bipartite ATP+acetyl-CoA architecture from general knowledge of acetyltransferase families meaningfully selects A over B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use transferable knowledge of GNAT-fold acetyltransferases, Rossmann-fold nucleotide-binding domains, and the distinctive bipartite architecture of the TmcA/TrmO/NAT10 family (shared across bacteria, archaea, and eukaryotes) to identify the acetyltransferase activity. The protein length (~816 aa), the presence of both ATP- and acetyl-CoA-binding motifs, and the absence of transmembrane helices or kinase/ACT domains collectively distinguish option A from the three non-acetyltransferase distractors without requiring recall of this exact protein's database annotation."
  },
  "case_id": "catalytic_activity_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8U3G4 (TMCA_PYRFU) for the 816-aa sequence from Pyrococcus furiosus is annotated as tRNA(Met) cytidine acetyltransferase TmcA, EC 2.3.1.193, with the exact catalytic reaction in option A listed as the primary annotated activity (evidence code ECO:0000255, HAMAP-Rule MF_01886). Additional broader RNA acetylation activities are annotated with partial experimental support (ECO:0000305, PubMed:32555463). The sequence matches the source record exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The primary annotation evidence is ECO:0000255 (HAMAP-Rule), a computational/probabilistic annotation rather than direct experimental characterization of this specific archaeal protein. The broader RNA acetylation activities carry additional experimental evidence (PubMed:32555463, 2020 Nature paper on NAT10/TmcA).",
    "The specific substrate detail 'cytidine(34) in elongator tRNA(Met)' is the canonical EC 2.3.1.193 reaction; the same enzyme also acetylates cytidine in other RNA contexts (tRNA, mRNA, general RNA) per additional UniProt annotations, but only option A is offered as the acetyltransferase choice.",
    "GNAT-fold recognition from raw sequence is a probabilistic inference; not all GNAT domains are equally obvious from sequence alone, though the bipartite architecture here is quite distinctive."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (acetyltransferase, synthetase, kinase, transporter). The sequence features clearly favor an acetyltransferase with RNA substrate specificity. No other option is defensible given the domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8U3G4 (TMCA_PYRFU) for the 816-aa sequence from Pyrococcus furiosus is annotated as tRNA(Met) cytidine acetyltransferase TmcA, EC 2.3.1.193, with the exact catalytic reaction in option A listed as the primary annotated activity (evidence code ECO:0000255, HAMAP-Rule MF_01886). Additional broader RNA acetylation activities are annotated with partial experimental support (ECO:0000305, PubMed:32555463). The sequence matches the source record exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 816-aa sequence exhibits a bipartite domain architecture: an N-terminal Rossmann-like fold (recognizable by the glycine-rich 'GDTLNKAKLAGILAGG' motif and the β-α-β-α-β topology typical of nucleotide-binding domains) and a C-terminal GNAT (GCN5-related N-acetyltransferase) fold (indicated by motifs such as 'ATHPD', 'GSGFGASPE', and the overall α/β arrangement in the C-terminal ~200 residues). This combination of an ATP-binding Rossmann domain fused to a GNAT acetyltransferase domain in a single ~800-residue polypeptide is the hallmark of the TmcA/TrmO/NAT10 family of RNA acetyltransferases. Among the four options, only A involves acetyl-CoA as a co-substrate, consistent with a GNAT-fold acetyltransferase. Option B (PRPP synthetase) would be ~300-400 aa with a distinct PRPP-synthetase fold and no GNAT domain. Option C (aspartate kinase) would be ~450-500 aa with ACT regulatory domains and a kinase fold, lacking any acetyltransferase motif. Option D (uridine transporter) would be a membrane protein with multiple transmembrane helices and NCS/MFS motifs, entirely absent here. Thus, recognition of the GNAT fold and the bipartite ATP+acetyl-CoA architecture from general knowledge of acetyltransferase families meaningfully selects A over B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use transferable knowledge of GNAT-fold acetyltransferases, Rossmann-fold nucleotide-binding domains, and the distinctive bipartite architecture of the TmcA/TrmO/NAT10 family (shared across bacteria, archaea, and eukaryotes) to identify the acetyltransferase activity. The protein length (~816 aa), the presence of both ATP- and acetyl-CoA-binding motifs, and the absence of transmembrane helices or kinase/ACT domains collectively distinguish option A from the three non-acetyltransferase distractors without requiring recall of this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (acetyltransferase, synthetase, kinase, transporter). The sequence features clearly favor an acetyltransferase with RNA substrate specificity. No other option is defensible given the domain architecture."
  },
  "important_caveats": [
    "The primary annotation evidence is ECO:0000255 (HAMAP-Rule), a computational/probabilistic annotation rather than direct experimental characterization of this specific archaeal protein. The broader RNA acetylation activities carry additional experimental evidence (PubMed:32555463, 2020 Nature paper on NAT10/TmcA).",
    "The specific substrate detail 'cytidine(34) in elongator tRNA(Met)' is the canonical EC 2.3.1.193 reaction; the same enzyme also acetylates cytidine in other RNA contexts (tRNA, mRNA, general RNA) per additional UniProt annotations, but only option A is offered as the acetyltransferase choice.",
    "GNAT-fold recognition from raw sequence is a probabilistic inference; not all GNAT domains are equally obvious from sequence alone, though the bipartite architecture here is quite distinctive."
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
  "benchmark_sequence_length": 816,
  "benchmark_sequence_sha256": "efad9c6b7776bbc78e56d40d80cd2f860218a2783d4d092d0f3250c6908ee57c",
  "current_entry_audit": {
    "entryVersion": 123,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 816,
  "current_source_sequence_sha256": "efad9c6b7776bbc78e56d40d80cd2f860218a2783d4d092d0f3250c6908ee57c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 122,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8U3G4",
  "selected_historical_entry_version": 122,
  "selected_historical_record_sha256": "71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc",
  "selected_historical_source_sequence_length": 816,
  "selected_historical_source_sequence_sha256": "efad9c6b7776bbc78e56d40d80cd2f860218a2783d4d092d0f3250c6908ee57c",
  "selected_historical_version": {
    "accession": "Q8U3G4",
    "database": "Swiss-Prot",
    "entryVersion": 122,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "TMCA_PYRFU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8U3G4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:29.260789+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U3G4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":123,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:29.260789+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U3G4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Pyrococcus\"],\"scientificName\":\"Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1)\",\"taxonId\":186497}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:29.260789+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U3G4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"}],\"value\":\"2.3.1.193\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"}],\"value\":\"tRNA(Met) cytidine acetyltransferase TmcA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:29.260789+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U3G4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.193\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"}],\"name\":\"cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:43788\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10693\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:32:29.260789+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U3G4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in RNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82211\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15704\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19834\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:32:29.260789+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U3G4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:53876\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:13670\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:13671\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:32:29.260789+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U3G4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in mRNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:58480\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15145\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:32:29.260789+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U3G4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U3G4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Sas-Chen A.\",\"Thomas J.M.\",\"Matzov D.\",\"Taoka M.\",\"Nance K.D.\",\"Nir R.\",\"Bryson K.M.\",\"Shachar R.\",\"Liman G.L.S.\",\"Burkhart B.W.\",\"Gamage S.T.\",\"Nobe Y.\",\"Briney C.A.\",\"Levy M.J.\",\"Fuchs R.T.\",\"Robb G.B.\",\"Hartmann J.\",\"Sharma S.\",\"Lin Q.\",\"Florens L.\",\"Washburn M.P.\",\"Isobe T.\",\"Santangelo T.J.\",\"Shalev-Benami M.\",\"Meier J.L.\",\"Schwartz S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32555463\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-020-2418-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"638\",\"id\":\"32555463\",\"journal\":\"Nature\",\"lastPage\":\"643\",\"publicationDate\":\"2020\",\"title\":\"Dynamic RNA acetylation revealed by quantitative cross-evolutionary mapping.\",\"volume\":\"583\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"COM1\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:29.260789+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0fe20cdbbebc894c8fe3f69fc06f7510e6c75ffbb40ef2bf5e5d4291d6d3c501",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U3G4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H1",
  "excerpt": "ID   TMCA_PYRFU              Reviewed;         816 AA.\nAC   Q8U3G4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2002, sequence version 1.\nDT   28-JAN-2026, entry version 122.\nDE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};\nDE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886};\nGN   Name=tmcA {ECO:0000255|HAMAP-Rule:MF_01886};\nGN   OrderedLocusNames=PF0504 {ECO:0000312|EMBL:AAL80628.1};\nOS   Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Pyrococcus.\nOX   NCBI_TaxID=186497;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:36.397993+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc",
  "url": "https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};\nDE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:36.397993+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc",
  "url": "https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRC   STRAIN=COM1;\nRX   PubMed=32555463; DOI=10.1038/s41586-020-2418-2;\nRA   Sas-Chen A., Thomas J.M., Matzov D., Taoka M., Nance K.D., Nir R.,\nRA   Bryson K.M., Shachar R., Liman G.L.S., Burkhart B.W., Gamage S.T., Nobe Y.,\nRA   Briney C.A., Levy M.J., Fuchs R.T., Robb G.B., Hartmann J., Sharma S.,\nRA   Lin Q., Florens L., Washburn M.P., Isobe T., Santangelo T.J.,\nRA   Shalev-Benami M., Meier J.L., Schwartz S.;\nRT   \"Dynamic RNA acetylation revealed by quantitative cross-evolutionary\nRT   mapping.\";\nRL   Nature 583:638-643(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:36.397993+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc",
  "url": "https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O =\nCC         N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate +\nCC         CoA + H(+); Xref=Rhea:RHEA:43788, Rhea:RHEA-COMP:10693, Rhea:RHEA-\nCC         COMP:10694, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         EC=2.3.1.193; Evidence={ECO:0000255|HAMAP-Rule:MF_01886};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:36.397993+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc",
  "url": "https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in RNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:82211, Rhea:RHEA-COMP:15704, Rhea:RHEA-COMP:19834,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000255|HAMAP-Rule:MF_01886,\nCC         ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:36.397993+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc",
  "url": "https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in tRNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:53876, Rhea:RHEA-COMP:13670, Rhea:RHEA-COMP:13671,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000255|HAMAP-Rule:MF_01886,\nCC         ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:36.397993+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc",
  "url": "https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in mRNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:58480, Rhea:RHEA-COMP:15145, Rhea:RHEA-COMP:15146,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000255|HAMAP-Rule:MF_01886,\nCC         ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:36.397993+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "71fd83a16afe57d79f100bc89ee9e946933b081e7fc9d9cb76bef95d0c12ebcc",
  "url": "https://rest.uniprot.org/unisave/Q8U3G4?format=txt&versions=122"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 75. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
