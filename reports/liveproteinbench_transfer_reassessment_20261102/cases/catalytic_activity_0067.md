# catalytic_activity_0067

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0067.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPSHTFNPQAGYDLAVDRNLGLGEIFYNRAQKSHQAIAVCDGGAVLTYGQLHAKAYRLAQELSQWLRLTEKPVGIVVQHGMADVVAQMAVIYAGGSCAPMDPTLPDNQIQGRLKRLDAVCVLTDQANRHRDLGADVLCIDDFDIADLAPEDTLYPVATNLEHCAYLIHTSGTTAEPKAVQIAARSILHVAFYAPLEPVYDTDVVAHANNSSFDVSLFDIWVPLLRGAQIAVINKAVLLDPPMMAREIDRLGITVMATTTAVLNLAAFIYPKAFAKLRLVTIGGEAANVAAIRIILKNGPPAMLFNAYGPTECCVFCLAHQITPADVEHGSIGVSIGKPVGRTITYIAGDEGGESDQGELWIGGPGVSPGYFRQPEKNLAAFSDLGEAMTSLENPVRFYRTGDIVRRRPNGALEYVGRRDHQVKVRGFRIELEAVEAGLLKTGLFSDAVAMRIEMPQNGAGSILAAYVVPTDVSKPPTMDEALESAKSILPHYMVPQLELVPRLPLNRHLKVDRKQLAELFGRRWEDVSPAQPENASQDVRSALVSLWATVLASPLSTYGDDDDFLHLGGTSLQAAMLINQIRHKFDIEVSLLTLYDNTTLGALTSIIKQRLSGQSETLHNEKDSWVADSEIADDLSCPLDRPIDWCRDTEGRVFLTGGTGFVGAFLLADLLHMPQTSQVRCLVRATDAAVGQERLRAALDKYGLWEDGFADKLVAIAGLLEDDYLGMGREQFEEAASWASVVFHLGARVNYAQPYSLHRASNTLGTRNMVRFACAGRTKAIHYVSSIGCFGPTGSILGTTSVREDEPLLPHITALPYDHGYAQSQWVADALLRRLMDRGFPIAIYRPGFIVGHSQTGACNPDDFLSRLIDACREIGCYPQLPNQRKEFVPVDYVNAAILHIAASPASLGHAYHIVPPTRAVSIDMDNSMALVDRAGNSPMRPVSYKEWVERLAATSPKRLLPLQPMLAERVKDGLTRWELYENMPVYETTNTARALQNYPGGLQFPVLDTSLMKRYLDFLEAKG

[Multiple Choices]
A. (S)-norprotosinomenine + S-adenosyl-L-methionine = (S)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)
B. UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)
C. L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)
D. an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)
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

> The sequence-matched UniProt record annotates the reaction in choice C and cites experimental evidence (ECO:0000269) from the referenced study. This supports the key, though the annotation is not itself the primary experimental report.

Citations as saved: [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1,024-aa sequence is a large, soluble, apparently multidomain enzyme, with sequence features consistent with an NRPS/adenylate-forming enzyme rather than a compact SAM-dependent methyltransferase (A) or UDP-sugar dehydrogenase (B). It also lacks the evident membrane-spanning character expected for the dolichol-linked glycan mannosyltransferase in D. That family/architecture-level inference makes the specialized amino-acid and nucleotide-cofactor chemistry in C the meaningful choice among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable inference from sequence architecture and enzyme-family patterns distinguishes C from the offered alternatives, although those features alone do not prove the exact reaction or its physiological direction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered reaction is comparably supported by the sequence-level family and architecture cues.


### Important caveats

- The exact catalytic activity is specialized and is not established solely by the sequence-level inference.
- The reviewer-only record ties the annotation to experimental evidence, but the cited primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1,024-aa sequence is a large, soluble, apparently multidomain enzyme, with sequence features consistent with an NRPS/adenylate-forming enzyme rather than a compact SAM-dependent methyltransferase (A) or UDP-sugar dehydrogenase (B). It also lacks the evident membrane-spanning character expected for the dolichol-linked glycan mannosyltransferase in D. That family/architecture-level inference makes the specialized amino-acid and nucleotide-cofactor chemistry in C the meaningful choice among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from sequence architecture and enzyme-family patterns distinguishes C from the offered alternatives, although those features alone do not prove the exact reaction or its physiological direction."
  },
  "case_id": "catalytic_activity_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the reaction in choice C and cites experimental evidence (ECO:0000269) from the referenced study. This supports the key, though the annotation is not itself the primary experimental report."
  },
  "important_caveats": [
    "The exact catalytic activity is specialized and is not established solely by the sequence-level inference.",
    "The reviewer-only record ties the annotation to experimental evidence, but the cited primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction is comparably supported by the sequence-level family and architecture cues."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the reaction in choice C and cites experimental evidence (ECO:0000269) from the referenced study. This supports the key, though the annotation is not itself the primary experimental report.",
    "evidence_ids": ["H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1,024-aa sequence is a large, soluble, apparently multidomain enzyme, with sequence features consistent with an NRPS/adenylate-forming enzyme rather than a compact SAM-dependent methyltransferase (A) or UDP-sugar dehydrogenase (B). It also lacks the evident membrane-spanning character expected for the dolichol-linked glycan mannosyltransferase in D. That family/architecture-level inference makes the specialized amino-acid and nucleotide-cofactor chemistry in C the meaningful choice among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from sequence architecture and enzyme-family patterns distinguishes C from the offered alternatives, although those features alone do not prove the exact reaction or its physiological direction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction is comparably supported by the sequence-level family and architecture cues."
  },
  "important_caveats": [
    "The exact catalytic activity is specialized and is not established solely by the sequence-level inference.",
    "The reviewer-only record ties the annotation to experimental evidence, but the cited primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7T8F1L4 (FRZA_CLASX) is annotated with EC 1.2.1.101 and the exact reaction in choice C, supported by experimental evidence (ECO:0000269) from PubMed 33372776 (Zhang et al., JACS 2021). The sequence matches perfectly (1024 aa, SHA256 identical). The physiological direction is noted as right-to-left (reduction of L-tyrosine to L-tyrosinal), but the written reaction equation in choice C matches the canonical Rhea reaction RHEA:57412 exactly.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1024-aa sequence displays unmistakable nonribosomal peptide synthetase (NRPS) multi-domain architecture: (1) the A-domain adenylation motif 'GDEGGESDQGELWIGGPGVSPGY' (A3 signature), (2) the condensation-domain motif 'GHSQTGACNPDDFLSRLIDACREIG' containing the HHxxxDG pattern, (3) the PP-binding motif 'GGTGFVGAFLL' of a thiolation domain, and (4) NADP-binding Rossmann-like motifs ('GGAVLTYG'). This architecture is diagnostic of NRPS or NRPS-like enzymes. Among the four choices: (A) a SAM-dependent methyltransferase (~250-350 aa, Rossmann fold, no NRPS domains); (B) UDP-GlcNAc dehydrogenase (~350 aa, small oxidoreductase, no NRPS domains); (D) a dolichol mannosyltransferase (~250-350 aa glycosyltransferase, no NRPS domains) — none match a 1024-aa multi-domain NRPS. Only (C), EC 1.2.1.101 amino-aldehyde dehydrogenase (NADP+), is an NRPS-associated tailoring reaction that explains both the A-domain (AMP/diphosphate coupling) and the NADP-binding region (NADP+/NADPH). The combination of adenylation motif + NADP-binding + NRPS domain architecture uniquely selects C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the canonical NRPS A-domain GDEGGES motif, C-domain HHxxxDG motif, and PP-binding motif can eliminate choices A, B, and D as incompatible with a 1024-aa multi-domain NRPS enzyme. Only choice C describes an NRPS-related reaction (amino-aldehyde dehydrogenase coupled to adenylation), making it the sole viable answer. The specific substrate identity (tyrosine/tyrosinal) is a secondary detail; the primary discrimination is enzyme-class level.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The NRPS domain architecture in the sequence is unambiguous and incompatible with methyltransferase (A), small dehydrogenase (B), or glycosyltransferase (D) enzyme classes. Only C is consistent with the observed multi-domain NRPS-like architecture.


### Important caveats

- The specific identification of tyrosine/tyrosinal as the substrate (vs. another amino acid) would require A-domain specificity-code analysis, but this is unnecessary for answering the question since C is the only NRPS-related option.
- The physiological direction is right-to-left (reduction of L-tyrosine to L-tyrosinal), meaning the enzyme physiologically produces the aldehyde for NRPS assembly, but the written equation in C matches the canonical Rhea reaction direction.
- The annotation evidence code ECO:0000269 indicates experimental (not purely computational) support for the catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1024-aa sequence displays unmistakable nonribosomal peptide synthetase (NRPS) multi-domain architecture: (1) the A-domain adenylation motif 'GDEGGESDQGELWIGGPGVSPGY' (A3 signature), (2) the condensation-domain motif 'GHSQTGACNPDDFLSRLIDACREIG' containing the HHxxxDG pattern, (3) the PP-binding motif 'GGTGFVGAFLL' of a thiolation domain, and (4) NADP-binding Rossmann-like motifs ('GGAVLTYG'). This architecture is diagnostic of NRPS or NRPS-like enzymes. Among the four choices: (A) a SAM-dependent methyltransferase (~250-350 aa, Rossmann fold, no NRPS domains); (B) UDP-GlcNAc dehydrogenase (~350 aa, small oxidoreductase, no NRPS domains); (D) a dolichol mannosyltransferase (~250-350 aa glycosyltransferase, no NRPS domains) — none match a 1024-aa multi-domain NRPS. Only (C), EC 1.2.1.101 amino-aldehyde dehydrogenase (NADP+), is an NRPS-associated tailoring reaction that explains both the A-domain (AMP/diphosphate coupling) and the NADP-binding region (NADP+/NADPH). The combination of adenylation motif + NADP-binding + NRPS domain architecture uniquely selects C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the canonical NRPS A-domain GDEGGES motif, C-domain HHxxxDG motif, and PP-binding motif can eliminate choices A, B, and D as incompatible with a 1024-aa multi-domain NRPS enzyme. Only choice C describes an NRPS-related reaction (amino-aldehyde dehydrogenase coupled to adenylation), making it the sole viable answer. The specific substrate identity (tyrosine/tyrosinal) is a secondary detail; the primary discrimination is enzyme-class level."
  },
  "case_id": "catalytic_activity_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7T8F1L4 (FRZA_CLASX) is annotated with EC 1.2.1.101 and the exact reaction in choice C, supported by experimental evidence (ECO:0000269) from PubMed 33372776 (Zhang et al., JACS 2021). The sequence matches perfectly (1024 aa, SHA256 identical). The physiological direction is noted as right-to-left (reduction of L-tyrosine to L-tyrosinal), but the written reaction equation in choice C matches the canonical Rhea reaction RHEA:57412 exactly."
  },
  "important_caveats": [
    "The specific identification of tyrosine/tyrosinal as the substrate (vs. another amino acid) would require A-domain specificity-code analysis, but this is unnecessary for answering the question since C is the only NRPS-related option.",
    "The physiological direction is right-to-left (reduction of L-tyrosine to L-tyrosinal), meaning the enzyme physiologically produces the aldehyde for NRPS assembly, but the written equation in C matches the canonical Rhea reaction direction.",
    "The annotation evidence code ECO:0000269 indicates experimental (not purely computational) support for the catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NRPS domain architecture in the sequence is unambiguous and incompatible with methyltransferase (A), small dehydrogenase (B), or glycosyltransferase (D) enzyme classes. Only C is consistent with the observed multi-domain NRPS-like architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7T8F1L4 (FRZA_CLASX) is annotated with EC 1.2.1.101 and the exact reaction in choice C, supported by experimental evidence (ECO:0000269) from PubMed 33372776 (Zhang et al., JACS 2021). The sequence matches perfectly (1024 aa, SHA256 identical). The physiological direction is noted as right-to-left (reduction of L-tyrosine to L-tyrosinal), but the written reaction equation in choice C matches the canonical Rhea reaction RHEA:57412 exactly.",
    "evidence_ids": ["C5", "H4", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1024-aa sequence displays unmistakable nonribosomal peptide synthetase (NRPS) multi-domain architecture: (1) the A-domain adenylation motif 'GDEGGESDQGELWIGGPGVSPGY' (A3 signature), (2) the condensation-domain motif 'GHSQTGACNPDDFLSRLIDACREIG' containing the HHxxxDG pattern, (3) the PP-binding motif 'GGTGFVGAFLL' of a thiolation domain, and (4) NADP-binding Rossmann-like motifs ('GGAVLTYG'). This architecture is diagnostic of NRPS or NRPS-like enzymes. Among the four choices: (A) a SAM-dependent methyltransferase (~250-350 aa, Rossmann fold, no NRPS domains); (B) UDP-GlcNAc dehydrogenase (~350 aa, small oxidoreductase, no NRPS domains); (D) a dolichol mannosyltransferase (~250-350 aa glycosyltransferase, no NRPS domains) — none match a 1024-aa multi-domain NRPS. Only (C), EC 1.2.1.101 amino-aldehyde dehydrogenase (NADP+), is an NRPS-associated tailoring reaction that explains both the A-domain (AMP/diphosphate coupling) and the NADP-binding region (NADP+/NADPH). The combination of adenylation motif + NADP-binding + NRPS domain architecture uniquely selects C.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the canonical NRPS A-domain GDEGGES motif, C-domain HHxxxDG motif, and PP-binding motif can eliminate choices A, B, and D as incompatible with a 1024-aa multi-domain NRPS enzyme. Only choice C describes an NRPS-related reaction (amino-aldehyde dehydrogenase coupled to adenylation), making it the sole viable answer. The specific substrate identity (tyrosine/tyrosinal) is a secondary detail; the primary discrimination is enzyme-class level."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NRPS domain architecture in the sequence is unambiguous and incompatible with methyltransferase (A), small dehydrogenase (B), or glycosyltransferase (D) enzyme classes. Only C is consistent with the observed multi-domain NRPS-like architecture."
  },
  "important_caveats": [
    "The specific identification of tyrosine/tyrosinal as the substrate (vs. another amino acid) would require A-domain specificity-code analysis, but this is unnecessary for answering the question since C is the only NRPS-related option.",
    "The physiological direction is right-to-left (reduction of L-tyrosine to L-tyrosinal), meaning the enzyme physiologically produces the aldehyde for NRPS assembly, but the written equation in C matches the canonical Rhea reaction direction.",
    "The annotation evidence code ECO:0000269 indicates experimental (not purely computational) support for the catalytic activity."
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
  "benchmark_sequence_length": 1024,
  "benchmark_sequence_sha256": "78903b102e2259d837b80ac44bcf15e6ae1534722167cff1a23d530bb0db74e0",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1024,
  "current_source_sequence_sha256": "78903b102e2259d837b80ac44bcf15e6ae1534722167cff1a23d530bb0db74e0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8F1L4",
  "selected_historical_entry_version": 18,
  "selected_historical_record_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "selected_historical_source_sequence_length": 1024,
  "selected_historical_source_sequence_sha256": "78903b102e2259d837b80ac44bcf15e6ae1534722167cff1a23d530bb0db74e0",
  "selected_historical_version": {
    "accession": "A0A7T8F1L4",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZA_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1L4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.101\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Non-canonical nonribosomal peptide synthetase FrzA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:57414\"}}],\"reaction\":{\"ecNumber\":\"1.2.1.101\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"name\":\"L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:57412\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:141668\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456215\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H1",
  "excerpt": "ID   FRZA_CLASX              Reviewed;        1024 AA.\nAC   A0A7T8F1L4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};\nDE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};\nGN   Name=FrzA {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};\nDE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP +\nCC         NADPH + H(+); Xref=Rhea:RHEA:57412, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58315, ChEBI:CHEBI:58349, ChEBI:CHEBI:141668,\nCC         ChEBI:CHEBI:456215; EC=1.2.1.101;\nCC         Evidence={ECO:0000269|PubMed:33372776};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:57414;\nCC         Evidence={ECO:0000269|PubMed:33372776};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
