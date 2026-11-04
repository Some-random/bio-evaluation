# cofactor_0035

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0035.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRTTLTGTASVLDTTLTRLIDDVIENGSSFLADDENLQHYKQHLSHLETASKIALLRECLCVRPPLPLLPEDLLQNVDSILTRVRQHKILTPIFSLSPSRLIKHGDLGATRIHLWRGDITTLTGVTAITNAANSQGLGCFQPTHRCIDNIIHAEAGPRLREECFQRMQARGKELEPGEVLVTEGHALFASSVMHTVGPQLKRGASPTETERRQLAKCYESILEALELLPSDEDGSKSIALCCISTGLFAFPADEAAEIAVSTVTSWLQKHPSTTITDVIFNTFTQSDTEFYSKLLGPSHTKSISPVENTPQGSLSLAREWLSSADAVLVTAGAGLSAAEGLDYHSRDLFKRNFPGCLKFGLTSLYSVFGFNDWPSEEHRWGYFFTHLNMVANWSNTPTYQILIPWLRNFGQDAFVRTSNADGLFLANGWPKEQLSTPQGSYGYLQCLNNCRVDAVVPSAPLVADAMPHIDKATQKLMDPSKIPLCRFCGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKKNLVILELGVGMNTPGVLRWPNEDLVMRSDGRVKLIRVGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE

[Multiple Choices]
A. Zn(2+)
B. Mo-bis(molybdopterin guanine dinucleotide)
C. Mn(2+)
D. heme b
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

> The sequence-matched UniProt entry records Zn(2+) as the cofactor, with experimental evidence and a note that two zinc ions bind per subunit. Its cited reference also reports a crystal structure in complex with Zn(2+).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a multidomain ADP-ribose enzyme, and its cysteine/histidine-containing regions make a zinc-dependent catalytic domain a credible family-level inference. That pattern favors Zn(2+) over the more specialized molybdopterin cofactor or heme b, and over Mn(2+) as a less specifically indicated metal option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of zinc-dependent ADP-ribose enzyme families and metal-binding sequence patterns provides a meaningful, though not conclusive, basis for choosing Zn(2+) among these options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives are distinct, and the family-level zinc inference favors one offered option.


### Important caveats

- The sequence alone does not prove cofactor binding or establish the reported two-zinc stoichiometry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a multidomain ADP-ribose enzyme, and its cysteine/histidine-containing regions make a zinc-dependent catalytic domain a credible family-level inference. That pattern favors Zn(2+) over the more specialized molybdopterin cofactor or heme b, and over Mn(2+) as a less specifically indicated metal option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of zinc-dependent ADP-ribose enzyme families and metal-binding sequence patterns provides a meaningful, though not conclusive, basis for choosing Zn(2+) among these options."
  },
  "case_id": "cofactor_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry records Zn(2+) as the cofactor, with experimental evidence and a note that two zinc ions bind per subunit. Its cited reference also reports a crystal structure in complex with Zn(2+)."
  },
  "important_caveats": [
    "The sequence alone does not prove cofactor binding or establish the reported two-zinc stoichiometry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are distinct, and the family-level zinc inference favors one offered option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry records Zn(2+) as the cofactor, with experimental evidence and a note that two zinc ions bind per subunit. Its cited reference also reports a crystal structure in complex with Zn(2+).",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a multidomain ADP-ribose enzyme, and its cysteine/histidine-containing regions make a zinc-dependent catalytic domain a credible family-level inference. That pattern favors Zn(2+) over the more specialized molybdopterin cofactor or heme b, and over Mn(2+) as a less specifically indicated metal option.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of zinc-dependent ADP-ribose enzyme families and metal-binding sequence patterns provides a meaningful, though not conclusive, basis for choosing Zn(2+) among these options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are distinct, and the family-level zinc inference favors one offered option."
  },
  "important_caveats": [
    "The sequence alone does not prove cofactor binding or establish the reported two-zinc stoichiometry."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C5, C6, H3, H4) confirms Zn(2+) as the experimentally determined cofactor with ECO:0000269 (experimental evidence) from a 2024 JBC paper (PubMed:39270823) reporting X-ray crystallography at 2.22 Å in complex with Zn(2+), showing 2 Zn(2+) ions per subunit. The sequence in the benchmark matches the UniProt entry A0A559KX76 (597 AA, SHA-256 match). The cofactor annotation is backed by structural and biochemical evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains features recognizable as a macrodomain/ADP-ribosylhydrolase family protein: Cys-rich motifs (RECLCV near residues 55-60, CYS clusters, CRFCGSKMSICV) and a fold pattern consistent with the ~100-150 residue macrodomain domain. This family (including human MacroD1/D2, ARH3, and bacterial macrodomains) is well-characterized as Zn(2+)-dependent ADP-ribosylhydrolases, with Zn(2+) coordinated by conserved His and Cys residues. Against the alternatives: (1) Mo-bis(MGD) requires molybdoenzyme-specific domains (MPT-binding, Mo-cofactor binding motifs) absent here; (2) heme b requires CXXCH cytochrome motifs or specific His ligation patterns not present; (3) Mn(2+) is used by some phosphatases/hydrolases but the macrodomain ADP-ribosylhydrolase family overwhelmingly uses Zn(2+), and the Cys-His coordination geometry visible in the sequence (multiple Cys pairs flanking His residues) is more consistent with tetrahedral Zn(2+) than octahedral Mn(2+). A model familiar with the macrodomain protein family and its Zn-dependence, combined with recognition of the Cys-rich zinc-coordination motifs in the sequence, can meaningfully select Zn(2+) over the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The macrodomain/ADP-ribosylhydrolase family is a well-studied protein family whose Zn(2+) dependence is a family-level property transferable from other members (MacroD1, MacroD2, ARH3, bacterial macrodomains). The sequence shows Cys-rich motifs consistent with Zn coordination. The three distractors (Mo-cofactor, Mn(2+), heme b) are excluded by absence of their respective structural signatures and by family-level knowledge that macrodomain ADP-ribosylhydrolases are Zn-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The macrodomain family Zn-dependence and the Cys-rich sequence motifs provide a clear basis for selecting Zn(2+). The other three options lack any supporting sequence features: no molybdoenzyme domains, no heme-binding CXXCH motifs, and the coordination chemistry of the visible Cys/His clusters favors Zn over Mn.


### Important caveats

- The UniProt annotation is labeled 'Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase' with the ADP-ribosyltransferase activity inferred by similarity (ECO:0000250), but the hydrolase activity and Zn cofactor are experimentally confirmed (ECO:0000269, X-ray crystallography).
- The entry was first publicly released in June 2025 and the Zn cofactor was annotated in 2024; depending on the author's source snapshot, this protein may or may not have been annotated at the time of benchmark construction. However, the family-level Zn-dependence of macrodomains predates this specific entry.
- Distinguishing Zn(2+) from Mn(2+) by sequence alone can be subtle in some hydrolase families, but the macrodomain family context and Cys-His coordination geometry strongly favor Zn.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features recognizable as a macrodomain/ADP-ribosylhydrolase family protein: Cys-rich motifs (RECLCV near residues 55-60, CYS clusters, CRFCGSKMSICV) and a fold pattern consistent with the ~100-150 residue macrodomain domain. This family (including human MacroD1/D2, ARH3, and bacterial macrodomains) is well-characterized as Zn(2+)-dependent ADP-ribosylhydrolases, with Zn(2+) coordinated by conserved His and Cys residues. Against the alternatives: (1) Mo-bis(MGD) requires molybdoenzyme-specific domains (MPT-binding, Mo-cofactor binding motifs) absent here; (2) heme b requires CXXCH cytochrome motifs or specific His ligation patterns not present; (3) Mn(2+) is used by some phosphatases/hydrolases but the macrodomain ADP-ribosylhydrolase family overwhelmingly uses Zn(2+), and the Cys-His coordination geometry visible in the sequence (multiple Cys pairs flanking His residues) is more consistent with tetrahedral Zn(2+) than octahedral Mn(2+). A model familiar with the macrodomain protein family and its Zn-dependence, combined with recognition of the Cys-rich zinc-coordination motifs in the sequence, can meaningfully select Zn(2+) over the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The macrodomain/ADP-ribosylhydrolase family is a well-studied protein family whose Zn(2+) dependence is a family-level property transferable from other members (MacroD1, MacroD2, ARH3, bacterial macrodomains). The sequence shows Cys-rich motifs consistent with Zn coordination. The three distractors (Mo-cofactor, Mn(2+), heme b) are excluded by absence of their respective structural signatures and by family-level knowledge that macrodomain ADP-ribosylhydrolases are Zn-dependent."
  },
  "case_id": "cofactor_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, C6, H3, H4) confirms Zn(2+) as the experimentally determined cofactor with ECO:0000269 (experimental evidence) from a 2024 JBC paper (PubMed:39270823) reporting X-ray crystallography at 2.22 Å in complex with Zn(2+), showing 2 Zn(2+) ions per subunit. The sequence in the benchmark matches the UniProt entry A0A559KX76 (597 AA, SHA-256 match). The cofactor annotation is backed by structural and biochemical evidence."
  },
  "important_caveats": [
    "The UniProt annotation is labeled 'Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase' with the ADP-ribosyltransferase activity inferred by similarity (ECO:0000250), but the hydrolase activity and Zn cofactor are experimentally confirmed (ECO:0000269, X-ray crystallography).",
    "The entry was first publicly released in June 2025 and the Zn cofactor was annotated in 2024; depending on the author's source snapshot, this protein may or may not have been annotated at the time of benchmark construction. However, the family-level Zn-dependence of macrodomains predates this specific entry.",
    "Distinguishing Zn(2+) from Mn(2+) by sequence alone can be subtle in some hydrolase families, but the macrodomain family context and Cys-His coordination geometry strongly favor Zn."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The macrodomain family Zn-dependence and the Cys-rich sequence motifs provide a clear basis for selecting Zn(2+). The other three options lack any supporting sequence features: no molybdoenzyme domains, no heme-binding CXXCH motifs, and the coordination chemistry of the visible Cys/His clusters favors Zn over Mn."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, C6, H3, H4) confirms Zn(2+) as the experimentally determined cofactor with ECO:0000269 (experimental evidence) from a 2024 JBC paper (PubMed:39270823) reporting X-ray crystallography at 2.22 Å in complex with Zn(2+), showing 2 Zn(2+) ions per subunit. The sequence in the benchmark matches the UniProt entry A0A559KX76 (597 AA, SHA-256 match). The cofactor annotation is backed by structural and biochemical evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains features recognizable as a macrodomain/ADP-ribosylhydrolase family protein: Cys-rich motifs (RECLCV near residues 55-60, CYS clusters, CRFCGSKMSICV) and a fold pattern consistent with the ~100-150 residue macrodomain domain. This family (including human MacroD1/D2, ARH3, and bacterial macrodomains) is well-characterized as Zn(2+)-dependent ADP-ribosylhydrolases, with Zn(2+) coordinated by conserved His and Cys residues. Against the alternatives: (1) Mo-bis(MGD) requires molybdoenzyme-specific domains (MPT-binding, Mo-cofactor binding motifs) absent here; (2) heme b requires CXXCH cytochrome motifs or specific His ligation patterns not present; (3) Mn(2+) is used by some phosphatases/hydrolases but the macrodomain ADP-ribosylhydrolase family overwhelmingly uses Zn(2+), and the Cys-His coordination geometry visible in the sequence (multiple Cys pairs flanking His residues) is more consistent with tetrahedral Zn(2+) than octahedral Mn(2+). A model familiar with the macrodomain protein family and its Zn-dependence, combined with recognition of the Cys-rich zinc-coordination motifs in the sequence, can meaningfully select Zn(2+) over the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "The macrodomain/ADP-ribosylhydrolase family is a well-studied protein family whose Zn(2+) dependence is a family-level property transferable from other members (MacroD1, MacroD2, ARH3, bacterial macrodomains). The sequence shows Cys-rich motifs consistent with Zn coordination. The three distractors (Mo-cofactor, Mn(2+), heme b) are excluded by absence of their respective structural signatures and by family-level knowledge that macrodomain ADP-ribosylhydrolases are Zn-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The macrodomain family Zn-dependence and the Cys-rich sequence motifs provide a clear basis for selecting Zn(2+). The other three options lack any supporting sequence features: no molybdoenzyme domains, no heme-binding CXXCH motifs, and the coordination chemistry of the visible Cys/His clusters favors Zn over Mn."
  },
  "important_caveats": [
    "The UniProt annotation is labeled 'Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase' with the ADP-ribosyltransferase activity inferred by similarity (ECO:0000250), but the hydrolase activity and Zn cofactor are experimentally confirmed (ECO:0000269, X-ray crystallography).",
    "The entry was first publicly released in June 2025 and the Zn cofactor was annotated in 2024; depending on the author's source snapshot, this protein may or may not have been annotated at the time of benchmark construction. However, the family-level Zn-dependence of macrodomains predates this specific entry.",
    "Distinguishing Zn(2+) from Mn(2+) by sequence alone can be subtle in some hydrolase families, but the macrodomain family context and Cys-His coordination geometry strongly favor Zn."
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
  "benchmark_sequence_length": 597,
  "benchmark_sequence_sha256": "fb7122de3adfadd42d80b188dae7090de1939670d22c33aa431753afa5349321",
  "current_entry_audit": {
    "entryVersion": 24,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-10-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 597,
  "current_source_sequence_sha256": "fb7122de3adfadd42d80b188dae7090de1939670d22c33aa431753afa5349321",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 22,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A559KX76",
  "selected_historical_entry_version": 22,
  "selected_historical_record_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "selected_historical_source_sequence_length": 597,
  "selected_historical_source_sequence_sha256": "fb7122de3adfadd42d80b188dae7090de1939670d22c33aa431753afa5349321",
  "selected_historical_version": {
    "accession": "A0A559KX76",
    "database": "Swiss-Prot",
    "entryVersion": 22,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ADRHT_FUSOC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A559KX76\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":24,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-10-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Nectriaceae\",\"Fusarium\",\"Fusarium oxysporum species complex\"],\"scientificName\":\"Fusarium oxysporum f. sp. cubense\",\"taxonId\":61366}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"value\":\"Foc1Mfs1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WZU87063.1\",\"source\":\"EMBL\"}],\"value\":\"Macrodomain-fused SirTM 1\"}}],\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Protein-ADP-ribose hydrolase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0DN71\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable protein ADP-ribosyltransferase\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"value\":\"Binds 2 Zn(2+) ions per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ariza A.\",\"Liu Q.\",\"Cowieson N.P.\",\"Ahel I.\",\"Filippov D.V.\",\"Rack J.G.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39270823\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107770\"}],\"citationType\":\"journal article\",\"firstPage\":\"107770\",\"id\":\"39270823\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107770\",\"publicationDate\":\"2024\",\"title\":\"Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-dependent macrodomains.\",\"volume\":\"300\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8RSN\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"race 1 / IMI 141109\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS) IN COMPLEX WITH ZN(2+)\",\"FUNCTION AS AN HYDROLASE\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBUNIT\",\"MUTAGENESIS OF CYS-61 AND HIS-144\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H1",
  "excerpt": "ID   ADRHT_FUSOC             Reviewed;         597 AA.\nAC   A0A559KX76;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-OCT-2019, sequence version 1.\nDT   28-JAN-2026, entry version 22.\nDE   RecName: Full=Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase {ECO:0000305};\nDE   AltName: Full=Foc1Mfs1 {ECO:0000303|PubMed:39270823};\nDE   AltName: Full=Macrodomain-fused SirTM 1 {ECO:0000312|EMBL:WZU87063.1};\nDE   Includes:\nDE     RecName: Full=Protein-ADP-ribose hydrolase {ECO:0000305};\nDE              EC=3.2.1.- {ECO:0000269|PubMed:39270823};\nDE   Includes:\nDE     RecName: Full=Probable protein ADP-ribosyltransferase {ECO:0000305};\nDE              EC=2.4.2.- {ECO:0000250|UniProtKB:P0DN71};\nGN   Name=mfs1 {ECO:0000312|EMBL:WZU87063.1};\nGN   ORFNames=Focb16_v015632 {ECO:0000312|EMBL:TVY64815.1};\nOS   Fusarium oxysporum f. sp. cubense.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Nectriaceae; Fusarium;\nOC   Fusarium oxysporum species complex.\nOX   NCBI_TaxID=61366;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase {ECO:0000305};\nDE   AltName: Full=Foc1Mfs1 {ECO:0000303|PubMed:39270823};\nDE   AltName: Full=Macrodomain-fused SirTM 1 {ECO:0000312|EMBL:WZU87063.1};\nDE   Includes:\nDE     RecName: Full=Protein-ADP-ribose hydrolase {ECO:0000305};\nDE              EC=3.2.1.- {ECO:0000269|PubMed:39270823};\nDE   Includes:\nDE     RecName: Full=Probable protein ADP-ribosyltransferase {ECO:0000305};\nDE              EC=2.4.2.- {ECO:0000250|UniProtKB:P0DN71};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:8RSN}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS)\nRP   IN COMPLEX WITH ZN(2+), FUNCTION AS AN HYDROLASE, CATALYTIC ACTIVITY,\nRP   COFACTOR, SUBUNIT, AND MUTAGENESIS OF CYS-61 AND HIS-144.\nRC   STRAIN=race 1 / IMI 141109;\nRX   PubMed=39270823; DOI=10.1016/j.jbc.2024.107770;\nRA   Ariza A., Liu Q., Cowieson N.P., Ahel I., Filippov D.V., Rack J.G.M.;\nRT   \"Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-\nRT   dependent macrodomains.\";\nRL   J. Biol. Chem. 300:107770-107770(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000269|PubMed:39270823};\nCC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000305|PubMed:39270823};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 35. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
