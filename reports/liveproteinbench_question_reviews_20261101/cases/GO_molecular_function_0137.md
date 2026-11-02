# GO_molecular_function_0137

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — poly(A) binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDTGGHGCSLSSLYVGDLHPDVTESMLYEMFSPIGNILSIRVCRDVATRRSLGYAYINFQQPADAERALDTMNFEVIKGQPIRIMWSHRDPGLRKSGMGNIFIKNLENSIDNKALYDTFSTFGSILSSKVVYNEHGSRGFGFVHFETHEAAQKAINTMNGMLLNDRKVFVGHFKSRQKREAELGARALGFTNIYVKNLHANVDEQRLQDLFSQFGNMQSVKVMRDSNGQSRGFGFVNFEKHEEAQKAVDHMNGKEVSGQLLYVGRAQKRAERQSELKRRFEQMKQERQNRYQGVNLYVKNLDDSINDERLKEVFSTYGVITSAKVMTESSHSKGFGFVCFSSPEEATKAVTEMNGRIVGTKPLYVALAQRKEERKAILTNQYRRRPSHPVLSSFQQPTSYLLPAVPQSTAQAVYYSSGSITPMQPDPRWTAQPHGPPSTCPPAASVVQPLSTTQHPCIHLRGASQVSSQVPHTQRVVNIGTQTTGPGGEGSSIPGQLLVPHRGTSAVHSAHGVQESAVYVPGHQPLTVSMLAAAPLHEQKQMIGERLYSLIHDACAPLTGKITGMLLELDNLELLLLLESPESLHAKIEEAVAVLQVHREMESTDRN

[Multiple Choices]
A. translation regulator activity
B. enoyl-[acyl-carrier-protein] reductase (NADPH) activity
C. beta-catenin binding
D. poly(A) binding
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

> The supplied sequence exactly matches the mouse UniProt entry for polyadenylate-binding protein 1-like. Its annotation identifies poly(A) binding, and its function description cites experimental evidence for a poly(A)-binding role.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a characteristic PABP-like architecture: multiple N-terminal RNA-recognition motifs with conserved aromatic RNP-region patterns, followed by a C-terminal PABC-like region. This supports poly(A)-binding protein function over the enzyme and beta-catenin-binding choices.


**Missing item-specific fact**

> No external fact is strictly needed to favor D; recognizing the protein family from its sequence architecture provides a biological basis for the choice.


**Reason**

> The sequence contains recognizable family-level structural motifs that distinguish a PABP-like RNA-binding protein from the alternatives. This is a sequence-based inference, not reliance on remembering an accession or database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Translation regulation is a role associated with this protein, but poly(A) binding is the more direct molecular activity asked for and best distinguishes its primary function among the options.


### Important caveats

- The reviewer-only annotation supports the key but was not supplied to the evaluated model.
- The sequence match and cited experimental support establish the expected answer; they do not imply that every listed biological role is the protein's only function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a characteristic PABP-like architecture: multiple N-terminal RNA-recognition motifs with conserved aromatic RNP-region patterns, followed by a C-terminal PABC-like region. This supports poly(A)-binding protein function over the enzyme and beta-catenin-binding choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external fact is strictly needed to favor D; recognizing the protein family from its sequence architecture provides a biological basis for the choice.",
    "reason": "The sequence contains recognizable family-level structural motifs that distinguish a PABP-like RNA-binding protein from the alternatives. This is a sequence-based inference, not reliance on remembering an accession or database annotation."
  },
  "case_id": "GO_molecular_function_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H5",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mouse UniProt entry for polyadenylate-binding protein 1-like. Its annotation identifies poly(A) binding, and its function description cites experimental evidence for a poly(A)-binding role."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not supplied to the evaluated model.",
    "The sequence match and cited experimental support establish the expected answer; they do not imply that every listed biological role is the protein's only function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Translation regulation is a role associated with this protein, but poly(A) binding is the more direct molecular activity asked for and best distinguishes its primary function among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mouse UniProt entry for polyadenylate-binding protein 1-like. Its annotation identifies poly(A) binding, and its function description cites experimental evidence for a poly(A)-binding role.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H5", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a characteristic PABP-like architecture: multiple N-terminal RNA-recognition motifs with conserved aromatic RNP-region patterns, followed by a C-terminal PABC-like region. This supports poly(A)-binding protein function over the enzyme and beta-catenin-binding choices.",
    "missing_item_specific_fact": "No external fact is strictly needed to favor D; recognizing the protein family from its sequence architecture provides a biological basis for the choice.",
    "reason": "The sequence contains recognizable family-level structural motifs that distinguish a PABP-like RNA-binding protein from the alternatives. This is a sequence-based inference, not reliance on remembering an accession or database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Translation regulation is a role associated with this protein, but poly(A) binding is the more direct molecular activity asked for and best distinguishes its primary function among the options."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not supplied to the evaluated model.",
    "The sequence match and cited experimental support establish the expected answer; they do not imply that every listed biological role is the protein's only function."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A2A5N3 (PABPC1L_MOUSE, Polyadenylate-binding protein 1-like / Embryonic poly(A)-binding protein). GO:0008143 (poly(A) binding) is annotated with ISO:GO_Central evidence (C7, H7). The protein is explicitly named as a poly(A)-binding protein (C4, H1), and experimental papers (PubMed:22621333, PubMed:37052235) confirm its role in cytosolic mRNA polyadenylation and translational activation of maternally stored mRNA (C5, H5). The GO term definition (GO2) matches the option text exactly. The evidence code ISO:GO_Central indicates inference by orthology rather than direct biochemical assay, but the protein's identity and function are well-established.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H5](#evidence-h5), [H7](#evidence-h7), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple tandem RNA Recognition Motif (RRM) domains bearing the highly characteristic 'GFGF' motif (visible as GFGFVHFETHEAAQK, GFGFVNFEKHEEAQK, GFGFVCFSSPEEATK), which is the hallmark signature of the PABP (poly(A)-binding protein) family. A model recognizing RRM domains can infer RNA binding, and the specific GFGF pattern in a tandem RRM arrangement points to the PABP family, whose defining molecular function is poly(A) tail binding. Option B (enoyl-ACP reductase) is excluded by the absence of any catalytic or Rossmann-fold motifs. Option C (beta-catenin binding) is excluded by the absence of armadillo/HEAT-like protein-protein interaction domains. Option A (translation regulator activity) is a broad regulatory GO term; the question asks for the primary molecular function, which for a PABP-family protein is the specific binding activity (poly(A) binding) rather than the downstream regulatory effect.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GFGF motif in tandem RRM domains is a well-known, recognizable family signature for PABP proteins. A model with general knowledge of RNA-binding domain families can identify RRM domains from the sequence and recognize the GFGF pattern as PABP-specific, then conclude poly(A) binding. The distractors B and C are eliminable by domain architecture reasoning. The distinction between A and D relies on the standard GO convention that the primary molecular function of a binding protein is its binding activity, not its downstream regulatory role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A (translation regulator activity) could be loosely associated with PABP function since PABPs participate in translation initiation, but in GO molecular function ontology the primary activity assigned to PABP proteins is the binding function (poly(A) binding), and the question explicitly asks for the 'primary molecular function.' Options B and C are clearly incompatible with the domain architecture. No other option is defensible.


### Important caveats

- The GO:0008143 annotation uses evidence code ISO:GO_Central (inferred by sequence orthology from GO_Central), not a direct biochemical binding assay on this specific protein. However, the protein's identity as a PABP-family member is supported by multiple experimental studies on its function.
- The protein also carries GO:0008266 (poly(U) RNA binding) by IBA, indicating some broader RNA-binding capability, but poly(A) binding remains the defining and primary molecular function.
- The GFGF RRM motif is a family-level signature; a model must recognize it as PABP-specific rather than a generic RRM pattern to arrive at poly(A) binding specifically.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple tandem RNA Recognition Motif (RRM) domains bearing the highly characteristic 'GFGF' motif (visible as GFGFVHFETHEAAQK, GFGFVNFEKHEEAQK, GFGFVCFSSPEEATK), which is the hallmark signature of the PABP (poly(A)-binding protein) family. A model recognizing RRM domains can infer RNA binding, and the specific GFGF pattern in a tandem RRM arrangement points to the PABP family, whose defining molecular function is poly(A) tail binding. Option B (enoyl-ACP reductase) is excluded by the absence of any catalytic or Rossmann-fold motifs. Option C (beta-catenin binding) is excluded by the absence of armadillo/HEAT-like protein-protein interaction domains. Option A (translation regulator activity) is a broad regulatory GO term; the question asks for the primary molecular function, which for a PABP-family protein is the specific binding activity (poly(A) binding) rather than the downstream regulatory effect.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GFGF motif in tandem RRM domains is a well-known, recognizable family signature for PABP proteins. A model with general knowledge of RNA-binding domain families can identify RRM domains from the sequence and recognize the GFGF pattern as PABP-specific, then conclude poly(A) binding. The distractors B and C are eliminable by domain architecture reasoning. The distinction between A and D relies on the standard GO convention that the primary molecular function of a binding protein is its binding activity, not its downstream regulatory role."
  },
  "case_id": "GO_molecular_function_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H5",
      "H7",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A2A5N3 (PABPC1L_MOUSE, Polyadenylate-binding protein 1-like / Embryonic poly(A)-binding protein). GO:0008143 (poly(A) binding) is annotated with ISO:GO_Central evidence (C7, H7). The protein is explicitly named as a poly(A)-binding protein (C4, H1), and experimental papers (PubMed:22621333, PubMed:37052235) confirm its role in cytosolic mRNA polyadenylation and translational activation of maternally stored mRNA (C5, H5). The GO term definition (GO2) matches the option text exactly. The evidence code ISO:GO_Central indicates inference by orthology rather than direct biochemical assay, but the protein's identity and function are well-established."
  },
  "important_caveats": [
    "The GO:0008143 annotation uses evidence code ISO:GO_Central (inferred by sequence orthology from GO_Central), not a direct biochemical binding assay on this specific protein. However, the protein's identity as a PABP-family member is supported by multiple experimental studies on its function.",
    "The protein also carries GO:0008266 (poly(U) RNA binding) by IBA, indicating some broader RNA-binding capability, but poly(A) binding remains the defining and primary molecular function.",
    "The GFGF RRM motif is a family-level signature; a model must recognize it as PABP-specific rather than a generic RRM pattern to arrive at poly(A) binding specifically."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (translation regulator activity) could be loosely associated with PABP function since PABPs participate in translation initiation, but in GO molecular function ontology the primary activity assigned to PABP proteins is the binding function (poly(A) binding), and the question explicitly asks for the 'primary molecular function.' Options B and C are clearly incompatible with the domain architecture. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A2A5N3 (PABPC1L_MOUSE, Polyadenylate-binding protein 1-like / Embryonic poly(A)-binding protein). GO:0008143 (poly(A) binding) is annotated with ISO:GO_Central evidence (C7, H7). The protein is explicitly named as a poly(A)-binding protein (C4, H1), and experimental papers (PubMed:22621333, PubMed:37052235) confirm its role in cytosolic mRNA polyadenylation and translational activation of maternally stored mRNA (C5, H5). The GO term definition (GO2) matches the option text exactly. The evidence code ISO:GO_Central indicates inference by orthology rather than direct biochemical assay, but the protein's identity and function are well-established.",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H5", "H7", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple tandem RNA Recognition Motif (RRM) domains bearing the highly characteristic 'GFGF' motif (visible as GFGFVHFETHEAAQK, GFGFVNFEKHEEAQK, GFGFVCFSSPEEATK), which is the hallmark signature of the PABP (poly(A)-binding protein) family. A model recognizing RRM domains can infer RNA binding, and the specific GFGF pattern in a tandem RRM arrangement points to the PABP family, whose defining molecular function is poly(A) tail binding. Option B (enoyl-ACP reductase) is excluded by the absence of any catalytic or Rossmann-fold motifs. Option C (beta-catenin binding) is excluded by the absence of armadillo/HEAT-like protein-protein interaction domains. Option A (translation regulator activity) is a broad regulatory GO term; the question asks for the primary molecular function, which for a PABP-family protein is the specific binding activity (poly(A) binding) rather than the downstream regulatory effect.",
    "missing_item_specific_fact": "",
    "reason": "The GFGF motif in tandem RRM domains is a well-known, recognizable family signature for PABP proteins. A model with general knowledge of RNA-binding domain families can identify RRM domains from the sequence and recognize the GFGF pattern as PABP-specific, then conclude poly(A) binding. The distractors B and C are eliminable by domain architecture reasoning. The distinction between A and D relies on the standard GO convention that the primary molecular function of a binding protein is its binding activity, not its downstream regulatory role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (translation regulator activity) could be loosely associated with PABP function since PABPs participate in translation initiation, but in GO molecular function ontology the primary activity assigned to PABP proteins is the binding function (poly(A) binding), and the question explicitly asks for the 'primary molecular function.' Options B and C are clearly incompatible with the domain architecture. No other option is defensible."
  },
  "important_caveats": [
    "The GO:0008143 annotation uses evidence code ISO:GO_Central (inferred by sequence orthology from GO_Central), not a direct biochemical binding assay on this specific protein. However, the protein's identity as a PABP-family member is supported by multiple experimental studies on its function.",
    "The protein also carries GO:0008266 (poly(U) RNA binding) by IBA, indicating some broader RNA-binding capability, but poly(A) binding remains the defining and primary molecular function.",
    "The GFGF RRM motif is a family-level signature; a model must recognize it as PABP-specific rather than a generic RRM pattern to arrive at poly(A) binding specifically."
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

**Accession:** `A2A5N3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 130. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2A5N3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:57.258604+00:00.  

```json
"A2A5N3"
```

Source SHA-256: `d566950f6c160c21b495a831c49fe21f6381c9ebe24477f0310c86b9267f4c1f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2A5N3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:57.258604+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"15630085","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"22621333","source":"PubMed"}],"value":"Embryonic poly(A)-binding protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"MGI:1922908","source":"MGI"}],"value":"Poly(A) binding protein, cytoplasmic 1-like"}}],"recommendedName":{"fullName":{"value":"Polyadenylate-binding protein 1-like"}}}
```

Source SHA-256: `d566950f6c160c21b495a831c49fe21f6381c9ebe24477f0310c86b9267f4c1f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2A5N3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:57.258604+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22621333","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"37052235","source":"PubMed"}],"value":"Poly(A)-binding protein involved in oocyte maturation and early embryo development (PubMed:22621333, PubMed:37052235). It is required for cytosolic mRNA polyadenylation and translational activation of maternally stored mRNA in oocytes (PubMed:22621333)"}]}
```

Source SHA-256: `d566950f6c160c21b495a831c49fe21f6381c9ebe24477f0310c86b9267f4c1f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2A5N3.json)  
**Locator:** `/uniProtKBCrossReferences/38`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:57.258604+00:00.  

```json
{"database":"GO","id":"GO:0008143","properties":[{"key":"GoTerm","value":"F:poly(A) binding"},{"key":"GoEvidenceType","value":"ISO:GO_Central"}]}
```

Source SHA-256: `d566950f6c160c21b495a831c49fe21f6381c9ebe24477f0310c86b9267f4c1f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2A5N3?format=txt&versions=130)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-01T06:27:44.941566+00:00.  

```text
ID   PAP1L_MOUSE             Reviewed;         607 AA.
AC   A2A5N3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-FEB-2007, sequence version 1.
DT   28-JAN-2026, entry version 130.
DE   RecName: Full=Polyadenylate-binding protein 1-like;
DE   AltName: Full=Embryonic poly(A)-binding protein {ECO:0000303|PubMed:15630085, ECO:0000303|PubMed:22621333};
DE   AltName: Full=Poly(A) binding protein, cytoplasmic 1-like {ECO:0000312|MGI:MGI:1922908};
GN   Name=Pabpc1l {ECO:0000312|MGI:MGI:1922908};
GN   Synonyms=Epab {ECO:0000303|PubMed:15630085, ECO:0000303|PubMed:22621333,
GN   ECO:0000312|MGI:MGI:1922908};
OS   Mus musculus (Mouse).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Mus; Mus.
OX   NCBI_TaxID=10090;
```

Source SHA-256: `6505f2784a667dbf4f83cdfc24a7d90e7b706c1f1af2f8d90f99f79cb282e5ea`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2A5N3?format=txt&versions=130)  
**Locator:** `lines 55-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-01T06:27:44.941566+00:00.  

```text
CC   -!- FUNCTION: Poly(A)-binding protein involved in oocyte maturation and
CC       early embryo development (PubMed:22621333, PubMed:37052235). It is
CC       required for cytosolic mRNA polyadenylation and translational
CC       activation of maternally stored mRNA in oocytes (PubMed:22621333).
CC       {ECO:0000269|PubMed:22621333, ECO:0000269|PubMed:37052235}.
```

Source SHA-256: `6505f2784a667dbf4f83cdfc24a7d90e7b706c1f1af2f8d90f99f79cb282e5ea`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2A5N3?format=txt&versions=130)  
**Locator:** `lines 112-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-01T06:27:44.941566+00:00.  

```text
DR   GO; GO:0008143; F:poly(A) binding; ISO:GO_Central.
```

Source SHA-256: `6505f2784a667dbf4f83cdfc24a7d90e7b706c1f1af2f8d90f99f79cb282e5ea`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 79994-80004`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008143
name: poly(A) binding
namespace: molecular_function
def: "Binding to a sequence of adenylyl residues in an RNA molecule, such as the poly(A) tail, a sequence of adenylyl residues at the 3' end of eukaryotic mRNA." [GOC:jl]
synonym: "poly(A) binding, within an RNA molecule" EXACT []
synonym: "poly(rA) binding" EXACT [GOC:mah]
synonym: "poly-A binding" EXACT [GOC:mah]
synonym: "polyadenylate binding" EXACT [GOC:mah]
is_a: GO:0070717 ! poly-purine tract binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 137. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
