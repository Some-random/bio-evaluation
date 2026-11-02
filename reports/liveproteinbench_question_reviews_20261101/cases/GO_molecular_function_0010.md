# GO_molecular_function_0010

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — cysteine desulfurase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | uncertain | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNGNQIKQLKKLYRHILNEASKFENINYNVYFSNKAKEKFREFCSDTNFESEKLKTFQNECWDYLNMLKRQTIIHNLYHVDKPLVNK

[Multiple Choices]
A. sodium channel inhibitor activity
B. cysteine desulfurase activity
C. DNA nuclease activity
D. histone H3K18 acetyltransferase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: uncertain

> The sequence-matched annotation says Isd11 enhances the cysteine desulfurase activity of IscS; it does not establish that Isd11 itself catalyzes that reaction. Thus B is related to the protein's role but is not supported as its own molecular activity by the supplied evidence.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a short, 87-residue protein, which makes several listed catalytic activities less plausible, but that broad size-based reasoning does not identify its specific role or establish cysteine desulfurase catalysis.


**Missing item-specific fact**

> The needed fact is that this sequence is Isd11, an accessory protein that participates in Fe-S cluster biogenesis and enhances IscS activity, rather than an identified cysteine-desulfurase enzyme.


**Reason**

> Distinguishing the closest option requires protein-specific identification and functional annotation or experimental evidence not supplied with the sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No option is established as Isd11's own molecular activity by the supplied evidence. B is the closest association, but enhancing another protein's activity is not the same as possessing that catalytic activity.


### Important caveats

- The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.
- The cited functional annotation reports enhancement of IscS cysteine desulfurase activity; it does not independently establish that Isd11 lacks every possible catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a short, 87-residue protein, which makes several listed catalytic activities less plausible, but that broad size-based reasoning does not identify its specific role or establish cysteine desulfurase catalysis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The needed fact is that this sequence is Isd11, an accessory protein that participates in Fe-S cluster biogenesis and enhances IscS activity, rather than an identified cysteine-desulfurase enzyme.",
    "reason": "Distinguishing the closest option requires protein-specific identification and functional annotation or experimental evidence not supplied with the sequence and choices."
  },
  "case_id": "GO_molecular_function_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "cannot_determine",
    "reason": "The sequence-matched annotation says Isd11 enhances the cysteine desulfurase activity of IscS; it does not establish that Isd11 itself catalyzes that reaction. Thus B is related to the protein's role but is not supported as its own molecular activity by the supplied evidence."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited functional annotation reports enhancement of IscS cysteine desulfurase activity; it does not independently establish that Isd11 lacks every possible catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No option is established as Isd11's own molecular activity by the supplied evidence. B is the closest association, but enhancing another protein's activity is not the same as possessing that catalytic activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0010",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The sequence-matched annotation says Isd11 enhances the cysteine desulfurase activity of IscS; it does not establish that Isd11 itself catalyzes that reaction. Thus B is related to the protein's role but is not supported as its own molecular activity by the supplied evidence.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a short, 87-residue protein, which makes several listed catalytic activities less plausible, but that broad size-based reasoning does not identify its specific role or establish cysteine desulfurase catalysis.",
    "missing_item_specific_fact": "The needed fact is that this sequence is Isd11, an accessory protein that participates in Fe-S cluster biogenesis and enhances IscS activity, rather than an identified cysteine-desulfurase enzyme.",
    "reason": "Distinguishing the closest option requires protein-specific identification and functional annotation or experimental evidence not supplied with the sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No option is established as Isd11's own molecular activity by the supplied evidence. B is the closest association, but enhancing another protein's activity is not the same as possessing that catalytic activity."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited functional annotation reports enhancement of IscS cysteine desulfurase activity; it does not independently establish that Isd11 lacks every possible catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: contradicted

> The UniProt entry Q8IEK7 (Protein Isd11, P. falciparum) explicitly states its function as 'Participates in iron-sulfur cluster formation (ISC) pathway... Enhances cysteine desulfurase activity of IscS.' The GO term GO:0031071 (cysteine desulfurase activity) is defined as 'Catalysis of the reaction: L-cysteine + &#91;enzyme&#93;-cysteine = L-alanine + &#91;enzyme&#93;-S-sulfanylcysteine,' which is the catalytic activity of IscS/NFS1, not Isd11. Isd11 is a 87-aa accessory/stimulatory subunit that enhances IscS activity but does not itself catalyze the desulfurase reaction. The UniProt GO annotations for this entry include GO:0005198 (structural molecule activity, IBA) and GO:0016740 (transferase activity, IEA), but NOT GO:0031071. Attributing 'cysteine desulfurase activity' to Isd11 conflates the regulatory/accessory subunit with the catalytic enzyme it stimulates.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> None meaningfully available from the sequence. The 87-aa protein lacks PLP-binding motifs characteristic of cysteine desulfurases (IscS/NFS1 are ~400+ aa enzymes), lacks catalytic motifs of DNA nucleases (e.g., PD-(D/E)xK), lacks GNAT/MYST acetyltransferase motifs, and lacks the conotoxin-like disulfide-stabilized scaffold of sodium channel inhibitors. In fact, the very small size of the protein argues AGAINST it being a desulfurase. No sequence feature distinguishes it as an ISC-complex accessory protein.


**Missing item-specific fact**

> Knowledge that this specific 87-aa sequence corresponds to Isd11 of Plasmodium falciparum, and that Isd11 is an accessory subunit of the ISC desulfurase complex (even this association does not justify assigning the catalytic GO term to Isd11 itself).


**Reason**

> The sequence provides no distinctive catalytic or structural motifs that would allow a model to select among the four options through general biological reasoning. Selection of B requires recognizing the exact sequence as Isd11 and knowing its association with the ISC desulfurase complex — a protein-specific database fact. Moreover, even with that knowledge, the correct molecular function annotation would be 'enhances desulfurase activity' rather than 'cysteine desulfurase activity' itself.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B (if one loosely equates 'enhances desulfurase activity' with 'has desulfurase activity')"
]
```

> Strictly, none of the four options accurately describe Isd11's molecular function. The protein's actual function is as an accessory/stimulatory subunit of the ISC complex. If forced to choose, B is the closest thematic match (ISC pathway involvement), but it misattributes the catalytic activity of IscS to Isd11. The other three options (A, C, D) have no association whatsoever with this protein. The question is ambiguous in that the 'correct' answer requires accepting an inaccurate GO assignment.


### Important caveats

- The UniProt entry was first integrated into Swiss-Prot on 2025-04-09; the benchmark author's source snapshot date is unknown. If the benchmark was constructed before this Swiss-Prot integration, the annotation basis may differ.
- The Reactome pathway 'FXN:NFS1:ISD11:ISCU assembles 2Fe-2S iron-sulfur cluster' includes ISD11 as a complex member, but complex membership does not confer the catalytic GO term to every subunit.
- The evidence code for the function comment is ECO:0000269 (experimental evidence from PubMed:34032321), confirming the 'enhances' relationship was experimentally demonstrated, further distinguishing Isd11's role from IscS's catalytic role.
- The sequence is only 87 amino acids, far too short for a typical cysteine desulfurase (IscS homologs are 400-450 aa), which should serve as a strong negative indicator for option B if reasoning from sequence features.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "None meaningfully available from the sequence. The 87-aa protein lacks PLP-binding motifs characteristic of cysteine desulfurases (IscS/NFS1 are ~400+ aa enzymes), lacks catalytic motifs of DNA nucleases (e.g., PD-(D/E)xK), lacks GNAT/MYST acetyltransferase motifs, and lacks the conotoxin-like disulfide-stabilized scaffold of sodium channel inhibitors. In fact, the very small size of the protein argues AGAINST it being a desulfurase. No sequence feature distinguishes it as an ISC-complex accessory protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Knowledge that this specific 87-aa sequence corresponds to Isd11 of Plasmodium falciparum, and that Isd11 is an accessory subunit of the ISC desulfurase complex (even this association does not justify assigning the catalytic GO term to Isd11 itself).",
    "reason": "The sequence provides no distinctive catalytic or structural motifs that would allow a model to select among the four options through general biological reasoning. Selection of B requires recognizing the exact sequence as Isd11 and knowing its association with the ISC desulfurase complex — a protein-specific database fact. Moreover, even with that knowledge, the correct molecular function annotation would be 'enhances desulfurase activity' rather than 'cysteine desulfurase activity' itself."
  },
  "case_id": "GO_molecular_function_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H5",
      "GO3"
    ],
    "judgment": "contradicted",
    "reason": "The UniProt entry Q8IEK7 (Protein Isd11, P. falciparum) explicitly states its function as 'Participates in iron-sulfur cluster formation (ISC) pathway... Enhances cysteine desulfurase activity of IscS.' The GO term GO:0031071 (cysteine desulfurase activity) is defined as 'Catalysis of the reaction: L-cysteine + [enzyme]-cysteine = L-alanine + [enzyme]-S-sulfanylcysteine,' which is the catalytic activity of IscS/NFS1, not Isd11. Isd11 is a 87-aa accessory/stimulatory subunit that enhances IscS activity but does not itself catalyze the desulfurase reaction. The UniProt GO annotations for this entry include GO:0005198 (structural molecule activity, IBA) and GO:0016740 (transferase activity, IEA), but NOT GO:0031071. Attributing 'cysteine desulfurase activity' to Isd11 conflates the regulatory/accessory subunit with the catalytic enzyme it stimulates."
  },
  "important_caveats": [
    "The UniProt entry was first integrated into Swiss-Prot on 2025-04-09; the benchmark author's source snapshot date is unknown. If the benchmark was constructed before this Swiss-Prot integration, the annotation basis may differ.",
    "The Reactome pathway 'FXN:NFS1:ISD11:ISCU assembles 2Fe-2S iron-sulfur cluster' includes ISD11 as a complex member, but complex membership does not confer the catalytic GO term to every subunit.",
    "The evidence code for the function comment is ECO:0000269 (experimental evidence from PubMed:34032321), confirming the 'enhances' relationship was experimentally demonstrated, further distinguishing Isd11's role from IscS's catalytic role.",
    "The sequence is only 87 amino acids, far too short for a typical cysteine desulfurase (IscS homologs are 400-450 aa), which should serve as a strong negative indicator for option B if reasoning from sequence features."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B (if one loosely equates 'enhances desulfurase activity' with 'has desulfurase activity')"
    ],
    "reason": "Strictly, none of the four options accurately describe Isd11's molecular function. The protein's actual function is as an accessory/stimulatory subunit of the ISC complex. If forced to choose, B is the closest thematic match (ISC pathway involvement), but it misattributes the catalytic activity of IscS to Isd11. The other three options (A, C, D) have no association whatsoever with this protein. The question is ambiguous in that the 'correct' answer requires accepting an inaccurate GO assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0010",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The UniProt entry Q8IEK7 (Protein Isd11, P. falciparum) explicitly states its function as 'Participates in iron-sulfur cluster formation (ISC) pathway... Enhances cysteine desulfurase activity of IscS.' The GO term GO:0031071 (cysteine desulfurase activity) is defined as 'Catalysis of the reaction: L-cysteine + [enzyme]-cysteine = L-alanine + [enzyme]-S-sulfanylcysteine,' which is the catalytic activity of IscS/NFS1, not Isd11. Isd11 is a 87-aa accessory/stimulatory subunit that enhances IscS activity but does not itself catalyze the desulfurase reaction. The UniProt GO annotations for this entry include GO:0005198 (structural molecule activity, IBA) and GO:0016740 (transferase activity, IEA), but NOT GO:0031071. Attributing 'cysteine desulfurase activity' to Isd11 conflates the regulatory/accessory subunit with the catalytic enzyme it stimulates.",
    "evidence_ids": ["C5", "H4", "C6", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "None meaningfully available from the sequence. The 87-aa protein lacks PLP-binding motifs characteristic of cysteine desulfurases (IscS/NFS1 are ~400+ aa enzymes), lacks catalytic motifs of DNA nucleases (e.g., PD-(D/E)xK), lacks GNAT/MYST acetyltransferase motifs, and lacks the conotoxin-like disulfide-stabilized scaffold of sodium channel inhibitors. In fact, the very small size of the protein argues AGAINST it being a desulfurase. No sequence feature distinguishes it as an ISC-complex accessory protein.",
    "missing_item_specific_fact": "Knowledge that this specific 87-aa sequence corresponds to Isd11 of Plasmodium falciparum, and that Isd11 is an accessory subunit of the ISC desulfurase complex (even this association does not justify assigning the catalytic GO term to Isd11 itself).",
    "reason": "The sequence provides no distinctive catalytic or structural motifs that would allow a model to select among the four options through general biological reasoning. Selection of B requires recognizing the exact sequence as Isd11 and knowing its association with the ISC desulfurase complex — a protein-specific database fact. Moreover, even with that knowledge, the correct molecular function annotation would be 'enhances desulfurase activity' rather than 'cysteine desulfurase activity' itself."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B (if one loosely equates 'enhances desulfurase activity' with 'has desulfurase activity')"],
    "reason": "Strictly, none of the four options accurately describe Isd11's molecular function. The protein's actual function is as an accessory/stimulatory subunit of the ISC complex. If forced to choose, B is the closest thematic match (ISC pathway involvement), but it misattributes the catalytic activity of IscS to Isd11. The other three options (A, C, D) have no association whatsoever with this protein. The question is ambiguous in that the 'correct' answer requires accepting an inaccurate GO assignment."
  },
  "important_caveats": [
    "The UniProt entry was first integrated into Swiss-Prot on 2025-04-09; the benchmark author's source snapshot date is unknown. If the benchmark was constructed before this Swiss-Prot integration, the annotation basis may differ.",
    "The Reactome pathway 'FXN:NFS1:ISD11:ISCU assembles 2Fe-2S iron-sulfur cluster' includes ISD11 as a complex member, but complex membership does not confer the catalytic GO term to every subunit.",
    "The evidence code for the function comment is ECO:0000269 (experimental evidence from PubMed:34032321), confirming the 'enhances' relationship was experimentally demonstrated, further distinguishing Isd11's role from IscS's catalytic role.",
    "The sequence is only 87 amino acids, far too short for a typical cysteine desulfurase (IscS homologs are 400-450 aa), which should serve as a strong negative indicator for option B if reasoning from sequence features."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q8IEK7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 85. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.795774+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34032321","source":"PubMed"}],"value":"Participates in iron-sulfur cluster formation (ISC) pathway for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Enhances cysteine desulfurase activity of IscS (PubMed:34032321)"}]}
```

Source SHA-256: `dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)  
**Locator:** `/uniProtKBCrossReferences/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.795774+00:00.  

```json
{"database":"GO","id":"GO:0005198","properties":[{"key":"GoTerm","value":"F:structural molecule activity"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85)  
**Locator:** `lines 63-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-01T06:28:39.775629+00:00.  

```text
CC   -!- FUNCTION: Participates in iron-sulfur cluster formation (ISC) pathway
CC       for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Enhances
CC       cysteine desulfurase activity of IscS (PubMed:34032321).
CC       {ECO:0000269|PubMed:34032321}.
```

Source SHA-256: `18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85)  
**Locator:** `lines 101-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-01T06:28:39.775629+00:00.  

```text
DR   GO; GO:0016740; F:transferase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 172914-172931`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031071
name: cysteine desulfurase activity
namespace: molecular_function
def: "Catalysis of the reaction: L-cysteine + [enzyme]-cysteine = L-alanine + [enzyme]-S-sulfanylcysteine." [EC:2.8.1.7]
synonym: "cysteine desulfurylase activity" RELATED [EC:2.8.1.7]
synonym: "IscS" RELATED [EC:2.8.1.7]
synonym: "L-cysteine:enzyme cysteine sulfurtransferase activity" RELATED [EC:2.8.1.7]
synonym: "NIFS" RELATED [EC:2.8.1.7]
synonym: "SufS" RELATED [EC:2.8.1.7]
xref: EC:2.8.1.7
xref: Reactome:R-HSA-1362408 "FXN:NFS1:ISD11:ISCU assembles 2Fe-2S iron-sulfur cluster"
xref: Reactome:R-HSA-947514 "PXLP-K198-NFS1 transfers sulfur from cysteine onto MOCS3"
xref: RHEA:43892
is_a: GO:0016783 ! sulfurtransferase activity
property_value: skos:exactMatch EC:2.8.1.7
property_value: skos:exactMatch RHEA:43892

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
