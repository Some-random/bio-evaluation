# EC_number_0186

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 5.6.2.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNLCNVNNYYLIIAEKSKAAKKIAEALSEKPILCRKYNVSYWIIKDHNSSKYVIVPAAGHLFGLKGESGFPVYDADWKPLWEIDKNSYYTKRYYQLISSLSKYALGFINACDYDIEGSVIGYLIIKNLGDIKKAKRMKFSALTKSDILSAFRNISALDYDMINAGIARHKIDWLWGINVSRALMISLQDFAKKRVILSAGRVQSPTLVQVVNSEIERNLFIPLPKFTVSIIVKIKDYSLNIKVNKEFEKITEAKEFLNKLINKTVKVVEVENRVRLLERPSPFNLTDLQIEAGRIYGISPYNVERIAEDLYLDGLISYPRTNSQKIPSTISIYNIIKGLENSSYRKLVDLVRKITGGKYVVKQGIKDDPAHPAIHPTGEAPKNLPNSKFKIYDLIARRFLGSVSADAKLSNTIYTLKVSDFPLEFTVSYTKILERNWLDIYHFHNVKEDKPIFLSKGDEGKIVDGKVNISLSKPTSRYTKVSLLKWMESSNLGTEATRGRIIEILVKRKYLTNNGRYIIPTKLGFYIAEILNKFFPDIVDVRMTADMESKLEMIKTGKVLESKVIKENIEKLNKFIEEYKVNKDKVGESLAKALGLIKIVKCKYCDLEQYKDGLCKYHYEAKVRLLDAVEIWKERTKYDHKKILKRISSSKSTGKYVKDIVTYMLSSE

[Multiple Choices]
A. 5.4.99.14
B. 2.3.1.322
C. 2.1.1.393
D. 5.6.2.1
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

> The supplied sequence exactly matches the cited 668-aa UniProt entry for DNA topoisomerase 3, which assigns EC 5.6.2.1 and links the catalytic-activity annotation to experimental evidence from two publications.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No specific catalytic activity or organism is given in the question. Identifying the protein as a topoisomerase from its sequence would require sequence-specific family recognition; the exact EC assignment depends on the protein's catalytic activity.


**Missing item-specific fact**

> That this exact sequence is DNA topoisomerase 3 with ATP-independent DNA strand passage activity, classified as EC 5.6.2.1.


**Reason**

> The sequence may support protein-family prediction with external homology or domain knowledge, but the input alone does not establish the exact catalytic reaction needed to choose the complete EC number.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched, experimentally supported annotation assigns EC 5.6.2.1; no evidence supports another listed option for this sequence.


### Important caveats

- The UniProt annotation is reviewer-only and was not available to the evaluated model.
- The historical record and current entry both match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No specific catalytic activity or organism is given in the question. Identifying the protein as a topoisomerase from its sequence would require sequence-specific family recognition; the exact EC assignment depends on the protein's catalytic activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this exact sequence is DNA topoisomerase 3 with ATP-independent DNA strand passage activity, classified as EC 5.6.2.1.",
    "reason": "The sequence may support protein-family prediction with external homology or domain knowledge, but the input alone does not establish the exact catalytic reaction needed to choose the complete EC number."
  },
  "case_id": "EC_number_0186",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited 668-aa UniProt entry for DNA topoisomerase 3, which assigns EC 5.6.2.1 and links the catalytic-activity annotation to experimental evidence from two publications."
  },
  "important_caveats": [
    "The UniProt annotation is reviewer-only and was not available to the evaluated model.",
    "The historical record and current entry both match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched, experimentally supported annotation assigns EC 5.6.2.1; no evidence supports another listed option for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0186",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited 668-aa UniProt entry for DNA topoisomerase 3, which assigns EC 5.6.2.1 and links the catalytic-activity annotation to experimental evidence from two publications.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No specific catalytic activity or organism is given in the question. Identifying the protein as a topoisomerase from its sequence would require sequence-specific family recognition; the exact EC assignment depends on the protein's catalytic activity.",
    "missing_item_specific_fact": "That this exact sequence is DNA topoisomerase 3 with ATP-independent DNA strand passage activity, classified as EC 5.6.2.1.",
    "reason": "The sequence may support protein-family prediction with external homology or domain knowledge, but the input alone does not establish the exact catalytic reaction needed to choose the complete EC number."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched, experimentally supported annotation assigns EC 5.6.2.1; no evidence supports another listed option for this sequence."
  },
  "important_caveats": [
    "The UniProt annotation is reviewer-only and was not available to the evaluated model.",
    "The historical record and current entry both match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q97ZJ8 (TOP3_SACS2, DNA topoisomerase 3 from Saccharolobus solfataricus) is annotated with EC 5.6.2.1, supported by experimental evidence (ECO:0000269) from PubMed 22722926 (Valenti et al., JBC 2012) and PubMed 29253195 (Bizard et al., NAR 2018). The catalytic activity is described as 'ATP-independent breakage of single-stranded DNA, followed by passage and rejoining.' The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed, 668 aa, sequence version 1). Both the current entry (v134) and the historical archived entry (v132, within the 2026-05-07 cutoff) carry the same EC annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a Cys-rich cluster ('CKYCDLEQYKDGLCKYHYEAK') consistent with the zinc-binding domain of type IA topoisomerases, and the overall ~668 aa length and domain architecture are compatible with an archaeal Topo III. These features could in principle help eliminate transferase options (B, C) and point toward an isomerase. However, distinguishing EC 5.6.2.1 (topoisomerase) from EC 5.4.99.14 (another isomerase class) purely from sequence requires recognizing the specific TOPRIM fold, catalytic tyrosine context, and C-terminal domain arrangement of a type IA topoisomerase — a protein-family-level identification that in practice depends on database matching or memorization of this specific entry.


**Missing item-specific fact**

> The specific identification of this 668-aa archaeal protein as DNA topoisomerase 3 (Topo III / TopA) of Saccharolobus solfataricus, and the knowledge that type IA topoisomerases (Topo I and Topo III) share EC 5.6.2.1, is required to select D over A with confidence. Without recognizing the exact protein family, the sequence alone does not provide a decisive argument for 5.6.2.1 over 5.4.99.14.


**Reason**

> While the zinc-binding motif and approximate size offer weak hints toward a topoisomerase, the final 4-digit EC assignment depends on identifying the protein as a type IA topoisomerase (Topo III) rather than another isomerase. This is a protein-family-level identification that, in the absence of database tools, effectively requires memorization of the specific entry or recognition of the exact sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span two EC classes (isomerases: A and D; transferases: B and C), so the transferase options are clearly wrong for a DNA-processing enzyme. Between the two isomerase options, 5.6.2.1 is well-established for type IA topoisomerases, while 5.4.99.14 is an extremely obscure (possibly non-standard or fabricated) EC number, making it a weak distractor. No genuine ambiguity exists among the options given the correct answer.


### Important caveats

- The EC 5.6.2.1 annotation is supported by experimental evidence (ECO:0000269) from two independent publications, not merely by computational prediction or similarity transfer.
- The identity origin note states the accession was inferred mechanically from dataset image-path metadata and was absent from the evaluated model input; the model sees only the raw sequence.
- EC 5.4.99.14 could not be independently verified as a currently valid EC number; if it is a fabricated or retired entry, option A is trivially eliminable, slightly increasing the effective reasoning support for D.
- The sequence is from a hyperthermophilic archaeon; thermophilic adaptations (e.g., increased salt-bridge density, compact folding) do not by themselves identify the enzyme class.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Cys-rich cluster ('CKYCDLEQYKDGLCKYHYEAK') consistent with the zinc-binding domain of type IA topoisomerases, and the overall ~668 aa length and domain architecture are compatible with an archaeal Topo III. These features could in principle help eliminate transferase options (B, C) and point toward an isomerase. However, distinguishing EC 5.6.2.1 (topoisomerase) from EC 5.4.99.14 (another isomerase class) purely from sequence requires recognizing the specific TOPRIM fold, catalytic tyrosine context, and C-terminal domain arrangement of a type IA topoisomerase — a protein-family-level identification that in practice depends on database matching or memorization of this specific entry.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this 668-aa archaeal protein as DNA topoisomerase 3 (Topo III / TopA) of Saccharolobus solfataricus, and the knowledge that type IA topoisomerases (Topo I and Topo III) share EC 5.6.2.1, is required to select D over A with confidence. Without recognizing the exact protein family, the sequence alone does not provide a decisive argument for 5.6.2.1 over 5.4.99.14.",
    "reason": "While the zinc-binding motif and approximate size offer weak hints toward a topoisomerase, the final 4-digit EC assignment depends on identifying the protein as a type IA topoisomerase (Topo III) rather than another isomerase. This is a protein-family-level identification that, in the absence of database tools, effectively requires memorization of the specific entry or recognition of the exact sequence."
  },
  "case_id": "EC_number_0186",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q97ZJ8 (TOP3_SACS2, DNA topoisomerase 3 from Saccharolobus solfataricus) is annotated with EC 5.6.2.1, supported by experimental evidence (ECO:0000269) from PubMed 22722926 (Valenti et al., JBC 2012) and PubMed 29253195 (Bizard et al., NAR 2018). The catalytic activity is described as 'ATP-independent breakage of single-stranded DNA, followed by passage and rejoining.' The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed, 668 aa, sequence version 1). Both the current entry (v134) and the historical archived entry (v132, within the 2026-05-07 cutoff) carry the same EC annotation."
  },
  "important_caveats": [
    "The EC 5.6.2.1 annotation is supported by experimental evidence (ECO:0000269) from two independent publications, not merely by computational prediction or similarity transfer.",
    "The identity origin note states the accession was inferred mechanically from dataset image-path metadata and was absent from the evaluated model input; the model sees only the raw sequence.",
    "EC 5.4.99.14 could not be independently verified as a currently valid EC number; if it is a fabricated or retired entry, option A is trivially eliminable, slightly increasing the effective reasoning support for D.",
    "The sequence is from a hyperthermophilic archaeon; thermophilic adaptations (e.g., increased salt-bridge density, compact folding) do not by themselves identify the enzyme class."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span two EC classes (isomerases: A and D; transferases: B and C), so the transferase options are clearly wrong for a DNA-processing enzyme. Between the two isomerase options, 5.6.2.1 is well-established for type IA topoisomerases, while 5.4.99.14 is an extremely obscure (possibly non-standard or fabricated) EC number, making it a weak distractor. No genuine ambiguity exists among the options given the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0186",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q97ZJ8 (TOP3_SACS2, DNA topoisomerase 3 from Saccharolobus solfataricus) is annotated with EC 5.6.2.1, supported by experimental evidence (ECO:0000269) from PubMed 22722926 (Valenti et al., JBC 2012) and PubMed 29253195 (Bizard et al., NAR 2018). The catalytic activity is described as 'ATP-independent breakage of single-stranded DNA, followed by passage and rejoining.' The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed, 668 aa, sequence version 1). Both the current entry (v134) and the historical archived entry (v132, within the 2026-05-07 cutoff) carry the same EC annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a Cys-rich cluster ('CKYCDLEQYKDGLCKYHYEAK') consistent with the zinc-binding domain of type IA topoisomerases, and the overall ~668 aa length and domain architecture are compatible with an archaeal Topo III. These features could in principle help eliminate transferase options (B, C) and point toward an isomerase. However, distinguishing EC 5.6.2.1 (topoisomerase) from EC 5.4.99.14 (another isomerase class) purely from sequence requires recognizing the specific TOPRIM fold, catalytic tyrosine context, and C-terminal domain arrangement of a type IA topoisomerase — a protein-family-level identification that in practice depends on database matching or memorization of this specific entry.",
    "missing_item_specific_fact": "The specific identification of this 668-aa archaeal protein as DNA topoisomerase 3 (Topo III / TopA) of Saccharolobus solfataricus, and the knowledge that type IA topoisomerases (Topo I and Topo III) share EC 5.6.2.1, is required to select D over A with confidence. Without recognizing the exact protein family, the sequence alone does not provide a decisive argument for 5.6.2.1 over 5.4.99.14.",
    "reason": "While the zinc-binding motif and approximate size offer weak hints toward a topoisomerase, the final 4-digit EC assignment depends on identifying the protein as a type IA topoisomerase (Topo III) rather than another isomerase. This is a protein-family-level identification that, in the absence of database tools, effectively requires memorization of the specific entry or recognition of the exact sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span two EC classes (isomerases: A and D; transferases: B and C), so the transferase options are clearly wrong for a DNA-processing enzyme. Between the two isomerase options, 5.6.2.1 is well-established for type IA topoisomerases, while 5.4.99.14 is an extremely obscure (possibly non-standard or fabricated) EC number, making it a weak distractor. No genuine ambiguity exists among the options given the correct answer."
  },
  "important_caveats": [
    "The EC 5.6.2.1 annotation is supported by experimental evidence (ECO:0000269) from two independent publications, not merely by computational prediction or similarity transfer.",
    "The identity origin note states the accession was inferred mechanically from dataset image-path metadata and was absent from the evaluated model input; the model sees only the raw sequence.",
    "EC 5.4.99.14 could not be independently verified as a currently valid EC number; if it is a fabricated or retired entry, option A is trivially eliminable, slightly increasing the effective reasoning support for D.",
    "The sequence is from a hyperthermophilic archaeon; thermophilic adaptations (e.g., increased salt-bridge density, compact folding) do not by themselves identify the enzyme class."
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

**Accession:** `Q97ZJ8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 132. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
"Q97ZJ8"
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29253195","source":"PubMed"}],"value":"DNA topoisomerase III"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22722926","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29253195","source":"PubMed"}],"value":"5.6.2.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22722926","source":"PubMed"}],"value":"DNA topoisomerase 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22722926","source":"PubMed"}],"value":"SsTop3"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"29253195","source":"PubMed"}],"value":"SsTopA"}]}}
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.6.2.1","evidences":[{"evidenceCode":"ECO:0000269","id":"22722926","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29253195","source":"PubMed"}],"name":"ATP-independent breakage of single-stranded DNA, followed by passage and rejoining."}}
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
{"citation":{"authors":["Valenti A.","De Felice M.","Perugino G.","Bizard A.","Nadal M.","Rossi M.","Ciaramella M."],"citationCrossReferences":[{"database":"PubMed","id":"22722926"},{"database":"DOI","id":"10.1074/jbc.m112.366377"}],"citationType":"journal article","firstPage":"30282","id":"22722926","journal":"J. Biol. Chem.","lastPage":"30295","publicationDate":"2012","title":"Synergic and opposing activities of thermophilic RecQ-like helicase and topoisomerase 3 proteins in Holliday junction processing and replication fork stabilization.","volume":"287"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBUNIT","INTERACTION WITH LHR","DNA-BINDING"]}
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
{"citation":{"authors":["Bizard A.H.","Yang X.","Debat H.","Fogg J.M.","Zechiedrich L.","Strick T.R.","Garnier F.","Nadal M."],"citationCrossReferences":[{"database":"PubMed","id":"29253195"},{"database":"DOI","id":"10.1093/nar/gkx1247"}],"citationType":"journal article","firstPage":"861","id":"29253195","journal":"Nucleic Acids Res.","lastPage":"872","publicationDate":"2018","title":"TopA, the Sulfolobus solfataricus topoisomerase III, is a decatenase.","volume":"46"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
ID   TOP3_SACS2              Reviewed;         668 AA.
AC   Q97ZJ8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2001, sequence version 1.
DT   28-JAN-2026, entry version 132.
DE   RecName: Full=DNA topoisomerase 3 {ECO:0000303|PubMed:22722926};
DE            Short=SsTop3 {ECO:0000303|PubMed:22722926};
DE            Short=SsTopA {ECO:0000303|PubMed:29253195};
DE            EC=5.6.2.1 {ECO:0000269|PubMed:22722926, ECO:0000269|PubMed:29253195};
DE   AltName: Full=DNA topoisomerase III {ECO:0000303|PubMed:29253195};
GN   Name=topA {ECO:0000303|PubMed:22722926, ECO:0000312|EMBL:AAK41190.1};
GN   OrderedLocusNames=SSO0907 {ECO:0000312|EMBL:AAK41190.1};
OS   Saccharolobus solfataricus (strain ATCC 35092 / DSM 1617 / JCM 11322 / P2)
OS   (Sulfolobus solfataricus).
OC   Archaea; Thermoproteota; Thermoprotei; Sulfolobales; Sulfolobaceae;
OC   Saccharolobus.
OX   NCBI_TaxID=273057;
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
DE   RecName: Full=DNA topoisomerase 3 {ECO:0000303|PubMed:22722926};
DE            Short=SsTop3 {ECO:0000303|PubMed:22722926};
DE            Short=SsTopA {ECO:0000303|PubMed:29253195};
DE            EC=5.6.2.1 {ECO:0000269|PubMed:22722926, ECO:0000269|PubMed:29253195};
DE   AltName: Full=DNA topoisomerase III {ECO:0000303|PubMed:29253195};
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, SUBUNIT, INTERACTION WITH LHR, AND
RP   DNA-BINDING.
RX   PubMed=22722926; DOI=10.1074/jbc.m112.366377;
RA   Valenti A., De Felice M., Perugino G., Bizard A., Nadal M., Rossi M.,
RA   Ciaramella M.;
RT   "Synergic and opposing activities of thermophilic RecQ-like helicase and
RT   topoisomerase 3 proteins in Holliday junction processing and replication
RT   fork stabilization.";
RL   J. Biol. Chem. 287:30282-30295(2012).
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 40-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=29253195; DOI=10.1093/nar/gkx1247;
RA   Bizard A.H., Yang X., Debat H., Fogg J.M., Zechiedrich L., Strick T.R.,
RA   Garnier F., Nadal M.;
RT   "TopA, the Sulfolobus solfataricus topoisomerase III, is a decatenase.";
RL   Nucleic Acids Res. 46:861-872(2018).
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 68-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP-independent breakage of single-stranded DNA, followed by
CC         passage and rejoining.; EC=5.6.2.1;
CC         Evidence={ECO:0000269|PubMed:22722926, ECO:0000269|PubMed:29253195};
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 186. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
