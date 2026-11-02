# temperature_0025

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `temperature`  
**Author expected answer:** **D** — 80

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MYAYNGKLLDVDLTREKVKEVELSEDVLKKFYGGRGLGTYILWKELGEKWEKVDPLGEENLLLILTGPLTGYYPGMKTSIVSKSPESNGVVGSVLSSELGLELKAAGYDGIIIRGKAKSPVYLFIHNDTVEIRDATKYWGMGGIELYKTLLKEVHEEIRKKEKLKGVPKEPAMIYIGKGGENKVRFAAIMTKLMHAAGYGGYGAVMGSKNLKAVIAKGSGPLPEVYDKEKMKVLLREFWKELFSMTTFREWGTGAGGYSVGHDRSSEPIRNWQEEYHDNEEISVVNFENRTWIKKYWADYGCPVNCMKISYLRYGPYKGSISDAPDYELQAYMGTNLGIFEPEKIVYLSYLVDELGLDGINTGNILGFAAELYQRGILTKEDLGFELNWGDEKAFAKLLHLIVEKEGIGKILAEGTYRAALKISEIKGIDVTKYAVHVKGIAVGAHGIRSELDYTKDISYAVSVQGGDHTSTAALPAKGYTGELVEAFYDSAVICNFVTKPGFEKIIEFGNALSGFNITPEQWLNEIGLRIIHLQRILLLLGGPDVYWDPRKDDDNPPRFYEPLPSGPVKGKAPNREDIKAKVKQYYEEIGYDEHGIPKEEVLEELGIGEAKREVKRIKKRLNL

[Multiple Choices]
A. 32
B. 23
C. 64
D. 80
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

> The exact sequence matches the UniProt entry, which reports an experimentally supported optimum of 80 °C for oxidation of hexanal. This supports choice D, with the qualification that the reported optimum is for that assay and substrate.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options include high temperatures, but the sequence alone does not provide a defensible way to distinguish an exact value of 80 from 64 °C.


**Missing item-specific fact**

> The sequence-specific experimental result reporting an 80 °C optimum for hexanal oxidation.


**Reason**

> The required distinction relies on a protein-specific measured optimum absent from the question. General thermal-adaptation heuristics cannot establish that precise value.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice D matches the reported assay optimum; the other values are not supported by the supplied sequence alone.


### Important caveats

- The reported 80 °C optimum is specifically for oxidation of hexanal, not necessarily a universal optimum for every substrate or assay condition.
- The sequence match and experimental annotation are reviewer-only evidence, not information provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options include high temperatures, but the sequence alone does not provide a defensible way to distinguish an exact value of 80 from 64 °C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific experimental result reporting an 80 °C optimum for hexanal oxidation.",
    "reason": "The required distinction relies on a protein-specific measured optimum absent from the question. General thermal-adaptation heuristics cannot establish that precise value."
  },
  "case_id": "temperature_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which reports an experimentally supported optimum of 80 °C for oxidation of hexanal. This supports choice D, with the qualification that the reported optimum is for that assay and substrate."
  },
  "important_caveats": [
    "The reported 80 °C optimum is specifically for oxidation of hexanal, not necessarily a universal optimum for every substrate or assay condition.",
    "The sequence match and experimental annotation are reviewer-only evidence, not information provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice D matches the reported assay optimum; the other values are not supported by the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which reports an experimentally supported optimum of 80 °C for oxidation of hexanal. This supports choice D, with the qualification that the reported optimum is for that assay and substrate.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options include high temperatures, but the sequence alone does not provide a defensible way to distinguish an exact value of 80 from 64 °C.",
    "missing_item_specific_fact": "The sequence-specific experimental result reporting an 80 °C optimum for hexanal oxidation.",
    "reason": "The required distinction relies on a protein-specific measured optimum absent from the question. General thermal-adaptation heuristics cannot establish that precise value."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice D matches the reported assay optimum; the other values are not supported by the supplied sequence alone."
  },
  "important_caveats": [
    "The reported 80 °C optimum is specifically for oxidation of hexanal, not necessarily a universal optimum for every substrate or assay condition.",
    "The sequence match and experimental annotation are reviewer-only evidence, not information provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry E7FHH1 (ASOR_PYRFU) from Pyrococcus furiosus. The UniProt annotation explicitly states 'Optimum temperature is 80 degrees Celsius for the oxidation of hexanal,' supported by experimental evidence (ECO:0000269, PubMed:16199576, Bevers et al. 2005). This is a direct experimental measurement, not merely a computational prediction. The sequence match is confirmed across both current and historical (v59) snapshots.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General sequence analysis could suggest thermophily (e.g., elevated charged-residue content, potential ion-pair networks, reduced thermolabile residues), which might narrow choices from 23°C/32°C to the 64°C/80°C range. However, distinguishing 80°C from 64°C specifically requires knowing the organism identity (Pyrococcus furiosus, a hyperthermophile with ~100°C growth optimum) or the specific experimental measurement for this enzyme. Neither organism identity nor the 80°C value is derivable from the sequence by general biological reasoning alone.


**Missing item-specific fact**

> The identity of the source organism (Pyrococcus furiosus, a hyperthermophilic archaeon) and the experimentally measured optimum temperature of 80°C for this specific tungsten-containing oxidoreductase (Bevers et al., J. Bacteriol. 2005). Identifying the organism from the sequence requires database lookup (e.g., BLAST), and even knowing the organism, the enzyme optimum (80°C) differs from the growth optimum (~100°C), necessitating the specific measurement.


**Reason**

> The question provides only a raw amino acid sequence with no organism annotation. While hyperthermophilic sequence signatures (high charge, ion-pair potential) might suggest a thermophilic origin, they cannot reliably distinguish 80°C from 64°C. The correct answer depends on identifying the protein as belonging to Pyrococcus furiosus (a database lookup) and knowing the specific experimental optimum of 80°C for this enzyme. Recognizing the sequence as a P. furiosus protein and recalling its growth temperature is memorization, not reasoning from sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Without organism identification, a sequence showing thermophilic features could reasonably be assigned to either 64°C (thermophile) or 80°C (hyperthermophile). The general sequence heuristics mentioned in the system prompt (amino acid composition, internal bonds) do not provide a clear quantitative boundary between 64°C and 80°C. Only knowing the organism is Pyrococcus furiosus (hyperthermophile, ~100°C growth) or the specific experimental measurement resolves the ambiguity decisively toward D.


### Important caveats

- The 80°C value is a specific experimental measurement for hexanal oxidation with this enzyme, not a universal protein stability temperature. The question frames it as 'thermal adaptation category' which is a broader concept than a single substrate's optimum.
- Pyrococcus furiosus grows optimally at ~100°C; the enzyme optimum of 80°C is below the organism's growth optimum, so even knowing the organism would not trivially yield 80°C without the specific measurement.
- The organism identity (Pyrococcus furiosus) was absent from the model input and is reviewer-only information.
- The sequence is 624 AA and matches the canonical UniProt sequence exactly (SHA-256 confirmed), so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General sequence analysis could suggest thermophily (e.g., elevated charged-residue content, potential ion-pair networks, reduced thermolabile residues), which might narrow choices from 23°C/32°C to the 64°C/80°C range. However, distinguishing 80°C from 64°C specifically requires knowing the organism identity (Pyrococcus furiosus, a hyperthermophile with ~100°C growth optimum) or the specific experimental measurement for this enzyme. Neither organism identity nor the 80°C value is derivable from the sequence by general biological reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the source organism (Pyrococcus furiosus, a hyperthermophilic archaeon) and the experimentally measured optimum temperature of 80°C for this specific tungsten-containing oxidoreductase (Bevers et al., J. Bacteriol. 2005). Identifying the organism from the sequence requires database lookup (e.g., BLAST), and even knowing the organism, the enzyme optimum (80°C) differs from the growth optimum (~100°C), necessitating the specific measurement.",
    "reason": "The question provides only a raw amino acid sequence with no organism annotation. While hyperthermophilic sequence signatures (high charge, ion-pair potential) might suggest a thermophilic origin, they cannot reliably distinguish 80°C from 64°C. The correct answer depends on identifying the protein as belonging to Pyrococcus furiosus (a database lookup) and knowing the specific experimental optimum of 80°C for this enzyme. Recognizing the sequence as a P. furiosus protein and recalling its growth temperature is memorization, not reasoning from sequence features."
  },
  "case_id": "temperature_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry E7FHH1 (ASOR_PYRFU) from Pyrococcus furiosus. The UniProt annotation explicitly states 'Optimum temperature is 80 degrees Celsius for the oxidation of hexanal,' supported by experimental evidence (ECO:0000269, PubMed:16199576, Bevers et al. 2005). This is a direct experimental measurement, not merely a computational prediction. The sequence match is confirmed across both current and historical (v59) snapshots."
  },
  "important_caveats": [
    "The 80°C value is a specific experimental measurement for hexanal oxidation with this enzyme, not a universal protein stability temperature. The question frames it as 'thermal adaptation category' which is a broader concept than a single substrate's optimum.",
    "Pyrococcus furiosus grows optimally at ~100°C; the enzyme optimum of 80°C is below the organism's growth optimum, so even knowing the organism would not trivially yield 80°C without the specific measurement.",
    "The organism identity (Pyrococcus furiosus) was absent from the model input and is reviewer-only information.",
    "The sequence is 624 AA and matches the canonical UniProt sequence exactly (SHA-256 confirmed), so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Without organism identification, a sequence showing thermophilic features could reasonably be assigned to either 64°C (thermophile) or 80°C (hyperthermophile). The general sequence heuristics mentioned in the system prompt (amino acid composition, internal bonds) do not provide a clear quantitative boundary between 64°C and 80°C. Only knowing the organism is Pyrococcus furiosus (hyperthermophile, ~100°C growth) or the specific experimental measurement resolves the ambiguity decisively toward D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry E7FHH1 (ASOR_PYRFU) from Pyrococcus furiosus. The UniProt annotation explicitly states 'Optimum temperature is 80 degrees Celsius for the oxidation of hexanal,' supported by experimental evidence (ECO:0000269, PubMed:16199576, Bevers et al. 2005). This is a direct experimental measurement, not merely a computational prediction. The sequence match is confirmed across both current and historical (v59) snapshots.",
    "evidence_ids": ["C5", "C6", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General sequence analysis could suggest thermophily (e.g., elevated charged-residue content, potential ion-pair networks, reduced thermolabile residues), which might narrow choices from 23°C/32°C to the 64°C/80°C range. However, distinguishing 80°C from 64°C specifically requires knowing the organism identity (Pyrococcus furiosus, a hyperthermophile with ~100°C growth optimum) or the specific experimental measurement for this enzyme. Neither organism identity nor the 80°C value is derivable from the sequence by general biological reasoning alone.",
    "missing_item_specific_fact": "The identity of the source organism (Pyrococcus furiosus, a hyperthermophilic archaeon) and the experimentally measured optimum temperature of 80°C for this specific tungsten-containing oxidoreductase (Bevers et al., J. Bacteriol. 2005). Identifying the organism from the sequence requires database lookup (e.g., BLAST), and even knowing the organism, the enzyme optimum (80°C) differs from the growth optimum (~100°C), necessitating the specific measurement.",
    "reason": "The question provides only a raw amino acid sequence with no organism annotation. While hyperthermophilic sequence signatures (high charge, ion-pair potential) might suggest a thermophilic origin, they cannot reliably distinguish 80°C from 64°C. The correct answer depends on identifying the protein as belonging to Pyrococcus furiosus (a database lookup) and knowing the specific experimental optimum of 80°C for this enzyme. Recognizing the sequence as a P. furiosus protein and recalling its growth temperature is memorization, not reasoning from sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Without organism identification, a sequence showing thermophilic features could reasonably be assigned to either 64°C (thermophile) or 80°C (hyperthermophile). The general sequence heuristics mentioned in the system prompt (amino acid composition, internal bonds) do not provide a clear quantitative boundary between 64°C and 80°C. Only knowing the organism is Pyrococcus furiosus (hyperthermophile, ~100°C growth) or the specific experimental measurement resolves the ambiguity decisively toward D."
  },
  "important_caveats": [
    "The 80°C value is a specific experimental measurement for hexanal oxidation with this enzyme, not a universal protein stability temperature. The question frames it as 'thermal adaptation category' which is a broader concept than a single substrate's optimum.",
    "Pyrococcus furiosus grows optimally at ~100°C; the enzyme optimum of 80°C is below the organism's growth optimum, so even knowing the organism would not trivially yield 80°C without the specific measurement.",
    "The organism identity (Pyrococcus furiosus) was absent from the model input and is reviewer-only information.",
    "The sequence is 624 AA and matches the canonical UniProt sequence exactly (SHA-256 confirmed), so the annotation applies directly to the supplied sequence."
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

**Accession:** `E7FHH1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 59. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/comments/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
{"commentType":"BIOPHYSICOCHEMICAL PROPERTIES","kineticParameters":{"maximumVelocities":[{"enzyme":"enzyme with taurine as substrate (with benzyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"unit":"umol/min/mg","velocity":14.9},{"enzyme":"enzyme with hexanal as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":15.6},{"enzyme":"enzyme with hexanal as substrate (with benzyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"unit":"umol/min/mg","velocity":30.0},{"enzyme":"enzyme with hydratropaldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":9.3},{"enzyme":"enzyme with 2-ethylhexanal as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":8.3},{"enzyme":"enzyme with 2-methylvaleraldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":12.7},{"enzyme":"enzyme with 3-phenylbutyraldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":8.0},{"enzyme":"enzyme with 2-methylbutyraldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":7.7},{"enzyme":"enzyme with isobutyraldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":11.8},{"enzyme":"enzyme with 2-naphthaldehyde(beta) as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":7.7},{"enzyme":"enzyme with acetaldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":0.34},{"enzyme":"enzyme with cinnamaldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":7.4},{"enzyme":"enzyme with propionaldehyde as substrate (with benzyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"unit":"umol/min/mg","velocity":26.2},{"enzyme":"enzyme with 2-methoxybenzaldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":15.1},{"enzyme":"enzyme with glutaraldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":1.4},{"enzyme":"enzyme with formaldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":8.5},{"enzyme":"enzyme with crotonaldehyde as substrate (with methyl viologen as electron acceptor)","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"unit":"umol/min/mg","velocity":1.1}],"michaelisConstants":[{"constant":0.112,"evidences":[{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"substrate":"taurine","unit":"mM"},{"constant":0.18,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"hexanal","unit":"mM"},{"constant":0.23,"evidences":[{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"substrate":"hexanal","unit":"mM"},{"constant":0.12,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"hydratropaldehyde","unit":"mM"},{"constant":0.17,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"2-ethylhexanal","unit":"mM"},{"constant":0.27,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"2-methylvaleraldehyde","unit":"mM"},{"constant":0.42,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"3-phenylbutyraldehyde","unit":"mM"},{"constant":0.43,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"2-methylbutyraldehyde","unit":"mM"},{"constant":0.79,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"isobutyraldehyde","unit":"mM"},{"constant":1.3,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"2-naphthaldehyde(beta)","unit":"mM"},{"constant":1.5,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"acetaldehyde","unit":"mM"},{"constant":1.6,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"cinnamaldehyde","unit":"mM"},{"constant":2.047,"evidences":[{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"substrate":"propionaldehyde","unit":"mM"},{"constant":4.8,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"2-methoxybenzaldehyde","unit":"mM"},{"constant":9.4,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"glutaraldehyde","unit":"mM"},{"constant":45.0,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"formaldehyde","unit":"mM"},{"constant":46.0,"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"substrate":"crotonaldehyde","unit":"mM"}]},"temperatureDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"}],"value":"Optimum temperature is 80 degrees Celsius for the oxidation of hexanal."}]}}
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
{"citation":{"authors":["Bevers L.E.","Bol E.","Hagedoorn P.L.","Hagen W.R."],"citationCrossReferences":[{"database":"PubMed","id":"16199576"},{"database":"DOI","id":"10.1128/jb.187.20.7056-7061.2005"}],"citationType":"journal article","firstPage":"7056","id":"16199576","journal":"J. Bacteriol.","lastPage":"7061","publicationDate":"2005","title":"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus furiosus with a broad substrate specificity.","volume":"187"},"referenceComments":[{"type":"STRAIN","value":"ATCC 43587 / DSM 3638 / JCM 8422 / Vc1"}],"referenceNumber":3,"referencePositions":["PROTEIN SEQUENCE OF 1-21","FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 37-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
RN   [3]
RP   PROTEIN SEQUENCE OF 1-21, FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE, COFACTOR,
RP   AND BIOPHYSICOCHEMICAL PROPERTIES.
RC   STRAIN=ATCC 43587 / DSM 3638 / JCM 8422 / Vc1;
RX   PubMed=16199576; DOI=10.1128/jb.187.20.7056-7061.2005;
RA   Bevers L.E., Bol E., Hagedoorn P.L., Hagen W.R.;
RT   "WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus
RT   furiosus with a broad substrate specificity.";
RL   J. Bacteriol. 187:7056-7061(2005).
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 124-184`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:
CC       Kinetic parameters:
CC         KM=0.112 mM for taurine {ECO:0000269|PubMed:36269456};
CC         KM=0.18 mM for hexanal {ECO:0000269|PubMed:16199576};
CC         KM=0.230 mM for hexanal {ECO:0000269|PubMed:36269456};
CC         KM=0.12 mM for hydratropaldehyde {ECO:0000269|PubMed:16199576};
CC         KM=0.17 mM for 2-ethylhexanal {ECO:0000269|PubMed:16199576};
CC         KM=0.27 mM for 2-methylvaleraldehyde {ECO:0000269|PubMed:16199576};
CC         KM=0.42 mM for 3-phenylbutyraldehyde {ECO:0000269|PubMed:16199576};
CC         KM=0.43 mM for 2-methylbutyraldehyde {ECO:0000269|PubMed:16199576};
CC         KM=0.79 mM for isobutyraldehyde {ECO:0000269|PubMed:16199576};
CC         KM=1.3 mM for 2-naphthaldehyde(beta) {ECO:0000269|PubMed:16199576};
CC         KM=1.5 mM for acetaldehyde {ECO:0000269|PubMed:16199576};
CC         KM=1.6 mM for cinnamaldehyde {ECO:0000269|PubMed:16199576};
CC         KM=2.047 mM for propionaldehyde {ECO:0000269|PubMed:36269456};
CC         KM=4.8 mM for 2-methoxybenzaldehyde {ECO:0000269|PubMed:16199576};
CC         KM=9.4 mM for glutaraldehyde {ECO:0000269|PubMed:16199576};
CC         KM=45 mM for formaldehyde {ECO:0000269|PubMed:16199576};
CC         KM=46 mM for crotonaldehyde {ECO:0000269|PubMed:16199576};
CC         Vmax=14.9 umol/min/mg enzyme with taurine as substrate (with benzyl
CC         viologen as electron acceptor) {ECO:0000269|PubMed:36269456};
CC         Vmax=15.6 umol/min/mg enzyme with hexanal as substrate (with methyl
CC         viologen as electron acceptor) {ECO:0000269|PubMed:16199576};
CC         Vmax=30.0 umol/min/mg enzyme with hexanal as substrate (with benzyl
CC         viologen as electron acceptor) {ECO:0000269|PubMed:36269456};
CC         Vmax=9.3 umol/min/mg enzyme with hydratropaldehyde as substrate (with
CC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};
CC         Vmax=8.3 umol/min/mg enzyme with 2-ethylhexanal as substrate (with
CC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};
CC         Vmax=12.7 umol/min/mg enzyme with 2-methylvaleraldehyde as substrate
CC         (with methyl viologen as electron acceptor)
CC         {ECO:0000269|PubMed:16199576};
CC         Vmax=8.0 umol/min/mg enzyme with 3-phenylbutyraldehyde as substrate
CC         (with methyl viologen as electron acceptor)
CC         {ECO:0000269|PubMed:16199576};
CC         Vmax=7.7 umol/min/mg enzyme with 2-methylbutyraldehyde as substrate
CC         (with methyl viologen as electron acceptor)
CC         {ECO:0000269|PubMed:16199576};
CC         Vmax=11.8 umol/min/mg enzyme with isobutyraldehyde as substrate (with
CC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};
CC         Vmax=7.7 umol/min/mg enzyme with 2-naphthaldehyde(beta) as substrate
CC         (with methyl viologen as electron acceptor)
CC         {ECO:0000269|PubMed:16199576};
CC         Vmax=0.34 umol/min/mg enzyme with acetaldehyde as substrate (with
CC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};
CC         Vmax=7.4 umol/min/mg enzyme with cinnamaldehyde as substrate (with
CC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};
CC         Vmax=26.2 umol/min/mg enzyme with propionaldehyde as substrate (with
CC         benzyl viologen as electron acceptor) {ECO:0000269|PubMed:36269456};
CC         Vmax=15.1 umol/min/mg enzyme with 2-methoxybenzaldehyde as substrate
CC         (with methyl viologen as electron acceptor)
CC         {ECO:0000269|PubMed:16199576};
CC         Vmax=1.4 umol/min/mg enzyme with glutaraldehyde as substrate (with
CC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};
CC         Vmax=8.5 umol/min/mg enzyme with formaldehyde as substrate (with
CC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};
CC         Vmax=1.1 umol/min/mg enzyme with crotonaldehyde as substrate (with
CC         methyl viologen as electron acceptor) {ECO:0000269|PubMed:16199576};
CC       Temperature dependence:
CC         Optimum temperature is 80 degrees Celsius for the oxidation of
CC         hexanal. {ECO:0000269|PubMed:16199576};
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
