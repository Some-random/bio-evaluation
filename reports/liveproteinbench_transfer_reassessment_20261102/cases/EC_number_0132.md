# EC_number_0132

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0132.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 4.2.1.9

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. 4.2.1.18
B. 2.7.1.52
C. 4.2.1.9
D. 2.3.1.322
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

> The exact sequence matches the UniProt entry, which assigns EC 4.2.1.9 and records the corresponding catalytic reaction with experimental evidence (ECO:0000269).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The roughly 600-residue sequence, including an N-terminal region consistent with a mitochondrial targeting peptide and conserved cysteine-containing features, is credibly recognizable as a dihydroxy-acid dehydratase/IlvD-family enzyme. Family-level knowledge links this enzyme type to EC 4.2.1.9. That inference distinguishes it from the two transferase choices and gives a meaningful basis to prefer this option over the other lyase choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence offers family-level evidence for the enzyme class and reaction; identifying the precise EC choice need not rely on recalling an annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-family inference supports C, and the supplied source evidence confirms that EC assignment.


### Important caveats

- The database’s experimental evidence attribution supports the key, but the underlying primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The roughly 600-residue sequence, including an N-terminal region consistent with a mitochondrial targeting peptide and conserved cysteine-containing features, is credibly recognizable as a dihydroxy-acid dehydratase/IlvD-family enzyme. Family-level knowledge links this enzyme type to EC 4.2.1.9. That inference distinguishes it from the two transferase choices and gives a meaningful basis to prefer this option over the other lyase choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers family-level evidence for the enzyme class and reaction; identifying the precise EC choice need not rely on recalling an annotation for this exact protein."
  },
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which assigns EC 4.2.1.9 and records the corresponding catalytic reaction with experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The database’s experimental evidence attribution supports the key, but the underlying primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference supports C, and the supplied source evidence confirms that EC assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which assigns EC 4.2.1.9 and records the corresponding catalytic reaction with experimental evidence (ECO:0000269).",
    "evidence_ids": ["C1", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The roughly 600-residue sequence, including an N-terminal region consistent with a mitochondrial targeting peptide and conserved cysteine-containing features, is credibly recognizable as a dihydroxy-acid dehydratase/IlvD-family enzyme. Family-level knowledge links this enzyme type to EC 4.2.1.9. That inference distinguishes it from the two transferase choices and gives a meaningful basis to prefer this option over the other lyase choice.",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers family-level evidence for the enzyme class and reaction; identifying the precise EC choice need not rely on recalling an annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference supports C, and the supplied source evidence confirms that EC assignment."
  },
  "important_caveats": [
    "The database’s experimental evidence attribution supports the key, but the underlying primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q0CPG9 (ASTD_ASPTN) is annotated with EC 4.2.1.9 (dihydroxy-acid dehydratase) supported by experimental evidence (ECO:0000269, PubMed:29995859). The catalytic activity reactions (dehydration of 2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate + H2O) confirm EC 4.2.1.9. The sequence in the question matches the source entry exactly (SHA-256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple highly conserved motifs diagnostic of the dihydroxy-acid dehydratase (DHAD/ILVD) family: (1) the 'GAGLGQ' motif in the N-terminal domain (visible in 'IMGAGLGQDVALL'), which is a hallmark of the DHAD family found across bacteria (E. coli IlvD), yeast (ILV3), and fungi; (2) the 'TDGRFSGG' and 'GSHGFLIGH' motifs in the C-terminal domain, which are conserved across DHAD homologs and participate in substrate binding and catalysis; (3) the overall two-domain architecture (N-terminal dehydratase domain + C-terminal domain) typical of DHAD enzymes; (4) a positively charged N-terminal mitochondrial targeting sequence (multiple Arg/Lys residues) consistent with fungal mitochondrial DHAD. These features clearly distinguish the protein from aconitase (4.2.1.18, which would require &#91;4Fe-4S&#93; cluster-binding Cys motifs like C-x-x-C-x-x-x-x-C), pyruvate kinase (2.7.1.52, a completely different fold with PEP-binding and nucleotide-binding motifs), and an acyltransferase (2.3.1.322, which would have a different catalytic architecture). The DHAD family motifs are well-characterized transferable knowledge from homologs across multiple organisms.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the DHAD/ILVD family from conserved sequence motifs (GAGLGQ, TDGRFSGG, GSHGFLIGH) that are shared with characterized DHAD enzymes in E. coli, yeast, and other fungi. These motifs are well-documented family signatures and are sufficient to distinguish EC 4.2.1.9 from the other three options, which belong to entirely different enzyme families and folds.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC classes (4.2.x.x hydro-lyases, 2.7.x.x transferases, 2.3.x.x acyltransferases) and the sequence features unambiguously point to the DHAD family. Aconitase would require iron-sulfur cluster motifs, pyruvate kinase would show nucleotide/PEP-binding features, and an acyltransferase would have a completely different architecture. No ambiguity exists.


### Important caveats

- The UniProt annotation for EC 4.2.1.9 is supported by experimental evidence (ECO:0000269) from PubMed 29995859, not merely computational prediction.
- The protein is a fungal mitochondrial DHAD (astD) involved in aspterric acid biosynthesis, which is a specialized secondary metabolite pathway rather than the canonical branched-chain amino acid pathway, but the enzyme family and EC assignment are the same.
- The DHAD family motifs are well-established across many characterized homologs, making this a legitimate family-recognition task rather than a memorization task.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple highly conserved motifs diagnostic of the dihydroxy-acid dehydratase (DHAD/ILVD) family: (1) the 'GAGLGQ' motif in the N-terminal domain (visible in 'IMGAGLGQDVALL'), which is a hallmark of the DHAD family found across bacteria (E. coli IlvD), yeast (ILV3), and fungi; (2) the 'TDGRFSGG' and 'GSHGFLIGH' motifs in the C-terminal domain, which are conserved across DHAD homologs and participate in substrate binding and catalysis; (3) the overall two-domain architecture (N-terminal dehydratase domain + C-terminal domain) typical of DHAD enzymes; (4) a positively charged N-terminal mitochondrial targeting sequence (multiple Arg/Lys residues) consistent with fungal mitochondrial DHAD. These features clearly distinguish the protein from aconitase (4.2.1.18, which would require [4Fe-4S] cluster-binding Cys motifs like C-x-x-C-x-x-x-x-C), pyruvate kinase (2.7.1.52, a completely different fold with PEP-binding and nucleotide-binding motifs), and an acyltransferase (2.3.1.322, which would have a different catalytic architecture). The DHAD family motifs are well-characterized transferable knowledge from homologs across multiple organisms.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the DHAD/ILVD family from conserved sequence motifs (GAGLGQ, TDGRFSGG, GSHGFLIGH) that are shared with characterized DHAD enzymes in E. coli, yeast, and other fungi. These motifs are well-documented family signatures and are sufficient to distinguish EC 4.2.1.9 from the other three options, which belong to entirely different enzyme families and folds."
  },
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG9 (ASTD_ASPTN) is annotated with EC 4.2.1.9 (dihydroxy-acid dehydratase) supported by experimental evidence (ECO:0000269, PubMed:29995859). The catalytic activity reactions (dehydration of 2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate + H2O) confirm EC 4.2.1.9. The sequence in the question matches the source entry exactly (SHA-256 match confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.2.1.9 is supported by experimental evidence (ECO:0000269) from PubMed 29995859, not merely computational prediction.",
    "The protein is a fungal mitochondrial DHAD (astD) involved in aspterric acid biosynthesis, which is a specialized secondary metabolite pathway rather than the canonical branched-chain amino acid pathway, but the enzyme family and EC assignment are the same.",
    "The DHAD family motifs are well-established across many characterized homologs, making this a legitimate family-recognition task rather than a memorization task."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (4.2.x.x hydro-lyases, 2.7.x.x transferases, 2.3.x.x acyltransferases) and the sequence features unambiguously point to the DHAD family. Aconitase would require iron-sulfur cluster motifs, pyruvate kinase would show nucleotide/PEP-binding features, and an acyltransferase would have a completely different architecture. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG9 (ASTD_ASPTN) is annotated with EC 4.2.1.9 (dihydroxy-acid dehydratase) supported by experimental evidence (ECO:0000269, PubMed:29995859). The catalytic activity reactions (dehydration of 2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate + H2O) confirm EC 4.2.1.9. The sequence in the question matches the source entry exactly (SHA-256 match confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple highly conserved motifs diagnostic of the dihydroxy-acid dehydratase (DHAD/ILVD) family: (1) the 'GAGLGQ' motif in the N-terminal domain (visible in 'IMGAGLGQDVALL'), which is a hallmark of the DHAD family found across bacteria (E. coli IlvD), yeast (ILV3), and fungi; (2) the 'TDGRFSGG' and 'GSHGFLIGH' motifs in the C-terminal domain, which are conserved across DHAD homologs and participate in substrate binding and catalysis; (3) the overall two-domain architecture (N-terminal dehydratase domain + C-terminal domain) typical of DHAD enzymes; (4) a positively charged N-terminal mitochondrial targeting sequence (multiple Arg/Lys residues) consistent with fungal mitochondrial DHAD. These features clearly distinguish the protein from aconitase (4.2.1.18, which would require [4Fe-4S] cluster-binding Cys motifs like C-x-x-C-x-x-x-x-C), pyruvate kinase (2.7.1.52, a completely different fold with PEP-binding and nucleotide-binding motifs), and an acyltransferase (2.3.1.322, which would have a different catalytic architecture). The DHAD family motifs are well-characterized transferable knowledge from homologs across multiple organisms.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the DHAD/ILVD family from conserved sequence motifs (GAGLGQ, TDGRFSGG, GSHGFLIGH) that are shared with characterized DHAD enzymes in E. coli, yeast, and other fungi. These motifs are well-documented family signatures and are sufficient to distinguish EC 4.2.1.9 from the other three options, which belong to entirely different enzyme families and folds."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (4.2.x.x hydro-lyases, 2.7.x.x transferases, 2.3.x.x acyltransferases) and the sequence features unambiguously point to the DHAD family. Aconitase would require iron-sulfur cluster motifs, pyruvate kinase would show nucleotide/PEP-binding features, and an acyltransferase would have a completely different architecture. No ambiguity exists."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.2.1.9 is supported by experimental evidence (ECO:0000269) from PubMed 29995859, not merely computational prediction.",
    "The protein is a fungal mitochondrial DHAD (astD) involved in aspterric acid biosynthesis, which is a specialized secondary metabolite pathway rather than the canonical branched-chain amino acid pathway, but the enzyme family and EC assignment are the same.",
    "The DHAD family motifs are well-established across many characterized homologs, making this a legitimate family-recognition task rather than a memorization task."
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
  "benchmark_sequence_length": 598,
  "benchmark_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 598,
  "current_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0CPG9",
  "selected_historical_entry_version": 90,
  "selected_historical_record_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "selected_historical_source_sequence_length": 598,
  "selected_historical_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "selected_historical_version": {
    "accession": "Q0CPG9",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTD_ASPTN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0CPG9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase astD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24810\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"name\":\"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24809\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:11851\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49072\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:27695\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"name\":\"(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:27694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49258\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DOMAIN\",\"ACTIVITY REGULATION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H1",
  "excerpt": "ID   ASTD_ASPTN              Reviewed;         598 AA.\nAC   Q0CPG9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\nGN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, DOMAIN,\nRP   ACTIVITY REGULATION, AND PATHWAY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate\nCC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:49072; EC=4.2.1.9;\nCC         Evidence={ECO:0000269|PubMed:29995859};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;\nCC         Evidence={ECO:0000269|PubMed:29995859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-\nCC         oxopentanoate + H2O; Xref=Rhea:RHEA:27694, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:35146, ChEBI:CHEBI:49258; EC=4.2.1.9;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:27695;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 132. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
