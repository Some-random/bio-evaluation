# GO_cellular_component_0070

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — primosome complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIYHRIAVNVPLSDGLLTYSHSEPLPPGTRVLVPFRNKTVVGMVWETDIAPDMDAARILSVQTVFVEEKPLSQSWRDLLAFTSRYYHYPTGQAVFAALPQGLKETRAVEMPQPPLFYALNEAGRAQTPPPARFNKKAALWDALLSGEMTMAALKQANAQAAKLIEDWAEQGWIETTEAAKPVLRPYRGQASHSEFVLNTGQQKASDEIQTALGRFRSFLLYGITGSGKTEVYFDAMAKVLAQGRQVLFLLPEINLTPQLLKRVENRFADVPTAVLHSRMAAGRRTQDYLRAMLGQAKLVIGTRLAVFTPLPDVGLIVVDEEHDGSFKQDNELRYHARDLAVWRAKQGGCPVVLGSATPSLESWHKAQSGAYRLLQLTERAHASAQLPQVDILNIGRLKLDNGFSPQALQLLKQNFEAGGMSLVYLNRRGFAPALFCGDCGHTFGCPNCSAKMVLHQRARQLRCHHCDHREPIPFKCPDCGNQDLTAVGHGTQRVEETLRAFLPKAAVVRVDRDSTAHKNDWADLYRRIANDEIDILVGTQMLAKGHDFARLNLVIVLNADGSLYSADFRAPERLFAELMQVSGRAGRADKPGKVLIQTQLPEHPVFAAVKAQDYAVFAENELNERQMFAMPPFGFQTAVRADAPRVADAMEFLNAAKETLAPLLPESVSRFGAAPMLMVRLAERERAQVFLESTSRQDLHRAVSLWVQVLQQNRDGKIRWSVDVDPQEA

[Multiple Choices]
A. cell surface
B. primosome complex
C. microneme
D. plasma membrane
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

> The exact-match sequence has a UniProt GO annotation to primosome complex (GO:1990077), assigned by UniRule (IEA); the archived entry available by the approximate benchmark cutoff carries the same annotation. This supports the key as a computational annotation, not as direct experimental localization evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains ATPase/helicase-like motifs, which can suggest a soluble DNA-processing protein and make membrane or microneme choices unlikely. But those motifs alone do not establish membership in a primosome complex.


**Missing item-specific fact**

> The sequence-specific identification as PriA, a replication-restart helicase, and its association with the primosome are needed to distinguish choice B reliably.


**Reason**

> The key is supported by a sequence-matched database annotation, but that annotation and the specific PriA identity are absent from the model input. Broad inference that this is a DNA helicase does not by itself establish the requested complex location.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Cell surface and plasma membrane are related terms, but the available sequence features do not make either a defensible alternative for this DNA-helicase-like protein. The main limitation is dependence on the specific complex annotation, not a clear tie between choices.


### Important caveats

- The GO evidence is IEA:UniProtKB-UniRule, so it is computational annotation rather than direct experimental localization evidence.
- The exact author source snapshot is unknown; the historical entry matched the sequence and carried the annotation by the approximate cutoff.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains ATPase/helicase-like motifs, which can suggest a soluble DNA-processing protein and make membrane or microneme choices unlikely. But those motifs alone do not establish membership in a primosome complex.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific identification as PriA, a replication-restart helicase, and its association with the primosome are needed to distinguish choice B reliably.",
    "reason": "The key is supported by a sequence-matched database annotation, but that annotation and the specific PriA identity are absent from the model input. Broad inference that this is a DNA helicase does not by itself establish the requested complex location."
  },
  "case_id": "GO_cellular_component_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact-match sequence has a UniProt GO annotation to primosome complex (GO:1990077), assigned by UniRule (IEA); the archived entry available by the approximate benchmark cutoff carries the same annotation. This supports the key as a computational annotation, not as direct experimental localization evidence."
  },
  "important_caveats": [
    "The GO evidence is IEA:UniProtKB-UniRule, so it is computational annotation rather than direct experimental localization evidence.",
    "The exact author source snapshot is unknown; the historical entry matched the sequence and carried the annotation by the approximate cutoff."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Cell surface and plasma membrane are related terms, but the available sequence features do not make either a defensible alternative for this DNA-helicase-like protein. The main limitation is dependence on the specific complex annotation, not a clear tie between choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-match sequence has a UniProt GO annotation to primosome complex (GO:1990077), assigned by UniRule (IEA); the archived entry available by the approximate benchmark cutoff carries the same annotation. This supports the key as a computational annotation, not as direct experimental localization evidence.",
    "evidence_ids": ["C1", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains ATPase/helicase-like motifs, which can suggest a soluble DNA-processing protein and make membrane or microneme choices unlikely. But those motifs alone do not establish membership in a primosome complex.",
    "missing_item_specific_fact": "The sequence-specific identification as PriA, a replication-restart helicase, and its association with the primosome are needed to distinguish choice B reliably.",
    "reason": "The key is supported by a sequence-matched database annotation, but that annotation and the specific PriA identity are absent from the model input. Broad inference that this is a DNA helicase does not by itself establish the requested complex location."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Cell surface and plasma membrane are related terms, but the available sequence features do not make either a defensible alternative for this DNA-helicase-like protein. The main limitation is dependence on the specific complex annotation, not a clear tie between choices."
  },
  "important_caveats": [
    "The GO evidence is IEA:UniProtKB-UniRule, so it is computational annotation rather than direct experimental localization evidence.",
    "The exact author source snapshot is unknown; the historical entry matched the sequence and carried the annotation by the approximate cutoff."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5F6V8 (sequence matched exactly, 729 AA) annotates this protein as PriA (Replication restart protein / ATP-dependent DNA helicase) with GO:1990077 (primosome complex), evidence code IEA:UniProtKB-UniRule. The GO definition for primosome complex explicitly includes replicative helicases that form at replication forks. The annotation is computational (IEA via HAMAP rule MF_00983), but it is consistent with the well-established biology of PriA as a core primosome component. No contradicting evidence is present.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three distractors are eliminable by general biological reasoning: (A) cell surface and (D) plasma membrane require transmembrane domains or signal/anchor sequences, which are absent from this hydrophilic 729-residue protein; (C) microneme is an organelle exclusive to apicomplexan parasites (e.g., Plasmodium, Toxoplasma), and this sequence contains bacterial-type motifs (e.g., Walker A-like GTQRVEET, zinc-finger CHHCDHREPIPFKCPDCGNQ) inconsistent with an apicomplexan secretory organelle protein. The remaining positive reasoning path is recognizing helicase/ATPase motifs (Walker A/B, RecA-like domains, zinc finger) characteristic of a DNA replication helicase, which in bacteria is a core component of the primosome complex (the complex that initiates/restarts replication at forks). Among the four choices, only B is a DNA-replication-associated complex.


**Missing item-specific fact**

> None strictly required for elimination. Positive identification of the exact GO term 'primosome complex' (as opposed to a more generic 'nucleoid' or 'replisome') benefits from knowing PriA's specific role, but the question's four choices make elimination sufficient.


**Reason**

> The model can distinguish the answer using general molecular biology: absence of membrane-targeting signals eliminates A and D; organismal context (bacterial helicase motifs, no apicomplexan targeting signals) eliminates C; presence of helicase/ATPase motifs points to a replication complex, and 'primosome complex' is the only replication-associated option. This constitutes a concrete biological argument grounded in the supplied sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (cell surface, microneme, plasma membrane) are clearly incompatible with a bacterial DNA helicase lacking transmembrane segments and apicomplexan targeting signals. Only B is biologically plausible.


### Important caveats

- The GO annotation is IEA (Inferred from Electronic Annotation) via UniRule/HAMAP, not direct experimental localization. However, the biological role of PriA in the primosome is well-supported by the cited experimental literature (PubMed 16030229, 21861872, 23193948).
- The reviewer identified the accession Q5F6V8 from dataset metadata absent from the model input; the model must rely solely on sequence analysis and general knowledge.
- The primosome complex is a protein-DNA complex (GO:1990077 is_a GO:0032993), not a classical 'compartment' like mitochondria or nucleus; the GO Cellular Component namespace includes macromolecular complexes, so this is a valid annotation target.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three distractors are eliminable by general biological reasoning: (A) cell surface and (D) plasma membrane require transmembrane domains or signal/anchor sequences, which are absent from this hydrophilic 729-residue protein; (C) microneme is an organelle exclusive to apicomplexan parasites (e.g., Plasmodium, Toxoplasma), and this sequence contains bacterial-type motifs (e.g., Walker A-like GTQRVEET, zinc-finger CHHCDHREPIPFKCPDCGNQ) inconsistent with an apicomplexan secretory organelle protein. The remaining positive reasoning path is recognizing helicase/ATPase motifs (Walker A/B, RecA-like domains, zinc finger) characteristic of a DNA replication helicase, which in bacteria is a core component of the primosome complex (the complex that initiates/restarts replication at forks). Among the four choices, only B is a DNA-replication-associated complex.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required for elimination. Positive identification of the exact GO term 'primosome complex' (as opposed to a more generic 'nucleoid' or 'replisome') benefits from knowing PriA's specific role, but the question's four choices make elimination sufficient.",
    "reason": "The model can distinguish the answer using general molecular biology: absence of membrane-targeting signals eliminates A and D; organismal context (bacterial helicase motifs, no apicomplexan targeting signals) eliminates C; presence of helicase/ATPase motifs points to a replication complex, and 'primosome complex' is the only replication-associated option. This constitutes a concrete biological argument grounded in the supplied sequence and choices."
  },
  "case_id": "GO_cellular_component_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5F6V8 (sequence matched exactly, 729 AA) annotates this protein as PriA (Replication restart protein / ATP-dependent DNA helicase) with GO:1990077 (primosome complex), evidence code IEA:UniProtKB-UniRule. The GO definition for primosome complex explicitly includes replicative helicases that form at replication forks. The annotation is computational (IEA via HAMAP rule MF_00983), but it is consistent with the well-established biology of PriA as a core primosome component. No contradicting evidence is present."
  },
  "important_caveats": [
    "The GO annotation is IEA (Inferred from Electronic Annotation) via UniRule/HAMAP, not direct experimental localization. However, the biological role of PriA in the primosome is well-supported by the cited experimental literature (PubMed 16030229, 21861872, 23193948).",
    "The reviewer identified the accession Q5F6V8 from dataset metadata absent from the model input; the model must rely solely on sequence analysis and general knowledge.",
    "The primosome complex is a protein-DNA complex (GO:1990077 is_a GO:0032993), not a classical 'compartment' like mitochondria or nucleus; the GO Cellular Component namespace includes macromolecular complexes, so this is a valid annotation target."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (cell surface, microneme, plasma membrane) are clearly incompatible with a bacterial DNA helicase lacking transmembrane segments and apicomplexan targeting signals. Only B is biologically plausible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5F6V8 (sequence matched exactly, 729 AA) annotates this protein as PriA (Replication restart protein / ATP-dependent DNA helicase) with GO:1990077 (primosome complex), evidence code IEA:UniProtKB-UniRule. The GO definition for primosome complex explicitly includes replicative helicases that form at replication forks. The annotation is computational (IEA via HAMAP rule MF_00983), but it is consistent with the well-established biology of PriA as a core primosome component. No contradicting evidence is present.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three distractors are eliminable by general biological reasoning: (A) cell surface and (D) plasma membrane require transmembrane domains or signal/anchor sequences, which are absent from this hydrophilic 729-residue protein; (C) microneme is an organelle exclusive to apicomplexan parasites (e.g., Plasmodium, Toxoplasma), and this sequence contains bacterial-type motifs (e.g., Walker A-like GTQRVEET, zinc-finger CHHCDHREPIPFKCPDCGNQ) inconsistent with an apicomplexan secretory organelle protein. The remaining positive reasoning path is recognizing helicase/ATPase motifs (Walker A/B, RecA-like domains, zinc finger) characteristic of a DNA replication helicase, which in bacteria is a core component of the primosome complex (the complex that initiates/restarts replication at forks). Among the four choices, only B is a DNA-replication-associated complex.",
    "missing_item_specific_fact": "None strictly required for elimination. Positive identification of the exact GO term 'primosome complex' (as opposed to a more generic 'nucleoid' or 'replisome') benefits from knowing PriA's specific role, but the question's four choices make elimination sufficient.",
    "reason": "The model can distinguish the answer using general molecular biology: absence of membrane-targeting signals eliminates A and D; organismal context (bacterial helicase motifs, no apicomplexan targeting signals) eliminates C; presence of helicase/ATPase motifs points to a replication complex, and 'primosome complex' is the only replication-associated option. This constitutes a concrete biological argument grounded in the supplied sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (cell surface, microneme, plasma membrane) are clearly incompatible with a bacterial DNA helicase lacking transmembrane segments and apicomplexan targeting signals. Only B is biologically plausible."
  },
  "important_caveats": [
    "The GO annotation is IEA (Inferred from Electronic Annotation) via UniRule/HAMAP, not direct experimental localization. However, the biological role of PriA in the primosome is well-supported by the cited experimental literature (PubMed 16030229, 21861872, 23193948).",
    "The reviewer identified the accession Q5F6V8 from dataset metadata absent from the model input; the model must rely solely on sequence analysis and general knowledge.",
    "The primosome complex is a protein-DNA complex (GO:1990077 is_a GO:0032993), not a classical 'compartment' like mitochondria or nucleus; the GO Cellular Component namespace includes macromolecular complexes, so this is a valid annotation target."
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

**Accession:** `Q5F6V8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 129. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.112172+00:00.  

```json
"Q5F6V8"
```

Source SHA-256: `b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.112172+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305","id":"21861872","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"23193948","source":"PubMed"}],"value":"5.6.2.4"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"}],"value":"ATP-dependent DNA helicase PriA"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"}],"value":"DNA 3'-5' helicase PriA"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16030229","source":"PubMed"}],"value":"Helicase PriA"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"}],"value":"Replication restart protein PriA"}}}
```

Source SHA-256: `b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F6V8.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.112172+00:00.  

```json
{"database":"GO","id":"GO:1990077","properties":[{"key":"GoTerm","value":"C:primosome complex"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniRule"}]}
```

Source SHA-256: `b5b3e858bb9761d1b737c3ba299a6e1429b6885613578b017e20a1b0ffec3241`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 129 / 1.  
**Retrieved:** 2026-11-01T06:28:37.505271+00:00.  

```text
ID   PRIA_NEIG1              Reviewed;         729 AA.
AC   Q5F6V8;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   15-MAR-2005, sequence version 1.
DT   28-JAN-2026, entry version 129.
DE   RecName: Full=Replication restart protein PriA {ECO:0000255|HAMAP-Rule:MF_00983};
DE   AltName: Full=ATP-dependent DNA helicase PriA {ECO:0000255|HAMAP-Rule:MF_00983};
DE            EC=5.6.2.4 {ECO:0000255|HAMAP-Rule:MF_00983, ECO:0000305|PubMed:21861872, ECO:0000305|PubMed:23193948};
DE   AltName: Full=DNA 3'-5' helicase PriA {ECO:0000255|HAMAP-Rule:MF_00983};
DE   AltName: Full=Helicase PriA {ECO:0000303|PubMed:16030229};
GN   Name=priA {ECO:0000255|HAMAP-Rule:MF_00983};
GN   OrderedLocusNames=NGO_1437 {ECO:0000312|EMBL:AAW90079.1};
OS   Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;
OC   Neisseriaceae; Neisseria.
OX   NCBI_TaxID=242231;
```

Source SHA-256: `149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F6V8?format=txt&versions=129)  
**Locator:** `lines 127-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 129 / 1.  
**Retrieved:** 2026-11-01T06:28:37.505271+00:00.  

```text
DR   GO; GO:1990077; C:primosome complex; IEA:UniProtKB-UniRule.
```

Source SHA-256: `149f53c33eaf2ea402a9b117865fd102b5ab54abe5c58034fe43b571a3a2e5d3`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 549032-549040`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1990077
name: primosome complex
namespace: cellular_component
def: "Any of a family of protein complexes that form at the origin of replication or stalled replication forks and function in replication primer synthesis in all organisms. Early complexes initiate double-stranded DNA unwinding. The core unit consists of a replicative helicase and a primase. The helicase further unwinds the DNA and recruits the polymerase machinery. The primase synthesizes RNA primers that act as templates for complementary stand replication by the polymerase machinery. The primosome contains a number of associated proteins and protein complexes and contributes to the processes of replication initiation, lagging strand elongation, and replication restart." [GOC:bhm, GOC:mah, PMID:21856207]
synonym: "primosome" EXACT []
is_a: GO:0032993 ! protein-DNA complex
relationship: part_of GO:0030894 ! replisome

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
