# GO_molecular_function_0073

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — structural constituent of vitelline membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MCGRRLLFLAAFGCLLANAFSLPATRNEEFDDGFPESEFDYEERHTREIPAQAYAPPIVYNSQSSYSPAKDQGYSAPAAPVYSPAAPSYSAPAAPSYSAPAAPSYSAPAAPSYSAPAAPSYSAPAAPSYSAPASSSYSAPAAPSYSAPAAPSYSAPAAPSYSAPASSSYSAPAAPSYSAPAAPSYSAPAAPSYSAPAAPSYSAPAAPSYSAPAAPSYSAPSAPSYSAQKTSSYSAPAAPSYHAPAAPASSYSAPAGPSYSAPAAPSYSAPSYSAPASSYSALKAPSYSAPAAPSYSAPAAPSYSSSASPSYSSPASSSYSAPAAPTYSAPKAQSYSAPAAPSYSAPAAPSYSAPASSSYSAPAAPSYSAPAAPSYSAPAAPSYSAPASSSYSAPAAPSYSAPAAPSYSAPASSSYSAPAAPSYSAPAAPSYSAPAAPSYSAPAAPSYSAPASSGYSAARAYSAGSAAPASGYSAPKTSSGYSAPASSGSPAASSYSAPASSTASSGYSAPASKSSGYARSEMDHQILGMARTAGGYGSAAPSAAYGAASLPSPPCPKNYVFSCSSVFTPAPCSQGYGY

[Multiple Choices]
A. structural constituent of vitelline membrane
B. odorant binding
C. acid phosphatase activity
D. methylated histone binding
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

> The exact sequence matches the UniProt record for a Drosophila vitelline membrane-like protein. Its annotation says it is incorporated into the vitelline membrane, and the GO term in choice A is assigned to it. The incorporation is supported by a cited experimental-evidence annotation; the GO assignment itself is attributed to computational sequence-based inference (ISM:FlyBase).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic signal sequence suggests secretion, while the very long, low-complexity Ser/Pro/Ala-rich repeat region is more consistent with an extracellular structural protein than with an acid-phosphatase enzyme, a globular odorant-binding protein, or a methylated-histone-binding protein.


**Missing item-specific fact**

> The sequence alone does not establish the specific Drosophila vitelline-membrane location or its experimentally supported role there; that would require protein-specific annotation or experimental evidence.


**Reason**

> The sequence architecture gives meaningful grounds to prefer the secreted structural-protein option over the listed alternatives, although it does not independently prove the precise GO term.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, A best fits the sequence's apparent secreted, repeat-rich structural-protein architecture; the other options are poorly supported by those features.


### Important caveats

- The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown.
- The reviewer-only accession and annotations were not supplied to the evaluated model.
- The GO assignment is reported as computationally inferred, whereas the cited functional annotation describes experimental evidence for incorporation into the vitelline membrane.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal sequence suggests secretion, while the very long, low-complexity Ser/Pro/Ala-rich repeat region is more consistent with an extracellular structural protein than with an acid-phosphatase enzyme, a globular odorant-binding protein, or a methylated-histone-binding protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish the specific Drosophila vitelline-membrane location or its experimentally supported role there; that would require protein-specific annotation or experimental evidence.",
    "reason": "The sequence architecture gives meaningful grounds to prefer the secreted structural-protein option over the listed alternatives, although it does not independently prove the precise GO term."
  },
  "case_id": "GO_molecular_function_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record for a Drosophila vitelline membrane-like protein. Its annotation says it is incorporated into the vitelline membrane, and the GO term in choice A is assigned to it. The incorporation is supported by a cited experimental-evidence annotation; the GO assignment itself is attributed to computational sequence-based inference (ISM:FlyBase)."
  },
  "important_caveats": [
    "The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The reviewer-only accession and annotations were not supplied to the evaluated model.",
    "The GO assignment is reported as computationally inferred, whereas the cited functional annotation describes experimental evidence for incorporation into the vitelline membrane."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, A best fits the sequence's apparent secreted, repeat-rich structural-protein architecture; the other options are poorly supported by those features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record for a Drosophila vitelline membrane-like protein. Its annotation says it is incorporated into the vitelline membrane, and the GO term in choice A is assigned to it. The incorporation is supported by a cited experimental-evidence annotation; the GO assignment itself is attributed to computational sequence-based inference (ISM:FlyBase).",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal sequence suggests secretion, while the very long, low-complexity Ser/Pro/Ala-rich repeat region is more consistent with an extracellular structural protein than with an acid-phosphatase enzyme, a globular odorant-binding protein, or a methylated-histone-binding protein.",
    "missing_item_specific_fact": "The sequence alone does not establish the specific Drosophila vitelline-membrane location or its experimentally supported role there; that would require protein-specific annotation or experimental evidence.",
    "reason": "The sequence architecture gives meaningful grounds to prefer the secreted structural-protein option over the listed alternatives, although it does not independently prove the precise GO term."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, A best fits the sequence's apparent secreted, repeat-rich structural-protein architecture; the other options are poorly supported by those features."
  },
  "important_caveats": [
    "The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The reviewer-only accession and annotations were not supplied to the evaluated model.",
    "The GO assignment is reported as computationally inferred, whereas the cited functional annotation describes experimental evidence for incorporation into the vitelline membrane."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A8JUV4 (VTUL_DROME) is annotated with GO:0008316 (structural constituent of vitelline membrane) with evidence code ISM:FlyBase. The FUNCTION comment (ECO:0000269, PubMed:19540119) confirms it is a 'Major early eggshell protein secreted by follicle cells into the perivitelline space and incorporated into the vitelline membrane.' The protein is named 'Vitelline membrane-like protein.' Sequence match is exact (578 aa, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an N-terminal signal peptide (MCGRRLLFLAAFGCLLANAFSLPATRN), indicating a secreted protein. The bulk of the sequence is dominated by highly repetitive Ser/Tyr/Ala/Pro motifs (SYSAPAAP repeats), characteristic of structural/assembly proteins rather than enzymes or specific ligand-binding proteins. The C-terminal region contains cysteines (…VSCSSVFTPAPCSQGYGY) suggestive of disulfide cross-linking. None of the other three options are compatible: (B) odorant-binding proteins are ~150 aa with a conserved 6-cysteine OB-fold, not a 578-aa repetitive secreted protein; (C) acid phosphatases require a DXDXP catalytic motif and a specific fold, entirely absent here; (D) methylated histone binding requires reader domains (chromodomain, Tudor, PHD, MBT), none present. Among the four choices, only A describes a structural constituent activity, which is the only category consistent with a secreted, repetitive, cross-linking protein.


**Missing item-specific fact**

> Positive identification of 'vitelline membrane' specifically (as opposed to other secreted structural proteins like chorion or cuticle proteins) relies on knowledge that this particular repetitive SYSAPAAP pattern is characteristic of Drosophila vitelline membrane proteins. However, since A is the sole structural option among the four choices, the elimination argument suffices to select it.


**Reason**

> The sequence clearly lacks catalytic residues (no acid phosphatase DXDXP motif), lacks OB-fold/cysteine-stabilized small-binding-protein architecture (odorant binding), and lacks any known chromatin-reader domain (methylated histone binding). The secreted, highly repetitive, cysteine-containing architecture is consistent only with a structural constituent role. Among the four provided options, A is the unique structural-constituent choice, making the answer reachable by elimination without needing to recall the specific protein identity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct functional categories (structural, binding, catalytic, reader-domain binding). The sequence's architecture unambiguously excludes B, C, and D, leaving A as the only defensible choice.


### Important caveats

- The GO annotation evidence code is ISM (Inferred by Sequence or Structural Model) from FlyBase, not a direct experimental structural determination. However, the FUNCTION comment is supported by direct assay (ECO:0000269, PubMed:19540119).
- The specific recognition that the SYSAPAAP repetitive motif is diagnostic of vitelline membrane proteins (vs. other Drosophila eggshell proteins) is domain-specific knowledge; the question is answerable here only because A is the sole structural option among the four choices.
- The protein was first publicly released in UniProt on 2025-02-05; the benchmark construction date is unknown but the sequence has been available in databases since 2007.
- The GO term GO:0008316 is defined with 'An example of this is found in Drosophila melanogaster,' making it a Drosophila-centric term; the reasoning relies on recognizing the organism context or using elimination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an N-terminal signal peptide (MCGRRLLFLAAFGCLLANAFSLPATRN), indicating a secreted protein. The bulk of the sequence is dominated by highly repetitive Ser/Tyr/Ala/Pro motifs (SYSAPAAP repeats), characteristic of structural/assembly proteins rather than enzymes or specific ligand-binding proteins. The C-terminal region contains cysteines (…VSCSSVFTPAPCSQGYGY) suggestive of disulfide cross-linking. None of the other three options are compatible: (B) odorant-binding proteins are ~150 aa with a conserved 6-cysteine OB-fold, not a 578-aa repetitive secreted protein; (C) acid phosphatases require a DXDXP catalytic motif and a specific fold, entirely absent here; (D) methylated histone binding requires reader domains (chromodomain, Tudor, PHD, MBT), none present. Among the four choices, only A describes a structural constituent activity, which is the only category consistent with a secreted, repetitive, cross-linking protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of 'vitelline membrane' specifically (as opposed to other secreted structural proteins like chorion or cuticle proteins) relies on knowledge that this particular repetitive SYSAPAAP pattern is characteristic of Drosophila vitelline membrane proteins. However, since A is the sole structural option among the four choices, the elimination argument suffices to select it.",
    "reason": "The sequence clearly lacks catalytic residues (no acid phosphatase DXDXP motif), lacks OB-fold/cysteine-stabilized small-binding-protein architecture (odorant binding), and lacks any known chromatin-reader domain (methylated histone binding). The secreted, highly repetitive, cysteine-containing architecture is consistent only with a structural constituent role. Among the four provided options, A is the unique structural-constituent choice, making the answer reachable by elimination without needing to recall the specific protein identity."
  },
  "case_id": "GO_molecular_function_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A8JUV4 (VTUL_DROME) is annotated with GO:0008316 (structural constituent of vitelline membrane) with evidence code ISM:FlyBase. The FUNCTION comment (ECO:0000269, PubMed:19540119) confirms it is a 'Major early eggshell protein secreted by follicle cells into the perivitelline space and incorporated into the vitelline membrane.' The protein is named 'Vitelline membrane-like protein.' Sequence match is exact (578 aa, SHA256 confirmed)."
  },
  "important_caveats": [
    "The GO annotation evidence code is ISM (Inferred by Sequence or Structural Model) from FlyBase, not a direct experimental structural determination. However, the FUNCTION comment is supported by direct assay (ECO:0000269, PubMed:19540119).",
    "The specific recognition that the SYSAPAAP repetitive motif is diagnostic of vitelline membrane proteins (vs. other Drosophila eggshell proteins) is domain-specific knowledge; the question is answerable here only because A is the sole structural option among the four choices.",
    "The protein was first publicly released in UniProt on 2025-02-05; the benchmark construction date is unknown but the sequence has been available in databases since 2007.",
    "The GO term GO:0008316 is defined with 'An example of this is found in Drosophila melanogaster,' making it a Drosophila-centric term; the reasoning relies on recognizing the organism context or using elimination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct functional categories (structural, binding, catalytic, reader-domain binding). The sequence's architecture unambiguously excludes B, C, and D, leaving A as the only defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A8JUV4 (VTUL_DROME) is annotated with GO:0008316 (structural constituent of vitelline membrane) with evidence code ISM:FlyBase. The FUNCTION comment (ECO:0000269, PubMed:19540119) confirms it is a 'Major early eggshell protein secreted by follicle cells into the perivitelline space and incorporated into the vitelline membrane.' The protein is named 'Vitelline membrane-like protein.' Sequence match is exact (578 aa, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H4", "H5", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an N-terminal signal peptide (MCGRRLLFLAAFGCLLANAFSLPATRN), indicating a secreted protein. The bulk of the sequence is dominated by highly repetitive Ser/Tyr/Ala/Pro motifs (SYSAPAAP repeats), characteristic of structural/assembly proteins rather than enzymes or specific ligand-binding proteins. The C-terminal region contains cysteines (…VSCSSVFTPAPCSQGYGY) suggestive of disulfide cross-linking. None of the other three options are compatible: (B) odorant-binding proteins are ~150 aa with a conserved 6-cysteine OB-fold, not a 578-aa repetitive secreted protein; (C) acid phosphatases require a DXDXP catalytic motif and a specific fold, entirely absent here; (D) methylated histone binding requires reader domains (chromodomain, Tudor, PHD, MBT), none present. Among the four choices, only A describes a structural constituent activity, which is the only category consistent with a secreted, repetitive, cross-linking protein.",
    "missing_item_specific_fact": "Positive identification of 'vitelline membrane' specifically (as opposed to other secreted structural proteins like chorion or cuticle proteins) relies on knowledge that this particular repetitive SYSAPAAP pattern is characteristic of Drosophila vitelline membrane proteins. However, since A is the sole structural option among the four choices, the elimination argument suffices to select it.",
    "reason": "The sequence clearly lacks catalytic residues (no acid phosphatase DXDXP motif), lacks OB-fold/cysteine-stabilized small-binding-protein architecture (odorant binding), and lacks any known chromatin-reader domain (methylated histone binding). The secreted, highly repetitive, cysteine-containing architecture is consistent only with a structural constituent role. Among the four provided options, A is the unique structural-constituent choice, making the answer reachable by elimination without needing to recall the specific protein identity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct functional categories (structural, binding, catalytic, reader-domain binding). The sequence's architecture unambiguously excludes B, C, and D, leaving A as the only defensible choice."
  },
  "important_caveats": [
    "The GO annotation evidence code is ISM (Inferred by Sequence or Structural Model) from FlyBase, not a direct experimental structural determination. However, the FUNCTION comment is supported by direct assay (ECO:0000269, PubMed:19540119).",
    "The specific recognition that the SYSAPAAP repetitive motif is diagnostic of vitelline membrane proteins (vs. other Drosophila eggshell proteins) is domain-specific knowledge; the question is answerable here only because A is the sole structural option among the four choices.",
    "The protein was first publicly released in UniProt on 2025-02-05; the benchmark construction date is unknown but the sequence has been available in databases since 2007.",
    "The GO term GO:0008316 is defined with 'An example of this is found in Drosophila melanogaster,' making it a Drosophila-centric term; the reasoning relies on recognizing the organism context or using elimination."
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

**Accession:** `A8JUV4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 119. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8JUV4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:10.083584+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0085362","source":"FlyBase"}],"value":"Vitelline membrane-like protein"}}}
```

Source SHA-256: `d80891aa93381e968359329b957b532f55ee57a8445bf45f7803a6e686222440`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8JUV4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:10.083584+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"19540119","source":"PubMed"}],"value":"Major early eggshell protein secreted by follicle cells into the perivitelline space and incorporated into the vitelline membrane (PubMed:19540119). Localized sulfation by pip may be involved in embryo dorsal-ventral axis determination (PubMed:19540119)"}]}
```

Source SHA-256: `d80891aa93381e968359329b957b532f55ee57a8445bf45f7803a6e686222440`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8JUV4.json)  
**Locator:** `/uniProtKBCrossReferences/30`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:10.083584+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000255","id":"16637280","source":"PubMed"}],"id":"GO:0008316","properties":[{"key":"GoTerm","value":"F:structural constituent of vitelline membrane"},{"key":"GoEvidenceType","value":"ISM:FlyBase"}]}
```

Source SHA-256: `d80891aa93381e968359329b957b532f55ee57a8445bf45f7803a6e686222440`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8JUV4.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:10.083584+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Stevens L.M.","Stein D."],"citationCrossReferences":[{"database":"PubMed","id":"19540119"},{"database":"DOI","id":"10.1016/j.cub.2009.05.050"}],"citationType":"journal article","firstPage":"1200","id":"19540119","journal":"Curr. Biol.","lastPage":"1205","publicationDate":"2009","title":"Sulfation of eggshell components by Pipe defines dorsal-ventral polarity in the Drosophila embryo.","volume":"19"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","TISSUE SPECIFICITY","SULFATION","DISRUPTION PHENOTYPE","IDENTIFICATION BY MASS SPECTROMETRY"]}
```

Source SHA-256: `d80891aa93381e968359329b957b532f55ee57a8445bf45f7803a6e686222440`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8JUV4?format=txt&versions=119)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-02T04:27:12.691080+00:00.  

```text
ID   VTUL_DROME              Reviewed;         578 AA.
AC   A8JUV4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   04-DEC-2007, sequence version 1.
DT   28-JAN-2026, entry version 119.
DE   RecName: Full=Vitelline membrane-like protein {ECO:0000312|FlyBase:FBgn0085362};
DE   Flags: Precursor;
GN   Name=Vml {ECO:0000312|FlyBase:FBgn0085362};
GN   Synonyms=CRM-80 {ECO:0000303|PubMed:20832396};
GN   ORFNames=CG34333 {ECO:0000312|FlyBase:FBgn0085362};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `0016e13b6a832f68a64502d2cf5fd5a6dce16e2957f74fbffdc26fe5e046cb04`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8JUV4?format=txt&versions=119)  
**Locator:** `lines 84-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-02T04:27:12.691080+00:00.  

```text
CC   -!- FUNCTION: Major early eggshell protein secreted by follicle cells into
CC       the perivitelline space and incorporated into the vitelline membrane
CC       (PubMed:19540119). Localized sulfation by pip may be involved in embryo
CC       dorsal-ventral axis determination (PubMed:19540119).
CC       {ECO:0000269|PubMed:19540119}.
```

Source SHA-256: `0016e13b6a832f68a64502d2cf5fd5a6dce16e2957f74fbffdc26fe5e046cb04`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8JUV4?format=txt&versions=119)  
**Locator:** `lines 146-146`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-02T04:27:12.691080+00:00.  

```text
DR   GO; GO:0008316; F:structural constituent of vitelline membrane; ISM:FlyBase.
```

Source SHA-256: `0016e13b6a832f68a64502d2cf5fd5a6dce16e2957f74fbffdc26fe5e046cb04`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 73. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
