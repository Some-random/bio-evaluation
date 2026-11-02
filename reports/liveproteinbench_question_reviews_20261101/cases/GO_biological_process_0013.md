# GO_biological_process_0013

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — translation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIMLKTQRRIAAELLKCGENRIWIDPERIEDVAAAITREDIKRLIHDGVIKKKPIKGQSRARARAFQEARKKGRHRGPGSKKGKKTARMGKKEVWMMTIRALRKELRKLKAEGKLDAHTYRRLYIRAKGGQFKNKRQLYMFMQEHGILKE

[Multiple Choices]
A. translation
B. positive regulation of DNA replication
C. dTDP biosynthetic process
D. negative regulation of cellular response to oxidative stress
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

> The exact sequence matches UniProt entry Q5JJG6, annotated as large ribosomal subunit protein eL19, with a 23S rRNA-binding function and a GO annotation to translation. This supports A, although the cited functional and GO annotations are computational rather than experimental.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compact and rich in basic residues, which is broadly consistent with a nucleic-acid-binding protein and makes translation a plausible choice over the metabolic-enzyme option. That composition alone does not establish ribosomal identity or distinguish ribosome binding from other nucleic-acid-related roles.


**Missing item-specific fact**

> The sequence’s identity as archaeal large ribosomal subunit protein eL19, including its association with 23S rRNA, is needed to specifically select translation.


**Reason**

> The input supplies no organism, protein-family annotation, or ribosome context. The broad sequence-composition clue is not sufficiently specific to identify the biological process; selecting A depends on the protein-specific identity or annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports translation for the matched sequence; no other listed option is supported by that evidence.


### Important caveats

- The sequence match is documented for both current and historical UniProt records, but the author’s exact source snapshot is unknown.
- The cited UniProt function and GO translation annotation use HAMAP/UniRule computational evidence; they are not direct experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compact and rich in basic residues, which is broadly consistent with a nucleic-acid-binding protein and makes translation a plausible choice over the metabolic-enzyme option. That composition alone does not establish ribosomal identity or distinguish ribosome binding from other nucleic-acid-related roles.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence’s identity as archaeal large ribosomal subunit protein eL19, including its association with 23S rRNA, is needed to specifically select translation.",
    "reason": "The input supplies no organism, protein-family annotation, or ribosome context. The broad sequence-composition clue is not sufficiently specific to identify the biological process; selecting A depends on the protein-specific identity or annotation."
  },
  "case_id": "GO_biological_process_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q5JJG6, annotated as large ribosomal subunit protein eL19, with a 23S rRNA-binding function and a GO annotation to translation. This supports A, although the cited functional and GO annotations are computational rather than experimental."
  },
  "important_caveats": [
    "The sequence match is documented for both current and historical UniProt records, but the author’s exact source snapshot is unknown.",
    "The cited UniProt function and GO translation annotation use HAMAP/UniRule computational evidence; they are not direct experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports translation for the matched sequence; no other listed option is supported by that evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q5JJG6, annotated as large ribosomal subunit protein eL19, with a 23S rRNA-binding function and a GO annotation to translation. This supports A, although the cited functional and GO annotations are computational rather than experimental.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compact and rich in basic residues, which is broadly consistent with a nucleic-acid-binding protein and makes translation a plausible choice over the metabolic-enzyme option. That composition alone does not establish ribosomal identity or distinguish ribosome binding from other nucleic-acid-related roles.",
    "missing_item_specific_fact": "The sequence’s identity as archaeal large ribosomal subunit protein eL19, including its association with 23S rRNA, is needed to specifically select translation.",
    "reason": "The input supplies no organism, protein-family annotation, or ribosome context. The broad sequence-composition clue is not sufficiently specific to identify the biological process; selecting A depends on the protein-specific identity or annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports translation for the matched sequence; no other listed option is supported by that evidence."
  },
  "important_caveats": [
    "The sequence match is documented for both current and historical UniProt records, but the author’s exact source snapshot is unknown.",
    "The cited UniProt function and GO translation annotation use HAMAP/UniRule computational evidence; they are not direct experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5JJG6 annotates this protein as 'Large ribosomal subunit protein eL19' from Thermococcus kodakarensis, with the function 'Binds to the 23S rRNA' and GO:0006412 (translation). The evidence code is IEA:UniProtKB-UniRule (computational/HAMAP-Rule), not experimental. However, the biological reasoning is sound: ribosomal proteins are core structural components of the ribosome, whose primary biological process is translation. The sequence matches the benchmark input exactly (SHA-256 confirmed). The annotation is computational but well-established for ribosomal proteins.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 150-aa sequence exhibits extreme basic-residue enrichment (numerous clustered Lys/Arg stretches: KKK, ARARAR, ARKK, GRHRG, SKKGKKT, RRLYIRAK), a hallmark of ribosomal proteins that electrostatically interact with negatively charged rRNA. The small size and absence of any recognizable enzymatic catalytic motifs (ruling out C: dTDP biosynthetic enzyme), absence of kinase/cyclin/signaling domains (ruling out B: DNA replication regulation), and absence of redox-sensing or transcription-factor motifs (ruling out D: oxidative stress regulation) collectively point toward a ribosomal protein whose primary biological process is translation. This is general structural biology knowledge about ribosomal protein composition.


**Missing item-specific fact**

> None critical. The extreme basicity and small size are sufficient general indicators of a ribosomal protein; one need not know the specific eL19 identity to infer 'translation' over the other three unrelated processes.


**Reason**

> The sequence composition (small, highly basic, no enzymatic or regulatory domains) provides concrete structural-biological grounds to favor 'translation' over the three distractors, which require entirely different protein architectures (enzymes, signaling regulators, stress-response factors).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span completely unrelated biological processes (translation, DNA replication regulation, nucleotide biosynthesis, oxidative stress regulation). The sequence features clearly favor a ribosomal protein and thus translation; none of the distractors are plausible given the observed composition.


### Important caveats

- The UniProt GO annotation carries evidence code IEA (Inferred from Electronic Annotation) via UniRule/HAMAP, not direct experimental evidence. However, ribosomal protein identity and role in translation are extremely well-established.
- The accession Q5JJG6 was inferred reviewer-only from dataset metadata; the evaluated model received only the raw sequence and choices.
- The HAMAP rule annotation (MF_01475) is a computational profile match, not a crystallographic or biochemical experiment, but the biological conclusion (ribosomal protein → translation) is robust.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 150-aa sequence exhibits extreme basic-residue enrichment (numerous clustered Lys/Arg stretches: KKK, ARARAR, ARKK, GRHRG, SKKGKKT, RRLYIRAK), a hallmark of ribosomal proteins that electrostatically interact with negatively charged rRNA. The small size and absence of any recognizable enzymatic catalytic motifs (ruling out C: dTDP biosynthetic enzyme), absence of kinase/cyclin/signaling domains (ruling out B: DNA replication regulation), and absence of redox-sensing or transcription-factor motifs (ruling out D: oxidative stress regulation) collectively point toward a ribosomal protein whose primary biological process is translation. This is general structural biology knowledge about ribosomal protein composition.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The extreme basicity and small size are sufficient general indicators of a ribosomal protein; one need not know the specific eL19 identity to infer 'translation' over the other three unrelated processes.",
    "reason": "The sequence composition (small, highly basic, no enzymatic or regulatory domains) provides concrete structural-biological grounds to favor 'translation' over the three distractors, which require entirely different protein architectures (enzymes, signaling regulators, stress-response factors)."
  },
  "case_id": "GO_biological_process_0013",
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
    "reason": "The UniProt entry Q5JJG6 annotates this protein as 'Large ribosomal subunit protein eL19' from Thermococcus kodakarensis, with the function 'Binds to the 23S rRNA' and GO:0006412 (translation). The evidence code is IEA:UniProtKB-UniRule (computational/HAMAP-Rule), not experimental. However, the biological reasoning is sound: ribosomal proteins are core structural components of the ribosome, whose primary biological process is translation. The sequence matches the benchmark input exactly (SHA-256 confirmed). The annotation is computational but well-established for ribosomal proteins."
  },
  "important_caveats": [
    "The UniProt GO annotation carries evidence code IEA (Inferred from Electronic Annotation) via UniRule/HAMAP, not direct experimental evidence. However, ribosomal protein identity and role in translation are extremely well-established.",
    "The accession Q5JJG6 was inferred reviewer-only from dataset metadata; the evaluated model received only the raw sequence and choices.",
    "The HAMAP rule annotation (MF_01475) is a computational profile match, not a crystallographic or biochemical experiment, but the biological conclusion (ribosomal protein → translation) is robust."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span completely unrelated biological processes (translation, DNA replication regulation, nucleotide biosynthesis, oxidative stress regulation). The sequence features clearly favor a ribosomal protein and thus translation; none of the distractors are plausible given the observed composition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5JJG6 annotates this protein as 'Large ribosomal subunit protein eL19' from Thermococcus kodakarensis, with the function 'Binds to the 23S rRNA' and GO:0006412 (translation). The evidence code is IEA:UniProtKB-UniRule (computational/HAMAP-Rule), not experimental. However, the biological reasoning is sound: ribosomal proteins are core structural components of the ribosome, whose primary biological process is translation. The sequence matches the benchmark input exactly (SHA-256 confirmed). The annotation is computational but well-established for ribosomal proteins.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 150-aa sequence exhibits extreme basic-residue enrichment (numerous clustered Lys/Arg stretches: KKK, ARARAR, ARKK, GRHRG, SKKGKKT, RRLYIRAK), a hallmark of ribosomal proteins that electrostatically interact with negatively charged rRNA. The small size and absence of any recognizable enzymatic catalytic motifs (ruling out C: dTDP biosynthetic enzyme), absence of kinase/cyclin/signaling domains (ruling out B: DNA replication regulation), and absence of redox-sensing or transcription-factor motifs (ruling out D: oxidative stress regulation) collectively point toward a ribosomal protein whose primary biological process is translation. This is general structural biology knowledge about ribosomal protein composition.",
    "missing_item_specific_fact": "None critical. The extreme basicity and small size are sufficient general indicators of a ribosomal protein; one need not know the specific eL19 identity to infer 'translation' over the other three unrelated processes.",
    "reason": "The sequence composition (small, highly basic, no enzymatic or regulatory domains) provides concrete structural-biological grounds to favor 'translation' over the three distractors, which require entirely different protein architectures (enzymes, signaling regulators, stress-response factors)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span completely unrelated biological processes (translation, DNA replication regulation, nucleotide biosynthesis, oxidative stress regulation). The sequence features clearly favor a ribosomal protein and thus translation; none of the distractors are plausible given the observed composition."
  },
  "important_caveats": [
    "The UniProt GO annotation carries evidence code IEA (Inferred from Electronic Annotation) via UniRule/HAMAP, not direct experimental evidence. However, ribosomal protein identity and role in translation are extremely well-established.",
    "The accession Q5JJG6 was inferred reviewer-only from dataset metadata; the evaluated model received only the raw sequence and choices.",
    "The HAMAP rule annotation (MF_01475) is a computational profile match, not a crystallographic or biochemical experiment, but the biological conclusion (ribosomal protein → translation) is robust."
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

**Accession:** `Q5JJG6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 113. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JJG6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.208051+00:00.  

```json
"Q5JJG6"
```

Source SHA-256: `6c9674c5391066625f25fea0fc494eb473625550343c219b3134ce8e569dad73`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JJG6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.208051+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01475","source":"HAMAP-Rule"}],"value":"Large ribosomal subunit protein eL19"}}}
```

Source SHA-256: `6c9674c5391066625f25fea0fc494eb473625550343c219b3134ce8e569dad73`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JJG6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.208051+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01475","source":"HAMAP-Rule"}],"value":"Binds to the 23S rRNA"}]}
```

Source SHA-256: `6c9674c5391066625f25fea0fc494eb473625550343c219b3134ce8e569dad73`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JJG6.json)  
**Locator:** `/uniProtKBCrossReferences/27`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.208051+00:00.  

```json
{"database":"GO","id":"GO:0006412","properties":[{"key":"GoTerm","value":"P:translation"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniRule"}]}
```

Source SHA-256: `6c9674c5391066625f25fea0fc494eb473625550343c219b3134ce8e569dad73`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JJG6?format=txt&versions=113)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 113 / 1.  
**Retrieved:** 2026-11-02T04:31:30.628071+00:00.  

```text
ID   RL19E_THEKO             Reviewed;         150 AA.
AC   Q5JJG6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   15-FEB-2005, sequence version 1.
DT   28-JAN-2026, entry version 113.
DE   RecName: Full=Large ribosomal subunit protein eL19 {ECO:0000255|HAMAP-Rule:MF_01475};
GN   Name=rpl19e {ECO:0000255|HAMAP-Rule:MF_01475};
GN   OrderedLocusNames=TK1523 {ECO:0000312|EMBL:BAD85712.1};
OS   Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)
OS   (Pyrococcus kodakaraensis (strain KOD1)).
OC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;
OC   Thermococcaceae; Thermococcus.
OX   NCBI_TaxID=69014;
```

Source SHA-256: `89f2058191e5c852afb7a552db1ff6204bc8ed83b2550cad9f645c365cf70da9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JJG6?format=txt&versions=113)  
**Locator:** `lines 35-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 113 / 1.  
**Retrieved:** 2026-11-02T04:31:30.628071+00:00.  

```text
CC   -!- FUNCTION: Binds to the 23S rRNA. {ECO:0000255|HAMAP-Rule:MF_01475}.
```

Source SHA-256: `89f2058191e5c852afb7a552db1ff6204bc8ed83b2550cad9f645c365cf70da9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JJG6?format=txt&versions=113)  
**Locator:** `lines 72-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 113 / 1.  
**Retrieved:** 2026-11-02T04:31:30.628071+00:00.  

```text
DR   GO; GO:0006412; P:translation; IEA:UniProtKB-UniRule.
```

Source SHA-256: `89f2058191e5c852afb7a552db1ff6204bc8ed83b2550cad9f645c365cf70da9`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 66015-66038`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0006412
name: translation
namespace: biological_process
alt_id: GO:0006416
alt_id: GO:0006453
alt_id: GO:0043037
def: "The cellular metabolic process in which a protein is formed, using the sequence of a mature mRNA or circRNA molecule to specify the sequence of amino acids in a polypeptide chain. Translation is mediated by the ribosome, and begins with the formation of a ternary complex between aminoacylated initiator methionine tRNA, GTP, and initiation factor 2, which subsequently associates with the small subunit of the ribosome and an mRNA or circRNA. Translation ends with the release of a polypeptide chain from the ribosome." [GOC:curators]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_plant
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
synonym: "protein translation" EXACT []
xref: Reactome:R-HSA-72766 "Translation"
xref: Wikipedia:Translation_(genetics)
is_a: GO:0009059 ! macromolecule biosynthetic process
is_a: GO:0019538 ! protein metabolic process
relationship: part_of GO:0160307 ! protein biosynthetic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 13. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
