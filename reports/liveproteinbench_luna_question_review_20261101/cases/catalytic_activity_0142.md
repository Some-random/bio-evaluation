# catalytic_activity_0142

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAARDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNEMGCFTYPLVPGFETVGIATEVGSKVTKMKVGDKVAVGIMVGSCGKCDDCVNDRECYCPEVITSYGRIDHDGTPTYGGFSNETVANEKFVFRFPEKLPMAAGAPLLNAGVSVYSPMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGADAFLVSTDAKQMQAGSGTLDGILDTVPVVHPIEPLLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVASTVGGSTTEAQEMLDFAAEHNITANVEIIPMDYINTAMERIEKNDVRYRFVIDVGNTLTPPES

[Multiple Choices]
A. benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-[protein] + CoA + H(+)
B. 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)
C. (2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl diphosphate
D. UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

## Luna’s full visible review

### Expected-answer support: supported

> The exact sequence matches a UniProt entry annotating choice B as a catalytic reaction, but that assignment is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence. The same entry reports experimental evidence for a different reaction, which does not contradict B.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could plausibly indicate an oxidoreductase, making the NADP-linked choice B more compatible than the transferase, terpene-cyclization, or sugar-decarboxylation choices. That broad class inference does not establish the specific substrates and products in B.

**Missing item-specific fact**

> The protein-specific catalytic annotation linking this sequence to the 17-O-acetylnorajmaline reaction.

**Reason**

> Choosing the exact transformation requires protein-specific functional information absent from the input; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Only choice B is supported by the supplied reviewer evidence as an annotation for the matching sequence; the separately reported experimental reaction is not among the options.

### Important caveats

- The choice-B annotation is transferred from a related UniProt entry, rather than directly experimentally established for this sequence in the cited annotation.
- The matching protein has experimental evidence for a distinct catalytic reaction, which does not by itself exclude the transferred choice-B activity.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating choice B as a catalytic reaction, but that assignment is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence. The same entry reports experimental evidence for a different reaction, which does not contradict B.",
    "evidence_ids": [
      "C1",
      "C5",
      "H4",
      "H5"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could plausibly indicate an oxidoreductase, making the NADP-linked choice B more compatible than the transferase, terpene-cyclization, or sugar-decarboxylation choices. That broad class inference does not establish the specific substrates and products in B.",
    "missing_item_specific_fact": "The protein-specific catalytic annotation linking this sequence to the 17-O-acetylnorajmaline reaction.",
    "reason": "Choosing the exact transformation requires protein-specific functional information absent from the input; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice B is supported by the supplied reviewer evidence as an annotation for the matching sequence; the separately reported experimental reaction is not among the options."
  },
  "important_caveats": [
    "The choice-B annotation is transferred from a related UniProt entry, rather than directly experimentally established for this sequence in the cited annotation.",
    "The matching protein has experimental evidence for a distinct catalytic reaction, which does not by itself exclude the transferred choice-B activity."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A0U4BHM2`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 30. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.340033+00:00.  

```json
"A0A0U4BHM2"
```

Source SHA-256: `c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.340033+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0U3S9Q3","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:12322"}}],"reaction":{"ecNumber":"1.3.1.73","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0U3S9Q3","source":"UniProtKB"}],"name":"17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:12320"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17372"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:77725"}]}}
```

Source SHA-256: `c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)  
**Locator:** `lines 39-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:25.840272+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine
CC         + NADPH + 2 H(+); Xref=Rhea:RHEA:12320, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:17372, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349,
CC         ChEBI:CHEBI:77725; EC=1.3.1.73;
CC         Evidence={ECO:0000250|UniProtKB:A0A0U3S9Q3};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:12322;
CC         Evidence={ECO:0000250|UniProtKB:A0A0U3S9Q3};
```

Source SHA-256: `f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)  
**Locator:** `lines 47-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:25.840272+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH +
CC         H(+); Xref=Rhea:RHEA:79635, ChEBI:CHEBI:15378, ChEBI:CHEBI:16408,
CC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349, ChEBI:CHEBI:230482;
CC         Evidence={ECO:0000269|PubMed:26715562};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:79637;
CC         Evidence={ECO:0000269|PubMed:26715562};
```

Source SHA-256: `f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 142). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
