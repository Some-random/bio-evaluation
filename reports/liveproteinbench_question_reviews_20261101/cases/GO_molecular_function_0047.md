# GO_molecular_function_0047

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — metal ion binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTLLDVRVAAIRELTPVIREYSFEALASTLPGFSAGSHVQLHLPNGRRNAYSLLSDPADTRQYRIAVRQQDASRGGSRYLHQHLKVGDRLRLSPPANLFPLHGEAQKHILVAAGIGITPFLAYSQELLRRGADFELHYAYRAGSSDAYVDELRQQLGPRLHEYLSGQRRLDLASLLQGRTLGTHVYACGPQSLLLDLQEQASAQGWSPRRVHWEAFAAAEPGQPFRVELARSGQQLEVAADESLLEALEAAGVEVPNLCRGGVCGQCQTPWLKGDVEHRDHFLSANERTSSLMPCVSRGCGSPILLDL

[Multiple Choices]
A. histone H3K9 acetyltransferase activity
B. metal ion binding
C. DNA N-glycosylase activity
D. deacetylase activity
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

> The exact-matched protein record describes the beta subunit as binding a 2Fe-2S cluster, and annotates metal ion binding. This supports B, although the GO metal-ion annotation itself is computationally assigned.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Cys-rich region near its C-terminus (…NLCRGGVCGQCQTP…), which is consistent with metal-coordinating residues in an iron-sulfur-cluster-binding protein. That makes metal ion binding the defensible choice over the histone-modifying and DNA-glycosylase activities offered.


**Missing item-specific fact**

> No protein-specific annotation or experiment is required to make this sequence-based inference, though such evidence would establish the binding more directly.


**Reason**

> The Cys-rich sequence feature provides a concrete biological clue for metal binding; this is more than identifying the exact sequence or merely invoking a predictor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, metal ion binding is supported by the sequence and the matched protein evidence. The options do not include the protein's broader oxidoreductase role.


### Important caveats

- The matched record reports binding a 2Fe-2S cluster; the broader metal-ion-binding GO annotation is marked as computationally assigned.
- The reviewer-only record supports the key but was not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Cys-rich region near its C-terminus (…NLCRGGVCGQCQTP…), which is consistent with metal-coordinating residues in an iron-sulfur-cluster-binding protein. That makes metal ion binding the defensible choice over the histone-modifying and DNA-glycosylase activities offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation or experiment is required to make this sequence-based inference, though such evidence would establish the binding more directly.",
    "reason": "The Cys-rich sequence feature provides a concrete biological clue for metal binding; this is more than identifying the exact sequence or merely invoking a predictor."
  },
  "case_id": "GO_molecular_function_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact-matched protein record describes the beta subunit as binding a 2Fe-2S cluster, and annotates metal ion binding. This supports B, although the GO metal-ion annotation itself is computationally assigned."
  },
  "important_caveats": [
    "The matched record reports binding a 2Fe-2S cluster; the broader metal-ion-binding GO annotation is marked as computationally assigned.",
    "The reviewer-only record supports the key but was not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, metal ion binding is supported by the sequence and the matched protein evidence. The options do not include the protein's broader oxidoreductase role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched protein record describes the beta subunit as binding a 2Fe-2S cluster, and annotates metal ion binding. This supports B, although the GO metal-ion annotation itself is computationally assigned.",
    "evidence_ids": ["C1", "C5", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Cys-rich region near its C-terminus (…NLCRGGVCGQCQTP…), which is consistent with metal-coordinating residues in an iron-sulfur-cluster-binding protein. That makes metal ion binding the defensible choice over the histone-modifying and DNA-glycosylase activities offered.",
    "missing_item_specific_fact": "No protein-specific annotation or experiment is required to make this sequence-based inference, though such evidence would establish the binding more directly.",
    "reason": "The Cys-rich sequence feature provides a concrete biological clue for metal binding; this is more than identifying the exact sequence or merely invoking a predictor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, metal ion binding is supported by the sequence and the matched protein evidence. The options do not include the protein's broader oxidoreductase role."
  },
  "important_caveats": [
    "The matched record reports binding a 2Fe-2S cluster; the broader metal-ion-binding GO annotation is marked as computationally assigned.",
    "The reviewer-only record supports the key but was not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A4XXY8 (HODMB_ECTM1) carries GO:0046872 (metal ion binding) annotated as IEA:UniProtKB-KW (H5), and GO:0051537 (2 iron, 2 sulfur cluster binding) as IEA:InterPro (C6/H4). The underlying fact is experimentally supported: the beta subunit binds FMN and a 2Fe-2S cluster (PubMed:27851736, Nature 2016; ECO:0000269 in C5/H3). Among the four options, B is the only GO term annotated for this protein. Options A, C, and D have no annotation or experimental basis. However, calling metal ion binding the 'primary' molecular function is a simplification: the protein's primary catalytic role is oxidoreductase activity (GO:0016491, also IEA), which is absent from the choices. B is the best and only defensible answer among the given options.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two cysteine-rich motifs — '...LCRGGVCGQCQTPWLK...' and '...LMPCVSRGCGSPILLDL' — whose Cys spacing (C-x-x-C and C-x-x-C patterns) is a well-known hallmark of 2Fe-2S cluster coordination. This provides positive sequence-level evidence for metal ion binding. Additionally, the protein is a ~309-residue bacterial enzyme (no eukaryotic chromatin context), which argues against histone H3K9 acetyltransferase (A). No recognizable DNA-glycosylase catalytic motifs (e.g., HhH-GPD, helix-turn-helix with N-terminal catalytic residues) or deacetylase motifs (e.g., the conserved His-Asp catalytic dyad of sirtuins or the HD domain of HDACs) are apparent. Process of elimination combined with the Cys-motif positive signal meaningfully distinguishes B.


**Missing item-specific fact**

> The exact identity of the protein as the HODM beta subunit and the experimental confirmation of 2Fe-2S cluster binding (Nature 2016) are not provided to the model. However, the Cys-rich motifs and bacterial context supply sufficient general biological reasoning to favor metal ion binding over the three unrelated distractors without requiring memorization of this specific entry.


**Reason**

> A model can identify Cys-x-x-C motifs as Fe-S cluster coordination sites, note the absence of acetyltransferase/glycosylase/deacetylase structural hallmarks, and use the bacterial origin to exclude eukaryotic chromatin-modifying functions. This constitutes a concrete, generalizable biological argument rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option B (metal ion binding) has any annotation or experimental basis for this protein. Options A, C, and D are entirely unrelated to a bacterial oxidoreductase beta subunit. The 'primary molecular function' framing slightly overstates metal ion binding (the true primary function is oxidoreductase, absent from choices), but among the four given options, B is unambiguously the only correct one.


### Important caveats

- The GO:0046872 (metal ion binding) annotation is IEA:UniProtKB-KW — an automatic keyword-based annotation, not a direct experimental assignment. The underlying 2Fe-2S cluster binding is experimentally supported (PubMed:27851736), but the specific GO term 'metal ion binding' is a broad, computationally assigned parent term.
- The protein's primary molecular function is oxidoreductase activity (GO:0016491), not metal ion binding. The question's 'primary molecular function' framing is imprecise; metal ion binding is a cofactor-supporting function. However, since oxidoreductase is not among the choices, B is the only defensible answer.
- The GO:0051537 (2Fe-2S cluster binding) annotation is more specific than GO:0046872 (metal ion binding) but is also IEA:InterPro. Neither specific annotation carries an experimental evidence code directly, though the experimental paper confirms the cluster.
- The accession A4XXY8 was inferred by the reviewer from dataset metadata, not from the model input. The model sees only the 309-aa sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two cysteine-rich motifs — '...LCRGGVCGQCQTPWLK...' and '...LMPCVSRGCGSPILLDL' — whose Cys spacing (C-x-x-C and C-x-x-C patterns) is a well-known hallmark of 2Fe-2S cluster coordination. This provides positive sequence-level evidence for metal ion binding. Additionally, the protein is a ~309-residue bacterial enzyme (no eukaryotic chromatin context), which argues against histone H3K9 acetyltransferase (A). No recognizable DNA-glycosylase catalytic motifs (e.g., HhH-GPD, helix-turn-helix with N-terminal catalytic residues) or deacetylase motifs (e.g., the conserved His-Asp catalytic dyad of sirtuins or the HD domain of HDACs) are apparent. Process of elimination combined with the Cys-motif positive signal meaningfully distinguishes B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact identity of the protein as the HODM beta subunit and the experimental confirmation of 2Fe-2S cluster binding (Nature 2016) are not provided to the model. However, the Cys-rich motifs and bacterial context supply sufficient general biological reasoning to favor metal ion binding over the three unrelated distractors without requiring memorization of this specific entry.",
    "reason": "A model can identify Cys-x-x-C motifs as Fe-S cluster coordination sites, note the absence of acetyltransferase/glycosylase/deacetylase structural hallmarks, and use the bacterial origin to exclude eukaryotic chromatin-modifying functions. This constitutes a concrete, generalizable biological argument rather than pure lookup."
  },
  "case_id": "GO_molecular_function_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "H5",
      "H6",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A4XXY8 (HODMB_ECTM1) carries GO:0046872 (metal ion binding) annotated as IEA:UniProtKB-KW (H5), and GO:0051537 (2 iron, 2 sulfur cluster binding) as IEA:InterPro (C6/H4). The underlying fact is experimentally supported: the beta subunit binds FMN and a 2Fe-2S cluster (PubMed:27851736, Nature 2016; ECO:0000269 in C5/H3). Among the four options, B is the only GO term annotated for this protein. Options A, C, and D have no annotation or experimental basis. However, calling metal ion binding the 'primary' molecular function is a simplification: the protein's primary catalytic role is oxidoreductase activity (GO:0016491, also IEA), which is absent from the choices. B is the best and only defensible answer among the given options."
  },
  "important_caveats": [
    "The GO:0046872 (metal ion binding) annotation is IEA:UniProtKB-KW — an automatic keyword-based annotation, not a direct experimental assignment. The underlying 2Fe-2S cluster binding is experimentally supported (PubMed:27851736), but the specific GO term 'metal ion binding' is a broad, computationally assigned parent term.",
    "The protein's primary molecular function is oxidoreductase activity (GO:0016491), not metal ion binding. The question's 'primary molecular function' framing is imprecise; metal ion binding is a cofactor-supporting function. However, since oxidoreductase is not among the choices, B is the only defensible answer.",
    "The GO:0051537 (2Fe-2S cluster binding) annotation is more specific than GO:0046872 (metal ion binding) but is also IEA:InterPro. Neither specific annotation carries an experimental evidence code directly, though the experimental paper confirms the cluster.",
    "The accession A4XXY8 was inferred by the reviewer from dataset metadata, not from the model input. The model sees only the 309-aa sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B (metal ion binding) has any annotation or experimental basis for this protein. Options A, C, and D are entirely unrelated to a bacterial oxidoreductase beta subunit. The 'primary molecular function' framing slightly overstates metal ion binding (the true primary function is oxidoreductase, absent from choices), but among the four given options, B is unambiguously the only correct one."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A4XXY8 (HODMB_ECTM1) carries GO:0046872 (metal ion binding) annotated as IEA:UniProtKB-KW (H5), and GO:0051537 (2 iron, 2 sulfur cluster binding) as IEA:InterPro (C6/H4). The underlying fact is experimentally supported: the beta subunit binds FMN and a 2Fe-2S cluster (PubMed:27851736, Nature 2016; ECO:0000269 in C5/H3). Among the four options, B is the only GO term annotated for this protein. Options A, C, and D have no annotation or experimental basis. However, calling metal ion binding the 'primary' molecular function is a simplification: the protein's primary catalytic role is oxidoreductase activity (GO:0016491, also IEA), which is absent from the choices. B is the best and only defensible answer among the given options.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "H5", "H6", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two cysteine-rich motifs — '...LCRGGVCGQCQTPWLK...' and '...LMPCVSRGCGSPILLDL' — whose Cys spacing (C-x-x-C and C-x-x-C patterns) is a well-known hallmark of 2Fe-2S cluster coordination. This provides positive sequence-level evidence for metal ion binding. Additionally, the protein is a ~309-residue bacterial enzyme (no eukaryotic chromatin context), which argues against histone H3K9 acetyltransferase (A). No recognizable DNA-glycosylase catalytic motifs (e.g., HhH-GPD, helix-turn-helix with N-terminal catalytic residues) or deacetylase motifs (e.g., the conserved His-Asp catalytic dyad of sirtuins or the HD domain of HDACs) are apparent. Process of elimination combined with the Cys-motif positive signal meaningfully distinguishes B.",
    "missing_item_specific_fact": "The exact identity of the protein as the HODM beta subunit and the experimental confirmation of 2Fe-2S cluster binding (Nature 2016) are not provided to the model. However, the Cys-rich motifs and bacterial context supply sufficient general biological reasoning to favor metal ion binding over the three unrelated distractors without requiring memorization of this specific entry.",
    "reason": "A model can identify Cys-x-x-C motifs as Fe-S cluster coordination sites, note the absence of acetyltransferase/glycosylase/deacetylase structural hallmarks, and use the bacterial origin to exclude eukaryotic chromatin-modifying functions. This constitutes a concrete, generalizable biological argument rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B (metal ion binding) has any annotation or experimental basis for this protein. Options A, C, and D are entirely unrelated to a bacterial oxidoreductase beta subunit. The 'primary molecular function' framing slightly overstates metal ion binding (the true primary function is oxidoreductase, absent from choices), but among the four given options, B is unambiguously the only correct one."
  },
  "important_caveats": [
    "The GO:0046872 (metal ion binding) annotation is IEA:UniProtKB-KW — an automatic keyword-based annotation, not a direct experimental assignment. The underlying 2Fe-2S cluster binding is experimentally supported (PubMed:27851736), but the specific GO term 'metal ion binding' is a broad, computationally assigned parent term.",
    "The protein's primary molecular function is oxidoreductase activity (GO:0016491), not metal ion binding. The question's 'primary molecular function' framing is imprecise; metal ion binding is a cofactor-supporting function. However, since oxidoreductase is not among the choices, B is the only defensible answer.",
    "The GO:0051537 (2Fe-2S cluster binding) annotation is more specific than GO:0046872 (metal ion binding) but is also IEA:InterPro. Neither specific annotation carries an experimental evidence code directly, though the experimental paper confirms the cluster.",
    "The accession A4XXY8 was inferred by the reviewer from dataset metadata, not from the model input. The model sees only the 309-aa sequence."
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

**Accession:** `A4XXY8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 114. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:59.775561+00:00.  

```json
"A4XXY8"
```

Source SHA-256: `14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:59.775561+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27851736","source":"PubMed"}],"value":"Component of the heme-dependent oxidative N-demethylase (HODM) enzyme, that catalyzes the NADPH-dependent oxidation of dimethylamine (DMA) to methylamine (MA) and formaldehyde. Functions in bacterial methylated amine catabolism, linking alkylamine oxidation to the tetrahydrofolate C1 pool. The beta subunit of HODM binds FMN and a 2Fe-2S cluster, and likely reduces the ferric heme iron of the alpha subunit to ferrous using NADPH"}]}
```

Source SHA-256: `14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY8.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:59.775561+00:00.  

```json
{"database":"GO","id":"GO:0051537","properties":[{"key":"GoTerm","value":"F:2 iron, 2 sulfur cluster binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114)  
**Locator:** `lines 32-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:27:01.748975+00:00.  

```text
CC   -!- FUNCTION: Component of the heme-dependent oxidative N-demethylase
CC       (HODM) enzyme, that catalyzes the NADPH-dependent oxidation of
CC       dimethylamine (DMA) to methylamine (MA) and formaldehyde. Functions in
CC       bacterial methylated amine catabolism, linking alkylamine oxidation to
CC       the tetrahydrofolate C1 pool. The beta subunit of HODM binds FMN and a
CC       2Fe-2S cluster, and likely reduces the ferric heme iron of the alpha
CC       subunit to ferrous using NADPH. {ECO:0000269|PubMed:27851736}.
```

Source SHA-256: `76f92cfc1f9ead1f561371a2da8acce3787355263fc28bb8326613f4ec3df955`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114)  
**Locator:** `lines 66-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:27:01.748975+00:00.  

```text
DR   GO; GO:0051537; F:2 iron, 2 sulfur cluster binding; IEA:UniProtKB-KW.
```

Source SHA-256: `76f92cfc1f9ead1f561371a2da8acce3787355263fc28bb8326613f4ec3df955`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114)  
**Locator:** `lines 67-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:27:01.748975+00:00.  

```text
DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.
```

Source SHA-256: `76f92cfc1f9ead1f561371a2da8acce3787355263fc28bb8326613f4ec3df955`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114)  
**Locator:** `lines 68-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:27:01.748975+00:00.  

```text
DR   GO; GO:0016491; F:oxidoreductase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `76f92cfc1f9ead1f561371a2da8acce3787355263fc28bb8326613f4ec3df955`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 281280-281292`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0046872
name: metal ion binding
namespace: molecular_function
def: "Binding to a metal ion." [GOC:ai]
subset: goslim_agr
subset: goslim_drosophila
subset: goslim_flybase_ribbon
subset: goslim_metagenomics
synonym: "heavy metal binding" NARROW []
synonym: "metal binding" EXACT []
is_a: GO:0043169 ! cation binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 47. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
