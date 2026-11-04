# active_site_0144

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0144.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 367 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPQVRNPILPGFNPDPSILRVGEDYYIATSTFEWYPGVQIHHSRDLANWELVARPLNRKSQLDMRGNPDSCGIWAPCLSHDGERFWLVYTDVKRKDGSFKDTPNYIVTAEKIEGPWSDPIYINSSGFDPSLFHDDDGRKWFVNMLWDHRRRPQLFEGIVLQEFDPKAGKLVGPRKNIFTGTDLALVEGPHLYKRNGWYYLLTAEGGTGYEHACTFARSRNIWGPYEVHPQKYILTSKDHPHAALQRAGHGDIVDTPDGRTYLVHLTGRPTTQFRRCVLGRETAIQEAYWGDDDWLYVKNGPVPSLWVDLPAARDDTKYWEEKRYTFESGLHKDFQWLRTPETDRIFRTREDGKLTLIGRESIGSWFEQALVARRQTHFSCDAETVIDFSPEDQRQFAGLTAYYCRYNFFYLAVSAHSDGQRELFIMASEASWPLGELRYPVPEGVRIPNEGKVRLALTIRGRELQFYYALEGEELKKIGPVLDASIVSDECGGHQKHGSFTGAFVGVAASDLNGTAAEATFDYFIYRPVQHPSDRYEI

[Multiple Choices]
A. Position 154 (Nucleophile)
B. Position 367 (Proton donor)
C. Position 2153 (For beta-ketoacyl synthase 2 activity)
D. Position 124 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies position 367 as the proton donor. This supports choice B, though the annotation is transferred by similarity rather than direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 538-residue sequence is consistent with a GH43 glycosidase, whose family-level catalytic mechanism includes a glutamate proton donor. Position 367 is Glu in the supplied sequence, whereas position 154 is Leu and position 124 is Ser; position 2153 is outside the sequence. Those features meaningfully distinguish B from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choice can be inferred from the sequence residue identities and transferable family-level knowledge about GH43 catalysis; recalling this protein's specific database annotation is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B matches both the proton-donor role and a plausible catalytic residue at the stated position; the other positions or residue descriptions do not fit.


### Important caveats

- The source annotation assigns the proton-donor role by similarity to another protein, not by direct experimental evidence for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 538-residue sequence is consistent with a GH43 glycosidase, whose family-level catalytic mechanism includes a glutamate proton donor. Position 367 is Glu in the supplied sequence, whereas position 154 is Leu and position 124 is Ser; position 2153 is outside the sequence. Those features meaningfully distinguish B from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choice can be inferred from the sequence residue identities and transferable family-level knowledge about GH43 catalysis; recalling this protein's specific database annotation is not necessary."
  },
  "case_id": "active_site_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 367 as the proton donor. This supports choice B, though the annotation is transferred by similarity rather than direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The source annotation assigns the proton-donor role by similarity to another protein, not by direct experimental evidence for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B matches both the proton-donor role and a plausible catalytic residue at the stated position; the other positions or residue descriptions do not fit."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 367 as the proton donor. This supports choice B, though the annotation is transferred by similarity rather than direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 538-residue sequence is consistent with a GH43 glycosidase, whose family-level catalytic mechanism includes a glutamate proton donor. Position 367 is Glu in the supplied sequence, whereas position 154 is Leu and position 124 is Ser; position 2153 is outside the sequence. Those features meaningfully distinguish B from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The choice can be inferred from the sequence residue identities and transferable family-level knowledge about GH43 catalysis; recalling this protein's specific database annotation is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B matches both the proton-donor role and a plausible catalytic residue at the stated position; the other positions or residue descriptions do not fit."
  },
  "important_caveats": [
    "The source annotation assigns the proton-donor role by similarity to another protein, not by direct experimental evidence for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry V9TT49 annotates position 367 as 'Proton donor' (Active site feature). The residue at position 367 in the supplied 538-aa sequence is Glutamic acid (E), which is the canonical acid catalyst in GH43 glycoside hydrolases. The annotation evidence code is ECO:0000250 (inferred by similarity to Q45071), meaning this is a computational/family-level inference rather than direct experimental measurement on this exact protein, but it is consistent with established GH43 catalytic mechanisms. The annotation is present and matches the expected answer B.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A model can meaningfully narrow the choices using sequence-level reasoning and general biochemistry: (1) Option C (position 2153) is immediately eliminated because the protein is only 538 residues long. (2) Option A (position 154, Nucleophile): residue 154 is Leucine (L), which has no nucleophilic side chain and cannot serve as a catalytic nucleophile in any enzyme. (3) Between B (position 367, Glutamic acid, Proton donor) and D (position 124, Serine, Proton donor): in glycoside hydrolases (the functional class indicated by the beta-propeller-like sequence architecture and conserved motifs such as 'TGTDLALVEG' and 'WYYLL'), the acid/base catalyst (proton donor) is canonically an Asp or Glu, not a Ser. Serine serves as a nucleophile in serine proteases but is essentially never the proton donor in glycosidases. Glu at position 367, embedded in the context 'IGRE-SIGSWFEQ', aligns with the conserved catalytic Glu of GH43-family enzymes. This combination of length elimination, amino-acid chemistry, and family-level catalytic-residue knowledge (Glu/Asp as acid in glycosidases) provides a concrete, transferable basis to select B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The discrimination relies on: (a) arithmetic elimination of C by sequence length, (b) amino-acid identity at position 154 being Leu (non-nucleophilic), and (c) the well-established principle that glycosidase proton donors are Asp/Glu rather than Ser. These are all transferable biochemical principles applicable to any glycosidase-like sequence without needing the specific UniProt annotation for V9TT49.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor is eliminated by a distinct, non-overlapping criterion: C by impossibility (position > length), A by amino-acid chemistry (Leu cannot be a nucleophile), D by family-level catalytic-residue preference (Ser is not a proton donor in glycosidases). Only B satisfies all constraints simultaneously.


### Important caveats

- The UniProt annotation at position 367 carries evidence code ECO:0000250 (similarity to Q45071), meaning it is a family-level computational inference rather than direct experimental mutagenesis or structural proof on this specific protein.
- GH43 family recognition from the raw sequence is plausible via beta-propeller motifs but not trivially obvious; however, the amino-acid chemistry argument (Glu vs. Ser as proton donor) provides a robust fallback even without explicit family identification.
- The question labels options by role (Nucleophile, Proton donor) rather than asking the model to assign roles, which reduces ambiguity in the catalytic-mechanism assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can meaningfully narrow the choices using sequence-level reasoning and general biochemistry: (1) Option C (position 2153) is immediately eliminated because the protein is only 538 residues long. (2) Option A (position 154, Nucleophile): residue 154 is Leucine (L), which has no nucleophilic side chain and cannot serve as a catalytic nucleophile in any enzyme. (3) Between B (position 367, Glutamic acid, Proton donor) and D (position 124, Serine, Proton donor): in glycoside hydrolases (the functional class indicated by the beta-propeller-like sequence architecture and conserved motifs such as 'TGTDLALVEG' and 'WYYLL'), the acid/base catalyst (proton donor) is canonically an Asp or Glu, not a Ser. Serine serves as a nucleophile in serine proteases but is essentially never the proton donor in glycosidases. Glu at position 367, embedded in the context 'IGRE-SIGSWFEQ', aligns with the conserved catalytic Glu of GH43-family enzymes. This combination of length elimination, amino-acid chemistry, and family-level catalytic-residue knowledge (Glu/Asp as acid in glycosidases) provides a concrete, transferable basis to select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The discrimination relies on: (a) arithmetic elimination of C by sequence length, (b) amino-acid identity at position 154 being Leu (non-nucleophilic), and (c) the well-established principle that glycosidase proton donors are Asp/Glu rather than Ser. These are all transferable biochemical principles applicable to any glycosidase-like sequence without needing the specific UniProt annotation for V9TT49."
  },
  "case_id": "active_site_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry V9TT49 annotates position 367 as 'Proton donor' (Active site feature). The residue at position 367 in the supplied 538-aa sequence is Glutamic acid (E), which is the canonical acid catalyst in GH43 glycoside hydrolases. The annotation evidence code is ECO:0000250 (inferred by similarity to Q45071), meaning this is a computational/family-level inference rather than direct experimental measurement on this exact protein, but it is consistent with established GH43 catalytic mechanisms. The annotation is present and matches the expected answer B."
  },
  "important_caveats": [
    "The UniProt annotation at position 367 carries evidence code ECO:0000250 (similarity to Q45071), meaning it is a family-level computational inference rather than direct experimental mutagenesis or structural proof on this specific protein.",
    "GH43 family recognition from the raw sequence is plausible via beta-propeller motifs but not trivially obvious; however, the amino-acid chemistry argument (Glu vs. Ser as proton donor) provides a robust fallback even without explicit family identification.",
    "The question labels options by role (Nucleophile, Proton donor) rather than asking the model to assign roles, which reduces ambiguity in the catalytic-mechanism assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor is eliminated by a distinct, non-overlapping criterion: C by impossibility (position > length), A by amino-acid chemistry (Leu cannot be a nucleophile), D by family-level catalytic-residue preference (Ser is not a proton donor in glycosidases). Only B satisfies all constraints simultaneously."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry V9TT49 annotates position 367 as 'Proton donor' (Active site feature). The residue at position 367 in the supplied 538-aa sequence is Glutamic acid (E), which is the canonical acid catalyst in GH43 glycoside hydrolases. The annotation evidence code is ECO:0000250 (inferred by similarity to Q45071), meaning this is a computational/family-level inference rather than direct experimental measurement on this exact protein, but it is consistent with established GH43 catalytic mechanisms. The annotation is present and matches the expected answer B.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A model can meaningfully narrow the choices using sequence-level reasoning and general biochemistry: (1) Option C (position 2153) is immediately eliminated because the protein is only 538 residues long. (2) Option A (position 154, Nucleophile): residue 154 is Leucine (L), which has no nucleophilic side chain and cannot serve as a catalytic nucleophile in any enzyme. (3) Between B (position 367, Glutamic acid, Proton donor) and D (position 124, Serine, Proton donor): in glycoside hydrolases (the functional class indicated by the beta-propeller-like sequence architecture and conserved motifs such as 'TGTDLALVEG' and 'WYYLL'), the acid/base catalyst (proton donor) is canonically an Asp or Glu, not a Ser. Serine serves as a nucleophile in serine proteases but is essentially never the proton donor in glycosidases. Glu at position 367, embedded in the context 'IGRE-SIGSWFEQ', aligns with the conserved catalytic Glu of GH43-family enzymes. This combination of length elimination, amino-acid chemistry, and family-level catalytic-residue knowledge (Glu/Asp as acid in glycosidases) provides a concrete, transferable basis to select B.",
    "missing_item_specific_fact": "",
    "reason": "The discrimination relies on: (a) arithmetic elimination of C by sequence length, (b) amino-acid identity at position 154 being Leu (non-nucleophilic), and (c) the well-established principle that glycosidase proton donors are Asp/Glu rather than Ser. These are all transferable biochemical principles applicable to any glycosidase-like sequence without needing the specific UniProt annotation for V9TT49."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor is eliminated by a distinct, non-overlapping criterion: C by impossibility (position > length), A by amino-acid chemistry (Leu cannot be a nucleophile), D by family-level catalytic-residue preference (Ser is not a proton donor in glycosidases). Only B satisfies all constraints simultaneously."
  },
  "important_caveats": [
    "The UniProt annotation at position 367 carries evidence code ECO:0000250 (similarity to Q45071), meaning it is a family-level computational inference rather than direct experimental mutagenesis or structural proof on this specific protein.",
    "GH43 family recognition from the raw sequence is plausible via beta-propeller motifs but not trivially obvious; however, the amino-acid chemistry argument (Glu vs. Ser as proton donor) provides a robust fallback even without explicit family identification.",
    "The question labels options by role (Nucleophile, Proton donor) rather than asking the model to assign roles, which reduces ambiguity in the catalytic-mechanism assignment."
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
  "benchmark_sequence_length": 538,
  "benchmark_sequence_sha256": "4c5f6ce116665066820aa85f61aa5d53cbd37564158534eb94cfe0b3bdb23c65",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 538,
  "current_source_sequence_sha256": "4c5f6ce116665066820aa85f61aa5d53cbd37564158534eb94cfe0b3bdb23c65",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "V9TT49",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "selected_historical_source_sequence_length": 538,
  "selected_historical_source_sequence_sha256": "4c5f6ce116665066820aa85f61aa5d53cbd37564158534eb94cfe0b3bdb23c65",
  "selected_historical_version": {
    "accession": "V9TT49",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XY43B_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"V9TT49\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"includes\":[{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"1,4-beta-D-xylan xylohydrolase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Xylan 1,4-beta-xylosidase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.37\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Beta-xylosidase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.55\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Alpha-L-arabinofuranosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Arabinosidase\"}]}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Xylosidase/arabinosidase 43B\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q45071\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":367},\"start\":{\"modifier\":\"EXACT\",\"value\":367}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.\",\"Shi P.\",\"Huang H.\",\"Luo H.\",\"Wang Y.\",\"Zhang W.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24262572\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.foodchem.2013.10.062\"}],\"citationType\":\"journal article\",\"firstPage\":\"381\",\"id\":\"24262572\",\"journal\":\"Food Chem.\",\"lastPage\":\"387\",\"publicationDate\":\"2014\",\"title\":\"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and one GH11 xylanase from Humicola insolens and their synergy in the degradation of xylan.\",\"volume\":\"148\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:30.461216+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93",
  "url": "https://rest.uniprot.org/uniprotkb/V9TT49.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   XY43B_HUMIN             Reviewed;         538 AA.\nAC   V9TT49;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Xylosidase/arabinosidase 43B {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};\nDE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};\nDE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};\nDE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};\nGN   Name=Xyl43B {ECO:0000303|PubMed:24262572};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "url": "https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   SUBCELLULAR LOCATION, AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=24262572; DOI=10.1016/j.foodchem.2013.10.062;\nRA   Yang X., Shi P., Huang H., Luo H., Wang Y., Zhang W., Yao B.;\nRT   \"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and\nRT   one GH11 xylanase from Humicola insolens and their synergy in the\nRT   degradation of xylan.\";\nRL   Food Chem. 148:381-387(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "url": "https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        367\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q45071\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:54.377134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c",
  "url": "https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 144. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
