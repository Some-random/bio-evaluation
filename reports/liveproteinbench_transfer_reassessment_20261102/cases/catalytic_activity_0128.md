# catalytic_activity_0128

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0128.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — 4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NAD(+) + H2O

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MALLTDDFDAVVASRRAVRAFLPTPISRKLISEIIDIARLAPSNSNTQPWSIHVLTGEPKQALSALLGIAHNDPSADPLAHLPDDLARKYRERQEKWGELFYGLHQIDKCDDAGRARVSGLNFDFFGAPVGLIFTIDSNLKKYSWLDYGLFLQTLMLTARSRGLSTCPQVSFARFQSLIKDFLHLDDSQEIVCGMSLGYADENATVNSLRMPREMAQGFTHFMGFDR

[Multiple Choices]
A. 4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NAD(+) + H2O
B. (S,S)-2,5-di-(p-hydroxybenzyl)piperazine + reduced [NADPH--hemoprotein reductase] + O2 = (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexane]-2',5'-dien-4'-one + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
C. L-arabinitol + NAD(+) = L-xylulose + NADH + H(+)
D. AH2 + 2 S-adenosyl-L-methionine = 2 5'-deoxyadenosin-5'-yl radical + 2 L-methionine + A + 2 H(+)
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

> The sequence-matched UniProt record gives the reaction in option A as the catalytic activity and assigns it ECO:0000269 evidence linked to a publication, which indicates experimental evidence. The primary paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 227-residue sequence is more consistent with a compact soluble reductase than with the alternatives' characteristic enzyme classes. It lacks the conspicuous CxxxCxxC motif expected for a radical-SAM enzyme (D) and the heme-binding cysteine motif and larger architecture characteristic of a P450-type enzyme (B); it also lacks an obvious N-terminal dinucleotide-binding motif expected for many NAD-dependent polyol dehydrogenases (C). These transferable sequence/class patterns make the NADH-dependent reduction in A the best fit among the offered choices, though they do not by themselves prove its exact substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choices correspond to substantially different enzyme classes and mechanisms, and sequence length and recognizable motif patterns provide a meaningful, probabilistic basis for distinguishing A without knowing this protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered reaction has a comparably strong fit to the sequence and its likely enzyme class.


### Important caveats

- The reaction annotation is experimental evidence as represented in the database, but the cited primary study was not independently assessed.
- The sequence-based argument favors A among these choices; it is not an independent demonstration of the exact substrate or product.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 227-residue sequence is more consistent with a compact soluble reductase than with the alternatives' characteristic enzyme classes. It lacks the conspicuous CxxxCxxC motif expected for a radical-SAM enzyme (D) and the heme-binding cysteine motif and larger architecture characteristic of a P450-type enzyme (B); it also lacks an obvious N-terminal dinucleotide-binding motif expected for many NAD-dependent polyol dehydrogenases (C). These transferable sequence/class patterns make the NADH-dependent reduction in A the best fit among the offered choices, though they do not by themselves prove its exact substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choices correspond to substantially different enzyme classes and mechanisms, and sequence length and recognizable motif patterns provide a meaningful, probabilistic basis for distinguishing A without knowing this protein's database annotation."
  },
  "case_id": "catalytic_activity_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record gives the reaction in option A as the catalytic activity and assigns it ECO:0000269 evidence linked to a publication, which indicates experimental evidence. The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reaction annotation is experimental evidence as represented in the database, but the cited primary study was not independently assessed.",
    "The sequence-based argument favors A among these choices; it is not an independent demonstration of the exact substrate or product."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction has a comparably strong fit to the sequence and its likely enzyme class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record gives the reaction in option A as the catalytic activity and assigns it ECO:0000269 evidence linked to a publication, which indicates experimental evidence. The primary paper was not independently reviewed here.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 227-residue sequence is more consistent with a compact soluble reductase than with the alternatives' characteristic enzyme classes. It lacks the conspicuous CxxxCxxC motif expected for a radical-SAM enzyme (D) and the heme-binding cysteine motif and larger architecture characteristic of a P450-type enzyme (B); it also lacks an obvious N-terminal dinucleotide-binding motif expected for many NAD-dependent polyol dehydrogenases (C). These transferable sequence/class patterns make the NADH-dependent reduction in A the best fit among the offered choices, though they do not by themselves prove its exact substrate.",
    "missing_item_specific_fact": "",
    "reason": "The choices correspond to substantially different enzyme classes and mechanisms, and sequence length and recognizable motif patterns provide a meaningful, probabilistic basis for distinguishing A without knowing this protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction has a comparably strong fit to the sequence and its likely enzyme class."
  },
  "important_caveats": [
    "The reaction annotation is experimental evidence as represented in the database, but the cited primary study was not independently assessed.",
    "The sequence-based argument favors A among these choices; it is not an independent demonstration of the exact substrate or product."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9FD36 (PNBA_PSEPU) explicitly annotates the catalytic activity as '4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NAD(+) + H2O' with experimental evidence (ECO:0000269, PubMed:11157934). The sequence in the question matches the UniProt sequence (227 aa, SHA-256 matched). Choice A is verbatim the annotated reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 227-aa sequence contains motifs consistent with an NAD(P)H-dependent flavoprotein oxidoreductase: a 'GLNFD' flavin-binding-like motif, a Rossmann-like 'GAPVGLIFTID' region, and a C-terminal 'GMSLGY' segment. These features point toward a flavoprotein reductase architecture. Among the four choices: (B) requires a P450 or P450-reductase architecture (typically 400–680 aa with FxxGxxxCxG heme-binding or FAD/FMN two-domain structure) — clearly incompatible with a 227-aa single-domain protein; (D) requires a radical SAM enzyme with the diagnostic CX3CX2C &#91;4Fe-4S&#93; cluster motif — absent from this sequence; (C) describes a sugar-alcohol dehydrogenase (SDR family, typically 250–350 aa with a TGxxxGG NAD-binding motif and no flavin) — the sequence lacks TGxxxGG and instead shows flavoprotein motifs. Only (A) describes a flavoprotein NADH-dependent nitroreductase reaction, consistent with the ~227-aa length, flavin-binding motifs, and NADH cofactor usage inferred from the Rossmann-like architecture. This elimination logic relies on family-level architectural knowledge (P450 size, radical SAM motifs, SDR motifs, flavoprotein reductase size/motifs) transferable from other proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use sequence length (~227 aa), absence of radical SAM CX3CX2C motif, absence of SDR TGxxxGG motif, absence of P450 heme-binding motif, and presence of flavoprotein-like motifs (GLNFD, Rossmann-like GAPVGLIFTID) to eliminate B, C, and D, leaving A as the only flavoprotein NADH-dependent reductase reaction among the choices. This is a defensible family/architecture-based inference from transferable protein knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The architectural elimination is clear: B requires a much larger P450/P450R system, D requires radical SAM motifs not present, and C requires SDR architecture incompatible with the observed flavoprotein motifs. Only A matches the flavoprotein NADH-dependent reductase architecture indicated by the sequence.


### Important caveats

- The reviewer-only evidence confirms the UniProt annotation with experimental evidence code (ECO:0000269), but this annotation was not available to the evaluated model.
- The sequence-to-family inference (flavoprotein reductase) is probabilistic; the specific substrate (4-nitrobenzoate vs. other nitroaromatics) cannot be determined from sequence alone, but among the four offered choices only A is a flavoprotein NADH-dependent nitroreductase reaction.
- The protein (PnbA) is not a classic NfsB-type nitroreductase but belongs to a distinct 4-nitrobenzoate reductase family; nonetheless, the broad architectural elimination of B, C, and D remains valid.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 227-aa sequence contains motifs consistent with an NAD(P)H-dependent flavoprotein oxidoreductase: a 'GLNFD' flavin-binding-like motif, a Rossmann-like 'GAPVGLIFTID' region, and a C-terminal 'GMSLGY' segment. These features point toward a flavoprotein reductase architecture. Among the four choices: (B) requires a P450 or P450-reductase architecture (typically 400–680 aa with FxxGxxxCxG heme-binding or FAD/FMN two-domain structure) — clearly incompatible with a 227-aa single-domain protein; (D) requires a radical SAM enzyme with the diagnostic CX3CX2C [4Fe-4S] cluster motif — absent from this sequence; (C) describes a sugar-alcohol dehydrogenase (SDR family, typically 250–350 aa with a TGxxxGG NAD-binding motif and no flavin) — the sequence lacks TGxxxGG and instead shows flavoprotein motifs. Only (A) describes a flavoprotein NADH-dependent nitroreductase reaction, consistent with the ~227-aa length, flavin-binding motifs, and NADH cofactor usage inferred from the Rossmann-like architecture. This elimination logic relies on family-level architectural knowledge (P450 size, radical SAM motifs, SDR motifs, flavoprotein reductase size/motifs) transferable from other proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use sequence length (~227 aa), absence of radical SAM CX3CX2C motif, absence of SDR TGxxxGG motif, absence of P450 heme-binding motif, and presence of flavoprotein-like motifs (GLNFD, Rossmann-like GAPVGLIFTID) to eliminate B, C, and D, leaving A as the only flavoprotein NADH-dependent reductase reaction among the choices. This is a defensible family/architecture-based inference from transferable protein knowledge."
  },
  "case_id": "catalytic_activity_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9FD36 (PNBA_PSEPU) explicitly annotates the catalytic activity as '4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NAD(+) + H2O' with experimental evidence (ECO:0000269, PubMed:11157934). The sequence in the question matches the UniProt sequence (227 aa, SHA-256 matched). Choice A is verbatim the annotated reaction."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the UniProt annotation with experimental evidence code (ECO:0000269), but this annotation was not available to the evaluated model.",
    "The sequence-to-family inference (flavoprotein reductase) is probabilistic; the specific substrate (4-nitrobenzoate vs. other nitroaromatics) cannot be determined from sequence alone, but among the four offered choices only A is a flavoprotein NADH-dependent nitroreductase reaction.",
    "The protein (PnbA) is not a classic NfsB-type nitroreductase but belongs to a distinct 4-nitrobenzoate reductase family; nonetheless, the broad architectural elimination of B, C, and D remains valid."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The architectural elimination is clear: B requires a much larger P450/P450R system, D requires radical SAM motifs not present, and C requires SDR architecture incompatible with the observed flavoprotein motifs. Only A matches the flavoprotein NADH-dependent reductase architecture indicated by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9FD36 (PNBA_PSEPU) explicitly annotates the catalytic activity as '4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NAD(+) + H2O' with experimental evidence (ECO:0000269, PubMed:11157934). The sequence in the question matches the UniProt sequence (227 aa, SHA-256 matched). Choice A is verbatim the annotated reaction.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 227-aa sequence contains motifs consistent with an NAD(P)H-dependent flavoprotein oxidoreductase: a 'GLNFD' flavin-binding-like motif, a Rossmann-like 'GAPVGLIFTID' region, and a C-terminal 'GMSLGY' segment. These features point toward a flavoprotein reductase architecture. Among the four choices: (B) requires a P450 or P450-reductase architecture (typically 400–680 aa with FxxGxxxCxG heme-binding or FAD/FMN two-domain structure) — clearly incompatible with a 227-aa single-domain protein; (D) requires a radical SAM enzyme with the diagnostic CX3CX2C [4Fe-4S] cluster motif — absent from this sequence; (C) describes a sugar-alcohol dehydrogenase (SDR family, typically 250–350 aa with a TGxxxGG NAD-binding motif and no flavin) — the sequence lacks TGxxxGG and instead shows flavoprotein motifs. Only (A) describes a flavoprotein NADH-dependent nitroreductase reaction, consistent with the ~227-aa length, flavin-binding motifs, and NADH cofactor usage inferred from the Rossmann-like architecture. This elimination logic relies on family-level architectural knowledge (P450 size, radical SAM motifs, SDR motifs, flavoprotein reductase size/motifs) transferable from other proteins.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use sequence length (~227 aa), absence of radical SAM CX3CX2C motif, absence of SDR TGxxxGG motif, absence of P450 heme-binding motif, and presence of flavoprotein-like motifs (GLNFD, Rossmann-like GAPVGLIFTID) to eliminate B, C, and D, leaving A as the only flavoprotein NADH-dependent reductase reaction among the choices. This is a defensible family/architecture-based inference from transferable protein knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The architectural elimination is clear: B requires a much larger P450/P450R system, D requires radical SAM motifs not present, and C requires SDR architecture incompatible with the observed flavoprotein motifs. Only A matches the flavoprotein NADH-dependent reductase architecture indicated by the sequence."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the UniProt annotation with experimental evidence code (ECO:0000269), but this annotation was not available to the evaluated model.",
    "The sequence-to-family inference (flavoprotein reductase) is probabilistic; the specific substrate (4-nitrobenzoate vs. other nitroaromatics) cannot be determined from sequence alone, but among the four offered choices only A is a flavoprotein NADH-dependent nitroreductase reaction.",
    "The protein (PnbA) is not a classic NfsB-type nitroreductase but belongs to a distinct 4-nitrobenzoate reductase family; nonetheless, the broad architectural elimination of B, C, and D remains valid."
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
  "benchmark_sequence_length": 227,
  "benchmark_sequence_sha256": "3b51488ac857ad147730e4507dad5133e7f22b0c61382381fe8906536f65a0c4",
  "current_entry_audit": {
    "entryVersion": 60,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 227,
  "current_source_sequence_sha256": "3b51488ac857ad147730e4507dad5133e7f22b0c61382381fe8906536f65a0c4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9FD36",
  "selected_historical_entry_version": 59,
  "selected_historical_record_sha256": "b8e05036a664f774b75486960f2bb65b17e0fc9481338a912a9e57c2a38f1637",
  "selected_historical_source_sequence_length": 227,
  "selected_historical_source_sequence_sha256": "3b51488ac857ad147730e4507dad5133e7f22b0c61382381fe8906536f65a0c4",
  "selected_historical_version": {
    "accession": "Q9FD36",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PNBA_PSEPU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9FD36\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":60,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Arthrobacter siderocapsulatus\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas putida\",\"taxonId\":303}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"value\":\"1.7.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"value\":\"4-nitrobenzoate reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"value\":\"4NBen reductase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80200\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"name\":\"4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NAD(+) + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80199\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142863\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231457\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Hughes M.A.\",\"Williams P.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11157934\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.183.4.1225-1232.2001\"}],\"citationType\":\"journal article\",\"firstPage\":\"1225\",\"id\":\"11157934\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"1232\",\"publicationDate\":\"2001\",\"title\":\"Cloning and characterisation of the pnb genes, encoding enzymes for 4-nitrobenzoate catabolism in Pseudomonas putida TW3.\",\"volume\":\"183\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"TW3\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H1",
  "excerpt": "ID   PNBA_PSEPU              Reviewed;         227 AA.\nAC   Q9FD36;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2001, sequence version 1.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=4-nitrobenzoate reductase {ECO:0000303|PubMed:11157934};\nDE            Short=4NBen reductase {ECO:0000303|PubMed:11157934};\nDE            EC=1.7.1.- {ECO:0000269|PubMed:11157934};\nGN   Name=pnbA {ECO:0000303|PubMed:11157934};\nOS   Pseudomonas putida (Arthrobacter siderocapsulatus).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=303;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:49.936444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8e05036a664f774b75486960f2bb65b17e0fc9481338a912a9e57c2a38f1637",
  "url": "https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4-nitrobenzoate reductase {ECO:0000303|PubMed:11157934};\nDE            Short=4NBen reductase {ECO:0000303|PubMed:11157934};\nDE            EC=1.7.1.- {ECO:0000269|PubMed:11157934};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:49.936444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8e05036a664f774b75486960f2bb65b17e0fc9481338a912a9e57c2a38f1637",
  "url": "https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=TW3;\nRX   PubMed=11157934; DOI=10.1128/jb.183.4.1225-1232.2001;\nRA   Hughes M.A., Williams P.A.;\nRT   \"Cloning and characterisation of the pnb genes, encoding enzymes for 4-\nRT   nitrobenzoate catabolism in Pseudomonas putida TW3.\";\nRL   J. Bacteriol. 183:1225-1232(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:49.936444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8e05036a664f774b75486960f2bb65b17e0fc9481338a912a9e57c2a38f1637",
  "url": "https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate +\nCC         2 NAD(+) + H2O; Xref=Rhea:RHEA:80199, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57540, ChEBI:CHEBI:57945,\nCC         ChEBI:CHEBI:142863, ChEBI:CHEBI:231457;\nCC         Evidence={ECO:0000269|PubMed:11157934};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80200;\nCC         Evidence={ECO:0000269|PubMed:11157934};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:49.936444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8e05036a664f774b75486960f2bb65b17e0fc9481338a912a9e57c2a38f1637",
  "url": "https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
