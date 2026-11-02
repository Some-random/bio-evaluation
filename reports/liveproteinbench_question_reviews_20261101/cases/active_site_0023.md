# active_site_0023

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 157 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVGKSTLLSVLASASVAFAACSLDSHCPEETPCCSQYGECGTGAYCLGGCDPRMSFSLESCVPEPVCESASYTFTSMDGITSNTKYLGDASKSNWVYSGSPVIYNDNVLLTMSANSVGTVMASSTYMWYGNVKAKFKTSRGQGVITAFILFSDVKDEIDYEFVGSELTTAQSNYYFQGITNYDNELNITLSDTYANYHEYEIDWTPDEITWLVDGQVGRTKKRADTWNATANQWNFPQTPARVQLSLWPGGLASNGAGTIAWAGGEIDWNSEDIQNNGYYYAAFESVDISCYNAKSAPGTNSGKSYYYNSVLGTNNTVIDSKNATILSSLLATGTNMTAGESAAASGSTAASTAATVPGLTGSGGGGVGDNHSDDGSSSSDSSSGSATSSSSGSSSTGSSGFSQGDGSTSTSKSSADSLVANQERVLKGSLFAGIVAVVAMMAL

[Multiple Choices]
A. Position 112 (Nucleophile)
B. Position 157 (Nucleophile)
C. Position 123 (Proton donor)
D. Position 122 (Nucleophile)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

### Expected-answer support: supported

> The sequence-matched UniProt record annotates position 157 as the nucleophile, citing PubMed 33846308; the archived record also contains this annotation. This supports choice B, though it is an annotation rather than independent validation here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an acidic catalytic-region motif around E157 and E161 (EIDYE); glutamate is a plausible catalytic nucleophile in this enzyme context. The alternative nucleophile positions correspond to methionine and alanine, while the alternative proton-donor position is serine, making B the strongest sequence-based choice.


**Missing item-specific fact**

> The exact experimentally or curator-assigned catalytic role of position 157 is not stated in the input; that role assignment is supported by the reviewer-only annotation.


**Reason**

> The sequence and choices provide a meaningful motif-and-residue-chemistry basis for distinguishing B, although assigning the precise catalytic role is more certain with protein-specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only position 157 is a glutamate among the offered nucleophile positions, and the sequence motif supports its catalytic plausibility; the other listed positions do not present an equally strong alternative.


### Important caveats

- The historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.
- The cited active-site annotation is linked to a publication, but the underlying experiment was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an acidic catalytic-region motif around E157 and E161 (EIDYE); glutamate is a plausible catalytic nucleophile in this enzyme context. The alternative nucleophile positions correspond to methionine and alanine, while the alternative proton-donor position is serine, making B the strongest sequence-based choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact experimentally or curator-assigned catalytic role of position 157 is not stated in the input; that role assignment is supported by the reviewer-only annotation.",
    "reason": "The sequence and choices provide a meaningful motif-and-residue-chemistry basis for distinguishing B, although assigning the precise catalytic role is more certain with protein-specific annotation."
  },
  "case_id": "active_site_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 157 as the nucleophile, citing PubMed 33846308; the archived record also contains this annotation. This supports choice B, though it is an annotation rather than independent validation here."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited active-site annotation is linked to a publication, but the underlying experiment was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 157 is a glutamate among the offered nucleophile positions, and the sequence motif supports its catalytic plausibility; the other listed positions do not present an equally strong alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 157 as the nucleophile, citing PubMed 33846308; the archived record also contains this annotation. This supports choice B, though it is an annotation rather than independent validation here.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an acidic catalytic-region motif around E157 and E161 (EIDYE); glutamate is a plausible catalytic nucleophile in this enzyme context. The alternative nucleophile positions correspond to methionine and alanine, while the alternative proton-donor position is serine, making B the strongest sequence-based choice.",
    "missing_item_specific_fact": "The exact experimentally or curator-assigned catalytic role of position 157 is not stated in the input; that role assignment is supported by the reviewer-only annotation.",
    "reason": "The sequence and choices provide a meaningful motif-and-residue-chemistry basis for distinguishing B, although assigning the precise catalytic role is more certain with protein-specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 157 is a glutamate among the offered nucleophile positions, and the sequence motif supports its catalytic plausibility; the other listed positions do not present an equally strong alternative."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited active-site annotation is linked to a publication, but the underlying experiment was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A384K116 (Crh-like protein 3, Botrytis cinerea) explicitly annotates position 157 as 'Nucleophile' (Active site) with evidence code ECO:0000305 (inferred by curator) citing PubMed:33846308 (Bi et al., Nat. Commun. 2021). The sequence at position 157 is Glutamic acid (E), consistent with the canonical catalytic nucleophile in GH18 chitinase/transglycosylases. The proton donor is annotated at position 161 (also E), matching the two-Glu mechanism of GH18 enzymes. Sequence SHA256 matches between the benchmark input and the UniProt record.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Among the four choices, the amino acids at the stated positions are: A→Met(112), B→Glu(157), C→Ser(123), D→Ala(122). Glutamate is the only chemically plausible catalytic nucleophile in glycoside-hydrolase/transglycosylase active sites; Alanine and Methionine lack the carboxylate required for nucleophilic attack on the anomeric carbon, and Serine is not the nucleophile in the retaining GH18 mechanism. The sequence around positions 153–161 (D-V-K-D-E-I-D-Y-E) contains the recognizable GH18 catalytic motif (DXXDXDXE variant) in which the first Glu (157) acts as nucleophile and the second Glu (161) as proton donor. A model that identifies the protein as a GH18-family chitinase/transglycosylase (via the SXGG-adjacent catalytic motif and overall architecture) and applies the known two-Glu mechanism can eliminate A, C, and D and select B.


**Missing item-specific fact**

> None strictly missing; however, precise residue-numbering requires the model to count to position 157 within a 444-aa sequence and to correctly parse the degenerate GH18 motif among several Glu residues elsewhere in the sequence (e.g., E29, E59, E64, E68, E166, E208, E285). The motif context narrows the choice but exact indexing is non-trivial from raw sequence alone.


**Reason**

> The biological reasoning chain (family assignment → catalytic mechanism → chemical identity of nucleophile → elimination of non-catalytic residues) provides meaningful grounds to distinguish B from the distractors. The distractors are chemically implausible (Ala, Met as nucleophiles; Ser as proton donor in a GH18 enzyme), so elimination reasoning is effective. The GH18 DXXDXDXE motif is a well-known, publicly taught sequence signature, not an obscure item-specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices present distinct amino-acid types at distinct positions. Only Glu(157) is chemically compatible with a glycosidase/transglycosylase nucleophile. No other option lists a Glu as nucleophile, and the proton-donor option (C, Ser123) is inconsistent with GH18 mechanism. No genuine ambiguity exists among the presented choices.


### Important caveats

- The UniProt annotation evidence code ECO:0000305 indicates curator inference based on the cited PubMed paper (33846308), not a direct crystallographic or mutagenesis experiment on Crh3 itself. The mechanistic assignment is transferred from the broader GH18 family understanding validated in the Crh1 study.
- The model must correctly count to position 157 in a 444-residue sequence; an off-by-one or miscount could lead to selecting a neighboring residue. This is a practical difficulty but does not introduce a missing biological fact.
- The protein is annotated as a Precursor (signal peptide + mature protein). The numbering in the UniProt entry is for the full precursor sequence, which matches the supplied sequence length (444 aa), so no offset adjustment is needed.
- The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence analysis and general enzymology knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Among the four choices, the amino acids at the stated positions are: A→Met(112), B→Glu(157), C→Ser(123), D→Ala(122). Glutamate is the only chemically plausible catalytic nucleophile in glycoside-hydrolase/transglycosylase active sites; Alanine and Methionine lack the carboxylate required for nucleophilic attack on the anomeric carbon, and Serine is not the nucleophile in the retaining GH18 mechanism. The sequence around positions 153–161 (D-V-K-D-E-I-D-Y-E) contains the recognizable GH18 catalytic motif (DXXDXDXE variant) in which the first Glu (157) acts as nucleophile and the second Glu (161) as proton donor. A model that identifies the protein as a GH18-family chitinase/transglycosylase (via the SXGG-adjacent catalytic motif and overall architecture) and applies the known two-Glu mechanism can eliminate A, C, and D and select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly missing; however, precise residue-numbering requires the model to count to position 157 within a 444-aa sequence and to correctly parse the degenerate GH18 motif among several Glu residues elsewhere in the sequence (e.g., E29, E59, E64, E68, E166, E208, E285). The motif context narrows the choice but exact indexing is non-trivial from raw sequence alone.",
    "reason": "The biological reasoning chain (family assignment → catalytic mechanism → chemical identity of nucleophile → elimination of non-catalytic residues) provides meaningful grounds to distinguish B from the distractors. The distractors are chemically implausible (Ala, Met as nucleophiles; Ser as proton donor in a GH18 enzyme), so elimination reasoning is effective. The GH18 DXXDXDXE motif is a well-known, publicly taught sequence signature, not an obscure item-specific annotation."
  },
  "case_id": "active_site_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "C1",
      "C3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A384K116 (Crh-like protein 3, Botrytis cinerea) explicitly annotates position 157 as 'Nucleophile' (Active site) with evidence code ECO:0000305 (inferred by curator) citing PubMed:33846308 (Bi et al., Nat. Commun. 2021). The sequence at position 157 is Glutamic acid (E), consistent with the canonical catalytic nucleophile in GH18 chitinase/transglycosylases. The proton donor is annotated at position 161 (also E), matching the two-Glu mechanism of GH18 enzymes. Sequence SHA256 matches between the benchmark input and the UniProt record."
  },
  "important_caveats": [
    "The UniProt annotation evidence code ECO:0000305 indicates curator inference based on the cited PubMed paper (33846308), not a direct crystallographic or mutagenesis experiment on Crh3 itself. The mechanistic assignment is transferred from the broader GH18 family understanding validated in the Crh1 study.",
    "The model must correctly count to position 157 in a 444-residue sequence; an off-by-one or miscount could lead to selecting a neighboring residue. This is a practical difficulty but does not introduce a missing biological fact.",
    "The protein is annotated as a Precursor (signal peptide + mature protein). The numbering in the UniProt entry is for the full precursor sequence, which matches the supplied sequence length (444 aa), so no offset adjustment is needed.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence analysis and general enzymology knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices present distinct amino-acid types at distinct positions. Only Glu(157) is chemically compatible with a glycosidase/transglycosylase nucleophile. No other option lists a Glu as nucleophile, and the proton-donor option (C, Ser123) is inconsistent with GH18 mechanism. No genuine ambiguity exists among the presented choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A384K116 (Crh-like protein 3, Botrytis cinerea) explicitly annotates position 157 as 'Nucleophile' (Active site) with evidence code ECO:0000305 (inferred by curator) citing PubMed:33846308 (Bi et al., Nat. Commun. 2021). The sequence at position 157 is Glutamic acid (E), consistent with the canonical catalytic nucleophile in GH18 chitinase/transglycosylases. The proton donor is annotated at position 161 (also E), matching the two-Glu mechanism of GH18 enzymes. Sequence SHA256 matches between the benchmark input and the UniProt record.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "C1", "C3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Among the four choices, the amino acids at the stated positions are: A→Met(112), B→Glu(157), C→Ser(123), D→Ala(122). Glutamate is the only chemically plausible catalytic nucleophile in glycoside-hydrolase/transglycosylase active sites; Alanine and Methionine lack the carboxylate required for nucleophilic attack on the anomeric carbon, and Serine is not the nucleophile in the retaining GH18 mechanism. The sequence around positions 153–161 (D-V-K-D-E-I-D-Y-E) contains the recognizable GH18 catalytic motif (DXXDXDXE variant) in which the first Glu (157) acts as nucleophile and the second Glu (161) as proton donor. A model that identifies the protein as a GH18-family chitinase/transglycosylase (via the SXGG-adjacent catalytic motif and overall architecture) and applies the known two-Glu mechanism can eliminate A, C, and D and select B.",
    "missing_item_specific_fact": "None strictly missing; however, precise residue-numbering requires the model to count to position 157 within a 444-aa sequence and to correctly parse the degenerate GH18 motif among several Glu residues elsewhere in the sequence (e.g., E29, E59, E64, E68, E166, E208, E285). The motif context narrows the choice but exact indexing is non-trivial from raw sequence alone.",
    "reason": "The biological reasoning chain (family assignment → catalytic mechanism → chemical identity of nucleophile → elimination of non-catalytic residues) provides meaningful grounds to distinguish B from the distractors. The distractors are chemically implausible (Ala, Met as nucleophiles; Ser as proton donor in a GH18 enzyme), so elimination reasoning is effective. The GH18 DXXDXDXE motif is a well-known, publicly taught sequence signature, not an obscure item-specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices present distinct amino-acid types at distinct positions. Only Glu(157) is chemically compatible with a glycosidase/transglycosylase nucleophile. No other option lists a Glu as nucleophile, and the proton-donor option (C, Ser123) is inconsistent with GH18 mechanism. No genuine ambiguity exists among the presented choices."
  },
  "important_caveats": [
    "The UniProt annotation evidence code ECO:0000305 indicates curator inference based on the cited PubMed paper (33846308), not a direct crystallographic or mutagenesis experiment on Crh3 itself. The mechanistic assignment is transferred from the broader GH18 family understanding validated in the Crh1 study.",
    "The model must correctly count to position 157 in a 444-residue sequence; an off-by-one or miscount could lead to selecting a neighboring residue. This is a practical difficulty but does not introduce a missing biological fact.",
    "The protein is annotated as a Precursor (signal peptide + mature protein). The numbering in the UniProt entry is for the full precursor sequence, which matches the supplied sequence length (444 aa), so no offset adjustment is needed.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence analysis and general enzymology knowledge."
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

**Accession:** `A0A384K116` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
"A0A384K116"
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"commonName":"Noble rot fungus","lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Pezizomycotina","Leotiomycetes","Helotiales","Sclerotiniaceae","Botrytis"],"scientificName":"Botrytis cinerea (strain B05.10)","synonyms":["Botryotinia fuckeliana"],"taxonId":332648}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"flag":"Precursor","includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"3.2.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"Chitinase crh3"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"2.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"Chitin transglycosylase crh3"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33846308","source":"PubMed"}],"value":"Crh-like protein 3"}}}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"description":"Nucleophile","evidences":[{"evidenceCode":"ECO:0000305","id":"33846308","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":157},"start":{"modifier":"EXACT","value":157}},"type":"Active site"}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000305","id":"33846308","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":161},"start":{"modifier":"EXACT","value":161}},"type":"Active site"}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)  
**Locator:** `lines 141-143`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:01.844205+00:00.  

```text
FT   ACT_SITE        157
FT                   /note="Nucleophile"
FT                   /evidence="ECO:0000305|PubMed:33846308"
```

Source SHA-256: `68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)  
**Locator:** `lines 144-146`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:01.844205+00:00.  

```text
FT   ACT_SITE        161
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000305|PubMed:33846308"
```

Source SHA-256: `68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
