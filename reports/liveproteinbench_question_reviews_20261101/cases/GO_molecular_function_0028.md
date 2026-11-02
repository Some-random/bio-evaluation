# GO_molecular_function_0028

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — nutrient reservoir activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLSKVVLLVALAAICGAQGASYAGRHTADMDFLHKQKKIFDLLLYVRQADLSDAEWYDVGRNYDMESNMDMYKDKNVVQKFLWWYKQGMFLSRNAIFTPLNSEQKYEVRMLFELLYNAKDFQTFYKTAAWARLRMNSGMFTTAFSIAVLYRPDTKYMKFPAIYEIYPNYFFDSSVIEEAQNLKMSRGSSVVTGMNNIETYIVNTNYSSKNMREYNDPEYKLDYFMEDVELNAYYYYMREMLPYWMSSSQYHMPKEIRGQLYYFLHKQLMTRYFLERMSNDLGKTAEFDWNKPINSGFYSTIMYSNGVTFPQRNRFSSLPYYKYKYLNVINALEMRLMDAIDSGYLIDEYGKKIDIYTPEGLNMLGNVIEGSSDSINTKFYGMYDILARDILGYNFDFQNKNNLIPSALQSYSTSMRDPAFYMLYQNILSYFLRYKKLQPQYSQSELQMPGVKFESVNIDKLYTYFDKCDTLINNAVAVENFKGGMYLRLKARRACMNYERFTYKININSDKETKGMMRIFLGPAFDEIKHDMVYLQKYFYLFMEMDRFAVTLRPGSNSIERQSSESPFTTSTIMPSDIFYDKLNKAIGGSEPFTYSEKMLGFPERLILPRGKPEGMRYKMFFFLSSMDESNTKSYEIPLYGKMTLDDKVFGFPLDRPMWAWNFTIPNMYFKDVFIYNRPNEESMNY

[Multiple Choices]
A. 2-oxoglutarate-dependent dioxygenase activity
B. nicotinate-nucleotide adenylyltransferase activity
C. nutrient reservoir activity
D. mRNA N-acetyltransferase activity
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

> The supplied sequence exactly matches the UniProt entry for honeybee Hexamerin 70c, annotated as a storage protein that may supply nutrients. Its GO annotation is nutrient reservoir activity, which fits that function. The GO annotation itself is IEA:UniProtKB-KW, so it is computationally assigned; the function description is literature-cited rather than independently validated by the excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted protein, but that alone does not distinguish nutrient storage from the listed enzyme activities with enough specificity to establish choice C.


**Missing item-specific fact**

> The sequence’s identity as honeybee Hexamerin 70c and its storage-protein function are not supplied in the question; identifying or looking up that protein-specific annotation is needed to distinguish the choices.


**Reason**

> The sequence and choices provide no clear, independently discriminating functional motif or context. Recognizing the protein or consulting its annotation supplies the decisive fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the matched protein’s annotated storage function, nutrient reservoir activity is the clear best choice among the listed options.


### Important caveats

- The sequence match and UniProt identity are reviewer-only evidence, not information supplied to the evaluated model.
- The exact source snapshot used by the author is unknown. The GO annotation is electronically inferred; the cited function statement is not, from these excerpts alone, proof of a direct experimental assay of the molecular function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, but that alone does not distinguish nutrient storage from the listed enzyme activities with enough specificity to establish choice C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence’s identity as honeybee Hexamerin 70c and its storage-protein function are not supplied in the question; identifying or looking up that protein-specific annotation is needed to distinguish the choices.",
    "reason": "The sequence and choices provide no clear, independently discriminating functional motif or context. Recognizing the protein or consulting its annotation supplies the decisive fact."
  },
  "case_id": "GO_molecular_function_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for honeybee Hexamerin 70c, annotated as a storage protein that may supply nutrients. Its GO annotation is nutrient reservoir activity, which fits that function. The GO annotation itself is IEA:UniProtKB-KW, so it is computationally assigned; the function description is literature-cited rather than independently validated by the excerpts."
  },
  "important_caveats": [
    "The sequence match and UniProt identity are reviewer-only evidence, not information supplied to the evaluated model.",
    "The exact source snapshot used by the author is unknown. The GO annotation is electronically inferred; the cited function statement is not, from these excerpts alone, proof of a direct experimental assay of the molecular function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched protein’s annotated storage function, nutrient reservoir activity is the clear best choice among the listed options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for honeybee Hexamerin 70c, annotated as a storage protein that may supply nutrients. Its GO annotation is nutrient reservoir activity, which fits that function. The GO annotation itself is IEA:UniProtKB-KW, so it is computationally assigned; the function description is literature-cited rather than independently validated by the excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, but that alone does not distinguish nutrient storage from the listed enzyme activities with enough specificity to establish choice C.",
    "missing_item_specific_fact": "The sequence’s identity as honeybee Hexamerin 70c and its storage-protein function are not supplied in the question; identifying or looking up that protein-specific annotation is needed to distinguish the choices.",
    "reason": "The sequence and choices provide no clear, independently discriminating functional motif or context. Recognizing the protein or consulting its annotation supplies the decisive fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched protein’s annotated storage function, nutrient reservoir activity is the clear best choice among the listed options."
  },
  "important_caveats": [
    "The sequence match and UniProt identity are reviewer-only evidence, not information supplied to the evaluated model.",
    "The exact source snapshot used by the author is unknown. The GO annotation is electronically inferred; the cited function statement is not, from these excerpts alone, proof of a direct experimental assay of the molecular function."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A8U1C2Y4 (Hexamerin 70c, Apis mellifera) with exact sequence identity. The UniProt FUNCTION comment (ECO:0000305, PubMed:26466725) states it is a 'Storage protein produced during nutritional abundance, which may function as a nutrient supply.' The GO annotation GO:0045735 (nutrient reservoir activity) is assigned via IEA:UniProtKB-KW, and the GO term definition ('Functions in the storage of nutritious substrates') aligns with the hexamerin/arylphorin storage-protein role. The underlying functional claim is supported by literature evidence even though the GO annotation itself is computationally inferred.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A weak argument exists: the protein is 686 aa, has a clear N-terminal signal peptide (MLSKVVLLVALAAICGAQ), is rich in aromatic residues (consistent with 'arylphorin'), and lacks recognizable catalytic motifs for 2-oxoglutarate-dependent dioxygenase (no Fe(II)/2-OG triad context), nicotinate-nucleotide adenylyltransferase (no NMNAT fold motifs), or mRNA N-acetyltransferase. Three of four options are catalytic activities; one is a non-catalytic storage function. One could reason 'large secreted protein without enzyme motifs → storage protein → nutrient reservoir.' However, this absence-of-motif reasoning is inherently weak and does not uniquely identify the hexamerin family or the specific GO term 'nutrient reservoir activity.'


**Missing item-specific fact**

> Knowledge that this sequence belongs to the hexamerin/arylphorin family of insect storage proteins, and that the GO ontology maps storage-protein function specifically to GO:0045735 'nutrient reservoir activity.' Without recognizing the hexamerin family or knowing the ontology mapping, a model cannot confidently select C over the three catalytic distractors based on sequence features alone.


**Reason**

> The reasoning path from sequence to 'nutrient reservoir activity' requires recognizing the hexamerin family (an item-specific annotation fact) and knowing the GO ontology term for storage proteins. The 'no catalytic motifs → storage protein' heuristic is too generic and weak to reliably distinguish C from the three catalytic options, especially since absence of identifiable motifs does not exclude catalytic activity. Selection depends on protein-family-level knowledge absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D all require specific catalytic activities with well-defined mechanistic requirements (2-OG dioxygenase Fe(II) triad, NMNAT fold, GNAT fold). None of these motifs are identifiable in the sequence, making them clearly non-defensible. Option C is the only non-catalytic option and is the only one consistent with a large secreted storage protein. No ambiguity among choices.


### Important caveats

- The GO annotation is IEA (Inferred from Electronic Annotation via keyword), not direct experimental evidence for the molecular function term. The underlying functional description is supported by literature (PubMed:26466725) but the GO term assignment itself is computational.
- The protein is annotated as a 'Precursor' with signal peptide cleavage; the mature protein lacks the N-terminal signal sequence.
- Hexamerins are a well-characterized insect storage protein family, but the sequence itself does not contain a universally recognized diagnostic motif that would allow confident family assignment without prior knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A weak argument exists: the protein is 686 aa, has a clear N-terminal signal peptide (MLSKVVLLVALAAICGAQ), is rich in aromatic residues (consistent with 'arylphorin'), and lacks recognizable catalytic motifs for 2-oxoglutarate-dependent dioxygenase (no Fe(II)/2-OG triad context), nicotinate-nucleotide adenylyltransferase (no NMNAT fold motifs), or mRNA N-acetyltransferase. Three of four options are catalytic activities; one is a non-catalytic storage function. One could reason 'large secreted protein without enzyme motifs → storage protein → nutrient reservoir.' However, this absence-of-motif reasoning is inherently weak and does not uniquely identify the hexamerin family or the specific GO term 'nutrient reservoir activity.'",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Knowledge that this sequence belongs to the hexamerin/arylphorin family of insect storage proteins, and that the GO ontology maps storage-protein function specifically to GO:0045735 'nutrient reservoir activity.' Without recognizing the hexamerin family or knowing the ontology mapping, a model cannot confidently select C over the three catalytic distractors based on sequence features alone.",
    "reason": "The reasoning path from sequence to 'nutrient reservoir activity' requires recognizing the hexamerin family (an item-specific annotation fact) and knowing the GO ontology term for storage proteins. The 'no catalytic motifs → storage protein' heuristic is too generic and weak to reliably distinguish C from the three catalytic options, especially since absence of identifiable motifs does not exclude catalytic activity. Selection depends on protein-family-level knowledge absent from the input."
  },
  "case_id": "GO_molecular_function_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A8U1C2Y4 (Hexamerin 70c, Apis mellifera) with exact sequence identity. The UniProt FUNCTION comment (ECO:0000305, PubMed:26466725) states it is a 'Storage protein produced during nutritional abundance, which may function as a nutrient supply.' The GO annotation GO:0045735 (nutrient reservoir activity) is assigned via IEA:UniProtKB-KW, and the GO term definition ('Functions in the storage of nutritious substrates') aligns with the hexamerin/arylphorin storage-protein role. The underlying functional claim is supported by literature evidence even though the GO annotation itself is computationally inferred."
  },
  "important_caveats": [
    "The GO annotation is IEA (Inferred from Electronic Annotation via keyword), not direct experimental evidence for the molecular function term. The underlying functional description is supported by literature (PubMed:26466725) but the GO term assignment itself is computational.",
    "The protein is annotated as a 'Precursor' with signal peptide cleavage; the mature protein lacks the N-terminal signal sequence.",
    "Hexamerins are a well-characterized insect storage protein family, but the sequence itself does not contain a universally recognized diagnostic motif that would allow confident family assignment without prior knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D all require specific catalytic activities with well-defined mechanistic requirements (2-OG dioxygenase Fe(II) triad, NMNAT fold, GNAT fold). None of these motifs are identifiable in the sequence, making them clearly non-defensible. Option C is the only non-catalytic option and is the only one consistent with a large secreted storage protein. No ambiguity among choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A8U1C2Y4 (Hexamerin 70c, Apis mellifera) with exact sequence identity. The UniProt FUNCTION comment (ECO:0000305, PubMed:26466725) states it is a 'Storage protein produced during nutritional abundance, which may function as a nutrient supply.' The GO annotation GO:0045735 (nutrient reservoir activity) is assigned via IEA:UniProtKB-KW, and the GO term definition ('Functions in the storage of nutritious substrates') aligns with the hexamerin/arylphorin storage-protein role. The underlying functional claim is supported by literature evidence even though the GO annotation itself is computationally inferred.",
    "evidence_ids": ["C1", "C4", "C5", "H5", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A weak argument exists: the protein is 686 aa, has a clear N-terminal signal peptide (MLSKVVLLVALAAICGAQ), is rich in aromatic residues (consistent with 'arylphorin'), and lacks recognizable catalytic motifs for 2-oxoglutarate-dependent dioxygenase (no Fe(II)/2-OG triad context), nicotinate-nucleotide adenylyltransferase (no NMNAT fold motifs), or mRNA N-acetyltransferase. Three of four options are catalytic activities; one is a non-catalytic storage function. One could reason 'large secreted protein without enzyme motifs → storage protein → nutrient reservoir.' However, this absence-of-motif reasoning is inherently weak and does not uniquely identify the hexamerin family or the specific GO term 'nutrient reservoir activity.'",
    "missing_item_specific_fact": "Knowledge that this sequence belongs to the hexamerin/arylphorin family of insect storage proteins, and that the GO ontology maps storage-protein function specifically to GO:0045735 'nutrient reservoir activity.' Without recognizing the hexamerin family or knowing the ontology mapping, a model cannot confidently select C over the three catalytic distractors based on sequence features alone.",
    "reason": "The reasoning path from sequence to 'nutrient reservoir activity' requires recognizing the hexamerin family (an item-specific annotation fact) and knowing the GO ontology term for storage proteins. The 'no catalytic motifs → storage protein' heuristic is too generic and weak to reliably distinguish C from the three catalytic options, especially since absence of identifiable motifs does not exclude catalytic activity. Selection depends on protein-family-level knowledge absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D all require specific catalytic activities with well-defined mechanistic requirements (2-OG dioxygenase Fe(II) triad, NMNAT fold, GNAT fold). None of these motifs are identifiable in the sequence, making them clearly non-defensible. Option C is the only non-catalytic option and is the only one consistent with a large secreted storage protein. No ambiguity among choices."
  },
  "important_caveats": [
    "The GO annotation is IEA (Inferred from Electronic Annotation via keyword), not direct experimental evidence for the molecular function term. The underlying functional description is supported by literature (PubMed:26466725) but the GO term assignment itself is computational.",
    "The protein is annotated as a 'Precursor' with signal peptide cleavage; the mature protein lacks the N-terminal signal sequence.",
    "Hexamerins are a well-characterized insect storage protein family, but the sequence itself does not contain a universally recognized diagnostic motif that would allow confident family assignment without prior knowledge."
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

**Accession:** `A0A8U1C2Y4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:05.694578+00:00.  

```json
"A0A8U1C2Y4"
```

Source SHA-256: `f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:05.694578+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34309096","source":"PubMed"}],"value":"Arylphorin Hex70c"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"9692239","source":"PubMed"}],"value":"Hexamerin 70c"}}}
```

Source SHA-256: `f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:05.694578+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"26466725","source":"PubMed"}],"value":"Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause"}]}
```

Source SHA-256: `f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13)  
**Locator:** `lines 93-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:07.744095+00:00.  

```text
CC   -!- FUNCTION: Storage protein produced during nutritional abundance, which
CC       may function as a nutrient supply to compensate for lack of dietary
CC       proteins during metamorphosis, egg production and diapause.
CC       {ECO:0000305|PubMed:26466725}.
```

Source SHA-256: `5b78371342b563bd895a42c33846d29247ccb53979102fb9ae0e54ce91fe4d52`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13)  
**Locator:** `lines 153-153`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:07.744095+00:00.  

```text
DR   GO; GO:0045735; F:nutrient reservoir activity; IEA:UniProtKB-KW.
```

Source SHA-256: `5b78371342b563bd895a42c33846d29247ccb53979102fb9ae0e54ce91fe4d52`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 268007-268020`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0045735
name: nutrient reservoir activity
namespace: molecular_function
def: "Functions in the storage of nutritious substrates." [GOC:ai]
comment: Note that this term can be used in place of the obsolete terms 'storage protein ; GO:0005187' and 'storage protein of fat body (sensu Insecta) ; GO:0008041'.
subset: goslim_generic
subset: goslim_pir
subset: goslim_prokaryote
synonym: "storage protein" RELATED []
synonym: "storage protein of fat body" RELATED []
synonym: "yolk protein" RELATED []
is_a: GO:0003674 ! molecular_function

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
