# EC_number_0017

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.97.1.14

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGSKETKNTSRRDFLIKGAGAAALGAGAFAISQVPLLEKLASANEDTVKDLLPFPELIESDEIIIRMQNDVRRALKKPLNEIQWIMVIDLKKCVGCSSCTVACVSENVLPPGVVYRPVIEEEIGTFPNVTKKFTPRPCMQCEHPPCTKVCPIGATYKSEDGIVAIDYDKCIGCRYCITACPYGARTFDWGEYHTENTPEIMQYEKEPNYEYGVERVREKKNSPIGNARKCHFCKHRLHKGMLSMCVTTCIGRATYIGDKNDPESLVAELIASPRVMRLKEELGTEPNVYYLT

[Multiple Choices]
A. 1.97.1.14
B. 1.97.1.13
C. 2.5.1.76
D. 2.7.1.52
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

> The exact sequence matches the UniProt entry annotated as selenate reductase subunit B with EC 1.97.1.14. The annotation is linked to a publication reporting characterization of the selenate reductase complex; this supports the key as an annotation, though it does not establish that the isolated subunit independently catalyzes the reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone offers no sufficiently specific, defensible basis to identify this protein's exact annotated EC number among the choices. Its motifs may suggest a metal-binding or redox-related protein, but do not establish the selenate reductase subunit identity or its precise reaction.


**Missing item-specific fact**

> The protein-specific annotation identifying this sequence as selenate reductase subunit B and assigning EC 1.97.1.14, or equivalent experimental information about its role in the selenate reductase complex.


**Reason**

> Choosing the exact four-part EC classification requires a protein-specific functional fact absent from the question. Recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports option A; the other choices specify different EC classifications. The caveat about assigning a complex reaction to a subunit does not make another listed choice better supported.


### Important caveats

- The reviewer-only database evidence was not supplied to the evaluated model.
- The linked publication concerns the respiratory selenate reductase complex; the available excerpts do not independently verify catalytic activity of isolated subunit B.
- The exact author source snapshot is unknown, although the sequence matches both the retrieved current entry and the checked historical entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone offers no sufficiently specific, defensible basis to identify this protein's exact annotated EC number among the choices. Its motifs may suggest a metal-binding or redox-related protein, but do not establish the selenate reductase subunit identity or its precise reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation identifying this sequence as selenate reductase subunit B and assigning EC 1.97.1.14, or equivalent experimental information about its role in the selenate reductase complex.",
    "reason": "Choosing the exact four-part EC classification requires a protein-specific functional fact absent from the question. Recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as selenate reductase subunit B with EC 1.97.1.14. The annotation is linked to a publication reporting characterization of the selenate reductase complex; this supports the key as an annotation, though it does not establish that the isolated subunit independently catalyzes the reaction."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not supplied to the evaluated model.",
    "The linked publication concerns the respiratory selenate reductase complex; the available excerpts do not independently verify catalytic activity of isolated subunit B.",
    "The exact author source snapshot is unknown, although the sequence matches both the retrieved current entry and the checked historical entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports option A; the other choices specify different EC classifications. The caveat about assigning a complex reaction to a subunit does not make another listed choice better supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as selenate reductase subunit B with EC 1.97.1.14. The annotation is linked to a publication reporting characterization of the selenate reductase complex; this supports the key as an annotation, though it does not establish that the isolated subunit independently catalyzes the reaction.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone offers no sufficiently specific, defensible basis to identify this protein's exact annotated EC number among the choices. Its motifs may suggest a metal-binding or redox-related protein, but do not establish the selenate reductase subunit identity or its precise reaction.",
    "missing_item_specific_fact": "The protein-specific annotation identifying this sequence as selenate reductase subunit B and assigning EC 1.97.1.14, or equivalent experimental information about its role in the selenate reductase complex.",
    "reason": "Choosing the exact four-part EC classification requires a protein-specific functional fact absent from the question. Recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports option A; the other choices specify different EC classifications. The caveat about assigning a complex reaction to a subunit does not make another listed choice better supported."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not supplied to the evaluated model.",
    "The linked publication concerns the respiratory selenate reductase complex; the available excerpts do not independently verify catalytic activity of isolated subunit B.",
    "The exact author source snapshot is unknown, although the sequence matches both the retrieved current entry and the checked historical entry."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0A8X5N4 (SRDB_MESS1, Selenate reductase subunit B) explicitly annotates EC=1.97.1.14 with catalytic reaction 'selenite + a quinone + H2O = selenate + a quinol'. The annotation is supported by reference PubMed:21357486 (Kuroda et al., 2011), which describes experimental characterization of the srdBCA operon encoding the respiratory selenate reductase complex, including 'FUNCTION AS A SELENATE REDUCTASE' and 'SUBUNIT' reference positions. The evidence code is ECO:0000305 (inferred by similarity), but the underlying reference reports experimental characterization of the complex. The sequence in the question matches the UniProt entry exactly (SHA256 confirmed).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple cysteine-rich motifs (e.g., CIGCRYCITACPYGART, CHFCKHRLHKGMLSMCVTTCIGRATYIGDK) consistent with iron-sulfur cluster coordination, and a glycine-rich N-terminal region (GAGAAALGAGAF) suggestive of a Rossmann-like nucleotide/flavin-binding fold. These features support an electron-transport oxidoreductase (EC class 1), which could plausibly eliminate the transferase options C (2.5.1.76) and D (2.7.1.52). However, both A (1.97.1.14) and B (1.97.1.13) belong to the same EC subclass 1.97.1 (oxidoreductases acting on other nitrogenous compounds as donors, with a quinone or similar compound as acceptor). No sequence motif or structural feature in the supplied 292-aa sequence specifically identifies selenate/selenite as the substrate rather than another nitrogenous compound, making the A-vs-B distinction impossible from general biological reasoning on the sequence alone.


**Missing item-specific fact**

> The specific substrate specificity of this protein (selenite/quinone couple) and its membership in the srdBCA operon of Mesobacillus selenatarsenatis, which together assign EC 1.97.1.14 rather than the adjacent 1.97.1.13. This requires either exact sequence-to-database lookup or memorization of the Kuroda et al. 2011 operon characterization.


**Reason**

> While sequence features (Fe-S clusters, glycine-rich region) weakly favor an oxidoreductase over a transferase, the critical discrimination between the two class-1 options (A vs B) cannot be made from the sequence. The answer depends on recognizing this specific protein's annotation or its operon context, which is an item-specific database fact absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 1.97.1.14 and 1.97.1.13 are oxidoreductases in the same EC subclass acting on nitrogenous compound donors with quinone acceptors. The sequence provides no motif or feature that uniquely identifies selenite/selenate as the substrate over another nitrogenous compound. Without the specific database annotation or operon context, a well-informed biologist could not confidently choose A over B from the sequence alone.


### Important caveats

- The UniProt evidence code is ECO:0000305 (inferred by similarity), not direct experimental measurement of this isolated subunit's catalytic activity; the experimental evidence pertains to the reconstituted srdBCA complex.
- The accession A0A0A8X5N4 and its annotation were identified by the reviewer from dataset metadata; they were not provided to the evaluated model.
- EC 1.97.1.13 is a very closely related number in the same subclass; its exact definition and whether it is a currently active EC entry should be verified, but its presence as a distractor makes the A-vs-B distinction particularly demanding without lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple cysteine-rich motifs (e.g., CIGCRYCITACPYGART, CHFCKHRLHKGMLSMCVTTCIGRATYIGDK) consistent with iron-sulfur cluster coordination, and a glycine-rich N-terminal region (GAGAAALGAGAF) suggestive of a Rossmann-like nucleotide/flavin-binding fold. These features support an electron-transport oxidoreductase (EC class 1), which could plausibly eliminate the transferase options C (2.5.1.76) and D (2.7.1.52). However, both A (1.97.1.14) and B (1.97.1.13) belong to the same EC subclass 1.97.1 (oxidoreductases acting on other nitrogenous compounds as donors, with a quinone or similar compound as acceptor). No sequence motif or structural feature in the supplied 292-aa sequence specifically identifies selenate/selenite as the substrate rather than another nitrogenous compound, making the A-vs-B distinction impossible from general biological reasoning on the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this protein (selenite/quinone couple) and its membership in the srdBCA operon of Mesobacillus selenatarsenatis, which together assign EC 1.97.1.14 rather than the adjacent 1.97.1.13. This requires either exact sequence-to-database lookup or memorization of the Kuroda et al. 2011 operon characterization.",
    "reason": "While sequence features (Fe-S clusters, glycine-rich region) weakly favor an oxidoreductase over a transferase, the critical discrimination between the two class-1 options (A vs B) cannot be made from the sequence. The answer depends on recognizing this specific protein's annotation or its operon context, which is an item-specific database fact absent from the input."
  },
  "case_id": "EC_number_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0A8X5N4 (SRDB_MESS1, Selenate reductase subunit B) explicitly annotates EC=1.97.1.14 with catalytic reaction 'selenite + a quinone + H2O = selenate + a quinol'. The annotation is supported by reference PubMed:21357486 (Kuroda et al., 2011), which describes experimental characterization of the srdBCA operon encoding the respiratory selenate reductase complex, including 'FUNCTION AS A SELENATE REDUCTASE' and 'SUBUNIT' reference positions. The evidence code is ECO:0000305 (inferred by similarity), but the underlying reference reports experimental characterization of the complex. The sequence in the question matches the UniProt entry exactly (SHA256 confirmed)."
  },
  "important_caveats": [
    "The UniProt evidence code is ECO:0000305 (inferred by similarity), not direct experimental measurement of this isolated subunit's catalytic activity; the experimental evidence pertains to the reconstituted srdBCA complex.",
    "The accession A0A0A8X5N4 and its annotation were identified by the reviewer from dataset metadata; they were not provided to the evaluated model.",
    "EC 1.97.1.13 is a very closely related number in the same subclass; its exact definition and whether it is a currently active EC entry should be verified, but its presence as a distractor makes the A-vs-B distinction particularly demanding without lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 1.97.1.14 and 1.97.1.13 are oxidoreductases in the same EC subclass acting on nitrogenous compound donors with quinone acceptors. The sequence provides no motif or feature that uniquely identifies selenite/selenate as the substrate over another nitrogenous compound. Without the specific database annotation or operon context, a well-informed biologist could not confidently choose A over B from the sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0A8X5N4 (SRDB_MESS1, Selenate reductase subunit B) explicitly annotates EC=1.97.1.14 with catalytic reaction 'selenite + a quinone + H2O = selenate + a quinol'. The annotation is supported by reference PubMed:21357486 (Kuroda et al., 2011), which describes experimental characterization of the srdBCA operon encoding the respiratory selenate reductase complex, including 'FUNCTION AS A SELENATE REDUCTASE' and 'SUBUNIT' reference positions. The evidence code is ECO:0000305 (inferred by similarity), but the underlying reference reports experimental characterization of the complex. The sequence in the question matches the UniProt entry exactly (SHA256 confirmed).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple cysteine-rich motifs (e.g., CIGCRYCITACPYGART, CHFCKHRLHKGMLSMCVTTCIGRATYIGDK) consistent with iron-sulfur cluster coordination, and a glycine-rich N-terminal region (GAGAAALGAGAF) suggestive of a Rossmann-like nucleotide/flavin-binding fold. These features support an electron-transport oxidoreductase (EC class 1), which could plausibly eliminate the transferase options C (2.5.1.76) and D (2.7.1.52). However, both A (1.97.1.14) and B (1.97.1.13) belong to the same EC subclass 1.97.1 (oxidoreductases acting on other nitrogenous compounds as donors, with a quinone or similar compound as acceptor). No sequence motif or structural feature in the supplied 292-aa sequence specifically identifies selenate/selenite as the substrate rather than another nitrogenous compound, making the A-vs-B distinction impossible from general biological reasoning on the sequence alone.",
    "missing_item_specific_fact": "The specific substrate specificity of this protein (selenite/quinone couple) and its membership in the srdBCA operon of Mesobacillus selenatarsenatis, which together assign EC 1.97.1.14 rather than the adjacent 1.97.1.13. This requires either exact sequence-to-database lookup or memorization of the Kuroda et al. 2011 operon characterization.",
    "reason": "While sequence features (Fe-S clusters, glycine-rich region) weakly favor an oxidoreductase over a transferase, the critical discrimination between the two class-1 options (A vs B) cannot be made from the sequence. The answer depends on recognizing this specific protein's annotation or its operon context, which is an item-specific database fact absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 1.97.1.14 and 1.97.1.13 are oxidoreductases in the same EC subclass acting on nitrogenous compound donors with quinone acceptors. The sequence provides no motif or feature that uniquely identifies selenite/selenate as the substrate over another nitrogenous compound. Without the specific database annotation or operon context, a well-informed biologist could not confidently choose A over B from the sequence alone."
  },
  "important_caveats": [
    "The UniProt evidence code is ECO:0000305 (inferred by similarity), not direct experimental measurement of this isolated subunit's catalytic activity; the experimental evidence pertains to the reconstituted srdBCA complex.",
    "The accession A0A0A8X5N4 and its annotation were identified by the reviewer from dataset metadata; they were not provided to the evaluated model.",
    "EC 1.97.1.13 is a very closely related number in the same subclass; its exact definition and whether it is a currently active EC entry should be verified, but its presence as a distractor makes the A-vs-B distinction particularly demanding without lookup."
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

**Accession:** `A0A0A8X5N4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 28. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:58.709600+00:00.  

```json
"A0A0A8X5N4"
```

Source SHA-256: `ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:58.709600+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Selenate reductase electron transport subunit"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"21357486","source":"PubMed"}],"value":"1.97.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Selenate reductase subunit B"}}}
```

Source SHA-256: `ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:58.709600+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.97.1.14","evidences":[{"evidenceCode":"ECO:0000305","id":"21357486","source":"PubMed"}],"name":"selenite + a quinone + H2O = selenate + a quinol","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:51636"},{"database":"ChEBI","id":"CHEBI:15075"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:18212"},{"database":"ChEBI","id":"CHEBI:24646"},{"database":"ChEBI","id":"CHEBI:132124"}]}}
```

Source SHA-256: `ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:58.709600+00:00.  

```json
{"citation":{"authors":["Kuroda M.","Yamashita M.","Miwa E.","Imao K.","Fujimoto N.","Ono H.","Nagano K.","Sei K.","Ike M."],"citationCrossReferences":[{"database":"PubMed","id":"21357486"},{"database":"DOI","id":"10.1128/jb.01197-10"}],"citationType":"journal article","firstPage":"2141","id":"21357486","journal":"J. Bacteriol.","lastPage":"2148","publicationDate":"2011","title":"Molecular cloning and characterization of the srdBCA operon, encoding the respiratory selenate reductase complex, from the selenate-reducing bacterium Bacillus selenatarsenatis SF-1.","volume":"193"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAJ83592.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"DSM 18680 / JCM 14380 / FERM P-15431 / SF-1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION AS A SELENATE REDUCTASE","SUBUNIT"]}
```

Source SHA-256: `ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:01.544310+00:00.  

```text
ID   SRDB_MESS1              Reviewed;         292 AA.
AC   A0A0A8X5N4; E9RFC9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   04-MAR-2015, sequence version 1.
DT   28-JAN-2026, entry version 28.
DE   RecName: Full=Selenate reductase subunit B {ECO:0000305};
DE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};
DE   AltName: Full=Selenate reductase electron transport subunit {ECO:0000305};
DE   Flags: Precursor;
GN   Name=srdB {ECO:0000303|PubMed:21357486};
GN   ORFNames=SAMD00020551_1550 {ECO:0000312|EMBL:GAM13406.1};
OS   Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431
OS   / SF-1).
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae;
OC   Mesobacillus.
OX   NCBI_TaxID=1321606;
```

Source SHA-256: `d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:01.544310+00:00.  

```text
DE   RecName: Full=Selenate reductase subunit B {ECO:0000305};
DE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};
DE   AltName: Full=Selenate reductase electron transport subunit {ECO:0000305};
DE   Flags: Precursor;
```

Source SHA-256: `d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)  
**Locator:** `lines 17-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:01.544310+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAJ83592.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION AS A SELENATE REDUCTASE, AND
RP   SUBUNIT.
RC   STRAIN=DSM 18680 / JCM 14380 / FERM P-15431 / SF-1;
RX   PubMed=21357486; DOI=10.1128/jb.01197-10;
RA   Kuroda M., Yamashita M., Miwa E., Imao K., Fujimoto N., Ono H., Nagano K.,
RA   Sei K., Ike M.;
RT   "Molecular cloning and characterization of the srdBCA operon, encoding the
RT   respiratory selenate reductase complex, from the selenate-reducing
RT   bacterium Bacillus selenatarsenatis SF-1.";
RL   J. Bacteriol. 193:2141-2148(2011).
```

Source SHA-256: `d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)  
**Locator:** `lines 42-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:01.544310+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=selenite + a quinone + H2O = selenate + a quinol;
CC         Xref=Rhea:RHEA:51636, ChEBI:CHEBI:15075, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:18212, ChEBI:CHEBI:24646, ChEBI:CHEBI:132124;
CC         EC=1.97.1.14; Evidence={ECO:0000305|PubMed:21357486};
```

Source SHA-256: `d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
