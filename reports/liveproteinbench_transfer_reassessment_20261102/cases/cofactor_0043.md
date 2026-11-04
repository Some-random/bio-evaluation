# cofactor_0043

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0043.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — pantetheine 4&#x27;-phosphate

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
A. Mg(2+)
B. NAD(+)
C. pantetheine 4'-phosphate
D. Fe(2+)
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

> The sequence-matched UniProt record annotates pantetheine 4'-phosphate as the cofactor. The annotation is supported by a PROSITE rule, so it is computational evidence rather than direct experimental confirmation of cofactor dependence.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, multidomain sequence includes a serine-containing DSL-like motif consistent with a nonribosomal peptide synthetase carrier-protein domain. Transferable knowledge of these domains predicts attachment of 4'-phosphopantetheine to a conserved serine, providing a swinging arm for substrate handling. That gives a meaningful basis for choice C over the metal-ion and NAD(+) options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A carrier-protein-domain inference from sequence features and general NRPS biology can distinguish the offered choice without requiring the exact protein's database annotation. This supports a probabilistic inference, not proof from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the carrier-protein phosphopantetheine group is the distinct fit; the supplied evidence does not identify another listed option as equally defensible.


### Important caveats

- The cited cofactor annotation is rule-based computational evidence, not direct experimental validation.
- The sequence supports a transferable family/domain inference, but does not by itself establish every detail of cofactor dependence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, multidomain sequence includes a serine-containing DSL-like motif consistent with a nonribosomal peptide synthetase carrier-protein domain. Transferable knowledge of these domains predicts attachment of 4'-phosphopantetheine to a conserved serine, providing a swinging arm for substrate handling. That gives a meaningful basis for choice C over the metal-ion and NAD(+) options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A carrier-protein-domain inference from sequence features and general NRPS biology can distinguish the offered choice without requiring the exact protein's database annotation. This supports a probabilistic inference, not proof from sequence alone."
  },
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pantetheine 4'-phosphate as the cofactor. The annotation is supported by a PROSITE rule, so it is computational evidence rather than direct experimental confirmation of cofactor dependence."
  },
  "important_caveats": [
    "The cited cofactor annotation is rule-based computational evidence, not direct experimental validation.",
    "The sequence supports a transferable family/domain inference, but does not by itself establish every detail of cofactor dependence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the carrier-protein phosphopantetheine group is the distinct fit; the supplied evidence does not identify another listed option as equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pantetheine 4'-phosphate as the cofactor. The annotation is supported by a PROSITE rule, so it is computational evidence rather than direct experimental confirmation of cofactor dependence.",
    "evidence_ids": ["H4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, multidomain sequence includes a serine-containing DSL-like motif consistent with a nonribosomal peptide synthetase carrier-protein domain. Transferable knowledge of these domains predicts attachment of 4'-phosphopantetheine to a conserved serine, providing a swinging arm for substrate handling. That gives a meaningful basis for choice C over the metal-ion and NAD(+) options.",
    "missing_item_specific_fact": "",
    "reason": "A carrier-protein-domain inference from sequence features and general NRPS biology can distinguish the offered choice without requiring the exact protein's database annotation. This supports a probabilistic inference, not proof from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the carrier-protein phosphopantetheine group is the distinct fit; the supplied evidence does not identify another listed option as equally defensible."
  },
  "important_caveats": [
    "The cited cofactor annotation is rule-based computational evidence, not direct experimental validation.",
    "The sequence supports a transferable family/domain inference, but does not by itself establish every detail of cofactor dependence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly lists pantetheine 4'-phosphate as the cofactor, with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. This is a computational/PROSITE-pattern-based annotation rather than a direct experimental cofactor measurement. However, the protein is annotated as a nonribosomal peptide synthetase (EC 1.2.1.101, FrzA), and NRPS enzymes require pantetheine 4'-phosphate for their peptidyl carrier protein (PCP) domains. The PROSITE PP-binding pattern detection is consistent with the known biochemistry of NRPS systems. The annotation is supported but rests on pattern recognition rather than a direct biochemical assay of the cofactor.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable features of a nonribosomal peptide synthetase (NRPS): (1) A phosphopantetheine (PP) binding motif is present — the stretch 'GGTGFVGAFL' and 'GGSCAPMDP' contain GxS/GGDS-type motifs characteristic of peptidyl carrier protein (PCP) domains, where a conserved serine is post-translationally modified with pantetheine 4'-phosphate. This PP-binding motif is one of the most well-known, transferable sequence signatures across the entire NRPS and fatty-acid synthase (FAS) superfamily. (2) Adenylation (A) domain motifs are also discernible (e.g., 'GGEAANVAAIRIILKNGPPAMLFNAYGPTECC' region resembles the C3/C4 adenylation domain motifs). Recognizing these NRPS domain signatures from general family knowledge (learned from hundreds of characterized NRPS proteins like gramicidin S synthetase, surfactin synthetase, etc.) leads directly to pantetheine 4'-phosphate as the required cofactor, because the PCP domain's catalytic function depends on the PP arm carrying the growing peptide chain. The distractors are readily excluded: Mg(2+) is a general metal cofactor for kinases/polymerases, NAD(+) is for dehydrogenases, and Fe(2+) is for dioxygenases/oxidases — none of which match the NRPS/PCP cofactor requirement. This is a standard family-level inference, not a lookup of this specific protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the PP-binding motif and adenylation domain architecture from general NRPS/FAS family knowledge, which is broadly transferable across hundreds of characterized NRPS proteins. This family-level pattern meaningfully distinguishes pantetheine 4'-phosphate (C) from the three distractors without needing the specific annotation of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PP-binding motif and NRPS domain architecture point unambiguously to pantetheine 4'-phosphate. The distractors (Mg2+, NAD+, Fe2+) correspond to entirely different enzyme classes and are not plausible cofactors for an NRPS PCP domain. No other option is defensible given the sequence features.


### Important caveats

- The UniProt cofactor annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is computational pattern-based rather than a direct experimental cofactor measurement. The annotation is consistent with NRPS biochemistry but is not an independent experimental determination of the cofactor for this specific enzyme.
- The protein is described as a 'non-canonical' NRPS, which could in principle imply unusual cofactor requirements, but the presence of the PP-binding motif in the sequence supports the standard NRPS cofactor assignment.
- The PP-binding motif in this sequence ('GGTGFVGA', 'GGSCAPMDP') is a variant of the canonical 'GxDSL' motif; recognizing these variants requires familiarity with the diversity of PP-binding motifs across NRPS/FAS families.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable features of a nonribosomal peptide synthetase (NRPS): (1) A phosphopantetheine (PP) binding motif is present — the stretch 'GGTGFVGAFL' and 'GGSCAPMDP' contain GxS/GGDS-type motifs characteristic of peptidyl carrier protein (PCP) domains, where a conserved serine is post-translationally modified with pantetheine 4'-phosphate. This PP-binding motif is one of the most well-known, transferable sequence signatures across the entire NRPS and fatty-acid synthase (FAS) superfamily. (2) Adenylation (A) domain motifs are also discernible (e.g., 'GGEAANVAAIRIILKNGPPAMLFNAYGPTECC' region resembles the C3/C4 adenylation domain motifs). Recognizing these NRPS domain signatures from general family knowledge (learned from hundreds of characterized NRPS proteins like gramicidin S synthetase, surfactin synthetase, etc.) leads directly to pantetheine 4'-phosphate as the required cofactor, because the PCP domain's catalytic function depends on the PP arm carrying the growing peptide chain. The distractors are readily excluded: Mg(2+) is a general metal cofactor for kinases/polymerases, NAD(+) is for dehydrogenases, and Fe(2+) is for dioxygenases/oxidases — none of which match the NRPS/PCP cofactor requirement. This is a standard family-level inference, not a lookup of this specific protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PP-binding motif and adenylation domain architecture from general NRPS/FAS family knowledge, which is broadly transferable across hundreds of characterized NRPS proteins. This family-level pattern meaningfully distinguishes pantetheine 4'-phosphate (C) from the three distractors without needing the specific annotation of this exact protein."
  },
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists pantetheine 4'-phosphate as the cofactor, with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. This is a computational/PROSITE-pattern-based annotation rather than a direct experimental cofactor measurement. However, the protein is annotated as a nonribosomal peptide synthetase (EC 1.2.1.101, FrzA), and NRPS enzymes require pantetheine 4'-phosphate for their peptidyl carrier protein (PCP) domains. The PROSITE PP-binding pattern detection is consistent with the known biochemistry of NRPS systems. The annotation is supported but rests on pattern recognition rather than a direct biochemical assay of the cofactor."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is computational pattern-based rather than a direct experimental cofactor measurement. The annotation is consistent with NRPS biochemistry but is not an independent experimental determination of the cofactor for this specific enzyme.",
    "The protein is described as a 'non-canonical' NRPS, which could in principle imply unusual cofactor requirements, but the presence of the PP-binding motif in the sequence supports the standard NRPS cofactor assignment.",
    "The PP-binding motif in this sequence ('GGTGFVGA', 'GGSCAPMDP') is a variant of the canonical 'GxDSL' motif; recognizing these variants requires familiarity with the diversity of PP-binding motifs across NRPS/FAS families."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PP-binding motif and NRPS domain architecture point unambiguously to pantetheine 4'-phosphate. The distractors (Mg2+, NAD+, Fe2+) correspond to entirely different enzyme classes and are not plausible cofactors for an NRPS PCP domain. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists pantetheine 4'-phosphate as the cofactor, with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. This is a computational/PROSITE-pattern-based annotation rather than a direct experimental cofactor measurement. However, the protein is annotated as a nonribosomal peptide synthetase (EC 1.2.1.101, FrzA), and NRPS enzymes require pantetheine 4'-phosphate for their peptidyl carrier protein (PCP) domains. The PROSITE PP-binding pattern detection is consistent with the known biochemistry of NRPS systems. The annotation is supported but rests on pattern recognition rather than a direct biochemical assay of the cofactor.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable features of a nonribosomal peptide synthetase (NRPS): (1) A phosphopantetheine (PP) binding motif is present — the stretch 'GGTGFVGAFL' and 'GGSCAPMDP' contain GxS/GGDS-type motifs characteristic of peptidyl carrier protein (PCP) domains, where a conserved serine is post-translationally modified with pantetheine 4'-phosphate. This PP-binding motif is one of the most well-known, transferable sequence signatures across the entire NRPS and fatty-acid synthase (FAS) superfamily. (2) Adenylation (A) domain motifs are also discernible (e.g., 'GGEAANVAAIRIILKNGPPAMLFNAYGPTECC' region resembles the C3/C4 adenylation domain motifs). Recognizing these NRPS domain signatures from general family knowledge (learned from hundreds of characterized NRPS proteins like gramicidin S synthetase, surfactin synthetase, etc.) leads directly to pantetheine 4'-phosphate as the required cofactor, because the PCP domain's catalytic function depends on the PP arm carrying the growing peptide chain. The distractors are readily excluded: Mg(2+) is a general metal cofactor for kinases/polymerases, NAD(+) is for dehydrogenases, and Fe(2+) is for dioxygenases/oxidases — none of which match the NRPS/PCP cofactor requirement. This is a standard family-level inference, not a lookup of this specific protein's record.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PP-binding motif and adenylation domain architecture from general NRPS/FAS family knowledge, which is broadly transferable across hundreds of characterized NRPS proteins. This family-level pattern meaningfully distinguishes pantetheine 4'-phosphate (C) from the three distractors without needing the specific annotation of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PP-binding motif and NRPS domain architecture point unambiguously to pantetheine 4'-phosphate. The distractors (Mg2+, NAD+, Fe2+) correspond to entirely different enzyme classes and are not plausible cofactors for an NRPS PCP domain. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is computational pattern-based rather than a direct experimental cofactor measurement. The annotation is consistent with NRPS biochemistry but is not an independent experimental determination of the cofactor for this specific enzyme.",
    "The protein is described as a 'non-canonical' NRPS, which could in principle imply unusual cofactor requirements, but the presence of the PP-binding motif in the sequence supports the standard NRPS cofactor assignment.",
    "The PP-binding motif in this sequence ('GGTGFVGA', 'GGSCAPMDP') is a variant of the canonical 'GxDSL' motif; recognizing these variants requires familiarity with the diversity of PP-binding motifs across NRPS/FAS families."
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
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:47942\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00258\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"pantetheine 4'-phosphate\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
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
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00258};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
