# cofactor_0092

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MYAYNGKLLDVDLTREKVKEVELSEDVLKKFYGGRGLGTYILWKELGEKWEKVDPLGEENLLLILTGPLTGYYPGMKTSIVSKSPESNGVVGSVLSSELGLELKAAGYDGIIIRGKAKSPVYLFIHNDTVEIRDATKYWGMGGIELYKTLLKEVHEEIRKKEKLKGVPKEPAMIYIGKGGENKVRFAAIMTKLMHAAGYGGYGAVMGSKNLKAVIAKGSGPLPEVYDKEKMKVLLREFWKELFSMTTFREWGTGAGGYSVGHDRSSEPIRNWQEEYHDNEEISVVNFENRTWIKKYWADYGCPVNCMKISYLRYGPYKGSISDAPDYELQAYMGTNLGIFEPEKIVYLSYLVDELGLDGINTGNILGFAAELYQRGILTKEDLGFELNWGDEKAFAKLLHLIVEKEGIGKILAEGTYRAALKISEIKGIDVTKYAVHVKGIAVGAHGIRSELDYTKDISYAVSVQGGDHTSTAALPAKGYTGELVEAFYDSAVICNFVTKPGFEKIIEFGNALSGFNITPEQWLNEIGLRIIHLQRILLLLGGPDVYWDPRKDDDNPPRFYEPLPSGPVKGKAPNREDIKAKVKQYYEEIGYDEHGIPKEEVLEELGIGEAKREVKRIKKRLNL

[Multiple Choices]
A. Mn(2+)
B. Fe cation
C. Fe(2+)
D. [4Fe-4S] cluster
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry annotates one &#91;4Fe-4S&#93; cluster per subunit with experimental evidence codes; the cited crystallography also reports the protein in complex with an iron-sulfur cluster. Thus D is supported among the listed choices. The annotation also identifies tungstopterin, which is not offered.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [C6](#evidence-c6), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include a specific iron-sulfur cluster, but the sequence alone supplies no decisive evidence establishing that this particular protein binds a &#91;4Fe-4S&#93; cluster rather than another listed iron form.


**Missing item-specific fact**

> The protein-specific cofactor annotation or experimental evidence that this protein binds a &#91;4Fe-4S&#93; cluster.


**Reason**

> The supplied input is only a sequence and choices. Identifying the cofactor for this large enzyme requires a protein-specific fact not established by a sufficiently discriminating sequence feature or biological context in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, the evidence supports D; the protein also binds tungstopterin, but that cofactor is not an option.


### Important caveats

- Reviewer-only evidence supports the key but was not supplied to the evaluated model.
- The cofactor annotation is linked to experimental evidence, including crystallography; it is not merely a sequence-based prediction.
- The available evidence supports the matched sequence, while the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include a specific iron-sulfur cluster, but the sequence alone supplies no decisive evidence establishing that this particular protein binds a [4Fe-4S] cluster rather than another listed iron form.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cofactor annotation or experimental evidence that this protein binds a [4Fe-4S] cluster.",
    "reason": "The supplied input is only a sequence and choices. Identifying the cofactor for this large enzyme requires a protein-specific fact not established by a sufficiently discriminating sequence feature or biological context in the question."
  },
  "case_id": "cofactor_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H4",
      "H5",
      "C6",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates one [4Fe-4S] cluster per subunit with experimental evidence codes; the cited crystallography also reports the protein in complex with an iron-sulfur cluster. Thus D is supported among the listed choices. The annotation also identifies tungstopterin, which is not offered."
  },
  "important_caveats": [
    "Reviewer-only evidence supports the key but was not supplied to the evaluated model.",
    "The cofactor annotation is linked to experimental evidence, including crystallography; it is not merely a sequence-based prediction.",
    "The available evidence supports the matched sequence, while the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the evidence supports D; the protein also binds tungstopterin, but that cofactor is not an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates one [4Fe-4S] cluster per subunit with experimental evidence codes; the cited crystallography also reports the protein in complex with an iron-sulfur cluster. Thus D is supported among the listed choices. The annotation also identifies tungstopterin, which is not offered.",
    "evidence_ids": ["C5", "C8", "H4", "H5", "C6", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include a specific iron-sulfur cluster, but the sequence alone supplies no decisive evidence establishing that this particular protein binds a [4Fe-4S] cluster rather than another listed iron form.",
    "missing_item_specific_fact": "The protein-specific cofactor annotation or experimental evidence that this protein binds a [4Fe-4S] cluster.",
    "reason": "The supplied input is only a sequence and choices. Identifying the cofactor for this large enzyme requires a protein-specific fact not established by a sufficiently discriminating sequence feature or biological context in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the evidence supports D; the protein also binds tungstopterin, but that cofactor is not an option."
  },
  "important_caveats": [
    "Reviewer-only evidence supports the key but was not supplied to the evaluated model.",
    "The cofactor annotation is linked to experimental evidence, including crystallography; it is not merely a sequence-based prediction.",
    "The available evidence supports the matched sequence, while the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt E7FHH1 (WOR5/ASOR from Pyrococcus furiosus) is experimentally annotated with a &#91;4Fe-4S&#93; cluster cofactor (ECO:0000269, direct evidence from PubMed:16199576 and PubMed:36269456). X-ray crystallography at 1.94 Å (PDB 6X1O, 6X6U) confirmed the protein in complex with a &#91;4Fe-4S&#93; cluster and tungstopterin. The note specifies three cysteine ligands and one aspartic acid ligand. Among the four choices, &#91;4Fe-4S&#93; cluster is the only correct cofactor; tungstopterin (the other cofactor) is not offered as an option.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 624-aa sequence belongs to a large multi-domain oxidoreductase with Cys-rich motifs (e.g., 'CPVNC' and other Cys residues in the C-terminal region) consistent with Fe-S cluster coordination. In biochemistry, Cys-cluster motifs in electron-transfer oxidoreductases characteristically indicate &#91;4Fe-4S&#93; clusters, which serve as electron-transfer cofactors. Free divalent metal ions (Mn²⁺, Fe²⁺) are not the typical 'cofactors' of ferredoxin-type oxidoreductases; they serve catalytic roles in hydrolases or isomerases. 'Fe cation' is not a standard cofactor designation. Thus, general knowledge of metalloenzyme cofactor types and the Cys-cluster signature in the sequence meaningfully distinguishes &#91;4Fe-4S&#93; from the three free-ion distractors.


**Missing item-specific fact**

> None strictly required. Recognizing the exact WOR5/ASOR identity and its dual-cofactor architecture would be item-specific lookup, but the question is answerable via general principles: oxidoreductase + Cys clusters → Fe-S cluster; free ions are not electron-transfer cofactors in this enzyme class.


**Reason**

> A model with general biochemistry knowledge can reason: (1) the protein is a large oxidoreductase with Cys-rich regions suggestive of Fe-S cluster binding; (2) &#91;4Fe-4S&#93; is the canonical electron-transfer cofactor in ferredoxin-type oxidoreductases; (3) Mn²⁺, Fe²⁺, and 'Fe cation' are not standard cofactor designations for this enzyme class. This provides a concrete biological argument favoring D without requiring memorization of the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein has two cofactors (&#91;4Fe-4S&#93; and tungstopterin), but tungstopterin is not among the choices. Among the four options, only &#91;4Fe-4S&#93; is experimentally supported. Mn(2+), 'Fe cation', and Fe(2+) are not cofactors of this enzyme. No ambiguity exists among the provided choices.


### Important caveats

- The protein also binds tungstopterin as a cofactor (ECO:0000269), which is arguably the primary catalytic cofactor for the tungsten-dependent reaction. The question's singular 'the specific cofactor' is slightly imprecise, but since tungstopterin is not an option, this does not affect answer selection.
- The &#91;4Fe-4S&#93; cluster here has an unusual 3-Cys + 1-Asp coordination (rather than the typical 4-Cys), which is a protein-specific structural detail not easily deducible from sequence alone, though it does not affect the multiple-choice answer.
- The Cys-cluster pattern in the sequence (CPVNC plus scattered Cys) is suggestive but not a textbook CxxCPx2CxxC motif; the 3-Cys+1-Asp arrangement makes sequence-based prediction of cluster type less straightforward than for canonical ferredoxins.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 624-aa sequence belongs to a large multi-domain oxidoreductase with Cys-rich motifs (e.g., 'CPVNC' and other Cys residues in the C-terminal region) consistent with Fe-S cluster coordination. In biochemistry, Cys-cluster motifs in electron-transfer oxidoreductases characteristically indicate [4Fe-4S] clusters, which serve as electron-transfer cofactors. Free divalent metal ions (Mn²⁺, Fe²⁺) are not the typical 'cofactors' of ferredoxin-type oxidoreductases; they serve catalytic roles in hydrolases or isomerases. 'Fe cation' is not a standard cofactor designation. Thus, general knowledge of metalloenzyme cofactor types and the Cys-cluster signature in the sequence meaningfully distinguishes [4Fe-4S] from the three free-ion distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Recognizing the exact WOR5/ASOR identity and its dual-cofactor architecture would be item-specific lookup, but the question is answerable via general principles: oxidoreductase + Cys clusters → Fe-S cluster; free ions are not electron-transfer cofactors in this enzyme class.",
    "reason": "A model with general biochemistry knowledge can reason: (1) the protein is a large oxidoreductase with Cys-rich regions suggestive of Fe-S cluster binding; (2) [4Fe-4S] is the canonical electron-transfer cofactor in ferredoxin-type oxidoreductases; (3) Mn²⁺, Fe²⁺, and 'Fe cation' are not standard cofactor designations for this enzyme class. This provides a concrete biological argument favoring D without requiring memorization of the specific UniProt entry."
  },
  "case_id": "cofactor_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt E7FHH1 (WOR5/ASOR from Pyrococcus furiosus) is experimentally annotated with a [4Fe-4S] cluster cofactor (ECO:0000269, direct evidence from PubMed:16199576 and PubMed:36269456). X-ray crystallography at 1.94 Å (PDB 6X1O, 6X6U) confirmed the protein in complex with a [4Fe-4S] cluster and tungstopterin. The note specifies three cysteine ligands and one aspartic acid ligand. Among the four choices, [4Fe-4S] cluster is the only correct cofactor; tungstopterin (the other cofactor) is not offered as an option."
  },
  "important_caveats": [
    "The protein also binds tungstopterin as a cofactor (ECO:0000269), which is arguably the primary catalytic cofactor for the tungsten-dependent reaction. The question's singular 'the specific cofactor' is slightly imprecise, but since tungstopterin is not an option, this does not affect answer selection.",
    "The [4Fe-4S] cluster here has an unusual 3-Cys + 1-Asp coordination (rather than the typical 4-Cys), which is a protein-specific structural detail not easily deducible from sequence alone, though it does not affect the multiple-choice answer.",
    "The Cys-cluster pattern in the sequence (CPVNC plus scattered Cys) is suggestive but not a textbook CxxCPx2CxxC motif; the 3-Cys+1-Asp arrangement makes sequence-based prediction of cluster type less straightforward than for canonical ferredoxins."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has two cofactors ([4Fe-4S] and tungstopterin), but tungstopterin is not among the choices. Among the four options, only [4Fe-4S] is experimentally supported. Mn(2+), 'Fe cation', and Fe(2+) are not cofactors of this enzyme. No ambiguity exists among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt E7FHH1 (WOR5/ASOR from Pyrococcus furiosus) is experimentally annotated with a [4Fe-4S] cluster cofactor (ECO:0000269, direct evidence from PubMed:16199576 and PubMed:36269456). X-ray crystallography at 1.94 Å (PDB 6X1O, 6X6U) confirmed the protein in complex with a [4Fe-4S] cluster and tungstopterin. The note specifies three cysteine ligands and one aspartic acid ligand. Among the four choices, [4Fe-4S] cluster is the only correct cofactor; tungstopterin (the other cofactor) is not offered as an option.",
    "evidence_ids": ["C5", "C6", "C8", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 624-aa sequence belongs to a large multi-domain oxidoreductase with Cys-rich motifs (e.g., 'CPVNC' and other Cys residues in the C-terminal region) consistent with Fe-S cluster coordination. In biochemistry, Cys-cluster motifs in electron-transfer oxidoreductases characteristically indicate [4Fe-4S] clusters, which serve as electron-transfer cofactors. Free divalent metal ions (Mn²⁺, Fe²⁺) are not the typical 'cofactors' of ferredoxin-type oxidoreductases; they serve catalytic roles in hydrolases or isomerases. 'Fe cation' is not a standard cofactor designation. Thus, general knowledge of metalloenzyme cofactor types and the Cys-cluster signature in the sequence meaningfully distinguishes [4Fe-4S] from the three free-ion distractors.",
    "missing_item_specific_fact": "None strictly required. Recognizing the exact WOR5/ASOR identity and its dual-cofactor architecture would be item-specific lookup, but the question is answerable via general principles: oxidoreductase + Cys clusters → Fe-S cluster; free ions are not electron-transfer cofactors in this enzyme class.",
    "reason": "A model with general biochemistry knowledge can reason: (1) the protein is a large oxidoreductase with Cys-rich regions suggestive of Fe-S cluster binding; (2) [4Fe-4S] is the canonical electron-transfer cofactor in ferredoxin-type oxidoreductases; (3) Mn²⁺, Fe²⁺, and 'Fe cation' are not standard cofactor designations for this enzyme class. This provides a concrete biological argument favoring D without requiring memorization of the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has two cofactors ([4Fe-4S] and tungstopterin), but tungstopterin is not among the choices. Among the four options, only [4Fe-4S] is experimentally supported. Mn(2+), 'Fe cation', and Fe(2+) are not cofactors of this enzyme. No ambiguity exists among the provided choices."
  },
  "important_caveats": [
    "The protein also binds tungstopterin as a cofactor (ECO:0000269), which is arguably the primary catalytic cofactor for the tungsten-dependent reaction. The question's singular 'the specific cofactor' is slightly imprecise, but since tungstopterin is not an option, this does not affect answer selection.",
    "The [4Fe-4S] cluster here has an unusual 3-Cys + 1-Asp coordination (rather than the typical 4-Cys), which is a protein-specific structural detail not easily deducible from sequence alone, though it does not affect the multiple-choice answer.",
    "The Cys-cluster pattern in the sequence (CPVNC plus scattered Cys) is suggestive but not a textbook CxxCPx2CxxC motif; the 3-Cys+1-Asp arrangement makes sequence-based prediction of cluster type less straightforward than for canonical ferredoxins."
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
**Locator:** `/comments/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:49883"},"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"name":"[4Fe-4S] cluster"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"value":"Binds 1 [4Fe-4S] cluster per subunit (PubMed:16199576, PubMed:36269456). The [4Fe-4S] cluster has three cysteine ligands and one aspartic acid ligand (PubMed:36269456)."}]}}
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/comments/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:30402"},"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"name":"tungstopterin"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"value":"Binds 1 tungstopterin cofactor per subunit."}]}}
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
{"citation":{"authors":["Mathew L.G.","Haja D.K.","Pritchett C.","McCormick W.","Zeineddine R.","Fontenot L.S.","Rivera M.E.","Glushka J.","Adams M.W.W.","Lanzilotta W.N."],"citationCrossReferences":[{"database":"PubMed","id":"36269456"},{"database":"DOI","id":"10.1007/s00775-022-01965-0"}],"citationType":"journal article","firstPage":"747","id":"36269456","journal":"J. Biol. Inorg. Chem.","lastPage":"758","publicationDate":"2022","title":"An unprecedented function for a tungsten-containing oxidoreductase.","volume":"27"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6X1O","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6X6U","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"COM1"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR (4FE-4S) CLUSTER AND TUNGSTOPTERIN","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 46-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
RN   [4] {ECO:0007744|PDB:6X1O, ECO:0007744|PDB:6X6U}
RP   X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR
RP   (4FE-4S) CLUSTER AND TUNGSTOPTERIN, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND SUBCELLULAR LOCATION.
RC   STRAIN=COM1;
RX   PubMed=36269456; DOI=10.1007/s00775-022-01965-0;
RA   Mathew L.G., Haja D.K., Pritchett C., McCormick W., Zeineddine R.,
RA   Fontenot L.S., Rivera M.E., Glushka J., Adams M.W.W., Lanzilotta W.N.;
RT   "An unprecedented function for a tungsten-containing oxidoreductase.";
RL   J. Biol. Inorg. Chem. 27:747-758(2022).
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 112-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;
CC         Evidence={ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};
CC       Note=Binds 1 [4Fe-4S] cluster per subunit (PubMed:16199576,
CC       PubMed:36269456). The [4Fe-4S] cluster has three cysteine ligands and
CC       one aspartic acid ligand (PubMed:36269456).
CC       {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 119-123`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=tungstopterin; Xref=ChEBI:CHEBI:30402;
CC         Evidence={ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};
CC       Note=Binds 1 tungstopterin cofactor per subunit.
CC       {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 92. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
