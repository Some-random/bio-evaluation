# GO_biological_process_0043

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — threonine biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASYPKKKCGVLGATGSVGQRFILLLADHPFLELHAIGASNRSAGKKYKDAVRWKQTTAMSERLSNLVLRDCRADQFSDCDLVFSGLNSDVAGEIEMEFIKAEIPVFSNAKNYRKHPLVPLVVPTVNPQHLDLIPHQRKEFGLKKGFLVCNSNCAVIGVVIPFAALQAKFGPVEEVEVFTEQAVSGAGYPGVPSMDIMDNVIPYISGEEDKLENEAQKILGSLNADATAFDEQKGLTVGATCTRVGVTDGHMAFVSLRFKNRPGPSAEEVKQAMREYQSEAQKLGCPSAPREAIKVFDEPDRPQPRLDRDISKGYTVSVGRVREAAPGSYFDLRFAALSHNTVIGAAGSSILNAEVAVIKGYI

[Multiple Choices]
A. chitin metabolic process
B. cobalt ion transport
C. threonine biosynthetic process
D. killing of cells of another organism
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

> The supplied sequence exactly matches the cited 363-aa protein. Its annotation identifies it as aspartate-semialdehyde dehydrogenase, and the record assigns threonine biosynthesis with IDA evidence; the cited function places the enzyme in the aspartate-family amino-acid pathway, including threonine.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C10](#evidence-c10), [H4](#evidence-h4), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe very different processes, but the sequence alone does not provide a general biological argument identifying threonine biosynthesis as this protein’s role.


**Missing item-specific fact**

> The protein-specific identification as aspartate-semialdehyde dehydrogenase and the fact that its reaction contributes to threonine biosynthesis.


**Reason**

> Selecting C depends on knowing or establishing this sequence’s enzyme identity and pathway role—an item-specific fact not supplied in the question. Recognizing the sequence from an external record would be lookup or memorization, not reasoning from the provided context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotation also links this enzyme to methionine and homoserine biosynthesis, but those processes are not among the choices; threonine biosynthesis is the only listed option supported by the sequence’s protein-specific function.


### Important caveats

- The functional and GO annotations are reviewer-only evidence and were not supplied to the evaluated model.
- The record’s threonine-biosynthesis GO annotation is marked IDA; the cited functional annotation also reports a role in multiple aspartate-family amino-acid pathways.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe very different processes, but the sequence alone does not provide a general biological argument identifying threonine biosynthesis as this protein’s role.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as aspartate-semialdehyde dehydrogenase and the fact that its reaction contributes to threonine biosynthesis.",
    "reason": "Selecting C depends on knowing or establishing this sequence’s enzyme identity and pathway role—an item-specific fact not supplied in the question. Recognizing the sequence from an external record would be lookup or memorization, not reasoning from the provided context."
  },
  "case_id": "GO_biological_process_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C10",
      "H4",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited 363-aa protein. Its annotation identifies it as aspartate-semialdehyde dehydrogenase, and the record assigns threonine biosynthesis with IDA evidence; the cited function places the enzyme in the aspartate-family amino-acid pathway, including threonine."
  },
  "important_caveats": [
    "The functional and GO annotations are reviewer-only evidence and were not supplied to the evaluated model.",
    "The record’s threonine-biosynthesis GO annotation is marked IDA; the cited functional annotation also reports a role in multiple aspartate-family amino-acid pathways."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation also links this enzyme to methionine and homoserine biosynthesis, but those processes are not among the choices; threonine biosynthesis is the only listed option supported by the sequence’s protein-specific function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited 363-aa protein. Its annotation identifies it as aspartate-semialdehyde dehydrogenase, and the record assigns threonine biosynthesis with IDA evidence; the cited function places the enzyme in the aspartate-family amino-acid pathway, including threonine.",
    "evidence_ids": ["C1", "C4", "C5", "C10", "H4", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe very different processes, but the sequence alone does not provide a general biological argument identifying threonine biosynthesis as this protein’s role.",
    "missing_item_specific_fact": "The protein-specific identification as aspartate-semialdehyde dehydrogenase and the fact that its reaction contributes to threonine biosynthesis.",
    "reason": "Selecting C depends on knowing or establishing this sequence’s enzyme identity and pathway role—an item-specific fact not supplied in the question. Recognizing the sequence from an external record would be lookup or memorization, not reasoning from the provided context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation also links this enzyme to methionine and homoserine biosynthesis, but those processes are not among the choices; threonine biosynthesis is the only listed option supported by the sequence’s protein-specific function."
  },
  "important_caveats": [
    "The functional and GO annotations are reviewer-only evidence and were not supplied to the evaluated model.",
    "The record’s threonine-biosynthesis GO annotation is marked IDA; the cited functional annotation also reports a role in multiple aspartate-family amino-acid pathways."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q4WWR8) from Aspergillus fumigatus. UniProt annotates GO:0009088 'L-threonine biosynthetic process' with IDA evidence (Inferred from Direct Assay, PubMed:28045392, a crystallographic/functional study). The PATHWAY comment explicitly states 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The FUNCTION comment confirms it mediates the second step in biosynthesis of aspartate-family amino acids including threonine. The sequence matches the benchmark input exactly (SHA-256 confirmed). The expected answer C is well-supported by experimental (IDA) annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C10](#evidence-c10), [H4](#evidence-h4), [H6](#evidence-h6), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD(P)H-binding motif (GVLGATGSVGQRFILL) and is ~363 aa, consistent with a monomeric NAD(P)-dependent dehydrogenase. Dehydrogenases are not glycosidases (eliminates chitin metabolic process, A), not membrane transporters (eliminates cobalt ion transport, B), and not effectors of cell killing (eliminates D). Dehydrogenases are ubiquitous in amino acid biosynthesis pathways, particularly the aspartate pathway (aspartate → aspartyl-phosphate → aspartate-semialdehyde → homoserine → threonine/methionine), which is a standard undergraduate biochemistry pathway. Among the four options, only C (threonine biosynthetic process) is consistent with a small-molecule NAD(P)-dependent dehydrogenase functioning in a biosynthetic pathway.


**Missing item-specific fact**

> The specific assignment to 'threonine' rather than 'methionine' biosynthesis (the protein is also step 2/3 in methionine biosynthesis) requires knowing the full aspartate pathway topology. However, since methionine biosynthesis is not among the options, this does not impede selection among the given choices.


**Reason**

> A model can reason from the Rossmann-fold dehydrogenase signature to eliminate transport, polysaccharide metabolism, and cell-killing options, then select the amino acid biosynthesis option. The specific 'threonine' label aligns with well-known aspartate-pathway biochemistry. The distractors are functionally distant enough that general enzyme-class reasoning suffices to distinguish the answer without memorizing this particular protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four options, only C (threonine biosynthetic process) is consistent with an NAD(P)-dependent dehydrogenase. Chitin metabolism requires glycosidases, cobalt transport requires membrane transporters, and cell killing involves immune/defense effectors. No other option is a viable alternative for this enzyme class.


### Important caveats

- The protein is equally annotated in methionine biosynthesis (step 2/3 of L-homoserine from L-aspartate, GO:0071266). The question's framing as 'primary biological process' is somewhat imprecise since the enzyme serves both branches, but methionine biosynthesis is not among the choices.
- The GO:0009088 annotation carries IDA evidence code (Inferred from Direct Assay via PubMed:28045392, a crystallographic study), which is the strongest experimental evidence type, lending high confidence to the annotation.
- The sequence was matched exactly to UniProt Q4WWR8 (entry version 118/120, sequence version 1), confirming the annotation applies to the benchmark input.
- The ontology term for option C (GO:0009088) was not found in the supplied ontology excerpts (term_ids list is empty for option C), but this is a retrieval artifact of the reviewer-only evidence; the term exists in GO and is annotated to this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)H-binding motif (GVLGATGSVGQRFILL) and is ~363 aa, consistent with a monomeric NAD(P)-dependent dehydrogenase. Dehydrogenases are not glycosidases (eliminates chitin metabolic process, A), not membrane transporters (eliminates cobalt ion transport, B), and not effectors of cell killing (eliminates D). Dehydrogenases are ubiquitous in amino acid biosynthesis pathways, particularly the aspartate pathway (aspartate → aspartyl-phosphate → aspartate-semialdehyde → homoserine → threonine/methionine), which is a standard undergraduate biochemistry pathway. Among the four options, only C (threonine biosynthetic process) is consistent with a small-molecule NAD(P)-dependent dehydrogenase functioning in a biosynthetic pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific assignment to 'threonine' rather than 'methionine' biosynthesis (the protein is also step 2/3 in methionine biosynthesis) requires knowing the full aspartate pathway topology. However, since methionine biosynthesis is not among the options, this does not impede selection among the given choices.",
    "reason": "A model can reason from the Rossmann-fold dehydrogenase signature to eliminate transport, polysaccharide metabolism, and cell-killing options, then select the amino acid biosynthesis option. The specific 'threonine' label aligns with well-known aspartate-pathway biochemistry. The distractors are functionally distant enough that general enzyme-class reasoning suffices to distinguish the answer without memorizing this particular protein's annotation."
  },
  "case_id": "GO_biological_process_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C10",
      "H4",
      "H6",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q4WWR8) from Aspergillus fumigatus. UniProt annotates GO:0009088 'L-threonine biosynthetic process' with IDA evidence (Inferred from Direct Assay, PubMed:28045392, a crystallographic/functional study). The PATHWAY comment explicitly states 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The FUNCTION comment confirms it mediates the second step in biosynthesis of aspartate-family amino acids including threonine. The sequence matches the benchmark input exactly (SHA-256 confirmed). The expected answer C is well-supported by experimental (IDA) annotation."
  },
  "important_caveats": [
    "The protein is equally annotated in methionine biosynthesis (step 2/3 of L-homoserine from L-aspartate, GO:0071266). The question's framing as 'primary biological process' is somewhat imprecise since the enzyme serves both branches, but methionine biosynthesis is not among the choices.",
    "The GO:0009088 annotation carries IDA evidence code (Inferred from Direct Assay via PubMed:28045392, a crystallographic study), which is the strongest experimental evidence type, lending high confidence to the annotation.",
    "The sequence was matched exactly to UniProt Q4WWR8 (entry version 118/120, sequence version 1), confirming the annotation applies to the benchmark input.",
    "The ontology term for option C (GO:0009088) was not found in the supplied ontology excerpts (term_ids list is empty for option C), but this is a retrieval artifact of the reviewer-only evidence; the term exists in GO and is annotated to this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, only C (threonine biosynthetic process) is consistent with an NAD(P)-dependent dehydrogenase. Chitin metabolism requires glycosidases, cobalt transport requires membrane transporters, and cell killing involves immune/defense effectors. No other option is a viable alternative for this enzyme class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q4WWR8) from Aspergillus fumigatus. UniProt annotates GO:0009088 'L-threonine biosynthetic process' with IDA evidence (Inferred from Direct Assay, PubMed:28045392, a crystallographic/functional study). The PATHWAY comment explicitly states 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The FUNCTION comment confirms it mediates the second step in biosynthesis of aspartate-family amino acids including threonine. The sequence matches the benchmark input exactly (SHA-256 confirmed). The expected answer C is well-supported by experimental (IDA) annotation.",
    "evidence_ids": ["C4", "C5", "C7", "C10", "H4", "H6", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)H-binding motif (GVLGATGSVGQRFILL) and is ~363 aa, consistent with a monomeric NAD(P)-dependent dehydrogenase. Dehydrogenases are not glycosidases (eliminates chitin metabolic process, A), not membrane transporters (eliminates cobalt ion transport, B), and not effectors of cell killing (eliminates D). Dehydrogenases are ubiquitous in amino acid biosynthesis pathways, particularly the aspartate pathway (aspartate → aspartyl-phosphate → aspartate-semialdehyde → homoserine → threonine/methionine), which is a standard undergraduate biochemistry pathway. Among the four options, only C (threonine biosynthetic process) is consistent with a small-molecule NAD(P)-dependent dehydrogenase functioning in a biosynthetic pathway.",
    "missing_item_specific_fact": "The specific assignment to 'threonine' rather than 'methionine' biosynthesis (the protein is also step 2/3 in methionine biosynthesis) requires knowing the full aspartate pathway topology. However, since methionine biosynthesis is not among the options, this does not impede selection among the given choices.",
    "reason": "A model can reason from the Rossmann-fold dehydrogenase signature to eliminate transport, polysaccharide metabolism, and cell-killing options, then select the amino acid biosynthesis option. The specific 'threonine' label aligns with well-known aspartate-pathway biochemistry. The distractors are functionally distant enough that general enzyme-class reasoning suffices to distinguish the answer without memorizing this particular protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, only C (threonine biosynthetic process) is consistent with an NAD(P)-dependent dehydrogenase. Chitin metabolism requires glycosidases, cobalt transport requires membrane transporters, and cell killing involves immune/defense effectors. No other option is a viable alternative for this enzyme class."
  },
  "important_caveats": [
    "The protein is equally annotated in methionine biosynthesis (step 2/3 of L-homoserine from L-aspartate, GO:0071266). The question's framing as 'primary biological process' is somewhat imprecise since the enzyme serves both branches, but methionine biosynthesis is not among the choices.",
    "The GO:0009088 annotation carries IDA evidence code (Inferred from Direct Assay via PubMed:28045392, a crystallographic study), which is the strongest experimental evidence type, lending high confidence to the annotation.",
    "The sequence was matched exactly to UniProt Q4WWR8 (entry version 118/120, sequence version 1), confirming the annotation applies to the benchmark input.",
    "The ontology term for option C (GO:0009088) was not found in the supplied ontology excerpts (term_ids list is empty for option C), but this is a retrieval artifact of the reviewer-only evidence; the term exists in GO and is annotated to this protein."
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

**Accession:** `Q4WWR8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 118. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
"Q4WWR8"
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28045392","source":"PubMed"}],"value":"AfASADH"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28045392","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28045392","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"value":"Catalyzes the NADPH-dependent formation of L-aspartate 4-semialdehyde (L-ASA) by the reductive dephosphorylation of 4-phospho-L-aspartate (PubMed:28045392, PubMed:29608391). Mediates the second step in the biosynthesis of amino acids that derive from aspartate (the aspartate family of amino acids), including methioinine and threonine, the latter of which is a precursor to isoleucine (PubMed:28045392)"}]}
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28045392","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5"}]}
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/uniProtKBCrossReferences/29`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"28045392","source":"PubMed"}],"id":"GO:0009088","properties":[{"key":"GoTerm","value":"P:L-threonine biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)  
**Locator:** `lines 65-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-02T04:31:00.563757+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate 4-
CC       semialdehyde (L-ASA) by the reductive dephosphorylation of 4-phospho-L-
CC       aspartate (PubMed:28045392, PubMed:29608391). Mediates the second step
CC       in the biosynthesis of amino acids that derive from aspartate (the
CC       aspartate family of amino acids), including methioinine and threonine,
CC       the latter of which is a precursor to isoleucine (PubMed:28045392).
CC       {ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391}.
```

Source SHA-256: `048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)  
**Locator:** `lines 95-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-02T04:31:00.563757+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine
CC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:28045392}.
```

Source SHA-256: `048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)  
**Locator:** `lines 137-137`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-02T04:31:00.563757+00:00.  

```text
DR   GO; GO:0009088; P:threonine biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
