# GO_molecular_function_0177

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — glycosyltransferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGLTDIFLNLLLFVYPAVFIIYQIILYEISARKQINQEALKYSNLPVLSIIVPIKNEEISVIQGLLDNLSNLIWDKKKLEIIIVSDDNEDYFTKIINTVKVPKDLTVYFYRREKKLGYKSGALQYGFEKATGDLILTIDVDSRLPPNALINAYEKMQSNTCDAIVFQWNGYSSNQYSTLAKGMVVSTLFASKALFEGKEKLKLKIYPVGSGTMFSREALRVVNGWDYRLVQDDLEIGTRLIYNGKNVCASGIPIYVEVPDNFYSFYVQQTRWAMGSAEVLRNRLKYIIKSKISFTQRMDLIIYLLQYTPVIVTFFISTLLSLMLPFRIGHDPLNSPALLFWLVSLGLYASLLLSLALKLGLNLKDSLMGIGRLTAFTVSISPFIVFNFFKGLLKSGNTYVITPKGTVKKTNKLLRIIAIIGVFGLLYLLSSILYIYEGYYVTGIWLLYYSSAYLYTMLLYYKEL

[Multiple Choices]
A. UDP-glycosyltransferase activity
B. glycosyltransferase activity
C. 5'-nucleotidase activity
D. carbohydrate derivative binding
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

### Expected-answer support: supported

> The exact sequence matches a UniProt entry annotated as a probable glycosyltransferase, with EC 2.4.-.- and a glycosyltransferase-activity GO annotation. This supports the broad expected function, but the annotation is inferential rather than direct experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic in several regions, consistent with a membrane protein, but that does not establish glycosyltransferase activity or distinguish it from the other listed functions.


**Missing item-specific fact**

> A protein-specific functional annotation or evidence identifying its catalytic family and substrate/donor specificity is needed; the sequence and choices alone do not establish glycosyltransferase activity.


**Reason**

> The answer is supported by the matched protein's database annotation, not by a clear, general sequence-based argument available in the question. In particular, the sequence does not reveal whether the enzyme is a UDP-glycosyltransferase.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> UDP-glycosyltransferase activity is a narrower kind of glycosyltransferase activity, so the options overlap. The available annotation supports broad glycosyltransferase activity but does not resolve whether the narrower UDP-specific option also applies.


### Important caveats

- The matched UniProt annotation calls the protein a probable glycosyltransferase; the cited GO annotation is IEA, not evidence of a direct biochemical assay.
- The database record also describes a probable role in a DNA-damage-response locus, which does not itself establish a molecular catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic in several regions, consistent with a membrane protein, but that does not establish glycosyltransferase activity or distinguish it from the other listed functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific functional annotation or evidence identifying its catalytic family and substrate/donor specificity is needed; the sequence and choices alone do not establish glycosyltransferase activity.",
    "reason": "The answer is supported by the matched protein's database annotation, not by a clear, general sequence-based argument available in the question. In particular, the sequence does not reveal whether the enzyme is a UDP-glycosyltransferase."
  },
  "case_id": "GO_molecular_function_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a probable glycosyltransferase, with EC 2.4.-.- and a glycosyltransferase-activity GO annotation. This supports the broad expected function, but the annotation is inferential rather than direct experimental evidence."
  },
  "important_caveats": [
    "The matched UniProt annotation calls the protein a probable glycosyltransferase; the cited GO annotation is IEA, not evidence of a direct biochemical assay.",
    "The database record also describes a probable role in a DNA-damage-response locus, which does not itself establish a molecular catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "UDP-glycosyltransferase activity is a narrower kind of glycosyltransferase activity, so the options overlap. The available annotation supports broad glycosyltransferase activity but does not resolve whether the narrower UDP-specific option also applies."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a probable glycosyltransferase, with EC 2.4.-.- and a glycosyltransferase-activity GO annotation. This supports the broad expected function, but the annotation is inferential rather than direct experimental evidence.",
    "evidence_ids": ["C1", "C4", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic in several regions, consistent with a membrane protein, but that does not establish glycosyltransferase activity or distinguish it from the other listed functions.",
    "missing_item_specific_fact": "A protein-specific functional annotation or evidence identifying its catalytic family and substrate/donor specificity is needed; the sequence and choices alone do not establish glycosyltransferase activity.",
    "reason": "The answer is supported by the matched protein's database annotation, not by a clear, general sequence-based argument available in the question. In particular, the sequence does not reveal whether the enzyme is a UDP-glycosyltransferase."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "UDP-glycosyltransferase activity is a narrower kind of glycosyltransferase activity, so the options overlap. The available annotation supports broad glycosyltransferase activity but does not resolve whether the narrower UDP-specific option also applies."
  },
  "important_caveats": [
    "The matched UniProt annotation calls the protein a probable glycosyltransferase; the cited GO annotation is IEA, not evidence of a direct biochemical assay.",
    "The database record also describes a probable role in a DNA-damage-response locus, which does not itself establish a molecular catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4J8Q7 (sequence matched) annotates this protein as 'Probable glycosyltransferase Saci_1499' with EC 2.4.-.- (C4, H1), and carries the GO term GO:0016757 (glycosyltransferase activity) via IEA:UniProtKB-KW (H4). GO:0016757 maps exactly to option B. The EC 2.4.-.- is the generic glycosyltransferase class, consistent with B rather than the more specific UDP-glycosyltransferase (A). However, the annotation is IEA (electronic/computational inference) and the protein name includes 'Probable,' indicating the assignment is not experimentally confirmed. Option C (5'-nucleotidase, EC 3.1.3.5, a hydrolase) and D (carbohydrate derivative binding, a non-catalytic binding term) are inconsistent with the transferase annotation.

Citations as saved: [C4](#evidence-c4), [H1](#evidence-h1), [H4](#evidence-h4), [GO3](#evidence-go3), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Some partial reasoning is possible: the protein has multiple transmembrane segments (long hydrophobic stretches throughout), which is inconsistent with classical soluble UDP-glycosyltransferases (UGTs, typically cytosolic single-domain enzymes), providing a weak argument against option A. The absence of recognizable nucleotidase catalytic motifs (e.g., HxH, specific phosphatase residues) weakly argues against C. The multi-pass membrane architecture suggests a catalytic or transport role rather than simple binding, weakly arguing against D. However, none of these arguments positively identify the protein as a glycosyltransferase rather than, say, a membrane transporter, flippase, or other integral membrane enzyme.


**Missing item-specific fact**

> The specific sequence-family assignment (e.g., GT-B fold nucleotide-binding motif, PSPG box, or other glycosyltransferase signature) that would positively identify this protein as a glycosyltransferase from sequence alone. The UniProt annotation itself is IEA (computational inference), and the protein is labeled 'Probable,' indicating even the database relies on sequence-similarity heuristics rather than experimental characterization. Distinguishing A (UDP-glycosyltransferase, a specific subclass) from B (general glycosyltransferase) requires knowing the specific sugar-donor preference, which is not determinable from the sequence without family-specific knowledge or experimental data.


**Reason**

> The core identification as a glycosyltransferase depends on recognizing family-specific motifs or database annotation. The sequence does not contain a widely recognized, easily identifiable catalytic signature that would allow a model to confidently assign glycosyltransferase activity over other membrane-protein functions using only general biological knowledge. The annotation is itself computational (IEA), and the protein is 'probable,' underscoring the reliance on pattern-matching rather than definitive experimental evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While A (UDP-glycosyltransferase) is a child term of B (glycosyltransferase), the EC 2.4.-.- annotation is generic and does not specify a UDP-sugar donor. The multi-pass membrane topology is atypical for classical UDP-glycosyltransferases. C and D are clearly inconsistent with a transferase annotation. B is the most defensible single answer given the available annotation.


### Important caveats

- The GO annotation (GO:0016757) carries evidence code IEA (Inferred from Electronic Annotation), meaning it is a computational inference, not experimental evidence.
- The protein is named 'Probable glycosyltransferase,' indicating uncertainty even at the database level.
- The EC number 2.4.-.- is the generic glycosyltransferase class; no specific subclass or sugar-donor preference has been experimentally determined.
- The function comment describes a role in DNA damage response/homologous recombination (PubMed:26148716), which is a biological context rather than a direct enzymatic characterization.
- The reviewer-only evidence was not available to the evaluated model; the model sees only the 464-aa sequence and four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Some partial reasoning is possible: the protein has multiple transmembrane segments (long hydrophobic stretches throughout), which is inconsistent with classical soluble UDP-glycosyltransferases (UGTs, typically cytosolic single-domain enzymes), providing a weak argument against option A. The absence of recognizable nucleotidase catalytic motifs (e.g., HxH, specific phosphatase residues) weakly argues against C. The multi-pass membrane architecture suggests a catalytic or transport role rather than simple binding, weakly arguing against D. However, none of these arguments positively identify the protein as a glycosyltransferase rather than, say, a membrane transporter, flippase, or other integral membrane enzyme.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific sequence-family assignment (e.g., GT-B fold nucleotide-binding motif, PSPG box, or other glycosyltransferase signature) that would positively identify this protein as a glycosyltransferase from sequence alone. The UniProt annotation itself is IEA (computational inference), and the protein is labeled 'Probable,' indicating even the database relies on sequence-similarity heuristics rather than experimental characterization. Distinguishing A (UDP-glycosyltransferase, a specific subclass) from B (general glycosyltransferase) requires knowing the specific sugar-donor preference, which is not determinable from the sequence without family-specific knowledge or experimental data.",
    "reason": "The core identification as a glycosyltransferase depends on recognizing family-specific motifs or database annotation. The sequence does not contain a widely recognized, easily identifiable catalytic signature that would allow a model to confidently assign glycosyltransferase activity over other membrane-protein functions using only general biological knowledge. The annotation is itself computational (IEA), and the protein is 'probable,' underscoring the reliance on pattern-matching rather than definitive experimental evidence."
  },
  "case_id": "GO_molecular_function_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "H1",
      "H4",
      "GO3",
      "GO1",
      "GO2",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4J8Q7 (sequence matched) annotates this protein as 'Probable glycosyltransferase Saci_1499' with EC 2.4.-.- (C4, H1), and carries the GO term GO:0016757 (glycosyltransferase activity) via IEA:UniProtKB-KW (H4). GO:0016757 maps exactly to option B. The EC 2.4.-.- is the generic glycosyltransferase class, consistent with B rather than the more specific UDP-glycosyltransferase (A). However, the annotation is IEA (electronic/computational inference) and the protein name includes 'Probable,' indicating the assignment is not experimentally confirmed. Option C (5'-nucleotidase, EC 3.1.3.5, a hydrolase) and D (carbohydrate derivative binding, a non-catalytic binding term) are inconsistent with the transferase annotation."
  },
  "important_caveats": [
    "The GO annotation (GO:0016757) carries evidence code IEA (Inferred from Electronic Annotation), meaning it is a computational inference, not experimental evidence.",
    "The protein is named 'Probable glycosyltransferase,' indicating uncertainty even at the database level.",
    "The EC number 2.4.-.- is the generic glycosyltransferase class; no specific subclass or sugar-donor preference has been experimentally determined.",
    "The function comment describes a role in DNA damage response/homologous recombination (PubMed:26148716), which is a biological context rather than a direct enzymatic characterization.",
    "The reviewer-only evidence was not available to the evaluated model; the model sees only the 464-aa sequence and four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A (UDP-glycosyltransferase) is a child term of B (glycosyltransferase), the EC 2.4.-.- annotation is generic and does not specify a UDP-sugar donor. The multi-pass membrane topology is atypical for classical UDP-glycosyltransferases. C and D are clearly inconsistent with a transferase annotation. B is the most defensible single answer given the available annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4J8Q7 (sequence matched) annotates this protein as 'Probable glycosyltransferase Saci_1499' with EC 2.4.-.- (C4, H1), and carries the GO term GO:0016757 (glycosyltransferase activity) via IEA:UniProtKB-KW (H4). GO:0016757 maps exactly to option B. The EC 2.4.-.- is the generic glycosyltransferase class, consistent with B rather than the more specific UDP-glycosyltransferase (A). However, the annotation is IEA (electronic/computational inference) and the protein name includes 'Probable,' indicating the assignment is not experimentally confirmed. Option C (5'-nucleotidase, EC 3.1.3.5, a hydrolase) and D (carbohydrate derivative binding, a non-catalytic binding term) are inconsistent with the transferase annotation.",
    "evidence_ids": ["C4", "H1", "H4", "GO3", "GO1", "GO2", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Some partial reasoning is possible: the protein has multiple transmembrane segments (long hydrophobic stretches throughout), which is inconsistent with classical soluble UDP-glycosyltransferases (UGTs, typically cytosolic single-domain enzymes), providing a weak argument against option A. The absence of recognizable nucleotidase catalytic motifs (e.g., HxH, specific phosphatase residues) weakly argues against C. The multi-pass membrane architecture suggests a catalytic or transport role rather than simple binding, weakly arguing against D. However, none of these arguments positively identify the protein as a glycosyltransferase rather than, say, a membrane transporter, flippase, or other integral membrane enzyme.",
    "missing_item_specific_fact": "The specific sequence-family assignment (e.g., GT-B fold nucleotide-binding motif, PSPG box, or other glycosyltransferase signature) that would positively identify this protein as a glycosyltransferase from sequence alone. The UniProt annotation itself is IEA (computational inference), and the protein is labeled 'Probable,' indicating even the database relies on sequence-similarity heuristics rather than experimental characterization. Distinguishing A (UDP-glycosyltransferase, a specific subclass) from B (general glycosyltransferase) requires knowing the specific sugar-donor preference, which is not determinable from the sequence without family-specific knowledge or experimental data.",
    "reason": "The core identification as a glycosyltransferase depends on recognizing family-specific motifs or database annotation. The sequence does not contain a widely recognized, easily identifiable catalytic signature that would allow a model to confidently assign glycosyltransferase activity over other membrane-protein functions using only general biological knowledge. The annotation is itself computational (IEA), and the protein is 'probable,' underscoring the reliance on pattern-matching rather than definitive experimental evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A (UDP-glycosyltransferase) is a child term of B (glycosyltransferase), the EC 2.4.-.- annotation is generic and does not specify a UDP-sugar donor. The multi-pass membrane topology is atypical for classical UDP-glycosyltransferases. C and D are clearly inconsistent with a transferase annotation. B is the most defensible single answer given the available annotation."
  },
  "important_caveats": [
    "The GO annotation (GO:0016757) carries evidence code IEA (Inferred from Electronic Annotation), meaning it is a computational inference, not experimental evidence.",
    "The protein is named 'Probable glycosyltransferase,' indicating uncertainty even at the database level.",
    "The EC number 2.4.-.- is the generic glycosyltransferase class; no specific subclass or sugar-donor preference has been experimentally determined.",
    "The function comment describes a role in DNA damage response/homologous recombination (PubMed:26148716), which is a biological context rather than a direct enzymatic characterization.",
    "The reviewer-only evidence was not available to the evaluated model; the model sees only the 464-aa sequence and four choices."
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

**Accession:** `Q4J8Q7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 83. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:48.833149+00:00.  

```json
"Q4J8Q7"
```

Source SHA-256: `3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:48.833149+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"value":"2.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Probable glycosyltransferase Saci_1499"}}}
```

Source SHA-256: `3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-02T04:30:51.056852+00:00.  

```text
ID   Y1499_SULAC             Reviewed;         464 AA.
AC   Q4J8Q7;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-AUG-2005, sequence version 1.
DT   28-JAN-2026, entry version 83.
DE   RecName: Full=Probable glycosyltransferase Saci_1499 {ECO:0000305};
DE            EC=2.4.-.-;
GN   OrderedLocusNames=Saci_1499 {ECO:0000312|EMBL:AAY80820.1};
OS   Sulfolobus acidocaldarius (strain ATCC 33909 / DSM 639 / JCM 8929 / NBRC
OS   15157 / NCIMB 11770).
OC   Archaea; Thermoproteota; Thermoprotei; Sulfolobales; Sulfolobaceae;
OC   Sulfolobus.
OX   NCBI_TaxID=330779;
```

Source SHA-256: `77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)  
**Locator:** `lines 56-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-02T04:30:51.056852+00:00.  

```text
DR   GO; GO:0016757; F:glycosyltransferase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 80524-80531`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008194
name: UDP-glycosyltransferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a glycosyl group from a UDP-sugar to a small hydrophobic molecule." [PMID:11846783]
xref: Reactome:R-HSA-162730 "phosphatidylinositol + UDP-N-acetyl-D-glucosamine -> N-acetylglucosaminyl-PI + UDP"
is_a: GO:0016757 ! glycosyltransferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 81203-81255`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008253
name: 5'-nucleotidase activity
namespace: molecular_function
def: "Catalysis of the reaction: a nucleoside 5'-phosphate + H2O = a nucleoside + phosphate." [EC:3.1.3.5, PMID:27907199]
synonym: "5' nucleotidase activity" EXACT []
synonym: "5'-adenylic phosphatase" NARROW [EC:3.1.3.5]
synonym: "5'-AMP nucleotidase" NARROW [EC:3.1.3.5]
synonym: "5'-AMPase" NARROW [EC:3.1.3.5]
synonym: "5'-mononucleotidase activity" RELATED [EC:3.1.3.5]
synonym: "5'-ribonucleotide phosphohydrolase activity" NARROW [EC:3.1.3.5]
synonym: "adenosine 5'-phosphatase" NARROW [EC:3.1.3.5]
synonym: "adenosine monophosphatase" NARROW [EC:3.1.3.5]
synonym: "AMP phosphatase" NARROW [EC:3.1.3.5]
synonym: "AMP phosphohydrolase" NARROW [EC:3.1.3.5]
synonym: "AMPase" NARROW [EC:3.1.3.5]
synonym: "snake venom 5'-nucleotidase" NARROW [EC:3.1.3.5]
synonym: "thimidine monophosphate nucleotidase" NARROW [EC:3.1.3.5]
synonym: "UMPase" NARROW [EC:3.1.3.5]
synonym: "uridine 5'-nucleotidase" NARROW [EC:3.1.3.5]
xref: EC:3.1.3.5
xref: MetaCyc:5-NUCLEOTID-RXN
xref: Reactome:R-HSA-109278 "NT5E:Zn2+ hydrolyses AMP,dAMP,GMP, IMP"
xref: Reactome:R-HSA-109291 "CMP or TMP or UMP + H2O => cytidine, thymidine, or uridine + orthophosphate [NT5E]"
xref: Reactome:R-HSA-109380 "(d)CMP, TMP, or (d)UMP + H2O => (deoxy)cytidine, thymidine, or (deoxy)uridine + orthophosphate (NT5C1A)"
xref: Reactome:R-HSA-109387 "(d)AMP, (d)GMP, or (d)IMP + H2O => (deoxy)adenosine, (deoxy)guanosine, or (deoxy)inosine + orthophosphate (NT5C1A)"
xref: Reactome:R-HSA-109415 "AMP + H2O => adenosine + orthophosphate [NT5C1B]"
xref: Reactome:R-HSA-109449 "(d)CMP, TMP, or (d)UMP + H2O => (deoxy)cytidine, thymidine, or (deoxy)uridine + orthophosphate (NT5C3)"
xref: Reactome:R-HSA-109470 "(d)GMP or (d)IMP + H2O => (d)G or (d)I + orthophosphate (NT5C)"
xref: Reactome:R-HSA-109480 "TMP, uridine 2', 3', or 5' monophosphates, or deoxyuridine 3' or 5' monophosphates + H2O => thymidine or (deoxy)uridine + orthophosphate [NT5C]"
xref: Reactome:R-HSA-109514 "TMP, (d)UMP, uridine 2' monophosphate, or uridine 3'-monophosphate + H2O => thymidine, deoxyuridine, or uridine + orthophosphate [NT5M]"
xref: Reactome:R-HSA-5694126 "NT5C3B hydrolyses 7MGP to 7MG"
xref: Reactome:R-HSA-74248 "(d)GMP or (d)IMP + H2O => (2'-deoxy)guanosine or (2'-deoxy)inosine + orthophosphate (NT5C2)"
xref: Reactome:R-HSA-8940070 "NT5E:Zn2+ hydrolyses NAD+"
xref: Reactome:R-HSA-8940074 "NT5E:Zn2+ hydrolyses NMN"
xref: Reactome:R-HSA-9755078 "NT5C2 tetramer dephosphorylates RBV-MP"
xref: RHEA:12484
xref: RHEA:22140
xref: RHEA:27714
xref: RHEA:27718
xref: RHEA:29359
xref: RHEA:29375
xref: RHEA:30815
is_a: GO:0008252 ! nucleotidase activity
property_value: skos:exactMatch EC:3.1.3.5
property_value: skos:exactMatch RHEA:22140
property_value: skos:narrowMatch RHEA:12484
property_value: skos:narrowMatch RHEA:27714
property_value: skos:narrowMatch RHEA:27718
property_value: skos:narrowMatch RHEA:29359
property_value: skos:narrowMatch RHEA:29375
property_value: skos:narrowMatch RHEA:30815

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 129828-129846`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016757
name: glycosyltransferase activity
namespace: molecular_function
alt_id: GO:0016932
def: "Catalysis of the transfer of a glycosyl group from one compound (donor) to another (acceptor)." [GOC:jl, ISBN:0198506732]
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_yeast
synonym: "transferase activity, transferring glycosyl groups" EXACT []
synonym: "transferase activity, transferring other glycosyl groups" NARROW []
synonym: "transglycosidase activity" EXACT []
synonym: "transglycosylase activity" EXACT []
xref: EC:2.4.-.-
xref: Reactome:R-HSA-5173005 "B3GALTL transfers glucose to O-fucosyl-proteins"
xref: Reactome:R-HSA-6785565 "Defective B3GALTL does not transfer glucose to O-fucosyl-proteins"
is_a: GO:0016740 ! transferase activity
property_value: skos:exactMatch EC:2.4.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 404743-404751`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0097367
name: carbohydrate derivative binding
namespace: molecular_function
def: "Binding to a carbohydrate derivative." [GOC:pr]
subset: goslim_agr
subset: goslim_mouse
is_a: GO:0005488 ! binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 177. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
