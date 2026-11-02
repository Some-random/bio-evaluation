# GO_molecular_function_0140

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — RNA polymerase II cis-regulatory region sequence-specific DNA binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGHLQAARPYGSPTSMHASLHMPEPNMGPSGMAFPSMAPELYAPPQPLRAPDATSQPAPKAYACSTCGKGFARRSDLARHERIHTGVRPHVCEYPNCGKQFIQRSALTVHQRVHTGEKPHMCERCGKPFSDSSSLARHRRIHSGKRPYKCPYADCQKTFTRRTTLTRHQNHHTGTVEDAARATAEVLARNSVARSASARPTRSEGDQISNHGSPLSTPSPAQRTMSMSPSAELAAANGMQHQYNGNSSLPAHMRTDLHSSSPAATTSSGFSSNVRPTSHPNAYGAAPPPTTLEPSIEGSQGPGSAVGSPHMSSVGWASPSHVASPAHSNSGGNSSYVYPDPDSSYPTNAAAQGQMFYSAAMGLQRPGSAEPGAQSAYKPRQNELWAA

[Multiple Choices]
A. phosphoglycolate phosphatase activity
B. peroxidase inhibitor activity
C. NADPH dehydrogenase activity
D. RNA polymerase II cis-regulatory region sequence-specific DNA binding
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

> The exact sequence matches the UniProt record annotated with the keyed GO term. That specific annotation is computational (IEA:TreeGrafter); separately, the record describes the protein as a transcription factor with evidence linked to a publication, but the excerpts do not establish direct experimental measurement of this particular DNA-binding activity.

Citations as saved: [C7](#evidence-c7), [C5](#evidence-c5), [H5](#evidence-h5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains tandem C2H2-type zinc-finger motifs, a strong sequence-based clue for a eukaryotic DNA-binding transcription factor. This meaningfully favors D over the phosphatase, peroxidase-inhibitor, and NADPH-dehydrogenase choices.


**Missing item-specific fact**

> The sequence alone does not establish the protein's exact DNA target or independently prove its RNA polymerase II cis-regulatory role; those finer specifics are supported by protein-specific annotation rather than the supplied prompt.


**Reason**

> The prominent zinc-finger pattern and the alternatives provide a concrete basis for selecting the transcription-factor DNA-binding option, even though the exact GO specificity is not fully demonstrated by sequence inspection alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, D is substantially better aligned with the tandem C2H2 zinc-finger pattern than the three enzymatic or inhibitor activities.


### Important caveats

- The exact sequence match is confirmed in both current and historical UniProt records, but the author's precise source snapshot is unknown.
- The exact keyed GO annotation is computationally assigned; the cited functional description supports transcription-factor status but is not, in these excerpts, direct experimental evidence of sequence-specific DNA binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains tandem C2H2-type zinc-finger motifs, a strong sequence-based clue for a eukaryotic DNA-binding transcription factor. This meaningfully favors D over the phosphatase, peroxidase-inhibitor, and NADPH-dehydrogenase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish the protein's exact DNA target or independently prove its RNA polymerase II cis-regulatory role; those finer specifics are supported by protein-specific annotation rather than the supplied prompt.",
    "reason": "The prominent zinc-finger pattern and the alternatives provide a concrete basis for selecting the transcription-factor DNA-binding option, even though the exact GO specificity is not fully demonstrated by sequence inspection alone."
  },
  "case_id": "GO_molecular_function_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C5",
      "H5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record annotated with the keyed GO term. That specific annotation is computational (IEA:TreeGrafter); separately, the record describes the protein as a transcription factor with evidence linked to a publication, but the excerpts do not establish direct experimental measurement of this particular DNA-binding activity."
  },
  "important_caveats": [
    "The exact sequence match is confirmed in both current and historical UniProt records, but the author's precise source snapshot is unknown.",
    "The exact keyed GO annotation is computationally assigned; the cited functional description supports transcription-factor status but is not, in these excerpts, direct experimental evidence of sequence-specific DNA binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D is substantially better aligned with the tandem C2H2 zinc-finger pattern than the three enzymatic or inhibitor activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record annotated with the keyed GO term. That specific annotation is computational (IEA:TreeGrafter); separately, the record describes the protein as a transcription factor with evidence linked to a publication, but the excerpts do not establish direct experimental measurement of this particular DNA-binding activity.",
    "evidence_ids": ["C7", "C5", "H5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains tandem C2H2-type zinc-finger motifs, a strong sequence-based clue for a eukaryotic DNA-binding transcription factor. This meaningfully favors D over the phosphatase, peroxidase-inhibitor, and NADPH-dehydrogenase choices.",
    "missing_item_specific_fact": "The sequence alone does not establish the protein's exact DNA target or independently prove its RNA polymerase II cis-regulatory role; those finer specifics are supported by protein-specific annotation rather than the supplied prompt.",
    "reason": "The prominent zinc-finger pattern and the alternatives provide a concrete basis for selecting the transcription-factor DNA-binding option, even though the exact GO specificity is not fully demonstrated by sequence inspection alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D is substantially better aligned with the tandem C2H2 zinc-finger pattern than the three enzymatic or inhibitor activities."
  },
  "important_caveats": [
    "The exact sequence match is confirmed in both current and historical UniProt records, but the author's precise source snapshot is unknown.",
    "The exact keyed GO annotation is computationally assigned; the cited functional description supports transcription-factor status but is not, in these excerpts, direct experimental evidence of sequence-specific DNA binding."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A9P4XV22 (ZAP1_CRYP1), annotated as a C2H2-type transcription factor. GO:0000978 (RNA polymerase II cis-regulatory region sequence-specific DNA binding) is explicitly annotated in the entry (evidence: IEA:TreeGrafter). The protein is experimentally confirmed as a transcription factor (PubMed:39611846, ECO:0000269). While the specific GO term assignment is computational (TreeGrafter), the underlying function—C2H2 zinc finger transcription factor binding cis-regulatory DNA—is well-supported by both the experimental TF characterization and the canonical biology of C2H2 zinc finger proteins in fungi.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains three recognizable C2H2 zinc finger motifs (C-X2-4-C-X12-H-X3-5-H pattern): e.g., 'ACSTCGKGFARRSDLARHERIHTG' (C-X3-C-X12-H-X3-H), 'MCERCGKPFSDSSSLARHRRIHSG' (C-X2-C-X11-H-X3-H), and 'CPYADCQKTFTRRTTLTRHQNHHTG' (C-X4-C-X11-H-X2-H). C2H2 zinc fingers are canonical eukaryotic DNA-binding domains of transcription factors. In eukaryotes (including fungi), such TFs bind cis-regulatory sequences to regulate RNA polymerase II transcription. None of the distractor options (phosphatase, peroxidase inhibitor, NADPH dehydrogenase) have any corresponding catalytic or binding motifs in the sequence.


**Missing item-specific fact**

> None required. Identification of C2H2 zinc finger motifs from primary sequence and the inference that they mediate sequence-specific DNA binding in eukaryotic transcription factors constitutes general biological knowledge.


**Reason**

> A model can identify the tandem C2H2 zinc finger pattern directly from the amino acid sequence without knowing the specific protein identity. The logical chain (C2H2 ZF → TF → cis-regulatory DNA binding for RNA Pol II) is standard molecular biology. The distractors (hydrolase, inhibitor, oxidoreductase activities) lack any corresponding structural or catalytic motifs in the sequence, making them eliminable by general reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular functions (phosphatase, inhibitor, oxidoreductase, DNA binding). The presence of clear C2H2 zinc finger motifs uniquely supports the DNA-binding transcription factor option. No other option has any sequence-level support.


### Important caveats

- The specific GO:0000978 annotation carries evidence code IEA:TreeGrafter (computational phylogenetic transfer), not direct experimental validation of this exact GO term for this protein. However, the protein's identity as a C2H2-type transcription factor is experimentally supported.
- The UniProt entry was first released 2025-04-09; the benchmark author's source snapshot is unknown. The sequence match is confirmed for entry version 11 (released 2026-01-28).
- The fungal Zap1 homolog's specific DNA-binding target (zinc-responsive elements vs. other cis-regulatory sequences) is inferred from homology to S. cerevisiae Zap1; the exact cis-element specificity in C. parasitica was not independently verified in the provided evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains three recognizable C2H2 zinc finger motifs (C-X2-4-C-X12-H-X3-5-H pattern): e.g., 'ACSTCGKGFARRSDLARHERIHTG' (C-X3-C-X12-H-X3-H), 'MCERCGKPFSDSSSLARHRRIHSG' (C-X2-C-X11-H-X3-H), and 'CPYADCQKTFTRRTTLTRHQNHHTG' (C-X4-C-X11-H-X2-H). C2H2 zinc fingers are canonical eukaryotic DNA-binding domains of transcription factors. In eukaryotes (including fungi), such TFs bind cis-regulatory sequences to regulate RNA polymerase II transcription. None of the distractor options (phosphatase, peroxidase inhibitor, NADPH dehydrogenase) have any corresponding catalytic or binding motifs in the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. Identification of C2H2 zinc finger motifs from primary sequence and the inference that they mediate sequence-specific DNA binding in eukaryotic transcription factors constitutes general biological knowledge.",
    "reason": "A model can identify the tandem C2H2 zinc finger pattern directly from the amino acid sequence without knowing the specific protein identity. The logical chain (C2H2 ZF → TF → cis-regulatory DNA binding for RNA Pol II) is standard molecular biology. The distractors (hydrolase, inhibitor, oxidoreductase activities) lack any corresponding structural or catalytic motifs in the sequence, making them eliminable by general reasoning."
  },
  "case_id": "GO_molecular_function_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H3",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A9P4XV22 (ZAP1_CRYP1), annotated as a C2H2-type transcription factor. GO:0000978 (RNA polymerase II cis-regulatory region sequence-specific DNA binding) is explicitly annotated in the entry (evidence: IEA:TreeGrafter). The protein is experimentally confirmed as a transcription factor (PubMed:39611846, ECO:0000269). While the specific GO term assignment is computational (TreeGrafter), the underlying function—C2H2 zinc finger transcription factor binding cis-regulatory DNA—is well-supported by both the experimental TF characterization and the canonical biology of C2H2 zinc finger proteins in fungi."
  },
  "important_caveats": [
    "The specific GO:0000978 annotation carries evidence code IEA:TreeGrafter (computational phylogenetic transfer), not direct experimental validation of this exact GO term for this protein. However, the protein's identity as a C2H2-type transcription factor is experimentally supported.",
    "The UniProt entry was first released 2025-04-09; the benchmark author's source snapshot is unknown. The sequence match is confirmed for entry version 11 (released 2026-01-28).",
    "The fungal Zap1 homolog's specific DNA-binding target (zinc-responsive elements vs. other cis-regulatory sequences) is inferred from homology to S. cerevisiae Zap1; the exact cis-element specificity in C. parasitica was not independently verified in the provided evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular functions (phosphatase, inhibitor, oxidoreductase, DNA binding). The presence of clear C2H2 zinc finger motifs uniquely supports the DNA-binding transcription factor option. No other option has any sequence-level support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A9P4XV22 (ZAP1_CRYP1), annotated as a C2H2-type transcription factor. GO:0000978 (RNA polymerase II cis-regulatory region sequence-specific DNA binding) is explicitly annotated in the entry (evidence: IEA:TreeGrafter). The protein is experimentally confirmed as a transcription factor (PubMed:39611846, ECO:0000269). While the specific GO term assignment is computational (TreeGrafter), the underlying function—C2H2 zinc finger transcription factor binding cis-regulatory DNA—is well-supported by both the experimental TF characterization and the canonical biology of C2H2 zinc finger proteins in fungi.",
    "evidence_ids": ["C4", "C5", "C7", "H3", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains three recognizable C2H2 zinc finger motifs (C-X2-4-C-X12-H-X3-5-H pattern): e.g., 'ACSTCGKGFARRSDLARHERIHTG' (C-X3-C-X12-H-X3-H), 'MCERCGKPFSDSSSLARHRRIHSG' (C-X2-C-X11-H-X3-H), and 'CPYADCQKTFTRRTTLTRHQNHHTG' (C-X4-C-X11-H-X2-H). C2H2 zinc fingers are canonical eukaryotic DNA-binding domains of transcription factors. In eukaryotes (including fungi), such TFs bind cis-regulatory sequences to regulate RNA polymerase II transcription. None of the distractor options (phosphatase, peroxidase inhibitor, NADPH dehydrogenase) have any corresponding catalytic or binding motifs in the sequence.",
    "missing_item_specific_fact": "None required. Identification of C2H2 zinc finger motifs from primary sequence and the inference that they mediate sequence-specific DNA binding in eukaryotic transcription factors constitutes general biological knowledge.",
    "reason": "A model can identify the tandem C2H2 zinc finger pattern directly from the amino acid sequence without knowing the specific protein identity. The logical chain (C2H2 ZF → TF → cis-regulatory DNA binding for RNA Pol II) is standard molecular biology. The distractors (hydrolase, inhibitor, oxidoreductase activities) lack any corresponding structural or catalytic motifs in the sequence, making them eliminable by general reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular functions (phosphatase, inhibitor, oxidoreductase, DNA binding). The presence of clear C2H2 zinc finger motifs uniquely supports the DNA-binding transcription factor option. No other option has any sequence-level support."
  },
  "important_caveats": [
    "The specific GO:0000978 annotation carries evidence code IEA:TreeGrafter (computational phylogenetic transfer), not direct experimental validation of this exact GO term for this protein. However, the protein's identity as a C2H2-type transcription factor is experimentally supported.",
    "The UniProt entry was first released 2025-04-09; the benchmark author's source snapshot is unknown. The sequence match is confirmed for entry version 11 (released 2026-01-28).",
    "The fungal Zap1 homolog's specific DNA-binding target (zinc-responsive elements vs. other cis-regulatory sequences) is inferred from homology to S. cerevisiae Zap1; the exact cis-element specificity in C. parasitica was not independently verified in the provided evidence."
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

**Accession:** `A0A9P4XV22` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 11. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:16.008633+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39611846","source":"PubMed"}],"value":"C2H2-type transcription factor ZAP1"}}}
```

Source SHA-256: `eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:16.008633+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"value":"Transcription factor that plays an important role in C.parasitica development and virulence"}]}
```

Source SHA-256: `eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:16.008633+00:00.  

```json
{"database":"GO","id":"GO:0000978","properties":[{"key":"GoTerm","value":"F:RNA polymerase II cis-regulatory region sequence-specific DNA binding"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11)  
**Locator:** `lines 31-32`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-02T04:26:18.672095+00:00.  

```text
CC   -!- FUNCTION: Transcription factor that plays an important role in
CC       C.parasitica development and virulence. {ECO:0000269|PubMed:39611846}.
```

Source SHA-256: `ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11)  
**Locator:** `lines 56-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-02T04:26:18.672095+00:00.  

```text
DR   GO; GO:0000978; F:RNA polymerase II cis-regulatory region sequence-specific DNA binding; IEA:TreeGrafter.
```

Source SHA-256: `ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 7126-7141`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000978
name: RNA polymerase II cis-regulatory region sequence-specific DNA binding
namespace: molecular_function
alt_id: GO:0000980
def: "Binding to a specific upstream regulatory DNA sequence (transcription factor recognition sequence or binding site) located in cis relative to the transcription start site (i.e., on the same strand of DNA) of a gene transcribed by RNA polymerase II." [GOC:txnOH-2018]
comment: Note that the phrase "upstream activating sequence", or UAS is often used in S. cerevisiae literature to refer to cis-regulatory sequences. In bacteria such as E. coli, the phrase "upstream activating sequence", or UAS is usually a synonym for "enhancer".
synonym: "RNA polymerase II core promoter proximal region sequence-specific DNA binding" RELATED []
synonym: "RNA polymerase II distal enhancer sequence-specific DNA binding" RELATED []
synonym: "RNA polymerase II promoter proximal region sequence-specific DNA binding" RELATED []
synonym: "RNA polymerase II proximal promoter sequence-specific DNA binding" RELATED []
synonym: "RNA polymerase II upstream activating sequence (UAS) sequence-specific DNA binding" RELATED []
xref: Reactome:R-HSA-400204 "PPARA binds RXRA"
is_a: GO:0000977 ! RNA polymerase II transcription regulatory region sequence-specific DNA binding
is_a: GO:0000987 ! cis-regulatory region sequence-specific DNA binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 140. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
