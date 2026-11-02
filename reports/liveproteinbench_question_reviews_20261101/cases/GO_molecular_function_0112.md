# GO_molecular_function_0112

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — G protein-coupled receptor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASLRGSETMCNITTSCNVDSNIDQFFQPTLYIIVIVLGFPTNCMALWAAYMQVKQKNELGIYLMNLSIADLLYITTLPLWIDYFVHHDNWIHGQVSCKLFGFIFYTNIYVSIAFLCCISVDRYLAVAHPLKFAKVRRVKTALLVSAIVWLTEIVANSAPLFHDELFQDRFNHTFCFEKYPMEPWVAGMNLYRTFLGFLAPWGIMLAAYRGILRAVRGNVSTERQEKAKIKRLALSLILIVLLCFAPYHVLLLWRSVLFLINPCDCGGEENLFGAYHVTLALTSLNCVADPILYCFVNEGARHDVGRALATLLGLFQRGKSPETLMGASITVETPLAVKKPDFYSEVKTNAYKNDIEVLKDECLQMTILSVKK

[Multiple Choices]
A. S-adenosylmethionine-dependent methyltransferase activity
B. G protein-coupled receptor activity
C. manganese ion binding
D. histone H3K9 demethylase activity
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

> The exact sequence matches the zebrafish GPR4 entry. UniProt reports proton-sensing GPCR activity and a GO annotation for G protein-coupled receptor activity; the function is linked to experimental evidence (ECO:0000269).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has many hydrophobic segments consistent with a seven-transmembrane receptor. That topology supports a GPCR over the listed methyltransferase, demethylase, or manganese-binding alternatives, which would not be expected to have this receptor-like membrane architecture.


**Missing item-specific fact**

> Identifying this particular receptor as GPR4 and establishing its proton-sensing and G-protein-coupling activity require protein-specific annotation or experimental evidence; those details are not needed to distinguish the broad GPCR option from these distractors.


**Reason**

> The sequence provides a meaningful structural-family clue that distinguishes the broad molecular-function class among the choices, although it does not by itself establish the exact receptor subtype or ligand.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the strongly hydrophobic multi-pass receptor-like sequence and the specific alternatives, B is the clearly best-supported choice.


### Important caveats

- The sequence topology supports GPCR-family inference but is not, by itself, experimental confirmation of G-protein coupling.
- Reviewer-only database and experimental evidence supports the key but was not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many hydrophobic segments consistent with a seven-transmembrane receptor. That topology supports a GPCR over the listed methyltransferase, demethylase, or manganese-binding alternatives, which would not be expected to have this receptor-like membrane architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Identifying this particular receptor as GPR4 and establishing its proton-sensing and G-protein-coupling activity require protein-specific annotation or experimental evidence; those details are not needed to distinguish the broad GPCR option from these distractors.",
    "reason": "The sequence provides a meaningful structural-family clue that distinguishes the broad molecular-function class among the choices, although it does not by itself establish the exact receptor subtype or ligand."
  },
  "case_id": "GO_molecular_function_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the zebrafish GPR4 entry. UniProt reports proton-sensing GPCR activity and a GO annotation for G protein-coupled receptor activity; the function is linked to experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The sequence topology supports GPCR-family inference but is not, by itself, experimental confirmation of G-protein coupling.",
    "Reviewer-only database and experimental evidence supports the key but was not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the strongly hydrophobic multi-pass receptor-like sequence and the specific alternatives, B is the clearly best-supported choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the zebrafish GPR4 entry. UniProt reports proton-sensing GPCR activity and a GO annotation for G protein-coupled receptor activity; the function is linked to experimental evidence (ECO:0000269).",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has many hydrophobic segments consistent with a seven-transmembrane receptor. That topology supports a GPCR over the listed methyltransferase, demethylase, or manganese-binding alternatives, which would not be expected to have this receptor-like membrane architecture.",
    "missing_item_specific_fact": "Identifying this particular receptor as GPR4 and establishing its proton-sensing and G-protein-coupling activity require protein-specific annotation or experimental evidence; those details are not needed to distinguish the broad GPCR option from these distractors.",
    "reason": "The sequence provides a meaningful structural-family clue that distinguishes the broad molecular-function class among the choices, although it does not by itself establish the exact receptor subtype or ligand."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the strongly hydrophobic multi-pass receptor-like sequence and the specific alternatives, B is the clearly best-supported choice."
  },
  "important_caveats": [
    "The sequence topology supports GPCR-family inference but is not, by itself, experimental confirmation of G-protein coupling.",
    "Reviewer-only database and experimental evidence supports the key but was not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProtKB entry E7FEL0 (sequence SHA256 match confirmed, 373 AA) identifies this protein as G protein-coupled receptor 4 (zGPR4) from Danio rerio. GO annotation GO:0004930 (G protein-coupled receptor activity) is assigned with IDA:UniProtKB evidence, supported by a 2025 Nature Communications cryo-EM structure of the activated GPR4-Gs signaling complex (PDB 8ZFZ, 9J31). The protein is described as a proton-sensing GPCR coupled to Gs.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays approximately seven hydrophobic transmembrane helix segments (e.g., 'IIVIVLGFPTNCMALWAAYMQVK', 'IYLMNLSIADLLYITTLPLWIDYFV', 'CKLFGFIFYTNIYVSIAFLCCISV', 'VRRVKTALLVSAIVWLTEIVANSAP', 'MNLYRTFLGFLAPWGIMLAAYRGIL', 'KRLALSLILIVLLCFAPYHVLLLW', 'VLFLINPCDCGGEENLFGAYHVTLALTSLNCVADPILYCFVNEGARHDVGRALATLLGLF') alternating with hydrophilic loops, consistent with the canonical 7TM GPCR topology. Critically, the DRY motif ('ISVDRYLAVAHPLKF') is present at the TM3/ICL2 boundary, a well-known GPCR hallmark. A variant of the NPxxY motif ('TNAY') appears near the TM7 end. The N-terminal region is relatively hydrophilic (extracellular) and the C-terminal tail is hydrophilic (intracellular), consistent with GPCR topology. None of the distractor functions (SAM-dependent methyltransferase, manganese binding, histone demethylase) are supported: there is no Rossmann-fold or VLDLGCG motif, no characteristic His/Asp/Glu metal-binding cluster, and no JmjC-domain catalytic residues.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 7TM architecture, DRY motif, and NPxxY-like motif are general, textbook-level GPCR signatures identifiable from the amino acid sequence. A model with standard molecular biology knowledge can reason from these features to GPCR activity and exclude the other functional classes by absence of their characteristic motifs. This does not require memorizing the specific UniProt entry for zebrafish GPR4.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct functional classes (catalytic methyltransferase, metal binding, histone demethylase, receptor signaling). The 7TM topology with DRY motif is specific to GPCRs and incompatible with the other three options. No other option is defensible given the sequence features.


### Important caveats

- The GO annotation evidence code is IDA (Inferred from Direct Assay), backed by cryo-EM structural and functional data (PubMed:39799123), making this a high-confidence experimental annotation rather than a computational prediction.
- The protein is a zebrafish ortholog (Danio rerio GPR4); the 2025 paper providing the GO annotation post-dates the original sequence deposition (2011), so the annotation was added later. The sequence itself, however, has been stable since version 1.
- The DRY motif in this sequence reads D-R-Y (canonical), and the NPxxY-like motif reads T-N-A-Y, a minor variant; both are within the range of known GPCR sequence variation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays approximately seven hydrophobic transmembrane helix segments (e.g., 'IIVIVLGFPTNCMALWAAYMQVK', 'IYLMNLSIADLLYITTLPLWIDYFV', 'CKLFGFIFYTNIYVSIAFLCCISV', 'VRRVKTALLVSAIVWLTEIVANSAP', 'MNLYRTFLGFLAPWGIMLAAYRGIL', 'KRLALSLILIVLLCFAPYHVLLLW', 'VLFLINPCDCGGEENLFGAYHVTLALTSLNCVADPILYCFVNEGARHDVGRALATLLGLF') alternating with hydrophilic loops, consistent with the canonical 7TM GPCR topology. Critically, the DRY motif ('ISVDRYLAVAHPLKF') is present at the TM3/ICL2 boundary, a well-known GPCR hallmark. A variant of the NPxxY motif ('TNAY') appears near the TM7 end. The N-terminal region is relatively hydrophilic (extracellular) and the C-terminal tail is hydrophilic (intracellular), consistent with GPCR topology. None of the distractor functions (SAM-dependent methyltransferase, manganese binding, histone demethylase) are supported: there is no Rossmann-fold or VLDLGCG motif, no characteristic His/Asp/Glu metal-binding cluster, and no JmjC-domain catalytic residues.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 7TM architecture, DRY motif, and NPxxY-like motif are general, textbook-level GPCR signatures identifiable from the amino acid sequence. A model with standard molecular biology knowledge can reason from these features to GPCR activity and exclude the other functional classes by absence of their characteristic motifs. This does not require memorizing the specific UniProt entry for zebrafish GPR4."
  },
  "case_id": "GO_molecular_function_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProtKB entry E7FEL0 (sequence SHA256 match confirmed, 373 AA) identifies this protein as G protein-coupled receptor 4 (zGPR4) from Danio rerio. GO annotation GO:0004930 (G protein-coupled receptor activity) is assigned with IDA:UniProtKB evidence, supported by a 2025 Nature Communications cryo-EM structure of the activated GPR4-Gs signaling complex (PDB 8ZFZ, 9J31). The protein is described as a proton-sensing GPCR coupled to Gs."
  },
  "important_caveats": [
    "The GO annotation evidence code is IDA (Inferred from Direct Assay), backed by cryo-EM structural and functional data (PubMed:39799123), making this a high-confidence experimental annotation rather than a computational prediction.",
    "The protein is a zebrafish ortholog (Danio rerio GPR4); the 2025 paper providing the GO annotation post-dates the original sequence deposition (2011), so the annotation was added later. The sequence itself, however, has been stable since version 1.",
    "The DRY motif in this sequence reads D-R-Y (canonical), and the NPxxY-like motif reads T-N-A-Y, a minor variant; both are within the range of known GPCR sequence variation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct functional classes (catalytic methyltransferase, metal binding, histone demethylase, receptor signaling). The 7TM topology with DRY motif is specific to GPCRs and incompatible with the other three options. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProtKB entry E7FEL0 (sequence SHA256 match confirmed, 373 AA) identifies this protein as G protein-coupled receptor 4 (zGPR4) from Danio rerio. GO annotation GO:0004930 (G protein-coupled receptor activity) is assigned with IDA:UniProtKB evidence, supported by a 2025 Nature Communications cryo-EM structure of the activated GPR4-Gs signaling complex (PDB 8ZFZ, 9J31). The protein is described as a proton-sensing GPCR coupled to Gs.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays approximately seven hydrophobic transmembrane helix segments (e.g., 'IIVIVLGFPTNCMALWAAYMQVK', 'IYLMNLSIADLLYITTLPLWIDYFV', 'CKLFGFIFYTNIYVSIAFLCCISV', 'VRRVKTALLVSAIVWLTEIVANSAP', 'MNLYRTFLGFLAPWGIMLAAYRGIL', 'KRLALSLILIVLLCFAPYHVLLLW', 'VLFLINPCDCGGEENLFGAYHVTLALTSLNCVADPILYCFVNEGARHDVGRALATLLGLF') alternating with hydrophilic loops, consistent with the canonical 7TM GPCR topology. Critically, the DRY motif ('ISVDRYLAVAHPLKF') is present at the TM3/ICL2 boundary, a well-known GPCR hallmark. A variant of the NPxxY motif ('TNAY') appears near the TM7 end. The N-terminal region is relatively hydrophilic (extracellular) and the C-terminal tail is hydrophilic (intracellular), consistent with GPCR topology. None of the distractor functions (SAM-dependent methyltransferase, manganese binding, histone demethylase) are supported: there is no Rossmann-fold or VLDLGCG motif, no characteristic His/Asp/Glu metal-binding cluster, and no JmjC-domain catalytic residues.",
    "missing_item_specific_fact": "",
    "reason": "The 7TM architecture, DRY motif, and NPxxY-like motif are general, textbook-level GPCR signatures identifiable from the amino acid sequence. A model with standard molecular biology knowledge can reason from these features to GPCR activity and exclude the other functional classes by absence of their characteristic motifs. This does not require memorizing the specific UniProt entry for zebrafish GPR4."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct functional classes (catalytic methyltransferase, metal binding, histone demethylase, receptor signaling). The 7TM topology with DRY motif is specific to GPCRs and incompatible with the other three options. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GO annotation evidence code is IDA (Inferred from Direct Assay), backed by cryo-EM structural and functional data (PubMed:39799123), making this a high-confidence experimental annotation rather than a computational prediction.",
    "The protein is a zebrafish ortholog (Danio rerio GPR4); the 2025 paper providing the GO annotation post-dates the original sequence deposition (2011), so the annotation was added later. The sequence itself, however, has been stable since version 1.",
    "The DRY motif in this sequence reads D-R-Y (canonical), and the NPxxY-like motif reads T-N-A-Y, a minor variant; both are within the range of known GPCR sequence variation."
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

**Accession:** `E7FEL0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 99. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
"E7FEL0"
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39799123","source":"PubMed"}],"value":"G protein-coupled receptor 4"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39799123","source":"PubMed"}],"value":"zGPR4"}]}}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39799123","source":"PubMed"}],"value":"Proton-sensing G protein-coupled receptor activated by extracellular pH, which is required to monitor pH changes and generate adaptive reactions (PubMed:39799123). Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase (PubMed:39799123). GPR4 is mainly coupled to G(s) G proteins and mediates activation of adenylate cyclase activity (PubMed:39799123)"}]}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/uniProtKBCrossReferences/34`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39799123","source":"PubMed"}],"id":"GO:0004930","properties":[{"key":"GoTerm","value":"F:G protein-coupled receptor activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"citation":{"authors":["Ma Y.","Wang Y.","Tang M.","Weng Y.","Chen Y.","Xu Y.","An S.","Wu Y.","Zhao S.","Xu H.","Li D.","Liu M.","Lu W.","Ru H.","Song G."],"citationCrossReferences":[{"database":"PubMed","id":"39799123"},{"database":"DOI","id":"10.1038/s41467-025-55901-2"}],"citationType":"journal article","firstPage":"605","id":"39799123","journal":"Nat. Commun.","lastPage":"605","publicationDate":"2025","title":"Cryo-EM structure of an activated GPR4-Gs signaling complex.","volume":"16"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8ZFZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9J31","source":"PDB"}],"referenceNumber":2,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (3.05 ANGSTROMS) OF 2-360 IN COMPLEX WITH GNAS","FUNCTION","MUTAGENESIS OF GLN-53; ASN-58; GLU-59; ASP-71; HIS-87; ASP-89; TYR-106; TYR-110; ARG-123; ARG-137; 164-ASP-GLU-165; HIS-173; GLU-178; ASN-219; GLU-226; TYR-248; TYR-276; HIS-277; ASP-290 AND GLU-299"]}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
ID   GPR4_DANRE              Reviewed;         373 AA.
AC   E7FEL0; A0A8M2B4J4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   08-MAR-2011, sequence version 1.
DT   28-JAN-2026, entry version 99.
DE   RecName: Full=G-protein coupled receptor 4 {ECO:0000303|PubMed:39799123};
DE            Short=zGPR4 {ECO:0000303|PubMed:39799123};
GN   Name=gpr4 {ECO:0000303|PubMed:39799123,
GN   ECO:0000312|ZFIN:ZDB-GENE-101202-1};
OS   Danio rerio (Zebrafish) (Brachydanio rerio).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;
OC   Actinopterygii; Neopterygii; Teleostei; Ostariophysi; Cypriniformes;
OC   Danionidae; Danioninae; Danio.
OX   NCBI_TaxID=7955;
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 52-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
RN   [2] {ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31}
RP   STRUCTURE BY ELECTRON MICROSCOPY (3.05 ANGSTROMS) OF 2-360 IN COMPLEX WITH
RP   GNAS, FUNCTION, AND MUTAGENESIS OF GLN-53; ASN-58; GLU-59; ASP-71; HIS-87;
RP   ASP-89; TYR-106; TYR-110; ARG-123; ARG-137; 164-ASP-GLU-165; HIS-173;
RP   GLU-178; ASN-219; GLU-226; TYR-248; TYR-276; HIS-277; ASP-290 AND GLU-299.
RX   PubMed=39799123; DOI=10.1038/s41467-025-55901-2;
RA   Ma Y., Wang Y., Tang M., Weng Y., Chen Y., Xu Y., An S., Wu Y., Zhao S.,
RA   Xu H., Li D., Liu M., Lu W., Ru H., Song G.;
RT   "Cryo-EM structure of an activated GPR4-Gs signaling complex.";
RL   Nat. Commun. 16:605-605(2025).
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 62-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
CC   -!- FUNCTION: Proton-sensing G-protein coupled receptor activated by
CC       extracellular pH, which is required to monitor pH changes and generate
CC       adaptive reactions (PubMed:39799123). Ligand binding causes a
CC       conformation change that triggers signaling via guanine nucleotide-
CC       binding proteins (G proteins) and modulates the activity of downstream
CC       effectors, such as adenylate cyclase (PubMed:39799123). GPR4 is mainly
CC       coupled to G(s) G proteins and mediates activation of adenylate cyclase
CC       activity (PubMed:39799123). {ECO:0000269|PubMed:39799123}.
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 118-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
DR   GO; GO:0004930; F:G protein-coupled receptor activity; IDA:UniProtKB.
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 52078-52112`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004930
name: G protein-coupled receptor activity
namespace: molecular_function
alt_id: GO:0001622
alt_id: GO:0001623
alt_id: GO:0001624
alt_id: GO:0001625
alt_id: GO:0016526
def: "Combining with an extracellular signal and transmitting the signal across the membrane by activating an associated G-protein; promotes the exchange of GDP for GTP on the alpha subunit of a heterotrimeric G-protein complex." [GOC:bf, Wikipedia:GPCR]
subset: goslim_chembl
synonym: "EBV-induced receptor" NARROW []
synonym: "Epstein-Barr Virus-induced receptor activity" NARROW []
synonym: "G protein coupled receptor activity" EXACT []
synonym: "G protein linked receptor activity" EXACT []
synonym: "G-protein coupled receptor activity" EXACT []
synonym: "G-protein coupled receptor activity, unknown ligand" NARROW []
synonym: "G-protein linked receptor activity" EXACT []
synonym: "GPCR activity" EXACT []
synonym: "ligand-dependent GPCR activity" EXACT []
synonym: "Mas proto-oncogene receptor activity" NARROW []
synonym: "orphan G protein coupled receptor activity" NARROW []
synonym: "orphan G-protein coupled receptor activity" NARROW []
synonym: "orphan GPCR activity" NARROW []
synonym: "RDC1 receptor activity" NARROW []
synonym: "receptor activity, G-protein coupled" EXACT [GOC:bf]
synonym: "SREB receptor" NARROW []
synonym: "super conserved receptor expressed in brain receptor activity" NARROW []
xref: Reactome:R-HSA-114552 "Thrombin-activated PARs activate G12/13"
xref: Reactome:R-HSA-114558 "Thrombin-activated PARs activate Gq"
xref: Reactome:R-HSA-167408 "The high affinity receptor complex binds to G-protein"
xref: Reactome:R-HSA-381706 "GLP1R:GLP1 activates G(s)"
xref: Wikipedia:GPCR
is_a: GO:0004888 ! transmembrane signaling receptor activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
