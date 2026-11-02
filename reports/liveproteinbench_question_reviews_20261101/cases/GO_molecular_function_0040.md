# GO_molecular_function_0040

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — 2 iron, 2 sulfur cluster binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFNNFLNMYMCTLAEKLCKFKKNNFNNIHRNNNFYRDNNFYRDNNFYRDNNFYRDNNFYRDNNLYTNNNLYRDNNFYRDNNFYRDNNFYRDNNLYTNNNLYRDNNLYTNNNLYRDNNFYNITLRKFHFIQTISNNNFNFEIIKKYGDVINKIMFIHTQKKNKQERFMFNNKKYIKRKEYILNDLNEFISIIPHPEINNEITNNSNQKKNKDNKQNVLSTNQQIITNYNLNHKENVTSNLNFNNKEEDEKKLDKLLKKRNIKKRDIVTITEEAKEELKKIISINKKENNNNYNNMNTICSDNHNDMNTICNDKNILKLFFITKGCNGLTHSFNFISKKDIHKEDEIIYDDQNNILLVIDKNCILYVINTTLDYYKDDLTEKFIFKNPNITSICPCGTSFHFSKKK

[Multiple Choices]
A. RNA methyltransferase activity
B. protein heterodimerization activity
C. 2 iron, 2 sulfur cluster binding
D. guanyl-nucleotide exchange factor activity
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

> The sequence-matched UniProt record annotates 2 iron, 2 sulfur cluster binding (IBA), supporting C as a computationally inferred GO function. Experimental evidence reports binding and transfer of &#91;4Fe-4S&#93; clusters, which supports iron-sulfur cluster binding generally but does not itself establish binding specifically to a 2Fe-2S cluster.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The cysteine-containing sequence could suggest metal or iron-sulfur cluster involvement, making C plausible over RNA methyltransferase or guanyl-nucleotide exchange. But sequence composition alone does not establish the specific 2Fe-2S cluster binding activity.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence distinguishing 2Fe-2S binding from other iron-sulfur cluster interactions is absent from the question input.


**Reason**

> Choosing the precise GO term requires a protein-specific annotation or measurement; generic sequence clues can suggest metal binding but cannot uniquely establish the cluster type.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is the supported choice among the listed options, though its specific 2Fe-2S wording rests on an IBA annotation rather than the cited experimental evidence, which concerns &#91;4Fe-4S&#93; clusters.


### Important caveats

- The sequence match identifies a Plasmodium falciparum IscA2 entry, but that identity and its annotations were reviewer-only, not supplied to the evaluated model.
- The cited GO annotation is computationally inferred; it should not be represented as a direct experimental demonstration of 2Fe-2S binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The cysteine-containing sequence could suggest metal or iron-sulfur cluster involvement, making C plausible over RNA methyltransferase or guanyl-nucleotide exchange. But sequence composition alone does not establish the specific 2Fe-2S cluster binding activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence distinguishing 2Fe-2S binding from other iron-sulfur cluster interactions is absent from the question input.",
    "reason": "Choosing the precise GO term requires a protein-specific annotation or measurement; generic sequence clues can suggest metal binding but cannot uniquely establish the cluster type."
  },
  "case_id": "GO_molecular_function_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates 2 iron, 2 sulfur cluster binding (IBA), supporting C as a computationally inferred GO function. Experimental evidence reports binding and transfer of [4Fe-4S] clusters, which supports iron-sulfur cluster binding generally but does not itself establish binding specifically to a 2Fe-2S cluster."
  },
  "important_caveats": [
    "The sequence match identifies a Plasmodium falciparum IscA2 entry, but that identity and its annotations were reviewer-only, not supplied to the evaluated model.",
    "The cited GO annotation is computationally inferred; it should not be represented as a direct experimental demonstration of 2Fe-2S binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the supported choice among the listed options, though its specific 2Fe-2S wording rests on an IBA annotation rather than the cited experimental evidence, which concerns [4Fe-4S] clusters."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates 2 iron, 2 sulfur cluster binding (IBA), supporting C as a computationally inferred GO function. Experimental evidence reports binding and transfer of [4Fe-4S] clusters, which supports iron-sulfur cluster binding generally but does not itself establish binding specifically to a 2Fe-2S cluster.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The cysteine-containing sequence could suggest metal or iron-sulfur cluster involvement, making C plausible over RNA methyltransferase or guanyl-nucleotide exchange. But sequence composition alone does not establish the specific 2Fe-2S cluster binding activity.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence distinguishing 2Fe-2S binding from other iron-sulfur cluster interactions is absent from the question input.",
    "reason": "Choosing the precise GO term requires a protein-specific annotation or measurement; generic sequence clues can suggest metal binding but cannot uniquely establish the cluster type."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the supported choice among the listed options, though its specific 2Fe-2S wording rests on an IBA annotation rather than the cited experimental evidence, which concerns [4Fe-4S] clusters."
  },
  "important_caveats": [
    "The sequence match identifies a Plasmodium falciparum IscA2 entry, but that identity and its annotations were reviewer-only, not supplied to the evaluated model.",
    "The cited GO annotation is computationally inferred; it should not be represented as a direct experimental demonstration of 2Fe-2S binding."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry O97297 (ISCA2_PLAF7, Iron-sulfur assembly protein IscA2) carries GO:0051537 '2 iron, 2 sulfur cluster binding' as a molecular-function annotation (evidence code IBA:GO_Central, a computational inference). The protein is experimentally confirmed (PubMed:34032321, ECO:0000269) to participate in the ISC pathway for Fe-S cluster biogenesis and to bind/transfer &#91;4Fe-4S&#93; clusters. The 2Fe-2S annotation is database-supported, though the evidence code is computational (IBA) rather than direct experimental, and the experimental paper specifically describes &#91;4Fe-4S&#93; binding (GO:0051539, IEA). The annotation exists and is consistent with the protein's role as an ISC scaffold/carrying protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal region 'ITSICPCGTSFHFSKKK' contains a C-P-C (Cys-Pro-Cys) motif reminiscent of ferredoxin-type 2Fe-2S coordination, and the protein has sparse cysteine residues (including 'MNTICSDNHNDMNTICNDK'). Options A (RNA methyltransferase) and D (GEF) lack any recognizable catalytic or structural motifs in this sequence. However, the overwhelming Asn-rich character of the sequence (NNFYRDNNFYRDNN… repeats) makes motif identification extremely unreliable, and the CPC motif alone is insufficient to definitively distinguish option C from option B (protein heterodimerization), which is a generic binding activity not easily excluded from sequence alone.


**Missing item-specific fact**

> The identification of this specific 404-aa Asn-rich P. falciparum protein as IscA2, an ISC scaffold protein in the Fe-S cluster biogenesis pathway, is a database annotation fact (UniProt O97297). Without recognizing this protein or knowing the P. falciparum mitochondrial ISC pathway, the sparse Cys motifs embedded in Asn-rich repeats are too ambiguous to confidently assign Fe-S cluster binding over generic protein-protein interaction.


**Reason**

> While the C-terminal CPC motif provides a weak positive hint toward Fe-S binding, the sequence is dominated by Asn-rich repeats that obscure functional motifs. Reliably selecting C over B (heterodimerization) requires knowing this protein is IscA2, an ISC scaffold protein—a specific database/experimental annotation rather than a conclusion derivable from general sequence analysis of this atypical protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Option B (protein heterodimerization activity) is a generic molecular function that cannot be definitively excluded from sequence alone, especially for a protein whose ISC scaffold role involves protein-protein interactions. The 2Fe-2S annotation (C) carries only IBA (computational) evidence, while the experimental evidence (PubMed:34032321) specifically describes &#91;4Fe-4S&#93; binding (GO:0051539, annotated only as IEA). A reasonable analyst might question whether 2Fe-2S is the 'primary' molecular function versus 4Fe-4S binding, though 4Fe-4S is not among the options.


### Important caveats

- The GO:0051537 (2Fe-2S binding) annotation uses evidence code IBA:GO_Central, a computational inference, not direct experimental evidence.
- The experimental paper (Sadik et al., 2021, PubMed:34032321) specifically demonstrates &#91;4Fe-4S&#93; cluster binding and transfer, while 2Fe-2S binding is inferred by association.
- The protein sequence is extremely Asn-rich (hallmark of P. falciparum), making motif-based identification of Fe-S binding motifs unreliable without prior knowledge of the protein family.
- The protein also carries GO:0051539 (4Fe-4S cluster binding, IEA) and GO:0046872 (metal ion binding, IEA), indicating Fe-S binding is the broader functional category.
- The reviewer-only evidence establishes the protein identity (O97297/ISCA2_PLAF7) but this accession was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region 'ITSICPCGTSFHFSKKK' contains a C-P-C (Cys-Pro-Cys) motif reminiscent of ferredoxin-type 2Fe-2S coordination, and the protein has sparse cysteine residues (including 'MNTICSDNHNDMNTICNDK'). Options A (RNA methyltransferase) and D (GEF) lack any recognizable catalytic or structural motifs in this sequence. However, the overwhelming Asn-rich character of the sequence (NNFYRDNNFYRDNN… repeats) makes motif identification extremely unreliable, and the CPC motif alone is insufficient to definitively distinguish option C from option B (protein heterodimerization), which is a generic binding activity not easily excluded from sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this specific 404-aa Asn-rich P. falciparum protein as IscA2, an ISC scaffold protein in the Fe-S cluster biogenesis pathway, is a database annotation fact (UniProt O97297). Without recognizing this protein or knowing the P. falciparum mitochondrial ISC pathway, the sparse Cys motifs embedded in Asn-rich repeats are too ambiguous to confidently assign Fe-S cluster binding over generic protein-protein interaction.",
    "reason": "While the C-terminal CPC motif provides a weak positive hint toward Fe-S binding, the sequence is dominated by Asn-rich repeats that obscure functional motifs. Reliably selecting C over B (heterodimerization) requires knowing this protein is IscA2, an ISC scaffold protein—a specific database/experimental annotation rather than a conclusion derivable from general sequence analysis of this atypical protein."
  },
  "case_id": "GO_molecular_function_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry O97297 (ISCA2_PLAF7, Iron-sulfur assembly protein IscA2) carries GO:0051537 '2 iron, 2 sulfur cluster binding' as a molecular-function annotation (evidence code IBA:GO_Central, a computational inference). The protein is experimentally confirmed (PubMed:34032321, ECO:0000269) to participate in the ISC pathway for Fe-S cluster biogenesis and to bind/transfer [4Fe-4S] clusters. The 2Fe-2S annotation is database-supported, though the evidence code is computational (IBA) rather than direct experimental, and the experimental paper specifically describes [4Fe-4S] binding (GO:0051539, IEA). The annotation exists and is consistent with the protein's role as an ISC scaffold/carrying protein."
  },
  "important_caveats": [
    "The GO:0051537 (2Fe-2S binding) annotation uses evidence code IBA:GO_Central, a computational inference, not direct experimental evidence.",
    "The experimental paper (Sadik et al., 2021, PubMed:34032321) specifically demonstrates [4Fe-4S] cluster binding and transfer, while 2Fe-2S binding is inferred by association.",
    "The protein sequence is extremely Asn-rich (hallmark of P. falciparum), making motif-based identification of Fe-S binding motifs unreliable without prior knowledge of the protein family.",
    "The protein also carries GO:0051539 (4Fe-4S cluster binding, IEA) and GO:0046872 (metal ion binding, IEA), indicating Fe-S binding is the broader functional category.",
    "The reviewer-only evidence establishes the protein identity (O97297/ISCA2_PLAF7) but this accession was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Option B (protein heterodimerization activity) is a generic molecular function that cannot be definitively excluded from sequence alone, especially for a protein whose ISC scaffold role involves protein-protein interactions. The 2Fe-2S annotation (C) carries only IBA (computational) evidence, while the experimental evidence (PubMed:34032321) specifically describes [4Fe-4S] binding (GO:0051539, annotated only as IEA). A reasonable analyst might question whether 2Fe-2S is the 'primary' molecular function versus 4Fe-4S binding, though 4Fe-4S is not among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry O97297 (ISCA2_PLAF7, Iron-sulfur assembly protein IscA2) carries GO:0051537 '2 iron, 2 sulfur cluster binding' as a molecular-function annotation (evidence code IBA:GO_Central, a computational inference). The protein is experimentally confirmed (PubMed:34032321, ECO:0000269) to participate in the ISC pathway for Fe-S cluster biogenesis and to bind/transfer [4Fe-4S] clusters. The 2Fe-2S annotation is database-supported, though the evidence code is computational (IBA) rather than direct experimental, and the experimental paper specifically describes [4Fe-4S] binding (GO:0051539, IEA). The annotation exists and is consistent with the protein's role as an ISC scaffold/carrying protein.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal region 'ITSICPCGTSFHFSKKK' contains a C-P-C (Cys-Pro-Cys) motif reminiscent of ferredoxin-type 2Fe-2S coordination, and the protein has sparse cysteine residues (including 'MNTICSDNHNDMNTICNDK'). Options A (RNA methyltransferase) and D (GEF) lack any recognizable catalytic or structural motifs in this sequence. However, the overwhelming Asn-rich character of the sequence (NNFYRDNNFYRDNN… repeats) makes motif identification extremely unreliable, and the CPC motif alone is insufficient to definitively distinguish option C from option B (protein heterodimerization), which is a generic binding activity not easily excluded from sequence alone.",
    "missing_item_specific_fact": "The identification of this specific 404-aa Asn-rich P. falciparum protein as IscA2, an ISC scaffold protein in the Fe-S cluster biogenesis pathway, is a database annotation fact (UniProt O97297). Without recognizing this protein or knowing the P. falciparum mitochondrial ISC pathway, the sparse Cys motifs embedded in Asn-rich repeats are too ambiguous to confidently assign Fe-S cluster binding over generic protein-protein interaction.",
    "reason": "While the C-terminal CPC motif provides a weak positive hint toward Fe-S binding, the sequence is dominated by Asn-rich repeats that obscure functional motifs. Reliably selecting C over B (heterodimerization) requires knowing this protein is IscA2, an ISC scaffold protein—a specific database/experimental annotation rather than a conclusion derivable from general sequence analysis of this atypical protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Option B (protein heterodimerization activity) is a generic molecular function that cannot be definitively excluded from sequence alone, especially for a protein whose ISC scaffold role involves protein-protein interactions. The 2Fe-2S annotation (C) carries only IBA (computational) evidence, while the experimental evidence (PubMed:34032321) specifically describes [4Fe-4S] binding (GO:0051539, annotated only as IEA). A reasonable analyst might question whether 2Fe-2S is the 'primary' molecular function versus 4Fe-4S binding, though 4Fe-4S is not among the options."
  },
  "important_caveats": [
    "The GO:0051537 (2Fe-2S binding) annotation uses evidence code IBA:GO_Central, a computational inference, not direct experimental evidence.",
    "The experimental paper (Sadik et al., 2021, PubMed:34032321) specifically demonstrates [4Fe-4S] cluster binding and transfer, while 2Fe-2S binding is inferred by association.",
    "The protein sequence is extremely Asn-rich (hallmark of P. falciparum), making motif-based identification of Fe-S binding motifs unreliable without prior knowledge of the protein family.",
    "The protein also carries GO:0051539 (4Fe-4S cluster binding, IEA) and GO:0046872 (metal ion binding, IEA), indicating Fe-S binding is the broader functional category.",
    "The reviewer-only evidence establishes the protein identity (O97297/ISCA2_PLAF7) but this accession was not provided to the evaluated model."
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

**Accession:** `O97297` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 128. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Iron-sulfur assembly protein IscA2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34032321","source":"PubMed"}],"value":"PfIscA2"}]}}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34032321","source":"PubMed"}],"value":"Participates in iron-sulfur cluster formation (ISC) pathway for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Can bind and transfer [4Fe-4S] clusters to target apo-proteins (PubMed:34032321)"}]}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"database":"GO","id":"GO:0051537","properties":[{"key":"GoTerm","value":"F:2 iron, 2 sulfur cluster binding"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 78-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
CC   -!- FUNCTION: Participates in iron-sulfur cluster formation (ISC) pathway
CC       for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Can bind
CC       and transfer [4Fe-4S] clusters to target apo-proteins
CC       (PubMed:34032321). {ECO:0000269|PubMed:34032321}.
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 111-111`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
DR   GO; GO:0051537; F:2 iron, 2 sulfur cluster binding; IBA:GO_Central.
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 112-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
DR   GO; GO:0051539; F:4 iron, 4 sulfur cluster binding; IEA:UniProtKB-KW.
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 40. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
