# GO_cellular_component_0098

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGSNITSTSIIFLLTGVPGLEAFHTWISIPFCFLSVTALLGNSLILFATITQPSLHEPMYYFLSMLSATDLGLSISTLVTMLSIFWFNVREISFNACLSHMFFIKFFTVMESSVLLAMAFDRFVAVSNPLRYAMILTDSRIAQIGVASVIRGLLMLTPMVALLIRLSYCHSQVLHHSYCYHPDVMKLSCTDTRINSAVGLTAMFSTVGVDLLLILLSYVLIIRTVLSVASPEERKETFSTCVSHIVAFAIYYIPLISLSIVHRFGKQAPAYVHTMIANTYLLISPLMNPVIYSVKTKQIRRAVIKILHSKET

[Multiple Choices]
A. plasma membrane
B. Dbf4-dependent protein kinase complex
C. chromatin
D. synapse
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence match has a UniProt GO annotation to plasma membrane (IBA, a phylogenetic inference), and the matched record describes a multipass membrane protein. This supports A, though the supplied excerpts do not establish the localization experimentally.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments support a multipass membrane protein and make chromatin or a soluble kinase complex implausible. They do not, by themselves, establish plasma membrane rather than a specialized membrane location such as a synapse.


**Missing item-specific fact**

> Distinguishing A from D requires protein-specific localization or functional identity; the sequence-level membrane topology alone does not establish whether this protein is synapse-associated.


**Reason**

> General sequence reasoning strongly narrows the choices to a membrane-associated option but does not resolve the distinction between plasma membrane and synapse. The supporting plasma-membrane annotation is reviewer-only and was not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports membrane association, but no supplied evidence specifically supports synaptic localization; the matched database annotation supports plasma membrane.


### Important caveats

- The GO plasma-membrane annotation is IBA, a computational phylogenetic inference, not direct experimental evidence in the excerpts.
- The UniProt subcellular-location statement is the broader term “Membrane”; it does not independently specify plasma membrane.
- The current and historical database records match the sequence, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments support a multipass membrane protein and make chromatin or a soluble kinase complex implausible. They do not, by themselves, establish plasma membrane rather than a specialized membrane location such as a synapse.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Distinguishing A from D requires protein-specific localization or functional identity; the sequence-level membrane topology alone does not establish whether this protein is synapse-associated.",
    "reason": "General sequence reasoning strongly narrows the choices to a membrane-associated option but does not resolve the distinction between plasma membrane and synapse. The supporting plasma-membrane annotation is reviewer-only and was not supplied in the question."
  },
  "case_id": "GO_cellular_component_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match has a UniProt GO annotation to plasma membrane (IBA, a phylogenetic inference), and the matched record describes a multipass membrane protein. This supports A, though the supplied excerpts do not establish the localization experimentally."
  },
  "important_caveats": [
    "The GO plasma-membrane annotation is IBA, a computational phylogenetic inference, not direct experimental evidence in the excerpts.",
    "The UniProt subcellular-location statement is the broader term “Membrane”; it does not independently specify plasma membrane.",
    "The current and historical database records match the sequence, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports membrane association, but no supplied evidence specifically supports synaptic localization; the matched database annotation supports plasma membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match has a UniProt GO annotation to plasma membrane (IBA, a phylogenetic inference), and the matched record describes a multipass membrane protein. This supports A, though the supplied excerpts do not establish the localization experimentally.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments support a multipass membrane protein and make chromatin or a soluble kinase complex implausible. They do not, by themselves, establish plasma membrane rather than a specialized membrane location such as a synapse.",
    "missing_item_specific_fact": "Distinguishing A from D requires protein-specific localization or functional identity; the sequence-level membrane topology alone does not establish whether this protein is synapse-associated.",
    "reason": "General sequence reasoning strongly narrows the choices to a membrane-associated option but does not resolve the distinction between plasma membrane and synapse. The supporting plasma-membrane annotation is reviewer-only and was not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports membrane association, but no supplied evidence specifically supports synaptic localization; the matched database annotation supports plasma membrane."
  },
  "important_caveats": [
    "The GO plasma-membrane annotation is IBA, a computational phylogenetic inference, not direct experimental evidence in the excerpts.",
    "The UniProt subcellular-location statement is the broader term “Membrane”; it does not independently specify plasma membrane.",
    "The current and historical database records match the sequence, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A3B3IT45 (Olfactory receptor OR51C1, Homo sapiens) annotates the protein as a 'Multi-pass membrane protein' located at 'Membrane' (ECO:0000305, ECO:0000255) and carries GO:0005886 (plasma membrane) via IBA:GO_Central. The sequence is 312 aa and matches the benchmark exactly. While the GO annotation uses computational inference (IBA), the protein is a canonical 7-transmembrane GPCR (olfactory receptor), a class universally localized to the plasma membrane. The expected answer 'plasma membrane' is consistent with both the database annotation and well-established biology of olfactory receptors.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 312-aa sequence exhibits the hallmark architecture of a 7-transmembrane G-protein-coupled receptor: multiple long hydrophobic stretches (~20-25 residues) separated by shorter hydrophilic loops, a DRY-like motif (DRFVAVSNPLRY near TM3), and an NPxxY-like motif (NPVIYSVKTKQ) near TM7. A biologist can reason: (1) multiple transmembrane helices → integral membrane protein; (2) 7-TM topology with GPCR signature motifs → GPCR family; (3) GPCRs are canonically plasma membrane receptors, not components of nuclear complexes (Dbf4-dependent kinase, chromatin) or synaptic junctions. The distractors (Dbf4 kinase complex, chromatin) are nuclear structures incompatible with a multi-pass membrane protein, and 'synapse' is a specialized junction not indicated by the sequence.


**Missing item-specific fact**

> None essential. Recognizing the specific olfactory receptor identity is not required; the 7-TM GPCR architecture and its plasma-membrane localization are general biological knowledge accessible from the sequence.


**Reason**

> The sequence itself provides sufficient structural cues (7 hydrophobic TM segments, GPCR conserved motifs) to infer multi-pass membrane topology and, combined with general knowledge that GPCRs reside at the plasma membrane, to select option A over nuclear or synaptic alternatives without needing to look up the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are biologically distinct compartments (plasma membrane, nuclear kinase complex, chromatin, synapse). A 7-TM GPCR is unambiguously a plasma membrane protein; none of the other options are compatible with its topology or function.


### Important caveats

- The GO:0005886 annotation uses evidence code IBA:GO_Central (computational inference by orthology), not direct experimental localization. The 'Membrane' and 'Multi-pass membrane protein' subcellular location annotations use ECO:0000305 (curator inference) and ECO:0000255 (sequence/structure similarity), respectively.
- The UniProt entry was first public in 2025-02-05; the benchmark author's exact source snapshot is unknown, though the sequence matches across versions.
- Olfactory receptors in humans are expressed on the cilia of olfactory sensory neurons; the 'plasma membrane' annotation refers to the neuronal plasma membrane (including ciliary membrane), not a generic cell surface.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 312-aa sequence exhibits the hallmark architecture of a 7-transmembrane G-protein-coupled receptor: multiple long hydrophobic stretches (~20-25 residues) separated by shorter hydrophilic loops, a DRY-like motif (DRFVAVSNPLRY near TM3), and an NPxxY-like motif (NPVIYSVKTKQ) near TM7. A biologist can reason: (1) multiple transmembrane helices → integral membrane protein; (2) 7-TM topology with GPCR signature motifs → GPCR family; (3) GPCRs are canonically plasma membrane receptors, not components of nuclear complexes (Dbf4-dependent kinase, chromatin) or synaptic junctions. The distractors (Dbf4 kinase complex, chromatin) are nuclear structures incompatible with a multi-pass membrane protein, and 'synapse' is a specialized junction not indicated by the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None essential. Recognizing the specific olfactory receptor identity is not required; the 7-TM GPCR architecture and its plasma-membrane localization are general biological knowledge accessible from the sequence.",
    "reason": "The sequence itself provides sufficient structural cues (7 hydrophobic TM segments, GPCR conserved motifs) to infer multi-pass membrane topology and, combined with general knowledge that GPCRs reside at the plasma membrane, to select option A over nuclear or synaptic alternatives without needing to look up the specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A3B3IT45 (Olfactory receptor OR51C1, Homo sapiens) annotates the protein as a 'Multi-pass membrane protein' located at 'Membrane' (ECO:0000305, ECO:0000255) and carries GO:0005886 (plasma membrane) via IBA:GO_Central. The sequence is 312 aa and matches the benchmark exactly. While the GO annotation uses computational inference (IBA), the protein is a canonical 7-transmembrane GPCR (olfactory receptor), a class universally localized to the plasma membrane. The expected answer 'plasma membrane' is consistent with both the database annotation and well-established biology of olfactory receptors."
  },
  "important_caveats": [
    "The GO:0005886 annotation uses evidence code IBA:GO_Central (computational inference by orthology), not direct experimental localization. The 'Membrane' and 'Multi-pass membrane protein' subcellular location annotations use ECO:0000305 (curator inference) and ECO:0000255 (sequence/structure similarity), respectively.",
    "The UniProt entry was first public in 2025-02-05; the benchmark author's exact source snapshot is unknown, though the sequence matches across versions.",
    "Olfactory receptors in humans are expressed on the cilia of olfactory sensory neurons; the 'plasma membrane' annotation refers to the neuronal plasma membrane (including ciliary membrane), not a generic cell surface."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are biologically distinct compartments (plasma membrane, nuclear kinase complex, chromatin, synapse). A 7-TM GPCR is unambiguously a plasma membrane protein; none of the other options are compatible with its topology or function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A3B3IT45 (Olfactory receptor OR51C1, Homo sapiens) annotates the protein as a 'Multi-pass membrane protein' located at 'Membrane' (ECO:0000305, ECO:0000255) and carries GO:0005886 (plasma membrane) via IBA:GO_Central. The sequence is 312 aa and matches the benchmark exactly. While the GO annotation uses computational inference (IBA), the protein is a canonical 7-transmembrane GPCR (olfactory receptor), a class universally localized to the plasma membrane. The expected answer 'plasma membrane' is consistent with both the database annotation and well-established biology of olfactory receptors.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 312-aa sequence exhibits the hallmark architecture of a 7-transmembrane G-protein-coupled receptor: multiple long hydrophobic stretches (~20-25 residues) separated by shorter hydrophilic loops, a DRY-like motif (DRFVAVSNPLRY near TM3), and an NPxxY-like motif (NPVIYSVKTKQ) near TM7. A biologist can reason: (1) multiple transmembrane helices → integral membrane protein; (2) 7-TM topology with GPCR signature motifs → GPCR family; (3) GPCRs are canonically plasma membrane receptors, not components of nuclear complexes (Dbf4-dependent kinase, chromatin) or synaptic junctions. The distractors (Dbf4 kinase complex, chromatin) are nuclear structures incompatible with a multi-pass membrane protein, and 'synapse' is a specialized junction not indicated by the sequence.",
    "missing_item_specific_fact": "None essential. Recognizing the specific olfactory receptor identity is not required; the 7-TM GPCR architecture and its plasma-membrane localization are general biological knowledge accessible from the sequence.",
    "reason": "The sequence itself provides sufficient structural cues (7 hydrophobic TM segments, GPCR conserved motifs) to infer multi-pass membrane topology and, combined with general knowledge that GPCRs reside at the plasma membrane, to select option A over nuclear or synaptic alternatives without needing to look up the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are biologically distinct compartments (plasma membrane, nuclear kinase complex, chromatin, synapse). A 7-TM GPCR is unambiguously a plasma membrane protein; none of the other options are compatible with its topology or function."
  },
  "important_caveats": [
    "The GO:0005886 annotation uses evidence code IBA:GO_Central (computational inference by orthology), not direct experimental localization. The 'Membrane' and 'Multi-pass membrane protein' subcellular location annotations use ECO:0000305 (curator inference) and ECO:0000255 (sequence/structure similarity), respectively.",
    "The UniProt entry was first public in 2025-02-05; the benchmark author's exact source snapshot is unknown, though the sequence matches across versions.",
    "Olfactory receptors in humans are expressed on the cilia of olfactory sensory neurons; the 'plasma membrane' annotation refers to the neuronal plasma membrane (including ciliary membrane), not a generic cell surface."
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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0162","value":"Membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/uniProtKBCrossReferences/26`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
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
**Locator:** `lines 44-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Multi-pass membrane
CC       protein {ECO:0000255}.
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 77-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IBA:GO_Central.
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 98. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
