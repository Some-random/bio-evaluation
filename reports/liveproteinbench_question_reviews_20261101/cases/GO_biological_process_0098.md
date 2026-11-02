# GO_biological_process_0098

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — triterpenoid biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MWRLKIAEGGNDPYLYSTNNFVGRQTWEFDSEYGTPEAIKEVEEARQIFYKNRFQVKPCGDLLWRFQFLREKNFKQTIPQVKVGDGEEVTYEAASTTLKRSVNLLTALQADDGHWPAEIAGPQFFLPPLVFCLYITGHLNVVFNVHHREEILRSIYYHQNEDGGWGLHIEGHSTMFCTALNYICLRMLGVGPDEGDDNACPRARKWILDHGSVTHIPSWGKTWLSILGLFDWSGSNPMPPEFWILPTFMPMYPAKMWCYCRMVYMPMSYLYGKRFVGPITPLIKQLREELFSEPFEEIKWKKVRHLCAPEDLYYPHPLIQDLMWDSLYLFTEPLLTRWPFNNLIRQKALQVTMDHIHYEDENSRYITIGCVEKVLCMLACWVEDPNGVCYKKHLARVPDYIWIAEDGLKMQSFGSQQWDCGFAVQALLASNMSLDEIGPALKKGHFFIKESQVKDNPSGDFKSMHRHISKGSWTFSDQDHGWQVSDCTAEGLKCCLILSTMPPEIVGEKMDPERLYDSVNVLLSLQSENGGLSAWEPAGAQAWLELLNPTEFFADIVIEHEYVECTGASIQALVLFKKMYPGHRKKEIENFIAKAAKYLEDTQYPNGSWYGNWGVCFTYGTWFALGGLAAAGKTYANCAAMRKGVEFLLKSQKEDGGWGESYVSCPKKDFVPLEGPSNLTQTAWALMGLIYARQMERDPTPLHQAAKLLINSQLENGDFPQQEITGVFMKNCMLHYPMYRTIYPLWAIAEYRTHVPLRLS

[Multiple Choices]
A. cellular response to nicotine
B. mitophagy
C. triterpenoid biosynthetic process
D. regulation of translation
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

> The exact sequence matches a soapwort beta-amyrin synthase. The cited UniProt annotation reports experimentally supported conversion of oxidosqualene to beta-amyrin in a triterpene-saponin pathway and assigns the GO term triterpenoid biosynthetic process.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated QW motifs and a DCTAE motif characteristic of oxidosqualene cyclases. This enzyme family cyclizes oxidosqualene to triterpenes, supporting choice C over nicotine response, mitophagy, or translation regulation.


**Missing item-specific fact**

> The exact protein identity and experimentally established product are not supplied, so those specifics would require external lookup; they are not necessary to distinguish the broad process from these choices using the sequence motifs.


**Reason**

> A recognizable enzyme-family signature in the supplied sequence provides a concrete biological basis for the triterpenoid-biosynthesis choice, rather than requiring recall of this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence signature and the experimentally supported annotation both point to triterpenoid biosynthesis; the other options describe unrelated processes.


### Important caveats

- The experimental support is reported through the cited UniProt annotation; the primary paper was not independently reviewed here.
- The reviewer-only accession and annotation support the key but were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated QW motifs and a DCTAE motif characteristic of oxidosqualene cyclases. This enzyme family cyclizes oxidosqualene to triterpenes, supporting choice C over nicotine response, mitophagy, or translation regulation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein identity and experimentally established product are not supplied, so those specifics would require external lookup; they are not necessary to distinguish the broad process from these choices using the sequence motifs.",
    "reason": "A recognizable enzyme-family signature in the supplied sequence provides a concrete biological basis for the triterpenoid-biosynthesis choice, rather than requiring recall of this exact protein's database entry."
  },
  "case_id": "GO_biological_process_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H3",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a soapwort beta-amyrin synthase. The cited UniProt annotation reports experimentally supported conversion of oxidosqualene to beta-amyrin in a triterpene-saponin pathway and assigns the GO term triterpenoid biosynthetic process."
  },
  "important_caveats": [
    "The experimental support is reported through the cited UniProt annotation; the primary paper was not independently reviewed here.",
    "The reviewer-only accession and annotation support the key but were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence signature and the experimentally supported annotation both point to triterpenoid biosynthesis; the other options describe unrelated processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a soapwort beta-amyrin synthase. The cited UniProt annotation reports experimentally supported conversion of oxidosqualene to beta-amyrin in a triterpene-saponin pathway and assigns the GO term triterpenoid biosynthetic process.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H3", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated QW motifs and a DCTAE motif characteristic of oxidosqualene cyclases. This enzyme family cyclizes oxidosqualene to triterpenes, supporting choice C over nicotine response, mitophagy, or translation regulation.",
    "missing_item_specific_fact": "The exact protein identity and experimentally established product are not supplied, so those specifics would require external lookup; they are not necessary to distinguish the broad process from these choices using the sequence motifs.",
    "reason": "A recognizable enzyme-family signature in the supplied sequence provides a concrete biological basis for the triterpenoid-biosynthesis choice, rather than requiring recall of this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence signature and the experimentally supported annotation both point to triterpenoid biosynthesis; the other options describe unrelated processes."
  },
  "important_caveats": [
    "The experimental support is reported through the cited UniProt annotation; the primary paper was not independently reviewed here.",
    "The reviewer-only accession and annotation support the key but were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Beta-amyrin synthase 1 (SobAS1, EC 5.4.99.39) from Saponaria officinalis, an oxidosqualene cyclase converting oxidosqualene to beta-amyrin. UniProt annotates GO:0016104 (triterpenoid biosynthetic process) with IDA evidence code from PubMed:39043959 (experimental assay). The pathway annotation reads 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The sequence matches exactly (760 AA, identical SHA256). Beta-amyrin is a triterpenoid, so the GO term assignment is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains well-known conserved catalytic motifs of the oxidosqualene cyclase (OSC) family: the DCTAE motif (visible as 'SDCTAEGLKCCLILSTMPPEIV') and the QW motif ('QQWDCGFAVQALL'). These motifs identify the protein as an OSC, a class of enzymes that cyclize 2,3-oxidosqualene into triterpenoid skeletons. Recognizing these motifs allows inference to triterpenoid biosynthesis. The distractors (nicotine response, mitophagy, regulation of translation) are mechanistically incompatible with a cyclase enzyme involved in secondary metabolism, further narrowing the choice.


**Missing item-specific fact**

> None required beyond general biochemistry knowledge of OSC family motifs and their role in triterpenoid biosynthesis.


**Reason**

> A knowledgeable biochemist can identify conserved DCTAE and QW motifs in the sequence, assign the protein to the oxidosqualene cyclase family, and deduce triterpenoid biosynthesis. This is a concrete sequence-to-function reasoning chain based on shared family signatures, not a lookup of a specific database entry for this exact sequence. The three distractors are categorically incompatible with the identified enzyme class.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (cellular response to nicotine), B (mitophagy), and D (regulation of translation) are mechanistically unrelated to an oxidosqualene cyclase. Only C (triterpenoid biosynthetic process) is consistent with the protein's enzymatic function. No ambiguity exists.


### Important caveats

- The GO annotation carries IDA (Inferred by Direct Assay) evidence from PubMed:39043959, an experimental 2025 paper, so the key is experimentally grounded, not merely computational.
- The UniProt entry was first public on 2025-06-18; the benchmark's exact construction date is unknown, but the sequence has been stable since 2024-11-27.
- Motif recognition (DCTAE, QW) requires specialized biochemistry knowledge of the OSC superfamily; this is legitimate domain reasoning but not trivial general biology.
- The reviewer-only accession and metadata were absent from the evaluated model input; the model must work from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains well-known conserved catalytic motifs of the oxidosqualene cyclase (OSC) family: the DCTAE motif (visible as 'SDCTAEGLKCCLILSTMPPEIV') and the QW motif ('QQWDCGFAVQALL'). These motifs identify the protein as an OSC, a class of enzymes that cyclize 2,3-oxidosqualene into triterpenoid skeletons. Recognizing these motifs allows inference to triterpenoid biosynthesis. The distractors (nicotine response, mitophagy, regulation of translation) are mechanistically incompatible with a cyclase enzyme involved in secondary metabolism, further narrowing the choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required beyond general biochemistry knowledge of OSC family motifs and their role in triterpenoid biosynthesis.",
    "reason": "A knowledgeable biochemist can identify conserved DCTAE and QW motifs in the sequence, assign the protein to the oxidosqualene cyclase family, and deduce triterpenoid biosynthesis. This is a concrete sequence-to-function reasoning chain based on shared family signatures, not a lookup of a specific database entry for this exact sequence. The three distractors are categorically incompatible with the identified enzyme class."
  },
  "case_id": "GO_biological_process_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The protein is Beta-amyrin synthase 1 (SobAS1, EC 5.4.99.39) from Saponaria officinalis, an oxidosqualene cyclase converting oxidosqualene to beta-amyrin. UniProt annotates GO:0016104 (triterpenoid biosynthetic process) with IDA evidence code from PubMed:39043959 (experimental assay). The pathway annotation reads 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The sequence matches exactly (760 AA, identical SHA256). Beta-amyrin is a triterpenoid, so the GO term assignment is directly and experimentally supported."
  },
  "important_caveats": [
    "The GO annotation carries IDA (Inferred by Direct Assay) evidence from PubMed:39043959, an experimental 2025 paper, so the key is experimentally grounded, not merely computational.",
    "The UniProt entry was first public on 2025-06-18; the benchmark's exact construction date is unknown, but the sequence has been stable since 2024-11-27.",
    "Motif recognition (DCTAE, QW) requires specialized biochemistry knowledge of the OSC superfamily; this is legitimate domain reasoning but not trivial general biology.",
    "The reviewer-only accession and metadata were absent from the evaluated model input; the model must work from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (cellular response to nicotine), B (mitophagy), and D (regulation of translation) are mechanistically unrelated to an oxidosqualene cyclase. Only C (triterpenoid biosynthetic process) is consistent with the protein's enzymatic function. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Beta-amyrin synthase 1 (SobAS1, EC 5.4.99.39) from Saponaria officinalis, an oxidosqualene cyclase converting oxidosqualene to beta-amyrin. UniProt annotates GO:0016104 (triterpenoid biosynthetic process) with IDA evidence code from PubMed:39043959 (experimental assay). The pathway annotation reads 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The sequence matches exactly (760 AA, identical SHA256). Beta-amyrin is a triterpenoid, so the GO term assignment is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains well-known conserved catalytic motifs of the oxidosqualene cyclase (OSC) family: the DCTAE motif (visible as 'SDCTAEGLKCCLILSTMPPEIV') and the QW motif ('QQWDCGFAVQALL'). These motifs identify the protein as an OSC, a class of enzymes that cyclize 2,3-oxidosqualene into triterpenoid skeletons. Recognizing these motifs allows inference to triterpenoid biosynthesis. The distractors (nicotine response, mitophagy, regulation of translation) are mechanistically incompatible with a cyclase enzyme involved in secondary metabolism, further narrowing the choice.",
    "missing_item_specific_fact": "None required beyond general biochemistry knowledge of OSC family motifs and their role in triterpenoid biosynthesis.",
    "reason": "A knowledgeable biochemist can identify conserved DCTAE and QW motifs in the sequence, assign the protein to the oxidosqualene cyclase family, and deduce triterpenoid biosynthesis. This is a concrete sequence-to-function reasoning chain based on shared family signatures, not a lookup of a specific database entry for this exact sequence. The three distractors are categorically incompatible with the identified enzyme class."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (cellular response to nicotine), B (mitophagy), and D (regulation of translation) are mechanistically unrelated to an oxidosqualene cyclase. Only C (triterpenoid biosynthetic process) is consistent with the protein's enzymatic function. No ambiguity exists."
  },
  "important_caveats": [
    "The GO annotation carries IDA (Inferred by Direct Assay) evidence from PubMed:39043959, an experimental 2025 paper, so the key is experimentally grounded, not merely computational.",
    "The UniProt entry was first public on 2025-06-18; the benchmark's exact construction date is unknown, but the sequence has been stable since 2024-11-27.",
    "Motif recognition (DCTAE, QW) requires specialized biochemistry knowledge of the OSC superfamily; this is legitimate domain reasoning but not trivial general biology.",
    "The reviewer-only accession and metadata were absent from the evaluated model input; the model must work from the raw sequence alone."
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

**Accession:** `A0AAW1L0L7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
"A0AAW1L0L7"
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"5.4.99.39"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"Beta-amyrin synthase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SobAS1"}]}}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). Oxidosqualene cyclase mediating the conversion of oxidosqualene to beta-amyrin, generating five rings and eight asymmetric centers in a single transformation (PubMed:39043959)"}]}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39043959","source":"PubMed"}],"id":"GO:0016104","properties":[{"key":"GoTerm","value":"P:triterpenoid biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:41.045167+00:00.  

```text
CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.
CC       saponarioside A and saponarioside B) biosynthetic pathway, leading to
CC       the production of natural products with detergent properties used as
CC       traditional sources of soap (PubMed:39043959). Oxidosqualene cyclase
CC       mediating the conversion of oxidosqualene to beta-amyrin, generating
CC       five rings and eight asymmetric centers in a single transformation
CC       (PubMed:39043959). {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)  
**Locator:** `lines 47-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:41.045167+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)  
**Locator:** `lines 72-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:41.045167+00:00.  

```text
DR   GO; GO:0016104; P:triterpenoid biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 98. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
