# temperature_0002

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `temperature`  
**Author expected answer:** **B** — 35

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNRSDAYGYFRNQGREYVITTPRTPARWFNYLFNDTYYTEISQTGQGDSVAFRPHNRTLTRGFRYFYLKDLETGGTWSPLYQPLKTEPEAYECIHSLGTTEIRSVSQEIASSIHVFVPRAGQQEIWTVTLTNTGVKPRSLSLFTAFSLENGGVMGSKCQFDQESQILSSYSFPYHVTYGQKAGCDDHTNVVYVYPDYPADSYDCSQRAFFGGDDIYELPAAVQKGRCSGGQAEAENPLGALQQTITLEPGEQAVRHFVVGCASSLEEIRSSKAELAAKGYAVLLQETEDYWEGITGMFRVETPDDDVNAFMNIWLKKQIVMQTRTNRMSSYCPVRNQLQDALGYALVDPAGAAEYMISVLQGQERSGFIQQWIMTDGSPPKNLCLLKHTDGPVWLIICITALLNQCGDTELLQRQVGFKGSSDSATIYQHLLLAADYMAGETGAHGLCLMGDGDWNDPINGPGRLGRGESAWNTMALVYAIQALIPFCEQLGDTENAEQLNTVARRLADAVNRICWDGGWYVAGFDDDGTPFGTAQDEEGKLFLNTQTWAIMSGIASGERLDQCLAAIDSLDTPFGPRLLEPPFSGWNPKWGRISLKLAGTTENGSVYCHASMFKAFADCIAGRGSEAWQTISRTLPTNPDNPPGQNGQVPIFVPNYYFGLADSPNFGKSSHHVSTGTVGWMLWTTLEYALGIRATANGLKIDPCIPADWPEYTVERKYRSASYRIHVLNPSGISRGTVKVTVDGEAWMAAALPYEAGREYQVTVQLEQ

[Multiple Choices]
A. 36
B. 35
C. 29-38
D. 69
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Thermal Adaptation Prediction, which is to predict the thermal adaptation category of a protein. This relates to the optimal temperature range in which the protein is stable and functional (e.g., cold-adapted, moderate temperature-adapted, or heat-adapted). This property is encoded by subtle patterns in the amino acid sequence that affect the protein's structural stability, such as amino acid composition and the potential for internal bonds. Based on the provided sequence, you must classify the protein into its most likely thermal category.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry, which reports an optimum of 35 °C for reverse phosphorolytic activity, citing experimental evidence from PubMed 35947916. This supports choice B, though the cited paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and organism context may suggest a broadly moderate-temperature enzyme, but they do not meaningfully distinguish an optimum of 35 °C from 36 °C or establish the specific measured optimum.


**Missing item-specific fact**

> The experimentally reported temperature optimum for this protein’s reverse phosphorolytic activity is 35 °C.


**Reason**

> The supplied input gives no assay result or sufficiently discriminating sequence-based evidence for the precise value; choosing 35 over nearby temperatures depends on a protein-specific fact absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The task describes thermal-category prediction, but the options mix exact temperatures with a range. Since 35 °C falls within 29–38 °C, both B and C can fit unless the intended target is explicitly the exact optimum.


### Important caveats

- The reported optimum is qualified as applying to reverse phosphorolytic activity.
- The database annotation cites experimental evidence, but the primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and organism context may suggest a broadly moderate-temperature enzyme, but they do not meaningfully distinguish an optimum of 35 °C from 36 °C or establish the specific measured optimum.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally reported temperature optimum for this protein’s reverse phosphorolytic activity is 35 °C.",
    "reason": "The supplied input gives no assay result or sufficiently discriminating sequence-based evidence for the precise value; choosing 35 over nearby temperatures depends on a protein-specific fact absent from the input."
  },
  "case_id": "temperature_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which reports an optimum of 35 °C for reverse phosphorolytic activity, citing experimental evidence from PubMed 35947916. This supports choice B, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reported optimum is qualified as applying to reverse phosphorolytic activity.",
    "The database annotation cites experimental evidence, but the primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The task describes thermal-category prediction, but the options mix exact temperatures with a range. Since 35 °C falls within 29–38 °C, both B and C can fit unless the intended target is explicitly the exact optimum."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which reports an optimum of 35 °C for reverse phosphorolytic activity, citing experimental evidence from PubMed 35947916. This supports choice B, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and organism context may suggest a broadly moderate-temperature enzyme, but they do not meaningfully distinguish an optimum of 35 °C from 36 °C or establish the specific measured optimum.",
    "missing_item_specific_fact": "The experimentally reported temperature optimum for this protein’s reverse phosphorolytic activity is 35 °C.",
    "reason": "The supplied input gives no assay result or sufficiently discriminating sequence-based evidence for the precise value; choosing 35 over nearby temperatures depends on a protein-specific fact absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The task describes thermal-category prediction, but the options mix exact temperatures with a range. Since 35 °C falls within 29–38 °C, both B and C can fit unless the intended target is explicitly the exact optimum."
  },
  "important_caveats": [
    "The reported optimum is qualified as applying to reverse phosphorolytic activity.",
    "The database annotation cites experimental evidence, but the primary paper was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A089MMR2 (Paenibacillus borealis, sequence matched at 769 AA) contains an experimentally determined annotation (ECO:0000269, PubMed:35947916) stating: 'Optimum temperature is 35 degrees Celsius (for the reverse phosphorolytic activity).' The expected answer B (35) directly matches this experimental measurement. The sequence SHA256 matches the benchmark input.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can reason from the sequence and organism context to eliminate D (69°C) as thermophilic, since Paenibacillus species are mesophilic and the sequence lacks hallmark thermophilic adaptations (excessive charged residues, ionic network density). The organism name 'borealis' and stability data at 4°C hint at a cold-tolerant mesophile. However, distinguishing 35 from 36 degrees Celsius—or deciding between the precise value 35 and the range 29-38—requires knowledge of the specific experimental optimum measured for this protein.


**Missing item-specific fact**

> The exact experimentally determined optimum temperature of 35°C for this specific GH94 phosphorylase (PubMed:35947916), which cannot be derived from sequence composition, organism taxonomy, or general thermal-adaptation heuristics. No sequence feature uniquely encodes '35 rather than 36' or 'a point value rather than a range.'


**Reason**

> While general biological knowledge narrows the answer to a mesophilic range (eliminating 69°C), the precise distinction between 35, 36, and the range 29-38 depends entirely on the protein-specific experimental measurement. A trained model could memorize the UniProt annotation, but no sequence-based reasoning argument meaningfully separates 35 from 36 or from the encompassing range.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Option C (29-38) is a range that encompasses the experimentally determined optimum of 35°C. If the question asks for a 'thermal adaptation category,' a range description is arguably as valid as a point value. The distinction between B (35) and C (29-38) depends on whether the benchmark expects the exact optimum or a categorical range. Additionally, A (36) is within 1°C of the true optimum and within typical experimental error, though it is not the reported value.


### Important caveats

- The UniProt annotation specifies 35°C for the 'reverse phosphorolytic activity'—the forward reaction optimum could differ, though no alternative value is annotated.
- The evidence code ECO:0000269 confirms experimental determination (PubMed:35947916), not computational prediction.
- The question frames the task as predicting from sequence alone, but the correct answer is an item-specific experimental measurement not derivable from sequence features.
- Option C (29-38) could be considered a valid 'category' answer if the benchmark schema treats ranges as legitimate thermal-adaptation classifications.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can reason from the sequence and organism context to eliminate D (69°C) as thermophilic, since Paenibacillus species are mesophilic and the sequence lacks hallmark thermophilic adaptations (excessive charged residues, ionic network density). The organism name 'borealis' and stability data at 4°C hint at a cold-tolerant mesophile. However, distinguishing 35 from 36 degrees Celsius—or deciding between the precise value 35 and the range 29-38—requires knowledge of the specific experimental optimum measured for this protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact experimentally determined optimum temperature of 35°C for this specific GH94 phosphorylase (PubMed:35947916), which cannot be derived from sequence composition, organism taxonomy, or general thermal-adaptation heuristics. No sequence feature uniquely encodes '35 rather than 36' or 'a point value rather than a range.'",
    "reason": "While general biological knowledge narrows the answer to a mesophilic range (eliminating 69°C), the precise distinction between 35, 36, and the range 29-38 depends entirely on the protein-specific experimental measurement. A trained model could memorize the UniProt annotation, but no sequence-based reasoning argument meaningfully separates 35 from 36 or from the encompassing range."
  },
  "case_id": "temperature_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A089MMR2 (Paenibacillus borealis, sequence matched at 769 AA) contains an experimentally determined annotation (ECO:0000269, PubMed:35947916) stating: 'Optimum temperature is 35 degrees Celsius (for the reverse phosphorolytic activity).' The expected answer B (35) directly matches this experimental measurement. The sequence SHA256 matches the benchmark input."
  },
  "important_caveats": [
    "The UniProt annotation specifies 35°C for the 'reverse phosphorolytic activity'—the forward reaction optimum could differ, though no alternative value is annotated.",
    "The evidence code ECO:0000269 confirms experimental determination (PubMed:35947916), not computational prediction.",
    "The question frames the task as predicting from sequence alone, but the correct answer is an item-specific experimental measurement not derivable from sequence features.",
    "Option C (29-38) could be considered a valid 'category' answer if the benchmark schema treats ranges as legitimate thermal-adaptation classifications."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Option C (29-38) is a range that encompasses the experimentally determined optimum of 35°C. If the question asks for a 'thermal adaptation category,' a range description is arguably as valid as a point value. The distinction between B (35) and C (29-38) depends on whether the benchmark expects the exact optimum or a categorical range. Additionally, A (36) is within 1°C of the true optimum and within typical experimental error, though it is not the reported value."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A089MMR2 (Paenibacillus borealis, sequence matched at 769 AA) contains an experimentally determined annotation (ECO:0000269, PubMed:35947916) stating: 'Optimum temperature is 35 degrees Celsius (for the reverse phosphorolytic activity).' The expected answer B (35) directly matches this experimental measurement. The sequence SHA256 matches the benchmark input.",
    "evidence_ids": ["C5", "H3", "C6", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can reason from the sequence and organism context to eliminate D (69°C) as thermophilic, since Paenibacillus species are mesophilic and the sequence lacks hallmark thermophilic adaptations (excessive charged residues, ionic network density). The organism name 'borealis' and stability data at 4°C hint at a cold-tolerant mesophile. However, distinguishing 35 from 36 degrees Celsius—or deciding between the precise value 35 and the range 29-38—requires knowledge of the specific experimental optimum measured for this protein.",
    "missing_item_specific_fact": "The exact experimentally determined optimum temperature of 35°C for this specific GH94 phosphorylase (PubMed:35947916), which cannot be derived from sequence composition, organism taxonomy, or general thermal-adaptation heuristics. No sequence feature uniquely encodes '35 rather than 36' or 'a point value rather than a range.'",
    "reason": "While general biological knowledge narrows the answer to a mesophilic range (eliminating 69°C), the precise distinction between 35, 36, and the range 29-38 depends entirely on the protein-specific experimental measurement. A trained model could memorize the UniProt annotation, but no sequence-based reasoning argument meaningfully separates 35 from 36 or from the encompassing range."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Option C (29-38) is a range that encompasses the experimentally determined optimum of 35°C. If the question asks for a 'thermal adaptation category,' a range description is arguably as valid as a point value. The distinction between B (35) and C (29-38) depends on whether the benchmark expects the exact optimum or a categorical range. Additionally, A (36) is within 1°C of the true optimum and within typical experimental error, though it is not the reported value."
  },
  "important_caveats": [
    "The UniProt annotation specifies 35°C for the 'reverse phosphorolytic activity'—the forward reaction optimum could differ, though no alternative value is annotated.",
    "The evidence code ECO:0000269 confirms experimental determination (PubMed:35947916), not computational prediction.",
    "The question frames the task as predicting from sequence alone, but the correct answer is an item-specific experimental measurement not derivable from sequence features.",
    "Option C (29-38) could be considered a valid 'category' answer if the benchmark schema treats ranges as legitimate thermal-adaptation classifications."
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

**Accession:** `A0A089MMR2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.192125+00:00.  

```json
"A0A089MMR2"
```

Source SHA-256: `9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.192125+00:00.  

```json
{"commentType":"BIOPHYSICOCHEMICAL PROPERTIES","kineticParameters":{"michaelisConstants":[{"constant":7.89,"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"substrate":"3-O-beta-D-glucosyl-D-glucuronate","unit":"mM"},{"constant":1.52,"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"substrate":"phosphate","unit":"mM"},{"constant":1.57,"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"substrate":"alpha-D-glucose 1-phosphate","unit":"mM"},{"constant":11.7,"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"substrate":"D-glucuronic acid","unit":"mM"},{"constant":3.02,"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"substrate":"p-nitrophenyl-beta-D-glucuronide","unit":"mM"}],"note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"value":"kcat is 102 sec(-1) with O-beta-D-glucosyl-D-glucuronate as substrate (PubMed:35947916). kcat is 156 sec(-1) with alpha-D-glucose 1-phosphate as substrate (PubMed:35947916). kcat is 351 sec(-1) with D-glucuronic acid as substrate (PubMed:35947916). kcat is 433 sec(-1) with p-nitrophenyl-beta-D-glucuronide as substrate (PubMed:35947916)."}]}},"phDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"value":"Optimum pH is 6.9 (for the reverse phosphorolytic activity) (PubMed:35947916). Stable between pH 6.6 and 8.8 at 4 degrees Celsius for 24 hours (PubMed:35947916)."}]},"temperatureDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"value":"Optimum temperature is 35 degrees Celsius (for the reverse phosphorolytic activity) (PubMed:35947916). Retains more than 90% of its original activity after incubation at 30 degrees Celsius for 1 hour (PubMed:35947916)."}]}}
```

Source SHA-256: `9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.192125+00:00.  

```json
{"citation":{"authors":["Isono N.","Mizutani E.","Hayashida H.","Katsuzaki H.","Saburi W."],"citationCrossReferences":[{"database":"PubMed","id":"35947916"},{"database":"DOI","id":"10.1016/j.bbrc.2022.07.098"}],"citationType":"journal article","firstPage":"60","id":"35947916","journal":"Biochem. Biophys. Res. Commun.","lastPage":"65","publicationDate":"2022","title":"Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.","volume":"625"},"referenceComments":[{"type":"STRAIN","value":"DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT"]}
```

Source SHA-256: `9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)  
**Locator:** `lines 19-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:27:15.632691+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.
RC   STRAIN=DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19;
RX   PubMed=35947916; DOI=10.1016/j.bbrc.2022.07.098;
RA   Isono N., Mizutani E., Hayashida H., Katsuzaki H., Saburi W.;
RT   "Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-
RT   beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of
RT   the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.";
RL   Biochem. Biophys. Res. Commun. 625:60-65(2022).
```

Source SHA-256: `abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)  
**Locator:** `lines 53-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:27:15.632691+00:00.  

```text
CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:
CC       Kinetic parameters:
CC         KM=7.89 mM for 3-O-beta-D-glucosyl-D-glucuronate
CC         {ECO:0000269|PubMed:35947916};
CC         KM=1.52 mM for phosphate {ECO:0000269|PubMed:35947916};
CC         KM=1.57 mM for alpha-D-glucose 1-phosphate
CC         {ECO:0000269|PubMed:35947916};
CC         KM=11.7 mM for D-glucuronic acid {ECO:0000269|PubMed:35947916};
CC         KM=3.02 mM for p-nitrophenyl-beta-D-glucuronide
CC         {ECO:0000269|PubMed:35947916};
CC         Note=kcat is 102 sec(-1) with O-beta-D-glucosyl-D-glucuronate as
CC         substrate (PubMed:35947916). kcat is 156 sec(-1) with alpha-D-glucose
CC         1-phosphate as substrate (PubMed:35947916). kcat is 351 sec(-1) with
CC         D-glucuronic acid as substrate (PubMed:35947916). kcat is 433 sec(-1)
CC         with p-nitrophenyl-beta-D-glucuronide as substrate (PubMed:35947916).
CC         {ECO:0000269|PubMed:35947916};
CC       pH dependence:
CC         Optimum pH is 6.9 (for the reverse phosphorolytic activity)
CC         (PubMed:35947916). Stable between pH 6.6 and 8.8 at 4 degrees Celsius
CC         for 24 hours (PubMed:35947916). {ECO:0000269|PubMed:35947916};
CC       Temperature dependence:
CC         Optimum temperature is 35 degrees Celsius (for the reverse
CC         phosphorolytic activity) (PubMed:35947916). Retains more than 90% of
CC         its original activity after incubation at 30 degrees Celsius for 1
CC         hour (PubMed:35947916). {ECO:0000269|PubMed:35947916};
```

Source SHA-256: `abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
