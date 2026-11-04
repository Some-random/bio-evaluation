# pathway_0097

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0097.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Protein biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSDSQQSVEVLNQLLARLSVATPDNRDEVATEVSSFVNGNIIEHDAPEHFFNGLAKAIKDKKSAVNALAAVSHVASTSGLAPSVEPYVVALVPAILEQTGSKDKDVQSAANAALHAVVTAVNPVAVKAVLPHLTKSLSETNKWQEKVAVLSAISALVDQAKSQISLRMTELIPVLSEAMWDTKKEVKNAATATMTKATETVENKDIERFIPKLIECIANPSEVPETVHLLGATTFVAEVTPATLSIMTPLLSRGLAERETPIKRKSAVIIDNMCKLVEDPQIVAPFLNKLLPGLKNNFSVIADPEAREVTLRGLKTLRRVGAVGEGDVLPEISHAGDPATTLGVLDSLLKTENIAKKFRPAVEYISCIGGDLIDERIIDQQTWFTHVLPYMTIFLHQNQAKEILDEFRKRAVDNIPEPPKFDDEEEEGEDLCNCEFSLAYGAKILLNRTQLRLKRGRRYGLCGPNGSGKSTLMRAIANGQVDGFPSQEECRTVYVEHDIDGTHAETSVLDFVFQGDVGTKEAISAKLKEFGFDDEMIVMPIAALSGGWKMKLALARAVLKNADILLLDEPTNHLDTVNVAWLTNYLITCGITSIVVSHDSGFLDNICQYIIHYEGLKLRKYKGNLSALVERVPSAKSYYELGASDLEFRFPEPGYLEGVKTKQKAIVKVSNMTFQYPGTSKPQISDVSFQCSLSSRIAVIGPNGAGKSTLINVLTGELLPTTGEVYTHENIRIAYIKQHAFAHIESHLDKTPSEYIQWRFQTGEDRETMDRANRQINEDDAQAMNKIFKIDGTPRRIAGIHSRRKFKNSYEYECSFLLGENIGMKSERWVPMMSVDNAWLPRGEVIESHGKMVAEVDMKEALASGQFRPLTRKEIEEHCAMLGLDAELVSHSRIRGLSGGQKVKLVLAAGTWQRPHLIVLDEPTNYLDRDSLGALSKALKEFEGGVIIITHSAEFTKDLTEEVWAVRDGLMTPSGHNWVSGQGSGPRLEKKEDEEDKFDAMGNKISSGTKKTKLSSAELRKKKKERMKKKKELGDAYVSDDDADF

[Multiple Choices]
A. Antifungal biosynthesis. .
B. One-carbon metabolism
C. chorismate biosynthesis
D. Protein biosynthesis
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record identifies the protein as elongation factor 3 and annotates its pathway as protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred by similarity (ECO:0000250), rather than presented as direct experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a large protein with two tandem P-loop ATPase domains, including repeated glycine-rich nucleotide-binding motifs. That architecture is characteristic of fungal elongation factor 3, a translation elongation factor. Recognizing this family-level pattern supports protein biosynthesis over the offered biosynthetic and one-carbon metabolism alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable family and domain-architecture inference meaningfully distinguishes the pathway among these choices; identifying the exact target's database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, protein biosynthesis is the clear pathway match for an elongation factor.


### Important caveats

- The reviewer-only pathway annotation is similarity-transferred, not direct experimental proof.
- The sequence-matched source record supports the expected answer, but its target-specific annotation was not part of the original inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a large protein with two tandem P-loop ATPase domains, including repeated glycine-rich nucleotide-binding motifs. That architecture is characteristic of fungal elongation factor 3, a translation elongation factor. Recognizing this family-level pattern supports protein biosynthesis over the offered biosynthetic and one-carbon metabolism alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable family and domain-architecture inference meaningfully distinguishes the pathway among these choices; identifying the exact target's database record is not necessary."
  },
  "case_id": "pathway_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as elongation factor 3 and annotates its pathway as protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred by similarity (ECO:0000250), rather than presented as direct experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only pathway annotation is similarity-transferred, not direct experimental proof.",
    "The sequence-matched source record supports the expected answer, but its target-specific annotation was not part of the original inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, protein biosynthesis is the clear pathway match for an elongation factor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as elongation factor 3 and annotates its pathway as protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred by similarity (ECO:0000250), rather than presented as direct experimental evidence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a large protein with two tandem P-loop ATPase domains, including repeated glycine-rich nucleotide-binding motifs. That architecture is characteristic of fungal elongation factor 3, a translation elongation factor. Recognizing this family-level pattern supports protein biosynthesis over the offered biosynthetic and one-carbon metabolism alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A transferable family and domain-architecture inference meaningfully distinguishes the pathway among these choices; identifying the exact target's database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, protein biosynthesis is the clear pathway match for an elongation factor."
  },
  "important_caveats": [
    "The reviewer-only pathway annotation is similarity-transferred, not direct experimental proof.",
    "The sequence-matched source record supports the expected answer, but its target-specific annotation was not part of the original inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C4, C5, H1, H2) identifies this protein as Elongation Factor 3 (eEF3) and explicitly assigns the pathway 'Protein biosynthesis; polypeptide chain elongation.' The protein is a translation elongation factor, which is a direct component of the protein biosynthesis pathway. The evidence is consistent and the sequence matches the annotated entry.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two distinct ABC-type ATPase domains, each with a canonical Walker A motif (GPGSGKST at ~position 530 and GPNAGKST at ~position 680) and a Walker B motif (DEPTNHLDT and DEPTNYLDR). The presence of two such domains connected by a linker region, with no transmembrane helices, is the hallmark architecture of Eukaryotic Elongation Factor 3 (eEF3), a fungal-specific translation factor. This is a well-documented family signature: eEF3 uses its tandem ABC domains to stimulate EF-1-dependent aminoacyl-tRNA binding at the ribosomal A-site during translation. Recognizing the double-ABC-domain architecture (without TM segments) as eEF3 rather than a generic ABC transporter or other ATPase maps directly to translation/protein biosynthesis. The alternatives are clearly distinguishable: antifungal biosynthesis involves polyketide synthases or NRPS enzymes; one-carbon metabolism involves folate/methionine cycle enzymes; chorismate biosynthesis involves shikimate-pathway enzymes (DAHP synthase, shikimate kinase, chorismate synthase) — none of which have double-ABC-domain architecture.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the tandem Walker A/B motifs as ABC-type ATPase domains, note the absence of transmembrane helices (ruling out transporters), and connect the distinctive double-ABC-domain architecture to the eEF3 family of translation factors. This family-level inference from domain architecture is transferable knowledge about protein families and does not require memorizing the specific UniProt entry for this exact sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent clearly distinct biological processes. The double-ABC-domain architecture without transmembrane segments is incompatible with antifungal biosynthesis (polyketide/NRPS), one-carbon metabolism (folate enzymes), or chorismate biosynthesis (shikimate pathway enzymes). Only protein biosynthesis (translation elongation) is consistent with the observed domain architecture.


### Important caveats

- The UniProt pathway annotation carries evidence code ECO:0000250 (inferred by similarity to O93796), meaning it is computationally transferred rather than experimentally validated for this specific organism. However, eEF3's role in translation is well-established across fungi.
- ABC-type domains are found in many protein families; the key distinguishing feature is the tandem double-domain architecture without transmembrane segments, which specifically points to eEF3 rather than generic ABC transporters.
- The protein is from Zygosaccharomyces rouxii (a yeast), and eEF3 is fungal-specific, which further supports the translation-factor interpretation over alternative ABC-domain proteins.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two distinct ABC-type ATPase domains, each with a canonical Walker A motif (GPGSGKST at ~position 530 and GPNAGKST at ~position 680) and a Walker B motif (DEPTNHLDT and DEPTNYLDR). The presence of two such domains connected by a linker region, with no transmembrane helices, is the hallmark architecture of Eukaryotic Elongation Factor 3 (eEF3), a fungal-specific translation factor. This is a well-documented family signature: eEF3 uses its tandem ABC domains to stimulate EF-1-dependent aminoacyl-tRNA binding at the ribosomal A-site during translation. Recognizing the double-ABC-domain architecture (without TM segments) as eEF3 rather than a generic ABC transporter or other ATPase maps directly to translation/protein biosynthesis. The alternatives are clearly distinguishable: antifungal biosynthesis involves polyketide synthases or NRPS enzymes; one-carbon metabolism involves folate/methionine cycle enzymes; chorismate biosynthesis involves shikimate-pathway enzymes (DAHP synthase, shikimate kinase, chorismate synthase) — none of which have double-ABC-domain architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the tandem Walker A/B motifs as ABC-type ATPase domains, note the absence of transmembrane helices (ruling out transporters), and connect the distinctive double-ABC-domain architecture to the eEF3 family of translation factors. This family-level inference from domain architecture is transferable knowledge about protein families and does not require memorizing the specific UniProt entry for this exact sequence."
  },
  "case_id": "pathway_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C4, C5, H1, H2) identifies this protein as Elongation Factor 3 (eEF3) and explicitly assigns the pathway 'Protein biosynthesis; polypeptide chain elongation.' The protein is a translation elongation factor, which is a direct component of the protein biosynthesis pathway. The evidence is consistent and the sequence matches the annotated entry."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000250 (inferred by similarity to O93796), meaning it is computationally transferred rather than experimentally validated for this specific organism. However, eEF3's role in translation is well-established across fungi.",
    "ABC-type domains are found in many protein families; the key distinguishing feature is the tandem double-domain architecture without transmembrane segments, which specifically points to eEF3 rather than generic ABC transporters.",
    "The protein is from Zygosaccharomyces rouxii (a yeast), and eEF3 is fungal-specific, which further supports the translation-factor interpretation over alternative ABC-domain proteins."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct biological processes. The double-ABC-domain architecture without transmembrane segments is incompatible with antifungal biosynthesis (polyketide/NRPS), one-carbon metabolism (folate enzymes), or chorismate biosynthesis (shikimate pathway enzymes). Only protein biosynthesis (translation elongation) is consistent with the observed domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C4, C5, H1, H2) identifies this protein as Elongation Factor 3 (eEF3) and explicitly assigns the pathway 'Protein biosynthesis; polypeptide chain elongation.' The protein is a translation elongation factor, which is a direct component of the protein biosynthesis pathway. The evidence is consistent and the sequence matches the annotated entry.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two distinct ABC-type ATPase domains, each with a canonical Walker A motif (GPGSGKST at ~position 530 and GPNAGKST at ~position 680) and a Walker B motif (DEPTNHLDT and DEPTNYLDR). The presence of two such domains connected by a linker region, with no transmembrane helices, is the hallmark architecture of Eukaryotic Elongation Factor 3 (eEF3), a fungal-specific translation factor. This is a well-documented family signature: eEF3 uses its tandem ABC domains to stimulate EF-1-dependent aminoacyl-tRNA binding at the ribosomal A-site during translation. Recognizing the double-ABC-domain architecture (without TM segments) as eEF3 rather than a generic ABC transporter or other ATPase maps directly to translation/protein biosynthesis. The alternatives are clearly distinguishable: antifungal biosynthesis involves polyketide synthases or NRPS enzymes; one-carbon metabolism involves folate/methionine cycle enzymes; chorismate biosynthesis involves shikimate-pathway enzymes (DAHP synthase, shikimate kinase, chorismate synthase) — none of which have double-ABC-domain architecture.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the tandem Walker A/B motifs as ABC-type ATPase domains, note the absence of transmembrane helices (ruling out transporters), and connect the distinctive double-ABC-domain architecture to the eEF3 family of translation factors. This family-level inference from domain architecture is transferable knowledge about protein families and does not require memorizing the specific UniProt entry for this exact sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct biological processes. The double-ABC-domain architecture without transmembrane segments is incompatible with antifungal biosynthesis (polyketide/NRPS), one-carbon metabolism (folate enzymes), or chorismate biosynthesis (shikimate pathway enzymes). Only protein biosynthesis (translation elongation) is consistent with the observed domain architecture."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000250 (inferred by similarity to O93796), meaning it is computationally transferred rather than experimentally validated for this specific organism. However, eEF3's role in translation is well-established across fungi.",
    "ABC-type domains are found in many protein families; the key distinguishing feature is the tandem double-domain architecture without transmembrane segments, which specifically points to eEF3 rather than generic ABC transporters.",
    "The protein is from Zygosaccharomyces rouxii (a yeast), and eEF3 is fungal-specific, which further supports the translation-factor interpretation over alternative ABC-domain proteins."
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
  "benchmark_sequence_length": 1045,
  "benchmark_sequence_sha256": "094f94f39d6a8f23eb2de3d8e4d1b9f242225c1d6c58b3aaf95af78970917f8f",
  "current_entry_audit": {
    "entryVersion": 93,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-07-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1045,
  "current_source_sequence_sha256": "094f94f39d6a8f23eb2de3d8e4d1b9f242225c1d6c58b3aaf95af78970917f8f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 92,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C5E4D9",
  "selected_historical_entry_version": 92,
  "selected_historical_record_sha256": "24912b3780dfdc2175cd526300f2f38c8d113474ab82078ce32761e3bafbca36",
  "selected_historical_source_sequence_length": 1045,
  "selected_historical_source_sequence_sha256": "094f94f39d6a8f23eb2de3d8e4d1b9f242225c1d6c58b3aaf95af78970917f8f",
  "selected_historical_version": {
    "accession": "C5E4D9",
    "database": "Swiss-Prot",
    "entryVersion": 92,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "EF3_ZYGRC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C5E4D9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:30.729914+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14",
  "url": "https://rest.uniprot.org/uniprotkb/C5E4D9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":93,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-07-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:30.729914+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14",
  "url": "https://rest.uniprot.org/uniprotkb/C5E4D9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008536\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Saccharomycetes\",\"Saccharomycetales\",\"Saccharomycetaceae\",\"Zygosaccharomyces\"],\"scientificName\":\"Zygosaccharomyces rouxii (strain ATCC 2623 / CBS 732 / NBRC 1130 / NCYC 568 / NRRL Y-229)\",\"taxonId\":559307}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:30.729914+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14",
  "url": "https://rest.uniprot.org/uniprotkb/C5E4D9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Eukaryotic elongation factor 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"eEF3\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P16521\",\"source\":\"UniProtKB\"}],\"value\":\"3.6.4.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Elongation factor 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"EF-3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:30.729914+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14",
  "url": "https://rest.uniprot.org/uniprotkb/C5E4D9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93796\",\"source\":\"UniProtKB\"}],\"value\":\"Protein biosynthesis; polypeptide chain elongation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:27:30.729914+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14",
  "url": "https://rest.uniprot.org/uniprotkb/C5E4D9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5E4D9?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H1",
  "excerpt": "ID   EF3_ZYGRC               Reviewed;        1045 AA.\nAC   C5E4D9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-JUL-2009, sequence version 1.\nDT   28-JAN-2026, entry version 92.\nDE   RecName: Full=Elongation factor 3 {ECO:0000305};\nDE            Short=EF-3 {ECO:0000305};\nDE            EC=3.6.4.- {ECO:0000250|UniProtKB:P16521};\nDE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};\nDE            Short=eEF3 {ECO:0000305};\nGN   Name=TEF3 {ECO:0000305};\nGN   OrderedLocusNames=ZYRO0E05148g {ECO:0000312|EMBL:CAR30900.1};\nOS   Zygosaccharomyces rouxii (strain ATCC 2623 / CBS 732 / NBRC 1130 / NCYC 568\nOS   / NRRL Y-229).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Saccharomycetes;\nOC   Saccharomycetales; Saccharomycetaceae; Zygosaccharomyces.\nOX   NCBI_TaxID=559307 {ECO:0000312|Proteomes:UP000008536};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:35.219574+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "24912b3780dfdc2175cd526300f2f38c8d113474ab82078ce32761e3bafbca36",
  "url": "https://rest.uniprot.org/unisave/C5E4D9?format=txt&versions=92"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5E4D9?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H2",
  "excerpt": "CC   -!- PATHWAY: Protein biosynthesis; polypeptide chain elongation.\nCC       {ECO:0000250|UniProtKB:O93796}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:35.219574+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "24912b3780dfdc2175cd526300f2f38c8d113474ab82078ce32761e3bafbca36",
  "url": "https://rest.uniprot.org/unisave/C5E4D9?format=txt&versions=92"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
