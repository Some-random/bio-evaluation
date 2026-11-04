# GO_molecular_function_0083

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0083.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — hydrolase activity, hydrolyzing O-glycosyl compounds

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMLPLLAVSAFASLGAAQTYTSCNPTNSLKTWSLSTDFTQGSSDGWTAISGNVTYGSNGAEFTINKRYDAPTLETNFYIFFGEVEVVMRAANGTGIVSSIVMESDDLDEIDWECTGTDTTQIQTNYFGKGNTTTYDRAIWETVSSPQDEFHTYKVVWTAAAITWYIDGTAVRTLEYADAVDGKNYPQTPMVVKLGIWAGGDPSNSEGTIEWAGGETDYDEVPFTMYVKSVNIINYNPAASYNYTDKTGSYTSIVASNSTTGSGIHSSNSVSVFAPSSSTSTFTSSRALIATASTYPASVQTSSSGVVSLSSSSASSSSAAASSTSGSASAVFTGAAVTNLPSFFFTVFFALAIALAF

[Multiple Choices]
A. DNA-binding transcription repressor activity, RNA polymerase II-specific
B. vinorine hydroxylase activity
C. misfolded protein binding
D. hydrolase activity, hydrolyzing O-glycosyl compounds
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched record describes chitinase activity and reports endo-hydrolysis of chitin linkages; the supplied GO hierarchy places chitinase activity under option D's broader hydrolase term. The record also describes coupled transglycosylase activity, which does not contradict D.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [GO2](#evidence-go2), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, and the sequence's enzyme-like domain includes an acidic motif compatible with a fungal chitinase-family catalytic domain. Transferable knowledge that chitinases hydrolyze glycosidic bonds meaningfully favors D over transcriptional repression, vinorine hydroxylation, or misfolded-protein binding.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference supports the broad hydrolase choice without requiring knowledge of this exact protein's database annotation. The sequence alone may not establish its additional transglycosylase role or exact substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other options describe unrelated activities, while D is the broad category that includes chitinase-mediated glycosidic-bond hydrolysis.


### Important caveats

- The protein is reported to have coupled chitinase and transglycosylase activities; the choices do not offer the latter.
- Reviewer evidence supports the function for the sequence-matched protein, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the sequence's enzyme-like domain includes an acidic motif compatible with a fungal chitinase-family catalytic domain. Transferable knowledge that chitinases hydrolyze glycosidic bonds meaningfully favors D over transcriptional repression, vinorine hydroxylation, or misfolded-protein binding.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference supports the broad hydrolase choice without requiring knowledge of this exact protein's database annotation. The sequence alone may not establish its additional transglycosylase role or exact substrate specificity."
  },
  "case_id": "GO_molecular_function_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "GO2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record describes chitinase activity and reports endo-hydrolysis of chitin linkages; the supplied GO hierarchy places chitinase activity under option D's broader hydrolase term. The record also describes coupled transglycosylase activity, which does not contradict D."
  },
  "important_caveats": [
    "The protein is reported to have coupled chitinase and transglycosylase activities; the choices do not offer the latter.",
    "Reviewer evidence supports the function for the sequence-matched protein, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other options describe unrelated activities, while D is the broad category that includes chitinase-mediated glycosidic-bond hydrolysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record describes chitinase activity and reports endo-hydrolysis of chitin linkages; the supplied GO hierarchy places chitinase activity under option D's broader hydrolase term. The record also describes coupled transglycosylase activity, which does not contradict D.",
    "evidence_ids": ["C5", "C6", "GO2", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the sequence's enzyme-like domain includes an acidic motif compatible with a fungal chitinase-family catalytic domain. Transferable knowledge that chitinases hydrolyze glycosidic bonds meaningfully favors D over transcriptional repression, vinorine hydroxylation, or misfolded-protein binding.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference supports the broad hydrolase choice without requiring knowledge of this exact protein's database annotation. The sequence alone may not establish its additional transglycosylase role or exact substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other options describe unrelated activities, while D is the broad category that includes chitinase-mediated glycosidic-bond hydrolysis."
  },
  "important_caveats": [
    "The protein is reported to have coupled chitinase and transglycosylase activities; the choices do not offer the latter.",
    "Reviewer evidence supports the function for the sequence-matched protein, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q4WD22, Crh-like protein 1 from A. fumigatus) has experimentally confirmed EC 3.2.1.14 chitinase activity (endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin). GO:0004553 ('hydrolase activity, hydrolyzing O-glycosyl compounds') is an ancestor term of GO:0008843 (endochitinase activity) via GO:0004568 (chitinase activity), as confirmed by the ontology is_a paths. The GO term definition 'Catalysis of the hydrolysis of any O-glycosyl bond' with xref EC:3.2.1.- encompasses EC 3.2.1.14. The beta-1,4 glycosidic bonds in chitin are O-glycosyl bonds. Thus D is a valid (though general) molecular function annotation for this protein.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [H4](#evidence-h4), [GO2](#evidence-go2), [GO3](#evidence-go3), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence reveals a multi-domain architecture: (1) an N-terminal signal peptide (MMLPLLAVSAFASLGAAQ) indicating a secreted protein, (2) a catalytic domain region containing clustered acidic residues (e.g., 'TGTDTTQ', 'DPSNSEGT', 'GETDYDE') consistent with the DXXDXDXE catalytic motif of glycoside hydrolase family 18 (GH18) chitinases, (3) a Ser/Thr/Ala-rich O-glycosylation linker region ('SSTSTFTSSRALIATASTYPASVQTSSSGVVSLSSSSASSSSAAASSTSGSASAV') typical of fungal cell-wall-associated glycoside hydrolases, and (4) a C-terminal transmembrane anchor (hydrophobic stretch 'PFFFTVFFALAIALAF'). This architecture is a well-known pattern across fungal GH enzymes (chitinases, glucanases, transglycosylases) that hydrolyze O-glycosyl bonds. Choice A (DNA-binding transcription repressor) requires a nuclear localization signal and DNA-binding domain (zinc finger, homeodomain), entirely incompatible with a signal-peptide/TM-anchored secreted enzyme. Choice B (vinorine hydroxylase) is a cytochrome P450 (EC 1.14.14.104) requiring a heme-binding FxxGxRxCxG motif and ~500 aa length; this 357-aa protein lacks any P450 signature. Choice C (misfolded protein binding) implies chaperone-like protein-protein interaction domains (ATPase, substrate-binding clefts), absent here. The remaining option D (hydrolase activity, hydrolyzing O-glycosyl compounds) is the only one consistent with the GH18-like catalytic domain, the fungal secretion architecture, and the O-glycosylation linker.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A, B, and C based on the absence of their required structural features (DNA-binding domains, P450 heme motif, chaperone domains) and can positively identify D based on the GH18-like catalytic motif, fungal O-glycosylation linker, signal peptide, and TM anchor architecture — all transferable knowledge from the large family of fungal glycoside hydrolases. The inference does not require knowing this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only D is consistent with the sequence architecture. A, B, and C are clearly incompatible with the observed signal peptide, GH18-like catalytic domain, fungal O-glycosylation linker, and transmembrane anchor. No ambiguity exists among the offered alternatives.


### Important caveats

- GO:0004553 is a broad parent term; the protein's most specific annotation is endochitinase activity (GO:0008843) or chitinase activity (GO:0004568). The question asks for 'primary molecular function' and D is the only offered term on the correct lineage.
- The protein also has transglycosylase activity (EC 2.4.-.-, a transferase), but this is not offered as an option and does not conflict with the hydrolase annotation being the best available choice.
- The GO evidence for endochitinase activity is IEA (inferred from EC), while the chitinase/transglycosylase dual function is experimentally supported (ECO:0000269, PubMed:30971696).
- The O-glycosylation linker and GH18 motif recognition from sequence alone may require familiarity with fungal GH enzyme architecture; however, this is well-established transferable knowledge from hundreds of characterized fungal glycoside hydrolases.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence reveals a multi-domain architecture: (1) an N-terminal signal peptide (MMLPLLAVSAFASLGAAQ) indicating a secreted protein, (2) a catalytic domain region containing clustered acidic residues (e.g., 'TGTDTTQ', 'DPSNSEGT', 'GETDYDE') consistent with the DXXDXDXE catalytic motif of glycoside hydrolase family 18 (GH18) chitinases, (3) a Ser/Thr/Ala-rich O-glycosylation linker region ('SSTSTFTSSRALIATASTYPASVQTSSSGVVSLSSSSASSSSAAASSTSGSASAV') typical of fungal cell-wall-associated glycoside hydrolases, and (4) a C-terminal transmembrane anchor (hydrophobic stretch 'PFFFTVFFALAIALAF'). This architecture is a well-known pattern across fungal GH enzymes (chitinases, glucanases, transglycosylases) that hydrolyze O-glycosyl bonds. Choice A (DNA-binding transcription repressor) requires a nuclear localization signal and DNA-binding domain (zinc finger, homeodomain), entirely incompatible with a signal-peptide/TM-anchored secreted enzyme. Choice B (vinorine hydroxylase) is a cytochrome P450 (EC 1.14.14.104) requiring a heme-binding FxxGxRxCxG motif and ~500 aa length; this 357-aa protein lacks any P450 signature. Choice C (misfolded protein binding) implies chaperone-like protein-protein interaction domains (ATPase, substrate-binding clefts), absent here. The remaining option D (hydrolase activity, hydrolyzing O-glycosyl compounds) is the only one consistent with the GH18-like catalytic domain, the fungal secretion architecture, and the O-glycosylation linker.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A, B, and C based on the absence of their required structural features (DNA-binding domains, P450 heme motif, chaperone domains) and can positively identify D based on the GH18-like catalytic motif, fungal O-glycosylation linker, signal peptide, and TM anchor architecture — all transferable knowledge from the large family of fungal glycoside hydrolases. The inference does not require knowing this exact protein's database annotation."
  },
  "case_id": "GO_molecular_function_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "H4",
      "GO2",
      "GO3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein (Q4WD22, Crh-like protein 1 from A. fumigatus) has experimentally confirmed EC 3.2.1.14 chitinase activity (endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin). GO:0004553 ('hydrolase activity, hydrolyzing O-glycosyl compounds') is an ancestor term of GO:0008843 (endochitinase activity) via GO:0004568 (chitinase activity), as confirmed by the ontology is_a paths. The GO term definition 'Catalysis of the hydrolysis of any O-glycosyl bond' with xref EC:3.2.1.- encompasses EC 3.2.1.14. The beta-1,4 glycosidic bonds in chitin are O-glycosyl bonds. Thus D is a valid (though general) molecular function annotation for this protein."
  },
  "important_caveats": [
    "GO:0004553 is a broad parent term; the protein's most specific annotation is endochitinase activity (GO:0008843) or chitinase activity (GO:0004568). The question asks for 'primary molecular function' and D is the only offered term on the correct lineage.",
    "The protein also has transglycosylase activity (EC 2.4.-.-, a transferase), but this is not offered as an option and does not conflict with the hydrolase annotation being the best available choice.",
    "The GO evidence for endochitinase activity is IEA (inferred from EC), while the chitinase/transglycosylase dual function is experimentally supported (ECO:0000269, PubMed:30971696).",
    "The O-glycosylation linker and GH18 motif recognition from sequence alone may require familiarity with fungal GH enzyme architecture; however, this is well-established transferable knowledge from hundreds of characterized fungal glycoside hydrolases."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only D is consistent with the sequence architecture. A, B, and C are clearly incompatible with the observed signal peptide, GH18-like catalytic domain, fungal O-glycosylation linker, and transmembrane anchor. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q4WD22, Crh-like protein 1 from A. fumigatus) has experimentally confirmed EC 3.2.1.14 chitinase activity (endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin). GO:0004553 ('hydrolase activity, hydrolyzing O-glycosyl compounds') is an ancestor term of GO:0008843 (endochitinase activity) via GO:0004568 (chitinase activity), as confirmed by the ontology is_a paths. The GO term definition 'Catalysis of the hydrolysis of any O-glycosyl bond' with xref EC:3.2.1.- encompasses EC 3.2.1.14. The beta-1,4 glycosidic bonds in chitin are O-glycosyl bonds. Thus D is a valid (though general) molecular function annotation for this protein.",
    "evidence_ids": ["C4", "C6", "H4", "GO2", "GO3", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence reveals a multi-domain architecture: (1) an N-terminal signal peptide (MMLPLLAVSAFASLGAAQ) indicating a secreted protein, (2) a catalytic domain region containing clustered acidic residues (e.g., 'TGTDTTQ', 'DPSNSEGT', 'GETDYDE') consistent with the DXXDXDXE catalytic motif of glycoside hydrolase family 18 (GH18) chitinases, (3) a Ser/Thr/Ala-rich O-glycosylation linker region ('SSTSTFTSSRALIATASTYPASVQTSSSGVVSLSSSSASSSSAAASSTSGSASAV') typical of fungal cell-wall-associated glycoside hydrolases, and (4) a C-terminal transmembrane anchor (hydrophobic stretch 'PFFFTVFFALAIALAF'). This architecture is a well-known pattern across fungal GH enzymes (chitinases, glucanases, transglycosylases) that hydrolyze O-glycosyl bonds. Choice A (DNA-binding transcription repressor) requires a nuclear localization signal and DNA-binding domain (zinc finger, homeodomain), entirely incompatible with a signal-peptide/TM-anchored secreted enzyme. Choice B (vinorine hydroxylase) is a cytochrome P450 (EC 1.14.14.104) requiring a heme-binding FxxGxRxCxG motif and ~500 aa length; this 357-aa protein lacks any P450 signature. Choice C (misfolded protein binding) implies chaperone-like protein-protein interaction domains (ATPase, substrate-binding clefts), absent here. The remaining option D (hydrolase activity, hydrolyzing O-glycosyl compounds) is the only one consistent with the GH18-like catalytic domain, the fungal secretion architecture, and the O-glycosylation linker.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A, B, and C based on the absence of their required structural features (DNA-binding domains, P450 heme motif, chaperone domains) and can positively identify D based on the GH18-like catalytic motif, fungal O-glycosylation linker, signal peptide, and TM anchor architecture — all transferable knowledge from the large family of fungal glycoside hydrolases. The inference does not require knowing this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only D is consistent with the sequence architecture. A, B, and C are clearly incompatible with the observed signal peptide, GH18-like catalytic domain, fungal O-glycosylation linker, and transmembrane anchor. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "GO:0004553 is a broad parent term; the protein's most specific annotation is endochitinase activity (GO:0008843) or chitinase activity (GO:0004568). The question asks for 'primary molecular function' and D is the only offered term on the correct lineage.",
    "The protein also has transglycosylase activity (EC 2.4.-.-, a transferase), but this is not offered as an option and does not conflict with the hydrolase annotation being the best available choice.",
    "The GO evidence for endochitinase activity is IEA (inferred from EC), while the chitinase/transglycosylase dual function is experimentally supported (ECO:0000269, PubMed:30971696).",
    "The O-glycosylation linker and GH18 motif recognition from sequence alone may require familiarity with fungal GH enzyme architecture; however, this is well-established transferable knowledge from hundreds of characterized fungal glycoside hydrolases."
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
  "benchmark_sequence_length": 357,
  "benchmark_sequence_sha256": "ec9eee989d92a990718dcd7214cf49eeaec45c138b491bd8fd04ef815d8dc8af",
  "current_entry_audit": {
    "entryVersion": 109,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 357,
  "current_source_sequence_sha256": "ec9eee989d92a990718dcd7214cf49eeaec45c138b491bd8fd04ef815d8dc8af",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 107,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q4WD22",
  "selected_historical_entry_version": 107,
  "selected_historical_record_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "selected_historical_source_sequence_length": 357,
  "selected_historical_source_sequence_sha256": "ec9eee989d92a990718dcd7214cf49eeaec45c138b491bd8fd04ef815d8dc8af",
  "selected_historical_version": {
    "accession": "Q4WD22",
    "database": "Swiss-Prot",
    "entryVersion": 107,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH1_ASPFU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4WD22\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":109,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitinase crh1\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitin transglycosylase crh1\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Dual chitinase/transglycosylase that plays a role in cell wall architecture (PubMed:30971696). Chitinase and transglycosylase activities are coupled (PubMed:30971696). Required for the polysaccharide cross-linking at the septa and the cell wall (PubMed:30971696). More specifically, transfers chitin to 1,6-beta-glucan in the cell wall (PubMed:30971696)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"name\":\"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0008843\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:endochitinase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-EC\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Fang W.\",\"Sanz A.B.\",\"Bartual S.G.\",\"Wang B.\",\"Ferenbach A.T.\",\"Farkas V.\",\"Hurtado-Guerrero R.\",\"Arroyo J.\",\"van Aalten D.M.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30971696\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-019-09674-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"1669\",\"id\":\"30971696\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"1669\",\"publicationDate\":\"2019\",\"title\":\"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh transglycosylases.\",\"volume\":\"10\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:21.374081+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WD22.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H1",
  "excerpt": "ID   CRH1_ASPFU              Reviewed;         357 AA.\nAC   Q4WD22;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 107.\nDE   RecName: Full=Crh-like protein 1 {ECO:0000303|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitinase crh1 {ECO:0000303|PubMed:30971696};\nDE              EC=3.2.1.14 {ECO:0000305|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh1 {ECO:0000303|PubMed:30971696};\nDE              EC=2.4.-.- {ECO:0000269|PubMed:30971696};\nDE   Flags: Precursor;\nGN   Name=crh1 {ECO:0000303|PubMed:30971696}; ORFNames=AFUA_6G03230;\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30971696; DOI=10.1038/s41467-019-09674-0;\nRA   Fang W., Sanz A.B., Bartual S.G., Wang B., Ferenbach A.T., Farkas V.,\nRA   Hurtado-Guerrero R., Arroyo J., van Aalten D.M.F.;\nRT   \"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh\nRT   transglycosylases.\";\nRL   Nat. Commun. 10:1669-1669(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Dual chitinase/transglycosylase that plays a role in cell\nCC       wall architecture (PubMed:30971696). Chitinase and transglycosylase\nCC       activities are coupled (PubMed:30971696). Required for the\nCC       polysaccharide cross-linking at the septa and the cell wall\nCC       (PubMed:30971696). More specifically, transfers chitin to 1,6-beta-\nCC       glucan in the cell wall (PubMed:30971696).\nCC       {ECO:0000269|PubMed:30971696}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide\nCC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;\nCC         Evidence={ECO:0000305|PubMed:30971696};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0008843; F:endochitinase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0016757; F:glycosyltransferase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:34.790448+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b",
  "url": "https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0001227\nname: DNA-binding transcription repressor activity, RNA polymerase II-specific\nnamespace: molecular_function\nalt_id: GO:0001078\nalt_id: GO:0001206\nalt_id: GO:0001210\nalt_id: GO:0001214\ndef: \"A DNA-binding transcription factor activity that represses or decreases the transcription of specific gene sets transcribed by RNA polymerase II.\" [GOC:txnOH-2018]\ncomment: For usage guidance, see comment in GO:0003700 ; DNA-binding transcription factor activity.\nsynonym: \"distal enhancer DNA-binding transcription repressor activity, RNA polymerase II-specific\" NARROW []\nsynonym: \"metal ion regulated core promoter proximal region sequence-specific DNA binding RNA polymerase II transcription factor activity involved in negative regulation of transcription\" NARROW []\nsynonym: \"metal ion regulated sequence-specific DNA binding transcription factor activity involved in negative regulation of transcription\" NARROW []\nsynonym: \"proximal promoter DNA-binding transcription repressor activity, RNA polymerase II-specific\" NARROW []\nsynonym: \"RNA polymerase II core promoter proximal region sequence-specific DNA binding transcription factor activity involved in negative regulation of transcription\" NARROW []\nsynonym: \"RNA polymerase II distal enhancer sequence-specific DNA-binding transcription factor activity involved in negative regulation of transcription\" NARROW []\nsynonym: \"RNA polymerase II transcription regulatory region sequence-specific DNA binding transcription factor activity involved in negative regulation of transcription\" EXACT []\nsynonym: \"RNA polymerase II transcriptional repressor activity, metal ion regulated core promoter proximal region sequence-specific binding\" NARROW []\nsynonym: \"RNA polymerase II transcriptional repressor activity, metal ion regulated proximal promoter sequence-specific DNA binding\" NARROW []\nsynonym: \"sequence-specific distal enhancer binding RNA polymerase II transcription factor activity involved in negative regulation of transcription\" NARROW []\nsynonym: \"transcriptional repressor activity, metal ion regulated sequence-specific DNA binding\" NARROW []\nsynonym: \"transcriptional repressor activity, RNA polymerase II distal enhancer sequence-specific binding\" NARROW []\nsynonym: \"transcriptional repressor activity, RNA polymerase II proximal promoter sequence-specific DNA binding\" NARROW []\nsynonym: \"transcriptional repressor activity, RNA polymerase II transcription regulatory region sequence-specific DNA binding\" EXACT []\nxref: Reactome:R-HSA-8936851 \"AHRR binds ARNT\"\nis_a: GO:0000981 ! DNA-binding transcription factor activity, RNA polymerase II-specific\nis_a: GO:0001217 ! DNA-binding transcription repressor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0001227",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 8628-8655",
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
  "excerpt": "[Term]\nid: GO:0004553\nname: hydrolase activity, hydrolyzing O-glycosyl compounds\nnamespace: molecular_function\nalt_id: GO:0016800\ndef: \"Catalysis of the hydrolysis of any O-glycosyl bond.\" [GOC:mah]\nsynonym: \"O-glucosyl hydrolase activity\" EXACT []\nxref: EC:3.2.1.-\nxref: Reactome:R-HSA-5694563 \"ABHD10 hydrolyses MPAG\"\nxref: Reactome:R-HSA-6786652 \"CHIT1 hydrolyses CHIT to 3xADGP\"\nxref: Reactome:R-HSA-9661820 \"Bacterial GUSB hydrolyses BDG to BIL\"\nis_a: GO:0016798 ! hydrolase activity, acting on glycosyl bonds\nproperty_value: skos:exactMatch EC:3.2.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004553",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 44250-44263",
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
  "excerpt": "[Term]\nid: GO:0004568\nname: chitinase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of (1->4)-beta linkages of N-acetyl-D-glucosamine (GlcNAc) polymers of chitin and chitodextrins.\" [GOC:bf, GOC:kah, GOC:pde, PMID:11468293]\nxref: Reactome:R-HSA-6786421 \"CHIA hydrolyses chitin\"\nis_a: GO:0004553 ! hydrolase activity, hydrolyzing O-glycosyl compounds\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004568",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 44534-44541",
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
  "excerpt": "[Term]\nid: GO:0008843\nname: endochitinase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of nonterminal (1->4)-beta linkages of N-acetyl-D-glucosamine (GlcNAc) polymers of chitin and chitodextrins. Typically, endochitinases cleave randomly within the chitin chain.\" [EC:3.2.1.14, GOC:bf, GOC:kah, GOC:pde, PMID:11468293]\nsynonym: \"1,4-beta-poly-N-acetylglucosaminidase\" EXACT [EC:3.2.1.14]\nsynonym: \"chitinase\" EXACT [EC:3.2.1.14]\nsynonym: \"chitodextrinase\" EXACT [EC:3.2.1.14]\nsynonym: \"poly-beta-glucosaminidase\" EXACT [EC:3.2.1.14]\nxref: EC:3.2.1.14\nxref: MetaCyc:3.2.1.14-RXN\nis_a: GO:0004568 ! chitinase activity\nproperty_value: skos:exactMatch EC:3.2.1.14\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008843",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 88913-88926",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0050596\nname: vinorine hydroxylase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: H+ + NADPH + O2 + vinorine = H2O + NADP+ + vomilenine.\" [EC:1.14.14.104, RHEA:17257]\nsynonym: \"vinorine,NADPH:oxygen oxidoreductase (21alpha-hydroxylating)\" RELATED [EC:1.14.14.104]\nxref: EC:1.14.14.104\nxref: KEGG_REACTION:R05877\nxref: MetaCyc:1.14.13.75-RXN\nxref: RHEA:17257\nis_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen\nproperty_value: skos:exactMatch EC:1.14.14.104\nproperty_value: skos:exactMatch RHEA:17257\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0050596",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 317426-317439",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "excerpt": "[Term]\nid: GO:0051787\nname: misfolded protein binding\nnamespace: molecular_function\ndef: \"Binding to a misfolded protein.\" [GOC:ai]\nxref: Reactome:R-HSA-5324632 \"Dissociation of cytosolic HSF1:HSP90:HDAC6:PTGES3 upon sensing protein aggregates\"\nis_a: GO:0005515 ! protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051787",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 330727-330734",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 83. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
