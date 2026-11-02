# GO_biological_process_0154

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — lysine biosynthetic process via diaminopimelate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSVKKAGVLGATGSVGQRFILLLSKHPEFEIHALGASSRSAGKKYKDAASWKQTETLPETEQDIVVQECKPEGNFLECDVVFSGLDADVAGDIEKSFVEAGLAVVSNAKNYRREKDVPLVVPIVNPEHIDVVENKVKQAVSKGGKKPGFIICISNCSTAGLVAPLKPLVEKFGPIDALTTTTLQAISGAGFSPGVSGMDILDNIVPYISGEEDKLEWETKKILGGVNAEGTEFVPIPESEMKVSAQCNRVPVIDGHTECISLRFANRPAPSVEDVKQCLREYECAASKLGCHSAPKQTIHVLDQPDRPQPRLDRDRDSGYGVSVGRIREDSLLDFKMVVLSHNTIIGAAGAGILIAEILKAKNII

[Multiple Choices]
A. lysine biosynthetic process via diaminopimelate
B. axonal transport of mitochondrion
C. protein destabilization
D. heme biosynthetic process
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

### Expected-answer support: contradicted

> The sequence matches Candida albicans aspartate-semialdehyde dehydrogenase. Its documented role is in aspartate-family amino-acid biosynthesis, including threonine and methionine pathways. Candida is a fungus, whose lysine biosynthesis uses the alpha-aminoadipate route rather than the diaminopimelate route, so choice A is not a scientifically appropriate process for this protein. UniProt does carry A as an IEA UniPathway annotation, but that computational annotation conflicts with the organism's pathway biology and is not experimental evidence for A.

Citations as saved: [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H11](#evidence-h11).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a soluble enzyme, which makes a transport role less plausible, but that does not establish a particular amino-acid biosynthetic pathway or distinguish DAP-dependent lysine synthesis from heme synthesis.


**Missing item-specific fact**

> Identifying the enzyme as aspartate-semialdehyde dehydrogenase and knowing the organism-specific lysine pathway are needed; neither is stated in the prompt. The sequence alone does not justify a DAP-specific lysine-process assignment.


**Reason**

> Selecting a pathway-level GO process requires protein-specific functional identification and biological context. Remembering or looking up the sequence's annotation would supply that fact, but does not count as reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The known role of this enzyme is not represented among the choices. A appears in a UniProt computational annotation, but that annotation does not make the DAP-dependent lysine process biologically appropriate for this fungal protein.


### Important caveats

- The sequence match and organism identity come from reviewer-only evidence, not information supplied to the evaluated model.
- The UniProt lysine annotation is explicitly IEA; the cited functional description supports aspartate-family amino-acid biosynthesis instead.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a soluble enzyme, which makes a transport role less plausible, but that does not establish a particular amino-acid biosynthetic pathway or distinguish DAP-dependent lysine synthesis from heme synthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying the enzyme as aspartate-semialdehyde dehydrogenase and knowing the organism-specific lysine pathway are needed; neither is stated in the prompt. The sequence alone does not justify a DAP-specific lysine-process assignment.",
    "reason": "Selecting a pathway-level GO process requires protein-specific functional identification and biological context. Remembering or looking up the sequence's annotation would supply that fact, but does not count as reasoning from the provided input."
  },
  "case_id": "GO_biological_process_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C3",
      "C4",
      "C5",
      "H7",
      "H8",
      "H9",
      "H11"
    ],
    "judgment": "contradicted",
    "reason": "The sequence matches Candida albicans aspartate-semialdehyde dehydrogenase. Its documented role is in aspartate-family amino-acid biosynthesis, including threonine and methionine pathways. Candida is a fungus, whose lysine biosynthesis uses the alpha-aminoadipate route rather than the diaminopimelate route, so choice A is not a scientifically appropriate process for this protein. UniProt does carry A as an IEA UniPathway annotation, but that computational annotation conflicts with the organism's pathway biology and is not experimental evidence for A."
  },
  "important_caveats": [
    "The sequence match and organism identity come from reviewer-only evidence, not information supplied to the evaluated model.",
    "The UniProt lysine annotation is explicitly IEA; the cited functional description supports aspartate-family amino-acid biosynthesis instead."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The known role of this enzyme is not represented among the choices. A appears in a UniProt computational annotation, but that annotation does not make the DAP-dependent lysine process biologically appropriate for this fungal protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0154",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence matches Candida albicans aspartate-semialdehyde dehydrogenase. Its documented role is in aspartate-family amino-acid biosynthesis, including threonine and methionine pathways. Candida is a fungus, whose lysine biosynthesis uses the alpha-aminoadipate route rather than the diaminopimelate route, so choice A is not a scientifically appropriate process for this protein. UniProt does carry A as an IEA UniPathway annotation, but that computational annotation conflicts with the organism's pathway biology and is not experimental evidence for A.",
    "evidence_ids": ["C3", "C4", "C5", "H7", "H8", "H9", "H11"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a soluble enzyme, which makes a transport role less plausible, but that does not establish a particular amino-acid biosynthetic pathway or distinguish DAP-dependent lysine synthesis from heme synthesis.",
    "missing_item_specific_fact": "Identifying the enzyme as aspartate-semialdehyde dehydrogenase and knowing the organism-specific lysine pathway are needed; neither is stated in the prompt. The sequence alone does not justify a DAP-specific lysine-process assignment.",
    "reason": "Selecting a pathway-level GO process requires protein-specific functional identification and biological context. Remembering or looking up the sequence's annotation would supply that fact, but does not count as reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The known role of this enzyme is not represented among the choices. A appears in a UniProt computational annotation, but that annotation does not make the DAP-dependent lysine process biologically appropriate for this fungal protein."
  },
  "important_caveats": [
    "The sequence match and organism identity come from reviewer-only evidence, not information supplied to the evaluated model.",
    "The UniProt lysine annotation is explicitly IEA; the cited functional description supports aspartate-family amino-acid biosynthesis instead."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q5ALM0, gene HOM2) from Candida albicans. UniProt annotates it with GO:0009089 'lysine biosynthetic process via diaminopimelate' (evidence code IEA:UniProtKB-UniPathway, evidence_id H11). The enzyme catalyzes the NADPH-dependent reductive dephosphorylation of 4-phospho-L-aspartate to L-aspartate-4-semialdehyde, which is a required shared intermediate step in the diaminopimelate (DAP) lysine biosynthetic pathway. The annotation is a computational/pathway-inference annotation (IEA) rather than direct experimental evidence for lysine biosynthesis specifically; the experimental evidence (ECO:0000269, multiple PubMed references) supports the general ASADH function in the aspartate-family amino acid biosynthesis. The protein is also annotated for methionine, threonine, and homoserine biosynthesis. The key is supported by the database annotation and is biochemically valid, though it represents one of several pathway roles.

Citations as saved: [H11](#evidence-h11), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The ~365-residue sequence contains a Rossmann-fold NAD(P)-binding motif (GATGSVGQRFILLLSKHPEFEIHALGASSRSAGKKYKDAASWKQ) and catalytic residues characteristic of an aspartate-semialdehyde dehydrogenase, a small soluble metabolic enzyme. Option B (axonal transport of mitochondrion) requires motor/adaptor proteins (kinesin, dynein, Milton, Miro) with entirely different domain architectures. Option C (protein destabilization) involves ubiquitin ligases, proteases, or degron-recognition systems. Option D (heme biosynthetic process) involves porphyrin-ring-synthesis enzymes (ALA synthase, ferrochelatase, etc.) with distinct folds. None of B, C, or D are compatible with a small NAD(P)-dependent dehydrogenase. Option A (lysine biosynthetic process via diaminopimelate) is the only amino-acid-biosynthesis option and is consistent with the identified enzyme class. General biological reasoning about protein class and pathway membership distinguishes A from the other three.


**Missing item-specific fact**

> To choose specifically 'lysine biosynthetic process via diaminopimelate' over other amino-acid-biosynthesis GO terms (methionine, threonine, homoserine biosynthesis) that also apply to this enzyme, one would need the specific UniProt/GO annotation assignment. However, since no competing amino-acid-biosynthesis option is presented among the four choices, the elimination reasoning is sufficient.


**Reason**

> The sequence clearly identifies a small NAD(P)-dependent dehydrogenase. Three of the four options (axonal transport, protein destabilization, heme biosynthesis) are categorically incompatible with such an enzyme. The remaining option (A) is the only amino-acid-biosynthesis process listed and is biochemically valid for aspartate-semialdehyde dehydrogenase. A knowledgeable biologist can reach A by recognizing the enzyme class and eliminating incompatible processes without needing to recall the specific UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein participates in multiple amino-acid-biosynthetic pathways (methionine, threonine, homoserine, lysine via DAP), only one amino-acid-biosynthesis option (A) is presented. Options B, C, and D are categorically incompatible with a small metabolic dehydrogenase. No ambiguity exists among the supplied choices.


### Important caveats

- The GO:0009089 (lysine via DAP) annotation carries evidence code IEA:UniProtKB-UniPathway (computational/pathway inference), not direct experimental evidence for lysine biosynthesis. Experimental evidence (ECO:0000269) supports the general ASADH catalytic function in the aspartate-family pathway.
- The protein is annotated with multiple amino-acid-biosynthesis GO terms (homoserine, methionine, threonine, lysine via DAP). The UniProt PATHWAY comments explicitly list methionine and threonine biosynthesis but not the DAP lysine pathway as a separate entry; the lysine annotation comes from UniPathway.
- The gene name HOM2 and the pathway comments emphasize homoserine/methionine/threonine biosynthesis, making the choice of lysine via DAP as the 'primary' process a matter of annotation selection rather than a uniquely determined experimental fact.
- The reviewer-only evidence (UniProt accession, GO annotations) was not available to the evaluated model; the model must rely on sequence analysis and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The ~365-residue sequence contains a Rossmann-fold NAD(P)-binding motif (GATGSVGQRFILLLSKHPEFEIHALGASSRSAGKKYKDAASWKQ) and catalytic residues characteristic of an aspartate-semialdehyde dehydrogenase, a small soluble metabolic enzyme. Option B (axonal transport of mitochondrion) requires motor/adaptor proteins (kinesin, dynein, Milton, Miro) with entirely different domain architectures. Option C (protein destabilization) involves ubiquitin ligases, proteases, or degron-recognition systems. Option D (heme biosynthetic process) involves porphyrin-ring-synthesis enzymes (ALA synthase, ferrochelatase, etc.) with distinct folds. None of B, C, or D are compatible with a small NAD(P)-dependent dehydrogenase. Option A (lysine biosynthetic process via diaminopimelate) is the only amino-acid-biosynthesis option and is consistent with the identified enzyme class. General biological reasoning about protein class and pathway membership distinguishes A from the other three.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "To choose specifically 'lysine biosynthetic process via diaminopimelate' over other amino-acid-biosynthesis GO terms (methionine, threonine, homoserine biosynthesis) that also apply to this enzyme, one would need the specific UniProt/GO annotation assignment. However, since no competing amino-acid-biosynthesis option is presented among the four choices, the elimination reasoning is sufficient.",
    "reason": "The sequence clearly identifies a small NAD(P)-dependent dehydrogenase. Three of the four options (axonal transport, protein destabilization, heme biosynthesis) are categorically incompatible with such an enzyme. The remaining option (A) is the only amino-acid-biosynthesis process listed and is biochemically valid for aspartate-semialdehyde dehydrogenase. A knowledgeable biologist can reach A by recognizing the enzyme class and eliminating incompatible processes without needing to recall the specific UniProt annotation."
  },
  "case_id": "GO_biological_process_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "H11",
      "H7",
      "H8",
      "H9",
      "C4",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q5ALM0, gene HOM2) from Candida albicans. UniProt annotates it with GO:0009089 'lysine biosynthetic process via diaminopimelate' (evidence code IEA:UniProtKB-UniPathway, evidence_id H11). The enzyme catalyzes the NADPH-dependent reductive dephosphorylation of 4-phospho-L-aspartate to L-aspartate-4-semialdehyde, which is a required shared intermediate step in the diaminopimelate (DAP) lysine biosynthetic pathway. The annotation is a computational/pathway-inference annotation (IEA) rather than direct experimental evidence for lysine biosynthesis specifically; the experimental evidence (ECO:0000269, multiple PubMed references) supports the general ASADH function in the aspartate-family amino acid biosynthesis. The protein is also annotated for methionine, threonine, and homoserine biosynthesis. The key is supported by the database annotation and is biochemically valid, though it represents one of several pathway roles."
  },
  "important_caveats": [
    "The GO:0009089 (lysine via DAP) annotation carries evidence code IEA:UniProtKB-UniPathway (computational/pathway inference), not direct experimental evidence for lysine biosynthesis. Experimental evidence (ECO:0000269) supports the general ASADH catalytic function in the aspartate-family pathway.",
    "The protein is annotated with multiple amino-acid-biosynthesis GO terms (homoserine, methionine, threonine, lysine via DAP). The UniProt PATHWAY comments explicitly list methionine and threonine biosynthesis but not the DAP lysine pathway as a separate entry; the lysine annotation comes from UniPathway.",
    "The gene name HOM2 and the pathway comments emphasize homoserine/methionine/threonine biosynthesis, making the choice of lysine via DAP as the 'primary' process a matter of annotation selection rather than a uniquely determined experimental fact.",
    "The reviewer-only evidence (UniProt accession, GO annotations) was not available to the evaluated model; the model must rely on sequence analysis and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein participates in multiple amino-acid-biosynthetic pathways (methionine, threonine, homoserine, lysine via DAP), only one amino-acid-biosynthesis option (A) is presented. Options B, C, and D are categorically incompatible with a small metabolic dehydrogenase. No ambiguity exists among the supplied choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0154",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q5ALM0, gene HOM2) from Candida albicans. UniProt annotates it with GO:0009089 'lysine biosynthetic process via diaminopimelate' (evidence code IEA:UniProtKB-UniPathway, evidence_id H11). The enzyme catalyzes the NADPH-dependent reductive dephosphorylation of 4-phospho-L-aspartate to L-aspartate-4-semialdehyde, which is a required shared intermediate step in the diaminopimelate (DAP) lysine biosynthetic pathway. The annotation is a computational/pathway-inference annotation (IEA) rather than direct experimental evidence for lysine biosynthesis specifically; the experimental evidence (ECO:0000269, multiple PubMed references) supports the general ASADH function in the aspartate-family amino acid biosynthesis. The protein is also annotated for methionine, threonine, and homoserine biosynthesis. The key is supported by the database annotation and is biochemically valid, though it represents one of several pathway roles.",
    "evidence_ids": ["H11", "H7", "H8", "H9", "C4", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The ~365-residue sequence contains a Rossmann-fold NAD(P)-binding motif (GATGSVGQRFILLLSKHPEFEIHALGASSRSAGKKYKDAASWKQ) and catalytic residues characteristic of an aspartate-semialdehyde dehydrogenase, a small soluble metabolic enzyme. Option B (axonal transport of mitochondrion) requires motor/adaptor proteins (kinesin, dynein, Milton, Miro) with entirely different domain architectures. Option C (protein destabilization) involves ubiquitin ligases, proteases, or degron-recognition systems. Option D (heme biosynthetic process) involves porphyrin-ring-synthesis enzymes (ALA synthase, ferrochelatase, etc.) with distinct folds. None of B, C, or D are compatible with a small NAD(P)-dependent dehydrogenase. Option A (lysine biosynthetic process via diaminopimelate) is the only amino-acid-biosynthesis option and is consistent with the identified enzyme class. General biological reasoning about protein class and pathway membership distinguishes A from the other three.",
    "missing_item_specific_fact": "To choose specifically 'lysine biosynthetic process via diaminopimelate' over other amino-acid-biosynthesis GO terms (methionine, threonine, homoserine biosynthesis) that also apply to this enzyme, one would need the specific UniProt/GO annotation assignment. However, since no competing amino-acid-biosynthesis option is presented among the four choices, the elimination reasoning is sufficient.",
    "reason": "The sequence clearly identifies a small NAD(P)-dependent dehydrogenase. Three of the four options (axonal transport, protein destabilization, heme biosynthesis) are categorically incompatible with such an enzyme. The remaining option (A) is the only amino-acid-biosynthesis process listed and is biochemically valid for aspartate-semialdehyde dehydrogenase. A knowledgeable biologist can reach A by recognizing the enzyme class and eliminating incompatible processes without needing to recall the specific UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein participates in multiple amino-acid-biosynthetic pathways (methionine, threonine, homoserine, lysine via DAP), only one amino-acid-biosynthesis option (A) is presented. Options B, C, and D are categorically incompatible with a small metabolic dehydrogenase. No ambiguity exists among the supplied choices."
  },
  "important_caveats": [
    "The GO:0009089 (lysine via DAP) annotation carries evidence code IEA:UniProtKB-UniPathway (computational/pathway inference), not direct experimental evidence for lysine biosynthesis. Experimental evidence (ECO:0000269) supports the general ASADH catalytic function in the aspartate-family pathway.",
    "The protein is annotated with multiple amino-acid-biosynthesis GO terms (homoserine, methionine, threonine, lysine via DAP). The UniProt PATHWAY comments explicitly list methionine and threonine biosynthesis but not the DAP lysine pathway as a separate entry; the lysine annotation comes from UniPathway.",
    "The gene name HOM2 and the pathway comments emphasize homoserine/methionine/threonine biosynthesis, making the choice of lysine via DAP as the 'primary' process a matter of annotation selection rather than a uniquely determined experimental fact.",
    "The reviewer-only evidence (UniProt accession, GO annotations) was not available to the evaluated model; the model must rely on sequence analysis and general biological knowledge."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `external_premise_unverified_from_supplied_sources`.

> C3 identifies Candida albicans; C5/H7 describe aspartate-family amino-acid synthesis and H8/H9 methionine/threonine pathways. H11 nevertheless explicitly carries the keyed DAP-lysine term as IEA:UniPathway.

**Remaining uncertainty:** The model claim that this organism uses alpha-aminoadipate rather than DAP for lysine is not established by the supplied excerpts. It was not independently checked against a primary pathway source in this source-only pass.

Evidence checked: [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H11](#evidence-h11).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q5ALM0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 145. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"commonName":"Yeast","evidences":[{"evidenceCode":"ECO:0000312","id":"UP000000559","source":"Proteomes"}],"lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Saccharomycotina","Pichiomycetes","Debaryomycetaceae","Candida/Lodderomyces clade","Candida"],"scientificName":"Candida albicans (strain SC5314 / ATCC MYA-2876)","taxonId":237561}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17419877","source":"PubMed"}],"value":"CaASADH"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20124701","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32383780","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"34469014","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20124701","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32383780","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"34469014","source":"PubMed"}],"value":"Catalyzes the NADPH-dependent formation of L-aspartate 4-semialdehyde (L-ASA) by the reductive dephosphorylation of 4-phospho-L-aspartate (PubMed:20124701, PubMed:29608391, PubMed:32383780, PubMed:34469014). Mediates the second step in the biosynthesis of amino acids that derive from aspartate (the aspartate family of amino acids), including methioinine and threonine, the latter of which is a precursor to isoleucine (PubMed:20124701)"}]}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20124701","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3"}]}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20124701","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5"}]}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 83-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate 4-
CC       semialdehyde (L-ASA) by the reductive dephosphorylation of 4-phospho-L-
CC       aspartate (PubMed:20124701, PubMed:29608391, PubMed:32383780,
CC       PubMed:34469014). Mediates the second step in the biosynthesis of amino
CC       acids that derive from aspartate (the aspartate family of amino acids),
CC       including methioinine and threonine, the latter of which is a precursor
CC       to isoleucine (PubMed:20124701). {ECO:0000269|PubMed:20124701,
CC       ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:32383780,
CC       ECO:0000269|PubMed:34469014}.
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 114-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo
CC       pathway; L-homoserine from L-aspartate: step 2/3.
CC       {ECO:0000269|PubMed:20124701}.
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 117-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine
CC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:20124701}.
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 161-161`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
DR   GO; GO:0009089; P:lysine biosynthetic process via diaminopimelate; IEA:UniProtKB-UniPathway.
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 154. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
