# EC_number_0110

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.14.18.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTRQNVYELKDDTLSWYSRAVEEMKSRDINDPTSWWYQGAIHGYATYPSALTYWHDATGYPPSQQTVNSGFWNRCQHGTWYFLPWHRMYLFYFEEIVAKAIRDMGGPADWTLPYWNYCEAYNTSASPSNQQQALQIPPEFGSSQGPNADFASLWIKNRRNYVLNKNNVNPWPAMNEAEFTNSGGDISFGGGVTGFAHSGGQTGQLESLPHNVVHTDINGAMGNPDTAALDPIFWLHHANIDRLWQVWLAQAGRSNPVVNAWKDFRFKFHDANGQPVEIAVKDVETTQLLGYVYTPAFPLSSTTPARRSVPAMDVVGATSASFSVGDHMAPLDLTMVPQPARGARLLAARGGDEKRTILRISNVKGKGATSPIDLFITNRDNEEGNEENFVGCIGLFGLENASTPSVESDGSGLNFAIDISDTINKLRQRDDWDEDNIRVQLIPQSKQDSDVEINVGRVSLHSEID

[Multiple Choices]
A. 1.14.15.37
B. 2.3.1.31
C. 2.5.1.76
D. 1.14.18.1
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

> The exact sequence matches the UniProt entry annotated as tyrosinase HcTyr1 with EC 1.14.18.1. The entry cites experimental evidence for the enzyme's catalytic activity, including tyrosine oxidation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme with metal-binding catalytic residues, but that does not establish tyrosinase activity or distinguish EC 1.14.18.1 from the alternatives.


**Missing item-specific fact**

> The protein-specific identification and experimentally characterized catalytic activity of this sequence as a tyrosinase.


**Reason**

> The supplied sequence and choices do not provide a reliable biological basis for assigning the precise EC number; selecting D depends on protein-specific annotation or experimental knowledge absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence's experimental annotation supports D; the supplied evidence does not indicate another listed EC number is also defensible.


### Important caveats

- The reviewer-only UniProt annotation is sequence-matched and cites experimental evidence, but the cited primary study was not independently reviewed here.
- Reviewer-only identity and annotation evidence establish key support, not information available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme with metal-binding catalytic residues, but that does not establish tyrosinase activity or distinguish EC 1.14.18.1 from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and experimentally characterized catalytic activity of this sequence as a tyrosinase.",
    "reason": "The supplied sequence and choices do not provide a reliable biological basis for assigning the precise EC number; selecting D depends on protein-specific annotation or experimental knowledge absent from the input."
  },
  "case_id": "EC_number_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as tyrosinase HcTyr1 with EC 1.14.18.1. The entry cites experimental evidence for the enzyme's catalytic activity, including tyrosine oxidation."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation is sequence-matched and cites experimental evidence, but the cited primary study was not independently reviewed here.",
    "Reviewer-only identity and annotation evidence establish key support, not information available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's experimental annotation supports D; the supplied evidence does not indicate another listed EC number is also defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as tyrosinase HcTyr1 with EC 1.14.18.1. The entry cites experimental evidence for the enzyme's catalytic activity, including tyrosine oxidation.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme with metal-binding catalytic residues, but that does not establish tyrosinase activity or distinguish EC 1.14.18.1 from the alternatives.",
    "missing_item_specific_fact": "The protein-specific identification and experimentally characterized catalytic activity of this sequence as a tyrosinase.",
    "reason": "The supplied sequence and choices do not provide a reliable biological basis for assigning the precise EC number; selecting D depends on protein-specific annotation or experimental knowledge absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's experimental annotation supports D; the supplied evidence does not indicate another listed EC number is also defensible."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation is sequence-matched and cites experimental evidence, but the cited primary study was not independently reviewed here.",
    "Reviewer-only identity and annotation evidence establish key support, not information available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 466-aa sequence matches UniProt A0A261GRE4 (SHA256 confirmed, sequence version 1, Hahella sp. CCB-MM4). The entry is annotated as Tyrosinase HcTyr1 with EC 1.14.18.1, supported by experimental evidence (ECO:0000269, PubMed:39382070) including X-ray crystallography (PDB 8B74, 1.97 Å) and functional characterization of catalytic activities (L-tyrosine + O2 → L-dopaquinone + H2O; 2 L-tyrosine + O2 → 2 L-dopa; 2 L-dopa + O2 → 2 L-dopaquinone + 2 H2O). The annotation is experimentally grounded, not merely computational.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple conserved histidine residues in patterns characteristic of type-3 dicopper tyrosinases (e.g., HGY, HMAP, HSEID motifs), which coordinate the two copper ions in the tyrosinase active site. Tyrosinase is a well-known enzyme family whose EC number (1.14.18.1) is standard biochemistry knowledge. Options B (2.3.1.31, an acyltransferase) and C (2.5.1.76, an alkyl/aryl transferase) belong to EC class 2 (transferases) and can be eliminated by recognizing the protein as an oxidoreductase (EC class 1) based on its copper-binding architecture and lack of transferase motifs. Between A (1.14.15.37, a copper-containing monooxygenase sub-subclass) and D (1.14.18.1, tyrosinase), the specific histidine spacing and overall ~466-aa bacterial tyrosinase architecture favor the well-characterized tyrosinase family assignment. EC 1.14.15.37 is an extremely obscure or possibly non-standard entry, making it a weak distractor for a recognizable tyrosinase sequence.


**Missing item-specific fact**

> None critical. While the exact 4-digit EC assignment convention (1.14.18 vs 1.14.15) is a nomenclature fact, the tyrosinase EC number 1.14.18.1 is part of standard enzymology curricula, and the sequence-level tyrosinase signature (type-3 dicopper His motifs) provides a concrete biological basis for the assignment.


**Reason**

> The sequence displays recognizable tyrosinase family features (multiple conserved His residues in type-3 dicopper geometry, appropriate length for bacterial tyrosinase). Tyrosinase's EC number is well-established textbook knowledge. Transferase options are eliminable by enzyme-class reasoning. The remaining distinction (1.14.15.37 vs 1.14.18.1) is resolvable by recognizing the tyrosinase copper-binding signature, which is a concrete sequence-level argument rather than pure memorization of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are transferases (EC class 2), clearly incompatible with a copper-containing oxidoreductase. Option A (1.14.15.37) refers to a copper-containing monooxygenase sub-subclass, but the specific .37 entry is extremely obscure or potentially non-standard, and the sequence's histidine architecture matches the well-known tyrosinase family rather than other copper monooxygenases. D is the only well-supported and biochemically coherent choice.


### Important caveats

- The EC annotation is experimentally supported (PubMed:39382070, PDB:8B74), not purely computational, strengthening confidence in the key.
- EC 1.14.15.37's validity as a currently active EC number was not independently verified; if it is a fabricated or withdrawn entry, it serves as an easy distractor, slightly reducing the reasoning burden.
- The reviewer-only UniProt evidence confirms sequence match and annotation but was not available to the evaluated model; the reasoning assessment is based solely on what a knowledgeable model could extract from the raw sequence and general biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple conserved histidine residues in patterns characteristic of type-3 dicopper tyrosinases (e.g., HGY, HMAP, HSEID motifs), which coordinate the two copper ions in the tyrosinase active site. Tyrosinase is a well-known enzyme family whose EC number (1.14.18.1) is standard biochemistry knowledge. Options B (2.3.1.31, an acyltransferase) and C (2.5.1.76, an alkyl/aryl transferase) belong to EC class 2 (transferases) and can be eliminated by recognizing the protein as an oxidoreductase (EC class 1) based on its copper-binding architecture and lack of transferase motifs. Between A (1.14.15.37, a copper-containing monooxygenase sub-subclass) and D (1.14.18.1, tyrosinase), the specific histidine spacing and overall ~466-aa bacterial tyrosinase architecture favor the well-characterized tyrosinase family assignment. EC 1.14.15.37 is an extremely obscure or possibly non-standard entry, making it a weak distractor for a recognizable tyrosinase sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While the exact 4-digit EC assignment convention (1.14.18 vs 1.14.15) is a nomenclature fact, the tyrosinase EC number 1.14.18.1 is part of standard enzymology curricula, and the sequence-level tyrosinase signature (type-3 dicopper His motifs) provides a concrete biological basis for the assignment.",
    "reason": "The sequence displays recognizable tyrosinase family features (multiple conserved His residues in type-3 dicopper geometry, appropriate length for bacterial tyrosinase). Tyrosinase's EC number is well-established textbook knowledge. Transferase options are eliminable by enzyme-class reasoning. The remaining distinction (1.14.15.37 vs 1.14.18.1) is resolvable by recognizing the tyrosinase copper-binding signature, which is a concrete sequence-level argument rather than pure memorization of a database entry."
  },
  "case_id": "EC_number_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied 466-aa sequence matches UniProt A0A261GRE4 (SHA256 confirmed, sequence version 1, Hahella sp. CCB-MM4). The entry is annotated as Tyrosinase HcTyr1 with EC 1.14.18.1, supported by experimental evidence (ECO:0000269, PubMed:39382070) including X-ray crystallography (PDB 8B74, 1.97 Å) and functional characterization of catalytic activities (L-tyrosine + O2 → L-dopaquinone + H2O; 2 L-tyrosine + O2 → 2 L-dopa; 2 L-dopa + O2 → 2 L-dopaquinone + 2 H2O). The annotation is experimentally grounded, not merely computational."
  },
  "important_caveats": [
    "The EC annotation is experimentally supported (PubMed:39382070, PDB:8B74), not purely computational, strengthening confidence in the key.",
    "EC 1.14.15.37's validity as a currently active EC number was not independently verified; if it is a fabricated or withdrawn entry, it serves as an easy distractor, slightly reducing the reasoning burden.",
    "The reviewer-only UniProt evidence confirms sequence match and annotation but was not available to the evaluated model; the reasoning assessment is based solely on what a knowledgeable model could extract from the raw sequence and general biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are transferases (EC class 2), clearly incompatible with a copper-containing oxidoreductase. Option A (1.14.15.37) refers to a copper-containing monooxygenase sub-subclass, but the specific .37 entry is extremely obscure or potentially non-standard, and the sequence's histidine architecture matches the well-known tyrosinase family rather than other copper monooxygenases. D is the only well-supported and biochemically coherent choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 466-aa sequence matches UniProt A0A261GRE4 (SHA256 confirmed, sequence version 1, Hahella sp. CCB-MM4). The entry is annotated as Tyrosinase HcTyr1 with EC 1.14.18.1, supported by experimental evidence (ECO:0000269, PubMed:39382070) including X-ray crystallography (PDB 8B74, 1.97 Å) and functional characterization of catalytic activities (L-tyrosine + O2 → L-dopaquinone + H2O; 2 L-tyrosine + O2 → 2 L-dopa; 2 L-dopa + O2 → 2 L-dopaquinone + 2 H2O). The annotation is experimentally grounded, not merely computational.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H1", "H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple conserved histidine residues in patterns characteristic of type-3 dicopper tyrosinases (e.g., HGY, HMAP, HSEID motifs), which coordinate the two copper ions in the tyrosinase active site. Tyrosinase is a well-known enzyme family whose EC number (1.14.18.1) is standard biochemistry knowledge. Options B (2.3.1.31, an acyltransferase) and C (2.5.1.76, an alkyl/aryl transferase) belong to EC class 2 (transferases) and can be eliminated by recognizing the protein as an oxidoreductase (EC class 1) based on its copper-binding architecture and lack of transferase motifs. Between A (1.14.15.37, a copper-containing monooxygenase sub-subclass) and D (1.14.18.1, tyrosinase), the specific histidine spacing and overall ~466-aa bacterial tyrosinase architecture favor the well-characterized tyrosinase family assignment. EC 1.14.15.37 is an extremely obscure or possibly non-standard entry, making it a weak distractor for a recognizable tyrosinase sequence.",
    "missing_item_specific_fact": "None critical. While the exact 4-digit EC assignment convention (1.14.18 vs 1.14.15) is a nomenclature fact, the tyrosinase EC number 1.14.18.1 is part of standard enzymology curricula, and the sequence-level tyrosinase signature (type-3 dicopper His motifs) provides a concrete biological basis for the assignment.",
    "reason": "The sequence displays recognizable tyrosinase family features (multiple conserved His residues in type-3 dicopper geometry, appropriate length for bacterial tyrosinase). Tyrosinase's EC number is well-established textbook knowledge. Transferase options are eliminable by enzyme-class reasoning. The remaining distinction (1.14.15.37 vs 1.14.18.1) is resolvable by recognizing the tyrosinase copper-binding signature, which is a concrete sequence-level argument rather than pure memorization of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are transferases (EC class 2), clearly incompatible with a copper-containing oxidoreductase. Option A (1.14.15.37) refers to a copper-containing monooxygenase sub-subclass, but the specific .37 entry is extremely obscure or potentially non-standard, and the sequence's histidine architecture matches the well-known tyrosinase family rather than other copper monooxygenases. D is the only well-supported and biochemically coherent choice."
  },
  "important_caveats": [
    "The EC annotation is experimentally supported (PubMed:39382070, PDB:8B74), not purely computational, strengthening confidence in the key.",
    "EC 1.14.15.37's validity as a currently active EC number was not independently verified; if it is a fabricated or withdrawn entry, it serves as an easy distractor, slightly reducing the reasoning burden.",
    "The reviewer-only UniProt evidence confirms sequence match and annotation but was not available to the evaluated model; the reasoning assessment is based solely on what a knowledgeable model could extract from the raw sequence and general biochemistry."
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

**Accession:** `A0A261GRE4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 24. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.415551+00:00.  

```json
"A0A261GRE4"
```

Source SHA-256: `00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.415551+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"value":"1.14.18.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39382070","source":"PubMed"}],"value":"Tyrosinase HcTyr1"}}}
```

Source SHA-256: `00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.415551+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.14.18.1","evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"name":"L-tyrosine + O2 = L-dopaquinone + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:18117"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:57924"},{"database":"ChEBI","id":"CHEBI:58315"}]}}
```

Source SHA-256: `00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.415551+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"name":"2 L-tyrosine + O2 = 2 L-dopa","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:34283"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:57504"},{"database":"ChEBI","id":"CHEBI:58315"}]}}
```

Source SHA-256: `00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.415551+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.14.18.1","evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"name":"2 L-dopa + O2 = 2 L-dopaquinone + 2 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:34287"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:57504"},{"database":"ChEBI","id":"CHEBI:57924"}]}}
```

Source SHA-256: `00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.415551+00:00.  

```json
{"citation":{"authors":["de Almeida Santos G.","Englund A.N.B.","Dalleywater E.L.","Roehr A.K."],"citationCrossReferences":[{"database":"PubMed","id":"39382070"},{"database":"DOI","id":"10.1002/2211-5463.13906"}],"citationType":"journal article","firstPage":"0","id":"39382070","journal":"FEBS Open Bio","lastPage":"0","publicationDate":"2024","title":"Characterization of two bacterial tyrosinases from the halophilic bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in wetlands.","volume":"0"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8B74","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"CCB-MM4"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.97 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN","AUTO-CLEAVAGE"]}
```

Source SHA-256: `00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 24 / 1.  
**Retrieved:** 2026-11-01T06:27:24.781945+00:00.  

```text
ID   TYR1_HAHS4              Reviewed;         466 AA.
AC   A0A261GRE4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-DEC-2017, sequence version 1.
DT   28-JAN-2026, entry version 24.
DE   RecName: Full=Tyrosinase HcTyr1 {ECO:0000303|PubMed:39382070};
DE            EC=1.14.18.1 {ECO:0000269|PubMed:39382070};
GN   ORFNames=BTA51_09820 {ECO:0000312|EMBL:OZG74058.1};
OS   Hahella sp. (strain CCB-MM4).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Oceanospirillales; Hahellaceae; Hahella.
OX   NCBI_TaxID=1926491;
```

Source SHA-256: `68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 24 / 1.  
**Retrieved:** 2026-11-01T06:27:24.781945+00:00.  

```text
DE   RecName: Full=Tyrosinase HcTyr1 {ECO:0000303|PubMed:39382070};
DE            EC=1.14.18.1 {ECO:0000269|PubMed:39382070};
```

Source SHA-256: `68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)  
**Locator:** `lines 21-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 24 / 1.  
**Retrieved:** 2026-11-01T06:27:24.781945+00:00.  

```text
RN   [2] {ECO:0007744|PDB:8B74}
RP   X-RAY CRYSTALLOGRAPHY (1.97 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,
RP   COFACTOR, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT,
RP   DOMAIN, AND AUTO-CLEAVAGE.
RC   STRAIN=CCB-MM4;
RX   PubMed=39382070; DOI=10.1002/2211-5463.13906;
RA   de Almeida Santos G., Englund A.N.B., Dalleywater E.L., Roehr A.K.;
RT   "Characterization of two bacterial tyrosinases from the halophilic
RT   bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in
RT   wetlands.";
RL   FEBS Open Bio 0:0-0(2024).
```

Source SHA-256: `68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)  
**Locator:** `lines 38-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 24 / 1.  
**Retrieved:** 2026-11-01T06:27:24.781945+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-tyrosine + O2 = L-dopaquinone + H2O; Xref=Rhea:RHEA:18117,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15379, ChEBI:CHEBI:57924,
CC         ChEBI:CHEBI:58315; EC=1.14.18.1;
CC         Evidence={ECO:0000269|PubMed:39382070};
```

Source SHA-256: `68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)  
**Locator:** `lines 43-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 24 / 1.  
**Retrieved:** 2026-11-01T06:27:24.781945+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 L-tyrosine + O2 = 2 L-dopa; Xref=Rhea:RHEA:34283,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:57504, ChEBI:CHEBI:58315;
CC         Evidence={ECO:0000269|PubMed:39382070};
```

Source SHA-256: `68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)  
**Locator:** `lines 47-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 24 / 1.  
**Retrieved:** 2026-11-01T06:27:24.781945+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 L-dopa + O2 = 2 L-dopaquinone + 2 H2O; Xref=Rhea:RHEA:34287,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15379, ChEBI:CHEBI:57504,
CC         ChEBI:CHEBI:57924; EC=1.14.18.1;
CC         Evidence={ECO:0000269|PubMed:39382070};
```

Source SHA-256: `68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 110. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
