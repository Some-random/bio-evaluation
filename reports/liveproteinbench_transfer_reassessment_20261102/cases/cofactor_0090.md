# cofactor_0090

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0090.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAVFPLSAKHRKYALRALAVSIILVSAAYIALTERTERVRPQRVEQNLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGGAREVQFFTDEDGERNLVALEKKGGIWRRSASEADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLIYDSLYFHGQQVAAGDILAAEVVKGGTRHQAFYYRSDKEGGGGGNYYDEDGRVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAQGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. tungstopterin
B. Na(+)
C. Co(2+)
D. Zn(2+)
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

> The sequence-matched UniProt record identifies Zn(2+) as the cofactor and reports experimental evidence that the protein binds one zinc ion per subunit, while qualifying that Zn(2+) is probable in vivo and Ni(2+) was observed in the crystal structure. This supports the key, though the in-vivo metal assignment is qualified.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a signal-peptide-like N-terminus and a clustered histidine-rich region consistent with a bacterial metallopeptidase active site. Transferable knowledge that peptidoglycan-cleaving metallopeptidases commonly use zinc makes Zn(2+) the meaningful choice among tungsten-pterin, sodium, cobalt, and zinc. This is a family-level inference, not proof of the exact native metal; cobalt can sometimes substitute for zinc in metalloproteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence offers a plausible metal-binding feature, and enzyme-family knowledge meaningfully favors zinc over the other listed choices. Exact-protein evidence would improve certainty but is not necessary to distinguish the choices credibly.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source qualifies the in-vivo assignment, but among the offered options it supports zinc; it does not make another listed option comparably defensible.


### Important caveats

- The evidence says Zn(2+) is probable in vivo; the crystal structure contained Ni(2+).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a signal-peptide-like N-terminus and a clustered histidine-rich region consistent with a bacterial metallopeptidase active site. Transferable knowledge that peptidoglycan-cleaving metallopeptidases commonly use zinc makes Zn(2+) the meaningful choice among tungsten-pterin, sodium, cobalt, and zinc. This is a family-level inference, not proof of the exact native metal; cobalt can sometimes substitute for zinc in metalloproteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a plausible metal-binding feature, and enzyme-family knowledge meaningfully favors zinc over the other listed choices. Exact-protein evidence would improve certainty but is not necessary to distinguish the choices credibly."
  },
  "case_id": "cofactor_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies Zn(2+) as the cofactor and reports experimental evidence that the protein binds one zinc ion per subunit, while qualifying that Zn(2+) is probable in vivo and Ni(2+) was observed in the crystal structure. This supports the key, though the in-vivo metal assignment is qualified."
  },
  "important_caveats": [
    "The evidence says Zn(2+) is probable in vivo; the crystal structure contained Ni(2+)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source qualifies the in-vivo assignment, but among the offered options it supports zinc; it does not make another listed option comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies Zn(2+) as the cofactor and reports experimental evidence that the protein binds one zinc ion per subunit, while qualifying that Zn(2+) is probable in vivo and Ni(2+) was observed in the crystal structure. This supports the key, though the in-vivo metal assignment is qualified.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a signal-peptide-like N-terminus and a clustered histidine-rich region consistent with a bacterial metallopeptidase active site. Transferable knowledge that peptidoglycan-cleaving metallopeptidases commonly use zinc makes Zn(2+) the meaningful choice among tungsten-pterin, sodium, cobalt, and zinc. This is a family-level inference, not proof of the exact native metal; cobalt can sometimes substitute for zinc in metalloproteins.",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a plausible metal-binding feature, and enzyme-family knowledge meaningfully favors zinc over the other listed choices. Exact-protein evidence would improve certainty but is not necessary to distinguish the choices credibly."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source qualifies the in-vivo assignment, but among the offered options it supports zinc; it does not make another listed option comparably defensible."
  },
  "important_caveats": [
    "The evidence says Zn(2+) is probable in vivo; the crystal structure contained Ni(2+)."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E0N688 annotates Zn(2+) as the cofactor with evidence code ECO:0000269 (direct assay, PubMed:22046377). The protein is named 'Zinc metallopeptidase'/'Zinc-dependent metallopeptidase' and assigned EC 3.4.17.- (DD-carboxypeptidase) and EC 3.4.24.- (metalloendopeptidase). The annotation note states 'Binds 1 zinc ion per subunit. Binds a divalent metal cation, probably Zn(2+) in vivo, Ni(2+) ion is found in the crystal structure.' The crystal structure (3SLU) used Ni(2+) as a substitute, but the biological cofactor is annotated as Zn(2+). The expected answer D (Zn(2+)) is directly supported by experimental evidence.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'GIDY' motif (visible in 'GIDYAAPQGT'), which is a well-known family-level signature of the M23 peptidase family (DD-carboxypeptidases). Members of the M23 family are zinc-dependent metalloproteases. Additionally, the C-terminal catalytic region shows clustering of histidine residues (e.g., 'RHPILHTWRLHTGIDY' with three His in close proximity, and 'GNAVMIRHANGVETLYAHLSAF' with H...H spacing) and a tyrosine in 'GIDY' — a pattern consistent with zinc coordination geometry (His/His/Tyr triad) seen across metalloprotease families. The N-terminal hydrophobic segment suggests a signal peptide/outer-membrane anchoring typical of bacterial surface peptidases. Among the four choices: tungstopterin (A) is a cofactor for anaerobic oxidoreductases in hyperthermophiles, Na(+) (B) is not a catalytic cofactor for peptidases, and Co(2+) (C) is a rare substitute metal. The combination of the GIDY motif, His clustering, bacterial peptidase context, and the general rule that metalloproteases predominantly use Zn(2+) provides a concrete, transferable inference favoring Zn(2+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing the GIDY motif as an M23-family signature, combined with the histidine-rich zinc-binding-like pattern and the general biological principle that bacterial DD-carboxypeptidases/metalloendopeptidases use Zn(2+), can meaningfully distinguish Zn(2+) from the other three options without needing the specific UniProt record for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices are well-separated: tungstopterin is for anaerobic oxidoreductases, Na(+) is not a peptidase cofactor, Co(2+) is a rare substitute not the biological metal, and Zn(2+) is the canonical metalloprotease cofactor. The UniProt note mentioning Ni(2+) in the crystal structure does not create ambiguity because Ni(2+) is not among the offered choices. No two options are equally defensible.


### Important caveats

- The crystal structure (3SLU) was solved with Ni(2+) as a substitute; the biological in vivo cofactor is annotated as Zn(2+). This distinction does not affect the answer since Ni(2+) is not an offered choice.
- The EC assignments (3.4.17.- and 3.4.24.-) are transferred by similarity from Q5F676 (ECO:0000250), not independently determined for this exact sequence, but the zinc cofactor annotation itself carries direct-assay evidence (ECO:0000269).
- The GIDY motif recognition as an M23-family signature is a family-level pattern; the specific protein (Mpg) has dual carboxypeptidase/endopeptidase activity, which is somewhat unusual for canonical M23 peptidases, but the zinc-dependence is retained.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'GIDY' motif (visible in 'GIDYAAPQGT'), which is a well-known family-level signature of the M23 peptidase family (DD-carboxypeptidases). Members of the M23 family are zinc-dependent metalloproteases. Additionally, the C-terminal catalytic region shows clustering of histidine residues (e.g., 'RHPILHTWRLHTGIDY' with three His in close proximity, and 'GNAVMIRHANGVETLYAHLSAF' with H...H spacing) and a tyrosine in 'GIDY' — a pattern consistent with zinc coordination geometry (His/His/Tyr triad) seen across metalloprotease families. The N-terminal hydrophobic segment suggests a signal peptide/outer-membrane anchoring typical of bacterial surface peptidases. Among the four choices: tungstopterin (A) is a cofactor for anaerobic oxidoreductases in hyperthermophiles, Na(+) (B) is not a catalytic cofactor for peptidases, and Co(2+) (C) is a rare substitute metal. The combination of the GIDY motif, His clustering, bacterial peptidase context, and the general rule that metalloproteases predominantly use Zn(2+) provides a concrete, transferable inference favoring Zn(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the GIDY motif as an M23-family signature, combined with the histidine-rich zinc-binding-like pattern and the general biological principle that bacterial DD-carboxypeptidases/metalloendopeptidases use Zn(2+), can meaningfully distinguish Zn(2+) from the other three options without needing the specific UniProt record for this exact protein."
  },
  "case_id": "cofactor_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E0N688 annotates Zn(2+) as the cofactor with evidence code ECO:0000269 (direct assay, PubMed:22046377). The protein is named 'Zinc metallopeptidase'/'Zinc-dependent metallopeptidase' and assigned EC 3.4.17.- (DD-carboxypeptidase) and EC 3.4.24.- (metalloendopeptidase). The annotation note states 'Binds 1 zinc ion per subunit. Binds a divalent metal cation, probably Zn(2+) in vivo, Ni(2+) ion is found in the crystal structure.' The crystal structure (3SLU) used Ni(2+) as a substitute, but the biological cofactor is annotated as Zn(2+). The expected answer D (Zn(2+)) is directly supported by experimental evidence."
  },
  "important_caveats": [
    "The crystal structure (3SLU) was solved with Ni(2+) as a substitute; the biological in vivo cofactor is annotated as Zn(2+). This distinction does not affect the answer since Ni(2+) is not an offered choice.",
    "The EC assignments (3.4.17.- and 3.4.24.-) are transferred by similarity from Q5F676 (ECO:0000250), not independently determined for this exact sequence, but the zinc cofactor annotation itself carries direct-assay evidence (ECO:0000269).",
    "The GIDY motif recognition as an M23-family signature is a family-level pattern; the specific protein (Mpg) has dual carboxypeptidase/endopeptidase activity, which is somewhat unusual for canonical M23 peptidases, but the zinc-dependence is retained."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated: tungstopterin is for anaerobic oxidoreductases, Na(+) is not a peptidase cofactor, Co(2+) is a rare substitute not the biological metal, and Zn(2+) is the canonical metalloprotease cofactor. The UniProt note mentioning Ni(2+) in the crystal structure does not create ambiguity because Ni(2+) is not among the offered choices. No two options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E0N688 annotates Zn(2+) as the cofactor with evidence code ECO:0000269 (direct assay, PubMed:22046377). The protein is named 'Zinc metallopeptidase'/'Zinc-dependent metallopeptidase' and assigned EC 3.4.17.- (DD-carboxypeptidase) and EC 3.4.24.- (metalloendopeptidase). The annotation note states 'Binds 1 zinc ion per subunit. Binds a divalent metal cation, probably Zn(2+) in vivo, Ni(2+) ion is found in the crystal structure.' The crystal structure (3SLU) used Ni(2+) as a substitute, but the biological cofactor is annotated as Zn(2+). The expected answer D (Zn(2+)) is directly supported by experimental evidence.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'GIDY' motif (visible in 'GIDYAAPQGT'), which is a well-known family-level signature of the M23 peptidase family (DD-carboxypeptidases). Members of the M23 family are zinc-dependent metalloproteases. Additionally, the C-terminal catalytic region shows clustering of histidine residues (e.g., 'RHPILHTWRLHTGIDY' with three His in close proximity, and 'GNAVMIRHANGVETLYAHLSAF' with H...H spacing) and a tyrosine in 'GIDY' — a pattern consistent with zinc coordination geometry (His/His/Tyr triad) seen across metalloprotease families. The N-terminal hydrophobic segment suggests a signal peptide/outer-membrane anchoring typical of bacterial surface peptidases. Among the four choices: tungstopterin (A) is a cofactor for anaerobic oxidoreductases in hyperthermophiles, Na(+) (B) is not a catalytic cofactor for peptidases, and Co(2+) (C) is a rare substitute metal. The combination of the GIDY motif, His clustering, bacterial peptidase context, and the general rule that metalloproteases predominantly use Zn(2+) provides a concrete, transferable inference favoring Zn(2+).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the GIDY motif as an M23-family signature, combined with the histidine-rich zinc-binding-like pattern and the general biological principle that bacterial DD-carboxypeptidases/metalloendopeptidases use Zn(2+), can meaningfully distinguish Zn(2+) from the other three options without needing the specific UniProt record for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated: tungstopterin is for anaerobic oxidoreductases, Na(+) is not a peptidase cofactor, Co(2+) is a rare substitute not the biological metal, and Zn(2+) is the canonical metalloprotease cofactor. The UniProt note mentioning Ni(2+) in the crystal structure does not create ambiguity because Ni(2+) is not among the offered choices. No two options are equally defensible."
  },
  "important_caveats": [
    "The crystal structure (3SLU) was solved with Ni(2+) as a substitute; the biological in vivo cofactor is annotated as Zn(2+). This distinction does not affect the answer since Ni(2+) is not an offered choice.",
    "The EC assignments (3.4.17.- and 3.4.24.-) are transferred by similarity from Q5F676 (ECO:0000250), not independently determined for this exact sequence, but the zinc cofactor annotation itself carries direct-assay evidence (ECO:0000269).",
    "The GIDY motif recognition as an M23-family signature is a family-level pattern; the specific protein (Mpg) has dual carboxypeptidase/endopeptidase activity, which is somewhat unusual for canonical M23 peptidases, but the zinc-dependence is retained."
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
  "benchmark_sequence_length": 430,
  "benchmark_sequence_sha256": "3e75444ef73a59ea32e1df8dd911f094a963233fecca96f1fb511d7b05e30d56",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 430,
  "current_source_sequence_sha256": "3e75444ef73a59ea32e1df8dd911f094a963233fecca96f1fb511d7b05e30d56",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E0N688",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "selected_historical_source_sequence_length": 430,
  "selected_historical_source_sequence_sha256": "3e75444ef73a59ea32e1df8dd911f094a963233fecca96f1fb511d7b05e30d56",
  "selected_historical_version": {
    "accession": "E0N688",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MPG_NEIM3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E0N688\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Neisseriales\",\"Neisseriaceae\",\"Neisseria\"],\"scientificName\":\"Neisseria meningitidis serogroup B (strain ATCC 13091 / M2091)\",\"taxonId\":862513}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"Metalloprotease active against peptidoglycan\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"Outer membrane protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"OMP\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc metallopeptidase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc metalloprotease\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"Zinc-dependent metallopeptidase\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.17.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"DD-carboxypeptidase/endopeptidase Mpg\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 zinc ion per subunit. Binds a divalent metal cation, probably Zn(2+) in vivo, Ni(2+) ion is found in the crystal structure.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang X.\",\"Yang X.\",\"Yang C.\",\"Wu Z.\",\"Xu H.\",\"Shen Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22046377\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0026845\"}],\"citationType\":\"journal article\",\"firstPage\":\"e26845\",\"id\":\"22046377\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e26845\",\"publicationDate\":\"2011\",\"title\":\"Crystal structure of outer membrane protein NMB0315 from Neisseria meningitidis.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3SLU\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 13091 / M2091\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.41 ANGSTROMS) OF 54-420 IN COMPLEX WITH NICKEL\",\"COFACTOR\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"PTM\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   MPG_NEIM3               Reviewed;         430 AA.\nAC   E0N688;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2010, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};\nDE            EC=3.4.17.- {ECO:0000250|UniProtKB:Q5F676};\nDE            EC=3.4.24.- {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Outer membrane protein {ECO:0000303|PubMed:22046377};\nDE            Short=OMP {ECO:0000303|PubMed:22046377};\nDE   AltName: Full=Zinc metallopeptidase {ECO:0000305};\nDE   AltName: Full=Zinc metalloprotease {ECO:0000305};\nDE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000303|PubMed:22046377};\nDE   Flags: Precursor;\nGN   ORFNames=HMPREF0602_0018 {ECO:0000312|EMBL:EFM05396.1};\nOS   Neisseria meningitidis serogroup B (strain ATCC 13091 / M2091).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;\nOC   Neisseriaceae; Neisseria.\nOX   NCBI_TaxID=862513;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};\nDE            EC=3.4.17.- {ECO:0000250|UniProtKB:Q5F676};\nDE            EC=3.4.24.- {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Outer membrane protein {ECO:0000303|PubMed:22046377};\nDE            Short=OMP {ECO:0000303|PubMed:22046377};\nDE   AltName: Full=Zinc metallopeptidase {ECO:0000305};\nDE   AltName: Full=Zinc metalloprotease {ECO:0000305};\nDE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000303|PubMed:22046377};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:3SLU}\nRP   X-RAY CRYSTALLOGRAPHY (2.41 ANGSTROMS) OF 54-420 IN COMPLEX WITH NICKEL,\nRP   COFACTOR, SUBUNIT, SUBCELLULAR LOCATION, AND PTM.\nRC   STRAIN=ATCC 13091 / M2091 {ECO:0000303|PubMed:22046377};\nRX   PubMed=22046377; DOI=10.1371/journal.pone.0026845;\nRA   Wang X., Yang X., Yang C., Wu Z., Xu H., Shen Y.;\nRT   \"Crystal structure of outer membrane protein NMB0315 from Neisseria\nRT   meningitidis.\";\nRL   PLoS ONE 6:e26845-e26845(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000269|PubMed:22046377};\nCC       Note=Binds 1 zinc ion per subunit. Binds a divalent metal cation,\nCC       probably Zn(2+) in vivo, Ni(2+) ion is found in the crystal structure.\nCC       {ECO:0000269|PubMed:22046377};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 90. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
