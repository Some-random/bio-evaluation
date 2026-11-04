# EC_number_0057

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0057.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.2.1.11

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTPSKKRCGVLGATGAVGTRFILLLEQSPLLELVAVGASERSAGKKYRDAVRWKQASPMPASVADLTVRRCAPSEFSDCDIIFSGLDPVAAGDIEMAFLKANFAVFSNAKNYRLDPIVPLVVPLVNAGHIDVIPAQRKHYGLDKGLIVCNSNCAVVGLVIPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPFIPGEEGKIATESRKILGNLNPDLAGFSDQQPLQVSVACNRVPVLDGHTVCASLRFVNRPAPTASQVRDALREYKSEVQLLGCPSAPRQAIHVLDDVDRPQPRLDRDTEAGYACSVGRIREDDSGVFDIQFVALSHNTVLGASGSSILNAESAILKGYI

[Multiple Choices]
A. 1.2.1.46
B. 2.7.8.7
C. 2.3.1.31
D. 1.2.1.11
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

> The sequence-matched UniProt record assigns EC 1.2.1.11 and names the enzyme aspartate-semialdehyde dehydrogenase. Its catalytic-activity annotation gives the corresponding reaction and cites experimental evidence (ECO:0000269).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a glycine-rich N-terminal nucleotide-binding region and a conserved cysteine-containing region consistent with the aspartate-semialdehyde dehydrogenase family. Family-level knowledge links that enzyme to EC 1.2.1.11, distinguishing choice D from the offered alternatives. These sequence clues support a family inference rather than independently proving the exact reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could use transferable enzyme-family and sequence-pattern knowledge to favor D; it need not know this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level inference points to one offered EC number, and the sequence-matched source annotation supports that same choice.


### Important caveats

- The experimental evidence is reported through database annotations citing publications; the primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich N-terminal nucleotide-binding region and a conserved cysteine-containing region consistent with the aspartate-semialdehyde dehydrogenase family. Family-level knowledge links that enzyme to EC 1.2.1.11, distinguishing choice D from the offered alternatives. These sequence clues support a family inference rather than independently proving the exact reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use transferable enzyme-family and sequence-pattern knowledge to favor D; it need not know this exact protein's database entry."
  },
  "case_id": "EC_number_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.2.1.11 and names the enzyme aspartate-semialdehyde dehydrogenase. Its catalytic-activity annotation gives the corresponding reaction and cites experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The experimental evidence is reported through database annotations citing publications; the primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference points to one offered EC number, and the sequence-matched source annotation supports that same choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.2.1.11 and names the enzyme aspartate-semialdehyde dehydrogenase. Its catalytic-activity annotation gives the corresponding reaction and cites experimental evidence (ECO:0000269).",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a glycine-rich N-terminal nucleotide-binding region and a conserved cysteine-containing region consistent with the aspartate-semialdehyde dehydrogenase family. Family-level knowledge links that enzyme to EC 1.2.1.11, distinguishing choice D from the offered alternatives. These sequence clues support a family inference rather than independently proving the exact reaction.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use transferable enzyme-family and sequence-pattern knowledge to favor D; it need not know this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference points to one offered EC number, and the sequence-matched source annotation supports that same choice."
  },
  "important_caveats": [
    "The experimental evidence is reported through database annotations citing publications; the primary studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A179UL48 (sequence matched, 362 aa) is annotated as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, supported by experimental evidence codes ECO:0000269 from two PubMed references (29608391, 30107909) reporting functional assays and X-ray crystallography. The catalytic activity (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is explicitly confirmed. The expected answer D (1.2.1.11) is fully supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Two layers of transferable knowledge distinguish the answer. (1) The N-terminal motif 'GVLGATGAVG' contains a canonical Rossmann-fold NAD(P)-binding pattern (GxGxxG), identifying the protein as an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). This immediately eliminates B (2.7.8.7, a transferase) and C (2.3.1.31, a transferase), both of which are unrelated enzyme classes with no Rossmann fold. (2) Between the remaining two oxidoreductase options—A (1.2.1.46, general aldehyde dehydrogenase NADP+) and D (1.2.1.11, aspartate-semialdehyde dehydrogenase)—the sequence contains hallmark ASADH-family motifs: the 'CNSNC' motif (a Cys-containing catalytic motif characteristic of ASADH's thiohemiacetal-forming mechanism) and 'GHTVCASLRF' containing the catalytic Cys in the conserved 'VCAS' context. General aldehyde dehydrogenases (1.2.1.x family, e.g., ALDH2) instead feature a 'CAG' catalytic motif. The ~362-aa length, dimeric architecture, and NADP+-selective Rossmann fold are all consistent with fungal ASADH orthologs well characterized in the literature. These family-level sequence features are transferable knowledge from ASADH homologs across bacteria and fungi and meaningfully distinguish D from A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann fold eliminates the two transferase options. The specific Cys-containing motifs (CNSNC, VCAS) are well-documented family signatures of ASADH, distinct from the CAG motif of general aldehyde dehydrogenases. A knowledgeable model recognizing these motifs from ASADH homologs (e.g., E. coli, yeast, fungal orthologs) can credibly select D over A without needing a target-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are clearly eliminated by the oxidoreductase Rossmann fold. Between A and D, the ASADH-specific Cys motifs (CNSNC, VCAS) and the NADP+-selective Rossmann fold pattern provide a clear family-level distinction favoring D. No other option is genuinely defensible given these features.


### Important caveats

- Distinguishing 1.2.1.11 from 1.2.1.46 relies on recognizing ASADH-specific catalytic Cys motifs versus general ALDH motifs; a model unfamiliar with the exact motif contexts might find A and D harder to separate, though the CNSNC/VCAS patterns are well-documented ASADH signatures.
- The UniProt annotation is supported by experimental evidence (PubMed, PDB), not merely computational inference.
- The sequence is from Blastomyces gilchristii, a fungal pathogen; fungal ASADH is a validated drug target, and its motifs are well characterized in the literature.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Two layers of transferable knowledge distinguish the answer. (1) The N-terminal motif 'GVLGATGAVG' contains a canonical Rossmann-fold NAD(P)-binding pattern (GxGxxG), identifying the protein as an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). This immediately eliminates B (2.7.8.7, a transferase) and C (2.3.1.31, a transferase), both of which are unrelated enzyme classes with no Rossmann fold. (2) Between the remaining two oxidoreductase options—A (1.2.1.46, general aldehyde dehydrogenase NADP+) and D (1.2.1.11, aspartate-semialdehyde dehydrogenase)—the sequence contains hallmark ASADH-family motifs: the 'CNSNC' motif (a Cys-containing catalytic motif characteristic of ASADH's thiohemiacetal-forming mechanism) and 'GHTVCASLRF' containing the catalytic Cys in the conserved 'VCAS' context. General aldehyde dehydrogenases (1.2.1.x family, e.g., ALDH2) instead feature a 'CAG' catalytic motif. The ~362-aa length, dimeric architecture, and NADP+-selective Rossmann fold are all consistent with fungal ASADH orthologs well characterized in the literature. These family-level sequence features are transferable knowledge from ASADH homologs across bacteria and fungi and meaningfully distinguish D from A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold eliminates the two transferase options. The specific Cys-containing motifs (CNSNC, VCAS) are well-documented family signatures of ASADH, distinct from the CAG motif of general aldehyde dehydrogenases. A knowledgeable model recognizing these motifs from ASADH homologs (e.g., E. coli, yeast, fungal orthologs) can credibly select D over A without needing a target-specific database lookup."
  },
  "case_id": "EC_number_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A179UL48 (sequence matched, 362 aa) is annotated as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, supported by experimental evidence codes ECO:0000269 from two PubMed references (29608391, 30107909) reporting functional assays and X-ray crystallography. The catalytic activity (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is explicitly confirmed. The expected answer D (1.2.1.11) is fully supported."
  },
  "important_caveats": [
    "Distinguishing 1.2.1.11 from 1.2.1.46 relies on recognizing ASADH-specific catalytic Cys motifs versus general ALDH motifs; a model unfamiliar with the exact motif contexts might find A and D harder to separate, though the CNSNC/VCAS patterns are well-documented ASADH signatures.",
    "The UniProt annotation is supported by experimental evidence (PubMed, PDB), not merely computational inference.",
    "The sequence is from Blastomyces gilchristii, a fungal pathogen; fungal ASADH is a validated drug target, and its motifs are well characterized in the literature."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are clearly eliminated by the oxidoreductase Rossmann fold. Between A and D, the ASADH-specific Cys motifs (CNSNC, VCAS) and the NADP+-selective Rossmann fold pattern provide a clear family-level distinction favoring D. No other option is genuinely defensible given these features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A179UL48 (sequence matched, 362 aa) is annotated as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, supported by experimental evidence codes ECO:0000269 from two PubMed references (29608391, 30107909) reporting functional assays and X-ray crystallography. The catalytic activity (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is explicitly confirmed. The expected answer D (1.2.1.11) is fully supported.",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Two layers of transferable knowledge distinguish the answer. (1) The N-terminal motif 'GVLGATGAVG' contains a canonical Rossmann-fold NAD(P)-binding pattern (GxGxxG), identifying the protein as an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). This immediately eliminates B (2.7.8.7, a transferase) and C (2.3.1.31, a transferase), both of which are unrelated enzyme classes with no Rossmann fold. (2) Between the remaining two oxidoreductase options—A (1.2.1.46, general aldehyde dehydrogenase NADP+) and D (1.2.1.11, aspartate-semialdehyde dehydrogenase)—the sequence contains hallmark ASADH-family motifs: the 'CNSNC' motif (a Cys-containing catalytic motif characteristic of ASADH's thiohemiacetal-forming mechanism) and 'GHTVCASLRF' containing the catalytic Cys in the conserved 'VCAS' context. General aldehyde dehydrogenases (1.2.1.x family, e.g., ALDH2) instead feature a 'CAG' catalytic motif. The ~362-aa length, dimeric architecture, and NADP+-selective Rossmann fold are all consistent with fungal ASADH orthologs well characterized in the literature. These family-level sequence features are transferable knowledge from ASADH homologs across bacteria and fungi and meaningfully distinguish D from A.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold eliminates the two transferase options. The specific Cys-containing motifs (CNSNC, VCAS) are well-documented family signatures of ASADH, distinct from the CAG motif of general aldehyde dehydrogenases. A knowledgeable model recognizing these motifs from ASADH homologs (e.g., E. coli, yeast, fungal orthologs) can credibly select D over A without needing a target-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are clearly eliminated by the oxidoreductase Rossmann fold. Between A and D, the ASADH-specific Cys motifs (CNSNC, VCAS) and the NADP+-selective Rossmann fold pattern provide a clear family-level distinction favoring D. No other option is genuinely defensible given these features."
  },
  "important_caveats": [
    "Distinguishing 1.2.1.11 from 1.2.1.46 relies on recognizing ASADH-specific catalytic Cys motifs versus general ALDH motifs; a model unfamiliar with the exact motif contexts might find A and D harder to separate, though the CNSNC/VCAS patterns are well-documented ASADH signatures.",
    "The UniProt annotation is supported by experimental evidence (PubMed, PDB), not merely computational inference.",
    "The sequence is from Blastomyces gilchristii, a fungal pathogen; fungal ASADH is a validated drug target, and its motifs are well characterized in the literature."
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
  "benchmark_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 362,
  "current_source_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A179UL48",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "selected_historical_source_sequence_length": 362,
  "selected_historical_source_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "selected_historical_version": {
    "accession": "A0A179UL48",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_BLAGS",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A179UL48\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Blastomyces dermatitidis\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002038\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Onygenales\",\"Ajellomycetaceae\",\"Blastomyces\"],\"scientificName\":\"Blastomyces gilchristii (strain SLH14081)\",\"taxonId\":559298}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24286\"}}],\"reaction\":{\"ecNumber\":\"1.2.1.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"name\":\"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24284\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:537519\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30107909\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbrc.2018.08.053\"}],\"citationType\":\"journal article\",\"firstPage\":\"2848\",\"id\":\"30107909\",\"journal\":\"Biochem. Biophys. Res. Commun.\",\"lastPage\":\"2854\",\"publicationDate\":\"2018\",\"title\":\"Structural insights into inhibitor binding to a fungal ortholog of aspartate semialdehyde dehydrogenase.\",\"volume\":\"503\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C85\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND NADP(+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_BLAGS              Reviewed;         362 AA.\nAC   A0A179UL48;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};\nGN   ORFNames=BDBG_16922 {ECO:0000312|EMBL:OAT07949.1};\nOS   Blastomyces gilchristii (strain SLH14081) (Blastomyces dermatitidis).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Onygenales; Ajellomycetaceae; Blastomyces.\nOX   NCBI_TaxID=559298 {ECO:0000312|Proteomes:UP000002038};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "RN   [3] {ECO:0007744|PDB:6C85, ECO:0007744|PDB:6C8W}\nRP   X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND\nRP   NADP(+), FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=30107909; DOI=10.1016/j.bbrc.2018.08.053;\nRA   Dahal G.P., Viola R.E.;\nRT   \"Structural insights into inhibitor binding to a fungal ortholog of\nRT   aspartate semialdehyde dehydrogenase.\";\nRL   Biochem. Biophys. Res. Commun. 503:2848-2854(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-\nCC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;\nCC         Evidence={ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;\nCC         Evidence={ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 57. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
