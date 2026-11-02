# GO_biological_process_0189

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — adenylate cyclase-activating G protein-coupled receptor signaling pathway

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTQLPYLLDRRGGALAAPATAWGDMMLNRALFSVALLSSVGSAWVVLSYACIKELRSYRHQLILGLAISDLLMSLNFMFSAGWNVAGGDLALEESRTACSVNGFLTQVFVVQTDWWILVIAIATYIILGNFKTQSQFIQTHVWIPWVGPWVLSIIIAAICHGVLGYGYIGGWCWLTSDLMRLLINFIPRWLIVIAIALIYIRLYMIVRKARKWDIEGVSPDPGDDMADTSVILMSVGKKDRERQGSGVLVSRDVSVSFGRKGSTAPTFVTMVTTSGAGDSREAISSCSAREEGSRARTVNVNSSRSLSLGMRQPLNAAQLKRIAKKMMVYPVAYAIIWACPTAIRIYQGTTGSRAPLWITIVDKSCIVIQGLVDAVVYGLNERAWQGWRDHIRRIIYKNEGGRIIG

[Multiple Choices]
A. cilium disassembly
B. base-excision repair
C. adenylate cyclase-activating G protein-coupled receptor signaling pathway
D. regulation of DNA replication
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence matches the annotated GPR2 protein. Its UniProt function annotation says it senses nematode ascaroside pheromones and signals via adenylate cyclase; that annotation cites experimental evidence (ECO:0000269). The matching GO annotation for choice C is computationally assigned (IEA:TreeGrafter), so it should be distinguished from the cited functional evidence.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple strongly hydrophobic transmembrane segments characteristic of a seven-transmembrane receptor, which supports receptor-mediated signaling and distinguishes choice C from the DNA repair and DNA replication choices; it is also not characteristic of a cilium-disassembly factor.


**Missing item-specific fact**

> The sequence alone does not establish that this particular receptor signals through adenylate cyclase; that pathway-specific coupling is supported by protein-specific functional evidence, not by the transmembrane architecture alone.


**Reason**

> The sequence provides meaningful grounds to select GPCR signaling among these choices, although the adenylate-cyclase-specific mechanism is not independently inferable from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the choices, the GPCR-like sequence supports C substantially better than the DNA-related or cilium-disassembly alternatives.


### Important caveats

- The functional annotation cites a publication with experimental evidence, but the supplied reviewer evidence does not independently reproduce or assess the underlying experiments.
- The GO annotation itself is IEA:TreeGrafter, a computational annotation, rather than direct experimental GO evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic transmembrane segments characteristic of a seven-transmembrane receptor, which supports receptor-mediated signaling and distinguishes choice C from the DNA repair and DNA replication choices; it is also not characteristic of a cilium-disassembly factor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish that this particular receptor signals through adenylate cyclase; that pathway-specific coupling is supported by protein-specific functional evidence, not by the transmembrane architecture alone.",
    "reason": "The sequence provides meaningful grounds to select GPCR signaling among these choices, although the adenylate-cyclase-specific mechanism is not independently inferable from the supplied input."
  },
  "case_id": "GO_biological_process_0189",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated GPR2 protein. Its UniProt function annotation says it senses nematode ascaroside pheromones and signals via adenylate cyclase; that annotation cites experimental evidence (ECO:0000269). The matching GO annotation for choice C is computationally assigned (IEA:TreeGrafter), so it should be distinguished from the cited functional evidence."
  },
  "important_caveats": [
    "The functional annotation cites a publication with experimental evidence, but the supplied reviewer evidence does not independently reproduce or assess the underlying experiments.",
    "The GO annotation itself is IEA:TreeGrafter, a computational annotation, rather than direct experimental GO evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the choices, the GPCR-like sequence supports C substantially better than the DNA-related or cilium-disassembly alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0189",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated GPR2 protein. Its UniProt function annotation says it senses nematode ascaroside pheromones and signals via adenylate cyclase; that annotation cites experimental evidence (ECO:0000269). The matching GO annotation for choice C is computationally assigned (IEA:TreeGrafter), so it should be distinguished from the cited functional evidence.",
    "evidence_ids": ["H3", "H4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic transmembrane segments characteristic of a seven-transmembrane receptor, which supports receptor-mediated signaling and distinguishes choice C from the DNA repair and DNA replication choices; it is also not characteristic of a cilium-disassembly factor.",
    "missing_item_specific_fact": "The sequence alone does not establish that this particular receptor signals through adenylate cyclase; that pathway-specific coupling is supported by protein-specific functional evidence, not by the transmembrane architecture alone.",
    "reason": "The sequence provides meaningful grounds to select GPCR signaling among these choices, although the adenylate-cyclase-specific mechanism is not independently inferable from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the choices, the GPCR-like sequence supports C substantially better than the DNA-related or cilium-disassembly alternatives."
  },
  "important_caveats": [
    "The functional annotation cites a publication with experimental evidence, but the supplied reviewer evidence does not independently reproduce or assess the underlying experiments.",
    "The GO annotation itself is IEA:TreeGrafter, a computational annotation, rather than direct experimental GO evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (G1X9E2, Ascaroside receptor GPR2) carries an experimental-function annotation (ECO:0000269, PubMed:38649409) stating it is a 'G protein-coupled receptor that senses nematode ascaroside pheromones and signals via adenylate cyclase to positively regulate trap formation.' The GO term GO:0007189 (adenylate cyclase-activating GPCR signaling pathway) is annotated to this entry. The sequence itself displays a canonical 7-transmembrane GPCR topology with a DWW motif in TM3, consistent with the annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 406-aa sequence contains seven hydrophobic stretches of ~20-25 residues with alternating hydrophilic loops, a DWW motif in the third transmembrane segment (D2.50), and a long cytoplasmic loop with Ser/Thr-rich regions—hallmarks of a class-A (rhodopsin-like) 7TM GPCR. Recognizing this topology eliminates options B (base-excision repair: a nuclear DNA glycosylase/AP-endonuclease process) and D (regulation of DNA replication: a nuclear chromatin/cell-cycle process), both incompatible with a polytopic membrane receptor. Option A (cilium disassembly) describes structural breakdown of a microtubule-based organelle, not a primary signaling role of a GPCR. Among the four choices, only C names a GPCR signaling pathway, so identifying the protein as a GPCR from its transmembrane architecture is sufficient to select C.


**Missing item-specific fact**

> None strictly required. Distinguishing 'adenylate cyclase-activating' from other GPCR sub-pathways (e.g., phospholipase C-activating) would require ligand/G-protein coupling knowledge, but that specificity is unnecessary here because C is the sole GPCR-related option.


**Reason**

> The 7TM topology is extractable from the raw sequence by hydrophobicity analysis and conserved GPCR motifs (DWW in TM3, NPxxY-like region, long intracellular loop). This single structural inference eliminates three non-GPCR options and uniquely selects C without needing a database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D describe nuclear/DNA processes incompatible with a polytopic membrane protein. Option A (cilium disassembly) is a structural organelle-remodeling process, not a primary GPCR function. Only C is consistent with the 7TM GPCR architecture evident in the sequence.


### Important caveats

- The GO:0007189 annotation carries evidence code IEA:TreeGrafter (computational transfer), but the underlying experimental evidence (ECO:0000269, PubMed:38649409, Nat. Microbiol. 2024) supports the GPCR–adenylate cyclase signaling function.
- The protein is from a nematode-trapping fungus (Arthrobotrys oligospora), an organism where GPCR biology is less commonly encountered in training data; however, the 7TM topology is universal across eukaryotes and recognizable from sequence.
- The sequence-match between the benchmark input and UniProt G1X9E2 is confirmed (SHA-256 match, 406 aa).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 406-aa sequence contains seven hydrophobic stretches of ~20-25 residues with alternating hydrophilic loops, a DWW motif in the third transmembrane segment (D2.50), and a long cytoplasmic loop with Ser/Thr-rich regions—hallmarks of a class-A (rhodopsin-like) 7TM GPCR. Recognizing this topology eliminates options B (base-excision repair: a nuclear DNA glycosylase/AP-endonuclease process) and D (regulation of DNA replication: a nuclear chromatin/cell-cycle process), both incompatible with a polytopic membrane receptor. Option A (cilium disassembly) describes structural breakdown of a microtubule-based organelle, not a primary signaling role of a GPCR. Among the four choices, only C names a GPCR signaling pathway, so identifying the protein as a GPCR from its transmembrane architecture is sufficient to select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Distinguishing 'adenylate cyclase-activating' from other GPCR sub-pathways (e.g., phospholipase C-activating) would require ligand/G-protein coupling knowledge, but that specificity is unnecessary here because C is the sole GPCR-related option.",
    "reason": "The 7TM topology is extractable from the raw sequence by hydrophobicity analysis and conserved GPCR motifs (DWW in TM3, NPxxY-like region, long intracellular loop). This single structural inference eliminates three non-GPCR options and uniquely selects C without needing a database lookup."
  },
  "case_id": "GO_biological_process_0189",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (G1X9E2, Ascaroside receptor GPR2) carries an experimental-function annotation (ECO:0000269, PubMed:38649409) stating it is a 'G protein-coupled receptor that senses nematode ascaroside pheromones and signals via adenylate cyclase to positively regulate trap formation.' The GO term GO:0007189 (adenylate cyclase-activating GPCR signaling pathway) is annotated to this entry. The sequence itself displays a canonical 7-transmembrane GPCR topology with a DWW motif in TM3, consistent with the annotation."
  },
  "important_caveats": [
    "The GO:0007189 annotation carries evidence code IEA:TreeGrafter (computational transfer), but the underlying experimental evidence (ECO:0000269, PubMed:38649409, Nat. Microbiol. 2024) supports the GPCR–adenylate cyclase signaling function.",
    "The protein is from a nematode-trapping fungus (Arthrobotrys oligospora), an organism where GPCR biology is less commonly encountered in training data; however, the 7TM topology is universal across eukaryotes and recognizable from sequence.",
    "The sequence-match between the benchmark input and UniProt G1X9E2 is confirmed (SHA-256 match, 406 aa)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D describe nuclear/DNA processes incompatible with a polytopic membrane protein. Option A (cilium disassembly) is a structural organelle-remodeling process, not a primary GPCR function. Only C is consistent with the 7TM GPCR architecture evident in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0189",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (G1X9E2, Ascaroside receptor GPR2) carries an experimental-function annotation (ECO:0000269, PubMed:38649409) stating it is a 'G protein-coupled receptor that senses nematode ascaroside pheromones and signals via adenylate cyclase to positively regulate trap formation.' The GO term GO:0007189 (adenylate cyclase-activating GPCR signaling pathway) is annotated to this entry. The sequence itself displays a canonical 7-transmembrane GPCR topology with a DWW motif in TM3, consistent with the annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 406-aa sequence contains seven hydrophobic stretches of ~20-25 residues with alternating hydrophilic loops, a DWW motif in the third transmembrane segment (D2.50), and a long cytoplasmic loop with Ser/Thr-rich regions—hallmarks of a class-A (rhodopsin-like) 7TM GPCR. Recognizing this topology eliminates options B (base-excision repair: a nuclear DNA glycosylase/AP-endonuclease process) and D (regulation of DNA replication: a nuclear chromatin/cell-cycle process), both incompatible with a polytopic membrane receptor. Option A (cilium disassembly) describes structural breakdown of a microtubule-based organelle, not a primary signaling role of a GPCR. Among the four choices, only C names a GPCR signaling pathway, so identifying the protein as a GPCR from its transmembrane architecture is sufficient to select C.",
    "missing_item_specific_fact": "None strictly required. Distinguishing 'adenylate cyclase-activating' from other GPCR sub-pathways (e.g., phospholipase C-activating) would require ligand/G-protein coupling knowledge, but that specificity is unnecessary here because C is the sole GPCR-related option.",
    "reason": "The 7TM topology is extractable from the raw sequence by hydrophobicity analysis and conserved GPCR motifs (DWW in TM3, NPxxY-like region, long intracellular loop). This single structural inference eliminates three non-GPCR options and uniquely selects C without needing a database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D describe nuclear/DNA processes incompatible with a polytopic membrane protein. Option A (cilium disassembly) is a structural organelle-remodeling process, not a primary GPCR function. Only C is consistent with the 7TM GPCR architecture evident in the sequence."
  },
  "important_caveats": [
    "The GO:0007189 annotation carries evidence code IEA:TreeGrafter (computational transfer), but the underlying experimental evidence (ECO:0000269, PubMed:38649409, Nat. Microbiol. 2024) supports the GPCR–adenylate cyclase signaling function.",
    "The protein is from a nematode-trapping fungus (Arthrobotrys oligospora), an organism where GPCR biology is less commonly encountered in training data; however, the 7TM topology is universal across eukaryotes and recognizable from sequence.",
    "The sequence-match between the benchmark input and UniProt G1X9E2 is confirmed (SHA-256 match, 406 aa)."
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

**Accession:** `G1X9E2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 45. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Ascaroside receptor GPR2"}}}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38649409","source":"PubMed"}],"value":"G protein-coupled receptor that senses nematode ascaroside pheromones and signals via adenylate cyclase to positively regulate trap formation for nematode capture"}]}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"database":"GO","id":"GO:0007189","properties":[{"key":"GoTerm","value":"P:adenylate cyclase-activating G protein-coupled receptor signaling pathway"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 35-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
CC   -!- FUNCTION: G protein-coupled receptor that senses nematode ascaroside
CC       pheromones and signals via adenylate cyclase to positively regulate
CC       trap formation for nematode capture. {ECO:0000269|PubMed:38649409}.
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 71-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
DR   GO; GO:0007189; P:adenylate cyclase-activating G protein-coupled receptor signaling pathway; IEA:TreeGrafter.
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 74186-74212`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0007189
name: adenylate cyclase-activating G protein-coupled receptor signaling pathway
namespace: biological_process
alt_id: GO:0010579
alt_id: GO:0010580
def: "A G protein-coupled receptor signaling pathway in which the signal is transmitted via the activation of adenylyl cyclase activity which results in an increase in the intracellular concentration of cyclic AMP (cAMP). This pathway is negatively regulated by phosphodiesterase, which cleaves cAMP and terminates the signaling." [GOC:dph, GOC:mah, GOC:signaling, GOC:tb, ISBN:0815316194]
comment: This term can be used to annotate ligands, receptors and G-proteins that lead to activation of adenylate cyclase activity within a signaling pathway.
synonym: "activation of adenylate cyclase activity by G-protein signaling pathway" RELATED [GOC:bf]
synonym: "activation of adenylate cyclase activity involved in G-protein signaling" RELATED [GOC:signaling]
synonym: "adenylate cyclase-activating GPCR signaling pathway" EXACT [GOC:signaling]
synonym: "G protein signaling, adenylate cyclase activating pathway" EXACT []
synonym: "G protein signaling, adenylyl cyclase activating pathway" EXACT []
synonym: "G protein signalling, adenylate cyclase activating pathway" EXACT []
synonym: "G protein signalling, adenylyl cyclase activating pathway" EXACT []
synonym: "G-protein signaling, adenylate cyclase activating pathway" EXACT [GOC:dph, GOC:tb]
synonym: "G-protein signaling, adenylyl cyclase activating pathway" EXACT []
synonym: "G-protein signalling, adenylate cyclase activating pathway" EXACT []
synonym: "G-protein signalling, adenylyl cyclase activating pathway" EXACT []
synonym: "GPCR signaling pathway via activation of adenylate cyclase" EXACT [GOC:bf]
synonym: "GPCR signaling pathway via activation of adenylate cyclase activity" EXACT [GOC:signaling]
synonym: "positive regulation of adenylate cyclase activity by G-protein signaling pathway" RELATED [GOC:signaling]
synonym: "positive regulation of adenylate cyclase activity by G-protein signalling pathway" RELATED [GOC:mah]
synonym: "positive regulation of adenylate cyclase activity involved in G-protein coupled receptor signaling pathway" EXACT []
xref: Reactome:R-HSA-170660 "Adenylate cyclase activating pathway"
is_a: GO:0007188 ! adenylate cyclase-modulating G protein-coupled receptor signaling pathway

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 189. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
