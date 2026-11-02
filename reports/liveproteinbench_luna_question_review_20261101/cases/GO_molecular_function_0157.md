# GO_molecular_function_0157

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — G protein-coupled receptor activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MKQNPAKTARMWIIICLLFVLGQATDNDRDFKMCGKWLHGIAPQNLEYDLKTGCERIEISANESTLSIQGRITAKCTQSSSIQLDSNPHQNQSHFCVFWEPLLDLLIVEVNGKNHTLCKPNGLQGTCCTDLSQGVQDNAHMYGIVNGSVKGDIITGDLKGNYIFDGAHINCKEKFCDEARLKPRGANMIEEVVMRFNAKGRVDLPCAQGTVIEMDEEFTGHNFTVPAPRFVDANTIPSVYIPSSLRSVSRRKSKVVCTYYKNKTLFERGPSKSALLDDIVGLSVENETIRNLIEPVKIRFHHRPFAPDSSGRCVSWDTKQDNEVNWKDDGCDTVKINEEQTECHCNHLTYFAILVQVEQKSTVRHLKALTFITAVGCAVSLVSCLVLFYWLCKRRRGKKNQISLVHRGLVVAIFLLCLFFILTGILANVANETVCQLTGSLLHYGLLSTLCWMAMEVFHTFLLVRKVFNSPLPIWIFYLMGFGFPFLLVSILLSVGDIYGERKIKPSDDVNNPYRMCWMTEGDKSQLAHYIINIGLLAVVVSSGLVMLFLVVREIRNRPDWKKIHVAFLSIWGLTCLYGTTWALGFLDFGPFSEVTLFLFCIINSLQGFFLMLRYYALERMKKKDVSSSDGSSSGSSKQHMLQTNEKS

[Multiple Choices]
A. cardiolipin synthase activity
B. manganese ion binding
C. G protein-coupled receptor activity
D. rRNA (uridine-N3-)-methyltransferase activity
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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence matches the zebrafish ADGRG1 protein, and the matched entry annotates G protein-coupled receptor activity. Its function annotation is supported by cited experimental evidence for G-protein signaling; the GO term itself is annotated by computational inference (IEA:InterPro).

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a large extracellular N-terminal region followed by a cluster of seven strongly hydrophobic membrane-spanning segments and a cytoplasmic tail, a characteristic GPCR architecture. This meaningfully favors GPCR activity over the listed enzymatic alternatives.

**Missing item-specific fact**

> No protein-specific annotation is necessary to distinguish these choices at the broad functional level, though experimental evidence or family identification would confirm the receptor's precise activity.

**Reason**

> The supplied sequence itself provides a recognizable GPCR topology, while the distractors describe unrelated enzyme activities or ion binding.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The seven-transmembrane receptor architecture strongly distinguishes choice C from the other listed functions.

### Important caveats

- The reviewer-only database evidence supports the key but was not supplied to the evaluated model.
- The GO annotation is computationally inferred; separate cited experimental evidence supports the protein's G-protein signaling function.
- Sequence architecture supports the broad receptor classification but does not by itself establish every detail of ligand or signaling specificity.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the zebrafish ADGRG1 protein, and the matched entry annotates G protein-coupled receptor activity. Its function annotation is supported by cited experimental evidence for G-protein signaling; the GO term itself is annotated by computational inference (IEA:InterPro).",
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4",
      "H5"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a large extracellular N-terminal region followed by a cluster of seven strongly hydrophobic membrane-spanning segments and a cytoplasmic tail, a characteristic GPCR architecture. This meaningfully favors GPCR activity over the listed enzymatic alternatives.",
    "missing_item_specific_fact": "No protein-specific annotation is necessary to distinguish these choices at the broad functional level, though experimental evidence or family identification would confirm the receptor's precise activity.",
    "reason": "The supplied sequence itself provides a recognizable GPCR topology, while the distractors describe unrelated enzyme activities or ion binding."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The seven-transmembrane receptor architecture strongly distinguishes choice C from the other listed functions."
  },
  "important_caveats": [
    "The reviewer-only database evidence supports the key but was not supplied to the evaluated model.",
    "The GO annotation is computationally inferred; separate cited experimental evidence supports the protein's G-protein signaling function.",
    "Sequence architecture supports the broad receptor classification but does not by itself establish every detail of ligand or signaling specificity."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q59I63`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 119. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
"Q59I63"
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25607772","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29367382","source":"PubMed"}],"value":"Adhesion G protein-coupled receptor (aGPCR), which is involved in oligodendrocyte development and maintenance of peripheral myelin (PubMed:25607772, PubMed:29367382). Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as RhoA pathway (PubMed:25607772). Adgrg1 is coupled to G(12) and/or G(13) G proteins (gna12 and gna13, respectively) and mediates the activation Rho small GTPases (PubMed:25607772, PubMed:29367382). Adgrg1-dependent RhoA signaling promotes timely radial sorting of axons (PubMed:29367382). Required to establish proper myelin thickness and facilitate organization of the myelin sheath in the mature peripheral nervous system (PubMed:29367382)"}]}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/uniProtKBCrossReferences/27`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"database":"GO","id":"GO:0004930","properties":[{"key":"GoTerm","value":"F:G protein-coupled receptor activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 93-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
CC   -!- FUNCTION: Adhesion G-protein coupled receptor (aGPCR), which is
CC       involved in oligodendrocyte development and maintenance of peripheral
CC       myelin (PubMed:25607772, PubMed:29367382). Ligand binding causes a
CC       conformation change that triggers signaling via guanine nucleotide-
CC       binding proteins (G proteins) and modulates the activity of downstream
CC       effectors, such as RhoA pathway (PubMed:25607772). Adgrg1 is coupled to
CC       G(12) and/or G(13) G proteins (gna12 and gna13, respectively) and
CC       mediates the activation Rho small GTPases (PubMed:25607772,
CC       PubMed:29367382). Adgrg1-dependent RhoA signaling promotes timely
CC       radial sorting of axons (PubMed:29367382). Required to establish proper
CC       myelin thickness and facilitate organization of the myelin sheath in
CC       the mature peripheral nervous system (PubMed:29367382).
CC       {ECO:0000269|PubMed:25607772, ECO:0000269|PubMed:29367382}.
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 169-169`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
DR   GO; GO:0004930; F:G protein-coupled receptor activity; IEA:InterPro.
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 157). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
