# GO_cellular_component_0034

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — nucleus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVVPGGPSSRPAVGAQFFCTAGRGLEPFLMREVRERLAATQVEYISGKVFFTTCSDLNMLKQLKSAERLFLLIKKQLPFPVSSVSKGKILNELQRLINDDPESWLNAISIWKNLLELDAKKEKLSHKNANPLKRKVGEDDITAKKLKTEQIQELQETKECQLEKQIEEKILEQGNFITEGEKFQKLQDDVTEAVDTRNQTNLTFRVSCRCSGAVAKTLTAQEVGRVIGIALMKQFGWKADLRNPNLEIFIHLSDVYSVLGIPVFRVPLACRAYIKTAGLRSTIAWAMASLAEIKAGAVVLDPMCGLGTILLEAAKEWPHVYYVGADVSDSQLSGAYDNLRAAGLRDKIELLQVSVIELPLPSESVDIIISDIPFGKKFKLGKDIKRMLQEMERVLRVGGTIVLLLSEDHHRHLKGGEASSGPLNSQGGHTEEPGGEERLTPAEKAAVSEPVSSPFAASNQGRLDRMPPLGSLVPVDCYRVSLGKTDALISKYKKSHSPGR

[Multiple Choices]
A. histone deacetylase complex
B. nucleus
C. lipid droplet
D. midbody
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

> The exact sequence matches a UniProt entry annotated to the nucleus. However, the localization is transferred by similarity (ECO:0000250), and the GO annotation is ISS, so this supports the key as a computational inference rather than direct experimental evidence for this bovine protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a soluble enzyme involved in RNA modification, but that does not reliably distinguish nuclear localization from other cellular locations. It has no unmistakable targeting signal that establishes the answer.


**Missing item-specific fact**

> The protein-specific localization annotation or equivalent evidence that this THUMPD2 protein is nuclear.


**Reason**

> The supplied sequence and choices do not provide a sufficiently discriminating localization argument; selecting nucleus depends on protein-specific knowledge or external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Nucleus is the supported broad compartment. The other choices are more specific structures or complexes, and the supplied information does not establish association with them.


### Important caveats

- The matched UniProt localization is similarity-based, not direct experimental localization evidence for this exact bovine protein.
- Reviewer-only annotations support the key but were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a soluble enzyme involved in RNA modification, but that does not reliably distinguish nuclear localization from other cellular locations. It has no unmistakable targeting signal that establishes the answer.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization annotation or equivalent evidence that this THUMPD2 protein is nuclear.",
    "reason": "The supplied sequence and choices do not provide a sufficiently discriminating localization argument; selecting nucleus depends on protein-specific knowledge or external annotation."
  },
  "case_id": "GO_cellular_component_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to the nucleus. However, the localization is transferred by similarity (ECO:0000250), and the GO annotation is ISS, so this supports the key as a computational inference rather than direct experimental evidence for this bovine protein."
  },
  "important_caveats": [
    "The matched UniProt localization is similarity-based, not direct experimental localization evidence for this exact bovine protein.",
    "Reviewer-only annotations support the key but were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Nucleus is the supported broad compartment. The other choices are more specific structures or complexes, and the supplied information does not establish association with them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to the nucleus. However, the localization is transferred by similarity (ECO:0000250), and the GO annotation is ISS, so this supports the key as a computational inference rather than direct experimental evidence for this bovine protein.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a soluble enzyme involved in RNA modification, but that does not reliably distinguish nuclear localization from other cellular locations. It has no unmistakable targeting signal that establishes the answer.",
    "missing_item_specific_fact": "The protein-specific localization annotation or equivalent evidence that this THUMPD2 protein is nuclear.",
    "reason": "The supplied sequence and choices do not provide a sufficiently discriminating localization argument; selecting nucleus depends on protein-specific knowledge or external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Nucleus is the supported broad compartment. The other choices are more specific structures or complexes, and the supplied information does not establish association with them."
  },
  "important_caveats": [
    "The matched UniProt localization is similarity-based, not direct experimental localization evidence for this exact bovine protein.",
    "Reviewer-only annotations support the key but were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E1B8U2 (THUMPD2_BOVIN) annotates SUBCELLULAR LOCATION as Nucleus (evidence ECO:0000250, inferred by similarity to human Q9BTF0) and carries GO:0005634 (nucleus, ISS). The protein is a U6 snRNA (guanine-N2)-methyltransferase; U6 snRNA is a nuclear spliceosomal RNA, making nuclear localization functionally consistent. The experimental IDA evidence supports membership in the 'tRNA methyltransferase complex' (GO:0043527), which is not among the options but is a nuclear complex. The nucleus annotation, while ISS-level, is well-supported by the protein's enzymatic function targeting a nuclear RNA.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold-like methyltransferase domain (the region with conserved motifs around 'VSCRCSGAVAKTLTAQEVGRVIGIALMKQFGWKADLRNPNLEIFIHLSDVYSVLGIPVFRVPLACRAYIKTAGLRSTIAWAMASLAEIKAGAVVLDPMCGLGTILLEAAKEWPHVYYVGADVSDSQLSGAYDNLRAAGLRDKIELLQVSVIELPLPSESVDIIISDIPFGKKFKLGKDIKRMLQEMERVLRVGGTIVLLLS') and an RNA-binding THUMP domain. This domain architecture identifies the protein as an RNA-modifying enzyme, which is incompatible with lipid droplet (C: no lipid-handling domains) and midbody (D: no cytoskeletal/structural domains). The protein lacks the metalloprotease-like HDAC fold, eliminating the histone deacetylase complex (A). By elimination of three clearly incompatible options, nucleus (B) remains. Additionally, RNA-binding + methyltransferase architecture is associated with nuclear RNA processing pathways.


**Missing item-specific fact**

> The specific identity of the target RNA (U6 snRNA vs. cytoplasmic tRNA) would require item-specific knowledge, but since 'cytoplasm' is not among the options, the elimination-based reasoning suffices to select B.


**Reason**

> The domain architecture visible in the sequence (methyltransferase fold + RNA-binding THUMP domain) provides a concrete biological argument to eliminate options A, C, and D. The protein is clearly an enzyme acting on RNA, not a structural component of lipid droplets or the midbody, and it lacks HDAC domains. While positive identification of 'nucleus' over a hypothetical 'cytoplasm' would require knowing the specific RNA target, cytoplasm is not an option, so the elimination reasoning is sufficient and grounded in general biological knowledge of protein domain-function relationships.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated by protein domain architecture. Only 'nucleus' is compatible with an RNA methyltransferase bearing a THUMP domain. The histone deacetylase complex requires a completely different fold, and lipid droplet/midbody are incompatible with an enzymatic protein lacking any structural or lipid-handling domains.


### Important caveats

- The 'nucleus' annotation in UniProt is ISS (inferred by similarity to human ortholog Q9BTF0), not directly experimental for the bovine protein. The direct experimental evidence (IDA) supports 'tRNA methyltransferase complex' (GO:0043527), which is not among the answer options.
- No classical bipartite NLS is easily identifiable in the sequence, so positive nuclear targeting cannot be confirmed purely from primary sequence inspection; the reasoning relies on elimination and functional inference.
- The protein's GO annotation includes 'tRNA methyltransferase complex' (IDA), which could arguably be a more precise sub-compartment answer, but it is not offered as an option.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold-like methyltransferase domain (the region with conserved motifs around 'VSCRCSGAVAKTLTAQEVGRVIGIALMKQFGWKADLRNPNLEIFIHLSDVYSVLGIPVFRVPLACRAYIKTAGLRSTIAWAMASLAEIKAGAVVLDPMCGLGTILLEAAKEWPHVYYVGADVSDSQLSGAYDNLRAAGLRDKIELLQVSVIELPLPSESVDIIISDIPFGKKFKLGKDIKRMLQEMERVLRVGGTIVLLLS') and an RNA-binding THUMP domain. This domain architecture identifies the protein as an RNA-modifying enzyme, which is incompatible with lipid droplet (C: no lipid-handling domains) and midbody (D: no cytoskeletal/structural domains). The protein lacks the metalloprotease-like HDAC fold, eliminating the histone deacetylase complex (A). By elimination of three clearly incompatible options, nucleus (B) remains. Additionally, RNA-binding + methyltransferase architecture is associated with nuclear RNA processing pathways.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific identity of the target RNA (U6 snRNA vs. cytoplasmic tRNA) would require item-specific knowledge, but since 'cytoplasm' is not among the options, the elimination-based reasoning suffices to select B.",
    "reason": "The domain architecture visible in the sequence (methyltransferase fold + RNA-binding THUMP domain) provides a concrete biological argument to eliminate options A, C, and D. The protein is clearly an enzyme acting on RNA, not a structural component of lipid droplets or the midbody, and it lacks HDAC domains. While positive identification of 'nucleus' over a hypothetical 'cytoplasm' would require knowing the specific RNA target, cytoplasm is not an option, so the elimination reasoning is sufficient and grounded in general biological knowledge of protein domain-function relationships."
  },
  "case_id": "GO_cellular_component_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E1B8U2 (THUMPD2_BOVIN) annotates SUBCELLULAR LOCATION as Nucleus (evidence ECO:0000250, inferred by similarity to human Q9BTF0) and carries GO:0005634 (nucleus, ISS). The protein is a U6 snRNA (guanine-N2)-methyltransferase; U6 snRNA is a nuclear spliceosomal RNA, making nuclear localization functionally consistent. The experimental IDA evidence supports membership in the 'tRNA methyltransferase complex' (GO:0043527), which is not among the options but is a nuclear complex. The nucleus annotation, while ISS-level, is well-supported by the protein's enzymatic function targeting a nuclear RNA."
  },
  "important_caveats": [
    "The 'nucleus' annotation in UniProt is ISS (inferred by similarity to human ortholog Q9BTF0), not directly experimental for the bovine protein. The direct experimental evidence (IDA) supports 'tRNA methyltransferase complex' (GO:0043527), which is not among the answer options.",
    "No classical bipartite NLS is easily identifiable in the sequence, so positive nuclear targeting cannot be confirmed purely from primary sequence inspection; the reasoning relies on elimination and functional inference.",
    "The protein's GO annotation includes 'tRNA methyltransferase complex' (IDA), which could arguably be a more precise sub-compartment answer, but it is not offered as an option."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by protein domain architecture. Only 'nucleus' is compatible with an RNA methyltransferase bearing a THUMP domain. The histone deacetylase complex requires a completely different fold, and lipid droplet/midbody are incompatible with an enzymatic protein lacking any structural or lipid-handling domains."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E1B8U2 (THUMPD2_BOVIN) annotates SUBCELLULAR LOCATION as Nucleus (evidence ECO:0000250, inferred by similarity to human Q9BTF0) and carries GO:0005634 (nucleus, ISS). The protein is a U6 snRNA (guanine-N2)-methyltransferase; U6 snRNA is a nuclear spliceosomal RNA, making nuclear localization functionally consistent. The experimental IDA evidence supports membership in the 'tRNA methyltransferase complex' (GO:0043527), which is not among the options but is a nuclear complex. The nucleus annotation, while ISS-level, is well-supported by the protein's enzymatic function targeting a nuclear RNA.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold-like methyltransferase domain (the region with conserved motifs around 'VSCRCSGAVAKTLTAQEVGRVIGIALMKQFGWKADLRNPNLEIFIHLSDVYSVLGIPVFRVPLACRAYIKTAGLRSTIAWAMASLAEIKAGAVVLDPMCGLGTILLEAAKEWPHVYYVGADVSDSQLSGAYDNLRAAGLRDKIELLQVSVIELPLPSESVDIIISDIPFGKKFKLGKDIKRMLQEMERVLRVGGTIVLLLS') and an RNA-binding THUMP domain. This domain architecture identifies the protein as an RNA-modifying enzyme, which is incompatible with lipid droplet (C: no lipid-handling domains) and midbody (D: no cytoskeletal/structural domains). The protein lacks the metalloprotease-like HDAC fold, eliminating the histone deacetylase complex (A). By elimination of three clearly incompatible options, nucleus (B) remains. Additionally, RNA-binding + methyltransferase architecture is associated with nuclear RNA processing pathways.",
    "missing_item_specific_fact": "The specific identity of the target RNA (U6 snRNA vs. cytoplasmic tRNA) would require item-specific knowledge, but since 'cytoplasm' is not among the options, the elimination-based reasoning suffices to select B.",
    "reason": "The domain architecture visible in the sequence (methyltransferase fold + RNA-binding THUMP domain) provides a concrete biological argument to eliminate options A, C, and D. The protein is clearly an enzyme acting on RNA, not a structural component of lipid droplets or the midbody, and it lacks HDAC domains. While positive identification of 'nucleus' over a hypothetical 'cytoplasm' would require knowing the specific RNA target, cytoplasm is not an option, so the elimination reasoning is sufficient and grounded in general biological knowledge of protein domain-function relationships."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by protein domain architecture. Only 'nucleus' is compatible with an RNA methyltransferase bearing a THUMP domain. The histone deacetylase complex requires a completely different fold, and lipid droplet/midbody are incompatible with an enzymatic protein lacking any structural or lipid-handling domains."
  },
  "important_caveats": [
    "The 'nucleus' annotation in UniProt is ISS (inferred by similarity to human ortholog Q9BTF0), not directly experimental for the bovine protein. The direct experimental evidence (IDA) supports 'tRNA methyltransferase complex' (GO:0043527), which is not among the answer options.",
    "No classical bipartite NLS is easily identifiable in the sequence, so positive nuclear targeting cannot be confirmed purely from primary sequence inspection; the reasoning relies on elimination and functional inference.",
    "The protein's GO annotation includes 'tRNA methyltransferase complex' (IDA), which could arguably be a more precise sub-compartment answer, but it is not offered as an option."
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

**Accession:** `E1B8U2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 75. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1B8U2.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.727150+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BTF0","source":"UniProtKB"}],"id":"SL-0191","value":"Nucleus"}}]}
```

Source SHA-256: `7d8384f3beab8a1b4abbbf3e032df29bf3d3b69d2a2be354db274e4785783a8c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1B8U2.json)  
**Locator:** `/uniProtKBCrossReferences/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.727150+00:00.  

```json
{"database":"GO","id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `7d8384f3beab8a1b4abbbf3e032df29bf3d3b69d2a2be354db274e4785783a8c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1B8U2.json)  
**Locator:** `/uniProtKBCrossReferences/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.727150+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"37283053","source":"PubMed"}],"id":"GO:0043527","properties":[{"key":"GoTerm","value":"C:tRNA methyltransferase complex"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `7d8384f3beab8a1b4abbbf3e032df29bf3d3b69d2a2be354db274e4785783a8c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1B8U2?format=txt&versions=75)  
**Locator:** `lines 55-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 3.  
**Retrieved:** 2026-11-02T04:28:00.166333+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000250|UniProtKB:Q9BTF0}.
```

Source SHA-256: `a3e60d058c163a299bc1c844e328bc89a6d6be1a998922d23673039dab32c748`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1B8U2?format=txt&versions=75)  
**Locator:** `lines 82-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 3.  
**Retrieved:** 2026-11-02T04:28:00.166333+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; ISS:UniProtKB.
```

Source SHA-256: `a3e60d058c163a299bc1c844e328bc89a6d6be1a998922d23673039dab32c748`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1B8U2?format=txt&versions=75)  
**Locator:** `lines 83-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 3.  
**Retrieved:** 2026-11-02T04:28:00.166333+00:00.  

```text
DR   GO; GO:0043527; C:tRNA methyltransferase complex; IDA:UniProtKB.
```

Source SHA-256: `a3e60d058c163a299bc1c844e328bc89a6d6be1a998922d23673039dab32c748`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
