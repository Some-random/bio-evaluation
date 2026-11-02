# pathway_0097

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Protein biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDSQQSVEVLNQLLARLSVATPDNRDEVATEVSSFVNGNIIEHDAPEHFFNGLAKAIKDKKSAVNALAAVSHVASTSGLAPSVEPYVVALVPAILEQTGSKDKDVQSAANAALHAVVTAVNPVAVKAVLPHLTKSLSETNKWQEKVAVLSAISALVDQAKSQISLRMTELIPVLSEAMWDTKKEVKNAATATMTKATETVENKDIERFIPKLIECIANPSEVPETVHLLGATTFVAEVTPATLSIMTPLLSRGLAERETPIKRKSAVIIDNMCKLVEDPQIVAPFLNKLLPGLKNNFSVIADPEAREVTLRGLKTLRRVGAVGEGDVLPEISHAGDPATTLGVLDSLLKTENIAKKFRPAVEYISCIGGDLIDERIIDQQTWFTHVLPYMTIFLHQNQAKEILDEFRKRAVDNIPEPPKFDDEEEEGEDLCNCEFSLAYGAKILLNRTQLRLKRGRRYGLCGPNGSGKSTLMRAIANGQVDGFPSQEECRTVYVEHDIDGTHAETSVLDFVFQGDVGTKEAISAKLKEFGFDDEMIVMPIAALSGGWKMKLALARAVLKNADILLLDEPTNHLDTVNVAWLTNYLITCGITSIVVSHDSGFLDNICQYIIHYEGLKLRKYKGNLSALVERVPSAKSYYELGASDLEFRFPEPGYLEGVKTKQKAIVKVSNMTFQYPGTSKPQISDVSFQCSLSSRIAVIGPNGAGKSTLINVLTGELLPTTGEVYTHENIRIAYIKQHAFAHIESHLDKTPSEYIQWRFQTGEDRETMDRANRQINEDDAQAMNKIFKIDGTPRRIAGIHSRRKFKNSYEYECSFLLGENIGMKSERWVPMMSVDNAWLPRGEVIESHGKMVAEVDMKEALASGQFRPLTRKEIEEHCAMLGLDAELVSHSRIRGLSGGQKVKLVLAAGTWQRPHLIVLDEPTNYLDRDSLGALSKALKEFEGGVIIITHSAEFTKDLTEEVWAVRDGLMTPSGHNWVSGQGSGPRLEKKEDEEDKFDAMGNKISSGTKKTKLSSAELRKKKKERMKKKKELGDAYVSDDDADF

[Multiple Choices]
A. Antifungal biosynthesis. .
B. One-carbon metabolism
C. chorismate biosynthesis
D. Protein biosynthesis
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt sequence for elongation factor 3, whose pathway annotation is protein biosynthesis/polypeptide-chain elongation. The pathway annotation is transferred by similarity, not direct experimental evidence in the cited record.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains ATPase-like motifs, but those do not by themselves identify a protein-biosynthesis role or distinguish it reliably from the other pathway options.


**Missing item-specific fact**

> Identifying this specific protein as elongation factor 3, or knowing its protein-biosynthesis annotation, is needed to select D.


**Reason**

> The matching annotation supports the key, but that protein-specific identity and pathway fact are absent from the question. Recognizing the sequence from an external database would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports protein biosynthesis; the alternatives are not supported by the supplied evidence.


### Important caveats

- The cited pathway annotation is similarity-transferred (ECO:0000250), so it should not be represented as direct experimental proof for this exact protein.
- The exact author source snapshot is unknown, although the sequence matches the archived and current UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains ATPase-like motifs, but those do not by themselves identify a protein-biosynthesis role or distinguish it reliably from the other pathway options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this specific protein as elongation factor 3, or knowing its protein-biosynthesis annotation, is needed to select D.",
    "reason": "The matching annotation supports the key, but that protein-specific identity and pathway fact are absent from the question. Recognizing the sequence from an external database would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "pathway_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for elongation factor 3, whose pathway annotation is protein biosynthesis/polypeptide-chain elongation. The pathway annotation is transferred by similarity, not direct experimental evidence in the cited record."
  },
  "important_caveats": [
    "The cited pathway annotation is similarity-transferred (ECO:0000250), so it should not be represented as direct experimental proof for this exact protein.",
    "The exact author source snapshot is unknown, although the sequence matches the archived and current UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports protein biosynthesis; the alternatives are not supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for elongation factor 3, whose pathway annotation is protein biosynthesis/polypeptide-chain elongation. The pathway annotation is transferred by similarity, not direct experimental evidence in the cited record.",
    "evidence_ids": ["C1", "C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains ATPase-like motifs, but those do not by themselves identify a protein-biosynthesis role or distinguish it reliably from the other pathway options.",
    "missing_item_specific_fact": "Identifying this specific protein as elongation factor 3, or knowing its protein-biosynthesis annotation, is needed to select D.",
    "reason": "The matching annotation supports the key, but that protein-specific identity and pathway fact are absent from the question. Recognizing the sequence from an external database would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports protein biosynthesis; the alternatives are not supported by the supplied evidence."
  },
  "important_caveats": [
    "The cited pathway annotation is similarity-transferred (ECO:0000250), so it should not be represented as direct experimental proof for this exact protein.",
    "The exact author source snapshot is unknown, although the sequence matches the archived and current UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C5E4D9 (sequence SHA256 matched) annotates this protein as Elongation Factor 3 (eEF3) from Zygosaccharomyces rouxii, with the pathway comment 'Protein biosynthesis; polypeptide chain elongation' (evidence code ECO:0000250, transferred from O93796). EF3 is a well-characterized AAA+ protein essential for fungal translation. The answer D (Protein biosynthesis) is directly supported by the annotation, though the evidence code indicates computational transfer by similarity rather than direct experimental pathway reconstitution.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two canonical Walker A (P-loop) motifs ('GPNGSGKST' and 'GPNGAGKST') paired with two Walker B motifs ('DEPTNHL' and 'DEPTNYL'), indicating a multi-domain AAA+ ATPase architecture. In eukaryotic cells, multi-domain AAA+ proteins of this size (~1045 aa) are hallmarks of elongation factors (particularly EF3, which has three AAA+ domains). Metabolic enzymes in one-carbon metabolism (folate-dependent methyltransferases, serine hydroxymethyltransferase) or chorismate biosynthesis (DAHP synthase, chorismate synthase, shikimate kinases) have entirely different domain architectures (TIM barrels, Rossmann folds, specific catalytic residues for methyl/aryl chemistry) and would not present multiple P-loop/Walker B pairs. Thus, the nucleotide-binding motor architecture visible in the sequence supports assignment to protein biosynthesis (translation) over the metabolic distractors.


**Missing item-specific fact**

> None critical. Identifying the protein specifically as EF3 rather than another AAA+ protein would require database lookup, but the pathway-level question (protein biosynthesis vs. metabolic pathways) is addressable from the multi-AAA+ architecture.


**Reason**

> The presence of multiple P-loop and Walker B motifs is a concrete, interpretable sequence feature that distinguishes translation factors from metabolic enzymes. A biologist recognizing AAA+ architecture in a ~1 kb eukaryotic protein would reasonably infer a role in translation (protein biosynthesis) rather than in folate chemistry or shikimate-pathway reactions.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors (antifungal biosynthesis, one-carbon metabolism, chorismate biosynthesis) involve enzymes with fundamentally different domain architectures (methyltransferases, TIM barrels, aromatic-ring biosynthetic enzymes) that are incompatible with the observed multi-AAA+ nucleotide-binding motifs. Only protein biosynthesis is consistent with the sequence features.


### Important caveats

- The UniProt pathway annotation uses evidence code ECO:0000250 (similarity-based transfer from O93796, a S. cerevisiae EF3), not direct experimental pathway reconstitution for this specific Z. rouxii protein.
- The protein was integrated into Swiss-Prot in February 2025; the benchmark construction date is unknown, but the sequence (version 1, from 2009) has been available in TrEMBL since then.
- EF3 is unique to fungi; its AAA+ architecture and role in E-site tRNA release are well established in S. cerevisiae but the specific annotation here is transferred by homology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two canonical Walker A (P-loop) motifs ('GPNGSGKST' and 'GPNGAGKST') paired with two Walker B motifs ('DEPTNHL' and 'DEPTNYL'), indicating a multi-domain AAA+ ATPase architecture. In eukaryotic cells, multi-domain AAA+ proteins of this size (~1045 aa) are hallmarks of elongation factors (particularly EF3, which has three AAA+ domains). Metabolic enzymes in one-carbon metabolism (folate-dependent methyltransferases, serine hydroxymethyltransferase) or chorismate biosynthesis (DAHP synthase, chorismate synthase, shikimate kinases) have entirely different domain architectures (TIM barrels, Rossmann folds, specific catalytic residues for methyl/aryl chemistry) and would not present multiple P-loop/Walker B pairs. Thus, the nucleotide-binding motor architecture visible in the sequence supports assignment to protein biosynthesis (translation) over the metabolic distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Identifying the protein specifically as EF3 rather than another AAA+ protein would require database lookup, but the pathway-level question (protein biosynthesis vs. metabolic pathways) is addressable from the multi-AAA+ architecture.",
    "reason": "The presence of multiple P-loop and Walker B motifs is a concrete, interpretable sequence feature that distinguishes translation factors from metabolic enzymes. A biologist recognizing AAA+ architecture in a ~1 kb eukaryotic protein would reasonably infer a role in translation (protein biosynthesis) rather than in folate chemistry or shikimate-pathway reactions."
  },
  "case_id": "pathway_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C5E4D9 (sequence SHA256 matched) annotates this protein as Elongation Factor 3 (eEF3) from Zygosaccharomyces rouxii, with the pathway comment 'Protein biosynthesis; polypeptide chain elongation' (evidence code ECO:0000250, transferred from O93796). EF3 is a well-characterized AAA+ protein essential for fungal translation. The answer D (Protein biosynthesis) is directly supported by the annotation, though the evidence code indicates computational transfer by similarity rather than direct experimental pathway reconstitution."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses evidence code ECO:0000250 (similarity-based transfer from O93796, a S. cerevisiae EF3), not direct experimental pathway reconstitution for this specific Z. rouxii protein.",
    "The protein was integrated into Swiss-Prot in February 2025; the benchmark construction date is unknown, but the sequence (version 1, from 2009) has been available in TrEMBL since then.",
    "EF3 is unique to fungi; its AAA+ architecture and role in E-site tRNA release are well established in S. cerevisiae but the specific annotation here is transferred by homology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors (antifungal biosynthesis, one-carbon metabolism, chorismate biosynthesis) involve enzymes with fundamentally different domain architectures (methyltransferases, TIM barrels, aromatic-ring biosynthetic enzymes) that are incompatible with the observed multi-AAA+ nucleotide-binding motifs. Only protein biosynthesis is consistent with the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C5E4D9 (sequence SHA256 matched) annotates this protein as Elongation Factor 3 (eEF3) from Zygosaccharomyces rouxii, with the pathway comment 'Protein biosynthesis; polypeptide chain elongation' (evidence code ECO:0000250, transferred from O93796). EF3 is a well-characterized AAA+ protein essential for fungal translation. The answer D (Protein biosynthesis) is directly supported by the annotation, though the evidence code indicates computational transfer by similarity rather than direct experimental pathway reconstitution.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two canonical Walker A (P-loop) motifs ('GPNGSGKST' and 'GPNGAGKST') paired with two Walker B motifs ('DEPTNHL' and 'DEPTNYL'), indicating a multi-domain AAA+ ATPase architecture. In eukaryotic cells, multi-domain AAA+ proteins of this size (~1045 aa) are hallmarks of elongation factors (particularly EF3, which has three AAA+ domains). Metabolic enzymes in one-carbon metabolism (folate-dependent methyltransferases, serine hydroxymethyltransferase) or chorismate biosynthesis (DAHP synthase, chorismate synthase, shikimate kinases) have entirely different domain architectures (TIM barrels, Rossmann folds, specific catalytic residues for methyl/aryl chemistry) and would not present multiple P-loop/Walker B pairs. Thus, the nucleotide-binding motor architecture visible in the sequence supports assignment to protein biosynthesis (translation) over the metabolic distractors.",
    "missing_item_specific_fact": "None critical. Identifying the protein specifically as EF3 rather than another AAA+ protein would require database lookup, but the pathway-level question (protein biosynthesis vs. metabolic pathways) is addressable from the multi-AAA+ architecture.",
    "reason": "The presence of multiple P-loop and Walker B motifs is a concrete, interpretable sequence feature that distinguishes translation factors from metabolic enzymes. A biologist recognizing AAA+ architecture in a ~1 kb eukaryotic protein would reasonably infer a role in translation (protein biosynthesis) rather than in folate chemistry or shikimate-pathway reactions."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors (antifungal biosynthesis, one-carbon metabolism, chorismate biosynthesis) involve enzymes with fundamentally different domain architectures (methyltransferases, TIM barrels, aromatic-ring biosynthetic enzymes) that are incompatible with the observed multi-AAA+ nucleotide-binding motifs. Only protein biosynthesis is consistent with the sequence features."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses evidence code ECO:0000250 (similarity-based transfer from O93796, a S. cerevisiae EF3), not direct experimental pathway reconstitution for this specific Z. rouxii protein.",
    "The protein was integrated into Swiss-Prot in February 2025; the benchmark construction date is unknown, but the sequence (version 1, from 2009) has been available in TrEMBL since then.",
    "EF3 is unique to fungi; its AAA+ architecture and role in E-site tRNA release are well established in S. cerevisiae but the specific annotation here is transferred by homology."
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

**Accession:** `C5E4D9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 92. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:30.729914+00:00.  

```json
"C5E4D9"
```

Source SHA-256: `78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:30.729914+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Eukaryotic elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"eEF3"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P16521","source":"UniProtKB"}],"value":"3.6.4.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"EF-3"}]}}
```

Source SHA-256: `78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5E4D9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:30.729914+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"O93796","source":"UniProtKB"}],"value":"Protein biosynthesis; polypeptide chain elongation"}]}
```

Source SHA-256: `78dcdd53defbd870dd80429da3a521bf6b9c15cff19e86939dd9e30a390f5e14`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5E4D9?format=txt&versions=92)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:35.219574+00:00.  

```text
ID   EF3_ZYGRC               Reviewed;        1045 AA.
AC   C5E4D9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-JUL-2009, sequence version 1.
DT   28-JAN-2026, entry version 92.
DE   RecName: Full=Elongation factor 3 {ECO:0000305};
DE            Short=EF-3 {ECO:0000305};
DE            EC=3.6.4.- {ECO:0000250|UniProtKB:P16521};
DE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};
DE            Short=eEF3 {ECO:0000305};
GN   Name=TEF3 {ECO:0000305};
GN   OrderedLocusNames=ZYRO0E05148g {ECO:0000312|EMBL:CAR30900.1};
OS   Zygosaccharomyces rouxii (strain ATCC 2623 / CBS 732 / NBRC 1130 / NCYC 568
OS   / NRRL Y-229).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Saccharomycetes;
OC   Saccharomycetales; Saccharomycetaceae; Zygosaccharomyces.
OX   NCBI_TaxID=559307 {ECO:0000312|Proteomes:UP000008536};
```

Source SHA-256: `24912b3780dfdc2175cd526300f2f38c8d113474ab82078ce32761e3bafbca36`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5E4D9?format=txt&versions=92)  
**Locator:** `lines 58-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:35.219574+00:00.  

```text
CC   -!- PATHWAY: Protein biosynthesis; polypeptide chain elongation.
CC       {ECO:0000250|UniProtKB:O93796}.
```

Source SHA-256: `24912b3780dfdc2175cd526300f2f38c8d113474ab82078ce32761e3bafbca36`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
