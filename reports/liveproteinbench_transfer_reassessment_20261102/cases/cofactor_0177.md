# cofactor_0177

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0177.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTRGERVIAFIERFCIVPEGKLIGQPMRLDPFQKDFILAVYDNPAGTDMAILSIARKNGKTGLIAGILLAHLVGPEAVQNTQIVSGALSREQAAIVFNLAVKMVNLNPKLQEIVHITPSGKKLIGLPCNVEYKALSAEGKTTHGLSPILAILDETGQVRGPQDDFIDAITTAQGAHENPLLIVISTQAANDADLLSIWIDDAVKSKDPHIVCHVYEAPKDADISKRESWLAANPALGTFRSEKDMARQAEKAGRMPSFENTFRNLNLNQRVSTVSPFISRSVWELCGEMPINTPRKWYAGLDLSARNDLTALVIAGEADDGVWDVFPFFWTPQKTLEERTKTDRAPYDVWVREGLLRTTPGASVDYSFVVADIAEIIGDFDLTSMAFDRWRIDQFRKDADAIGLSLPLVEFGQGFKDMGPAVDTLESLMLNGRVRHGMHPVLTMCAVNAVVVKDAAGNRKLDKSKATGRIDGMVAMTMSVGAANGEVTEQGGDFDDFIFRPLSM

[Multiple Choices]
A. Fe(2+)
B. Mg(2+)
C. Cu(2+)
D. Co(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The matched protein record annotates Mg(2+) as a cofactor with experimental evidence. It also annotates Mn(2+), but Mn(2+) is not among the choices, so the key's Mg(2+) answer is supported.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an ATPase-like nucleotide-binding signature, including a GKT motif. ATP-dependent enzymes commonly use Mg(2+) to coordinate ATP phosphates during catalysis, making Mg(2+) a meaningful choice over Fe(2+), Cu(2+), or Co(2+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> This is a defensible family- and mechanism-level inference from the sequence and choices, though it does not establish the exact metal preference of this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source also annotates Mn(2+), but that is not offered; among the listed options, only Mg(2+) is supported.


### Important caveats

- The source annotates both Mg(2+) and Mn(2+), so the protein's metal use may not be exclusive to Mg(2+).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an ATPase-like nucleotide-binding signature, including a GKT motif. ATP-dependent enzymes commonly use Mg(2+) to coordinate ATP phosphates during catalysis, making Mg(2+) a meaningful choice over Fe(2+), Cu(2+), or Co(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "This is a defensible family- and mechanism-level inference from the sequence and choices, though it does not establish the exact metal preference of this particular protein."
  },
  "case_id": "cofactor_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched protein record annotates Mg(2+) as a cofactor with experimental evidence. It also annotates Mn(2+), but Mn(2+) is not among the choices, so the key's Mg(2+) answer is supported."
  },
  "important_caveats": [
    "The source annotates both Mg(2+) and Mn(2+), so the protein's metal use may not be exclusive to Mg(2+)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source also annotates Mn(2+), but that is not offered; among the listed options, only Mg(2+) is supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein record annotates Mg(2+) as a cofactor with experimental evidence. It also annotates Mn(2+), but Mn(2+) is not among the choices, so the key's Mg(2+) answer is supported.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an ATPase-like nucleotide-binding signature, including a GKT motif. ATP-dependent enzymes commonly use Mg(2+) to coordinate ATP phosphates during catalysis, making Mg(2+) a meaningful choice over Fe(2+), Cu(2+), or Co(2+).",
    "missing_item_specific_fact": "",
    "reason": "This is a defensible family- and mechanism-level inference from the sequence and choices, though it does not establish the exact metal preference of this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source also annotates Mn(2+), but that is not offered; among the listed options, only Mg(2+) is supported."
  },
  "important_caveats": [
    "The source annotates both Mg(2+) and Mn(2+), so the protein's metal use may not be exclusive to Mg(2+)."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9MCT1 (Terminase large subunit / DNA-packaging protein gp2 from Bacteriophage HK97) lists Mg(2+) as a cofactor with experimental evidence (ECO:0000269, PubMed 35947691, X-ray crystallography PDB 6Z6D). Mn(2+) is also listed as a cofactor, but it is not among the offered choices. The key B (Mg(2+)) is directly supported by the source annotation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains a canonical Walker A (P-loop) motif: 'ARKNGKTGLIAG' (GxxxxGK&#91;T/S&#93; pattern with GKT), and a Walker B motif: 'LAILDE' (hhhhDE pattern). These two motifs together are the defining signature of P-loop NTPases/ATPases. Virtually all characterized ATPases (kinases, helicases, AAA+ proteins, GTPases, motor proteins, and viral terminases) require Mg(2+) as the essential metal cofactor to coordinate the ATP phosphates during hydrolysis. This is one of the most universally established facts in biochemistry, supported by thousands of structurally and biochemically characterized ATPases. Among the four options (Fe2+, Mg2+, Cu2+, Co2+), only Mg2+ is the physiological cofactor of ATPases. Fe2+ is associated with oxygen transport/electron transfer, Cu2+ with oxidases, and Co2+ with B12-dependent enzymes and certain isomerases. The Walker A/B motif identification alone provides a concrete, high-confidence transferable inference that meaningfully and uniquely selects Mg(2+) from the offered alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the Walker A (GKT) and Walker B (DE) motifs in the sequence identifies the protein as an ATPase. The universal requirement of Mg(2+) for ATPase activity is textbook-level transferable knowledge derived from thousands of other proteins. This inference directly and uniquely selects option B over Fe(2+), Cu(2+), and Co(2+), none of which serve as ATPase cofactors.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Walker A/B motifs unambiguously identify an ATPase, for which Mg(2+) is the standard and essentially exclusive physiological cofactor. None of the other three options (Fe2+, Cu2+, Co2+) are plausible ATPase cofactors. Although Mn(2+) can substitute for Mg(2+) in some ATPases in vitro, it is not among the offered choices, so no ambiguity exists among the presented alternatives.


### Important caveats

- The UniProt annotation also lists Mn(2+) as a cofactor (ECO:0000269), but Mn(2+) is not among the four offered choices, so this does not affect the answerability among the given options.
- The protein is a viral terminase large subunit (ring-type ATPase), and the 2022 crystallographic study (PDB 6Z6D) provided the experimental cofactor assignment. The Walker A/B motif inference from the sequence alone is sufficient to predict Mg(2+) without needing to know the specific protein identity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains a canonical Walker A (P-loop) motif: 'ARKNGKTGLIAG' (GxxxxGK[T/S] pattern with GKT), and a Walker B motif: 'LAILDE' (hhhhDE pattern). These two motifs together are the defining signature of P-loop NTPases/ATPases. Virtually all characterized ATPases (kinases, helicases, AAA+ proteins, GTPases, motor proteins, and viral terminases) require Mg(2+) as the essential metal cofactor to coordinate the ATP phosphates during hydrolysis. This is one of the most universally established facts in biochemistry, supported by thousands of structurally and biochemically characterized ATPases. Among the four options (Fe2+, Mg2+, Cu2+, Co2+), only Mg2+ is the physiological cofactor of ATPases. Fe2+ is associated with oxygen transport/electron transfer, Cu2+ with oxidases, and Co2+ with B12-dependent enzymes and certain isomerases. The Walker A/B motif identification alone provides a concrete, high-confidence transferable inference that meaningfully and uniquely selects Mg(2+) from the offered alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the Walker A (GKT) and Walker B (DE) motifs in the sequence identifies the protein as an ATPase. The universal requirement of Mg(2+) for ATPase activity is textbook-level transferable knowledge derived from thousands of other proteins. This inference directly and uniquely selects option B over Fe(2+), Cu(2+), and Co(2+), none of which serve as ATPase cofactors."
  },
  "case_id": "cofactor_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9MCT1 (Terminase large subunit / DNA-packaging protein gp2 from Bacteriophage HK97) lists Mg(2+) as a cofactor with experimental evidence (ECO:0000269, PubMed 35947691, X-ray crystallography PDB 6Z6D). Mn(2+) is also listed as a cofactor, but it is not among the offered choices. The key B (Mg(2+)) is directly supported by the source annotation."
  },
  "important_caveats": [
    "The UniProt annotation also lists Mn(2+) as a cofactor (ECO:0000269), but Mn(2+) is not among the four offered choices, so this does not affect the answerability among the given options.",
    "The protein is a viral terminase large subunit (ring-type ATPase), and the 2022 crystallographic study (PDB 6Z6D) provided the experimental cofactor assignment. The Walker A/B motif inference from the sequence alone is sufficient to predict Mg(2+) without needing to know the specific protein identity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Walker A/B motifs unambiguously identify an ATPase, for which Mg(2+) is the standard and essentially exclusive physiological cofactor. None of the other three options (Fe2+, Cu2+, Co2+) are plausible ATPase cofactors. Although Mn(2+) can substitute for Mg(2+) in some ATPases in vitro, it is not among the offered choices, so no ambiguity exists among the presented alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9MCT1 (Terminase large subunit / DNA-packaging protein gp2 from Bacteriophage HK97) lists Mg(2+) as a cofactor with experimental evidence (ECO:0000269, PubMed 35947691, X-ray crystallography PDB 6Z6D). Mn(2+) is also listed as a cofactor, but it is not among the offered choices. The key B (Mg(2+)) is directly supported by the source annotation.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains a canonical Walker A (P-loop) motif: 'ARKNGKTGLIAG' (GxxxxGK[T/S] pattern with GKT), and a Walker B motif: 'LAILDE' (hhhhDE pattern). These two motifs together are the defining signature of P-loop NTPases/ATPases. Virtually all characterized ATPases (kinases, helicases, AAA+ proteins, GTPases, motor proteins, and viral terminases) require Mg(2+) as the essential metal cofactor to coordinate the ATP phosphates during hydrolysis. This is one of the most universally established facts in biochemistry, supported by thousands of structurally and biochemically characterized ATPases. Among the four options (Fe2+, Mg2+, Cu2+, Co2+), only Mg2+ is the physiological cofactor of ATPases. Fe2+ is associated with oxygen transport/electron transfer, Cu2+ with oxidases, and Co2+ with B12-dependent enzymes and certain isomerases. The Walker A/B motif identification alone provides a concrete, high-confidence transferable inference that meaningfully and uniquely selects Mg(2+) from the offered alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the Walker A (GKT) and Walker B (DE) motifs in the sequence identifies the protein as an ATPase. The universal requirement of Mg(2+) for ATPase activity is textbook-level transferable knowledge derived from thousands of other proteins. This inference directly and uniquely selects option B over Fe(2+), Cu(2+), and Co(2+), none of which serve as ATPase cofactors."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Walker A/B motifs unambiguously identify an ATPase, for which Mg(2+) is the standard and essentially exclusive physiological cofactor. None of the other three options (Fe2+, Cu2+, Co2+) are plausible ATPase cofactors. Although Mn(2+) can substitute for Mg(2+) in some ATPases in vitro, it is not among the offered choices, so no ambiguity exists among the presented alternatives."
  },
  "important_caveats": [
    "The UniProt annotation also lists Mn(2+) as a cofactor (ECO:0000269), but Mn(2+) is not among the four offered choices, so this does not affect the answerability among the given options.",
    "The protein is a viral terminase large subunit (ring-type ATPase), and the 2022 crystallographic study (PDB 6Z6D) provided the experimental cofactor assignment. The Walker A/B motif inference from the sequence alone is sufficient to predict Mg(2+) without needing to know the specific protein identity."
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
  "benchmark_sequence_length": 504,
  "benchmark_sequence_sha256": "8e87f171388c4d4f15153e69a6ed38cd38a9c1176b5148b491a88ff220fad067",
  "current_entry_audit": {
    "entryVersion": 68,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ee2441b906644046077d0bfe44187e39d7ed385540778e1e043fa90c3ce6f334",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 504,
  "current_source_sequence_sha256": "8e87f171388c4d4f15153e69a6ed38cd38a9c1176b5148b491a88ff220fad067",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 66,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9MCT1",
  "selected_historical_entry_version": 66,
  "selected_historical_record_sha256": "08dc5e490c969d0598d4ac801aabac1272030affcdcfa44887f89ef63e53343c",
  "selected_historical_source_sequence_length": 504,
  "selected_historical_source_sequence_sha256": "8e87f171388c4d4f15153e69a6ed38cd38a9c1176b5148b491a88ff220fad067",
  "selected_historical_version": {
    "accession": "Q9MCT1",
    "database": "Swiss-Prot",
    "entryVersion": 66,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TERL_BPHK7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9MCT1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9MCT1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:09.391226+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee2441b906644046077d0bfe44187e39d7ed385540778e1e043fa90c3ce6f334",
  "url": "https://rest.uniprot.org/uniprotkb/Q9MCT1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9MCT1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":68,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:09.391226+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee2441b906644046077d0bfe44187e39d7ed385540778e1e043fa90c3ce6f334",
  "url": "https://rest.uniprot.org/uniprotkb/Q9MCT1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9MCT1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacteriophage HK97\",\"lineage\":[\"Viruses\",\"Duplodnaviria\",\"Heunggongvirae\",\"Uroviricota\",\"Caudoviricetes\",\"Caudoviricetes incertae sedis\",\"Hendrixvirinae\",\"Byrnievirus\",\"Byrnievirus HK97\"],\"scientificName\":\"Enterobacteria phage HK97\",\"taxonId\":2681617}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:09.391226+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee2441b906644046077d0bfe44187e39d7ed385540778e1e043fa90c3ce6f334",
  "url": "https://rest.uniprot.org/uniprotkb/Q9MCT1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9MCT1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"DNA-packaging protein gp2\"}}],\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"value\":\"3.1.21.-\"}],\"fullName\":{\"value\":\"Endonuclease\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"value\":\"3.6.4.-\"}],\"fullName\":{\"value\":\"ATPase\"}}}],\"recommendedName\":{\"fullName\":{\"value\":\"Terminase, large subunit\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:09.391226+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee2441b906644046077d0bfe44187e39d7ed385540778e1e043fa90c3ce6f334",
  "url": "https://rest.uniprot.org/uniprotkb/Q9MCT1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9MCT1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947691\",\"source\":\"PubMed\"}],\"name\":\"Mg(2+)\"},{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947691\",\"source\":\"PubMed\"}],\"name\":\"Mn(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:09.391226+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee2441b906644046077d0bfe44187e39d7ed385540778e1e043fa90c3ce6f334",
  "url": "https://rest.uniprot.org/uniprotkb/Q9MCT1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9MCT1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Fung H.K.H.\",\"Grimes S.\",\"Huet A.\",\"Duda R.L.\",\"Chechik M.\",\"Gault J.\",\"Robinson C.V.\",\"Hendrix R.W.\",\"Jardine P.J.\",\"Conway J.F.\",\"Baumann C.G.\",\"Antson A.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35947691\"},{\"database\":\"DOI\",\"id\":\"10.1093/nar/gkac647\"}],\"citationType\":\"journal article\",\"firstPage\":\"8719\",\"id\":\"35947691\",\"journal\":\"Nucleic Acids Res.\",\"lastPage\":\"8732\",\"publicationDate\":\"2022\",\"title\":\"Structural basis of DNA packaging by a ring-type ATPase from an archetypal viral system.\",\"volume\":\"50\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6Z6D\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS)\",\"COFACTOR\",\"SUBUNIT\",\"MUTAGENESIS OF ARG-56; LYS-57; LYS-60 AND ARG-154\",\"FUNCTION\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:09.391226+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee2441b906644046077d0bfe44187e39d7ed385540778e1e043fa90c3ce6f334",
  "url": "https://rest.uniprot.org/uniprotkb/Q9MCT1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9MCT1?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H1",
  "excerpt": "ID   TERL_BPHK7              Reviewed;         504 AA.\nAC   Q9MCT1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 66.\nDE   RecName: Full=Terminase, large subunit;\nDE   AltName: Full=DNA-packaging protein gp2;\nDE   Includes:\nDE     RecName: Full=Endonuclease;\nDE              EC=3.1.21.-;\nDE   Includes:\nDE     RecName: Full=ATPase;\nDE              EC=3.6.4.-;\nGN   Name=2;\nOS   Enterobacteria phage HK97 (Bacteriophage HK97).\nOC   Viruses; Duplodnaviria; Heunggongvirae; Uroviricota; Caudoviricetes;\nOC   Hendrixvirinae; Byrnievirus; Byrnievirus HK97.\nOX   NCBI_TaxID=2681617;\nOH   NCBI_TaxID=562; Escherichia coli.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:11.849933+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "08dc5e490c969d0598d4ac801aabac1272030affcdcfa44887f89ef63e53343c",
  "url": "https://rest.uniprot.org/unisave/Q9MCT1?format=txt&versions=66"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9MCT1?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Terminase, large subunit;\nDE   AltName: Full=DNA-packaging protein gp2;\nDE   Includes:\nDE     RecName: Full=Endonuclease;\nDE              EC=3.1.21.-;\nDE   Includes:\nDE     RecName: Full=ATPase;\nDE              EC=3.6.4.-;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:11.849933+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "08dc5e490c969d0598d4ac801aabac1272030affcdcfa44887f89ef63e53343c",
  "url": "https://rest.uniprot.org/unisave/Q9MCT1?format=txt&versions=66"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9MCT1?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6Z6D}\nRP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS), COFACTOR, SUBUNIT, MUTAGENESIS OF\nRP   ARG-56; LYS-57; LYS-60 AND ARG-154, FUNCTION, AND ACTIVITY REGULATION.\nRX   PubMed=35947691; DOI=10.1093/nar/gkac647;\nRA   Fung H.K.H., Grimes S., Huet A., Duda R.L., Chechik M., Gault J.,\nRA   Robinson C.V., Hendrix R.W., Jardine P.J., Conway J.F., Baumann C.G.,\nRA   Antson A.A.;\nRT   \"Structural basis of DNA packaging by a ring-type ATPase from an archetypal\nRT   viral system.\";\nRL   Nucleic Acids Res. 50:8719-8732(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:11.849933+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "08dc5e490c969d0598d4ac801aabac1272030affcdcfa44887f89ef63e53343c",
  "url": "https://rest.uniprot.org/unisave/Q9MCT1?format=txt&versions=66"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9MCT1?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000269|PubMed:35947691};\nCC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;\nCC         Evidence={ECO:0000269|PubMed:35947691};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:11.849933+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "08dc5e490c969d0598d4ac801aabac1272030affcdcfa44887f89ef63e53343c",
  "url": "https://rest.uniprot.org/unisave/Q9MCT1?format=txt&versions=66"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 177. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
