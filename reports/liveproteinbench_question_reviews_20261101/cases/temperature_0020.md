# temperature_0020

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `temperature`  
**Author expected answer:** **D** — 55-60

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGRNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAINSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPESYSNFFGVAYDTPPKAHALKASRLLVPTTVARPSKPVRVFASTADPGTTTADQVYKVGHNLLLAHAAAIQVYRDKFQNTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQLLGPRLREFTPDQKKLLIGSYDYVGVNYYTATYVSSAQPPHDKKKAVFHTDGNFYTTDSKDGVLIGPLAGPAWLNIVPEGIYHVLQDIKENYEDPVIYITENGVYEVNDTAKTLSEARVDTTRLHYLQDHLSKVLEARHQGVRVQGYLVWSLMDNWELRAGYTSRFGLIHIDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKARPQEDDGAFDTPRKRLRKY

[Multiple Choices]
A. 23-35
B. 49-55
C. 30-43
D. 55-60
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

> The exact supplied sequence matches the UniProt entry, whose temperature-dependence annotation reports an optimum of 55–60 °C and cites experimental evidence (ECO:0000269, PubMed:18927081). The historical entry also matches the sequence. This supports choice D, though the cited primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No supplied context or sequence feature reliably distinguishes these precise temperature ranges; broad sequence-based thermal tendencies would not establish this enzyme's measured optimum.


**Missing item-specific fact**

> The protein-specific optimum temperature reported for this enzyme in the cited experimental study.


**Reason**

> Selecting D depends on an external experimental annotation or equivalent item-specific knowledge, not a defensible inference from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The intervals share the endpoint 55 °C, so a reported optimum at 55 °C fits both B and D. The evidence gives a 55–60 °C range, supporting D as written, but the choices are not mutually exclusive at that boundary.


### Important caveats

- The temperature annotation is experimental-coded and cites PubMed:18927081, but the primary paper was not independently retrieved or validated.
- An enzyme's reported optimum can depend on assay conditions and substrate; the annotation is not a general measure of organismal thermal adaptation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No supplied context or sequence feature reliably distinguishes these precise temperature ranges; broad sequence-based thermal tendencies would not establish this enzyme's measured optimum.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific optimum temperature reported for this enzyme in the cited experimental study.",
    "reason": "Selecting D depends on an external experimental annotation or equivalent item-specific knowledge, not a defensible inference from the sequence alone."
  },
  "case_id": "temperature_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry, whose temperature-dependence annotation reports an optimum of 55–60 °C and cites experimental evidence (ECO:0000269, PubMed:18927081). The historical entry also matches the sequence. This supports choice D, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The temperature annotation is experimental-coded and cites PubMed:18927081, but the primary paper was not independently retrieved or validated.",
    "An enzyme's reported optimum can depend on assay conditions and substrate; the annotation is not a general measure of organismal thermal adaptation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The intervals share the endpoint 55 °C, so a reported optimum at 55 °C fits both B and D. The evidence gives a 55–60 °C range, supporting D as written, but the choices are not mutually exclusive at that boundary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry, whose temperature-dependence annotation reports an optimum of 55–60 °C and cites experimental evidence (ECO:0000269, PubMed:18927081). The historical entry also matches the sequence. This supports choice D, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No supplied context or sequence feature reliably distinguishes these precise temperature ranges; broad sequence-based thermal tendencies would not establish this enzyme's measured optimum.",
    "missing_item_specific_fact": "The protein-specific optimum temperature reported for this enzyme in the cited experimental study.",
    "reason": "Selecting D depends on an external experimental annotation or equivalent item-specific knowledge, not a defensible inference from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The intervals share the endpoint 55 °C, so a reported optimum at 55 °C fits both B and D. The evidence gives a 55–60 °C range, supporting D as written, but the choices are not mutually exclusive at that boundary."
  },
  "important_caveats": [
    "The temperature annotation is experimental-coded and cites PubMed:18927081, but the primary paper was not independently retrieved or validated.",
    "An enzyme's reported optimum can depend on assay conditions and substrate; the annotation is not a general measure of organismal thermal adaptation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry B6ZKM3 (IpeGLU1, Ipecoside beta-D-glucosidase from Carapichea ipecacuanha) explicitly states 'Optimum temperature is 55-60 degrees Celsius' with evidence code ECO:0000269 (direct assay) from PubMed:18927081 (Nomura et al., JBC 2008). The benchmark sequence SHA256 matches the UniProt canonical sequence exactly (543 AA). The experimental measurement directly supports choice D.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a GH1 beta-glucosidase from a tropical plant. While one might note that glycoside hydrolase family 1 enzymes span a wide thermal range, and that the sequence contains features common to mesophilic-to-moderately-thermostable enzymes (e.g., moderate proline content, no extreme salt-bridge networks typical of >70°C thermophiles), no general sequence-composition rule reliably distinguishes a 49-55°C optimum from a 55-60°C optimum. Both ranges fall in the 'heat-adapted' category, and the 5-degree boundary between options B and D corresponds to a fine experimental distinction that cannot be resolved by amino-acid composition heuristics, isoelectric-point estimation, or loop-length analysis.


**Missing item-specific fact**

> The experimentally measured optimum temperature of 55-60°C for this specific IpeGLU1 enzyme (from the 2008 JBC assay by Nomura et al.) is the item-specific fact required to select D over B. No general biological principle applied to the 543-residue sequence can distinguish 49-55 from 55-60°C with the precision the question demands.


**Reason**

> The question requires choosing between two adjacent 'heat-adapted' ranges (49-55 vs 55-60°C). While the sequence could support a broad inference that the protein is not cold-adapted (ruling out A) and possibly not merely moderate (arguing against C), the fine distinction between B and D depends entirely on the specific experimental measurement for this enzyme. A model would need to recognize the exact sequence as IpeGLU1 and recall its published optimum temperature, which constitutes lookup/memorization rather than reasoning from sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Options B (49-55°C) and D (55-60°C) are adjacent ranges both representing heat-adapted enzymes. Without the specific experimental datum, a model analyzing sequence composition could reasonably argue for either range based on general thermostability indicators. The 5°C boundary between them is not marked by any identifiable sequence signature.


### Important caveats

- The 55-60°C optimum is an in vitro enzymatic assay result (ECO:0000269, direct assay), not an organismal environmental temperature. The source organism (Carapichea ipecacuanha) is a tropical plant that would never experience 55-60°C in vivo.
- The reviewer-only evidence confirms the key is correct, but this information was not available to the evaluated model.
- The question framing ('subtle patterns in the amino acid sequence that affect the protein's structural stability') implies sequence-based reasoning is expected, yet the required precision (5°C range distinction) exceeds what such reasoning can deliver.
- The UniProt entry was first publicly released in June 2025; the underlying experimental data dates to 2008. The annotation itself is experimental, not computational inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a GH1 beta-glucosidase from a tropical plant. While one might note that glycoside hydrolase family 1 enzymes span a wide thermal range, and that the sequence contains features common to mesophilic-to-moderately-thermostable enzymes (e.g., moderate proline content, no extreme salt-bridge networks typical of >70°C thermophiles), no general sequence-composition rule reliably distinguishes a 49-55°C optimum from a 55-60°C optimum. Both ranges fall in the 'heat-adapted' category, and the 5-degree boundary between options B and D corresponds to a fine experimental distinction that cannot be resolved by amino-acid composition heuristics, isoelectric-point estimation, or loop-length analysis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally measured optimum temperature of 55-60°C for this specific IpeGLU1 enzyme (from the 2008 JBC assay by Nomura et al.) is the item-specific fact required to select D over B. No general biological principle applied to the 543-residue sequence can distinguish 49-55 from 55-60°C with the precision the question demands.",
    "reason": "The question requires choosing between two adjacent 'heat-adapted' ranges (49-55 vs 55-60°C). While the sequence could support a broad inference that the protein is not cold-adapted (ruling out A) and possibly not merely moderate (arguing against C), the fine distinction between B and D depends entirely on the specific experimental measurement for this enzyme. A model would need to recognize the exact sequence as IpeGLU1 and recall its published optimum temperature, which constitutes lookup/memorization rather than reasoning from sequence features."
  },
  "case_id": "temperature_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry B6ZKM3 (IpeGLU1, Ipecoside beta-D-glucosidase from Carapichea ipecacuanha) explicitly states 'Optimum temperature is 55-60 degrees Celsius' with evidence code ECO:0000269 (direct assay) from PubMed:18927081 (Nomura et al., JBC 2008). The benchmark sequence SHA256 matches the UniProt canonical sequence exactly (543 AA). The experimental measurement directly supports choice D."
  },
  "important_caveats": [
    "The 55-60°C optimum is an in vitro enzymatic assay result (ECO:0000269, direct assay), not an organismal environmental temperature. The source organism (Carapichea ipecacuanha) is a tropical plant that would never experience 55-60°C in vivo.",
    "The reviewer-only evidence confirms the key is correct, but this information was not available to the evaluated model.",
    "The question framing ('subtle patterns in the amino acid sequence that affect the protein's structural stability') implies sequence-based reasoning is expected, yet the required precision (5°C range distinction) exceeds what such reasoning can deliver.",
    "The UniProt entry was first publicly released in June 2025; the underlying experimental data dates to 2008. The annotation itself is experimental, not computational inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Options B (49-55°C) and D (55-60°C) are adjacent ranges both representing heat-adapted enzymes. Without the specific experimental datum, a model analyzing sequence composition could reasonably argue for either range based on general thermostability indicators. The 5°C boundary between them is not marked by any identifiable sequence signature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry B6ZKM3 (IpeGLU1, Ipecoside beta-D-glucosidase from Carapichea ipecacuanha) explicitly states 'Optimum temperature is 55-60 degrees Celsius' with evidence code ECO:0000269 (direct assay) from PubMed:18927081 (Nomura et al., JBC 2008). The benchmark sequence SHA256 matches the UniProt canonical sequence exactly (543 AA). The experimental measurement directly supports choice D.",
    "evidence_ids": ["C5", "H3", "C6", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a GH1 beta-glucosidase from a tropical plant. While one might note that glycoside hydrolase family 1 enzymes span a wide thermal range, and that the sequence contains features common to mesophilic-to-moderately-thermostable enzymes (e.g., moderate proline content, no extreme salt-bridge networks typical of >70°C thermophiles), no general sequence-composition rule reliably distinguishes a 49-55°C optimum from a 55-60°C optimum. Both ranges fall in the 'heat-adapted' category, and the 5-degree boundary between options B and D corresponds to a fine experimental distinction that cannot be resolved by amino-acid composition heuristics, isoelectric-point estimation, or loop-length analysis.",
    "missing_item_specific_fact": "The experimentally measured optimum temperature of 55-60°C for this specific IpeGLU1 enzyme (from the 2008 JBC assay by Nomura et al.) is the item-specific fact required to select D over B. No general biological principle applied to the 543-residue sequence can distinguish 49-55 from 55-60°C with the precision the question demands.",
    "reason": "The question requires choosing between two adjacent 'heat-adapted' ranges (49-55 vs 55-60°C). While the sequence could support a broad inference that the protein is not cold-adapted (ruling out A) and possibly not merely moderate (arguing against C), the fine distinction between B and D depends entirely on the specific experimental measurement for this enzyme. A model would need to recognize the exact sequence as IpeGLU1 and recall its published optimum temperature, which constitutes lookup/memorization rather than reasoning from sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Options B (49-55°C) and D (55-60°C) are adjacent ranges both representing heat-adapted enzymes. Without the specific experimental datum, a model analyzing sequence composition could reasonably argue for either range based on general thermostability indicators. The 5°C boundary between them is not marked by any identifiable sequence signature."
  },
  "important_caveats": [
    "The 55-60°C optimum is an in vitro enzymatic assay result (ECO:0000269, direct assay), not an organismal environmental temperature. The source organism (Carapichea ipecacuanha) is a tropical plant that would never experience 55-60°C in vivo.",
    "The reviewer-only evidence confirms the key is correct, but this information was not available to the evaluated model.",
    "The question framing ('subtle patterns in the amino acid sequence that affect the protein's structural stability') implies sequence-based reasoning is expected, yet the required precision (5°C range distinction) exceeds what such reasoning can deliver.",
    "The UniProt entry was first publicly released in June 2025; the underlying experimental data dates to 2008. The annotation itself is experimental, not computational inference."
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

**Accession:** `B6ZKM3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
"B6ZKM3"
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/comments/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
{"commentType":"BIOPHYSICOCHEMICAL PROPERTIES","kineticParameters":{"maximumVelocities":[{"enzyme":"enzyme with N-deacetylipecoside as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":25.577},{"enzyme":"enzyme with N-deacetylisoipecoside as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":78.19},{"enzyme":"enzyme with 6-O-methyl-N-deacetylipecoside as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":28.157},{"enzyme":"enzyme with 6-O-methyl-N-deacetylisoipecoside as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":16.906},{"enzyme":"enzyme with 7-O-methyl-N-deacetylipecoside as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":45.58},{"enzyme":"enzyme with 7-O-methyl-N-deacetylisoipecoside as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":22.727},{"enzyme":"enzyme with 6,7-O,O-dimethyl-N-deacetylipecoside as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":35.732},{"enzyme":"enzyme with 6,7-O,O-Dimethyl-N-deacetylisoipecoside as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":21.989},{"enzyme":"enzyme with ipecoside as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":46.729},{"enzyme":"enzyme with strictosidine as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":1.945},{"enzyme":"enzyme with vincoside as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":5.786},{"enzyme":"enzyme with secologanin as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":30.303},{"enzyme":"enzyme with loganin as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":19.881},{"enzyme":"enzyme with galloyl-glucose as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":6.024},{"enzyme":"enzyme with p-nitrophenyl-beta-glucose as substrate","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"unit":"nmol/min/mg","velocity":3.546}],"michaelisConstants":[{"constant":0.32,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"N-deacetylipecoside","unit":"mM"},{"constant":5.8,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"N-deacetylisoipecoside","unit":"mM"},{"constant":0.39,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"6-O-methyl-N-deacetylipecoside","unit":"mM"},{"constant":1.3,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"6-O-methyl-N-deacetylisoipecoside","unit":"mM"},{"constant":12.7,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"7-O-methyl-N-deacetylipecoside","unit":"mM"},{"constant":25.5,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"7-O-methyl-N-deacetylisoipecoside","unit":"mM"},{"constant":13.5,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"6,7-O,O-dimethyl-N-deacetylipecoside","unit":"mM"},{"constant":35.0,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"6,7-O,O-Dimethyl-N-deacetylisoipecoside","unit":"mM"},{"constant":0.1,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"ipecoside","unit":"mM"},{"constant":0.19,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"strictosidine","unit":"mM"},{"constant":0.29,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"vincoside","unit":"mM"},{"constant":26.5,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"secologanin","unit":"mM"},{"constant":33.2,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"loganin","unit":"mM"},{"constant":65.1,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"galloyl-glucose","unit":"mM"},{"constant":21.5,"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"substrate":"p-nitrophenyl-beta-glucose","unit":"mM"}],"note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"kcat is 28.2 sec(-1) with N-deacetylipecoside as substrate (PubMed:18927081). kcat is 86.3 sec(-1) with N-deacetylisoipecoside as substrate (PubMed:18927081). kcat is 31.1 sec(-1) with 6-O-methyl-N-deacetylipecoside as substrate (PubMed:18927081). kcat is 18.7 sec(-1) with 6-O-methyl-N-deacetylisoipecoside as substrate (PubMed:18927081). kcat is 50.3 sec(-1) with 7-O-methyl-N-deacetylipecoside as substrate (PubMed:18927081). kcat is 25.1 sec(-1) with 7-O-methyl-N-deacetylisoipecoside as substrate (PubMed:18927081). kcat is 39.4 sec(-1) with 6,7-O,O-dimethyl-N-deacetylipecoside as substrate (PubMed:18927081). kcat is 24.3 sec(-1) with 6,7-O,O-Dimethyl-N-deacetylisoipecoside as substrate (PubMed:18927081). kcat is 51.6 sec(-1) with ipecoside as substrate (PubMed:18927081). kcat is 2.1 sec(-1) with strictosidine as substrate (PubMed:18927081). kcat is 6.4 sec(-1) with vincoside as substrate (PubMed:18927081). kcat is 33.4 sec(-1) with secologanin as substrate (PubMed:18927081). kcat is 21.9 sec(-1) with loganin as substrate (PubMed:18927081). kcat is 6.6 sec(-1) with galloyl-glucose as substrate (PubMed:18927081). kcat is 3.9 sec(-1) with p-nitrophenyl-beta-glucose as substrate (PubMed:18927081)."}]}},"phDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"Optimum pH is 5 with N-deacetylisoipecoside and N-deacetylipecoside as substrates."}]},"temperatureDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"Optimum temperature is 55-60 degrees Celsius."}]}}
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
{"citation":{"authors":["Nomura T.","Quesada A.L.","Kutchan T.M."],"citationCrossReferences":[{"database":"PubMed","id":"18927081"},{"database":"DOI","id":"10.1074/jbc.m806953200"}],"citationType":"journal article","firstPage":"34650","id":"18927081","journal":"J. Biol. Chem.","lastPage":"34659","publicationDate":"2008","title":"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.","volume":"283"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAH02544.1","source":"EMBL"}],"referenceComments":[{"type":"TISSUE","value":"Root"},{"type":"TISSUE","value":"Shoot"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION"]}
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51)  
**Locator:** `lines 19-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:27:52.619495+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAH02544.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.
RC   TISSUE=Root, and Shoot;
RX   PubMed=18927081; DOI=10.1074/jbc.m806953200;
RA   Nomura T., Quesada A.L., Kutchan T.M.;
RT   "The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis
RT   in Psychotria ipecacuanha.";
RL   J. Biol. Chem. 283:34650-34659(2008).
```

Source SHA-256: `90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51)  
**Locator:** `lines 95-174`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:27:52.619495+00:00.  

```text
CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:
CC       Kinetic parameters:
CC         KM=0.32 mM for N-deacetylipecoside {ECO:0000269|PubMed:18927081};
CC         KM=5.8 mM for N-deacetylisoipecoside {ECO:0000269|PubMed:18927081};
CC         KM=0.39 mM for 6-O-methyl-N-deacetylipecoside
CC         {ECO:0000269|PubMed:18927081};
CC         KM=1.3 mM for 6-O-methyl-N-deacetylisoipecoside
CC         {ECO:0000269|PubMed:18927081};
CC         KM=12.7 mM for 7-O-methyl-N-deacetylipecoside
CC         {ECO:0000269|PubMed:18927081};
CC         KM=25.5 mM for 7-O-methyl-N-deacetylisoipecoside
CC         {ECO:0000269|PubMed:18927081};
CC         KM=13.5 mM for 6,7-O,O-dimethyl-N-deacetylipecoside
CC         {ECO:0000269|PubMed:18927081};
CC         KM=35.0 mM for 6,7-O,O-Dimethyl-N-deacetylisoipecoside
CC         {ECO:0000269|PubMed:18927081};
CC         KM=0.10 mM for ipecoside {ECO:0000269|PubMed:18927081};
CC         KM=0.19 mM for strictosidine {ECO:0000269|PubMed:18927081};
CC         KM=0.29 mM for vincoside {ECO:0000269|PubMed:18927081};
CC         KM=26.5 mM for secologanin {ECO:0000269|PubMed:18927081};
CC         KM=33.2 mM for loganin {ECO:0000269|PubMed:18927081};
CC         KM=65.1 mM for galloyl-glucose {ECO:0000269|PubMed:18927081};
CC         KM=21.5 mM for p-nitrophenyl-beta-glucose
CC         {ECO:0000269|PubMed:18927081};
CC         Vmax=25.577 nmol/min/mg enzyme with N-deacetylipecoside as substrate
CC         {ECO:0000269|PubMed:18927081};
CC         Vmax=78.190 nmol/min/mg enzyme with N-deacetylisoipecoside as
CC         substrate {ECO:0000269|PubMed:18927081};
CC         Vmax=28.157 nmol/min/mg enzyme with 6-O-methyl-N-deacetylipecoside as
CC         substrate {ECO:0000269|PubMed:18927081};
CC         Vmax=16.906 nmol/min/mg enzyme with 6-O-methyl-N-deacetylisoipecoside
CC         as substrate {ECO:0000269|PubMed:18927081};
CC         Vmax=45.580 nmol/min/mg enzyme with 7-O-methyl-N-deacetylipecoside as
CC         substrate {ECO:0000269|PubMed:18927081};
CC         Vmax=22.727 nmol/min/mg enzyme with 7-O-methyl-N-deacetylisoipecoside
CC         as substrate {ECO:0000269|PubMed:18927081};
CC         Vmax=35.732 nmol/min/mg enzyme with 6,7-O,O-dimethyl-N-
CC         deacetylipecoside as substrate {ECO:0000269|PubMed:18927081};
CC         Vmax=21.989 nmol/min/mg enzyme with 6,7-O,O-Dimethyl-N-
CC         deacetylisoipecoside as substrate {ECO:0000269|PubMed:18927081};
CC         Vmax=46.729 nmol/min/mg enzyme with ipecoside as substrate
CC         {ECO:0000269|PubMed:18927081};
CC         Vmax=1.945 nmol/min/mg enzyme with strictosidine as substrate
CC         {ECO:0000269|PubMed:18927081};
CC         Vmax=5.786 nmol/min/mg enzyme with vincoside as substrate
CC         {ECO:0000269|PubMed:18927081};
CC         Vmax=30.303 nmol/min/mg enzyme with secologanin as substrate
CC         {ECO:0000269|PubMed:18927081};
CC         Vmax=19.881 nmol/min/mg enzyme with loganin as substrate
CC         {ECO:0000269|PubMed:18927081};
CC         Vmax=6.024 nmol/min/mg enzyme with galloyl-glucose as substrate
CC         {ECO:0000269|PubMed:18927081};
CC         Vmax=3.546 nmol/min/mg enzyme with p-nitrophenyl-beta-glucose as
CC         substrate {ECO:0000269|PubMed:18927081};
CC         Note=kcat is 28.2 sec(-1) with N-deacetylipecoside as substrate
CC         (PubMed:18927081). kcat is 86.3 sec(-1) with N-deacetylisoipecoside
CC         as substrate (PubMed:18927081). kcat is 31.1 sec(-1) with 6-O-methyl-
CC         N-deacetylipecoside as substrate (PubMed:18927081). kcat is 18.7
CC         sec(-1) with 6-O-methyl-N-deacetylisoipecoside as substrate
CC         (PubMed:18927081). kcat is 50.3 sec(-1) with 7-O-methyl-N-
CC         deacetylipecoside as substrate (PubMed:18927081). kcat is 25.1 sec(-
CC         1) with 7-O-methyl-N-deacetylisoipecoside as substrate
CC         (PubMed:18927081). kcat is 39.4 sec(-1) with 6,7-O,O-dimethyl-N-
CC         deacetylipecoside as substrate (PubMed:18927081). kcat is 24.3 sec(-
CC         1) with 6,7-O,O-Dimethyl-N-deacetylisoipecoside as substrate
CC         (PubMed:18927081). kcat is 51.6 sec(-1) with ipecoside as substrate
CC         (PubMed:18927081). kcat is 2.1 sec(-1) with strictosidine as
CC         substrate (PubMed:18927081). kcat is 6.4 sec(-1) with vincoside as
CC         substrate (PubMed:18927081). kcat is 33.4 sec(-1) with secologanin as
CC         substrate (PubMed:18927081). kcat is 21.9 sec(-1) with loganin as
CC         substrate (PubMed:18927081). kcat is 6.6 sec(-1) with galloyl-glucose
CC         as substrate (PubMed:18927081). kcat is 3.9 sec(-1) with p-
CC         nitrophenyl-beta-glucose as substrate (PubMed:18927081).
CC         {ECO:0000269|PubMed:18927081};
CC       pH dependence:
CC         Optimum pH is 5 with N-deacetylisoipecoside and N-deacetylipecoside
CC         as substrates. {ECO:0000269|PubMed:18927081};
CC       Temperature dependence:
CC         Optimum temperature is 55-60 degrees Celsius.
CC         {ECO:0000269|PubMed:18927081};
```

Source SHA-256: `90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
