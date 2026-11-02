# EC_number_0063

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.1.1.336

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNQFNKVCVIGLGYIGLPTAAIFASRKIKVIGVDINQNIVDIINKGKIHIVEPGLDILVHMVVNDGYLKATTLPEEADAFIIAVPTPFKGDNHEPNLDYIEMASKAIAKVLKKGNLVILESTSPVGTTEQMAKWLAEERSDLSFPHQCGEVSDIKIAHCPERVLPGQVIRELVENDRIIGGMTQKCAEYAIRLYKIFVQGECIMTNARTAEMTKLTENSFRDLNIAFANELSILCDKLDINVWELIKLANRHPRVNILQPGCGVGGHCIAVDPWFIVYQNPNEAKIIKTAREVNDNKPNFVVQKIKKKIKDILGPKIACLGLAFKPDIDDLRESPALDIVIKLASENASQILVVEPNIKQLPLKLQNKRNIKLVCLSQALDEADVVAVLVRHKEFIEVQSDKVVSFC

[Multiple Choices]
A. 1.1.1.122
B. 2.3.1.319
C. 3.6.1.5
D. 1.1.1.336
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated with EC 1.1.1.336, and the catalytic-activity annotation cites experimental evidence for the reaction assigned that EC number.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich sequence is compatible with a nucleotide-cofactor-binding oxidoreductase, which may broadly favor EC 1.1.1 choices over the transferase and hydrolase options. It does not distinguish the specific substrate activity represented by 1.1.1.336 from the other dehydrogenase choice.


**Missing item-specific fact**

> The enzyme's specific catalytic activity—oxidation of UDP-N-acetyl-D-mannosamine to UDP-N-acetyl-D-mannosaminouronate—is not supplied and is needed to identify EC 1.1.1.336.


**Reason**

> The sequence may support a broad enzyme-family inference, but the exact EC choice depends on protein-specific substrate and reaction annotation or experimental knowledge absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports one EC number for this protein, but the sequence and choices alone do not provide enough information to distinguish the closely related oxidoreductase options.


### Important caveats

- Reviewer-only UniProt evidence matches the supplied sequence, including a historical sequence match; the author's exact source snapshot is unknown.
- The EC annotation cites experimental evidence in a 2024 publication, but that primary paper was not independently retrieved or validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich sequence is compatible with a nucleotide-cofactor-binding oxidoreductase, which may broadly favor EC 1.1.1 choices over the transferase and hydrolase options. It does not distinguish the specific substrate activity represented by 1.1.1.336 from the other dehydrogenase choice.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's specific catalytic activity—oxidation of UDP-N-acetyl-D-mannosamine to UDP-N-acetyl-D-mannosaminouronate—is not supplied and is needed to identify EC 1.1.1.336.",
    "reason": "The sequence may support a broad enzyme-family inference, but the exact EC choice depends on protein-specific substrate and reaction annotation or experimental knowledge absent from the question."
  },
  "case_id": "EC_number_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with EC 1.1.1.336, and the catalytic-activity annotation cites experimental evidence for the reaction assigned that EC number."
  },
  "important_caveats": [
    "Reviewer-only UniProt evidence matches the supplied sequence, including a historical sequence match; the author's exact source snapshot is unknown.",
    "The EC annotation cites experimental evidence in a 2024 publication, but that primary paper was not independently retrieved or validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one EC number for this protein, but the sequence and choices alone do not provide enough information to distinguish the closely related oxidoreductase options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with EC 1.1.1.336, and the catalytic-activity annotation cites experimental evidence for the reaction assigned that EC number.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich sequence is compatible with a nucleotide-cofactor-binding oxidoreductase, which may broadly favor EC 1.1.1 choices over the transferase and hydrolase options. It does not distinguish the specific substrate activity represented by 1.1.1.336 from the other dehydrogenase choice.",
    "missing_item_specific_fact": "The enzyme's specific catalytic activity—oxidation of UDP-N-acetyl-D-mannosamine to UDP-N-acetyl-D-mannosaminouronate—is not supplied and is needed to identify EC 1.1.1.336.",
    "reason": "The sequence may support a broad enzyme-family inference, but the exact EC choice depends on protein-specific substrate and reaction annotation or experimental knowledge absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one EC number for this protein, but the sequence and choices alone do not provide enough information to distinguish the closely related oxidoreductase options."
  },
  "important_caveats": [
    "Reviewer-only UniProt evidence matches the supplied sequence, including a historical sequence match; the author's exact source snapshot is unknown.",
    "The EC annotation cites experimental evidence in a 2024 publication, but that primary paper was not independently retrieved or validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0U3AB61 (exact sequence match, 407 aa, Campylobacter jejuni) is annotated as UDP-N-acetyl-D-mannosamine dehydrogenase with EC 1.1.1.336, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic reaction (UDP-N-acetyl-alpha-D-mannosamine + 2 NAD+ + H2O → UDP-N-acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H+) confirms an oxidoreductase acting on CH-OH group with NAD+ as acceptor, consistent with EC 1.1.1.336.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal GLGYIGLP motif contains a GxGxxG Rossmann-fold pattern indicative of an NAD-binding oxidoreductase, which reasonably eliminates option B (transferase, EC 2) and option C (hydrolase, EC 3). However, both remaining options A (1.1.1.122) and D (1.1.1.336) are oxidoreductases acting on CH-OH donors with NAD+ as acceptor. Distinguishing between them requires knowing the specific substrate (UDP-N-acetyl-D-mannosamine vs. the substrate of 1.1.1.122), which is a protein-specific annotation fact not derivable from the sequence alone.


**Missing item-specific fact**

> The specific substrate identity and enzyme family assignment (UDP-sugar dehydrogenase vs. the enzyme class for EC 1.1.1.122) that distinguishes the fourth digit of the EC number. No obvious UDP-sugar-binding motif or family-specific signature in the sequence unambiguously separates 1.1.1.122 from 1.1.1.336 without prior knowledge of this particular enzyme.


**Reason**

> While the Rossmann fold narrows the answer to EC 1.1.1.x, the final distinction between two specific EC 1.1.1.x numbers depends on identifying the exact substrate, which is an item-specific annotation fact. The sequence does not contain a clearly recognizable UDP-sugar-binding domain motif that would allow a model to confidently select 336 over 122 through general reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (1.1.1.122) and D (1.1.1.336) are NAD-dependent oxidoreductases acting on CH-OH groups. Without the specific substrate annotation, a model relying solely on sequence features (Rossmann fold, length, overall composition) cannot confidently exclude one in favor of the other. The distinction rests on knowing the exact enzymatic reaction.


### Important caveats

- The EC 1.1.1.336 annotation is backed by experimental evidence (ECO:0000269, PubMed:38382015, 2024 Biochemistry paper), not merely computational inference.
- The Rossmann-fold motif (GLGYIGLP) provides partial reasoning support for the oxidoreductase class (EC 1.1.1.x) but not for the specific fourth digit.
- The sequence match between the benchmark input and UniProt A0A0U3AB61 is exact (SHA256 confirmed), so the annotation applies directly to this sequence.
- EC 1.1.1.122 as a distractor: its exact substrate identity should be verified; if it represents a structurally very different enzyme family, additional sequence-based reasoning might partially favor D, but this was not clearly demonstrable from the supplied sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal GLGYIGLP motif contains a GxGxxG Rossmann-fold pattern indicative of an NAD-binding oxidoreductase, which reasonably eliminates option B (transferase, EC 2) and option C (hydrolase, EC 3). However, both remaining options A (1.1.1.122) and D (1.1.1.336) are oxidoreductases acting on CH-OH donors with NAD+ as acceptor. Distinguishing between them requires knowing the specific substrate (UDP-N-acetyl-D-mannosamine vs. the substrate of 1.1.1.122), which is a protein-specific annotation fact not derivable from the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity and enzyme family assignment (UDP-sugar dehydrogenase vs. the enzyme class for EC 1.1.1.122) that distinguishes the fourth digit of the EC number. No obvious UDP-sugar-binding motif or family-specific signature in the sequence unambiguously separates 1.1.1.122 from 1.1.1.336 without prior knowledge of this particular enzyme.",
    "reason": "While the Rossmann fold narrows the answer to EC 1.1.1.x, the final distinction between two specific EC 1.1.1.x numbers depends on identifying the exact substrate, which is an item-specific annotation fact. The sequence does not contain a clearly recognizable UDP-sugar-binding domain motif that would allow a model to confidently select 336 over 122 through general reasoning alone."
  },
  "case_id": "EC_number_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3AB61 (exact sequence match, 407 aa, Campylobacter jejuni) is annotated as UDP-N-acetyl-D-mannosamine dehydrogenase with EC 1.1.1.336, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic reaction (UDP-N-acetyl-alpha-D-mannosamine + 2 NAD+ + H2O → UDP-N-acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H+) confirms an oxidoreductase acting on CH-OH group with NAD+ as acceptor, consistent with EC 1.1.1.336."
  },
  "important_caveats": [
    "The EC 1.1.1.336 annotation is backed by experimental evidence (ECO:0000269, PubMed:38382015, 2024 Biochemistry paper), not merely computational inference.",
    "The Rossmann-fold motif (GLGYIGLP) provides partial reasoning support for the oxidoreductase class (EC 1.1.1.x) but not for the specific fourth digit.",
    "The sequence match between the benchmark input and UniProt A0A0U3AB61 is exact (SHA256 confirmed), so the annotation applies directly to this sequence.",
    "EC 1.1.1.122 as a distractor: its exact substrate identity should be verified; if it represents a structurally very different enzyme family, additional sequence-based reasoning might partially favor D, but this was not clearly demonstrable from the supplied sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (1.1.1.122) and D (1.1.1.336) are NAD-dependent oxidoreductases acting on CH-OH groups. Without the specific substrate annotation, a model relying solely on sequence features (Rossmann fold, length, overall composition) cannot confidently exclude one in favor of the other. The distinction rests on knowing the exact enzymatic reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3AB61 (exact sequence match, 407 aa, Campylobacter jejuni) is annotated as UDP-N-acetyl-D-mannosamine dehydrogenase with EC 1.1.1.336, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic reaction (UDP-N-acetyl-alpha-D-mannosamine + 2 NAD+ + H2O → UDP-N-acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H+) confirms an oxidoreductase acting on CH-OH group with NAD+ as acceptor, consistent with EC 1.1.1.336.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal GLGYIGLP motif contains a GxGxxG Rossmann-fold pattern indicative of an NAD-binding oxidoreductase, which reasonably eliminates option B (transferase, EC 2) and option C (hydrolase, EC 3). However, both remaining options A (1.1.1.122) and D (1.1.1.336) are oxidoreductases acting on CH-OH donors with NAD+ as acceptor. Distinguishing between them requires knowing the specific substrate (UDP-N-acetyl-D-mannosamine vs. the substrate of 1.1.1.122), which is a protein-specific annotation fact not derivable from the sequence alone.",
    "missing_item_specific_fact": "The specific substrate identity and enzyme family assignment (UDP-sugar dehydrogenase vs. the enzyme class for EC 1.1.1.122) that distinguishes the fourth digit of the EC number. No obvious UDP-sugar-binding motif or family-specific signature in the sequence unambiguously separates 1.1.1.122 from 1.1.1.336 without prior knowledge of this particular enzyme.",
    "reason": "While the Rossmann fold narrows the answer to EC 1.1.1.x, the final distinction between two specific EC 1.1.1.x numbers depends on identifying the exact substrate, which is an item-specific annotation fact. The sequence does not contain a clearly recognizable UDP-sugar-binding domain motif that would allow a model to confidently select 336 over 122 through general reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (1.1.1.122) and D (1.1.1.336) are NAD-dependent oxidoreductases acting on CH-OH groups. Without the specific substrate annotation, a model relying solely on sequence features (Rossmann fold, length, overall composition) cannot confidently exclude one in favor of the other. The distinction rests on knowing the exact enzymatic reaction."
  },
  "important_caveats": [
    "The EC 1.1.1.336 annotation is backed by experimental evidence (ECO:0000269, PubMed:38382015, 2024 Biochemistry paper), not merely computational inference.",
    "The Rossmann-fold motif (GLGYIGLP) provides partial reasoning support for the oxidoreductase class (EC 1.1.1.x) but not for the specific fourth digit.",
    "The sequence match between the benchmark input and UniProt A0A0U3AB61 is exact (SHA256 confirmed), so the annotation applies directly to this sequence.",
    "EC 1.1.1.122 as a distractor: its exact substrate identity should be verified; if it represents a structurally very different enzyme family, additional sequence-based reasoning might partially favor D, but this was not clearly demonstrable from the supplied sequence alone."
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

**Accession:** `A0A0U3AB61` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 20. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.671066+00:00.  

```json
"A0A0U3AB61"
```

Source SHA-256: `1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.671066+00:00.  

```json
{"lineage":["Bacteria","Pseudomonadati","Campylobacterota","Epsilonproteobacteria","Campylobacterales","Campylobacteraceae","Campylobacter"],"scientificName":"Campylobacter jejuni","taxonId":197}
```

Source SHA-256: `1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.671066+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"UDP-ManNAc 6-dehydrogenase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"1.1.1.336"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-D-mannosamine dehydrogenase"}}}
```

Source SHA-256: `1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.671066+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:25781"}}],"reaction":{"ecNumber":"1.1.1.336","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O = UDP-N-acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:25780"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:68623"},{"database":"ChEBI","id":"CHEBI:70731"}]}}
```

Source SHA-256: `1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.671066+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"HS:11"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-01T06:27:21.162556+00:00.  

```text
ID   UAMDH_CAMJU             Reviewed;         407 AA.
AC   A0A0U3AB61;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-MAR-2016, sequence version 1.
DT   28-JAN-2026, entry version 20.
DE   RecName: Full=UDP-N-acetyl-D-mannosamine dehydrogenase {ECO:0000305};
DE            EC=1.1.1.336 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=UDP-ManNAc 6-dehydrogenase {ECO:0000303|PubMed:38382015};
GN   Name=HS11.16 {ECO:0000303|PubMed:38382015};
OS   Campylobacter jejuni.
OC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;
OC   Campylobacterales; Campylobacteraceae; Campylobacter.
OX   NCBI_TaxID=197;
```

Source SHA-256: `d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-01T06:27:21.162556+00:00.  

```text
DE   RecName: Full=UDP-N-acetyl-D-mannosamine dehydrogenase {ECO:0000305};
DE            EC=1.1.1.336 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=UDP-ManNAc 6-dehydrogenase {ECO:0000303|PubMed:38382015};
```

Source SHA-256: `d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)  
**Locator:** `lines 29-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-01T06:27:21.162556+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.
RC   STRAIN=HS:11;
RX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;
RA   Ghosh M.K., Raushel F.M.;
RT   "Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-
RT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter
RT   jejuni.";
RL   Biochemistry 63:688-698(2024).
```

Source SHA-256: `d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)  
**Locator:** `lines 43-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-01T06:27:21.162556+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O = UDP-N-
CC         acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+);
CC         Xref=Rhea:RHEA:25780, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:68623,
CC         ChEBI:CHEBI:70731; EC=1.1.1.336;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:25781;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 63. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
