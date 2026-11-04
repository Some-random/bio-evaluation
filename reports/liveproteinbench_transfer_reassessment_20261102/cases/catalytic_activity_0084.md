# catalytic_activity_0084

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0084.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — okaramine C + 2 reduced &#91;NADPH--hemoprotein reductase&#93; + 2 O2 = okaramine A + 2 oxidized &#91;NADPH--hemoprotein reductase&#93; + 4 H2O + 2 H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLLRPAKYQLPLPPGPRGLPIIGNLHQAPKEKAWEVYKQWSDRYGPIMSVNNGGMITIIVSSHEVVKNFLEKNNAVFSSRPQLLVLERALYGFTTPALPYGEKWLKHRALRGAVLKPAMAVRYRGLQDLESKQLLRDLLYSEDFTQCMRRQAASLFLGIAYGNRFPEETPEIIDIDQAVAQLGGISESMFQGTGMLREFFPVLKYFPGYDKFLKQLDDVGERLANIYVRRFRDGLSTPAWNWAKEYSKRPEAQGMGELELSFCIGSTYQASLTPYEILRIILLAAICHPEEKARLQKEIDLVVGKDNLPGWEHKDRIQFVQAFIYEALRWHAFSPLGAPRAVSRDIEYKGYFIPKGATLVLNQWAMDHDENVYDNPFTFRPQRWIDNPDLPHVIFGFGLRGCPGQHLARDHLFINTARLFWAFNFGNAYENGKKVELDLDELMQPRGGGSAFNQVPSFKASVIIRSSERRQIVENEWDAVEKDEQKILAEAMPLPE

[Multiple Choices]
A. an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)
B. okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)
C. 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)
D. 2'-hydroxy-2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2',2'-dihydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
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

> The sequence matches the reviewed UniProt entry annotating this protein as cytochrome P450 monooxygenase OkaD, with the okaramine C-to-A reaction supported by an ECO:0000269 citation to PubMed 28631282. This supports the keyed reaction for the supplied sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the characteristic P450 heme-binding motif, approximately FxxGxxxCxG, in the segment FGFGLRGCPG. P450s are oxygen-activating monooxygenases; among these choices, B is the P450-like reaction, using O2 and a reductase electron donor. A is a dolichol-linked glycan transfer, C is hydrolysis, and D specifies a ferredoxin-dependent reaction. This family-level inference meaningfully favors B, though it does not independently establish the exact okaramine substrate and product.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A conserved P450 sequence feature and transferable knowledge of P450 chemistry distinguish B from the offered alternatives without needing the exact protein's recorded annotation. The specific substrate transformation is more specialized than the family inference, but the choices make the P450-compatible option distinctive.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct reaction types and electron-donor systems; the P450 motif supports B over the other listed choices.


### Important caveats

- The exact okaramine C-to-A transformation is not derivable from the P450 motif alone; the motif supports the enzyme-family and reaction-class inference.
- The reviewer-only annotation cites experimental evidence, but the underlying publication was not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the characteristic P450 heme-binding motif, approximately FxxGxxxCxG, in the segment FGFGLRGCPG. P450s are oxygen-activating monooxygenases; among these choices, B is the P450-like reaction, using O2 and a reductase electron donor. A is a dolichol-linked glycan transfer, C is hydrolysis, and D specifies a ferredoxin-dependent reaction. This family-level inference meaningfully favors B, though it does not independently establish the exact okaramine substrate and product.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A conserved P450 sequence feature and transferable knowledge of P450 chemistry distinguish B from the offered alternatives without needing the exact protein's recorded annotation. The specific substrate transformation is more specialized than the family inference, but the choices make the P450-compatible option distinctive."
  },
  "case_id": "catalytic_activity_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the reviewed UniProt entry annotating this protein as cytochrome P450 monooxygenase OkaD, with the okaramine C-to-A reaction supported by an ECO:0000269 citation to PubMed 28631282. This supports the keyed reaction for the supplied sequence."
  },
  "important_caveats": [
    "The exact okaramine C-to-A transformation is not derivable from the P450 motif alone; the motif supports the enzyme-family and reaction-class inference.",
    "The reviewer-only annotation cites experimental evidence, but the underlying publication was not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction types and electron-donor systems; the P450 motif supports B over the other listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the reviewed UniProt entry annotating this protein as cytochrome P450 monooxygenase OkaD, with the okaramine C-to-A reaction supported by an ECO:0000269 citation to PubMed 28631282. This supports the keyed reaction for the supplied sequence.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the characteristic P450 heme-binding motif, approximately FxxGxxxCxG, in the segment FGFGLRGCPG. P450s are oxygen-activating monooxygenases; among these choices, B is the P450-like reaction, using O2 and a reductase electron donor. A is a dolichol-linked glycan transfer, C is hydrolysis, and D specifies a ferredoxin-dependent reaction. This family-level inference meaningfully favors B, though it does not independently establish the exact okaramine substrate and product.",
    "missing_item_specific_fact": "",
    "reason": "A conserved P450 sequence feature and transferable knowledge of P450 chemistry distinguish B from the offered alternatives without needing the exact protein's recorded annotation. The specific substrate transformation is more specialized than the family inference, but the choices make the P450-compatible option distinctive."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction types and electron-donor systems; the P450 motif supports B over the other listed choices."
  },
  "important_caveats": [
    "The exact okaramine C-to-A transformation is not derivable from the P450 motif alone; the motif supports the enzyme-family and reaction-class inference.",
    "The reviewer-only annotation cites experimental evidence, but the underlying publication was not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A2Z5U6I9 (OKAD_PENOH) explicitly annotates the catalytic activity as 'okaramine C + 2 reduced &#91;NADPH--hemoprotein reductase&#93; + 2 O2 = okaramine A + 2 oxidized &#91;NADPH--hemoprotein reductase&#93; + 4 H2O + 2 H(+)', matching choice B verbatim. The annotation carries ECO:0000269 (experimental evidence) from PubMed:28631282 (Lai et al., Angew. Chem. Int. Ed. 2017). The sequence in the benchmark matches the UniProt entry (SHA-256 match confirmed).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical P450 heme-binding motif (FGFGLRGCPG, matching FxxGxxxCxG) identifying it as a cytochrome P450 monooxygenase. The N-terminal ~28 residues (MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLLRPAKY) form a hydrophobic signal peptide typical of ER-membrane-associated fungal P450s. Transferable knowledge establishes that fungal ER P450s receive electrons from NADPH-cytochrome P450 reductase (a hemoprotein reductase), whereas ferredoxin-dependent P450s are localized to chloroplasts (plant carotenoid hydroxylases) or mitochondria. Among the four choices: A is a glycosyltransferase reaction (eliminated—wrong enzyme class); C is a hydrolase/esterase reaction (eliminated—wrong enzyme class); D is a P450 reaction but uses &#91;2Fe-2S&#93;-ferredoxin as electron donor, characteristic of chloroplast P450s, inconsistent with the ER signal peptide; B is a P450 reaction using NADPH--hemoprotein reductase, consistent with a fungal ER P450. Thus B is uniquely selected by the combination of P450 identification and subcellular-localization-based electron-donor inference, without needing to know the specific substrate name 'okaramine C'.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the P450 from the heme-binding motif, recognize the ER signal peptide, apply the well-established rule that fungal ER P450s use NADPH-cytochrome P450 reductase (not ferredoxin), and eliminate choices A, C, and D on mechanistic grounds. The specific substrate label 'okaramine C' need not be known because it is the only P450 reaction with the correct electron-donor partner among the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A and C are non-P450 reactions and are clearly eliminated. Choice D, while a P450 reaction, uses ferredoxin as electron donor—a hallmark of chloroplast P450s—contradicted by the ER signal peptide. Only B remains consistent with a fungal ER P450.


### Important caveats

- The specific substrate 'okaramine C' is an obscure secondary metabolite; a model unfamiliar with okaramines would rely entirely on the electron-donor/localization argument to select B over D.
- The signal peptide inference (ER localization → NADPH-reductase partner) is a strong but not absolute rule; some fungal P450s use alternative redox partners. However, among the four offered choices, the distinction is clear.
- The annotation evidence (ECO:0000269) is from a 2017 experimental study (Lai et al.), confirming the reaction was experimentally characterized rather than purely inferred.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical P450 heme-binding motif (FGFGLRGCPG, matching FxxGxxxCxG) identifying it as a cytochrome P450 monooxygenase. The N-terminal ~28 residues (MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLLRPAKY) form a hydrophobic signal peptide typical of ER-membrane-associated fungal P450s. Transferable knowledge establishes that fungal ER P450s receive electrons from NADPH-cytochrome P450 reductase (a hemoprotein reductase), whereas ferredoxin-dependent P450s are localized to chloroplasts (plant carotenoid hydroxylases) or mitochondria. Among the four choices: A is a glycosyltransferase reaction (eliminated—wrong enzyme class); C is a hydrolase/esterase reaction (eliminated—wrong enzyme class); D is a P450 reaction but uses [2Fe-2S]-ferredoxin as electron donor, characteristic of chloroplast P450s, inconsistent with the ER signal peptide; B is a P450 reaction using NADPH--hemoprotein reductase, consistent with a fungal ER P450. Thus B is uniquely selected by the combination of P450 identification and subcellular-localization-based electron-donor inference, without needing to know the specific substrate name 'okaramine C'.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the P450 from the heme-binding motif, recognize the ER signal peptide, apply the well-established rule that fungal ER P450s use NADPH-cytochrome P450 reductase (not ferredoxin), and eliminate choices A, C, and D on mechanistic grounds. The specific substrate label 'okaramine C' need not be known because it is the only P450 reaction with the correct electron-donor partner among the offered alternatives."
  },
  "case_id": "catalytic_activity_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A2Z5U6I9 (OKAD_PENOH) explicitly annotates the catalytic activity as 'okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)', matching choice B verbatim. The annotation carries ECO:0000269 (experimental evidence) from PubMed:28631282 (Lai et al., Angew. Chem. Int. Ed. 2017). The sequence in the benchmark matches the UniProt entry (SHA-256 match confirmed)."
  },
  "important_caveats": [
    "The specific substrate 'okaramine C' is an obscure secondary metabolite; a model unfamiliar with okaramines would rely entirely on the electron-donor/localization argument to select B over D.",
    "The signal peptide inference (ER localization → NADPH-reductase partner) is a strong but not absolute rule; some fungal P450s use alternative redox partners. However, among the four offered choices, the distinction is clear.",
    "The annotation evidence (ECO:0000269) is from a 2017 experimental study (Lai et al.), confirming the reaction was experimentally characterized rather than purely inferred."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and C are non-P450 reactions and are clearly eliminated. Choice D, while a P450 reaction, uses ferredoxin as electron donor—a hallmark of chloroplast P450s—contradicted by the ER signal peptide. Only B remains consistent with a fungal ER P450."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A2Z5U6I9 (OKAD_PENOH) explicitly annotates the catalytic activity as 'okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)', matching choice B verbatim. The annotation carries ECO:0000269 (experimental evidence) from PubMed:28631282 (Lai et al., Angew. Chem. Int. Ed. 2017). The sequence in the benchmark matches the UniProt entry (SHA-256 match confirmed).",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical P450 heme-binding motif (FGFGLRGCPG, matching FxxGxxxCxG) identifying it as a cytochrome P450 monooxygenase. The N-terminal ~28 residues (MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLLRPAKY) form a hydrophobic signal peptide typical of ER-membrane-associated fungal P450s. Transferable knowledge establishes that fungal ER P450s receive electrons from NADPH-cytochrome P450 reductase (a hemoprotein reductase), whereas ferredoxin-dependent P450s are localized to chloroplasts (plant carotenoid hydroxylases) or mitochondria. Among the four choices: A is a glycosyltransferase reaction (eliminated—wrong enzyme class); C is a hydrolase/esterase reaction (eliminated—wrong enzyme class); D is a P450 reaction but uses [2Fe-2S]-ferredoxin as electron donor, characteristic of chloroplast P450s, inconsistent with the ER signal peptide; B is a P450 reaction using NADPH--hemoprotein reductase, consistent with a fungal ER P450. Thus B is uniquely selected by the combination of P450 identification and subcellular-localization-based electron-donor inference, without needing to know the specific substrate name 'okaramine C'.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the P450 from the heme-binding motif, recognize the ER signal peptide, apply the well-established rule that fungal ER P450s use NADPH-cytochrome P450 reductase (not ferredoxin), and eliminate choices A, C, and D on mechanistic grounds. The specific substrate label 'okaramine C' need not be known because it is the only P450 reaction with the correct electron-donor partner among the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and C are non-P450 reactions and are clearly eliminated. Choice D, while a P450 reaction, uses ferredoxin as electron donor—a hallmark of chloroplast P450s—contradicted by the ER signal peptide. Only B remains consistent with a fungal ER P450."
  },
  "important_caveats": [
    "The specific substrate 'okaramine C' is an obscure secondary metabolite; a model unfamiliar with okaramines would rely entirely on the electron-donor/localization argument to select B over D.",
    "The signal peptide inference (ER localization → NADPH-reductase partner) is a strong but not absolute rule; some fungal P450s use alternative redox partners. However, among the four offered choices, the distinction is clear.",
    "The annotation evidence (ECO:0000269) is from a 2017 experimental study (Lai et al.), confirming the reaction was experimentally characterized rather than purely inferred."
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
  "benchmark_sequence_length": 529,
  "benchmark_sequence_sha256": "99280cdea8196dec317d2f18830c1825fab94ad5dea0f68ec9b853bab5214ffd",
  "current_entry_audit": {
    "entryVersion": 24,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-10-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 529,
  "current_source_sequence_sha256": "99280cdea8196dec317d2f18830c1825fab94ad5dea0f68ec9b853bab5214ffd",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 23,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2Z5U6I9",
  "selected_historical_entry_version": 23,
  "selected_historical_record_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "selected_historical_source_sequence_length": 529,
  "selected_historical_source_sequence_sha256": "99280cdea8196dec317d2f18830c1825fab94ad5dea0f68ec9b853bab5214ffd",
  "selected_historical_version": {
    "accession": "A0A2Z5U6I9",
    "database": "Swiss-Prot",
    "entryVersion": 23,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "OKAD_PENOH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2Z5U6I9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":24,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-10-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Penicillium\"],\"scientificName\":\"Penicillium ochrochloron\",\"taxonId\":69780}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"Okaramines biosynthesis cluster protein D\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"1.14.99.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase okaD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82704\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"name\":\"okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82703\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:193028\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232464\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lai C.Y.\",\"Lo I.W.\",\"Hewage R.T.\",\"Chen Y.C.\",\"Chen C.T.\",\"Lee C.F.\",\"Lin S.\",\"Tang M.C.\",\"Lin H.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28631282\"},{\"database\":\"DOI\",\"id\":\"10.1002/anie.201705501\"}],\"citationType\":\"journal article\",\"firstPage\":\"9478\",\"id\":\"28631282\",\"journal\":\"Angew. Chem. Int. Ed.\",\"lastPage\":\"9482\",\"publicationDate\":\"2017\",\"title\":\"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise Pathway of Okaramines.\",\"volume\":\"56\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H1",
  "excerpt": "ID   OKAD_PENOH              Reviewed;         529 AA.\nAC   A0A2Z5U6I9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-OCT-2018, sequence version 1.\nDT   28-JAN-2026, entry version 23.\nDE   RecName: Full=Cytochrome P450 monooxygenase okaD {ECO:0000303|PubMed:28631282};\nDE            EC=1.14.99.- {ECO:0000269|PubMed:28631282};\nDE   AltName: Full=Okaramines biosynthesis cluster protein D {ECO:0000303|PubMed:28631282};\nGN   Name=okaD {ECO:0000303|PubMed:28631282};\nOS   Penicillium ochrochloron.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.\nOX   NCBI_TaxID=69780;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cytochrome P450 monooxygenase okaD {ECO:0000303|PubMed:28631282};\nDE            EC=1.14.99.- {ECO:0000269|PubMed:28631282};\nDE   AltName: Full=Okaramines biosynthesis cluster protein D {ECO:0000303|PubMed:28631282};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=28631282; DOI=10.1002/anie.201705501;\nRA   Lai C.Y., Lo I.W., Hewage R.T., Chen Y.C., Chen C.T., Lee C.F., Lin S.,\nRA   Tang M.C., Lin H.C.;\nRT   \"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise\nRT   Pathway of Okaramines.\";\nRL   Angew. Chem. Int. Ed. 56:9478-9482(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2\nCC         = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2\nCC         H(+); Xref=Rhea:RHEA:82703, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:193028,\nCC         ChEBI:CHEBI:232464; Evidence={ECO:0000269|PubMed:28631282};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82704;\nCC         Evidence={ECO:0000269|PubMed:28631282};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
