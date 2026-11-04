# GO_biological_process_0079

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0079.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **A** — defense response to virus

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVKVDLESKRYGEKLKEVFLMLDNNVVECIKEITESSRNGKLVFFVGAGVSTLSDYPQWWRLVDKYHEELYGSPKKGNYSSDEYLRIPQIFYNVKGEMAFDGILKDFFQVDKPTNPIHDKILAMNPAHVITTNYDNLIDTACWKRGKYFSVISAEEDVANATSSRYLLKVHGDFRKGFKGENVVLKEDDYLNYDQNYPLISNLMKTIIATHTIVFIGYGLGDYNINMLLNWVRKLQKDSFHKPFFIRTDPSPIENETLIYYENKGLRIIDAASLIDSNEYDYLERYSAVMDLLIESQENKFITKDDEVIDYIYGKISPLFALQYIRKIDLKHVFEYDYHFEVNGTVVRHKNKGFGYMERFFELKESCDERSKLSKKQYERFNALFNFFEKNGVICMAKDAGTLNTSIEINSLAYHGKYDVMKKFIEEQSVSIEDDYKKAFFLACLGRWEESYDLYSNIILNSIDESNGCVYYLSQINRYRIYQSITQAVTQFNGLGLLTFGRHYKPFTDEFLARIEREMTNFNIDDLFNGMPFEFQKKYKILEFLSDNQFLYDDTVKLFELTNKVRSEMSEGSYSFGMSSDIVVLLRLYDNLRFLYENCLWSVSFHEFHQYIRNSMSLLIEKAEYERTRDIDELGFSFFGKKSGFFMEYYDFVNISRHFKIDDIKNLERSCSIDKIRFGEQEKIEEYLVGIAEEITKQFSANGMNVVFYTQFISEAKAALYFAKYVKLSEEGLGKIVKALLFYFPERDLDIGKRYVWLERLTKCNELPKSIISIIDDFLVLQAEKHIDQNYSEVSSNGLYSRDYGALIKHFEKNFISKRLSEITLCLTQDKQKQIDFLFKLLPLLSTNAKSHLLSFKSVENINDLMNGIRIGLIDEFTPEHEELIIEYLETRKVNYIVEKEKGIQTFSSNDYMSTFGIWYFLEEINNSKMEEFIGMDDQYDFFVDPENFDYKKFIPSWLKNYNDKLLGKIAGNKHMKHHVIEVLKERVKNSNDKRYLEILMNYFI

[Multiple Choices]
A. defense response to virus
B. glycolytic process
C. vesicle fusion to plasma membrane
D. peripheral nervous system myelin maintenance
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The matched historical record describes this protein as an anti-phage defense protein whose activation causes NAD+ depletion and abortive infection, supporting defense response to virus; phages are viruses. The record's GO assignment itself is IEA, so it is computational annotation, while the functional description cites experimental evidence.

Citations as saved: [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, soluble sequence is consistent with a bacterial NAD+-processing enzyme, and its conserved catalytic features can support recognition of a sirtuin-like NADase family. Transferable knowledge that bacterial defense-associated sirtuin/NADase proteins can trigger abortive phage infection favors A over glycolysis; the nervous-system and vesicle-fusion alternatives are also poor fits for this sequence context.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the known connection between bacterial defense NADases and anti-phage responses provide a meaningful basis for selecting A without needing the exact protein's recorded annotation. This remains a probabilistic inference from sequence and related proteins, not proof of the specific protein's experimental role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the defense response best fits the sequence-family inference; the other options describe unrelated processes.


### Important caveats

- The exact protein identity and reviewer-only source annotations were not original inputs and are not used as the basis for the transferability judgment.
- The GO assignment cited in the source is IEA; the source's functional description separately cites experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, soluble sequence is consistent with a bacterial NAD+-processing enzyme, and its conserved catalytic features can support recognition of a sirtuin-like NADase family. Transferable knowledge that bacterial defense-associated sirtuin/NADase proteins can trigger abortive phage infection favors A over glycolysis; the nervous-system and vesicle-fusion alternatives are also poor fits for this sequence context.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known connection between bacterial defense NADases and anti-phage responses provide a meaningful basis for selecting A without needing the exact protein's recorded annotation. This remains a probabilistic inference from sequence and related proteins, not proof of the specific protein's experimental role."
  },
  "case_id": "GO_biological_process_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The matched historical record describes this protein as an anti-phage defense protein whose activation causes NAD+ depletion and abortive infection, supporting defense response to virus; phages are viruses. The record's GO assignment itself is IEA, so it is computational annotation, while the functional description cites experimental evidence."
  },
  "important_caveats": [
    "The exact protein identity and reviewer-only source annotations were not original inputs and are not used as the basis for the transferability judgment.",
    "The GO assignment cited in the source is IEA; the source's functional description separately cites experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the defense response best fits the sequence-family inference; the other options describe unrelated processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched historical record describes this protein as an anti-phage defense protein whose activation causes NAD+ depletion and abortive infection, supporting defense response to virus; phages are viruses. The record's GO assignment itself is IEA, so it is computational annotation, while the functional description cites experimental evidence.",
    "evidence_ids": ["H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, soluble sequence is consistent with a bacterial NAD+-processing enzyme, and its conserved catalytic features can support recognition of a sirtuin-like NADase family. Transferable knowledge that bacterial defense-associated sirtuin/NADase proteins can trigger abortive phage infection favors A over glycolysis; the nervous-system and vesicle-fusion alternatives are also poor fits for this sequence context.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known connection between bacterial defense NADases and anti-phage responses provide a meaningful basis for selecting A without needing the exact protein's recorded annotation. This remains a probabilistic inference from sequence and related proteins, not proof of the specific protein's experimental role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the defense response best fits the sequence-family inference; the other options describe unrelated processes."
  },
  "important_caveats": [
    "The exact protein identity and reviewer-only source annotations were not original inputs and are not used as the basis for the transferability judgment.",
    "The GO assignment cited in the source is IEA; the source's functional description separately cites experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (P0DXN8) annotates this protein as 'Defense-associated sirtuin 2' (DSR2) with EC 3.2.2.5. Its experimentally characterized function (supported by 6 independent PubMed publications with ECO:0000269 evidence codes) is: 'Anti-phage defense protein that is activated through the binding to the phage tail tube protein monomer and which hydrolyzes NAD+ upon activation (NADase activity). The resulting depletion of NAD(+) leads to an abortive infection.' The GO annotation GO:0051607 'defense response to virus' is assigned (IEA:UniProtKB-KW), and the GO definition ('Reactions triggered in response to the presence of a virus that act to protect the cell or organism') applies since phages are viruses. Multiple cryo-EM structures (PDB 8WYA, 8Y13, 8K98, 8WKS, 8YKF, etc.) confirm the mechanism.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [H8](#evidence-h8), [H9](#evidence-h9), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable sirtuin (SIR2) domain motif (GAGVSTLSD near position 60), indicating an NAD+-dependent enzyme. The protein is ~1005 aa from a bacterium (no eukaryotic signal peptides, no SNARE motifs, no transmembrane segments typical of eukaryotic vesicle machinery). This immediately eliminates C (vesicle fusion to plasma membrane) and D (peripheral nervous system myelin maintenance) as they are exclusively eukaryotic/vertebrate processes incompatible with a bacterial protein. Among the remaining options A and B: bacterial SIR2-domain proteins are a well-established class of anti-phage defense systems (e.g., SIR2-containing abortive infection systems, Threona, and numerous other SIR2-based defense systems characterized from ~2019 onward), functioning through NAD+ depletion upon phage infection. Glycolytic enzymes (GAPDH ~350 aa, PK ~500 aa, PGK ~250 aa) are typically 250-500 aa and do not contain sirtuin domains. A 1005-aa bacterial protein with a SIR2 domain fits the defense-system paradigm, not glycolysis. The family-level inference from other bacterial SIR2 defense proteins meaningfully distinguishes A from B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sirtuin domain motif is identifiable from the sequence, the bacterial context eliminates eukaryotic-specific processes (C, D), and the well-established paradigm that large bacterial SIR2-domain proteins function as anti-phage defense systems (learned from multiple related protein families) distinguishes A from B. This is legitimate transferable knowledge from the SIR2-defense-system literature.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly eukaryotic-specific processes incompatible with a bacterial protein. Option B (glycolytic process) involves well-characterized small enzymes without sirtuin domains. Option A is the only choice consistent with a large bacterial SIR2-domain protein given the established defense-system paradigm.


### Important caveats

- The GO term 'defense response to virus' (GO:0051607) is annotated with evidence code IEA (inferred from electronic annotation via keyword), not direct experimental GO assignment. However, the underlying function is supported by extensive experimental evidence (ECO:0000269 from 6 publications).
- The sirtuin domain recognition relies on the GAG motif and overall domain architecture; a model unfamiliar with the bacterial SIR2-defense paradigm might not confidently choose A over B, though the size argument and family knowledge strongly favor A.
- The entry was first publicly released in February 2025; if the benchmark was constructed before that date, the annotation may have been derived from the 2022 Garb et al. paper rather than the UniProt entry itself.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable sirtuin (SIR2) domain motif (GAGVSTLSD near position 60), indicating an NAD+-dependent enzyme. The protein is ~1005 aa from a bacterium (no eukaryotic signal peptides, no SNARE motifs, no transmembrane segments typical of eukaryotic vesicle machinery). This immediately eliminates C (vesicle fusion to plasma membrane) and D (peripheral nervous system myelin maintenance) as they are exclusively eukaryotic/vertebrate processes incompatible with a bacterial protein. Among the remaining options A and B: bacterial SIR2-domain proteins are a well-established class of anti-phage defense systems (e.g., SIR2-containing abortive infection systems, Threona, and numerous other SIR2-based defense systems characterized from ~2019 onward), functioning through NAD+ depletion upon phage infection. Glycolytic enzymes (GAPDH ~350 aa, PK ~500 aa, PGK ~250 aa) are typically 250-500 aa and do not contain sirtuin domains. A 1005-aa bacterial protein with a SIR2 domain fits the defense-system paradigm, not glycolysis. The family-level inference from other bacterial SIR2 defense proteins meaningfully distinguishes A from B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sirtuin domain motif is identifiable from the sequence, the bacterial context eliminates eukaryotic-specific processes (C, D), and the well-established paradigm that large bacterial SIR2-domain proteins function as anti-phage defense systems (learned from multiple related protein families) distinguishes A from B. This is legitimate transferable knowledge from the SIR2-defense-system literature."
  },
  "case_id": "GO_biological_process_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "H8",
      "H9",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (P0DXN8) annotates this protein as 'Defense-associated sirtuin 2' (DSR2) with EC 3.2.2.5. Its experimentally characterized function (supported by 6 independent PubMed publications with ECO:0000269 evidence codes) is: 'Anti-phage defense protein that is activated through the binding to the phage tail tube protein monomer and which hydrolyzes NAD+ upon activation (NADase activity). The resulting depletion of NAD(+) leads to an abortive infection.' The GO annotation GO:0051607 'defense response to virus' is assigned (IEA:UniProtKB-KW), and the GO definition ('Reactions triggered in response to the presence of a virus that act to protect the cell or organism') applies since phages are viruses. Multiple cryo-EM structures (PDB 8WYA, 8Y13, 8K98, 8WKS, 8YKF, etc.) confirm the mechanism."
  },
  "important_caveats": [
    "The GO term 'defense response to virus' (GO:0051607) is annotated with evidence code IEA (inferred from electronic annotation via keyword), not direct experimental GO assignment. However, the underlying function is supported by extensive experimental evidence (ECO:0000269 from 6 publications).",
    "The sirtuin domain recognition relies on the GAG motif and overall domain architecture; a model unfamiliar with the bacterial SIR2-defense paradigm might not confidently choose A over B, though the size argument and family knowledge strongly favor A.",
    "The entry was first publicly released in February 2025; if the benchmark was constructed before that date, the annotation may have been derived from the 2022 Garb et al. paper rather than the UniProt entry itself."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eukaryotic-specific processes incompatible with a bacterial protein. Option B (glycolytic process) involves well-characterized small enzymes without sirtuin domains. Option A is the only choice consistent with a large bacterial SIR2-domain protein given the established defense-system paradigm."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (P0DXN8) annotates this protein as 'Defense-associated sirtuin 2' (DSR2) with EC 3.2.2.5. Its experimentally characterized function (supported by 6 independent PubMed publications with ECO:0000269 evidence codes) is: 'Anti-phage defense protein that is activated through the binding to the phage tail tube protein monomer and which hydrolyzes NAD+ upon activation (NADase activity). The resulting depletion of NAD(+) leads to an abortive infection.' The GO annotation GO:0051607 'defense response to virus' is assigned (IEA:UniProtKB-KW), and the GO definition ('Reactions triggered in response to the presence of a virus that act to protect the cell or organism') applies since phages are viruses. Multiple cryo-EM structures (PDB 8WYA, 8Y13, 8K98, 8WKS, 8YKF, etc.) confirm the mechanism.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "H8", "H9", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable sirtuin (SIR2) domain motif (GAGVSTLSD near position 60), indicating an NAD+-dependent enzyme. The protein is ~1005 aa from a bacterium (no eukaryotic signal peptides, no SNARE motifs, no transmembrane segments typical of eukaryotic vesicle machinery). This immediately eliminates C (vesicle fusion to plasma membrane) and D (peripheral nervous system myelin maintenance) as they are exclusively eukaryotic/vertebrate processes incompatible with a bacterial protein. Among the remaining options A and B: bacterial SIR2-domain proteins are a well-established class of anti-phage defense systems (e.g., SIR2-containing abortive infection systems, Threona, and numerous other SIR2-based defense systems characterized from ~2019 onward), functioning through NAD+ depletion upon phage infection. Glycolytic enzymes (GAPDH ~350 aa, PK ~500 aa, PGK ~250 aa) are typically 250-500 aa and do not contain sirtuin domains. A 1005-aa bacterial protein with a SIR2 domain fits the defense-system paradigm, not glycolysis. The family-level inference from other bacterial SIR2 defense proteins meaningfully distinguishes A from B.",
    "missing_item_specific_fact": "",
    "reason": "The sirtuin domain motif is identifiable from the sequence, the bacterial context eliminates eukaryotic-specific processes (C, D), and the well-established paradigm that large bacterial SIR2-domain proteins function as anti-phage defense systems (learned from multiple related protein families) distinguishes A from B. This is legitimate transferable knowledge from the SIR2-defense-system literature."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eukaryotic-specific processes incompatible with a bacterial protein. Option B (glycolytic process) involves well-characterized small enzymes without sirtuin domains. Option A is the only choice consistent with a large bacterial SIR2-domain protein given the established defense-system paradigm."
  },
  "important_caveats": [
    "The GO term 'defense response to virus' (GO:0051607) is annotated with evidence code IEA (inferred from electronic annotation via keyword), not direct experimental GO assignment. However, the underlying function is supported by extensive experimental evidence (ECO:0000269 from 6 publications).",
    "The sirtuin domain recognition relies on the GAG motif and overall domain architecture; a model unfamiliar with the bacterial SIR2-defense paradigm might not confidently choose A over B, though the size argument and family knowledge strongly favor A.",
    "The entry was first publicly released in February 2025; if the benchmark was constructed before that date, the annotation may have been derived from the 2022 Garb et al. paper rather than the UniProt entry itself."
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
  "benchmark_sequence_length": 1005,
  "benchmark_sequence_sha256": "a332c6e633f60b28e85281a737e0528d5b23210a87c285627c304ff5d2412161",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1005,
  "current_source_sequence_sha256": "a332c6e633f60b28e85281a737e0528d5b23210a87c285627c304ff5d2412161",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXN8",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "selected_historical_source_sequence_length": 1005,
  "selected_historical_source_sequence_sha256": "a332c6e633f60b28e85281a737e0528d5b23210a87c285627c304ff5d2412161",
  "selected_historical_version": {
    "accession": "P0DXN8",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DSR2_BACIU",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXN8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\"],\"scientificName\":\"Bacillus subtilis\",\"taxonId\":1423}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36192536\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38538592\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38555355\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38729958\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39039073\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39059542\",\"source\":\"PubMed\"}],\"value\":\"3.2.2.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36192536\",\"source\":\"PubMed\"}],\"value\":\"Defense-associated sirtuin 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36192536\",\"source\":\"PubMed\"}],\"value\":\"DSR2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36192536\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38538592\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38555355\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38729958\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39039073\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39059542\",\"source\":\"PubMed\"}],\"value\":\"Anti-phage defense protein that is activated through the binding to the phage tail tube protein monomer and which hydrolyzes NAD+ upon activation (NADase activity) (PubMed:36192536, PubMed:38538592, PubMed:38555355, PubMed:38729958, PubMed:39039073, PubMed:39059542). The resulting depletion of NAD(+) leads to an abortive infection (PubMed:36192536)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Garb J.\",\"Lopatina A.\",\"Bernheim A.\",\"Zaremba M.\",\"Siksnys V.\",\"Melamed S.\",\"Leavitt A.\",\"Millman A.\",\"Amitai G.\",\"Sorek R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36192536\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41564-022-01207-8\"}],\"citationType\":\"journal article\",\"firstPage\":\"1849\",\"id\":\"36192536\",\"journal\":\"Nat. Microbiol.\",\"lastPage\":\"1856\",\"publicationDate\":\"2022\",\"title\":\"Multiple phage resistance systems inhibit infection via SIR2-dependent NAD+ depletion.\",\"volume\":\"7\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R7-12 / 29R\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DOMAIN\",\"MUTAGENESIS OF ASN-133 AND HIS-171\",\"INTERACTION WITH PHAGE SPR TAIL TUBE PROTEIN (MICROBIAL INFECTION)\",\"ACTIVITY REGULATION (MICROBIAL INFECTION)\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang R.\",\"Xu Q.\",\"Wu Z.\",\"Li J.\",\"Guo H.\",\"Liao T.\",\"Shi Y.\",\"Yuan L.\",\"Gao H.\",\"Yang R.\",\"Shi Z.\",\"Li F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39039073\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-50410-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"6185\",\"id\":\"39039073\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"6185\",\"publicationDate\":\"2024\",\"title\":\"The structural basis of the activation and inhibition of DSR2 NADase by phage proteins.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y13\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y34\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y3M\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y3W\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y3Y\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZC9\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R7-12 / 29R\"}],\"referenceNumber\":3,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.11 ANGSTROMS) OF MUTANT HIS-171\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.14 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN AND NAD\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.25 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1\",\"FUNCTION\",\"SUBUNIT\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"MUTAGENESIS OF TYR-260\",\"NAD-BINDING\",\"INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION)\",\"INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION)\",\"ACTIVE SITE\",\"MUTAGENESIS OF TYR-134; ASP-135 AND HIS-171\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang J.T.\",\"Liu X.Y.\",\"Li Z.\",\"Wei X.Y.\",\"Song X.Y.\",\"Cui N.\",\"Zhong J.\",\"Li H.\",\"Jia N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38555355\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-47177-9\"}],\"citationType\":\"journal article\",\"firstPage\":\"2797\",\"id\":\"38555355\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2797\",\"publicationDate\":\"2024\",\"title\":\"Structural basis for phage-mediated activation and repression of bacterial DSR2 anti-phage defense system.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYA\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYB\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYC\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYD\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYF\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R7-12 / 29R\"}],\"referenceNumber\":4,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.37 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN AND NAD\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.62 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN\",\"STRUCTURE BY ELECTRON MICROSCOPY (2.56 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1\",\"STRUCTURE BY ELECTRON MICROSCOPY (2.85 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1 AND NAD\",\"INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION)\",\"DOMAIN\",\"SUBUNIT\",\"MUTAGENESIS OF TRP-59; TYR-71; ASN-133; ASP-135; ASP-188 AND TYR-282\",\"INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION)\",\"ACTIVITY REGULATION (MICROBIAL INFECTION)\",\"CATALYTIC ACTIVITY\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Huang J.\",\"Zhu K.\",\"Gao Y.\",\"Ye F.\",\"Li Z.\",\"Ge Y.\",\"Liu S.\",\"Yang J.\",\"Gao A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38729958\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-48291-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"3954\",\"id\":\"38729958\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"3954\",\"publicationDate\":\"2024\",\"title\":\"Molecular basis of bacterial DSR2 anti-phage defense and viral immune evasion.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WKS\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WKT\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WKX\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R7-12 / 29R\"}],\"referenceNumber\":5,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (4.15 ANGSTROMS)\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.58 ANGSTROMS) OF 2-1005 IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.86 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1\",\"MUTAGENESIS OF 259-ILE-TYR-260\",\"INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION)\",\"ACTIVITY REGULATION (MICROBIAL INFECTION)\",\"CATALYTIC ACTIVITY\",\"INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION)\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin H.\",\"Li X.\",\"Wang X.\",\"Zhang C.\",\"Gao J.\",\"Yu G.\",\"He Q.\",\"Yang J.\",\"Liu X.\",\"Wei Y.\",\"Li Z.\",\"Zhang H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38538592\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-47030-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"2692\",\"id\":\"38538592\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2692\",\"publicationDate\":\"2024\",\"title\":\"Insights into the modulation of bacterial NADase activity by phage proteins.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8K98\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8K9A\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8W56\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WFN\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WKN\",\"source\":\"PDB\"}],\"referenceNumber\":6,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS)\",\"STRUCTURE BY ELECTRON MICROSCOPY (2.90 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1\",\"SUBUNIT\",\"DOMAIN\",\"INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION)\",\"ACTIVITY REGULATION (MICROBIAL INFECTION)\",\"CATALYTIC ACTIVITY\",\"INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION)\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.\",\"Wang Y.\",\"Zheng J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39059542\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijbiomac.2024.134145\"}],\"citationType\":\"journal article\",\"firstPage\":\"134145\",\"id\":\"39059542\",\"journal\":\"Int. J. Biol. Macromol.\",\"lastPage\":\"134145\",\"publicationDate\":\"2024\",\"title\":\"Structural insights into autoinhibition and activation of defense-associated sirtuin protein.\",\"volume\":\"277\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8YKF\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8YL5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8YLN\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8YLT\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Z18\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZTR\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R7-12 / 29R\"}],\"referenceNumber\":7,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.53 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.09 ANGSTROMS) IN COMPLEX WITH NAD\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.26 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN N-TERMINUS DOMAIN\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.35 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1\",\"FUNCTION\",\"ACTIVITY REGULATION\",\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION)\",\"INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION)\",\"ACTIVE SITE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DSR2_BACIU              Reviewed;        1005 AA.\nAC   P0DXN8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Defense-associated sirtuin 2 {ECO:0000303|PubMed:36192536};\nDE            Short=DSR2 {ECO:0000303|PubMed:36192536};\nDE            EC=3.2.2.5 {ECO:0000269|PubMed:36192536, ECO:0000269|PubMed:38538592, ECO:0000269|PubMed:38555355, ECO:0000269|PubMed:38729958, ECO:0000269|PubMed:39039073, ECO:0000269|PubMed:39059542};\nGN   ORFNames=BKP58_08510;\nOS   Bacillus subtilis.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus.\nOX   NCBI_TaxID=1423;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, DOMAIN, MUTAGENESIS OF ASN-133 AND HIS-171,\nRP   INTERACTION WITH PHAGE SPR TAIL TUBE PROTEIN (MICROBIAL INFECTION), AND\nRP   ACTIVITY REGULATION (MICROBIAL INFECTION).\nRC   STRAIN=29R7-12 / 29R;\nRX   PubMed=36192536; DOI=10.1038/s41564-022-01207-8;\nRA   Garb J., Lopatina A., Bernheim A., Zaremba M., Siksnys V., Melamed S.,\nRA   Leavitt A., Millman A., Amitai G., Sorek R.;\nRT   \"Multiple phage resistance systems inhibit infection via SIR2-dependent\nRT   NAD+ depletion.\";\nRL   Nat. Microbiol. 7:1849-1856(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 22-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:8Y13, ECO:0007744|PDB:8Y34, ECO:0007744|PDB:8Y3M, ECO:0007744|PDB:8Y3W, ECO:0007744|PDB:8Y3Y, ECO:0007744|PDB:8ZC9}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.11 ANGSTROMS) OF MUTANT HIS-171,\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.14 ANGSTROMS) IN COMPLEX WITH PHAGE SPR\nRP   TAIL TUBE PROTEIN AND NAD, STRUCTURE BY ELECTRON MICROSCOPY (3.25\nRP   ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1, FUNCTION, SUBUNIT, CATALYTIC\nRP   ACTIVITY, ACTIVITY REGULATION, MUTAGENESIS OF TYR-260, NAD-BINDING,\nRP   INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION), INTERACTION\nRP   WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION), ACTIVE SITE, AND MUTAGENESIS\nRP   OF TYR-134; ASP-135 AND HIS-171.\nRC   STRAIN=29R7-12 / 29R;\nRX   PubMed=39039073; DOI=10.1038/s41467-024-50410-0;\nRA   Wang R., Xu Q., Wu Z., Li J., Guo H., Liao T., Shi Y., Yuan L., Gao H.,\nRA   Yang R., Shi Z., Li F.;\nRT   \"The structural basis of the activation and inhibition of DSR2 NADase by\nRT   phage proteins.\";\nRL   Nat. Commun. 15:6185-6185(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:8WYA, ECO:0007744|PDB:8WYB, ECO:0007744|PDB:8WYC, ECO:0007744|PDB:8WYD, ECO:0007744|PDB:8WYE, ECO:0007744|PDB:8WYF}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.37 ANGSTROMS) IN COMPLEX WITH PHAGE SPR\nRP   TAIL TUBE PROTEIN AND NAD, STRUCTURE BY ELECTRON MICROSCOPY (3.62\nRP   ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN, STRUCTURE BY\nRP   ELECTRON MICROSCOPY (2.56 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1,\nRP   STRUCTURE BY ELECTRON MICROSCOPY (2.85 ANGSTROMS) IN COMPLEX WITH PHAGE\nRP   SPBETA DSAD1 AND NAD, INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL\nRP   INFECTION), DOMAIN, SUBUNIT, MUTAGENESIS OF TRP-59; TYR-71; ASN-133;\nRP   ASP-135; ASP-188 AND TYR-282, INTERACTION WITH PHAGE SPR TAIL TUBE\nRP   (MICROBIAL INFECTION), ACTIVITY REGULATION (MICROBIAL INFECTION), CATALYTIC\nRP   ACTIVITY, AND FUNCTION.\nRC   STRAIN=29R7-12 / 29R;\nRX   PubMed=38555355; DOI=10.1038/s41467-024-47177-9;\nRA   Zhang J.T., Liu X.Y., Li Z., Wei X.Y., Song X.Y., Cui N., Zhong J., Li H.,\nRA   Jia N.;\nRT   \"Structural basis for phage-mediated activation and repression of bacterial\nRT   DSR2 anti-phage defense system.\";\nRL   Nat. Commun. 15:2797-2797(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H5",
  "excerpt": "RN   [5] {ECO:0007744|PDB:8WKS, ECO:0007744|PDB:8WKT, ECO:0007744|PDB:8WKX}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (4.15 ANGSTROMS), STRUCTURE BY ELECTRON\nRP   MICROSCOPY (3.58 ANGSTROMS) OF 2-1005 IN COMPLEX WITH PHAGE SPR TAIL TUBE\nRP   PROTEIN, STRUCTURE BY ELECTRON MICROSCOPY (3.86 ANGSTROMS) IN COMPLEX WITH\nRP   PHAGE SPBETA DSAD1, MUTAGENESIS OF 259-ILE-TYR-260, INTERACTION WITH PHAGE\nRP   SPR TAIL TUBE (MICROBIAL INFECTION), ACTIVITY REGULATION (MICROBIAL\nRP   INFECTION), CATALYTIC ACTIVITY, INTERACTION WITH PHAGE SPBETA DSAD1\nRP   (MICROBIAL INFECTION), AND FUNCTION.\nRC   STRAIN=29R7-12 / 29R;\nRX   PubMed=38729958; DOI=10.1038/s41467-024-48291-4;\nRA   Huang J., Zhu K., Gao Y., Ye F., Li Z., Ge Y., Liu S., Yang J., Gao A.;\nRT   \"Molecular basis of bacterial DSR2 anti-phage defense and viral immune\nRT   evasion.\";\nRL   Nat. Commun. 15:3954-3954(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H6",
  "excerpt": "RN   [6] {ECO:0007744|PDB:8K98, ECO:0007744|PDB:8K9A, ECO:0007744|PDB:8W56, ECO:0007744|PDB:8WFN, ECO:0007744|PDB:8WKN}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS), STRUCTURE BY ELECTRON\nRP   MICROSCOPY (2.90 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN,\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS) IN COMPLEX WITH PHAGE\nRP   SPBETA DSAD1, SUBUNIT, DOMAIN, INTERACTION WITH PHAGE SPR TAIL TUBE\nRP   (MICROBIAL INFECTION), ACTIVITY REGULATION (MICROBIAL INFECTION), CATALYTIC\nRP   ACTIVITY, INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION), AND\nRP   FUNCTION.\nRX   PubMed=38538592; DOI=10.1038/s41467-024-47030-z;\nRA   Yin H., Li X., Wang X., Zhang C., Gao J., Yu G., He Q., Yang J., Liu X.,\nRA   Wei Y., Li Z., Zhang H.;\nRT   \"Insights into the modulation of bacterial NADase activity by phage\nRT   proteins.\";\nRL   Nat. Commun. 15:2692-2692(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H7",
  "excerpt": "RN   [7] {ECO:0007744|PDB:8YKF, ECO:0007744|PDB:8YL5, ECO:0007744|PDB:8YLN, ECO:0007744|PDB:8YLT, ECO:0007744|PDB:8Z18, ECO:0007744|PDB:8ZTR}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.53 ANGSTROMS) IN COMPLEX WITH PHAGE SPR\nRP   TAIL TUBE PROTEIN, STRUCTURE BY ELECTRON MICROSCOPY (3.09 ANGSTROMS) IN\nRP   COMPLEX WITH NAD, STRUCTURE BY ELECTRON MICROSCOPY (3.26 ANGSTROMS) IN\nRP   COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN N-TERMINUS DOMAIN, STRUCTURE BY\nRP   ELECTRON MICROSCOPY (3.35 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1,\nRP   FUNCTION, ACTIVITY REGULATION, CATALYTIC ACTIVITY, SUBUNIT, INTERACTION\nRP   WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION), INTERACTION WITH PHAGE\nRP   SPBETA DSAD1 (MICROBIAL INFECTION), AND ACTIVE SITE.\nRC   STRAIN=29R7-12 / 29R;\nRX   PubMed=39059542; DOI=10.1016/j.ijbiomac.2024.134145;\nRA   Yang X., Wang Y., Zheng J.;\nRT   \"Structural insights into autoinhibition and activation of defense-\nRT   associated sirtuin protein.\";\nRL   Int. J. Biol. Macromol. 277:134145-134145(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H8",
  "excerpt": "CC   -!- FUNCTION: Anti-phage defense protein that is activated through the\nCC       binding to the phage tail tube protein monomer and which hydrolyzes\nCC       NAD+ upon activation (NADase activity) (PubMed:36192536,\nCC       PubMed:38538592, PubMed:38555355, PubMed:38729958, PubMed:39039073,\nCC       PubMed:39059542). The resulting depletion of NAD(+) leads to an\nCC       abortive infection (PubMed:36192536). {ECO:0000269|PubMed:36192536,\nCC       ECO:0000269|PubMed:38538592, ECO:0000269|PubMed:38555355,\nCC       ECO:0000269|PubMed:38729958, ECO:0000269|PubMed:39039073,\nCC       ECO:0000269|PubMed:39059542}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0051607; P:defense response to virus; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 258-258",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006096\nname: glycolytic process\nnamespace: biological_process\nalt_id: GO:0019641\nalt_id: GO:0019642\ndef: \"The chemical reactions and pathways resulting in the breakdown of a carbohydrate into pyruvate, with the concomitant production of a small amount of ATP and the reduction of NAD(P) to NAD(P)H. Glycolysis begins with the metabolism of a carbohydrate to generate products that can enter the pathway and ends with the production of pyruvate. Pyruvate may be converted to acetyl-coenzyme A, ethanol, lactate, or other small molecules.\" [GOC:bf, GOC:dph, ISBN:0201090910, ISBN:0716720094, ISBN:0879010479, Wikipedia:Glycolysis]\nsynonym: \"anaerobic glycolysis\" RELATED []\nsynonym: \"Embden-Meyerhof pathway\" RELATED []\nsynonym: \"Embden-Meyerhof-Parnas pathway\" RELATED []\nsynonym: \"glycolysis\" RELATED [GOC:dph]\nsynonym: \"modified Embden-Meyerhof pathway\" RELATED []\nxref: MetaCyc:GLYCOLYSIS-VARIANTS\nxref: MetaCyc:P341-PWY\nis_a: GO:0006090 ! pyruvate metabolic process\nis_a: GO:0006091 ! generation of precursor metabolites and energy\nis_a: GO:0016052 ! carbohydrate catabolic process\nis_a: GO:0019364 ! pyridine nucleotide catabolic process\nis_a: GO:0046032 ! ADP catabolic process\nis_a: GO:0046034 ! ATP metabolic process\nis_a: GO:0046496 ! nicotinamide nucleotide metabolic process\nrelationship: part_of GO:0009060 ! aerobic respiration\nproperty_value: skos:exactMatch MetaCyc:GLYCOLYSIS-VARIANTS\nproperty_value: skos:narrowMatch MetaCyc:P341-PWY\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006096",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 62693-62717",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0032287\nname: peripheral nervous system myelin maintenance\nnamespace: biological_process\ndef: \"The process in which the structure and material content of mature peripheral nervous system myelin is kept in a functional state.\" [GOC:dgh]\nsynonym: \"myelin maintenance in peripheral nervous system\" EXACT []\nsynonym: \"peripheral nervous system myelin sheath maintenance\" EXACT []\nis_a: GO:0043217 ! myelin maintenance\nrelationship: part_of GO:0022011 ! myelination in peripheral nervous system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032287",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 184676-184685",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0051607\nname: defense response to virus\nnamespace: biological_process\ndef: \"Reactions triggered in response to the presence of a virus that act to protect the cell or organism.\" [GOC:ai]\nsynonym: \"antiviral response\" EXACT []\nsynonym: \"defence response to virus\" EXACT []\nsynonym: \"defense response to viruses\" EXACT []\nxref: Reactome:R-HSA-8983711 \"OAS antiviral response\"\nis_a: GO:0006952 ! defense response\nis_a: GO:0009615 ! response to virus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051607",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 328631-328642",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0099500\nname: vesicle fusion to plasma membrane\nnamespace: biological_process\ndef: \"Fusion of the membrane of a vesicle with the plasma membrane, thereby releasing its contents into the extracellular space.\" [GOC:aruk, GOC:bc, ISBN:0071120009, PMID:18618940]\nis_a: GO:0006906 ! vesicle fusion\nis_a: GO:0140029 ! exocytic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0099500",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 414643-414650",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 79. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
