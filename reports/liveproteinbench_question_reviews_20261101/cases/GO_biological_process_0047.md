# GO_biological_process_0047

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — microtubule cytoskeleton organization

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MESGPRVEPGPGAPAAVLARIPQEPRPSPEGDPSPPPPPTPMSALVPDTPPDTPPAMKNASTPQQLPLEPVSPTGQVSPQPAPPPDECPSSEAKSRGPTPTATGPRDAKPSQRSSQPSPTAVPASDSPSAKQDVKKAGERHKLAKERREERAKYLAAKKAVWLEKEEKAKALREKQLQERRRRLEEQRLKAEQRRAALEERQRQKLEKNKERYEAAIQRSVKKTWAEIRQQRWSWAGALHHNSPGRKTSGSRCSVSAVNLPKHVDSIINKRLSKSSATLWNSPSRNRSLQLSAWESSIVDRLMTPTLSFLARSRSAVTLPRNGRDQGRGSGPGRRPTRARAGASLAPGPHPDRTHPSAAVPVCPRSASASPLTPCSAPRSAHRCTPSGERPERRKPGAGGSPALVRRRLEATPVQKKEKKDKERENEKEKSALARERNLKKRQSLPASIRPRISTGAELSTKSKARPTSPSTTWHRPASPCPSPGPGHTLPPKPPSPRGTTASPKGRIRRKEEAKESPSPSGPEDKNHSKSRTAEEKEPAAPASPAPSPVPSPTPAQPQKEQSSTQIPPDTAVPAVPTVPTFPTAPPTAAPSVTPSKPMAGTTDREEATRLLAEKRRQAREQREREEQERKLQAERDKRMREEQLAREAEARAEREAEARRREEQEAREKAQAEQEEQERLQKQKEEAEARSREEAERQRLEREKHFQKEEQERQERRKRLEEIMKRTRKSEAAETKKQDGKETMANNSGPDPVKAVETRPSGLQKDSMQKEELAPQEPQWSLPSKEMPGSLVNGLQPLPAHQENGFPAKGTAGDKSLGRAAEGLLPFAEADAFLKKAVVQPPQVTEVL

[Multiple Choices]
A. microtubule cytoskeleton organization
B. positive regulation of signal transduction
C. protein-containing complex disassembly
D. regulation of root development
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

> The exact supplied sequence matches the rat MAP7 domain-containing protein 1 record. Its archived UniProt annotation assigns microtubule cytoskeleton organization (GO:0000226), and describes a role in microtubule stabilization. This supports A, although the function annotation is transferred by similarity and the GO assignment is ISS, not direct experimental evidence.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is rich in low-complexity regions and coiled-coil-like segments, but those features do not specifically distinguish microtubule cytoskeleton organization from the other listed processes.


**Missing item-specific fact**

> The protein-specific identity and functional annotation that MAP7 domain-containing protein 1 stabilizes microtubules and is associated with microtubule cytoskeleton organization.


**Reason**

> The supplied sequence alone does not provide a sufficiently specific biological basis to select A. The distinguishing function comes from protein-specific annotation or prior knowledge, not a general sequence-level argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, microtubule cytoskeleton organization is supported by the matched protein annotation; the available evidence does not comparably support another listed option.


### Important caveats

- The sequence match is exact, but the author's source snapshot is unknown.
- The function annotation is evidence transferred by similarity (ECO:0000250); the GO annotation is ISS. Neither establishes direct experimental validation for this rat sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is rich in low-complexity regions and coiled-coil-like segments, but those features do not specifically distinguish microtubule cytoskeleton organization from the other listed processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and functional annotation that MAP7 domain-containing protein 1 stabilizes microtubules and is associated with microtubule cytoskeleton organization.",
    "reason": "The supplied sequence alone does not provide a sufficiently specific biological basis to select A. The distinguishing function comes from protein-specific annotation or prior knowledge, not a general sequence-level argument."
  },
  "case_id": "GO_biological_process_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the rat MAP7 domain-containing protein 1 record. Its archived UniProt annotation assigns microtubule cytoskeleton organization (GO:0000226), and describes a role in microtubule stabilization. This supports A, although the function annotation is transferred by similarity and the GO assignment is ISS, not direct experimental evidence."
  },
  "important_caveats": [
    "The sequence match is exact, but the author's source snapshot is unknown.",
    "The function annotation is evidence transferred by similarity (ECO:0000250); the GO annotation is ISS. Neither establishes direct experimental validation for this rat sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, microtubule cytoskeleton organization is supported by the matched protein annotation; the available evidence does not comparably support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the rat MAP7 domain-containing protein 1 record. Its archived UniProt annotation assigns microtubule cytoskeleton organization (GO:0000226), and describes a role in microtubule stabilization. This supports A, although the function annotation is transferred by similarity and the GO assignment is ISS, not direct experimental evidence.",
    "evidence_ids": ["H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is rich in low-complexity regions and coiled-coil-like segments, but those features do not specifically distinguish microtubule cytoskeleton organization from the other listed processes.",
    "missing_item_specific_fact": "The protein-specific identity and functional annotation that MAP7 domain-containing protein 1 stabilizes microtubules and is associated with microtubule cytoskeleton organization.",
    "reason": "The supplied sequence alone does not provide a sufficiently specific biological basis to select A. The distinguishing function comes from protein-specific annotation or prior knowledge, not a general sequence-level argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, microtubule cytoskeleton organization is supported by the matched protein annotation; the available evidence does not comparably support another listed option."
  },
  "important_caveats": [
    "The sequence match is exact, but the author's source snapshot is unknown.",
    "The function annotation is evidence transferred by similarity (ECO:0000250); the GO annotation is ISS. Neither establishes direct experimental validation for this rat sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A8I5ZM56 (MAP7 domain-containing protein 1, Rattus norvegicus) carries GO:0000226 (microtubule cytoskeleton organization) as a Biological Process annotation (evidence type ISS:UniProtKB). The FUNCTION comment explicitly describes it as a 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' that 'facilitate&#91;s&#93; microtubule stabilization through the maintenance of acetylated stable microtubules.' The protein name itself (MAP7 domain-containing) places it in the microtubule-associated protein family. The evidence code is ECO:0000250 (inferred by sequence/structural similarity) and ISS, so this is a transferred/computational annotation rather than direct experimental evidence, but it is the authoritative database annotation and is consistent with the well-characterized MAP7 domain family. Option A is directly supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> There is a weak general reasoning signal: the sequence contains extensive coiled-coil regions (e.g., the heptad-repeat-like stretch 'KAKERREERAKYLAAKKAVWLEKEEKAKALREKQLQERRRRLEEQRLKAEQRRAALEERQRQKLEKNKERYEAAIQRSVKKTWAEIRQQRW' and the C-terminal 'LAERDKRMREEQLAREAEARAEREAEARRREEQEAREKAQAEQEEQERLQKQKEEAEARSREEAERQRLEREKHFQKEEQERQERRKRLEEIMKRTRKSEAA') characteristic of structural/cytoskeletal proteins. This could suggest cytoskeletal involvement broadly. However, coiled coils are ubiquitous across many protein classes and do not specifically point to microtubule organization over other cytoskeletal or signaling functions. Option D (regulation of root development) is trivially eliminable as a plant-specific GO term applied to a rat protein. Distinguishing A from B and C requires recognizing the protein as a member of the MAP7 (microtubule-associated protein 7) domain family, which is an item-specific annotation/family-identification fact not derivable from generic sequence features alone.


**Missing item-specific fact**

> Identification of the protein as a MAP7 domain-containing protein (Map7d1/MTAP7D1) and knowledge that the MAP7 domain family is specifically a microtubule-binding/associated protein family. Without this, the coiled-coil architecture is too generic to uniquely select 'microtubule cytoskeleton organization' over 'positive regulation of signal transduction' or 'protein-containing complex disassembly.'


**Reason**

> The sequence provides only generic structural hints (coiled coils, proline-rich regions, charged stretches) that are consistent with many protein classes. The decisive step—recognizing this as a MAP7-domain microtubule-associated protein—requires either exact sequence/database lookup or memorization of the MAP7 protein family's function. The trivially eliminable distractor (D, a plant term for a rat protein) does not rescue the reasoning path because the remaining three options (A, B, C) cannot be meaningfully distinguished by general biological inference from this sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D is clearly inapplicable (root development is a plant-specific process; this is a rat protein). Options B and C are generic GO terms not specifically associated with this protein's annotated function. Option A is the annotated and functionally coherent answer. While B and C are not obviously contradictory from sequence alone, they lack any positive support, and the MAP7 family's well-established microtubule-binding role makes A the uniquely defensible choice once the protein identity is known.


### Important caveats

- The GO annotation evidence code is ISS (Inferred from Sequence Similarity) and the function comment uses ECO:0000250 (inferred by sequence/structural similarity), meaning the microtubule-stabilizing function is a transferred annotation from the human ortholog (A2AJI0), not direct experimental evidence for the rat protein.
- The UniProt accession was inferred from image-path metadata in the benchmark dataset; this identity was not provided to the evaluated model.
- The protein was first publicly released in UniProt on 2025-04-09; the benchmark's exact construction date and source snapshot are unknown.
- The sequence is 849 AA and matches the canonical UniProt entry exactly (SHA-256 match confirmed across current and historical versions).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "There is a weak general reasoning signal: the sequence contains extensive coiled-coil regions (e.g., the heptad-repeat-like stretch 'KAKERREERAKYLAAKKAVWLEKEEKAKALREKQLQERRRRLEEQRLKAEQRRAALEERQRQKLEKNKERYEAAIQRSVKKTWAEIRQQRW' and the C-terminal 'LAERDKRMREEQLAREAEARAEREAEARRREEQEAREKAQAEQEEQERLQKQKEEAEARSREEAERQRLEREKHFQKEEQERQERRKRLEEIMKRTRKSEAA') characteristic of structural/cytoskeletal proteins. This could suggest cytoskeletal involvement broadly. However, coiled coils are ubiquitous across many protein classes and do not specifically point to microtubule organization over other cytoskeletal or signaling functions. Option D (regulation of root development) is trivially eliminable as a plant-specific GO term applied to a rat protein. Distinguishing A from B and C requires recognizing the protein as a member of the MAP7 (microtubule-associated protein 7) domain family, which is an item-specific annotation/family-identification fact not derivable from generic sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identification of the protein as a MAP7 domain-containing protein (Map7d1/MTAP7D1) and knowledge that the MAP7 domain family is specifically a microtubule-binding/associated protein family. Without this, the coiled-coil architecture is too generic to uniquely select 'microtubule cytoskeleton organization' over 'positive regulation of signal transduction' or 'protein-containing complex disassembly.'",
    "reason": "The sequence provides only generic structural hints (coiled coils, proline-rich regions, charged stretches) that are consistent with many protein classes. The decisive step—recognizing this as a MAP7-domain microtubule-associated protein—requires either exact sequence/database lookup or memorization of the MAP7 protein family's function. The trivially eliminable distractor (D, a plant term for a rat protein) does not rescue the reasoning path because the remaining three options (A, B, C) cannot be meaningfully distinguished by general biological inference from this sequence alone."
  },
  "case_id": "GO_biological_process_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A8I5ZM56 (MAP7 domain-containing protein 1, Rattus norvegicus) carries GO:0000226 (microtubule cytoskeleton organization) as a Biological Process annotation (evidence type ISS:UniProtKB). The FUNCTION comment explicitly describes it as a 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' that 'facilitate[s] microtubule stabilization through the maintenance of acetylated stable microtubules.' The protein name itself (MAP7 domain-containing) places it in the microtubule-associated protein family. The evidence code is ECO:0000250 (inferred by sequence/structural similarity) and ISS, so this is a transferred/computational annotation rather than direct experimental evidence, but it is the authoritative database annotation and is consistent with the well-characterized MAP7 domain family. Option A is directly supported."
  },
  "important_caveats": [
    "The GO annotation evidence code is ISS (Inferred from Sequence Similarity) and the function comment uses ECO:0000250 (inferred by sequence/structural similarity), meaning the microtubule-stabilizing function is a transferred annotation from the human ortholog (A2AJI0), not direct experimental evidence for the rat protein.",
    "The UniProt accession was inferred from image-path metadata in the benchmark dataset; this identity was not provided to the evaluated model.",
    "The protein was first publicly released in UniProt on 2025-04-09; the benchmark's exact construction date and source snapshot are unknown.",
    "The sequence is 849 AA and matches the canonical UniProt entry exactly (SHA-256 match confirmed across current and historical versions)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is clearly inapplicable (root development is a plant-specific process; this is a rat protein). Options B and C are generic GO terms not specifically associated with this protein's annotated function. Option A is the annotated and functionally coherent answer. While B and C are not obviously contradictory from sequence alone, they lack any positive support, and the MAP7 family's well-established microtubule-binding role makes A the uniquely defensible choice once the protein identity is known."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A8I5ZM56 (MAP7 domain-containing protein 1, Rattus norvegicus) carries GO:0000226 (microtubule cytoskeleton organization) as a Biological Process annotation (evidence type ISS:UniProtKB). The FUNCTION comment explicitly describes it as a 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' that 'facilitate[s] microtubule stabilization through the maintenance of acetylated stable microtubules.' The protein name itself (MAP7 domain-containing) places it in the microtubule-associated protein family. The evidence code is ECO:0000250 (inferred by sequence/structural similarity) and ISS, so this is a transferred/computational annotation rather than direct experimental evidence, but it is the authoritative database annotation and is consistent with the well-characterized MAP7 domain family. Option A is directly supported.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "There is a weak general reasoning signal: the sequence contains extensive coiled-coil regions (e.g., the heptad-repeat-like stretch 'KAKERREERAKYLAAKKAVWLEKEEKAKALREKQLQERRRRLEEQRLKAEQRRAALEERQRQKLEKNKERYEAAIQRSVKKTWAEIRQQRW' and the C-terminal 'LAERDKRMREEQLAREAEARAEREAEARRREEQEAREKAQAEQEEQERLQKQKEEAEARSREEAERQRLEREKHFQKEEQERQERRKRLEEIMKRTRKSEAA') characteristic of structural/cytoskeletal proteins. This could suggest cytoskeletal involvement broadly. However, coiled coils are ubiquitous across many protein classes and do not specifically point to microtubule organization over other cytoskeletal or signaling functions. Option D (regulation of root development) is trivially eliminable as a plant-specific GO term applied to a rat protein. Distinguishing A from B and C requires recognizing the protein as a member of the MAP7 (microtubule-associated protein 7) domain family, which is an item-specific annotation/family-identification fact not derivable from generic sequence features alone.",
    "missing_item_specific_fact": "Identification of the protein as a MAP7 domain-containing protein (Map7d1/MTAP7D1) and knowledge that the MAP7 domain family is specifically a microtubule-binding/associated protein family. Without this, the coiled-coil architecture is too generic to uniquely select 'microtubule cytoskeleton organization' over 'positive regulation of signal transduction' or 'protein-containing complex disassembly.'",
    "reason": "The sequence provides only generic structural hints (coiled coils, proline-rich regions, charged stretches) that are consistent with many protein classes. The decisive step—recognizing this as a MAP7-domain microtubule-associated protein—requires either exact sequence/database lookup or memorization of the MAP7 protein family's function. The trivially eliminable distractor (D, a plant term for a rat protein) does not rescue the reasoning path because the remaining three options (A, B, C) cannot be meaningfully distinguished by general biological inference from this sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is clearly inapplicable (root development is a plant-specific process; this is a rat protein). Options B and C are generic GO terms not specifically associated with this protein's annotated function. Option A is the annotated and functionally coherent answer. While B and C are not obviously contradictory from sequence alone, they lack any positive support, and the MAP7 family's well-established microtubule-binding role makes A the uniquely defensible choice once the protein identity is known."
  },
  "important_caveats": [
    "The GO annotation evidence code is ISS (Inferred from Sequence Similarity) and the function comment uses ECO:0000250 (inferred by sequence/structural similarity), meaning the microtubule-stabilizing function is a transferred annotation from the human ortholog (A2AJI0), not direct experimental evidence for the rat protein.",
    "The UniProt accession was inferred from image-path metadata in the benchmark dataset; this identity was not provided to the evaluated model.",
    "The protein was first publicly released in UniProt on 2025-04-09; the benchmark's exact construction date and source snapshot are unknown.",
    "The sequence is 849 AA and matches the canonical UniProt entry exactly (SHA-256 match confirmed across current and historical versions)."
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

**Accession:** `A0A8I5ZM56` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.465249+00:00.  

```json
{"recommendedName":{"fullName":{"value":"MAP7 domain-containing protein 1"}}}
```

Source SHA-256: `1ebde045dc5cd2279bede8623441f3126cf1702b9f410da8cdc64ae95a8cdfc5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.465249+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A2AJI0","source":"UniProtKB"}],"value":"Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth. Facilitate microtubule stabilization through the maintenance of acetylated stable microtubules"}]}
```

Source SHA-256: `1ebde045dc5cd2279bede8623441f3126cf1702b9f410da8cdc64ae95a8cdfc5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I5ZM56.json)  
**Locator:** `/uniProtKBCrossReferences/26`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.465249+00:00.  

```json
{"database":"GO","id":"GO:0000226","properties":[{"key":"GoTerm","value":"P:microtubule cytoskeleton organization"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `1ebde045dc5cd2279bede8623441f3126cf1702b9f410da8cdc64ae95a8cdfc5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I5ZM56?format=txt&versions=18)  
**Locator:** `lines 60-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:59.955320+00:00.  

```text
CC   -!- FUNCTION: Microtubule-stabilizing protein involved in the control of
CC       cell motility and neurite outgrowth. Facilitate microtubule
CC       stabilization through the maintenance of acetylated stable
CC       microtubules. {ECO:0000250|UniProtKB:A2AJI0}.
```

Source SHA-256: `ee69cffcb1959a398f57c781fc9212a6b8142d932b2370924cde96c6cc19a50b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I5ZM56?format=txt&versions=18)  
**Locator:** `lines 103-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:59.955320+00:00.  

```text
DR   GO; GO:0000226; P:microtubule cytoskeleton organization; ISS:UniProtKB.
```

Source SHA-256: `ee69cffcb1959a398f57c781fc9212a6b8142d932b2370924cde96c6cc19a50b`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 2328-2338`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000226
name: microtubule cytoskeleton organization
namespace: biological_process
def: "A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of cytoskeletal structures comprising microtubules and their associated proteins." [GOC:mah]
subset: goslim_pombe
synonym: "microtubule cytoskeleton organisation" EXACT [GOC:mah]
synonym: "microtubule cytoskeleton organization and biogenesis" RELATED [GOC:mah]
is_a: GO:0007010 ! cytoskeleton organization
is_a: GO:0007017 ! microtubule-based process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 47. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
