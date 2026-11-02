# GO_molecular_function_0178

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — structural constituent of ribosome

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSEKAQNPMRELRIQKLVLNISVGESGDRLTRAAKVLEQLSGQTPVYSKARYTVRQFGIRRNEKIAVHVTVRGPKAEEILERGLKVKEYELRRRNFSETGNFGFGISEHIDLGIKYDPSIGIYGMDFYCCMTRPGERVAKRRRCKSRIGASHRITREETIRWFKQRFDGIVR

[Multiple Choices]
A. UDP-glucosyltransferase activity
B. mRNA binding
C. structural constituent of ribosome
D. ABC-type oligopeptide transporter activity
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

> The supplied sequence exactly matches the entry annotated as large ribosomal subunit protein uL5, and the entry describes it as a ribosome component. The GO annotation for “structural constituent of ribosome” is IEA:InterPro (computational), while the cited function record provides supporting ribosome context; this supports choice C without implying a direct assay of that precise molecular-function term.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The compact, basic sequence is compatible with an RNA-associated protein, and its lack of membrane-spanning regions argues against the ABC transporter choice. Those broad clues do not reliably distinguish a ribosomal structural role from mRNA binding or identify this protein as uL5.


**Missing item-specific fact**

> The protein-specific identification as ribosomal protein uL5, or equivalent homology/annotation evidence, is not supplied in the question.


**Reason**

> Choosing C over the plausible RNA-binding alternative requires recognizing or externally identifying this particular protein; generic sequence reasoning does not establish its precise GO molecular function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone does not clearly distinguish the RNA-related choices, but the sequence-matched evidence supports C as the expected answer.


### Important caveats

- The cited GO:0003735 annotation is computational (IEA:InterPro), not a direct experimental demonstration of that specific molecular-function term.
- The evidence matches the supplied sequence, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The compact, basic sequence is compatible with an RNA-associated protein, and its lack of membrane-spanning regions argues against the ABC transporter choice. Those broad clues do not reliably distinguish a ribosomal structural role from mRNA binding or identify this protein as uL5.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as ribosomal protein uL5, or equivalent homology/annotation evidence, is not supplied in the question.",
    "reason": "Choosing C over the plausible RNA-binding alternative requires recognizing or externally identifying this particular protein; generic sequence reasoning does not establish its precise GO molecular function."
  },
  "case_id": "GO_molecular_function_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the entry annotated as large ribosomal subunit protein uL5, and the entry describes it as a ribosome component. The GO annotation for “structural constituent of ribosome” is IEA:InterPro (computational), while the cited function record provides supporting ribosome context; this supports choice C without implying a direct assay of that precise molecular-function term."
  },
  "important_caveats": [
    "The cited GO:0003735 annotation is computational (IEA:InterPro), not a direct experimental demonstration of that specific molecular-function term.",
    "The evidence matches the supplied sequence, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not clearly distinguish the RNA-related choices, but the sequence-matched evidence supports C as the expected answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the entry annotated as large ribosomal subunit protein uL5, and the entry describes it as a ribosome component. The GO annotation for “structural constituent of ribosome” is IEA:InterPro (computational), while the cited function record provides supporting ribosome context; this supports choice C without implying a direct assay of that precise molecular-function term.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The compact, basic sequence is compatible with an RNA-associated protein, and its lack of membrane-spanning regions argues against the ABC transporter choice. Those broad clues do not reliably distinguish a ribosomal structural role from mRNA binding or identify this protein as uL5.",
    "missing_item_specific_fact": "The protein-specific identification as ribosomal protein uL5, or equivalent homology/annotation evidence, is not supplied in the question.",
    "reason": "Choosing C over the plausible RNA-binding alternative requires recognizing or externally identifying this particular protein; generic sequence reasoning does not establish its precise GO molecular function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not clearly distinguish the RNA-related choices, but the sequence-matched evidence supports C as the expected answer."
  },
  "important_caveats": [
    "The cited GO:0003735 annotation is computational (IEA:InterPro), not a direct experimental demonstration of that specific molecular-function term.",
    "The evidence matches the supplied sequence, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (173 aa, SHA256-matched) corresponds to UniProt G0SHQ2, annotated as 'Large ribosomal subunit protein uL5' (60S ribosomal protein L11) from Chaetomium thermophilum. The GO annotation GO:0003735 'structural constituent of ribosome' is present (IEA:InterPro), and the FUNCTION comment confirms it is a component of the ribosome. A cryo-EM structure (PDB 7OZS) confirms its role in the 5S RNP/ribosome assembly complex. Multiple independent evidence sources (protein name, function comment, GO annotation, structural evidence) all support choice C.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is only 173 aa and highly basic (abundant Lys/Arg residues throughout), with no transmembrane segments, no Walker A/B ATPase motifs in proper context, no glycosyltransferase catalytic domain, and no canonical mRNA-binding domain motifs (RRM, KH, PUA, etc.). ABC transporters (D) require ~500+ aa with transmembrane helices and nucleotide-binding domains; UDP-glucosyltransferases (A) are typically 300-500+ aa with PSPG-box-like catalytic motifs. The extreme basicity combined with very small size and absence of specific RNA-binding domain architecture is a hallmark of ribosomal proteins that pack electrostatically with rRNA, distinguishing C from B (mRNA-binding proteins typically possess recognizable RRM/KH domains and are often larger).


**Missing item-specific fact**

> None strictly required; however, the final C-vs-B distinction is somewhat subtle and relies on recognizing that extreme basicity + very small size + absence of specific RNA-binding domain motifs is more diagnostic of ribosomal proteins than of general mRNA-binding proteins.


**Reason**

> General biological knowledge about protein size constraints (eliminating A and D), the hallmark basic character of ribosomal proteins, and the absence of specific catalytic or RNA-binding domain motifs provides a defensible reasoning path to C. The B-vs-C distinction is addressable by noting that mRNA-binding proteins typically possess identifiable RRM, KH, or other specific RNA-binding folds, whereas this sequence's extreme basicity and small size are characteristic of ribosomal protein architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B (mRNA binding) might superficially seem plausible given the basic character, the absence of any canonical RNA-binding domain fold (RRM, KH, etc.) and the very small size make C the clearly better answer. A and D are ruled out by size and domain architecture. No other option is genuinely defensible.


### Important caveats

- The GO annotation for this entry is IEA:InterPro (computational transfer), not directly experimental for the GO term itself, though the protein's ribosomal identity is confirmed by cryo-EM structure (PDB 7OZS, ECO:0007744).
- The sequence contains 'GESGD' near the N-terminus which could superficially resemble a Walker A motif, but it lacks the canonical GxxxxGK&#91;ST&#93; consensus and the protein has no transmembrane topology, making ABC transporter activity implausible.
- The entry was first publicly released 2025-02-05; the author's exact source snapshot is unknown, though the sequence matches across all checked versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is only 173 aa and highly basic (abundant Lys/Arg residues throughout), with no transmembrane segments, no Walker A/B ATPase motifs in proper context, no glycosyltransferase catalytic domain, and no canonical mRNA-binding domain motifs (RRM, KH, PUA, etc.). ABC transporters (D) require ~500+ aa with transmembrane helices and nucleotide-binding domains; UDP-glucosyltransferases (A) are typically 300-500+ aa with PSPG-box-like catalytic motifs. The extreme basicity combined with very small size and absence of specific RNA-binding domain architecture is a hallmark of ribosomal proteins that pack electrostatically with rRNA, distinguishing C from B (mRNA-binding proteins typically possess recognizable RRM/KH domains and are often larger).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, the final C-vs-B distinction is somewhat subtle and relies on recognizing that extreme basicity + very small size + absence of specific RNA-binding domain motifs is more diagnostic of ribosomal proteins than of general mRNA-binding proteins.",
    "reason": "General biological knowledge about protein size constraints (eliminating A and D), the hallmark basic character of ribosomal proteins, and the absence of specific catalytic or RNA-binding domain motifs provides a defensible reasoning path to C. The B-vs-C distinction is addressable by noting that mRNA-binding proteins typically possess identifiable RRM, KH, or other specific RNA-binding folds, whereas this sequence's extreme basicity and small size are characteristic of ribosomal protein architecture."
  },
  "case_id": "GO_molecular_function_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence (173 aa, SHA256-matched) corresponds to UniProt G0SHQ2, annotated as 'Large ribosomal subunit protein uL5' (60S ribosomal protein L11) from Chaetomium thermophilum. The GO annotation GO:0003735 'structural constituent of ribosome' is present (IEA:InterPro), and the FUNCTION comment confirms it is a component of the ribosome. A cryo-EM structure (PDB 7OZS) confirms its role in the 5S RNP/ribosome assembly complex. Multiple independent evidence sources (protein name, function comment, GO annotation, structural evidence) all support choice C."
  },
  "important_caveats": [
    "The GO annotation for this entry is IEA:InterPro (computational transfer), not directly experimental for the GO term itself, though the protein's ribosomal identity is confirmed by cryo-EM structure (PDB 7OZS, ECO:0007744).",
    "The sequence contains 'GESGD' near the N-terminus which could superficially resemble a Walker A motif, but it lacks the canonical GxxxxGK[ST] consensus and the protein has no transmembrane topology, making ABC transporter activity implausible.",
    "The entry was first publicly released 2025-02-05; the author's exact source snapshot is unknown, though the sequence matches across all checked versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B (mRNA binding) might superficially seem plausible given the basic character, the absence of any canonical RNA-binding domain fold (RRM, KH, etc.) and the very small size make C the clearly better answer. A and D are ruled out by size and domain architecture. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (173 aa, SHA256-matched) corresponds to UniProt G0SHQ2, annotated as 'Large ribosomal subunit protein uL5' (60S ribosomal protein L11) from Chaetomium thermophilum. The GO annotation GO:0003735 'structural constituent of ribosome' is present (IEA:InterPro), and the FUNCTION comment confirms it is a component of the ribosome. A cryo-EM structure (PDB 7OZS) confirms its role in the 5S RNP/ribosome assembly complex. Multiple independent evidence sources (protein name, function comment, GO annotation, structural evidence) all support choice C.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is only 173 aa and highly basic (abundant Lys/Arg residues throughout), with no transmembrane segments, no Walker A/B ATPase motifs in proper context, no glycosyltransferase catalytic domain, and no canonical mRNA-binding domain motifs (RRM, KH, PUA, etc.). ABC transporters (D) require ~500+ aa with transmembrane helices and nucleotide-binding domains; UDP-glucosyltransferases (A) are typically 300-500+ aa with PSPG-box-like catalytic motifs. The extreme basicity combined with very small size and absence of specific RNA-binding domain architecture is a hallmark of ribosomal proteins that pack electrostatically with rRNA, distinguishing C from B (mRNA-binding proteins typically possess recognizable RRM/KH domains and are often larger).",
    "missing_item_specific_fact": "None strictly required; however, the final C-vs-B distinction is somewhat subtle and relies on recognizing that extreme basicity + very small size + absence of specific RNA-binding domain motifs is more diagnostic of ribosomal proteins than of general mRNA-binding proteins.",
    "reason": "General biological knowledge about protein size constraints (eliminating A and D), the hallmark basic character of ribosomal proteins, and the absence of specific catalytic or RNA-binding domain motifs provides a defensible reasoning path to C. The B-vs-C distinction is addressable by noting that mRNA-binding proteins typically possess identifiable RRM, KH, or other specific RNA-binding folds, whereas this sequence's extreme basicity and small size are characteristic of ribosomal protein architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B (mRNA binding) might superficially seem plausible given the basic character, the absence of any canonical RNA-binding domain fold (RRM, KH, etc.) and the very small size make C the clearly better answer. A and D are ruled out by size and domain architecture. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The GO annotation for this entry is IEA:InterPro (computational transfer), not directly experimental for the GO term itself, though the protein's ribosomal identity is confirmed by cryo-EM structure (PDB 7OZS, ECO:0007744).",
    "The sequence contains 'GESGD' near the N-terminus which could superficially resemble a Walker A motif, but it lacks the canonical GxxxxGK[ST] consensus and the protein has no transmembrane topology, making ABC transporter activity implausible.",
    "The entry was first publicly released 2025-02-05; the author's exact source snapshot is unknown, though the sequence matches across all checked versions."
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

**Accession:** `G0SHQ2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 53. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SHQ2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:28.267161+00:00.  

```json
"G0SHQ2"
```

Source SHA-256: `93360df0d16107081f9d9e8f13a70e6d32229c478daab4d9194a6b07f3ea13c6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SHQ2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:28.267161+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"60S ribosomal protein L11"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"ctRPL11"}]}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"Large ribosomal subunit protein uL5"}}}
```

Source SHA-256: `93360df0d16107081f9d9e8f13a70e6d32229c478daab4d9194a6b07f3ea13c6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SHQ2.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:28.267161+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"37291423","source":"PubMed"}],"value":"Component of the ribosome, a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell (PubMed:37291423). The small ribosomal subunit (SSU) binds messenger RNAs (mRNAs) and translates the encoded message by selecting cognate aminoacyl-transfer RNA (tRNA) molecules. The large subunit (LSU) contains the ribosomal catalytic site termed the peptidyl transferase center (PTC), which catalyzes the formation of peptide bonds, thereby polymerizing the amino acids delivered by tRNAs into a polypeptide chain. The nascent polypeptides leave the ribosome through a tunnel in the LSU and interact with protein factors that function in enzymatic processing, targeting, and the membrane insertion of nascent chains at the exit of the ribosomal tunnel"}]}
```

Source SHA-256: `93360df0d16107081f9d9e8f13a70e6d32229c478daab4d9194a6b07f3ea13c6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SHQ2.json)  
**Locator:** `/uniProtKBCrossReferences/71`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:28.267161+00:00.  

```json
{"database":"GO","id":"GO:0003735","properties":[{"key":"GoTerm","value":"F:structural constituent of ribosome"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `93360df0d16107081f9d9e8f13a70e6d32229c478daab4d9194a6b07f3ea13c6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SHQ2.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:28.267161+00:00.  

```json
{"citation":{"authors":["Castillo Duque de Estrada N.M.","Thoms M.","Flemming D.","Hammaren H.M.","Buschauer R.","Ameismeier M.","Bassler J.","Beck M.","Beckmann R.","Hurt E."],"citationCrossReferences":[{"database":"PubMed","id":"37291423"},{"database":"DOI","id":"10.1038/s41594-023-01006-7"}],"citationType":"journal article","firstPage":"1119","id":"37291423","journal":"Nat. Struct. Mol. Biol.","lastPage":"1131","publicationDate":"2023","title":"Structure of nascent 5S RNPs at the crossroad between ribosome assembly and MDM2-p53 pathways.","volume":"30"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7OZS","source":"PDB"}],"referenceNumber":7,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (3.50 ANGSTROMS) IN COMPLEX WITH RPL5; RRS1; RPF2; SYO1 AND 5S RNA","FUNCTION","SUBUNIT"]}
```

Source SHA-256: `93360df0d16107081f9d9e8f13a70e6d32229c478daab4d9194a6b07f3ea13c6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SHQ2?format=txt&versions=53)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 53 / 1.  
**Retrieved:** 2026-11-02T04:28:31.089069+00:00.  

```text
ID   RL11_CHATD              Reviewed;         173 AA.
AC   G0SHQ2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-OCT-2011, sequence version 1.
DT   28-JAN-2026, entry version 53.
DE   RecName: Full=Large ribosomal subunit protein uL5 {ECO:0000305|PubMed:37291423};
DE   AltName: Full=60S ribosomal protein L11 {ECO:0000305|PubMed:37291423};
DE            Short=ctRPL11 {ECO:0000305|PubMed:37291423};
GN   ORFNames=HT_0072970 {ECO:0000312|EMBL:EGS16972.1};
OS   Chaetomium thermophilum (strain DSM 1495 / CBS 144.50 / IMI 039719)
OS   (Thermochaetoides thermophila).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Thermochaetoides.
OX   NCBI_TaxID=759272;
```

Source SHA-256: `72c3302c793ecbc5f0bfc6b777abbb1139c3555a4df5e636bd916a71b826d7f8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SHQ2?format=txt&versions=53)  
**Locator:** `lines 79-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 53 / 1.  
**Retrieved:** 2026-11-02T04:28:31.089069+00:00.  

```text
CC   -!- FUNCTION: Component of the ribosome, a large ribonucleoprotein complex
CC       responsible for the synthesis of proteins in the cell
CC       (PubMed:37291423). The small ribosomal subunit (SSU) binds messenger
CC       RNAs (mRNAs) and translates the encoded message by selecting cognate
CC       aminoacyl-transfer RNA (tRNA) molecules. The large subunit (LSU)
CC       contains the ribosomal catalytic site termed the peptidyl transferase
CC       center (PTC), which catalyzes the formation of peptide bonds, thereby
CC       polymerizing the amino acids delivered by tRNAs into a polypeptide
CC       chain. The nascent polypeptides leave the ribosome through a tunnel in
CC       the LSU and interact with protein factors that function in enzymatic
CC       processing, targeting, and the membrane insertion of nascent chains at
CC       the exit of the ribosomal tunnel. {ECO:0000269|PubMed:37291423}.
```

Source SHA-256: `72c3302c793ecbc5f0bfc6b777abbb1139c3555a4df5e636bd916a71b826d7f8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SHQ2?format=txt&versions=53)  
**Locator:** `lines 164-164`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 53 / 1.  
**Retrieved:** 2026-11-02T04:28:31.089069+00:00.  

```text
DR   GO; GO:0003735; F:structural constituent of ribosome; IEA:InterPro.
```

Source SHA-256: `72c3302c793ecbc5f0bfc6b777abbb1139c3555a4df5e636bd916a71b826d7f8`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 28381-28401`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0003735
name: structural constituent of ribosome
namespace: molecular_function
alt_id: GO:0003736
alt_id: GO:0003737
alt_id: GO:0003738
alt_id: GO:0003739
alt_id: GO:0003740
alt_id: GO:0003741
alt_id: GO:0003742
def: "The action of a molecule that contributes to the structural integrity of the ribosome." [GOC:mah]
comment: Note that this term may be used to annotate ribosomal RNAs as well as ribosomal proteins.
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_metagenomics
subset: goslim_yeast
synonym: "ribosomal protein" BROAD []
synonym: "ribosomal RNA" RELATED []
is_a: GO:0005198 ! structural molecule activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 178. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
