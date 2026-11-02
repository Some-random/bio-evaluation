# GO_molecular_function_0147

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — 2 iron, 2 sulfur cluster binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKSKILCNLFKGKSCICLYTNCLNENNVNKCYYNLVRNYSDHVKDHFNKPRNVGSFDKNEKNIGTSIVGKASCGDVIKLQLKIENDVIKDARFMAFGCGSAIASSSYATELIKGKTIDEALKIKNNDIASHLSLPPVKIHCSLLAEDAIKHAIKNYREKVLT

[Multiple Choices]
A. estradiol 17-beta-dehydrogenase [NAD(P)+] activity
B. tau protein binding
C. beta-amyrin synthase activity
D. 2 iron, 2 sulfur cluster binding
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

> The sequence matches the UniProt entry annotated with GO:0051537, the exact term in choice D. That annotation is IBA (computational inference). Experimental evidence supports this protein's role in Fe-S cluster assembly, including assembly and transfer of &#91;4Fe-4S&#93; clusters, but does not directly establish binding to a 2Fe-2S cluster.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's cysteine-rich region is suggestive of an Fe-S-associated protein and makes D more plausible than the unrelated enzyme activities. But cysteine richness alone does not establish the specific 2Fe-2S binding activity named in D.


**Missing item-specific fact**

> The protein-specific GO:0051537 annotation or equivalent evidence assigning 2Fe-2S binding; that annotation is not provided in the question.


**Reason**

> The sequence offers a broad clue to Fe-S involvement, but identifying this protein and its specific GO annotation requires item-specific information. The experimental function cited in reviewer-only evidence supports Fe-S assembly, particularly involving 4Fe-4S clusters, rather than directly resolving the exact 2Fe-2S term.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D is supported by the matching protein annotation among the listed options. However, the exact 2Fe-2S specificity is inferred by annotation rather than directly demonstrated by the cited experimental function.


### Important caveats

- The sequence match and GO annotation support the key, but the GO evidence code IBA denotes computational inference, not direct experimental evidence.
- Experimental evidence for 4Fe-4S assembly does not itself prove 2Fe-2S binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's cysteine-rich region is suggestive of an Fe-S-associated protein and makes D more plausible than the unrelated enzyme activities. But cysteine richness alone does not establish the specific 2Fe-2S binding activity named in D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific GO:0051537 annotation or equivalent evidence assigning 2Fe-2S binding; that annotation is not provided in the question.",
    "reason": "The sequence offers a broad clue to Fe-S involvement, but identifying this protein and its specific GO annotation requires item-specific information. The experimental function cited in reviewer-only evidence supports Fe-S assembly, particularly involving 4Fe-4S clusters, rather than directly resolving the exact 2Fe-2S term."
  },
  "case_id": "GO_molecular_function_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated with GO:0051537, the exact term in choice D. That annotation is IBA (computational inference). Experimental evidence supports this protein's role in Fe-S cluster assembly, including assembly and transfer of [4Fe-4S] clusters, but does not directly establish binding to a 2Fe-2S cluster."
  },
  "important_caveats": [
    "The sequence match and GO annotation support the key, but the GO evidence code IBA denotes computational inference, not direct experimental evidence.",
    "Experimental evidence for 4Fe-4S assembly does not itself prove 2Fe-2S binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D is supported by the matching protein annotation among the listed options. However, the exact 2Fe-2S specificity is inferred by annotation rather than directly demonstrated by the cited experimental function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated with GO:0051537, the exact term in choice D. That annotation is IBA (computational inference). Experimental evidence supports this protein's role in Fe-S cluster assembly, including assembly and transfer of [4Fe-4S] clusters, but does not directly establish binding to a 2Fe-2S cluster.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's cysteine-rich region is suggestive of an Fe-S-associated protein and makes D more plausible than the unrelated enzyme activities. But cysteine richness alone does not establish the specific 2Fe-2S binding activity named in D.",
    "missing_item_specific_fact": "The protein-specific GO:0051537 annotation or equivalent evidence assigning 2Fe-2S binding; that annotation is not provided in the question.",
    "reason": "The sequence offers a broad clue to Fe-S involvement, but identifying this protein and its specific GO annotation requires item-specific information. The experimental function cited in reviewer-only evidence supports Fe-S assembly, particularly involving 4Fe-4S clusters, rather than directly resolving the exact 2Fe-2S term."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D is supported by the matching protein annotation among the listed options. However, the exact 2Fe-2S specificity is inferred by annotation rather than directly demonstrated by the cited experimental function."
  },
  "important_caveats": [
    "The sequence match and GO annotation support the key, but the GO evidence code IBA denotes computational inference, not direct experimental evidence.",
    "Experimental evidence for 4Fe-4S assembly does not itself prove 2Fe-2S binding."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q8IKT4, PfIscU from Plasmodium falciparum) is annotated with GO:0051537 '2 iron, 2 sulfur cluster binding' via IBA:GO_Central (C6, H4). The protein is experimentally confirmed (ECO:0000269, PubMed:34032321) as a scaffold for &#91;Fe-S&#93; cluster assembly. While the direct experimental evidence emphasizes &#91;4Fe-4S&#93; assembly, IscU proteins are well-known to transiently bind 2Fe-2S clusters during the assembly pathway, making the 2Fe-2S annotation biologically consistent. The GO term is present in the database annotation for this exact sequence (matched). The IBA evidence code indicates computational inference rather than direct measurement, but the annotation is not contradicted by the experimental data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 162-residue sequence contains an unusually high number of cysteine residues (~9, roughly 5.5% cysteine content, well above the typical 1-2% for most proteins), particularly clustered in the N-terminal region. Cysteine is the primary coordinating ligand for iron-sulfur clusters in proteins. Among the four options, only D (2Fe-2S cluster binding) involves a function that requires cysteine-mediated metal coordination. Option A (estradiol dehydrogenase) is a Rossmann-fold oxidoreductase, Option B (tau binding) involves cytoskeletal protein-protein interactions, and Option C (beta-amyrin synthase) is a large oxidosqualene cyclase — none of which are characterized by cysteine-rich sequences. The visible cysteine density in the input provides a general biological argument favoring Fe-S cluster binding over the other three choices.


**Missing item-specific fact**

> The specific distinction between 2Fe-2S and 4Fe-4S binding for this particular IscU scaffold requires annotation-level knowledge (the experimental data in PubMed:34032321 emphasizes 4Fe-4S assembly; the 2Fe-2S annotation is IBA-inferred). However, since 4Fe-4S binding is not among the options, the general Fe-S reasoning suffices to select D over A, B, and C.


**Reason**

> The cysteine-rich composition is directly observable in the supplied sequence and connects via general biochemistry to Fe-S cluster binding. This meaningfully distinguishes D from the three non-Fe-S options without requiring memorization of the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other three options (steroid dehydrogenase, tau binding, oxidosqualene cyclase) have no plausible connection to a cysteine-rich 162-residue protein. Only D involves iron-sulfur cluster chemistry. No alternative option is defensible given the sequence composition.


### Important caveats

- The GO:0051537 annotation is via IBA (Inferred by Biological Aspect), a computational inference method, not direct experimental measurement for this specific protein.
- The primary experimental evidence (PubMed:34032321, ECO:0000269) describes &#91;4Fe-4S&#93; cluster assembly by PfIscU; the 2Fe-2S assignment is a secondary annotation consistent with the known IscU mechanism but not the headline experimental finding.
- The sequence identity to Q8IKT4 was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence without accession context.
- The high cysteine count in the N-terminal region is atypical even for Fe-S proteins and may reflect the unusual Plasmodium IscU structure; however, it still supports the Fe-S binding interpretation over the other three options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 162-residue sequence contains an unusually high number of cysteine residues (~9, roughly 5.5% cysteine content, well above the typical 1-2% for most proteins), particularly clustered in the N-terminal region. Cysteine is the primary coordinating ligand for iron-sulfur clusters in proteins. Among the four options, only D (2Fe-2S cluster binding) involves a function that requires cysteine-mediated metal coordination. Option A (estradiol dehydrogenase) is a Rossmann-fold oxidoreductase, Option B (tau binding) involves cytoskeletal protein-protein interactions, and Option C (beta-amyrin synthase) is a large oxidosqualene cyclase — none of which are characterized by cysteine-rich sequences. The visible cysteine density in the input provides a general biological argument favoring Fe-S cluster binding over the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific distinction between 2Fe-2S and 4Fe-4S binding for this particular IscU scaffold requires annotation-level knowledge (the experimental data in PubMed:34032321 emphasizes 4Fe-4S assembly; the 2Fe-2S annotation is IBA-inferred). However, since 4Fe-4S binding is not among the options, the general Fe-S reasoning suffices to select D over A, B, and C.",
    "reason": "The cysteine-rich composition is directly observable in the supplied sequence and connects via general biochemistry to Fe-S cluster binding. This meaningfully distinguishes D from the three non-Fe-S options without requiring memorization of the specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein (Q8IKT4, PfIscU from Plasmodium falciparum) is annotated with GO:0051537 '2 iron, 2 sulfur cluster binding' via IBA:GO_Central (C6, H4). The protein is experimentally confirmed (ECO:0000269, PubMed:34032321) as a scaffold for [Fe-S] cluster assembly. While the direct experimental evidence emphasizes [4Fe-4S] assembly, IscU proteins are well-known to transiently bind 2Fe-2S clusters during the assembly pathway, making the 2Fe-2S annotation biologically consistent. The GO term is present in the database annotation for this exact sequence (matched). The IBA evidence code indicates computational inference rather than direct measurement, but the annotation is not contradicted by the experimental data."
  },
  "important_caveats": [
    "The GO:0051537 annotation is via IBA (Inferred by Biological Aspect), a computational inference method, not direct experimental measurement for this specific protein.",
    "The primary experimental evidence (PubMed:34032321, ECO:0000269) describes [4Fe-4S] cluster assembly by PfIscU; the 2Fe-2S assignment is a secondary annotation consistent with the known IscU mechanism but not the headline experimental finding.",
    "The sequence identity to Q8IKT4 was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence without accession context.",
    "The high cysteine count in the N-terminal region is atypical even for Fe-S proteins and may reflect the unusual Plasmodium IscU structure; however, it still supports the Fe-S binding interpretation over the other three options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other three options (steroid dehydrogenase, tau binding, oxidosqualene cyclase) have no plausible connection to a cysteine-rich 162-residue protein. Only D involves iron-sulfur cluster chemistry. No alternative option is defensible given the sequence composition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q8IKT4, PfIscU from Plasmodium falciparum) is annotated with GO:0051537 '2 iron, 2 sulfur cluster binding' via IBA:GO_Central (C6, H4). The protein is experimentally confirmed (ECO:0000269, PubMed:34032321) as a scaffold for [Fe-S] cluster assembly. While the direct experimental evidence emphasizes [4Fe-4S] assembly, IscU proteins are well-known to transiently bind 2Fe-2S clusters during the assembly pathway, making the 2Fe-2S annotation biologically consistent. The GO term is present in the database annotation for this exact sequence (matched). The IBA evidence code indicates computational inference rather than direct measurement, but the annotation is not contradicted by the experimental data.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 162-residue sequence contains an unusually high number of cysteine residues (~9, roughly 5.5% cysteine content, well above the typical 1-2% for most proteins), particularly clustered in the N-terminal region. Cysteine is the primary coordinating ligand for iron-sulfur clusters in proteins. Among the four options, only D (2Fe-2S cluster binding) involves a function that requires cysteine-mediated metal coordination. Option A (estradiol dehydrogenase) is a Rossmann-fold oxidoreductase, Option B (tau binding) involves cytoskeletal protein-protein interactions, and Option C (beta-amyrin synthase) is a large oxidosqualene cyclase — none of which are characterized by cysteine-rich sequences. The visible cysteine density in the input provides a general biological argument favoring Fe-S cluster binding over the other three choices.",
    "missing_item_specific_fact": "The specific distinction between 2Fe-2S and 4Fe-4S binding for this particular IscU scaffold requires annotation-level knowledge (the experimental data in PubMed:34032321 emphasizes 4Fe-4S assembly; the 2Fe-2S annotation is IBA-inferred). However, since 4Fe-4S binding is not among the options, the general Fe-S reasoning suffices to select D over A, B, and C.",
    "reason": "The cysteine-rich composition is directly observable in the supplied sequence and connects via general biochemistry to Fe-S cluster binding. This meaningfully distinguishes D from the three non-Fe-S options without requiring memorization of the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other three options (steroid dehydrogenase, tau binding, oxidosqualene cyclase) have no plausible connection to a cysteine-rich 162-residue protein. Only D involves iron-sulfur cluster chemistry. No alternative option is defensible given the sequence composition."
  },
  "important_caveats": [
    "The GO:0051537 annotation is via IBA (Inferred by Biological Aspect), a computational inference method, not direct experimental measurement for this specific protein.",
    "The primary experimental evidence (PubMed:34032321, ECO:0000269) describes [4Fe-4S] cluster assembly by PfIscU; the 2Fe-2S assignment is a secondary annotation consistent with the known IscU mechanism but not the headline experimental finding.",
    "The sequence identity to Q8IKT4 was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence without accession context.",
    "The high cysteine count in the N-terminal region is atypical even for Fe-S proteins and may reflect the unusual Plasmodium IscU structure; however, it still supports the Fe-S binding interpretation over the other three options."
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

**Accession:** `Q8IKT4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 123. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.665288+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Iron-sulfur cluster assembly protein IscU"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34032321","source":"PubMed"}],"value":"PfIscU"}]}}
```

Source SHA-256: `df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.665288+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34032321","source":"PubMed"}],"value":"Participates in iron-sulfur cluster formation (ISC) pathway for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Plays a role of a major scaffold protein for [Fe-S] assembly; assembles [4Fe-4S] clusters directly upon interaction with the catalytic component IscS-Isd11 as part of the scaffold complex (PubMed:34032321). Can transfer [4Fe-4S] clusters to target apo-proteins (PubMed:34032321)"}]}
```

Source SHA-256: `df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)  
**Locator:** `/uniProtKBCrossReferences/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.665288+00:00.  

```json
{"database":"GO","id":"GO:0051537","properties":[{"key":"GoTerm","value":"F:2 iron, 2 sulfur cluster binding"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)  
**Locator:** `lines 45-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 123 / 1.  
**Retrieved:** 2026-11-02T04:32:21.146174+00:00.  

```text
CC   -!- FUNCTION: Participates in iron-sulfur cluster formation (ISC) pathway
CC       for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Plays a
CC       role of a major scaffold protein for [Fe-S] assembly; assembles [4Fe-
CC       4S] clusters directly upon interaction with the catalytic component
CC       IscS-Isd11 as part of the scaffold complex (PubMed:34032321). Can
CC       transfer [4Fe-4S] clusters to target apo-proteins (PubMed:34032321).
CC       {ECO:0000269|PubMed:34032321}.
```

Source SHA-256: `1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)  
**Locator:** `lines 91-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 123 / 1.  
**Retrieved:** 2026-11-02T04:32:21.146174+00:00.  

```text
DR   GO; GO:0051537; F:2 iron, 2 sulfur cluster binding; IBA:GO_Central.
```

Source SHA-256: `1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 327878-327891`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0051537
name: 2 iron, 2 sulfur cluster binding
namespace: molecular_function
def: "Binding to a 2 iron, 2 sulfur (2Fe-2S) cluster; this cluster consists of two iron atoms, with two inorganic sulfur atoms found between the irons and acting as bridging ligands." [GOC:ai, PMID:15952888, Wikipedia:Iron-sulfur_cluster]
synonym: "2 Fe 2 S cluster binding" EXACT []
synonym: "2 iron, 2 sulphur cluster binding" EXACT []
synonym: "2Fe-2S cluster binding" EXACT []
synonym: "diiron disulfide cluster binding" EXACT []
synonym: "diiron disulphide cluster binding" EXACT []
synonym: "iron-sulfur cluster 2Fe-2S binding" EXACT []
synonym: "iron-sulphur cluster 2Fe-2S binding" EXACT []
is_a: GO:0051536 ! iron-sulfur cluster binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
