# catalytic_activity_0144

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0144.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — inosine(in) = inosine(out)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTTSSDSAMVNHTPSPWYKFGFKSFAEFNTYVTFVFLGMSIMMVASAVTSAPDFLTRYYVYATGDPDAVAETPLFWNNANTFYNAGTYVLQVLTELFSLTPFMRRIPLSVRLFVGLGIPFAELLLIIIVPAATIKSQHGAIAVIMVVACVGGFSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALLMSIIQIILKVSMGTSFHDILTMSRIYFGICIGIQLFAIFELAILRFNPFAQKYIAEYRAGAQRNAQNNESTLEETAPSMNEPAAGDIADLPATVDDKERALNEEEGDEVRAVTSEEFHVKRGAVLTATGDADKMVDLDQTGNITSTEQLLRASAASVFKRVYPMLVCVFLIYFTSLLTFPGVFFLVSTTSGWYMTVIVTLFNAGDFISRMVLMFRPLRPSPKVVVAGTLGRLIIIPFLVLCVRGIIRGEALPYVLITLLGLTNGYFGCMACIHCPRTTTLRYAGERSLAAMLSGISIMLGLCFGSNLSLAITLTH

[Multiple Choices]
A. lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol
B. inosine(in) = inosine(out)
C. Mg(2+)(in) = Mg(2+)(out)
D. a primary alcohol + NAD(+) = an aldehyde + NADH + H(+)
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

> The sequence-matched entry records inosine transport as the reaction, with experimental evidence cited (ECO:0000269). This supports choice B for the supplied protein.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The roughly 500-residue sequence has the many-transmembrane-helix architecture and sequence pattern characteristic of equilibrative nucleoside transporter family proteins. Transferable knowledge of that family supports nucleoside translocation, making B a meaningful fit; the other choices describe magnesium transport or chemically transforming enzyme reactions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition provides a credible distinction among these options without needing the exact protein's recorded answer. Sequence alone may not establish inosine as a substrate with certainty, but B is supported by the family inference and the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options present distinct reaction types, and the sequence supports a nucleoside transporter rather than the alternatives.


### Important caveats

- The evidence supports this specific substrate annotation experimentally, while the transferable inference from the sequence identifies the transporter family more readily than it proves inosine specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The roughly 500-residue sequence has the many-transmembrane-helix architecture and sequence pattern characteristic of equilibrative nucleoside transporter family proteins. Transferable knowledge of that family supports nucleoside translocation, making B a meaningful fit; the other choices describe magnesium transport or chemically transforming enzyme reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition provides a credible distinction among these options without needing the exact protein's recorded answer. Sequence alone may not establish inosine as a substrate with certainty, but B is supported by the family inference and the offered alternatives."
  },
  "case_id": "catalytic_activity_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched entry records inosine transport as the reaction, with experimental evidence cited (ECO:0000269). This supports choice B for the supplied protein."
  },
  "important_caveats": [
    "The evidence supports this specific substrate annotation experimentally, while the transferable inference from the sequence identifies the transporter family more readily than it proves inosine specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options present distinct reaction types, and the sequence supports a nucleoside transporter rather than the alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched entry records inosine transport as the reaction, with experimental evidence cited (ECO:0000269). This supports choice B for the supplied protein.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The roughly 500-residue sequence has the many-transmembrane-helix architecture and sequence pattern characteristic of equilibrative nucleoside transporter family proteins. Transferable knowledge of that family supports nucleoside translocation, making B a meaningful fit; the other choices describe magnesium transport or chemically transforming enzyme reactions.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition provides a credible distinction among these options without needing the exact protein's recorded answer. Sequence alone may not establish inosine as a substrate with certainty, but B is supported by the family inference and the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options present distinct reaction types, and the sequence supports a nucleoside transporter rather than the alternatives."
  },
  "important_caveats": [
    "The evidence supports this specific substrate annotation experimentally, while the transferable inference from the sequence identifies the transporter family more readily than it proves inosine specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9GTP4 (NT2_CRIFA, Crithidia fasciculata) explicitly annotates 'inosine(in) = inosine(out)' as a catalytic/transporter activity with direct experimental evidence (ECO:0000269, PubMed:15694482 and PubMed:20037157). The protein is named 'Nucleoside transporter 2' / 'Equilibrative nucleoside transporter 2.' The sequence in the question matches the canonical entry exactly (502 aa, SHA256 confirmed). The evidence is experimental, not merely computational inference.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 502-aa sequence exhibits a highly hydrophobic, multi-pass transmembrane architecture with approximately 11 transmembrane helical segments and an N-terminal signal peptide, which is the hallmark topology of the equilibrative nucleoside transporter (ENT/SLC29) family. This architecture immediately eliminates: (D) alcohol dehydrogenase, which is a ~350-aa soluble enzyme with a Rossmann-fold NAD-binding domain (GxGxG motif) and no TM segments; (A) lipid A phosphotransferase, which is a membrane-associated but not multi-pass TM enzyme with catalytic His/Asp residues for phosphotransfer; and (C) Mg(2+) transporters such as CorA (4 TM + large cytoplasmic domain) or MgtE (5 TM + CBS domains), whose topologies are fundamentally different from the 11-TM pattern seen here. Among the remaining transporter options, the equilibrative (passive, no ATP/proton coupling) format 'substrate(in) = substrate(out)' matches the ENT family mechanism. Within ENT transporters, purine nucleosides like inosine are canonical substrates. The sequence also contains a region (~residues 138-172) consistent with TM4, which in ENT family members forms part of the nucleoside-binding pocket. This is a family-level topological and mechanistic inference transferable from well-characterized ENT homologs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-pass TM topology (~11 helices), signal peptide, and equilibrative transport format are directly readable from the sequence and match the ENT family. Distinguishing ENT from Mg transporters (CorA/MgtE) and from soluble enzymes (ADH, lipid A phosphotransferase) is achievable through standard family-level topology knowledge without needing the specific UniProt annotation of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different protein classes (lipid A phosphotransferase, nucleoside transporter, Mg transporter, alcohol dehydrogenase) with distinct architectures and mechanisms. The sequence's 11-TM membrane topology and equilibrative format uniquely point to B. No other option is architecturally or mechanistically plausible for this sequence.


### Important caveats

- The UniProt entry also lists 'guanosine(in) = guanosine(out)' as a catalytic activity, but guanosine transport is not among the offered choices, so this does not create ambiguity within the given options.
- The protein is from Crithidia fasciculata (a trypanosomatid), an organism not explicitly stated in the question; however, the ENT family topology is conserved across eukaryotes and the reasoning does not depend on knowing the organism.
- The sequence was annotated in 2025 (Swiss-Prot integration) based on 2005 and 2010 experimental papers; the evidence codes (ECO:0000269) indicate direct experimental assay evidence, not computational prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 502-aa sequence exhibits a highly hydrophobic, multi-pass transmembrane architecture with approximately 11 transmembrane helical segments and an N-terminal signal peptide, which is the hallmark topology of the equilibrative nucleoside transporter (ENT/SLC29) family. This architecture immediately eliminates: (D) alcohol dehydrogenase, which is a ~350-aa soluble enzyme with a Rossmann-fold NAD-binding domain (GxGxG motif) and no TM segments; (A) lipid A phosphotransferase, which is a membrane-associated but not multi-pass TM enzyme with catalytic His/Asp residues for phosphotransfer; and (C) Mg(2+) transporters such as CorA (4 TM + large cytoplasmic domain) or MgtE (5 TM + CBS domains), whose topologies are fundamentally different from the 11-TM pattern seen here. Among the remaining transporter options, the equilibrative (passive, no ATP/proton coupling) format 'substrate(in) = substrate(out)' matches the ENT family mechanism. Within ENT transporters, purine nucleosides like inosine are canonical substrates. The sequence also contains a region (~residues 138-172) consistent with TM4, which in ENT family members forms part of the nucleoside-binding pocket. This is a family-level topological and mechanistic inference transferable from well-characterized ENT homologs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass TM topology (~11 helices), signal peptide, and equilibrative transport format are directly readable from the sequence and match the ENT family. Distinguishing ENT from Mg transporters (CorA/MgtE) and from soluble enzymes (ADH, lipid A phosphotransferase) is achievable through standard family-level topology knowledge without needing the specific UniProt annotation of this exact protein."
  },
  "case_id": "catalytic_activity_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP4 (NT2_CRIFA, Crithidia fasciculata) explicitly annotates 'inosine(in) = inosine(out)' as a catalytic/transporter activity with direct experimental evidence (ECO:0000269, PubMed:15694482 and PubMed:20037157). The protein is named 'Nucleoside transporter 2' / 'Equilibrative nucleoside transporter 2.' The sequence in the question matches the canonical entry exactly (502 aa, SHA256 confirmed). The evidence is experimental, not merely computational inference."
  },
  "important_caveats": [
    "The UniProt entry also lists 'guanosine(in) = guanosine(out)' as a catalytic activity, but guanosine transport is not among the offered choices, so this does not create ambiguity within the given options.",
    "The protein is from Crithidia fasciculata (a trypanosomatid), an organism not explicitly stated in the question; however, the ENT family topology is conserved across eukaryotes and the reasoning does not depend on knowing the organism.",
    "The sequence was annotated in 2025 (Swiss-Prot integration) based on 2005 and 2010 experimental papers; the evidence codes (ECO:0000269) indicate direct experimental assay evidence, not computational prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different protein classes (lipid A phosphotransferase, nucleoside transporter, Mg transporter, alcohol dehydrogenase) with distinct architectures and mechanisms. The sequence's 11-TM membrane topology and equilibrative format uniquely point to B. No other option is architecturally or mechanistically plausible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP4 (NT2_CRIFA, Crithidia fasciculata) explicitly annotates 'inosine(in) = inosine(out)' as a catalytic/transporter activity with direct experimental evidence (ECO:0000269, PubMed:15694482 and PubMed:20037157). The protein is named 'Nucleoside transporter 2' / 'Equilibrative nucleoside transporter 2.' The sequence in the question matches the canonical entry exactly (502 aa, SHA256 confirmed). The evidence is experimental, not merely computational inference.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 502-aa sequence exhibits a highly hydrophobic, multi-pass transmembrane architecture with approximately 11 transmembrane helical segments and an N-terminal signal peptide, which is the hallmark topology of the equilibrative nucleoside transporter (ENT/SLC29) family. This architecture immediately eliminates: (D) alcohol dehydrogenase, which is a ~350-aa soluble enzyme with a Rossmann-fold NAD-binding domain (GxGxG motif) and no TM segments; (A) lipid A phosphotransferase, which is a membrane-associated but not multi-pass TM enzyme with catalytic His/Asp residues for phosphotransfer; and (C) Mg(2+) transporters such as CorA (4 TM + large cytoplasmic domain) or MgtE (5 TM + CBS domains), whose topologies are fundamentally different from the 11-TM pattern seen here. Among the remaining transporter options, the equilibrative (passive, no ATP/proton coupling) format 'substrate(in) = substrate(out)' matches the ENT family mechanism. Within ENT transporters, purine nucleosides like inosine are canonical substrates. The sequence also contains a region (~residues 138-172) consistent with TM4, which in ENT family members forms part of the nucleoside-binding pocket. This is a family-level topological and mechanistic inference transferable from well-characterized ENT homologs.",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass TM topology (~11 helices), signal peptide, and equilibrative transport format are directly readable from the sequence and match the ENT family. Distinguishing ENT from Mg transporters (CorA/MgtE) and from soluble enzymes (ADH, lipid A phosphotransferase) is achievable through standard family-level topology knowledge without needing the specific UniProt annotation of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different protein classes (lipid A phosphotransferase, nucleoside transporter, Mg transporter, alcohol dehydrogenase) with distinct architectures and mechanisms. The sequence's 11-TM membrane topology and equilibrative format uniquely point to B. No other option is architecturally or mechanistically plausible for this sequence."
  },
  "important_caveats": [
    "The UniProt entry also lists 'guanosine(in) = guanosine(out)' as a catalytic activity, but guanosine transport is not among the offered choices, so this does not create ambiguity within the given options.",
    "The protein is from Crithidia fasciculata (a trypanosomatid), an organism not explicitly stated in the question; however, the ENT family topology is conserved across eukaryotes and the reasoning does not depend on knowing the organism.",
    "The sequence was annotated in 2025 (Swiss-Prot integration) based on 2005 and 2010 experimental papers; the evidence codes (ECO:0000269) indicate direct experimental assay evidence, not computational prediction."
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
  "benchmark_sequence_length": 502,
  "benchmark_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "current_entry_audit": {
    "entryVersion": 55,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2001-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 502,
  "current_source_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9GTP4",
  "selected_historical_entry_version": 55,
  "selected_historical_record_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "selected_historical_source_sequence_length": 502,
  "selected_historical_source_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "selected_historical_version": {
    "accession": "Q9GTP4",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NT2_CRIFA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9GTP4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":55,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2001-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAG22611.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Crithidia\"],\"scientificName\":\"Crithidia fasciculata\",\"taxonId\":5656}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"value\":\"Equilibrative nucleoside transporter 2\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"value\":\"CfNT2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"name\":\"inosine(in) = inosine(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75375\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17596\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"name\":\"guanosine(in) = guanosine(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75371\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16750\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu W.\",\"Arendt C.S.\",\"Gessford S.K.\",\"Ntaba D.\",\"Carter N.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15694482\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2004.11.018\"}],\"citationType\":\"journal article\",\"firstPage\":\"1\",\"id\":\"15694482\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"12\",\"publicationDate\":\"2005\",\"title\":\"Identification and characterization of purine nucleoside transporters from Crithidia fasciculata.\",\"volume\":\"140\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Arendt C.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20037157\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.074351\"}],\"citationType\":\"journal article\",\"firstPage\":\"6024\",\"id\":\"20037157\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"6035\",\"publicationDate\":\"2010\",\"title\":\"Role of transmembrane domain 4 in ligand permeation by Crithidia fasciculata equilibrative nucleoside transporter 2 (CfNT2).\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBCELLULAR LOCATION\",\"MUTAGENESIS OF VAL-89; HIS-138; GLY-139; ALA-140; ILE-141; ALA-142; VAL-143; ILE-144; MET-145; VAL-146; VAL-147; ALA-148; VAL-150; GLY-151; GLY-152; PHE-153; SER-154; LYS-155; ALA-156; LEU-157; ASP-159; SER-160; THR-162; ASN-163; ALA-164; LEU-165; VAL-166; GLY-167; PRO-168; PHE-169; PRO-170; THR-171 AND LYS-172\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H1",
  "excerpt": "ID   NT2_CRIFA               Reviewed;         502 AA.\nAC   Q9GTP4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2001, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=Nucleoside transporter 2 {ECO:0000303|PubMed:15694482};\nDE            Short=CfNT2 {ECO:0000303|PubMed:15694482, ECO:0000303|PubMed:20037157};\nDE   AltName: Full=Equilibrative nucleoside transporter 2 {ECO:0000303|PubMed:20037157};\nOS   Crithidia fasciculata.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Crithidia.\nOX   NCBI_TaxID=5656 {ECO:0000312|EMBL:AAG22611.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Nucleoside transporter 2 {ECO:0000303|PubMed:15694482};\nDE            Short=CfNT2 {ECO:0000303|PubMed:15694482, ECO:0000303|PubMed:20037157};\nDE   AltName: Full=Equilibrative nucleoside transporter 2 {ECO:0000303|PubMed:20037157};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   INDUCTION.\nRX   PubMed=15694482; DOI=10.1016/j.molbiopara.2004.11.018;\nRA   Liu W., Arendt C.S., Gessford S.K., Ntaba D., Carter N.S., Ullman B.;\nRT   \"Identification and characterization of purine nucleoside transporters from\nRT   Crithidia fasciculata.\";\nRL   Mol. Biochem. Parasitol. 140:1-12(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H4",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, SUBCELLULAR LOCATION, AND MUTAGENESIS OF\nRP   VAL-89; HIS-138; GLY-139; ALA-140; ILE-141; ALA-142; VAL-143; ILE-144;\nRP   MET-145; VAL-146; VAL-147; ALA-148; VAL-150; GLY-151; GLY-152; PHE-153;\nRP   SER-154; LYS-155; ALA-156; LEU-157; ASP-159; SER-160; THR-162; ASN-163;\nRP   ALA-164; LEU-165; VAL-166; GLY-167; PRO-168; PHE-169; PRO-170; THR-171 AND\nRP   LYS-172.\nRX   PubMed=20037157; DOI=10.1074/jbc.m109.074351;\nRA   Arendt C.S., Ullman B.;\nRT   \"Role of transmembrane domain 4 in ligand permeation by Crithidia\nRT   fasciculata equilibrative nucleoside transporter 2 (CfNT2).\";\nRL   J. Biol. Chem. 285:6024-6035(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=inosine(in) = inosine(out); Xref=Rhea:RHEA:75375,\nCC         ChEBI:CHEBI:17596; Evidence={ECO:0000269|PubMed:15694482,\nCC         ECO:0000269|PubMed:20037157};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=guanosine(in) = guanosine(out); Xref=Rhea:RHEA:75371,\nCC         ChEBI:CHEBI:16750; Evidence={ECO:0000269|PubMed:15694482};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 144. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
