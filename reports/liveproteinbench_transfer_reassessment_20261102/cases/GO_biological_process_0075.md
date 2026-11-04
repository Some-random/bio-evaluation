# GO_biological_process_0075

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0075.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — plasma membrane organization

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGKTKIYSVGFTVHEAQTLVTEKGQPVDPLVVVRCCGREYRTEIKYAKSNVVSWDESHTWTDLCLTDEEWETAYITFEVQAANAFWRNTLLGLVSVQLRLIQLRKTHQIRKALPLQHPDDTDVHGSLRVTVFACAPGEAPPSPGEEEVLEEEDHNDYDDLRKAVIDTNQVVEREAGSRLYHVYVTAYRVEDLPRSSKGARDPFVTCEFAGCKLKSTQARGCCSHTFNECFRFPVVTPLPEDAILIKIWDWNFMKADELIAVGRISFSELRTRQMVPRWFNLYGFDDEEVAQATKVAGQGGRLVANCYLGRILLGARAERLTKEDDLMPAHTVAARPYETPPVIPLAVLADVYEVQGAPGEKVSVEIWCGPARARTKWVTGLETKAAQRAGVAPQAFNRAMEGALGVASYLRGDIPEGEDRFPFDNTEGRVEDLRLVVPEDTKQQWDIIISLYVRGTTKGFMGDTRIAFQRLKMSKIPGHVHNNPRAPIWVPLISTPPFESVKPAPAILMVIEKSKVEAFARSKRKHVTAVGYQLRAYVYAARNLLSPSGALPNPFVQVACAGTSRETEVFEQTSSPVFMDCLLLDITMMTDPVSRLPTVAPIVVTLFEQRSWGIQFLGRATCHYDRLRGRLKPGESPTVAEPRWIKLRGGKYANRHLGDVLLLLELIRKRDAEIIPAFPMRPVVNMCNLTFSCLGVRSLYMTQRAKRLDYVSIRKGQDKKTELRRIRGPLLRISVSSYASAGRGNNEAILRYERNLPEDPTTVNKLWTTVTKAANADIFKVVNMEIDVPVDPIYDPRLVVQVYDRKQKPKYFIGEYSMSLVPLIPWVLDQQSAIEAVSPVNDFTDTVDLKHLGGLLRGFHGNSKNRGTGQIGLEALSAADRETADAHKEKTLAQSRFATYDPDNKTFSDSWLLPSGLPKILVSSYAVPGFRCDVIYTNMFTLNVYIPAKFVLFAEGKRAADKKTKEQYARPSVDSTLEQFLDDVIFPSDSLKKSVMGDIDVTGFVKFFVNLTHHEEPNPHVDSSAAEWASSEDRMRRHLRGEDAYPKLLKIRVYVIRAISLYVGDDRILPNPYLLFNLGDKSDTLRAEAKPNTHNPEFFTVWEKDVMFPDDSQFELQVWSAHEGTSGGLDDIFIGSTCIDLEERWFSKEWQKSMSKNQVPMEYRPLKQMPSGSFKGTVEMWVELMDFQKAGEVPKFDLQSPAATEVEIRVIVWGARNLNFKALGKDFVDAMIRCNLDCTGYRGSQPIAQQTDVHYYSKTGAAIFNWRMVYSRVVMPVSTCVLQIAAYDNRNMGESPFIGEVNLELRRYLERVASTLNSIDVDAELKLINRSRESADVSSFGFVQVSLQFISQSEATSKPVGLGREPPNRDPRLTTPQEGRKWEDVLGSAGLRVDYRPLWYWVRVAAVVFLSIWIFVVAFLYPSLLG

[Multiple Choices]
A. microtubule cytoskeleton organization
B. plasma membrane organization
C. aflatoxin biosynthetic process
D. regulation of monoatomic ion transmembrane transport
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

> The exact-sequence-matched UniProt record annotates plasma membrane organization (B) by computational IEA:TreeGrafter. Separately, experimental evidence reports a role in regulating rhoptry secretion, which is consistent with membrane-trafficking activity but does not directly establish the exact GO term.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has the characteristic pattern of a ferlin-family membrane-trafficking protein: multiple C2-like domains and a C-terminal transmembrane segment. Transferable knowledge that ferlins are calcium-responsive regulators of membrane fusion and secretion supports a membrane-organization process (B) over microtubule organization, aflatoxin biosynthesis, or regulation of ion transport. This is a family-level inference, not proof of this protein's precise GO annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence features and transferable ferlin-family biology meaningfully distinguish B among these choices, although the exact organism-specific function and GO annotation are not supplied in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence's membrane-trafficking family features.


### Important caveats

- The exact plasma-membrane-organization annotation is computational; the cited experimental evidence concerns rhoptry secretion, not direct demonstration of the GO term.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence has the characteristic pattern of a ferlin-family membrane-trafficking protein: multiple C2-like domains and a C-terminal transmembrane segment. Transferable knowledge that ferlins are calcium-responsive regulators of membrane fusion and secretion supports a membrane-organization process (B) over microtubule organization, aflatoxin biosynthesis, or regulation of ion transport. This is a family-level inference, not proof of this protein's precise GO annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and transferable ferlin-family biology meaningfully distinguish B among these choices, although the exact organism-specific function and GO annotation are not supplied in the original input."
  },
  "case_id": "GO_biological_process_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record annotates plasma membrane organization (B) by computational IEA:TreeGrafter. Separately, experimental evidence reports a role in regulating rhoptry secretion, which is consistent with membrane-trafficking activity but does not directly establish the exact GO term."
  },
  "important_caveats": [
    "The exact plasma-membrane-organization annotation is computational; the cited experimental evidence concerns rhoptry secretion, not direct demonstration of the GO term."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence's membrane-trafficking family features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record annotates plasma membrane organization (B) by computational IEA:TreeGrafter. Separately, experimental evidence reports a role in regulating rhoptry secretion, which is consistent with membrane-trafficking activity but does not directly establish the exact GO term.",
    "evidence_ids": ["C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has the characteristic pattern of a ferlin-family membrane-trafficking protein: multiple C2-like domains and a C-terminal transmembrane segment. Transferable knowledge that ferlins are calcium-responsive regulators of membrane fusion and secretion supports a membrane-organization process (B) over microtubule organization, aflatoxin biosynthesis, or regulation of ion transport. This is a family-level inference, not proof of this protein's precise GO annotation.",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and transferable ferlin-family biology meaningfully distinguish B among these choices, although the exact organism-specific function and GO annotation are not supplied in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence's membrane-trafficking family features."
  },
  "important_caveats": [
    "The exact plasma-membrane-organization annotation is computational; the cited experimental evidence concerns rhoptry secretion, not direct demonstration of the GO term."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The GO annotation GO:0007009 'plasma membrane organization' is present in the UniProt entry (evidence C6/H5), though only as IEA:TreeGrafter (computational phylogenetic inference). The experimental evidence (IMP, PubMed:30279285) actually supports 'regulated exocytosis' (GO:0045055), which is not among the offered choices. Among the four alternatives, B is the most defensible: ferlins are calcium-dependent membrane-associated proteins that function at the plasma membrane, and the IEA annotation is present. The answer is supported by the database record, though the evidence level is computational rather than experimental.

Citations as saved: [C6](#evidence-c6), [C7](#evidence-c7), [C5](#evidence-c5), [H5](#evidence-h5), [H6](#evidence-h6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~1426 AA) contains multiple C2 domain-like motifs (e.g., 'CCGREYRTEIKYAKSNVVSWDESHTWTDLCLTDEEWETAYITFEVQAANAFWRNTLLGLVSVQ' and repeated similar patterns), characteristic of the ferlin family of calcium sensors. Transferable knowledge from well-studied C2-domain proteins (synaptotagmin, PKC, ferlins 1-6) establishes that C2 domains mediate calcium-dependent phospholipid binding, targeting proteins to membranes. Ferlins specifically are large multi-C2-domain proteins that associate with the plasma membrane and organize exocytotic machinery there. This distinguishes B (plasma membrane organization) from: A (no microtubule-binding motifs; ferlins are not cytoskeletal proteins), C (aflatoxin biosynthesis is a fungal polyketide pathway, irrelevant to a protozoan with C2 domains), and D (ferlins sense calcium via C2 domains but are not ion channels or transport regulators; they lack transmembrane pore motifs and do not modulate ion flux across membranes). The C-terminal hydrophobic segment ('WYWVRVAAVVFLSIWIFVVAFLYPSLLG') further supports membrane association rather than cytoskeletal or ion-transport function.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of multiple C2 domains in the sequence, combined with family-level knowledge of ferlins and other C2-domain proteins (synaptotagmin, PKC), provides a concrete inference: the protein is a calcium-dependent membrane-associated protein that functions at the plasma membrane. This meaningfully eliminates A (no cytoskeletal features), C (fungal pathway), and D (not an ion transporter), leaving B as the most appropriate choice among the four options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, B is clearly the most defensible. A lacks any cytoskeletal domain evidence, C is a fungal-specific pathway irrelevant to this organism type, and D misattributes calcium sensing to ion transport regulation. While the experimental evidence points to 'regulated exocytosis' (not offered), among the provided alternatives B is the closest match to the protein's membrane-association function.


### Important caveats

- The GO:0007009 annotation is IEA:TreeGrafter (computational inference by phylogenetic similarity), not experimental evidence. The experimental evidence (IMP) supports 'regulated exocytosis' (GO:0045055), which is not among the choices.
- The protein was identified as Toxoplasma gondii Ferlin 2 only through reviewer-only accession matching; the evaluated model had only the raw sequence.
- The distinction between 'plasma membrane organization' and 'regulated exocytosis' is subtle; the question forces a choice that is not the most precise experimental annotation.
- The C2 domain identification from sequence alone is pattern-based and probabilistic, though the multiple repeated motifs and protein length strongly support ferlin family membership.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~1426 AA) contains multiple C2 domain-like motifs (e.g., 'CCGREYRTEIKYAKSNVVSWDESHTWTDLCLTDEEWETAYITFEVQAANAFWRNTLLGLVSVQ' and repeated similar patterns), characteristic of the ferlin family of calcium sensors. Transferable knowledge from well-studied C2-domain proteins (synaptotagmin, PKC, ferlins 1-6) establishes that C2 domains mediate calcium-dependent phospholipid binding, targeting proteins to membranes. Ferlins specifically are large multi-C2-domain proteins that associate with the plasma membrane and organize exocytotic machinery there. This distinguishes B (plasma membrane organization) from: A (no microtubule-binding motifs; ferlins are not cytoskeletal proteins), C (aflatoxin biosynthesis is a fungal polyketide pathway, irrelevant to a protozoan with C2 domains), and D (ferlins sense calcium via C2 domains but are not ion channels or transport regulators; they lack transmembrane pore motifs and do not modulate ion flux across membranes). The C-terminal hydrophobic segment ('WYWVRVAAVVFLSIWIFVVAFLYPSLLG') further supports membrane association rather than cytoskeletal or ion-transport function.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of multiple C2 domains in the sequence, combined with family-level knowledge of ferlins and other C2-domain proteins (synaptotagmin, PKC), provides a concrete inference: the protein is a calcium-dependent membrane-associated protein that functions at the plasma membrane. This meaningfully eliminates A (no cytoskeletal features), C (fungal pathway), and D (not an ion transporter), leaving B as the most appropriate choice among the four options."
  },
  "case_id": "GO_biological_process_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C7",
      "C5",
      "H5",
      "H6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The GO annotation GO:0007009 'plasma membrane organization' is present in the UniProt entry (evidence C6/H5), though only as IEA:TreeGrafter (computational phylogenetic inference). The experimental evidence (IMP, PubMed:30279285) actually supports 'regulated exocytosis' (GO:0045055), which is not among the offered choices. Among the four alternatives, B is the most defensible: ferlins are calcium-dependent membrane-associated proteins that function at the plasma membrane, and the IEA annotation is present. The answer is supported by the database record, though the evidence level is computational rather than experimental."
  },
  "important_caveats": [
    "The GO:0007009 annotation is IEA:TreeGrafter (computational inference by phylogenetic similarity), not experimental evidence. The experimental evidence (IMP) supports 'regulated exocytosis' (GO:0045055), which is not among the choices.",
    "The protein was identified as Toxoplasma gondii Ferlin 2 only through reviewer-only accession matching; the evaluated model had only the raw sequence.",
    "The distinction between 'plasma membrane organization' and 'regulated exocytosis' is subtle; the question forces a choice that is not the most precise experimental annotation.",
    "The C2 domain identification from sequence alone is pattern-based and probabilistic, though the multiple repeated motifs and protein length strongly support ferlin family membership."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, B is clearly the most defensible. A lacks any cytoskeletal domain evidence, C is a fungal-specific pathway irrelevant to this organism type, and D misattributes calcium sensing to ion transport regulation. While the experimental evidence points to 'regulated exocytosis' (not offered), among the provided alternatives B is the closest match to the protein's membrane-association function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The GO annotation GO:0007009 'plasma membrane organization' is present in the UniProt entry (evidence C6/H5), though only as IEA:TreeGrafter (computational phylogenetic inference). The experimental evidence (IMP, PubMed:30279285) actually supports 'regulated exocytosis' (GO:0045055), which is not among the offered choices. Among the four alternatives, B is the most defensible: ferlins are calcium-dependent membrane-associated proteins that function at the plasma membrane, and the IEA annotation is present. The answer is supported by the database record, though the evidence level is computational rather than experimental.",
    "evidence_ids": ["C6", "C7", "C5", "H5", "H6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~1426 AA) contains multiple C2 domain-like motifs (e.g., 'CCGREYRTEIKYAKSNVVSWDESHTWTDLCLTDEEWETAYITFEVQAANAFWRNTLLGLVSVQ' and repeated similar patterns), characteristic of the ferlin family of calcium sensors. Transferable knowledge from well-studied C2-domain proteins (synaptotagmin, PKC, ferlins 1-6) establishes that C2 domains mediate calcium-dependent phospholipid binding, targeting proteins to membranes. Ferlins specifically are large multi-C2-domain proteins that associate with the plasma membrane and organize exocytotic machinery there. This distinguishes B (plasma membrane organization) from: A (no microtubule-binding motifs; ferlins are not cytoskeletal proteins), C (aflatoxin biosynthesis is a fungal polyketide pathway, irrelevant to a protozoan with C2 domains), and D (ferlins sense calcium via C2 domains but are not ion channels or transport regulators; they lack transmembrane pore motifs and do not modulate ion flux across membranes). The C-terminal hydrophobic segment ('WYWVRVAAVVFLSIWIFVVAFLYPSLLG') further supports membrane association rather than cytoskeletal or ion-transport function.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of multiple C2 domains in the sequence, combined with family-level knowledge of ferlins and other C2-domain proteins (synaptotagmin, PKC), provides a concrete inference: the protein is a calcium-dependent membrane-associated protein that functions at the plasma membrane. This meaningfully eliminates A (no cytoskeletal features), C (fungal pathway), and D (not an ion transporter), leaving B as the most appropriate choice among the four options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, B is clearly the most defensible. A lacks any cytoskeletal domain evidence, C is a fungal-specific pathway irrelevant to this organism type, and D misattributes calcium sensing to ion transport regulation. While the experimental evidence points to 'regulated exocytosis' (not offered), among the provided alternatives B is the closest match to the protein's membrane-association function."
  },
  "important_caveats": [
    "The GO:0007009 annotation is IEA:TreeGrafter (computational inference by phylogenetic similarity), not experimental evidence. The experimental evidence (IMP) supports 'regulated exocytosis' (GO:0045055), which is not among the choices.",
    "The protein was identified as Toxoplasma gondii Ferlin 2 only through reviewer-only accession matching; the evaluated model had only the raw sequence.",
    "The distinction between 'plasma membrane organization' and 'regulated exocytosis' is subtle; the question forces a choice that is not the most precise experimental annotation.",
    "The C2 domain identification from sequence alone is pattern-based and probabilistic, though the multiple repeated motifs and protein length strongly support ferlin family membership."
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
  "benchmark_sequence_length": 1426,
  "benchmark_sequence_sha256": "5f16751b277974553550fa64f384077c33893fe628f81cead65b9d7ff0905bb2",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-04-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1426,
  "current_source_sequence_sha256": "5f16751b277974553550fa64f384077c33893fe628f81cead65b9d7ff0905bb2",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7J6K2G0",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "selected_historical_source_sequence_length": 1426,
  "selected_historical_source_sequence_sha256": "5f16751b277974553550fa64f384077c33893fe628f81cead65b9d7ff0905bb2",
  "selected_historical_version": {
    "accession": "A0A7J6K2G0",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FER2_TOXGO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7J6K2G0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-04-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000557509\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii\",\"taxonId\":5811}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30279285\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"Ferlin 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"FER2\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30279285\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"TgFER2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30279285\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"Regulates rhoptry secretion (PubMed:30279285, PubMed:33803212). Required for completing the lytic cycle (PubMed:30279285). Required for host cell invasion (PubMed:30279285). Not required for microneme secretion and conoid extrusion (PubMed:30279285)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0007009\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:plasma membrane organization\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000315\",\"id\":\"30279285\",\"source\":\"PubMed\"}],\"id\":\"GO:0045055\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:regulated exocytosis\"},{\"key\":\"GoEvidenceType\",\"value\":\"IMP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Coleman B.I.\",\"Saha S.\",\"Sato S.\",\"Engelberg K.\",\"Ferguson D.J.P.\",\"Coppens I.\",\"Lodoen M.B.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30279285\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.01510-18\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30279285\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2018\",\"title\":\"A Member of the Ferlin Calcium Sensor Family Is Essential for Toxoplasma gondii Rhoptry Secretion.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30279285\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"RH\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Tagoe D.N.A.\",\"Drozda A.A.\",\"Falco J.A.\",\"Bechtel T.J.\",\"Weerapana E.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33803212\"},{\"database\":\"DOI\",\"id\":\"10.3390/life11030217\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"33803212\",\"journal\":\"Life\",\"lastPage\":\"0\",\"publicationDate\":\"2021\",\"title\":\"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule Secretion.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"RH\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   FER2_TOXGO              Reviewed;        1426 AA.\nAC   A0A7J6K2G0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-APR-2021, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Ferlin 2 {ECO:0000303|PubMed:30279285, ECO:0000303|PubMed:33803212};\nDE            Short=FER2 {ECO:0000303|PubMed:33803212};\nDE            Short=TgFER2 {ECO:0000303|PubMed:30279285, ECO:0000303|PubMed:33803212};\nGN   ORFNames=TGRH88_069870 {ECO:0000312|EMBL:KAF4641177.1};\nOS   Toxoplasma gondii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=5811 {ECO:0000312|Proteomes:UP000557509};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.007451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=RH {ECO:0000303|PubMed:30279285};\nRX   PubMed=30279285; DOI=10.1128/mbio.01510-18;\nRA   Coleman B.I., Saha S., Sato S., Engelberg K., Ferguson D.J.P., Coppens I.,\nRA   Lodoen M.B., Gubbels M.J.;\nRT   \"A Member of the Ferlin Calcium Sensor Family Is Essential for Toxoplasma\nRT   gondii Rhoptry Secretion.\";\nRL   MBio 9:0-0(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.007451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION.\nRC   STRAIN=RH {ECO:0000303|PubMed:33803212};\nRX   PubMed=33803212; DOI=10.3390/life11030217;\nRA   Tagoe D.N.A., Drozda A.A., Falco J.A., Bechtel T.J., Weerapana E.,\nRA   Gubbels M.J.;\nRT   \"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule\nRT   Secretion.\";\nRL   Life 11:0-0(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.007451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Regulates rhoptry secretion (PubMed:30279285,\nCC       PubMed:33803212). Required for completing the lytic cycle\nCC       (PubMed:30279285). Required for host cell invasion (PubMed:30279285).\nCC       Not required for microneme secretion and conoid extrusion\nCC       (PubMed:30279285). {ECO:0000269|PubMed:30279285,\nCC       ECO:0000269|PubMed:33803212}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.007451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0007009; P:plasma membrane organization; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.007451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0045055; P:regulated exocytosis; IMP:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.007451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000226\nname: microtubule cytoskeleton organization\nnamespace: biological_process\ndef: \"A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of cytoskeletal structures comprising microtubules and their associated proteins.\" [GOC:mah]\nsubset: goslim_pombe\nsynonym: \"microtubule cytoskeleton organisation\" EXACT [GOC:mah]\nsynonym: \"microtubule cytoskeleton organization and biogenesis\" RELATED [GOC:mah]\nis_a: GO:0007010 ! cytoskeleton organization\nis_a: GO:0007017 ! microtubule-based process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000226",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 2328-2338",
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
  "excerpt": "[Term]\nid: GO:0007009\nname: plasma membrane organization\nnamespace: biological_process\ndef: \"A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of the plasma membrane.\" [GOC:dph, GOC:jl, GOC:mah]\nsubset: goslim_chembl\nsynonym: \"plasma membrane organisation\" EXACT []\nsynonym: \"plasma membrane organization and biogenesis\" RELATED [GOC:mah]\nis_a: GO:0061024 ! membrane organization\nrelationship: part_of GO:0010256 ! endomembrane system organization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007009",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 72411-72421",
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
  "excerpt": "[Term]\nid: GO:0034765\nname: regulation of monoatomic ion transmembrane transport\nnamespace: biological_process\ndef: \"Any process that modulates the frequency, rate or extent of the directed movement of ions from one side of a membrane to the other.\" [GOC:mah]\nsynonym: \"regulation of ion membrane transport\" EXACT []\nsynonym: \"regulation of ion transmembrane transport\" BROAD []\nsynonym: \"regulation of transmembrane ion transport\" EXACT [GOC:dph, GOC:tb]\nis_a: GO:0034762 ! regulation of transmembrane transport\nis_a: GO:0043269 ! regulation of monoatomic ion transport\nrelationship: regulates GO:0034220 ! monoatomic ion transmembrane transport\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0034765",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 212058-212069",
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
  "excerpt": "[Term]\nid: GO:0045122\nname: aflatoxin biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of aflatoxin, a fungal metabolite found as a contaminant in moldy grains that induces liver cancer. Aflatoxin induces a G to T transversion at codon 249 of p53, leading to its inactivation. Aflatoxin is converted to a chemical carcinogen by P450.\" [ISBN:0716731363, ISBN:0815316194, PMID:15006741]\nsynonym: \"aflatoxin anabolism\" EXACT []\nsynonym: \"aflatoxin biosynthesis\" EXACT []\nsynonym: \"aflatoxin formation\" EXACT []\nsynonym: \"aflatoxin synthesis\" EXACT []\nis_a: GO:0006083 ! acetate metabolic process\nis_a: GO:0043386 ! mycotoxin biosynthetic process\nis_a: GO:0046222 ! aflatoxin metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0045122",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 262067-262079",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 75. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
