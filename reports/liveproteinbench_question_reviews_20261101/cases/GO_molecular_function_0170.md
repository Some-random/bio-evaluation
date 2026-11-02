# GO_molecular_function_0170

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — UDP-glucuronate decarboxylase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKKRCLITGGAGFIGSHLAEELVKRGHPVTIVDNFYKGKSKYHEELTGNIPIIPISILDKNSMHELVNQHDVVFHLAAILGVKTTMEKSIELIETNFDGTRNILQAALKGKKKVIFASTSEVYGKGTPPFSEDDDRLYGATSKIRWSYAICKTLEETLCLGYALQGLPVTIVRYFNIYGPRAKDGPYAGVIPRFIRAALQGDDLLVYGDGKQTRCFTYVSDAVEATIAAMDEKVNGEIINIGSEDEKSIQEVAQDIHQLTHSSSKIVHVPFEKVYPHGFEEIPNRKPDVTKLKEMCQFHPNVSWEQGLKETIQWFREIEND

[Multiple Choices]
A. tRNA (guanine(18)-2'-O)-methyltransferase activity
B. UDP-glucuronate decarboxylase activity
C. histone kinase activity
D. protein-folding chaperone binding
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

### Expected-answer support: contradicted

> The sequence-matched protein is experimentally described as catalyzing decarboxylation of UDP-GlcNAcA to UDP-XylNAc and as unable to use UDP-glucuronic acid. Option B denotes decarboxylation of UDP-glucuronate to UDP-xylose, so the specific substrate and product do not match. Its GO annotation for B is computational (IEA:TreeGrafter), not experimental confirmation of that activity.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with an enzyme, but no supplied context or clear sequence feature distinguishes its exact nucleotide-sugar substrate specificity from the alternatives. Inferring a precise substrate and reaction requires protein-specific functional knowledge.


**Missing item-specific fact**

> The protein's experimentally characterized substrate specificity and catalytic reaction; specifically, that it acts on UDP-GlcNAcA rather than UDP-glucuronate.


**Reason**

> The sequence alone does not establish the specific molecular function at the level needed to choose among these options. Knowing the exact enzyme identity or its experimentally characterized reaction would require an external protein-specific fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports a decarboxylase function, but none of the options states the characterized UDP-GlcNAcA decarboxylase activity. Option B is related but specifies a different substrate and product.


### Important caveats

- The sequence match and experimental-function annotation apply to the supplied sequence, but the author's source snapshot is unknown.
- The GO annotation for option B is present in UniProt, but its IEA:TreeGrafter evidence is computational and conflicts with the stated experimentally characterized substrate specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, but no supplied context or clear sequence feature distinguishes its exact nucleotide-sugar substrate specificity from the alternatives. Inferring a precise substrate and reaction requires protein-specific functional knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally characterized substrate specificity and catalytic reaction; specifically, that it acts on UDP-GlcNAcA rather than UDP-glucuronate.",
    "reason": "The sequence alone does not establish the specific molecular function at the level needed to choose among these options. Knowing the exact enzyme identity or its experimentally characterized reaction would require an external protein-specific fact."
  },
  "case_id": "GO_molecular_function_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "GO2"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched protein is experimentally described as catalyzing decarboxylation of UDP-GlcNAcA to UDP-XylNAc and as unable to use UDP-glucuronic acid. Option B denotes decarboxylation of UDP-glucuronate to UDP-xylose, so the specific substrate and product do not match. Its GO annotation for B is computational (IEA:TreeGrafter), not experimental confirmation of that activity."
  },
  "important_caveats": [
    "The sequence match and experimental-function annotation apply to the supplied sequence, but the author's source snapshot is unknown.",
    "The GO annotation for option B is present in UniProt, but its IEA:TreeGrafter evidence is computational and conflicts with the stated experimentally characterized substrate specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports a decarboxylase function, but none of the options states the characterized UDP-GlcNAcA decarboxylase activity. Option B is related but specifies a different substrate and product."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0170",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched protein is experimentally described as catalyzing decarboxylation of UDP-GlcNAcA to UDP-XylNAc and as unable to use UDP-glucuronic acid. Option B denotes decarboxylation of UDP-glucuronate to UDP-xylose, so the specific substrate and product do not match. Its GO annotation for B is computational (IEA:TreeGrafter), not experimental confirmation of that activity.",
    "evidence_ids": ["C5", "C6", "C8", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, but no supplied context or clear sequence feature distinguishes its exact nucleotide-sugar substrate specificity from the alternatives. Inferring a precise substrate and reaction requires protein-specific functional knowledge.",
    "missing_item_specific_fact": "The protein's experimentally characterized substrate specificity and catalytic reaction; specifically, that it acts on UDP-GlcNAcA rather than UDP-glucuronate.",
    "reason": "The sequence alone does not establish the specific molecular function at the level needed to choose among these options. Knowing the exact enzyme identity or its experimentally characterized reaction would require an external protein-specific fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports a decarboxylase function, but none of the options states the characterized UDP-GlcNAcA decarboxylase activity. Option B is related but specifies a different substrate and product."
  },
  "important_caveats": [
    "The sequence match and experimental-function annotation apply to the supplied sequence, but the author's source snapshot is unknown.",
    "The GO annotation for option B is present in UniProt, but its IEA:TreeGrafter evidence is computational and conflicts with the stated experimentally characterized substrate specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The UniProt entry for A7GKX7 carries GO:0048040 (UDP-glucuronate decarboxylase activity) only via IEA:TreeGrafter (computational transfer). The experimental evidence (PubMed:20529859, ECO:0000269) in C5/H3 explicitly states the protein 'Cannot use other UDP-uronates, such as UDP-glucuronic acid (UDP-GlcA).' The protein's actual experimentally verified activity is UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase (EC 4.1.1.128), a different enzyme (EC 4.1.1.128 vs. EC 4.1.1.35 for GO:0048040). The GO annotation is an imprecise family-level computational transfer contradicted by the primary experimental data.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal 'GGAGFIGS' motif is a canonical Rossmann-fold NAD-binding signature found in NAD-dependent UDP-uronate decarboxylases and related dehydrogenases. This immediately rules out: (D) chaperone binding (a protein-protein interaction, not a catalytic activity; the sequence clearly encodes an enzyme), (C) histone kinase activity (kinases require a distinct bilobal kinase fold absent here, and this is a bacterial protein), and (A) tRNA methyltransferase (class I methyltransferases use a different Rossmann variant with a catalytic motif and lack the extended C-terminal UDP-sugar-binding domain seen here). Among the four choices, only B belongs to the NAD-dependent UDP-sugar decarboxylase superfamily, making it the uniquely defensible answer.


**Missing item-specific fact**

> Distinguishing the true substrate (UDP-GlcNAcA, EC 4.1.1.128) from the annotated substrate (UDP-glucuronate, EC 4.1.1.35) requires the specific experimental substrate-specificity data from PubMed:20529859. However, since UDP-GlcNAcA decarboxylase is not among the options, the reasoning path to B as the best available choice is intact.


**Reason**

> General knowledge of Rossmann-fold NAD-binding motifs, enzyme vs. binding protein architecture, and the distinction between bacterial metabolic enzymes and eukaryotic kinases/chaperones provides a concrete biological argument to eliminate A, C, and D and select B. The question does not require memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are clearly incompatible with the sequence architecture (bacterial NAD-dependent enzyme with Rossmann fold). Only B falls within the correct enzyme superfamily. No ambiguity among the four choices.


### Important caveats

- The expected answer B (UDP-glucuronate decarboxylase activity, GO:0048040, EC 4.1.1.35) is annotated in UniProt only via IEA:TreeGrafter and is contradicted by experimental evidence showing the protein acts on UDP-GlcNAcA (EC 4.1.1.128), not UDP-glucuronate.
- The benchmark key likely derives from the UniProt GO annotation list, which includes this imprecise TreeGrafter transfer. The true molecular function is UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase activity.
- Despite the substrate-specificity error in the key, B remains the best answer among the four provided options because it is the only one in the correct enzyme superfamily (NAD-dependent UDP-uronate decarboxylase).
- Sequence match to UniProt A7GKX7 is confirmed (SHA-256 match, 321 AA, both current and historical entry v94).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal 'GGAGFIGS' motif is a canonical Rossmann-fold NAD-binding signature found in NAD-dependent UDP-uronate decarboxylases and related dehydrogenases. This immediately rules out: (D) chaperone binding (a protein-protein interaction, not a catalytic activity; the sequence clearly encodes an enzyme), (C) histone kinase activity (kinases require a distinct bilobal kinase fold absent here, and this is a bacterial protein), and (A) tRNA methyltransferase (class I methyltransferases use a different Rossmann variant with a catalytic motif and lack the extended C-terminal UDP-sugar-binding domain seen here). Among the four choices, only B belongs to the NAD-dependent UDP-sugar decarboxylase superfamily, making it the uniquely defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Distinguishing the true substrate (UDP-GlcNAcA, EC 4.1.1.128) from the annotated substrate (UDP-glucuronate, EC 4.1.1.35) requires the specific experimental substrate-specificity data from PubMed:20529859. However, since UDP-GlcNAcA decarboxylase is not among the options, the reasoning path to B as the best available choice is intact.",
    "reason": "General knowledge of Rossmann-fold NAD-binding motifs, enzyme vs. binding protein architecture, and the distinction between bacterial metabolic enzymes and eukaryotic kinases/chaperones provides a concrete biological argument to eliminate A, C, and D and select B. The question does not require memorizing this specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6",
      "GO2"
    ],
    "judgment": "contradicted",
    "reason": "The UniProt entry for A7GKX7 carries GO:0048040 (UDP-glucuronate decarboxylase activity) only via IEA:TreeGrafter (computational transfer). The experimental evidence (PubMed:20529859, ECO:0000269) in C5/H3 explicitly states the protein 'Cannot use other UDP-uronates, such as UDP-glucuronic acid (UDP-GlcA).' The protein's actual experimentally verified activity is UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase (EC 4.1.1.128), a different enzyme (EC 4.1.1.128 vs. EC 4.1.1.35 for GO:0048040). The GO annotation is an imprecise family-level computational transfer contradicted by the primary experimental data."
  },
  "important_caveats": [
    "The expected answer B (UDP-glucuronate decarboxylase activity, GO:0048040, EC 4.1.1.35) is annotated in UniProt only via IEA:TreeGrafter and is contradicted by experimental evidence showing the protein acts on UDP-GlcNAcA (EC 4.1.1.128), not UDP-glucuronate.",
    "The benchmark key likely derives from the UniProt GO annotation list, which includes this imprecise TreeGrafter transfer. The true molecular function is UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase activity.",
    "Despite the substrate-specificity error in the key, B remains the best answer among the four provided options because it is the only one in the correct enzyme superfamily (NAD-dependent UDP-uronate decarboxylase).",
    "Sequence match to UniProt A7GKX7 is confirmed (SHA-256 match, 321 AA, both current and historical entry v94)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with the sequence architecture (bacterial NAD-dependent enzyme with Rossmann fold). Only B falls within the correct enzyme superfamily. No ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0170",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The UniProt entry for A7GKX7 carries GO:0048040 (UDP-glucuronate decarboxylase activity) only via IEA:TreeGrafter (computational transfer). The experimental evidence (PubMed:20529859, ECO:0000269) in C5/H3 explicitly states the protein 'Cannot use other UDP-uronates, such as UDP-glucuronic acid (UDP-GlcA).' The protein's actual experimentally verified activity is UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase (EC 4.1.1.128), a different enzyme (EC 4.1.1.128 vs. EC 4.1.1.35 for GO:0048040). The GO annotation is an imprecise family-level computational transfer contradicted by the primary experimental data.",
    "evidence_ids": ["C5", "C6", "C8", "H3", "H4", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal 'GGAGFIGS' motif is a canonical Rossmann-fold NAD-binding signature found in NAD-dependent UDP-uronate decarboxylases and related dehydrogenases. This immediately rules out: (D) chaperone binding (a protein-protein interaction, not a catalytic activity; the sequence clearly encodes an enzyme), (C) histone kinase activity (kinases require a distinct bilobal kinase fold absent here, and this is a bacterial protein), and (A) tRNA methyltransferase (class I methyltransferases use a different Rossmann variant with a catalytic motif and lack the extended C-terminal UDP-sugar-binding domain seen here). Among the four choices, only B belongs to the NAD-dependent UDP-sugar decarboxylase superfamily, making it the uniquely defensible answer.",
    "missing_item_specific_fact": "Distinguishing the true substrate (UDP-GlcNAcA, EC 4.1.1.128) from the annotated substrate (UDP-glucuronate, EC 4.1.1.35) requires the specific experimental substrate-specificity data from PubMed:20529859. However, since UDP-GlcNAcA decarboxylase is not among the options, the reasoning path to B as the best available choice is intact.",
    "reason": "General knowledge of Rossmann-fold NAD-binding motifs, enzyme vs. binding protein architecture, and the distinction between bacterial metabolic enzymes and eukaryotic kinases/chaperones provides a concrete biological argument to eliminate A, C, and D and select B. The question does not require memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with the sequence architecture (bacterial NAD-dependent enzyme with Rossmann fold). Only B falls within the correct enzyme superfamily. No ambiguity among the four choices."
  },
  "important_caveats": [
    "The expected answer B (UDP-glucuronate decarboxylase activity, GO:0048040, EC 4.1.1.35) is annotated in UniProt only via IEA:TreeGrafter and is contradicted by experimental evidence showing the protein acts on UDP-GlcNAcA (EC 4.1.1.128), not UDP-glucuronate.",
    "The benchmark key likely derives from the UniProt GO annotation list, which includes this imprecise TreeGrafter transfer. The true molecular function is UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase activity.",
    "Despite the substrate-specificity error in the key, B remains the best answer among the four provided options because it is the only one in the correct enzyme superfamily (NAD-dependent UDP-uronate decarboxylase).",
    "Sequence match to UniProt A7GKX7 is confirmed (SHA-256 match, 321 AA, both current and historical entry v94)."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `explicit_negative_substrate_evidence_traced`.

> C5 explicitly states inability to use UDP-glucuronic acid, while GO2 defines the keyed UDP-glucuronate decarboxylase reaction. C6 instead uses UDP-GlcNAcA; C8 nevertheless assigns the key via IEA:TreeGrafter.

**Remaining uncertainty:** This is stronger than mere absence: the supplied function text explicitly names the unusable keyed substrate. Primary assay conditions/paper were not independently reviewed.

Evidence checked: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [GO2](#evidence-go2).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A7GKX7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 94. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.082856+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"value":"Decarboxylase involved in the biosynthesis of the nucleotide-sugar UDP-N-acetylxylosamine (UDP-XylNAc) (PubMed:20529859). Catalyzes the NAD-dependent decarboxylation of UDP-N-acetylglucosaminuronic acid (UDP-GlcNAcA) to UDP-XylNAc (PubMed:20529859). Cannot use other UDP-uronates, such as UDP-glucuronic acid (UDP-GlcA) and UDP-galacturonic acid (UDP-GalA) (PubMed:20529859)"}]}
```

Source SHA-256: `e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.082856+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81488"}}],"reaction":{"ecNumber":"4.1.1.128","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"name":"UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81487"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:65040"},{"database":"ChEBI","id":"CHEBI:231888"}]}}
```

Source SHA-256: `e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.082856+00:00.  

```json
{"database":"GO","id":"GO:0048040","properties":[{"key":"GoTerm","value":"F:UDP-glucuronate decarboxylase activity"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)  
**Locator:** `lines 36-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 94 / 1.  
**Retrieved:** 2026-11-01T06:27:51.337169+00:00.  

```text
CC   -!- FUNCTION: Decarboxylase involved in the biosynthesis of the nucleotide-
CC       sugar UDP-N-acetylxylosamine (UDP-XylNAc) (PubMed:20529859). Catalyzes
CC       the NAD-dependent decarboxylation of UDP-N-acetylglucosaminuronic acid
CC       (UDP-GlcNAcA) to UDP-XylNAc (PubMed:20529859). Cannot use other UDP-
CC       uronates, such as UDP-glucuronic acid (UDP-GlcA) and UDP-galacturonic
CC       acid (UDP-GalA) (PubMed:20529859). {ECO:0000269|PubMed:20529859}.
```

Source SHA-256: `3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 94 / 1.  
**Retrieved:** 2026-11-01T06:27:51.337169+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-
CC         acetyl-alpha-D-xylosamine + CO2; Xref=Rhea:RHEA:81487,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:65040,
CC         ChEBI:CHEBI:231888; EC=4.1.1.128;
CC         Evidence={ECO:0000269|PubMed:20529859};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81488;
CC         Evidence={ECO:0000269|PubMed:20529859};
```

Source SHA-256: `3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)  
**Locator:** `lines 89-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 94 / 1.  
**Retrieved:** 2026-11-01T06:27:51.337169+00:00.  

```text
DR   GO; GO:0048040; F:UDP-glucuronate decarboxylase activity; IEA:TreeGrafter.
```

Source SHA-256: `3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 300082-300100`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0048040
name: UDP-glucuronate decarboxylase activity
namespace: molecular_function
def: "Catalysis of the reaction: H+ + UDP-alpha-D-glucuronate = CO2 + UDP-alpha-D-xylose." [EC:4.1.1.35, RHEA:23916]
synonym: "UDP-D-glucuronate carboxy-lyase (UDP-D-xylose-forming)" RELATED [EC:4.1.1.35]
synonym: "UDP-D-glucuronate carboxy-lyase activity" RELATED [EC:4.1.1.35]
synonym: "UDP-glucuronic acid decarboxylase activity" EXACT []
synonym: "UDPglucuronate decarboxylase activity" RELATED [EC:4.1.1.35]
synonym: "uridine-diphosphoglucuronate decarboxylase activity" RELATED [EC:4.1.1.35]
xref: EC:4.1.1.35
xref: KEGG_REACTION:R01384
xref: MetaCyc:UDP-GLUCURONATE-DECARBOXYLASE-RXN
xref: Reactome:R-HSA-8863761 "UXS1 tetramer decarboxylates UDP-glucuronate to UDP-xylose"
xref: RHEA:23916
is_a: GO:0016831 ! carboxy-lyase activity
property_value: skos:exactMatch EC:4.1.1.35
property_value: skos:exactMatch RHEA:23916

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 170. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
