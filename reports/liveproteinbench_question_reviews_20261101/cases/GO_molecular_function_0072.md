# GO_molecular_function_0072

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — toxin activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRHIGVFVGVLALALVLLVVEARSDAERGVCACPRIYMPVCGSNLKTYNNDCLLRCEINSDLGRANNLRKIADQACDNLTDNVNDFIPQEY

[Multiple Choices]
A. deacetylase activity
B. UDP-glucosyltransferase activity
C. fatty acid synthase activity
D. toxin activity
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

> The exact sequence matches a UniProt entry annotated with toxin activity (GO:0090729), but that annotation is IEA and based on a UniProt keyword, not direct experimental evidence for toxin activity. Experimental evidence instead supports protease-inhibitor activity, which is not among the choices.

Citations as saved: [H11](#evidence-h11), [GO5](#evidence-go5), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and cysteine-rich sequence are consistent with a secreted, disulfide-stabilized inhibitor, making the listed metabolic enzyme activities implausible. Those features do not establish toxin activity rather than a non-toxin protease inhibitor.


**Missing item-specific fact**

> The sequence's protein-specific toxin-activity annotation, or independent evidence that its protease-inhibitory action qualifies as toxin activity, is needed to select D.


**Reason**

> The sequence offers useful clues about secretion and inhibitor-like structure, but the precise toxin classification depends on an item-specific annotation or functional context not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No two listed choices are comparably supported; however, the experimentally supported peptidase-inhibitor function is absent, and the available support for D is annotation-level rather than experimental evidence of toxin activity.


### Important caveats

- The matched historical UniProt entry carries the toxin-activity annotation, but its IEA evidence code indicates an inferred annotation.
- The protein's reported anticoagulant and protease-inhibitory effects do not by themselves establish that toxin activity is its primary molecular function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and cysteine-rich sequence are consistent with a secreted, disulfide-stabilized inhibitor, making the listed metabolic enzyme activities implausible. Those features do not establish toxin activity rather than a non-toxin protease inhibitor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's protein-specific toxin-activity annotation, or independent evidence that its protease-inhibitory action qualifies as toxin activity, is needed to select D.",
    "reason": "The sequence offers useful clues about secretion and inhibitor-like structure, but the precise toxin classification depends on an item-specific annotation or functional context not supplied in the question."
  },
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "H11",
      "GO5",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with toxin activity (GO:0090729), but that annotation is IEA and based on a UniProt keyword, not direct experimental evidence for toxin activity. Experimental evidence instead supports protease-inhibitor activity, which is not among the choices."
  },
  "important_caveats": [
    "The matched historical UniProt entry carries the toxin-activity annotation, but its IEA evidence code indicates an inferred annotation.",
    "The protein's reported anticoagulant and protease-inhibitory effects do not by themselves establish that toxin activity is its primary molecular function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No two listed choices are comparably supported; however, the experimentally supported peptidase-inhibitor function is absent, and the available support for D is annotation-level rather than experimental evidence of toxin activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with toxin activity (GO:0090729), but that annotation is IEA and based on a UniProt keyword, not direct experimental evidence for toxin activity. Experimental evidence instead supports protease-inhibitor activity, which is not among the choices.",
    "evidence_ids": ["H11", "GO5", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and cysteine-rich sequence are consistent with a secreted, disulfide-stabilized inhibitor, making the listed metabolic enzyme activities implausible. Those features do not establish toxin activity rather than a non-toxin protease inhibitor.",
    "missing_item_specific_fact": "The sequence's protein-specific toxin-activity annotation, or independent evidence that its protease-inhibitory action qualifies as toxin activity, is needed to select D.",
    "reason": "The sequence offers useful clues about secretion and inhibitor-like structure, but the precise toxin classification depends on an item-specific annotation or functional context not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No two listed choices are comparably supported; however, the experimentally supported peptidase-inhibitor function is absent, and the available support for D is annotation-level rather than experimental evidence of toxin activity."
  },
  "important_caveats": [
    "The matched historical UniProt entry carries the toxin-activity annotation, but its IEA evidence code indicates an inferred annotation.",
    "The protein's reported anticoagulant and protease-inhibitory effects do not by themselves establish that toxin activity is its primary molecular function."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q177W0 does carry GO:0090729 'toxin activity' (evidence_id H11), so the expected answer has a database annotation. However, this annotation is IEA:UniProtKB-KW (electronic, keyword-based inference), not experimental. The primary experimental annotation (IDA, evidence_id C7/H9) is GO:0030414 'peptidase inhibitor activity,' and the FUNCTION comment describes anticoagulant/serine-protease-inhibitor activity. The 'toxin activity' assignment is a weak electronic annotation that may loosely reflect the protein's role in interfering with host physiology during blood-feeding, but it is not the experimentally supported primary molecular function.

Citations as saved: [H11](#evidence-h11), [H9](#evidence-h9), [H7](#evidence-h7), [C7](#evidence-c7), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 91-residue sequence contains a hydrophobic N-terminal signal peptide and multiple cysteines consistent with a small, disulfide-stabilized secreted protein. Fatty acid synthase (C) requires a multi-domain megasynthase (>2000 aa in eukaryotes); UDP-glucosyltransferase (B) requires a PSPG motif and transferase fold absent here; deacetylase (A) requires specific catalytic residues (e.g., His-Asp-His or metal-binding motifs) not present. By elimination based on size, domain architecture, and absence of catalytic motifs, only D remains plausible for a small secreted cysteine-rich arthropod protein.


**Missing item-specific fact**

> The specific assignment of 'toxin activity' rather than 'peptidase inhibitor activity' as the correct GO term depends on the benchmark's option set (peptidase inhibitor is not offered) and on the UniProt keyword-based IEA annotation. Without the option set, a knowledgeable annotator would more precisely assign 'serine-type endopeptidase inhibitor activity.'


**Reason**

> The elimination of A, B, and C relies on general structural/biochemical reasoning (protein size, absence of catalytic motifs, domain architecture) that is accessible from the sequence alone. D is selected as the only remaining option for a small secreted cysteine-rich protein. However, the positive identification specifically as 'toxin' rather than 'inhibitor' is somewhat arbitrary and depends on the option set design rather than a strong positive biological argument distinguishing 'toxin' from 'peptidase inhibitor.'


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are clearly incompatible with a 91-aa secreted cysteine-rich protein. Only D is structurally plausible among the four choices. There is no genuine ambiguity among the offered options, though the biological precision of labeling this Kazal-type trypsin inhibitor as a 'toxin' rather than a 'peptidase inhibitor' is debatable.


### Important caveats

- The 'toxin activity' annotation (GO:0090729) is IEA (electronic/keyword-based), not experimental. The IDA experimental annotation is 'peptidase inhibitor activity.'
- The GO definition of toxin activity (GO:0090729) requires 'initiating pathogenesis' and 'evolved function selected for,' with examples like botulinum toxin and snake venom. A Kazal-type trypsin inhibitor from a mosquito's salivary glands is a borderline case for this definition.
- The correct answer is determined largely by elimination of clearly incompatible options rather than by a strong positive argument for 'toxin' specifically.
- The UniProt keyword assignment that generated the IEA annotation is not independently validated as an accurate functional description.
- The protein's actual experimental function (anticoagulant, serine protease inhibitor) is not offered as an option, forcing selection of the closest available term.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 91-residue sequence contains a hydrophobic N-terminal signal peptide and multiple cysteines consistent with a small, disulfide-stabilized secreted protein. Fatty acid synthase (C) requires a multi-domain megasynthase (>2000 aa in eukaryotes); UDP-glucosyltransferase (B) requires a PSPG motif and transferase fold absent here; deacetylase (A) requires specific catalytic residues (e.g., His-Asp-His or metal-binding motifs) not present. By elimination based on size, domain architecture, and absence of catalytic motifs, only D remains plausible for a small secreted cysteine-rich arthropod protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific assignment of 'toxin activity' rather than 'peptidase inhibitor activity' as the correct GO term depends on the benchmark's option set (peptidase inhibitor is not offered) and on the UniProt keyword-based IEA annotation. Without the option set, a knowledgeable annotator would more precisely assign 'serine-type endopeptidase inhibitor activity.'",
    "reason": "The elimination of A, B, and C relies on general structural/biochemical reasoning (protein size, absence of catalytic motifs, domain architecture) that is accessible from the sequence alone. D is selected as the only remaining option for a small secreted cysteine-rich protein. However, the positive identification specifically as 'toxin' rather than 'inhibitor' is somewhat arbitrary and depends on the option set design rather than a strong positive biological argument distinguishing 'toxin' from 'peptidase inhibitor.'"
  },
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "H11",
      "H9",
      "H7",
      "C7",
      "C5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q177W0 does carry GO:0090729 'toxin activity' (evidence_id H11), so the expected answer has a database annotation. However, this annotation is IEA:UniProtKB-KW (electronic, keyword-based inference), not experimental. The primary experimental annotation (IDA, evidence_id C7/H9) is GO:0030414 'peptidase inhibitor activity,' and the FUNCTION comment describes anticoagulant/serine-protease-inhibitor activity. The 'toxin activity' assignment is a weak electronic annotation that may loosely reflect the protein's role in interfering with host physiology during blood-feeding, but it is not the experimentally supported primary molecular function."
  },
  "important_caveats": [
    "The 'toxin activity' annotation (GO:0090729) is IEA (electronic/keyword-based), not experimental. The IDA experimental annotation is 'peptidase inhibitor activity.'",
    "The GO definition of toxin activity (GO:0090729) requires 'initiating pathogenesis' and 'evolved function selected for,' with examples like botulinum toxin and snake venom. A Kazal-type trypsin inhibitor from a mosquito's salivary glands is a borderline case for this definition.",
    "The correct answer is determined largely by elimination of clearly incompatible options rather than by a strong positive argument for 'toxin' specifically.",
    "The UniProt keyword assignment that generated the IEA annotation is not independently validated as an accurate functional description.",
    "The protein's actual experimental function (anticoagulant, serine protease inhibitor) is not offered as an option, forcing selection of the closest available term."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a 91-aa secreted cysteine-rich protein. Only D is structurally plausible among the four choices. There is no genuine ambiguity among the offered options, though the biological precision of labeling this Kazal-type trypsin inhibitor as a 'toxin' rather than a 'peptidase inhibitor' is debatable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q177W0 does carry GO:0090729 'toxin activity' (evidence_id H11), so the expected answer has a database annotation. However, this annotation is IEA:UniProtKB-KW (electronic, keyword-based inference), not experimental. The primary experimental annotation (IDA, evidence_id C7/H9) is GO:0030414 'peptidase inhibitor activity,' and the FUNCTION comment describes anticoagulant/serine-protease-inhibitor activity. The 'toxin activity' assignment is a weak electronic annotation that may loosely reflect the protein's role in interfering with host physiology during blood-feeding, but it is not the experimentally supported primary molecular function.",
    "evidence_ids": ["H11", "H9", "H7", "C7", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 91-residue sequence contains a hydrophobic N-terminal signal peptide and multiple cysteines consistent with a small, disulfide-stabilized secreted protein. Fatty acid synthase (C) requires a multi-domain megasynthase (>2000 aa in eukaryotes); UDP-glucosyltransferase (B) requires a PSPG motif and transferase fold absent here; deacetylase (A) requires specific catalytic residues (e.g., His-Asp-His or metal-binding motifs) not present. By elimination based on size, domain architecture, and absence of catalytic motifs, only D remains plausible for a small secreted cysteine-rich arthropod protein.",
    "missing_item_specific_fact": "The specific assignment of 'toxin activity' rather than 'peptidase inhibitor activity' as the correct GO term depends on the benchmark's option set (peptidase inhibitor is not offered) and on the UniProt keyword-based IEA annotation. Without the option set, a knowledgeable annotator would more precisely assign 'serine-type endopeptidase inhibitor activity.'",
    "reason": "The elimination of A, B, and C relies on general structural/biochemical reasoning (protein size, absence of catalytic motifs, domain architecture) that is accessible from the sequence alone. D is selected as the only remaining option for a small secreted cysteine-rich protein. However, the positive identification specifically as 'toxin' rather than 'inhibitor' is somewhat arbitrary and depends on the option set design rather than a strong positive biological argument distinguishing 'toxin' from 'peptidase inhibitor.'"
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a 91-aa secreted cysteine-rich protein. Only D is structurally plausible among the four choices. There is no genuine ambiguity among the offered options, though the biological precision of labeling this Kazal-type trypsin inhibitor as a 'toxin' rather than a 'peptidase inhibitor' is debatable."
  },
  "important_caveats": [
    "The 'toxin activity' annotation (GO:0090729) is IEA (electronic/keyword-based), not experimental. The IDA experimental annotation is 'peptidase inhibitor activity.'",
    "The GO definition of toxin activity (GO:0090729) requires 'initiating pathogenesis' and 'evolved function selected for,' with examples like botulinum toxin and snake venom. A Kazal-type trypsin inhibitor from a mosquito's salivary glands is a borderline case for this definition.",
    "The correct answer is determined largely by elimination of clearly incompatible options rather than by a strong positive argument for 'toxin' specifically.",
    "The UniProt keyword assignment that generated the IEA annotation is not independently validated as an accurate functional description.",
    "The protein's actual experimental function (anticoagulant, serine protease inhibitor) is not offered as an option, forcing selection of the closest available term."
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

**Accession:** `Q177W0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:30.165069+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20363282","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21167902","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31726374","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"34800067","source":"PubMed"}],"value":"Anticoagulant protein that decreases host thrombin (F2) activity via an uncompetitive inhibition mechanism (PubMed:20363282, PubMed:21167902). Inhibits amidolytic activity of host plasmin (PLG) (PubMed:20363282, PubMed:31726374, PubMed:34800067). Inhibits amidolytic activity of host trypsin (PubMed:20363282). Inhibits trypsin-like endogenous activity from gut of female mosquitoes 24 hours after feeding and weakly affects enzyme activity from gut 3 hours after feeding, suggesting a possible role as an inhibitor of endogenous proteases (PubMed:20363282)"}]}
```

Source SHA-256: `6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:30.165069+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"20363282","source":"PubMed"}],"id":"GO:0030414","properties":[{"key":"GoTerm","value":"F:peptidase inhibitor activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)  
**Locator:** `lines 90-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:30:32.304115+00:00.  

```text
CC   -!- FUNCTION: Anticoagulant protein that decreases host thrombin (F2)
CC       activity via an uncompetitive inhibition mechanism (PubMed:20363282,
CC       PubMed:21167902). Inhibits amidolytic activity of host plasmin (PLG)
CC       (PubMed:20363282, PubMed:31726374, PubMed:34800067). Inhibits
CC       amidolytic activity of host trypsin (PubMed:20363282). Inhibits
CC       trypsin-like endogenous activity from gut of female mosquitoes 24 hours
CC       after feeding and weakly affects enzyme activity from gut 3 hours after
CC       feeding, suggesting a possible role as an inhibitor of endogenous
CC       proteases (PubMed:20363282). {ECO:0000269|PubMed:20363282,
CC       ECO:0000269|PubMed:21167902, ECO:0000269|PubMed:31726374,
CC       ECO:0000269|PubMed:34800067}.
```

Source SHA-256: `59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)  
**Locator:** `lines 151-151`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:30:32.304115+00:00.  

```text
DR   GO; GO:0030414; F:peptidase inhibitor activity; IDA:UniProtKB.
```

Source SHA-256: `59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)  
**Locator:** `lines 153-153`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:30:32.304115+00:00.  

```text
DR   GO; GO:0090729; F:toxin activity; IEA:UniProtKB-KW.
```

Source SHA-256: `59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 401379-401391`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0090729
name: toxin activity
namespace: molecular_function
alt_id: GO:0050827
def: "Interacting selectively with one or more biological molecules in another (target) organism, initiating pathogenesis (leading to an abnormal, generally detrimental state) in the target organism. The activity should refer to an evolved function of the active gene product, i.e. one that was selected for. Examples include the activity of botulinum toxin, and snake venom." [GOC:pt]
subset: goslim_generic
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
synonym: "toxin receptor binding" EXACT []
xref: Wikipedia:Toxin
is_a: GO:0003674 ! molecular_function

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 72. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
