# EC_number_0165

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.7.11.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDKKEVQHHRSQQAMTKSLYAIGMGLLGKSATNMDCANTNLESAGKSSSTNYNRNRFYNERFVPMASGTMPSVSGTNHHSRHQQLLLQQAPKCTADLNEKLVKINRQNANKELSTIQAKDMQSVDKNEEALKELQESIPEINKIFDVHCRIGSGTFSTVLLGTLQRERGLVETQRRRFAIKHHNPTNHPERILRELECMYRIGGVENVIGINCCIRYNDNVAFIMPYMTHDRFHDIYRSLNFPEIRDYLRNLLIALRHVHKFNVIHRDVKPSNILYNRRTGKFLLCDFGLAQRIADDGSVVQSSDLSSREVFSILRDLENGRSVTLTDGNSAQAEAEDYMARRRMRALGGGGSVERAVTGPPSIQKLREQAGGHLTKKDVANQRADTMRLLNRLRLVSPNADPNNYVVSTNTSKKEMHASRAGTPGYRPPEVLLRYPKQSTAVDVWAAGVIMLSLLSGLHPFFKAPHDCGALAEIINLFGDMPVRKTAFLLDRLILLAQKVNTLDLRRVCMRFRHADFFLAPEIQRKYQRPDGTTEMCRSCEQPTFNCLCSNSGHNLERYDGLDIFPAVAYDLLSRLLEVNPQKRITAEEALKHPFFSDQHRITPGIPLHQQQLIMHQQQHIMQHQQHLQRSRETLPSSAARTLKAFVCYPMEITSTASQAAGNI

[Multiple Choices]
A. 2.7.11.11
B. 1.1.1.138
C. 2.7.11.1
D. 1.3.1.36
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

> The exact sequence matches a Drosophila protein annotated as a non-specific serine/threonine protein kinase with EC 2.7.11.1. The cited UniProt evidence is computational (PROSITE-ProRule), so it supports the key as an annotation but does not establish experimental validation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a protein-kinase catalytic domain, which supports a protein kinase rather than the oxidoreductase choices. That does not, by itself, establish the specific kinase subclass needed to distinguish 2.7.11.1 from 2.7.11.11.


**Missing item-specific fact**

> The protein-specific functional annotation or evidence establishing its kinase subclass and substrate specificity.


**Reason**

> The choices include two protein-kinase EC numbers. Sequence motifs can support the broad kinase class, but identifying the precise EC assignment relies on a protein-specific fact absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports C; no evidence supplied here establishes A as an alternative assignment. The issue is that the exact subclass is not determined by a general kinase-motif argument.


### Important caveats

- The matching historical and current UniProt annotations cite PROSITE-ProRule, a computational rule, rather than direct experimental evidence.
- Reviewer-only accession and database information was not available in the evaluated input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a protein-kinase catalytic domain, which supports a protein kinase rather than the oxidoreductase choices. That does not, by itself, establish the specific kinase subclass needed to distinguish 2.7.11.1 from 2.7.11.11.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or evidence establishing its kinase subclass and substrate specificity.",
    "reason": "The choices include two protein-kinase EC numbers. Sequence motifs can support the broad kinase class, but identifying the precise EC assignment relies on a protein-specific fact absent from the input."
  },
  "case_id": "EC_number_0165",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a Drosophila protein annotated as a non-specific serine/threonine protein kinase with EC 2.7.11.1. The cited UniProt evidence is computational (PROSITE-ProRule), so it supports the key as an annotation but does not establish experimental validation."
  },
  "important_caveats": [
    "The matching historical and current UniProt annotations cite PROSITE-ProRule, a computational rule, rather than direct experimental evidence.",
    "Reviewer-only accession and database information was not available in the evaluated input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports C; no evidence supplied here establishes A as an alternative assignment. The issue is that the exact subclass is not determined by a general kinase-motif argument."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0165",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a Drosophila protein annotated as a non-specific serine/threonine protein kinase with EC 2.7.11.1. The cited UniProt evidence is computational (PROSITE-ProRule), so it supports the key as an annotation but does not establish experimental validation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a protein-kinase catalytic domain, which supports a protein kinase rather than the oxidoreductase choices. That does not, by itself, establish the specific kinase subclass needed to distinguish 2.7.11.1 from 2.7.11.11.",
    "missing_item_specific_fact": "The protein-specific functional annotation or evidence establishing its kinase subclass and substrate specificity.",
    "reason": "The choices include two protein-kinase EC numbers. Sequence motifs can support the broad kinase class, but identifying the precise EC assignment relies on a protein-specific fact absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports C; no evidence supplied here establishes A as an alternative assignment. The issue is that the exact subclass is not determined by a general kinase-motif argument."
  },
  "important_caveats": [
    "The matching historical and current UniProt annotations cite PROSITE-ProRule, a computational rule, rather than direct experimental evidence.",
    "Reviewer-only accession and database information was not available in the evaluated input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9VJ90 (CDC7B_DROME) annotates this protein with EC 2.7.11.1 (non-specific serine/threonine protein kinase). The sequence (665 AA, Drosophila melanogaster) matches the benchmark sequence exactly. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU10027), a computational/prorule-based assignment rather than direct experimental measurement, but the sequence clearly displays canonical protein kinase domain hallmarks: a glycine-rich loop (GSGTFSTVLLGTL), the HRD catalytic motif (HRADFFLAPE), and a DFG-like region, all consistent with a Ser/Thr protein kinase. The catalytic activity comments confirm transfer of phosphate from ATP to Ser/Thr residues on protein substrates.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable protein kinase domain signatures: a GxGxxG glycine-rich loop (GSGTFSTVLLGTL), the HRD catalytic triad (HRADFF), and a DFG-like motif, confirming EC class 2.7 (transferase, transferring phosphorus-containing groups). This eliminates choices B (1.1.1.138, L-iditol 2-dehydrogenase, an oxidoreductase) and D (1.3.1.36, another oxidoreductase) outright. Between the two remaining kinase options, EC 2.7.11.11 (MAP4K) kinases characteristically possess additional regulatory domains (PH, SH3, or specific N-terminal extensions) flanking the kinase core, whereas the supplied sequence shows a single kinase domain embedded in a ~665-residue protein with only modest N- and C-terminal extensions and no PH/SH3 architecture. This domain organization is inconsistent with MAP4Ks and consistent with a general Ser/Thr kinase (EC 2.7.11.1).


**Missing item-specific fact**

> Precise subfamily assignment (e.g., recognizing this as a Cdc7/Dbf4-family kinase) would require knowing the specific protein identity or a database lookup; however, the absence of MAP4K-specific domain architecture provides a defensible positive argument for 2.7.11.1 over 2.7.11.11.


**Reason**

> The kinase domain identification and elimination of oxidoreductases (B, D) is straightforward sequence reasoning. The final A-vs-C distinction is supported by the absence of MAP4K-typical accessory domains and the overall single-kinase-domain architecture, which is a legitimate biological argument, though not as airtight as the B/D eliminations. The question is answerable by reasoning without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B and D are clearly eliminated by the kinase domain. Between A and C, the domain architecture argument (no PH/SH3, no MAP4K-specific features) meaningfully favors C. While EC 2.7.11.1 is a broad 'catch-all' category and a very careful expert might debate the exact EC sub-classification, the supplied choices make C the most defensible answer.


### Important caveats

- The EC 2.7.11.1 annotation is based on PROSITE-ProRule (ECO:0000255), a computational/prorule assignment, not direct experimental enzymatic characterization. This is standard for most kinase annotations in UniProt.
- EC 2.7.11.1 is a very broad 'non-specific Ser/Thr protein kinase' category; many kinases receive this number as a default when no more specific EC entry exists. The distinction from EC 2.7.11.11 (MAP4K) relies on domain architecture reasoning rather than a single unambiguous sequence motif.
- The reviewer-only evidence confirms sequence match and current annotation, but the evaluated model had no access to the UniProt entry, protein name, or accession.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase domain signatures: a GxGxxG glycine-rich loop (GSGTFSTVLLGTL), the HRD catalytic triad (HRADFF), and a DFG-like motif, confirming EC class 2.7 (transferase, transferring phosphorus-containing groups). This eliminates choices B (1.1.1.138, L-iditol 2-dehydrogenase, an oxidoreductase) and D (1.3.1.36, another oxidoreductase) outright. Between the two remaining kinase options, EC 2.7.11.11 (MAP4K) kinases characteristically possess additional regulatory domains (PH, SH3, or specific N-terminal extensions) flanking the kinase core, whereas the supplied sequence shows a single kinase domain embedded in a ~665-residue protein with only modest N- and C-terminal extensions and no PH/SH3 architecture. This domain organization is inconsistent with MAP4Ks and consistent with a general Ser/Thr kinase (EC 2.7.11.1).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise subfamily assignment (e.g., recognizing this as a Cdc7/Dbf4-family kinase) would require knowing the specific protein identity or a database lookup; however, the absence of MAP4K-specific domain architecture provides a defensible positive argument for 2.7.11.1 over 2.7.11.11.",
    "reason": "The kinase domain identification and elimination of oxidoreductases (B, D) is straightforward sequence reasoning. The final A-vs-C distinction is supported by the absence of MAP4K-typical accessory domains and the overall single-kinase-domain architecture, which is a legitimate biological argument, though not as airtight as the B/D eliminations. The question is answerable by reasoning without requiring memorization of this specific protein's database entry."
  },
  "case_id": "EC_number_0165",
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
    "reason": "UniProt entry Q9VJ90 (CDC7B_DROME) annotates this protein with EC 2.7.11.1 (non-specific serine/threonine protein kinase). The sequence (665 AA, Drosophila melanogaster) matches the benchmark sequence exactly. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU10027), a computational/prorule-based assignment rather than direct experimental measurement, but the sequence clearly displays canonical protein kinase domain hallmarks: a glycine-rich loop (GSGTFSTVLLGTL), the HRD catalytic motif (HRADFFLAPE), and a DFG-like region, all consistent with a Ser/Thr protein kinase. The catalytic activity comments confirm transfer of phosphate from ATP to Ser/Thr residues on protein substrates."
  },
  "important_caveats": [
    "The EC 2.7.11.1 annotation is based on PROSITE-ProRule (ECO:0000255), a computational/prorule assignment, not direct experimental enzymatic characterization. This is standard for most kinase annotations in UniProt.",
    "EC 2.7.11.1 is a very broad 'non-specific Ser/Thr protein kinase' category; many kinases receive this number as a default when no more specific EC entry exists. The distinction from EC 2.7.11.11 (MAP4K) relies on domain architecture reasoning rather than a single unambiguous sequence motif.",
    "The reviewer-only evidence confirms sequence match and current annotation, but the evaluated model had no access to the UniProt entry, protein name, or accession."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and D are clearly eliminated by the kinase domain. Between A and C, the domain architecture argument (no PH/SH3, no MAP4K-specific features) meaningfully favors C. While EC 2.7.11.1 is a broad 'catch-all' category and a very careful expert might debate the exact EC sub-classification, the supplied choices make C the most defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0165",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9VJ90 (CDC7B_DROME) annotates this protein with EC 2.7.11.1 (non-specific serine/threonine protein kinase). The sequence (665 AA, Drosophila melanogaster) matches the benchmark sequence exactly. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU10027), a computational/prorule-based assignment rather than direct experimental measurement, but the sequence clearly displays canonical protein kinase domain hallmarks: a glycine-rich loop (GSGTFSTVLLGTL), the HRD catalytic motif (HRADFFLAPE), and a DFG-like region, all consistent with a Ser/Thr protein kinase. The catalytic activity comments confirm transfer of phosphate from ATP to Ser/Thr residues on protein substrates.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase domain signatures: a GxGxxG glycine-rich loop (GSGTFSTVLLGTL), the HRD catalytic triad (HRADFF), and a DFG-like motif, confirming EC class 2.7 (transferase, transferring phosphorus-containing groups). This eliminates choices B (1.1.1.138, L-iditol 2-dehydrogenase, an oxidoreductase) and D (1.3.1.36, another oxidoreductase) outright. Between the two remaining kinase options, EC 2.7.11.11 (MAP4K) kinases characteristically possess additional regulatory domains (PH, SH3, or specific N-terminal extensions) flanking the kinase core, whereas the supplied sequence shows a single kinase domain embedded in a ~665-residue protein with only modest N- and C-terminal extensions and no PH/SH3 architecture. This domain organization is inconsistent with MAP4Ks and consistent with a general Ser/Thr kinase (EC 2.7.11.1).",
    "missing_item_specific_fact": "Precise subfamily assignment (e.g., recognizing this as a Cdc7/Dbf4-family kinase) would require knowing the specific protein identity or a database lookup; however, the absence of MAP4K-specific domain architecture provides a defensible positive argument for 2.7.11.1 over 2.7.11.11.",
    "reason": "The kinase domain identification and elimination of oxidoreductases (B, D) is straightforward sequence reasoning. The final A-vs-C distinction is supported by the absence of MAP4K-typical accessory domains and the overall single-kinase-domain architecture, which is a legitimate biological argument, though not as airtight as the B/D eliminations. The question is answerable by reasoning without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and D are clearly eliminated by the kinase domain. Between A and C, the domain architecture argument (no PH/SH3, no MAP4K-specific features) meaningfully favors C. While EC 2.7.11.1 is a broad 'catch-all' category and a very careful expert might debate the exact EC sub-classification, the supplied choices make C the most defensible answer."
  },
  "important_caveats": [
    "The EC 2.7.11.1 annotation is based on PROSITE-ProRule (ECO:0000255), a computational/prorule assignment, not direct experimental enzymatic characterization. This is standard for most kinase annotations in UniProt.",
    "EC 2.7.11.1 is a very broad 'non-specific Ser/Thr protein kinase' category; many kinases receive this number as a default when no more specific EC entry exists. The distinction from EC 2.7.11.11 (MAP4K) relies on domain architecture reasoning rather than a single unambiguous sequence motif.",
    "The reviewer-only evidence confirms sequence match and current annotation, but the evaluated model had no access to the UniProt entry, protein name, or accession."
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

**Accession:** `Q9VJ90` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 211. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
"Q9VJ90"
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0032677","source":"FlyBase"}],"value":"non-specific serine/threonine protein kinase"}}}
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
ID   CDC7B_DROME             Reviewed;         665 AA.
AC   Q9VJ90; Q8T0Q5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 211.
DE   RecName: Full=non-specific serine/threonine protein kinase {ECO:0000312|FlyBase:FBgn0032677};
DE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};
GN   ORFNames=CG5790 {ECO:0000312|FlyBase:FBgn0032677};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
DE   RecName: Full=non-specific serine/threonine protein kinase {ECO:0000312|FlyBase:FBgn0032677};
DE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 92-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 98-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 165. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
