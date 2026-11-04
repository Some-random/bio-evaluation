# catalytic_activity_0058

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0058.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — 4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNKRDELIGLCIDFLAKVKDKTANANIERWLNENYGPDSETYQKISTLVIDGVAEGWAANDEISGPHYRRSRLCEPCAETFYFSITAVYMDSKGHELDNQQRTFRGDYHSHPYGELNMVIPLDEGAVLAGPLGWQGAGWTAPAPGSQHYPEVKNGALIAFFFLPAGRISYDFQAQG

[Multiple Choices]
A. a beta-lactam + H2O = a substituted beta-amino acid
B. 4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)
C. (S)-norprotosinomenine + S-adenosyl-L-methionine = (S)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)
D. L-leucine(in) = L-leucine(out)
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

> The supplied sequence exactly matches the source record, which annotates this protein with the reaction in option B and cites experimental evidence (ECO:0000269, PubMed 11157934). This supports the key, though the cited paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 176-residue sequence is a compact soluble protein, not a membrane transporter, making D unlikely. It also lacks an obvious SAM-dependent methyltransferase signature, arguing against C; and it lacks the characteristic catalytic motifs of common beta-lactamases, weakening A. These transferable sequence and family-pattern cues make B the best choice, although they do not independently establish the exact reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The alternatives differ in protein type and enzyme-family patterns that can be assessed probabilistically from the sequence. The inference is not certain, but it meaningfully favors B without requiring recall of this protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reaction choices are distinct, and the available evidence supports B rather than identifying another comparably defensible option.


### Important caveats

- The experimental-evidence citation supports the expected answer but was reviewer-only and was not available to the evaluated model.
- Sequence-based exclusion of distractors is probabilistic; the original input alone does not prove the exact catalytic reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 176-residue sequence is a compact soluble protein, not a membrane transporter, making D unlikely. It also lacks an obvious SAM-dependent methyltransferase signature, arguing against C; and it lacks the characteristic catalytic motifs of common beta-lactamases, weakening A. These transferable sequence and family-pattern cues make B the best choice, although they do not independently establish the exact reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The alternatives differ in protein type and enzyme-family patterns that can be assessed probabilistically from the sequence. The inference is not certain, but it meaningfully favors B without requiring recall of this protein's database entry."
  },
  "case_id": "catalytic_activity_0058",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the source record, which annotates this protein with the reaction in option B and cites experimental evidence (ECO:0000269, PubMed 11157934). This supports the key, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The experimental-evidence citation supports the expected answer but was reviewer-only and was not available to the evaluated model.",
    "Sequence-based exclusion of distractors is probabilistic; the original input alone does not prove the exact catalytic reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction choices are distinct, and the available evidence supports B rather than identifying another comparably defensible option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the source record, which annotates this protein with the reaction in option B and cites experimental evidence (ECO:0000269, PubMed 11157934). This supports the key, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 176-residue sequence is a compact soluble protein, not a membrane transporter, making D unlikely. It also lacks an obvious SAM-dependent methyltransferase signature, arguing against C; and it lacks the characteristic catalytic motifs of common beta-lactamases, weakening A. These transferable sequence and family-pattern cues make B the best choice, although they do not independently establish the exact reaction.",
    "missing_item_specific_fact": "",
    "reason": "The alternatives differ in protein type and enzyme-family patterns that can be assessed probabilistically from the sequence. The inference is not certain, but it meaningfully favors B without requiring recall of this protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction choices are distinct, and the available evidence supports B rather than identifying another comparably defensible option."
  },
  "important_caveats": [
    "The experimental-evidence citation supports the expected answer but was reviewer-only and was not available to the evaluated model.",
    "Sequence-based exclusion of distractors is probabilistic; the original input alone does not prove the exact catalytic reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9FD33 (PNBB_PSEPU) is annotated as 4-hydroxylaminobenzoate lyase (EC 4.3.3.-) with the exact reaction '4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)' supported by experimental evidence (ECO:0000269, PubMed:11157934). The benchmark sequence (176 AA) matches the UniProt sequence exactly. The annotation is experimentally determined, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 176-residue sequence provides several transferable discriminators against the distractors. (1) Choice D (L-leucine transporter) is effectively eliminated: membrane transporters require multiple transmembrane α-helices (typically 10-14 TM segments, ~300-500+ AA); a 176 AA protein cannot accommodate this topology. (2) Choice C (SAM-dependent methyltransferase) is unlikely: SAM-binding methyltransferases possess a conserved Rossmann-like fold with characteristic motifs (e.g., VLDLGCG, the β-sheet–α-helix–β-sheet sandwich) and are typically 200-400 AA; no such motifs are apparent in this sequence. (3) Choice A (β-lactamase) is disfavored: class A β-lactamases carry the SXXK catalytic motif and are usually 250-350 AA; class C/D are larger still. The 176 AA length and absence of a recognizable SXXK motif argue against this. (4) Choice B (4-hydroxylaminobenzoate lyase, EC 4.3.3.-) belongs to the Ntn-hydrolase superfamily, which characteristically comprises small proteins (~150-300 AA) with an N-terminal nucleophile and a compact αββα fold. The 176 AA size and the N-terminal region (MNKRDEL…) are consistent with this family. While positive identification of the specific EC 4.3.3.- subclass within Ntn-hydrolases is not trivially read from sequence, the combined size-based eliminations of D, C, and A leave B as the most consistent option. This is a defensible probabilistic inference from family-level knowledge rather than a guaranteed identification.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use protein-family size constraints (transporters are large multi-TM proteins; β-lactamases carry SXXK and are typically >250 AA; SAM methyltransferases have conserved Rossmann motifs and are >200 AA) to eliminate D, C, and A. The remaining option B (Ntn-hydrolase superfamily member, EC 4.3.3.-) is consistent with the 176 AA length and the general fold characteristics of small Ntn-hydrolases. The positive identification of the exact EC subclass within Ntn-hydrolases is probabilistic, but the elimination of the three distractors provides a meaningful basis for selecting B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The size-based elimination of D is near-certain, and the absence of SAM-binding motifs and SXXK motifs makes C and A substantially less likely. While a very small β-lactamase variant is theoretically conceivable, none of the well-characterized β-lactamase classes match a 176 AA protein lacking SXXK or metallo-β-lactamase motifs. No genuine ambiguity among the four offered choices is identified.


### Important caveats

- The positive identification of B specifically (as opposed to another Ntn-hydrolase subclass) relies on elimination of the other three choices rather than a unique sequence signature for EC 4.3.3.-.
- The N-terminal nucleophile in Ntn-hydrolases is typically Ser, Cys, Thr, or Met; the sequence begins with MNKRDEL, where Met could serve as the nucleophile if retained, but this is not a definitive diagnostic from sequence alone.
- The UniProt annotation carries experimental evidence (ECO:0000269), strengthening the key, but the model must reason from sequence features rather than access the database entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 176-residue sequence provides several transferable discriminators against the distractors. (1) Choice D (L-leucine transporter) is effectively eliminated: membrane transporters require multiple transmembrane α-helices (typically 10-14 TM segments, ~300-500+ AA); a 176 AA protein cannot accommodate this topology. (2) Choice C (SAM-dependent methyltransferase) is unlikely: SAM-binding methyltransferases possess a conserved Rossmann-like fold with characteristic motifs (e.g., VLDLGCG, the β-sheet–α-helix–β-sheet sandwich) and are typically 200-400 AA; no such motifs are apparent in this sequence. (3) Choice A (β-lactamase) is disfavored: class A β-lactamases carry the SXXK catalytic motif and are usually 250-350 AA; class C/D are larger still. The 176 AA length and absence of a recognizable SXXK motif argue against this. (4) Choice B (4-hydroxylaminobenzoate lyase, EC 4.3.3.-) belongs to the Ntn-hydrolase superfamily, which characteristically comprises small proteins (~150-300 AA) with an N-terminal nucleophile and a compact αββα fold. The 176 AA size and the N-terminal region (MNKRDEL…) are consistent with this family. While positive identification of the specific EC 4.3.3.- subclass within Ntn-hydrolases is not trivially read from sequence, the combined size-based eliminations of D, C, and A leave B as the most consistent option. This is a defensible probabilistic inference from family-level knowledge rather than a guaranteed identification.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use protein-family size constraints (transporters are large multi-TM proteins; β-lactamases carry SXXK and are typically >250 AA; SAM methyltransferases have conserved Rossmann motifs and are >200 AA) to eliminate D, C, and A. The remaining option B (Ntn-hydrolase superfamily member, EC 4.3.3.-) is consistent with the 176 AA length and the general fold characteristics of small Ntn-hydrolases. The positive identification of the exact EC subclass within Ntn-hydrolases is probabilistic, but the elimination of the three distractors provides a meaningful basis for selecting B."
  },
  "case_id": "catalytic_activity_0058",
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
    "reason": "The UniProt entry Q9FD33 (PNBB_PSEPU) is annotated as 4-hydroxylaminobenzoate lyase (EC 4.3.3.-) with the exact reaction '4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)' supported by experimental evidence (ECO:0000269, PubMed:11157934). The benchmark sequence (176 AA) matches the UniProt sequence exactly. The annotation is experimentally determined, not merely computational."
  },
  "important_caveats": [
    "The positive identification of B specifically (as opposed to another Ntn-hydrolase subclass) relies on elimination of the other three choices rather than a unique sequence signature for EC 4.3.3.-.",
    "The N-terminal nucleophile in Ntn-hydrolases is typically Ser, Cys, Thr, or Met; the sequence begins with MNKRDEL, where Met could serve as the nucleophile if retained, but this is not a definitive diagnostic from sequence alone.",
    "The UniProt annotation carries experimental evidence (ECO:0000269), strengthening the key, but the model must reason from sequence features rather than access the database entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size-based elimination of D is near-certain, and the absence of SAM-binding motifs and SXXK motifs makes C and A substantially less likely. While a very small β-lactamase variant is theoretically conceivable, none of the well-characterized β-lactamase classes match a 176 AA protein lacking SXXK or metallo-β-lactamase motifs. No genuine ambiguity among the four offered choices is identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9FD33 (PNBB_PSEPU) is annotated as 4-hydroxylaminobenzoate lyase (EC 4.3.3.-) with the exact reaction '4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)' supported by experimental evidence (ECO:0000269, PubMed:11157934). The benchmark sequence (176 AA) matches the UniProt sequence exactly. The annotation is experimentally determined, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 176-residue sequence provides several transferable discriminators against the distractors. (1) Choice D (L-leucine transporter) is effectively eliminated: membrane transporters require multiple transmembrane α-helices (typically 10-14 TM segments, ~300-500+ AA); a 176 AA protein cannot accommodate this topology. (2) Choice C (SAM-dependent methyltransferase) is unlikely: SAM-binding methyltransferases possess a conserved Rossmann-like fold with characteristic motifs (e.g., VLDLGCG, the β-sheet–α-helix–β-sheet sandwich) and are typically 200-400 AA; no such motifs are apparent in this sequence. (3) Choice A (β-lactamase) is disfavored: class A β-lactamases carry the SXXK catalytic motif and are usually 250-350 AA; class C/D are larger still. The 176 AA length and absence of a recognizable SXXK motif argue against this. (4) Choice B (4-hydroxylaminobenzoate lyase, EC 4.3.3.-) belongs to the Ntn-hydrolase superfamily, which characteristically comprises small proteins (~150-300 AA) with an N-terminal nucleophile and a compact αββα fold. The 176 AA size and the N-terminal region (MNKRDEL…) are consistent with this family. While positive identification of the specific EC 4.3.3.- subclass within Ntn-hydrolases is not trivially read from sequence, the combined size-based eliminations of D, C, and A leave B as the most consistent option. This is a defensible probabilistic inference from family-level knowledge rather than a guaranteed identification.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use protein-family size constraints (transporters are large multi-TM proteins; β-lactamases carry SXXK and are typically >250 AA; SAM methyltransferases have conserved Rossmann motifs and are >200 AA) to eliminate D, C, and A. The remaining option B (Ntn-hydrolase superfamily member, EC 4.3.3.-) is consistent with the 176 AA length and the general fold characteristics of small Ntn-hydrolases. The positive identification of the exact EC subclass within Ntn-hydrolases is probabilistic, but the elimination of the three distractors provides a meaningful basis for selecting B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size-based elimination of D is near-certain, and the absence of SAM-binding motifs and SXXK motifs makes C and A substantially less likely. While a very small β-lactamase variant is theoretically conceivable, none of the well-characterized β-lactamase classes match a 176 AA protein lacking SXXK or metallo-β-lactamase motifs. No genuine ambiguity among the four offered choices is identified."
  },
  "important_caveats": [
    "The positive identification of B specifically (as opposed to another Ntn-hydrolase subclass) relies on elimination of the other three choices rather than a unique sequence signature for EC 4.3.3.-.",
    "The N-terminal nucleophile in Ntn-hydrolases is typically Ser, Cys, Thr, or Met; the sequence begins with MNKRDEL, where Met could serve as the nucleophile if retained, but this is not a definitive diagnostic from sequence alone.",
    "The UniProt annotation carries experimental evidence (ECO:0000269), strengthening the key, but the model must reason from sequence features rather than access the database entry."
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
  "benchmark_sequence_length": 176,
  "benchmark_sequence_sha256": "995d9173c0b914450e19cad5a6d0171c45e8079f5dc92650073a58f5a366b849",
  "current_entry_audit": {
    "entryVersion": 36,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2001-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 176,
  "current_source_sequence_sha256": "995d9173c0b914450e19cad5a6d0171c45e8079f5dc92650073a58f5a366b849",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 36,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9FD33",
  "selected_historical_entry_version": 36,
  "selected_historical_record_sha256": "6691247797bb30cca466436872237092529deaffd2d4d5e25ce14a2e63546333",
  "selected_historical_source_sequence_length": 176,
  "selected_historical_source_sequence_sha256": "995d9173c0b914450e19cad5a6d0171c45e8079f5dc92650073a58f5a366b849",
  "selected_historical_version": {
    "accession": "Q9FD33",
    "database": "Swiss-Prot",
    "entryVersion": 36,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PNBB_PSEPU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD33.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9FD33\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:47.631253+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD33.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD33.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":36,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2001-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:47.631253+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD33.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD33.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Arthrobacter siderocapsulatus\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas putida\",\"taxonId\":303}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:47.631253+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD33.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD33.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"value\":\"4.3.3.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"value\":\"4-hydroxylaminobenzoate lyase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:47.631253+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD33.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD33.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80204\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"name\":\"4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80203\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:28938\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:36241\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231457\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:47.631253+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD33.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD33.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Hughes M.A.\",\"Williams P.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11157934\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.183.4.1225-1232.2001\"}],\"citationType\":\"journal article\",\"firstPage\":\"1225\",\"id\":\"11157934\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"1232\",\"publicationDate\":\"2001\",\"title\":\"Cloning and characterisation of the pnb genes, encoding enzymes for 4-nitrobenzoate catabolism in Pseudomonas putida TW3.\",\"volume\":\"183\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"TW3\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:32:47.631253+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD33.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H1",
  "excerpt": "ID   PNBB_PSEPU              Reviewed;         176 AA.\nAC   Q9FD33;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2001, sequence version 1.\nDT   28-JAN-2026, entry version 36.\nDE   RecName: Full=4-hydroxylaminobenzoate lyase {ECO:0000303|PubMed:11157934};\nDE            EC=4.3.3.- {ECO:0000269|PubMed:11157934};\nGN   Name=pnbB {ECO:0000303|PubMed:11157934};\nOS   Pseudomonas putida (Arthrobacter siderocapsulatus).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=303;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.128518+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6691247797bb30cca466436872237092529deaffd2d4d5e25ce14a2e63546333",
  "url": "https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4-hydroxylaminobenzoate lyase {ECO:0000303|PubMed:11157934};\nDE            EC=4.3.3.- {ECO:0000269|PubMed:11157934};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.128518+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6691247797bb30cca466436872237092529deaffd2d4d5e25ce14a2e63546333",
  "url": "https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=TW3;\nRX   PubMed=11157934; DOI=10.1128/jb.183.4.1225-1232.2001;\nRA   Hughes M.A., Williams P.A.;\nRT   \"Cloning and characterisation of the pnb genes, encoding enzymes for 4-\nRT   nitrobenzoate catabolism in Pseudomonas putida TW3.\";\nRL   J. Bacteriol. 183:1225-1232(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.128518+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 13-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6691247797bb30cca466436872237092529deaffd2d4d5e25ce14a2e63546333",
  "url": "https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate +\nCC         NH4(+); Xref=Rhea:RHEA:80203, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:28938, ChEBI:CHEBI:36241, ChEBI:CHEBI:231457;\nCC         Evidence={ECO:0000269|PubMed:11157934};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80204;\nCC         Evidence={ECO:0000269|PubMed:11157934};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.128518+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6691247797bb30cca466436872237092529deaffd2d4d5e25ce14a2e63546333",
  "url": "https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 58. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
