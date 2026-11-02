# pathway_0108

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Metabolic intermediate biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSYGESHGKAIGCVIDGFLSNIEINFDLIQKQLDRRRPNQSKLTSNRNEKDKLVILSGFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQVSKELENKNPPSRDLVDSYGTVRYNEKEKIFMDCFNRIYDMNASMLKTDEYNKNTLTIPSIDNTYINVKTNECNINQVDNNHNNYINDKDNTFNNSEKSDEWIYLQTRCPHPYTAVQICSYILKLKNKGDSVGGIATCIIQNPPIGIGEPIFDKLEAELAKMILSIPAVKGIEFGSGFNGTYMFGSMHNDIFIPVENMSTKKESDLLYDDKGECKNMSYHSTIQNNEDQILNSTKGFMPPKNDKNFNNIDDYNVTFNNNEEKLLITKTNNCGGILAGISTGNNIVFRSAIKPVSSIQIEKETSDFYGNMCNLKVQGRHDSCILPRLPPIIEASSSMVIGDLILRQISKYGDKKLPTLFRNM

[Multiple Choices]
A. Metabolic intermediate biosynthesis
B. Amino-acid degradation
C. protein glycosylation. .
D. chorismate biosynthesis
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

> The exact sequence matches a Plasmodium falciparum UniProt entry annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis, specifically chorismate biosynthesis. The pathway annotation is transferred by similarity (ECO:0000250), while cited studies support the enzyme’s identity and catalytic activity; this supports A without making the pathway annotation itself direct experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options do not provide enough context to infer the protein’s specific function from general pathway knowledge alone. Identifying chorismate synthase would distinguish the relevant pathway, but that requires a protein-specific functional identification.


**Missing item-specific fact**

> That this sequence encodes chorismate synthase, an enzyme functioning in chorismate biosynthesis.


**Reason**

> The input supplies only the sequence and broad pathway choices. Recognizing or recalling this particular protein’s annotation is an item-specific fact, not a pathway distinction established by the supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> The annotated pathway is chorismate biosynthesis, which is a type of metabolic intermediate biosynthesis. Thus A is the broader pathway category and D names the specific pathway; the choices do not make those levels mutually exclusive.


### Important caveats

- The sequence matches the cited UniProt record, but the pathway annotation is similarity-transferred rather than presented as direct experimental pathway evidence.
- The cited characterization includes a Plasmodium falciparum strain; it should not be treated as proof that this exact sequence was the experimentally tested construct.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options do not provide enough context to infer the protein’s specific function from general pathway knowledge alone. Identifying chorismate synthase would distinguish the relevant pathway, but that requires a protein-specific functional identification.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence encodes chorismate synthase, an enzyme functioning in chorismate biosynthesis.",
    "reason": "The input supplies only the sequence and broad pathway choices. Recognizing or recalling this particular protein’s annotation is an item-specific fact, not a pathway distinction established by the supplied context."
  },
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a Plasmodium falciparum UniProt entry annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis, specifically chorismate biosynthesis. The pathway annotation is transferred by similarity (ECO:0000250), while cited studies support the enzyme’s identity and catalytic activity; this supports A without making the pathway annotation itself direct experimental evidence."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the pathway annotation is similarity-transferred rather than presented as direct experimental pathway evidence.",
    "The cited characterization includes a Plasmodium falciparum strain; it should not be treated as proof that this exact sequence was the experimentally tested construct."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "The annotated pathway is chorismate biosynthesis, which is a type of metabolic intermediate biosynthesis. Thus A is the broader pathway category and D names the specific pathway; the choices do not make those levels mutually exclusive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a Plasmodium falciparum UniProt entry annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis, specifically chorismate biosynthesis. The pathway annotation is transferred by similarity (ECO:0000250), while cited studies support the enzyme’s identity and catalytic activity; this supports A without making the pathway annotation itself direct experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options do not provide enough context to infer the protein’s specific function from general pathway knowledge alone. Identifying chorismate synthase would distinguish the relevant pathway, but that requires a protein-specific functional identification.",
    "missing_item_specific_fact": "That this sequence encodes chorismate synthase, an enzyme functioning in chorismate biosynthesis.",
    "reason": "The input supplies only the sequence and broad pathway choices. Recognizing or recalling this particular protein’s annotation is an item-specific fact, not a pathway distinction established by the supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "The annotated pathway is chorismate biosynthesis, which is a type of metabolic intermediate biosynthesis. Thus A is the broader pathway category and D names the specific pathway; the choices do not make those levels mutually exclusive."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the pathway annotation is similarity-transferred rather than presented as direct experimental pathway evidence.",
    "The cited characterization includes a Plasmodium falciparum strain; it should not be treated as proof that this exact sequence was the experimentally tested construct."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt pathway annotation for C6KT66 (AROC_PLAF7, chorismate synthase from P. falciparum) explicitly states: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' Option A ('Metabolic intermediate biosynthesis') is the top-level super-pathway listed in this annotation, so it is technically present. However, option D ('chorismate biosynthesis') is the more specific and functionally precise pathway designation also explicitly stated in the same annotation. The key is supported but arguably imprecise relative to D.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No concrete sequence-derived argument from the 527-aa sequence alone meaningfully distinguishes chorismate synthase (and thus chorismate biosynthesis) from the other options. Chorismate synthase is a flavin-dependent enzyme with a specific structural fold, but recognizing this from raw sequence without database lookup requires specialized prior knowledge of the exact protein identity. None of the four options can be eliminated or confirmed through general biological reasoning applied to the sequence features visible in the input.


**Missing item-specific fact**

> The specific identity of this sequence as Plasmodium falciparum chorismate synthase (C6KT66/AROC_PLAF7) and its UniProt pathway annotation. Without knowing the protein's identity, a model cannot determine which of the four pathways it participates in.


**Reason**

> The question requires recognizing an exact 527-aa sequence and recalling its database pathway annotation. No general biological reasoning from sequence motifs, composition, or length reliably distinguishes chorismate synthase from a generic metabolic enzyme, a glycosylation factor, or an amino-acid degradation enzyme. This is a protein-identification lookup task dressed as a pathway-prediction task.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> The UniProt pathway annotation is hierarchical: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; …step 7/7.' Both A (the super-pathway) and D (the specific pathway) are explicitly stated. The question asks for the 'primary metabolic or signaling pathway,' which could reasonably refer to either the broad category (A) or the specific pathway (D). In standard biochemical usage, 'chorismate biosynthesis' (D) is the more precise and commonly cited pathway name for this enzyme, making D arguably the better answer. The author's selection of A over D is defensible only if one interprets 'primary' as the top-level UniProt category, but this is not clearly indicated in the question.


### Important caveats

- The pathway annotation is transferred by similarity (ECO:0000250|UniProtKB:Q12640), not independently experimentally verified for this specific Plasmodium entry, though the protein's chorismate synthase function is experimentally confirmed (PubMed 11298276, 31381947).
- The protein also has a second EC number (1.5.1.38, a bifunctional activity per PubMed 31381947), but this does not change the pathway assignment.
- The author key (A) is the super-pathway label; D (chorismate biosynthesis) is the specific pathway and is the more natural answer to 'primary pathway' in most biochemical contexts. This creates a genuine ambiguity that could mislead a well-reasoning model.
- All reviewer evidence is from UniProt annotations; the evaluated model had access only to the raw sequence and the four options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No concrete sequence-derived argument from the 527-aa sequence alone meaningfully distinguishes chorismate synthase (and thus chorismate biosynthesis) from the other options. Chorismate synthase is a flavin-dependent enzyme with a specific structural fold, but recognizing this from raw sequence without database lookup requires specialized prior knowledge of the exact protein identity. None of the four options can be eliminated or confirmed through general biological reasoning applied to the sequence features visible in the input.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this sequence as Plasmodium falciparum chorismate synthase (C6KT66/AROC_PLAF7) and its UniProt pathway annotation. Without knowing the protein's identity, a model cannot determine which of the four pathways it participates in.",
    "reason": "The question requires recognizing an exact 527-aa sequence and recalling its database pathway annotation. No general biological reasoning from sequence motifs, composition, or length reliably distinguishes chorismate synthase from a generic metabolic enzyme, a glycosylation factor, or an amino-acid degradation enzyme. This is a protein-identification lookup task dressed as a pathway-prediction task."
  },
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for C6KT66 (AROC_PLAF7, chorismate synthase from P. falciparum) explicitly states: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' Option A ('Metabolic intermediate biosynthesis') is the top-level super-pathway listed in this annotation, so it is technically present. However, option D ('chorismate biosynthesis') is the more specific and functionally precise pathway designation also explicitly stated in the same annotation. The key is supported but arguably imprecise relative to D."
  },
  "important_caveats": [
    "The pathway annotation is transferred by similarity (ECO:0000250|UniProtKB:Q12640), not independently experimentally verified for this specific Plasmodium entry, though the protein's chorismate synthase function is experimentally confirmed (PubMed 11298276, 31381947).",
    "The protein also has a second EC number (1.5.1.38, a bifunctional activity per PubMed 31381947), but this does not change the pathway assignment.",
    "The author key (A) is the super-pathway label; D (chorismate biosynthesis) is the specific pathway and is the more natural answer to 'primary pathway' in most biochemical contexts. This creates a genuine ambiguity that could mislead a well-reasoning model.",
    "All reviewer evidence is from UniProt annotations; the evaluated model had access only to the raw sequence and the four options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "The UniProt pathway annotation is hierarchical: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; …step 7/7.' Both A (the super-pathway) and D (the specific pathway) are explicitly stated. The question asks for the 'primary metabolic or signaling pathway,' which could reasonably refer to either the broad category (A) or the specific pathway (D). In standard biochemical usage, 'chorismate biosynthesis' (D) is the more precise and commonly cited pathway name for this enzyme, making D arguably the better answer. The author's selection of A over D is defensible only if one interprets 'primary' as the top-level UniProt category, but this is not clearly indicated in the question."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for C6KT66 (AROC_PLAF7, chorismate synthase from P. falciparum) explicitly states: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' Option A ('Metabolic intermediate biosynthesis') is the top-level super-pathway listed in this annotation, so it is technically present. However, option D ('chorismate biosynthesis') is the more specific and functionally precise pathway designation also explicitly stated in the same annotation. The key is supported but arguably imprecise relative to D.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No concrete sequence-derived argument from the 527-aa sequence alone meaningfully distinguishes chorismate synthase (and thus chorismate biosynthesis) from the other options. Chorismate synthase is a flavin-dependent enzyme with a specific structural fold, but recognizing this from raw sequence without database lookup requires specialized prior knowledge of the exact protein identity. None of the four options can be eliminated or confirmed through general biological reasoning applied to the sequence features visible in the input.",
    "missing_item_specific_fact": "The specific identity of this sequence as Plasmodium falciparum chorismate synthase (C6KT66/AROC_PLAF7) and its UniProt pathway annotation. Without knowing the protein's identity, a model cannot determine which of the four pathways it participates in.",
    "reason": "The question requires recognizing an exact 527-aa sequence and recalling its database pathway annotation. No general biological reasoning from sequence motifs, composition, or length reliably distinguishes chorismate synthase from a generic metabolic enzyme, a glycosylation factor, or an amino-acid degradation enzyme. This is a protein-identification lookup task dressed as a pathway-prediction task."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "The UniProt pathway annotation is hierarchical: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; …step 7/7.' Both A (the super-pathway) and D (the specific pathway) are explicitly stated. The question asks for the 'primary metabolic or signaling pathway,' which could reasonably refer to either the broad category (A) or the specific pathway (D). In standard biochemical usage, 'chorismate biosynthesis' (D) is the more precise and commonly cited pathway name for this enzyme, making D arguably the better answer. The author's selection of A over D is defensible only if one interprets 'primary' as the top-level UniProt category, but this is not clearly indicated in the question."
  },
  "important_caveats": [
    "The pathway annotation is transferred by similarity (ECO:0000250|UniProtKB:Q12640), not independently experimentally verified for this specific Plasmodium entry, though the protein's chorismate synthase function is experimentally confirmed (PubMed 11298276, 31381947).",
    "The protein also has a second EC number (1.5.1.38, a bifunctional activity per PubMed 31381947), but this does not change the pathway assignment.",
    "The author key (A) is the super-pathway label; D (chorismate biosynthesis) is the specific pathway and is the more natural answer to 'primary pathway' in most biochemical contexts. This creates a genuine ambiguity that could mislead a well-reasoning model.",
    "All reviewer evidence is from UniProt annotations; the evaluated model had access only to the raw sequence and the four options."
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

**Accession:** `C6KT66` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 89. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
"C6KT66"
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"31381947","source":"PubMed"}],"value":"1.5.1.38"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"11298276","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"value":"4.2.3.5"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"11298276","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"31381947","source":"PubMed"}],"value":"Chorismate synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11298276","source":"PubMed"}],"value":"PfCS"}]}}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q12640","source":"UniProtKB"}],"value":"Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7"}]}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"citation":{"authors":["Fitzpatrick T.","Ricken S.","Lanzer M.","Amrhein N.","Macheroux P.","Kappes B."],"citationCrossReferences":[{"database":"PubMed","id":"11298276"},{"database":"DOI","id":"10.1046/j.1365-2958.2001.02366.x"}],"citationType":"journal article","firstPage":"65","id":"11298276","journal":"Mol. Microbiol.","lastPage":"75","publicationDate":"2001","title":"Subcellular localization and characterization of chorismate synthase in the apicomplexan Plasmodium falciparum.","volume":"40"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11298276","source":"PubMed"}],"type":"STRAIN","value":"DD2"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBCELLULAR LOCATION","DEVELOPMENTAL STAGE"]}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
CC   -!- PATHWAY: Metabolic intermediate biosynthesis; chorismate biosynthesis;
CC       chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step
CC       7/7. {ECO:0000250|UniProtKB:Q12640}.
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
