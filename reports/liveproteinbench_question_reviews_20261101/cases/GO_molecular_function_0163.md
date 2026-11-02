# GO_molecular_function_0163

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — hydrolase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNNDEQLEFLINYLLDERSESIDIPKTFSEKRNLLRSLMNMRHPSNISEEFLRIQDEFLSRETANKNLTSVEDISLSSGKIMLWQGDITTLSADAIVNAANSKLLGCFIPMHNCIDNIIHSASGLQLREECNRMIMLQGGDEDVGKAKITNAYNLPSKYVVHTVGPSIERGMRVSSDDVKKLERCYNSCLELASEYKLNSIAFCCISTGVFNFPQKKAAEIAIRTVKDFLNSNETSLNHIIFDVFTDKDYDIYKKLLFGN

[Multiple Choices]
A. URM1 activating enzyme activity
B. hydrolase activity
C. cysteine desulfurase activity
D. magnesium ion binding
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

> The sequence matches the UniProt entry for a protein experimentally reported to hydrolyze ADP-ribosyl-glutamate bonds, supporting the broad hydrolase activity choice. The entry also assigns a more specific hydrolase GO term.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The supplied sequence alone does not provide a sufficiently specific, evident basis for identifying this protein's ADP-ribosyl hydrolase activity over the alternatives.


**Missing item-specific fact**

> The experimentally established substrate and catalytic activity of this particular protein are absent from the input.


**Reason**

> Choosing B is supported by protein-specific functional evidence, not by a concrete sequence-based argument available in the question. Recognizing the sequence or its annotation would amount to lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimentally described hydrolysis supports B, while the other choices describe activities not established by the supplied input or the cited functional evidence.


### Important caveats

- The UniProt entry and experimental evidence are reviewer-only and were not supplied to the evaluated model.
- The experimental reaction supports broad hydrolase activity; the specific UniProt GO annotation is not itself direct evidence of every possible hydrolase classification.
- The sequence matches the historical UniProt record, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence alone does not provide a sufficiently specific, evident basis for identifying this protein's ADP-ribosyl hydrolase activity over the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally established substrate and catalytic activity of this particular protein are absent from the input.",
    "reason": "Choosing B is supported by protein-specific functional evidence, not by a concrete sequence-based argument available in the question. Recognizing the sequence or its annotation would amount to lookup or memorization."
  },
  "case_id": "GO_molecular_function_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3",
      "H4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for a protein experimentally reported to hydrolyze ADP-ribosyl-glutamate bonds, supporting the broad hydrolase activity choice. The entry also assigns a more specific hydrolase GO term."
  },
  "important_caveats": [
    "The UniProt entry and experimental evidence are reviewer-only and were not supplied to the evaluated model.",
    "The experimental reaction supports broad hydrolase activity; the specific UniProt GO annotation is not itself direct evidence of every possible hydrolase classification.",
    "The sequence matches the historical UniProt record, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimentally described hydrolysis supports B, while the other choices describe activities not established by the supplied input or the cited functional evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for a protein experimentally reported to hydrolyze ADP-ribosyl-glutamate bonds, supporting the broad hydrolase activity choice. The entry also assigns a more specific hydrolase GO term.",
    "evidence_ids": ["H1", "H3", "H4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The supplied sequence alone does not provide a sufficiently specific, evident basis for identifying this protein's ADP-ribosyl hydrolase activity over the alternatives.",
    "missing_item_specific_fact": "The experimentally established substrate and catalytic activity of this particular protein are absent from the input.",
    "reason": "Choosing B is supported by protein-specific functional evidence, not by a concrete sequence-based argument available in the question. Recognizing the sequence or its annotation would amount to lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimentally described hydrolysis supports B, while the other choices describe activities not established by the supplied input or the cited functional evidence."
  },
  "important_caveats": [
    "The UniProt entry and experimental evidence are reviewer-only and were not supplied to the evaluated model.",
    "The experimental reaction supports broad hydrolase activity; the specific UniProt GO annotation is not itself direct evidence of every possible hydrolase classification.",
    "The sequence matches the historical UniProt record, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A166ACJ5 (ADPRH_METOA) is experimentally characterized (PubMed:39270823, IDA evidence) as a Protein-ADP-ribose hydrolase with EC 3.2.1.-. It is annotated with GO:0004553 (hydrolase activity, hydrolyzing O-glycosyl compounds), which is a child of GO:0016798 (hydrolase activity, acting on glycosyl bonds), which in turn is a child of GO:0016787 (hydrolase activity). The ontology path confirms GO:0004553 → GO:0016798 → GO:0016787. The catalytic activity (hydrolysis of ADP-ribosyl-glutamate bonds) is a hydrolase reaction. The protein binds zinc (GO:0008270), not magnesium, ruling out D. There is no evidence for URM1 activating enzyme (A) or cysteine desulfurase (C) activity. The expected answer B (hydrolase activity) is the correct parent-level GO term.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2), [GO3](#evidence-go3), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could partially eliminate distractors through general reasoning: URM1 activating enzymes (A) are typically 400+ residue E1-like enzymes with adenylation domains; cysteine desulfurases (C) are ~400 aa PLP-dependent enzymes (IscS/SufS family); magnesium ion binding (D) as a primary molecular function is unusual for a 260-aa protein of this complexity. However, positively identifying 'hydrolase activity' requires recognizing the macrodomain fold (MorMacro) and knowing that this particular macrodomain variant is a zinc-dependent hydrolase (eraser) rather than an ADP-ribose reader. The distinction between reader and hydrolase macrodomains depends on specific catalytic residues (the conserved Glu in the E-x-x-E motif) and the zinc-coordinating site, which is specialized family knowledge not derivable from general sequence features alone.


**Missing item-specific fact**

> The identification of this protein as a macrodomain-family ADP-ribosylhydrolase (rather than a reader or other fold) requires knowledge of the MorMacro protein family and its zinc-dependent catalytic mechanism for hydrolyzing ADP-ribosyl-glutamate bonds, established experimentally in PubMed:39270823. Without recognizing the macrodomain fold and knowing the catalytic Glu/Zn site, one cannot positively assign hydrolase activity from the 260-aa sequence alone.


**Reason**

> While elimination of clearly wrong distractors (A, C) is possible via size/family heuristics, the positive assignment of 'hydrolase activity' as the primary molecular function depends on recognizing the macrodomain fold and knowing that this specific variant is a catalytic hydrolase rather than a binding reader. This is protein-family-specific knowledge, not derivable from general biological reasoning applied to the raw sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B (hydrolase activity) is supported. A (URM1 activating enzyme) is a specific E1-like activity with no sequence similarity to this protein. C (cysteine desulfurase) is a PLP-dependent sulfurtransferase with no evidence here. D (magnesium ion binding) is contradicted by the zinc-binding annotation. The broad term 'hydrolase activity' (GO:0016787) correctly encompasses the specific annotation GO:0004553 via the is_a hierarchy.


### Important caveats

- The protein's specific annotation (GO:0004553, hydrolase activity, hydrolyzing O-glycosyl compounds) is more precise than the option text 'hydrolase activity' (GO:0016787), but the latter is the correct parent term and is valid as a GO molecular function annotation.
- The protein binds zinc ions (GO:0008270), not magnesium ions, making option D specifically incorrect rather than merely unsupported.
- The macrodomain fold recognition and reader-vs-hydrolase distinction require specialized knowledge; general sequence heuristics (size, composition) are insufficient for positive identification.
- The annotation evidence is experimental (IDA, PubMed:39270823, X-ray crystallography with Zn2+ and ADP-ribose complexes), establishing the function firmly but not making it inferable from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could partially eliminate distractors through general reasoning: URM1 activating enzymes (A) are typically 400+ residue E1-like enzymes with adenylation domains; cysteine desulfurases (C) are ~400 aa PLP-dependent enzymes (IscS/SufS family); magnesium ion binding (D) as a primary molecular function is unusual for a 260-aa protein of this complexity. However, positively identifying 'hydrolase activity' requires recognizing the macrodomain fold (MorMacro) and knowing that this particular macrodomain variant is a zinc-dependent hydrolase (eraser) rather than an ADP-ribose reader. The distinction between reader and hydrolase macrodomains depends on specific catalytic residues (the conserved Glu in the E-x-x-E motif) and the zinc-coordinating site, which is specialized family knowledge not derivable from general sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this protein as a macrodomain-family ADP-ribosylhydrolase (rather than a reader or other fold) requires knowledge of the MorMacro protein family and its zinc-dependent catalytic mechanism for hydrolyzing ADP-ribosyl-glutamate bonds, established experimentally in PubMed:39270823. Without recognizing the macrodomain fold and knowing the catalytic Glu/Zn site, one cannot positively assign hydrolase activity from the 260-aa sequence alone.",
    "reason": "While elimination of clearly wrong distractors (A, C) is possible via size/family heuristics, the positive assignment of 'hydrolase activity' as the primary molecular function depends on recognizing the macrodomain fold and knowing that this specific variant is a catalytic hydrolase rather than a binding reader. This is protein-family-specific knowledge, not derivable from general biological reasoning applied to the raw sequence."
  },
  "case_id": "GO_molecular_function_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5",
      "GO2",
      "GO3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A166ACJ5 (ADPRH_METOA) is experimentally characterized (PubMed:39270823, IDA evidence) as a Protein-ADP-ribose hydrolase with EC 3.2.1.-. It is annotated with GO:0004553 (hydrolase activity, hydrolyzing O-glycosyl compounds), which is a child of GO:0016798 (hydrolase activity, acting on glycosyl bonds), which in turn is a child of GO:0016787 (hydrolase activity). The ontology path confirms GO:0004553 → GO:0016798 → GO:0016787. The catalytic activity (hydrolysis of ADP-ribosyl-glutamate bonds) is a hydrolase reaction. The protein binds zinc (GO:0008270), not magnesium, ruling out D. There is no evidence for URM1 activating enzyme (A) or cysteine desulfurase (C) activity. The expected answer B (hydrolase activity) is the correct parent-level GO term."
  },
  "important_caveats": [
    "The protein's specific annotation (GO:0004553, hydrolase activity, hydrolyzing O-glycosyl compounds) is more precise than the option text 'hydrolase activity' (GO:0016787), but the latter is the correct parent term and is valid as a GO molecular function annotation.",
    "The protein binds zinc ions (GO:0008270), not magnesium ions, making option D specifically incorrect rather than merely unsupported.",
    "The macrodomain fold recognition and reader-vs-hydrolase distinction require specialized knowledge; general sequence heuristics (size, composition) are insufficient for positive identification.",
    "The annotation evidence is experimental (IDA, PubMed:39270823, X-ray crystallography with Zn2+ and ADP-ribose complexes), establishing the function firmly but not making it inferable from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B (hydrolase activity) is supported. A (URM1 activating enzyme) is a specific E1-like activity with no sequence similarity to this protein. C (cysteine desulfurase) is a PLP-dependent sulfurtransferase with no evidence here. D (magnesium ion binding) is contradicted by the zinc-binding annotation. The broad term 'hydrolase activity' (GO:0016787) correctly encompasses the specific annotation GO:0004553 via the is_a hierarchy."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A166ACJ5 (ADPRH_METOA) is experimentally characterized (PubMed:39270823, IDA evidence) as a Protein-ADP-ribose hydrolase with EC 3.2.1.-. It is annotated with GO:0004553 (hydrolase activity, hydrolyzing O-glycosyl compounds), which is a child of GO:0016798 (hydrolase activity, acting on glycosyl bonds), which in turn is a child of GO:0016787 (hydrolase activity). The ontology path confirms GO:0004553 → GO:0016798 → GO:0016787. The catalytic activity (hydrolysis of ADP-ribosyl-glutamate bonds) is a hydrolase reaction. The protein binds zinc (GO:0008270), not magnesium, ruling out D. There is no evidence for URM1 activating enzyme (A) or cysteine desulfurase (C) activity. The expected answer B (hydrolase activity) is the correct parent-level GO term.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H3", "H4", "H5", "GO2", "GO3", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could partially eliminate distractors through general reasoning: URM1 activating enzymes (A) are typically 400+ residue E1-like enzymes with adenylation domains; cysteine desulfurases (C) are ~400 aa PLP-dependent enzymes (IscS/SufS family); magnesium ion binding (D) as a primary molecular function is unusual for a 260-aa protein of this complexity. However, positively identifying 'hydrolase activity' requires recognizing the macrodomain fold (MorMacro) and knowing that this particular macrodomain variant is a zinc-dependent hydrolase (eraser) rather than an ADP-ribose reader. The distinction between reader and hydrolase macrodomains depends on specific catalytic residues (the conserved Glu in the E-x-x-E motif) and the zinc-coordinating site, which is specialized family knowledge not derivable from general sequence features alone.",
    "missing_item_specific_fact": "The identification of this protein as a macrodomain-family ADP-ribosylhydrolase (rather than a reader or other fold) requires knowledge of the MorMacro protein family and its zinc-dependent catalytic mechanism for hydrolyzing ADP-ribosyl-glutamate bonds, established experimentally in PubMed:39270823. Without recognizing the macrodomain fold and knowing the catalytic Glu/Zn site, one cannot positively assign hydrolase activity from the 260-aa sequence alone.",
    "reason": "While elimination of clearly wrong distractors (A, C) is possible via size/family heuristics, the positive assignment of 'hydrolase activity' as the primary molecular function depends on recognizing the macrodomain fold and knowing that this specific variant is a catalytic hydrolase rather than a binding reader. This is protein-family-specific knowledge, not derivable from general biological reasoning applied to the raw sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B (hydrolase activity) is supported. A (URM1 activating enzyme) is a specific E1-like activity with no sequence similarity to this protein. C (cysteine desulfurase) is a PLP-dependent sulfurtransferase with no evidence here. D (magnesium ion binding) is contradicted by the zinc-binding annotation. The broad term 'hydrolase activity' (GO:0016787) correctly encompasses the specific annotation GO:0004553 via the is_a hierarchy."
  },
  "important_caveats": [
    "The protein's specific annotation (GO:0004553, hydrolase activity, hydrolyzing O-glycosyl compounds) is more precise than the option text 'hydrolase activity' (GO:0016787), but the latter is the correct parent term and is valid as a GO molecular function annotation.",
    "The protein binds zinc ions (GO:0008270), not magnesium ions, making option D specifically incorrect rather than merely unsupported.",
    "The macrodomain fold recognition and reader-vs-hydrolase distinction require specialized knowledge; general sequence heuristics (size, composition) are insufficient for positive identification.",
    "The annotation evidence is experimental (IDA, PubMed:39270823, X-ray crystallography with Zn2+ and ADP-ribose complexes), establishing the function firmly but not making it inferable from sequence alone."
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

**Accession:** `A0A166ACJ5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 27. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:27.127121+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39270823","source":"PubMed"}],"value":"MorMacro"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"}],"value":"3.2.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Protein-ADP-ribose hydrolase"}}}
```

Source SHA-256: `dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:27.127121+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"}],"value":"ADP-ribosylhydrolase that hydrolyzes ADP-ribosyl-glutamate bonds (PubMed:39270823). In vitro, it can remove the ADP-ribosyl modification from the human mono-ADP-ribosylated PARP1 E988Q mutant, which is primarily modified on glutamate site with only minor aspartate contribution (PubMed:39270823). It cannot hydrolyze the ADP-ribosyl-aspartate bond of ribosylated S.pyogenes GcvH-L (PubMed:39270823)"}]}
```

Source SHA-256: `dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:27.127121+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"}],"name":"5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58248"},{"database":"Rhea","id":"RHEA-COMP:10208"},{"database":"Rhea","id":"RHEA-COMP:15089"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29973"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:142540"}]}}
```

Source SHA-256: `dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:27.127121+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39270823","source":"PubMed"}],"id":"GO:0004553","properties":[{"key":"GoTerm","value":"F:hydrolase activity, hydrolyzing O-glycosyl compounds"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:27.127121+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39270823","source":"PubMed"}],"id":"GO:0008270","properties":[{"key":"GoTerm","value":"F:zinc ion binding"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:29.689150+00:00.  

```text
ID   ADPRH_METOA             Reviewed;         260 AA.
AC   A0A166ACJ5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   06-JUL-2016, sequence version 1.
DT   28-JAN-2026, entry version 27.
DE   RecName: Full=Protein-ADP-ribose hydrolase {ECO:0000305};
DE            EC=3.2.1.- {ECO:0000269|PubMed:39270823};
DE   AltName: Full=MorMacro {ECO:0000303|PubMed:39270823};
GN   ORFNames=MBORA_13990 {ECO:0000312|EMBL:KZX11859.1};
OS   Methanobrevibacter oralis.
OC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;
OC   Methanobacteria; Methanobacteriales; Methanobacteriaceae;
OC   Methanobrevibacter.
OX   NCBI_TaxID=66851;
```

Source SHA-256: `f41d9345e837fc4cf2fc216b27d3d0376b1a15c8a77bce7c0dd1066928158c4f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27)  
**Locator:** `lines 33-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:29.689150+00:00.  

```text
CC   -!- FUNCTION: ADP-ribosylhydrolase that hydrolyzes ADP-ribosyl-glutamate
CC       bonds (PubMed:39270823). In vitro, it can remove the ADP-ribosyl
CC       modification from the human mono-ADP-ribosylated PARP1 E988Q mutant,
CC       which is primarily modified on glutamate site with only minor aspartate
CC       contribution (PubMed:39270823). It cannot hydrolyze the ADP-ribosyl-
CC       aspartate bond of ribosylated S.pyogenes GcvH-L (PubMed:39270823).
CC       {ECO:0000269|PubMed:39270823}.
```

Source SHA-256: `f41d9345e837fc4cf2fc216b27d3d0376b1a15c8a77bce7c0dd1066928158c4f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27)  
**Locator:** `lines 40-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:29.689150+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-
CC         [protein] + ADP-D-ribose + H(+); Xref=Rhea:RHEA:58248, Rhea:RHEA-
CC         COMP:10208, Rhea:RHEA-COMP:15089, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29973, ChEBI:CHEBI:57967,
CC         ChEBI:CHEBI:142540; Evidence={ECO:0000269|PubMed:39270823};
```

Source SHA-256: `f41d9345e837fc4cf2fc216b27d3d0376b1a15c8a77bce7c0dd1066928158c4f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27)  
**Locator:** `lines 71-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:29.689150+00:00.  

```text
DR   GO; GO:0004553; F:hydrolase activity, hydrolyzing O-glycosyl compounds; IDA:UniProtKB.
```

Source SHA-256: `f41d9345e837fc4cf2fc216b27d3d0376b1a15c8a77bce7c0dd1066928158c4f`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 44250-44263`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004553
name: hydrolase activity, hydrolyzing O-glycosyl compounds
namespace: molecular_function
alt_id: GO:0016800
def: "Catalysis of the hydrolysis of any O-glycosyl bond." [GOC:mah]
synonym: "O-glucosyl hydrolase activity" EXACT []
xref: EC:3.2.1.-
xref: Reactome:R-HSA-5694563 "ABHD10 hydrolyses MPAG"
xref: Reactome:R-HSA-6786652 "CHIT1 hydrolyses CHIT to 3xADGP"
xref: Reactome:R-HSA-9661820 "Bacterial GUSB hydrolyses BDG to BIL"
is_a: GO:0016798 ! hydrolase activity, acting on glycosyl bonds
property_value: skos:exactMatch EC:3.2.1.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 130166-130193`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016787
name: hydrolase activity
namespace: molecular_function
def: "Catalysis of the hydrolysis of various bonds, e.g. C-O, C-N, C-C, phosphoric anhydride bonds, etc." [ISBN:0198506732]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_prokaryote
subset: goslim_yeast
xref: EC:3.-.-.-
xref: Reactome:R-HSA-1236938 "Partial proteolysis of antigen in phagolysosomes"
xref: Reactome:R-HSA-2029475 "Production of AA by iPLA2 upon FCGR activation"
xref: Reactome:R-HSA-5694583 "ABHD4 hydrolyses NAPE"
xref: Reactome:R-HSA-5695964 "ABHD14B hydrolyses PNPB"
xref: Reactome:R-HSA-6786190 "CMBL hydrolyses OM to OLMS"
xref: Reactome:R-HSA-6788295 "HDHD1:Mg2+ dephosphorylates PURIDP"
xref: Reactome:R-HSA-8938314 "ENPPs hydrolyse CoA-SH to PPANT, PAP"
xref: Reactome:R-HSA-8952137 "Phospholipid phosphatase 6 hydrolyses Presqualene diphosphate to presqualene monophosphate"
xref: Reactome:R-HSA-9942295 "QNG1 hydrolyzes queuosine 5'-monophosphate yielding queuine and ribose 5'-monophosphate"
is_a: GO:0003824 ! catalytic activity
property_value: skos:exactMatch EC:3.-.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 130290-130307`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016798
name: hydrolase activity, acting on glycosyl bonds
namespace: molecular_function
def: "Catalysis of the hydrolysis of any glycosyl bond." [GOC:jl]
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_yeast
synonym: "glycosidase activity" EXACT []
synonym: "glycosylase" NARROW []
synonym: "N-glycosylase" NARROW []
xref: EC:3.2.-.-
xref: Reactome:R-HSA-1793176 "DS is cleaved from its proteoglycan"
xref: Reactome:R-HSA-2065233 "CS is cleaved from its proteoglycan"
xref: Reactome:R-HSA-5333609 "MeSebGalNac is hydrolysed to MeSeH and bGalNac"
is_a: GO:0016787 ! hydrolase activity
property_value: skos:exactMatch EC:3.2.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 163. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
