# GO_molecular_function_0173

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — olfactory receptor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGSNITSTSIIFLLTGVPGLEAFHTWISIPFCFLSVTALLGNSLILFATITQPSLHEPMYYFLSMLSATDLGLSISTLVTMLSIFWFNVREISFNACLSHMFFIKFFTVMESSVLLAMAFDRFVAVSNPLRYAMILTDSRIAQIGVASVIRGLLMLTPMVALLIRLSYCHSQVLHHSYCYHPDVMKLSCTDTRINSAVGLTAMFSTVGVDLLLILLSYVLIIRTVLSVASPEERKETFSTCVSHIVAFAIYYIPLISLSIVHRFGKQAPAYVHTMIANTYLLISPLMNPVIYSVKTKQIRRAVIKILHSKET

[Multiple Choices]
A. enoyl-[acyl-carrier-protein] reductase (NADPH) activity
B. olfactory receptor activity
C. beta-amyrin synthase activity
D. histone H3K14 acetyltransferase activity
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

> The exact sequence matches a UniProt record named olfactory receptor OR51C1, whose function annotation says odorant receptor. The record also assigns olfactory receptor activity (GO:0004984) by IBA, a phylogenetic inference annotation, not direct experimental evidence in the supplied materials.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly hydrophobic and consistent with a multi-pass, seven-transmembrane GPCR; it also has motifs compatible with an olfactory-receptor GPCR. Among the choices, B is the receptor activity, whereas the other options describe distinct enzyme activities.


**Missing item-specific fact**

> Identifying the specific odorant-receptor family with certainty would require protein-specific annotation or homology information not supplied. However, the sequence architecture and the available choices provide a meaningful basis to select B as the best match.


**Reason**

> The choice can be distinguished from these alternatives by the sequence's membrane-receptor architecture and compatible GPCR motifs; this does not depend solely on recognizing the exact sequence or recalling its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence's multi-pass receptor-like architecture strongly favors B over the enzyme activities in A, C, and D.


### Important caveats

- Reviewer-only database identity and annotations support the key but were absent from the evaluated input.
- The supplied database evidence is annotation-based, including a phylogenetic inference for the GO term; it does not establish direct experimental characterization of this sequence's odorant response.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multi-pass, seven-transmembrane GPCR; it also has motifs compatible with an olfactory-receptor GPCR. Among the choices, B is the receptor activity, whereas the other options describe distinct enzyme activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Identifying the specific odorant-receptor family with certainty would require protein-specific annotation or homology information not supplied. However, the sequence architecture and the available choices provide a meaningful basis to select B as the best match.",
    "reason": "The choice can be distinguished from these alternatives by the sequence's membrane-receptor architecture and compatible GPCR motifs; this does not depend solely on recognizing the exact sequence or recalling its database entry."
  },
  "case_id": "GO_molecular_function_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record named olfactory receptor OR51C1, whose function annotation says odorant receptor. The record also assigns olfactory receptor activity (GO:0004984) by IBA, a phylogenetic inference annotation, not direct experimental evidence in the supplied materials."
  },
  "important_caveats": [
    "Reviewer-only database identity and annotations support the key but were absent from the evaluated input.",
    "The supplied database evidence is annotation-based, including a phylogenetic inference for the GO term; it does not establish direct experimental characterization of this sequence's odorant response."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence's multi-pass receptor-like architecture strongly favors B over the enzyme activities in A, C, and D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record named olfactory receptor OR51C1, whose function annotation says odorant receptor. The record also assigns olfactory receptor activity (GO:0004984) by IBA, a phylogenetic inference annotation, not direct experimental evidence in the supplied materials.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multi-pass, seven-transmembrane GPCR; it also has motifs compatible with an olfactory-receptor GPCR. Among the choices, B is the receptor activity, whereas the other options describe distinct enzyme activities.",
    "missing_item_specific_fact": "Identifying the specific odorant-receptor family with certainty would require protein-specific annotation or homology information not supplied. However, the sequence architecture and the available choices provide a meaningful basis to select B as the best match.",
    "reason": "The choice can be distinguished from these alternatives by the sequence's membrane-receptor architecture and compatible GPCR motifs; this does not depend solely on recognizing the exact sequence or recalling its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence's multi-pass receptor-like architecture strongly favors B over the enzyme activities in A, C, and D."
  },
  "important_caveats": [
    "Reviewer-only database identity and annotations support the key but were absent from the evaluated input.",
    "The supplied database evidence is annotation-based, including a phylogenetic inference for the GO term; it does not establish direct experimental characterization of this sequence's odorant response."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (312 aa, sha256 matched) corresponds to UniProtKB A0A3B3IT45 (O51C1_HUMAN), named 'Olfactory receptor OR51C1' with function comment 'Odorant receptor' (ECO:0000305). GO:0004984 'olfactory receptor activity' is annotated with IBA:GO_Central evidence (C7, H4). The sequence exhibits canonical 7TM GPCR architecture (multiple ~20-25 residue hydrophobic TM segments, DRF variant of DRY motif in TM3, NPxxY-like motif in TM7) consistent with an olfactory receptor. The annotation is a computational inference from family membership but is well-supported by the protein's identity and structural features.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 312-aa sequence displays clear 7-transmembrane GPCR topology: approximately seven hydrophobic segments of 18-25 residues, a DRF (DRY-variant) motif in the TM3 region, and an NPxxY-like motif in the TM7 region. Among the four options, only B (olfactory receptor activity, GO:0004984) describes a GPCR/membrane receptor function. The other three are soluble enzymes: A (enoyl-ACP reductase) requires a Rossmann-fold NADPH-binding domain absent here; C (beta-amyrin synthase) is a ~750-aa plant cyclase far exceeding this protein's length; D (histone H3K14 acetyltransferase) is a nuclear GNAT/MYST-domain enzyme with no membrane-spanning architecture. Thus, recognizing 7TM GPCR architecture and eliminating non-receptor enzyme options provides a concrete reasoning path to B.


**Missing item-specific fact**

> None strictly required. Distinguishing this as an olfactory receptor specifically (vs. another GPCR subtype) would require family-level knowledge, but among the four provided options only one is a GPCR activity, so subtype-level identification is unnecessary for selection.


**Reason**

> A model applying general knowledge of GPCR structural signatures (7TM helices, conserved DRY/NPxxY motifs, ~300 aa length typical of olfactory receptors) and recognizing the absence of catalytic domains (Rossmann fold, cyclase motifs, acetyltransferase domain) can eliminate A, C, and D and select B without memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different protein classes (enzyme reductase, GPCR, plant cyclase, nuclear acetyltransferase). The 7TM GPCR architecture of the sequence uniquely matches option B. No other option is defensible given the membrane-protein topology and absence of catalytic motifs.


### Important caveats

- The GO:0004984 annotation uses IBA:GO_Central (computational inference from family), not direct experimental evidence for this specific receptor's odorant binding.
- The protein name derives from HGNC annotation (ECO:0000312), which is a naming authority assignment rather than functional characterization.
- Olfactory receptors are a large family (~400 in humans); the sequence alone confirms GPCR/olfactory-receptor class but not the specific ligand specificity of OR51C1.
- The reviewer-only accession identification was absent from the model input; the reasoning path relies solely on sequence-derived structural features.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 312-aa sequence displays clear 7-transmembrane GPCR topology: approximately seven hydrophobic segments of 18-25 residues, a DRF (DRY-variant) motif in the TM3 region, and an NPxxY-like motif in the TM7 region. Among the four options, only B (olfactory receptor activity, GO:0004984) describes a GPCR/membrane receptor function. The other three are soluble enzymes: A (enoyl-ACP reductase) requires a Rossmann-fold NADPH-binding domain absent here; C (beta-amyrin synthase) is a ~750-aa plant cyclase far exceeding this protein's length; D (histone H3K14 acetyltransferase) is a nuclear GNAT/MYST-domain enzyme with no membrane-spanning architecture. Thus, recognizing 7TM GPCR architecture and eliminating non-receptor enzyme options provides a concrete reasoning path to B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Distinguishing this as an olfactory receptor specifically (vs. another GPCR subtype) would require family-level knowledge, but among the four provided options only one is a GPCR activity, so subtype-level identification is unnecessary for selection.",
    "reason": "A model applying general knowledge of GPCR structural signatures (7TM helices, conserved DRY/NPxxY motifs, ~300 aa length typical of olfactory receptors) and recognizing the absence of catalytic domains (Rossmann fold, cyclase motifs, acetyltransferase domain) can eliminate A, C, and D and select B without memorizing this specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence (312 aa, sha256 matched) corresponds to UniProtKB A0A3B3IT45 (O51C1_HUMAN), named 'Olfactory receptor OR51C1' with function comment 'Odorant receptor' (ECO:0000305). GO:0004984 'olfactory receptor activity' is annotated with IBA:GO_Central evidence (C7, H4). The sequence exhibits canonical 7TM GPCR architecture (multiple ~20-25 residue hydrophobic TM segments, DRF variant of DRY motif in TM3, NPxxY-like motif in TM7) consistent with an olfactory receptor. The annotation is a computational inference from family membership but is well-supported by the protein's identity and structural features."
  },
  "important_caveats": [
    "The GO:0004984 annotation uses IBA:GO_Central (computational inference from family), not direct experimental evidence for this specific receptor's odorant binding.",
    "The protein name derives from HGNC annotation (ECO:0000312), which is a naming authority assignment rather than functional characterization.",
    "Olfactory receptors are a large family (~400 in humans); the sequence alone confirms GPCR/olfactory-receptor class but not the specific ligand specificity of OR51C1.",
    "The reviewer-only accession identification was absent from the model input; the reasoning path relies solely on sequence-derived structural features."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different protein classes (enzyme reductase, GPCR, plant cyclase, nuclear acetyltransferase). The 7TM GPCR architecture of the sequence uniquely matches option B. No other option is defensible given the membrane-protein topology and absence of catalytic motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (312 aa, sha256 matched) corresponds to UniProtKB A0A3B3IT45 (O51C1_HUMAN), named 'Olfactory receptor OR51C1' with function comment 'Odorant receptor' (ECO:0000305). GO:0004984 'olfactory receptor activity' is annotated with IBA:GO_Central evidence (C7, H4). The sequence exhibits canonical 7TM GPCR architecture (multiple ~20-25 residue hydrophobic TM segments, DRF variant of DRY motif in TM3, NPxxY-like motif in TM7) consistent with an olfactory receptor. The annotation is a computational inference from family membership but is well-supported by the protein's identity and structural features.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 312-aa sequence displays clear 7-transmembrane GPCR topology: approximately seven hydrophobic segments of 18-25 residues, a DRF (DRY-variant) motif in the TM3 region, and an NPxxY-like motif in the TM7 region. Among the four options, only B (olfactory receptor activity, GO:0004984) describes a GPCR/membrane receptor function. The other three are soluble enzymes: A (enoyl-ACP reductase) requires a Rossmann-fold NADPH-binding domain absent here; C (beta-amyrin synthase) is a ~750-aa plant cyclase far exceeding this protein's length; D (histone H3K14 acetyltransferase) is a nuclear GNAT/MYST-domain enzyme with no membrane-spanning architecture. Thus, recognizing 7TM GPCR architecture and eliminating non-receptor enzyme options provides a concrete reasoning path to B.",
    "missing_item_specific_fact": "None strictly required. Distinguishing this as an olfactory receptor specifically (vs. another GPCR subtype) would require family-level knowledge, but among the four provided options only one is a GPCR activity, so subtype-level identification is unnecessary for selection.",
    "reason": "A model applying general knowledge of GPCR structural signatures (7TM helices, conserved DRY/NPxxY motifs, ~300 aa length typical of olfactory receptors) and recognizing the absence of catalytic domains (Rossmann fold, cyclase motifs, acetyltransferase domain) can eliminate A, C, and D and select B without memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different protein classes (enzyme reductase, GPCR, plant cyclase, nuclear acetyltransferase). The 7TM GPCR architecture of the sequence uniquely matches option B. No other option is defensible given the membrane-protein topology and absence of catalytic motifs."
  },
  "important_caveats": [
    "The GO:0004984 annotation uses IBA:GO_Central (computational inference from family), not direct experimental evidence for this specific receptor's odorant binding.",
    "The protein name derives from HGNC annotation (ECO:0000312), which is a naming authority assignment rather than functional characterization.",
    "Olfactory receptors are a large family (~400 in humans); the sequence alone confirms GPCR/olfactory-receptor class but not the specific ligand specificity of OR51C1.",
    "The reviewer-only accession identification was absent from the model input; the reasoning path relies solely on sequence-derived structural features."
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

**Accession:** `A0A3B3IT45` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 33. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
"A0A3B3IT45"
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"HGNC:15191","source":"HGNC"}],"value":"Olfactory receptor OR51C1"}}}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Odorant receptor"}]}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/uniProtKBCrossReferences/28`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"database":"GO","id":"GO:0004984","properties":[{"key":"GoTerm","value":"F:olfactory receptor activity"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
ID   O51C1_HUMAN             Reviewed;         312 AA.
AC   A0A3B3IT45; Q8NH68;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-DEC-2018, sequence version 1.
DT   28-JAN-2026, entry version 33.
DE   RecName: Full=Olfactory receptor OR51C1 {ECO:0000312|HGNC:HGNC:15191};
GN   Name=OR51C1 {ECO:0000312|HGNC:HGNC:15191};
GN   Synonyms=OR51C1P {ECO:0000312|HGNC:HGNC:15191}, OR51C3P, OST734;
OS   Homo sapiens (Human).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Primates; Haplorrhini; Catarrhini; Hominidae;
OC   Homo.
OX   NCBI_TaxID=9606;
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 43-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
CC   -!- FUNCTION: Odorant receptor. {ECO:0000305}.
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 79-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
DR   GO; GO:0004984; F:olfactory receptor activity; IBA:GO_Central.
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 52529-52536`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004984
name: olfactory receptor activity
namespace: molecular_function
def: "Combining with an odorant and transmitting the signal from one side of the membrane to the other to initiate a change in cell activity in response to detection of smell." [GOC:bf, GOC:dph, GOC:sart, PMID:19135896, PMID:21041441]
synonym: "odorant receptor activity" EXACT [PMID:19135896, PMID:21041441]
is_a: GO:0004888 ! transmembrane signaling receptor activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 173. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
