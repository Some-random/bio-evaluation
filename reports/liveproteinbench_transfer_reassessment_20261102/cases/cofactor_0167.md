# cofactor_0167

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0167.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Mn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATPKSFRDNLAEILKTHDFRTVELEFRLGFQAPGEFITNINKHVWTTAKEKLGTPAQELVMVDKYIRSTPGESSRYVVFPDGQGYWEHKKKVAKETTTGGKYGVRSAFSLERRENGKPPVSFRMQRTKYRTTFVKGPWKIDFTRVESIPATDRDCESTYEIEVELYDMFYLFEKELDIIIQEGNKLVQSIVM

[Multiple Choices]
A. Fe cation
B. cob(II)alamin
C. Mo-bis(molybdopterin guanine dinucleotide)
D. Mn(2+)
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

> The sequence matches the cited UniProt record, which annotates Mn(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:11160672). The annotation applies to this sequence, though the primary study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A family-level recognition of this compact protein as a viral RNA triphosphatase supports a metal-dependent phosphohydrolase interpretation. Transferable knowledge of this enzyme class makes Mn(2+) a credible preference over cob(II)alamin or the specialized molybdenum cofactor; the sequence’s acidic residues are also compatible with metal-dependent catalysis. This is a probabilistic family inference, not an unambiguous sequence-only identification of the bound ion.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Related-enzyme knowledge provides a meaningful basis for selecting Mn(2+) among these alternatives without consulting this exact protein’s annotation. The sequence alone does not prove metal specificity, and distinguishing Mn(2+) from other metal ions is less certain than excluding the non-metal cofactors.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available evidence supports Mn(2+); no other offered choice is comparably defensible.


### Important caveats

- The source record's cofactor annotation is experimental-evidence-tagged, but that evidence was reviewer-only and was not part of the original model input.
- Family-based inference supports the answer but does not establish the exact ion with certainty from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A family-level recognition of this compact protein as a viral RNA triphosphatase supports a metal-dependent phosphohydrolase interpretation. Transferable knowledge of this enzyme class makes Mn(2+) a credible preference over cob(II)alamin or the specialized molybdenum cofactor; the sequence’s acidic residues are also compatible with metal-dependent catalysis. This is a probabilistic family inference, not an unambiguous sequence-only identification of the bound ion.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Related-enzyme knowledge provides a meaningful basis for selecting Mn(2+) among these alternatives without consulting this exact protein’s annotation. The sequence alone does not prove metal specificity, and distinguishing Mn(2+) from other metal ions is less certain than excluding the non-metal cofactors."
  },
  "case_id": "cofactor_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, which annotates Mn(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:11160672). The annotation applies to this sequence, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The source record's cofactor annotation is experimental-evidence-tagged, but that evidence was reviewer-only and was not part of the original model input.",
    "Family-based inference supports the answer but does not establish the exact ion with certainty from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available evidence supports Mn(2+); no other offered choice is comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, which annotates Mn(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:11160672). The annotation applies to this sequence, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A family-level recognition of this compact protein as a viral RNA triphosphatase supports a metal-dependent phosphohydrolase interpretation. Transferable knowledge of this enzyme class makes Mn(2+) a credible preference over cob(II)alamin or the specialized molybdenum cofactor; the sequence’s acidic residues are also compatible with metal-dependent catalysis. This is a probabilistic family inference, not an unambiguous sequence-only identification of the bound ion.",
    "missing_item_specific_fact": "",
    "reason": "Related-enzyme knowledge provides a meaningful basis for selecting Mn(2+) among these alternatives without consulting this exact protein’s annotation. The sequence alone does not prove metal specificity, and distinguishing Mn(2+) from other metal ions is less certain than excluding the non-metal cofactors."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available evidence supports Mn(2+); no other offered choice is comparably defensible."
  },
  "important_caveats": [
    "The source record's cofactor annotation is experimental-evidence-tagged, but that evidence was reviewer-only and was not part of the original model input.",
    "Family-based inference supports the answer but does not establish the exact ion with certainty from the sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q98500 (TPASE_PBCV1, 5'RNA triphosphatase A449R from PBCV-1) explicitly annotates Mn(2+) as the cofactor with experimental evidence (ECO:0000269|PubMed:11160672, Ho/Gong/Shuman 2001). The sequence matches exactly (193 AA, SHA256 confirmed). The expected answer D is directly supported by a direct-assay experimental reference.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options represent fundamentally different cofactor classes: Fe cation (redox/oxidoreductase), cob(II)alamin (radical/methyltransferase chemistry), Mo-bis(molybdopterin guanine dinucleotide) (molybdoenzyme oxidoreductases like nitrate reductase, xanthine oxidase), and Mn(2+) (divalent metal ion for hydrolytic enzymes such as phosphatases and nucleases). The sequence (193 AA) lacks any motifs diagnostic of redox enzymes: no Rossmann-fold NAD/FAD-binding, no molybdopterin-binding cysteine/serine clusters, no cob(II)alamin-binding domain architecture. Instead, the sequence contains clusters of acidic residues (multiple E and D residues, e.g., 'DCESTYEIEVELYDMFYLFEKELDIIIQEG') consistent with divalent-metal coordination sites typical of metallophosphatases. A model with general knowledge that phosphatases/nucleases require divalent metal ions (Mg2+, Mn2+) while Fe, B12, and Mo-bis(MGD) serve redox chemistry can eliminate A, B, and C and select D. This is a standard cofactor-to-enzyme-class inference learned from many other proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of three redox-associated cofactors and selection of a divalent metal ion is a well-established pattern in enzymology. The absence of redox motifs in the sequence combined with the presence of acidic-residue clusters provides a credible transferable argument distinguishing D from A, B, and C without needing the specific UniProt annotation for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct cofactor classes (transition-metal redox, organometallic B12, molybdoenzyme, divalent metal hydrolysis). Only Mn(2+) is consistent with a hydrolytic enzyme lacking redox motifs. No ambiguity among the offered choices.


### Important caveats

- The specific assignment of Mn(2+) over Mg(2+) for this particular triphosphatase was established experimentally (Ho et al. 2001); general phosphatase knowledge would suggest 'a divalent metal ion' but the question conveniently omits Mg(2+) from the choices, making Mn(2+) the only divalent-metal option.
- The sequence alone does not unambiguously identify the protein as a triphosphatase; the reasoning relies on cofactor-class elimination rather than positive motif identification.
- The reviewer evidence confirms experimental (not merely computational) support for the Mn(2+) assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options represent fundamentally different cofactor classes: Fe cation (redox/oxidoreductase), cob(II)alamin (radical/methyltransferase chemistry), Mo-bis(molybdopterin guanine dinucleotide) (molybdoenzyme oxidoreductases like nitrate reductase, xanthine oxidase), and Mn(2+) (divalent metal ion for hydrolytic enzymes such as phosphatases and nucleases). The sequence (193 AA) lacks any motifs diagnostic of redox enzymes: no Rossmann-fold NAD/FAD-binding, no molybdopterin-binding cysteine/serine clusters, no cob(II)alamin-binding domain architecture. Instead, the sequence contains clusters of acidic residues (multiple E and D residues, e.g., 'DCESTYEIEVELYDMFYLFEKELDIIIQEG') consistent with divalent-metal coordination sites typical of metallophosphatases. A model with general knowledge that phosphatases/nucleases require divalent metal ions (Mg2+, Mn2+) while Fe, B12, and Mo-bis(MGD) serve redox chemistry can eliminate A, B, and C and select D. This is a standard cofactor-to-enzyme-class inference learned from many other proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of three redox-associated cofactors and selection of a divalent metal ion is a well-established pattern in enzymology. The absence of redox motifs in the sequence combined with the presence of acidic-residue clusters provides a credible transferable argument distinguishing D from A, B, and C without needing the specific UniProt annotation for this protein."
  },
  "case_id": "cofactor_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q98500 (TPASE_PBCV1, 5'RNA triphosphatase A449R from PBCV-1) explicitly annotates Mn(2+) as the cofactor with experimental evidence (ECO:0000269|PubMed:11160672, Ho/Gong/Shuman 2001). The sequence matches exactly (193 AA, SHA256 confirmed). The expected answer D is directly supported by a direct-assay experimental reference."
  },
  "important_caveats": [
    "The specific assignment of Mn(2+) over Mg(2+) for this particular triphosphatase was established experimentally (Ho et al. 2001); general phosphatase knowledge would suggest 'a divalent metal ion' but the question conveniently omits Mg(2+) from the choices, making Mn(2+) the only divalent-metal option.",
    "The sequence alone does not unambiguously identify the protein as a triphosphatase; the reasoning relies on cofactor-class elimination rather than positive motif identification.",
    "The reviewer evidence confirms experimental (not merely computational) support for the Mn(2+) assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct cofactor classes (transition-metal redox, organometallic B12, molybdoenzyme, divalent metal hydrolysis). Only Mn(2+) is consistent with a hydrolytic enzyme lacking redox motifs. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q98500 (TPASE_PBCV1, 5'RNA triphosphatase A449R from PBCV-1) explicitly annotates Mn(2+) as the cofactor with experimental evidence (ECO:0000269|PubMed:11160672, Ho/Gong/Shuman 2001). The sequence matches exactly (193 AA, SHA256 confirmed). The expected answer D is directly supported by a direct-assay experimental reference.",
    "evidence_ids": ["C5", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options represent fundamentally different cofactor classes: Fe cation (redox/oxidoreductase), cob(II)alamin (radical/methyltransferase chemistry), Mo-bis(molybdopterin guanine dinucleotide) (molybdoenzyme oxidoreductases like nitrate reductase, xanthine oxidase), and Mn(2+) (divalent metal ion for hydrolytic enzymes such as phosphatases and nucleases). The sequence (193 AA) lacks any motifs diagnostic of redox enzymes: no Rossmann-fold NAD/FAD-binding, no molybdopterin-binding cysteine/serine clusters, no cob(II)alamin-binding domain architecture. Instead, the sequence contains clusters of acidic residues (multiple E and D residues, e.g., 'DCESTYEIEVELYDMFYLFEKELDIIIQEG') consistent with divalent-metal coordination sites typical of metallophosphatases. A model with general knowledge that phosphatases/nucleases require divalent metal ions (Mg2+, Mn2+) while Fe, B12, and Mo-bis(MGD) serve redox chemistry can eliminate A, B, and C and select D. This is a standard cofactor-to-enzyme-class inference learned from many other proteins.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of three redox-associated cofactors and selection of a divalent metal ion is a well-established pattern in enzymology. The absence of redox motifs in the sequence combined with the presence of acidic-residue clusters provides a credible transferable argument distinguishing D from A, B, and C without needing the specific UniProt annotation for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct cofactor classes (transition-metal redox, organometallic B12, molybdoenzyme, divalent metal hydrolysis). Only Mn(2+) is consistent with a hydrolytic enzyme lacking redox motifs. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The specific assignment of Mn(2+) over Mg(2+) for this particular triphosphatase was established experimentally (Ho et al. 2001); general phosphatase knowledge would suggest 'a divalent metal ion' but the question conveniently omits Mg(2+) from the choices, making Mn(2+) the only divalent-metal option.",
    "The sequence alone does not unambiguously identify the protein as a triphosphatase; the reasoning relies on cofactor-class elimination rather than positive motif identification.",
    "The reviewer evidence confirms experimental (not merely computational) support for the Mn(2+) assignment."
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
  "benchmark_sequence_length": 193,
  "benchmark_sequence_sha256": "2e3ef2dd5cc36f7f2ffcab76a32ce1bb6958f79ccde3e9c943bcd61f8649ed54",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1997-02-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 193,
  "current_source_sequence_sha256": "2e3ef2dd5cc36f7f2ffcab76a32ce1bb6958f79ccde3e9c943bcd61f8649ed54",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 85,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q98500",
  "selected_historical_entry_version": 85,
  "selected_historical_record_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "selected_historical_source_sequence_length": 193,
  "selected_historical_source_sequence_sha256": "2e3ef2dd5cc36f7f2ffcab76a32ce1bb6958f79ccde3e9c943bcd61f8649ed54",
  "selected_historical_version": {
    "accession": "Q98500",
    "database": "Swiss-Prot",
    "entryVersion": 85,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "TPASE_PBCV1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q98500\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1997-02-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"PBCV-1\",\"lineage\":[\"Viruses\",\"Varidnaviria\",\"Bamfordvirae\",\"Nucleocytoviricota\",\"Megaviricetes\",\"Algavirales\",\"Phycodnaviridae\",\"Chlorovirus\",\"Chlorovirus vanettense\"],\"scientificName\":\"Paramecium bursaria Chlorella virus 1\",\"taxonId\":10506}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"value\":\"3.6.1.74\"}],\"fullName\":{\"value\":\"5'RNA triphosphatase A449R\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11160672\",\"source\":\"PubMed\"}],\"name\":\"Mn(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ho C.K.\",\"Gong C.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11160672\"},{\"database\":\"DOI\",\"id\":\"10.1128/jvi.75.4.1744-1750.2001\"}],\"citationType\":\"journal article\",\"firstPage\":\"1744\",\"id\":\"11160672\",\"journal\":\"J. Virol.\",\"lastPage\":\"1750\",\"publicationDate\":\"2001\",\"title\":\"RNA triphosphatase component of the mRNA capping apparatus of Paramecium bursaria Chlorella virus 1.\",\"volume\":\"75\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CHARACTERIZATION OF TRIPHOSPHATASE ACTIVITY\",\"MUTAGENESIS OF GLU-26\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H1",
  "excerpt": "ID   TPASE_PBCV1             Reviewed;         193 AA.\nAC   Q98500;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-FEB-1997, sequence version 1.\nDT   28-JAN-2026, entry version 85.\nDE   RecName: Full=5'RNA triphosphatase A449R;\nDE            EC=3.6.1.74;\nGN   Name=A449R;\nOS   Paramecium bursaria Chlorella virus 1 (PBCV-1).\nOC   Viruses; Varidnaviria; Bamfordvirae; Nucleocytoviricota; Megaviricetes;\nOC   Algavirales; Phycodnaviridae; Chlorovirus; Chlorovirus vanettense.\nOX   NCBI_TaxID=10506;\nOH   NCBI_TaxID=3071; Chlorella.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=5'RNA triphosphatase A449R;\nDE            EC=3.6.1.74;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CHARACTERIZATION OF TRIPHOSPHATASE ACTIVITY, AND MUTAGENESIS OF\nRP   GLU-26.\nRX   PubMed=11160672; DOI=10.1128/jvi.75.4.1744-1750.2001;\nRA   Ho C.K., Gong C., Shuman S.;\nRT   \"RNA triphosphatase component of the mRNA capping apparatus of Paramecium\nRT   bursaria Chlorella virus 1.\";\nRL   J. Virol. 75:1744-1750(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;\nCC         Evidence={ECO:0000269|PubMed:11160672};\nCC   ---------------------------------------------------------------------------\nCC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms\nCC   Distributed under the Creative Commons Attribution (CC BY 4.0) License\nCC   ---------------------------------------------------------------------------\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 167. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
