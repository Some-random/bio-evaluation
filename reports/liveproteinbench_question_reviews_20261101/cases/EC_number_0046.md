# EC_number_0046

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 4.2.1.183

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSKPAAAAPSDPSKPSKPLKEVPGSYGLPVLGAVKDRLDFYWFQGDTEFFRIRMEQHKSTVFRVNYSPGPPGYPDSRGIILLDQKSFSVLLDNSKVDKSDTLLGPYIPNLAFTGGYRVLPYLDTSEAKHTAYKDLIFELLHVNSSRIIPEYNKVFAETAGSWEERIAKSGKAEVFASSDSMITKFLLRTIVHKDPAEPGPASLGPKFRDTYQLWTGVNFAGIAHTPLPHFLEELLFHTFRLPPFLVKKQYKALANFYRTHATEVLDLAEKKYGLDREETVHQLILILGINARLGLHKMIPALIYYLGLLGEDFQAKIAAEVRSAVHKNRAQGEEGVNITTQALLEMPLLRSTVLETLRLTPSIFYIYGRAREDMVIESHDAAFQIKKGELLGGHQYFVMRDPEVFEEPHKFVADRFLGERGKAVLPYLVWSNGRETESPSSSNKQCPAKDVAELITMQFVAEMFLRYDSFEITKDSFINTTELNVHLKSLKKRSV

[Multiple Choices]
A. 4.2.1.70
B. 2.3.1.319
C. 4.2.1.183
D. 2.1.2.1
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

> The supplied sequence exactly matches the 495-aa UniProt entry for CYP74M3. That entry assigns EC 4.2.1.183 to two catalytic reactions and cites PubMed evidence with ECO:0000269, supporting the keyed answer for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support broad family-level inference, but the input provides no reaction, substrate, or functional context that distinguishes this enzyme's specific EC assignment from the other choices.


**Missing item-specific fact**

> The protein-specific identification as CYP74M3 and its experimentally supported divinyl ether synthase reactions, which map to EC 4.2.1.183.


**Reason**

> The exact EC choice depends on knowing the specific catalytic activity of this protein. That annotation or experimental fact is absent from the question; recognizing the sequence from a database would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched annotation supports EC 4.2.1.183; no evidence supplied here supports another listed choice for this protein.


### Important caveats

- The functional evidence is reported through a UniProt annotation citing a 2016 publication; the primary paper was not independently reviewed here.
- Reviewer-only database evidence supports the key but was absent from the evaluated question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support broad family-level inference, but the input provides no reaction, substrate, or functional context that distinguishes this enzyme's specific EC assignment from the other choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as CYP74M3 and its experimentally supported divinyl ether synthase reactions, which map to EC 4.2.1.183.",
    "reason": "The exact EC choice depends on knowing the specific catalytic activity of this protein. That annotation or experimental fact is absent from the question; recognizing the sequence from a database would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 495-aa UniProt entry for CYP74M3. That entry assigns EC 4.2.1.183 to two catalytic reactions and cites PubMed evidence with ECO:0000269, supporting the keyed answer for this sequence."
  },
  "important_caveats": [
    "The functional evidence is reported through a UniProt annotation citing a 2016 publication; the primary paper was not independently reviewed here.",
    "Reviewer-only database evidence supports the key but was absent from the evaluated question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports EC 4.2.1.183; no evidence supplied here supports another listed choice for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 495-aa UniProt entry for CYP74M3. That entry assigns EC 4.2.1.183 to two catalytic reactions and cites PubMed evidence with ECO:0000269, supporting the keyed answer for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support broad family-level inference, but the input provides no reaction, substrate, or functional context that distinguishes this enzyme's specific EC assignment from the other choices.",
    "missing_item_specific_fact": "The protein-specific identification as CYP74M3 and its experimentally supported divinyl ether synthase reactions, which map to EC 4.2.1.183.",
    "reason": "The exact EC choice depends on knowing the specific catalytic activity of this protein. That annotation or experimental fact is absent from the question; recognizing the sequence from a database would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports EC 4.2.1.183; no evidence supplied here supports another listed choice for this protein."
  },
  "important_caveats": [
    "The functional evidence is reported through a UniProt annotation citing a 2016 publication; the primary paper was not independently reviewed here.",
    "Reviewer-only database evidence supports the key but was absent from the evaluated question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry D8QZ31 (C74M3_SELML, Selaginella moellendorffii, 495 AA). The entry is annotated as 'Divinyl ether synthase CYP74M3' with EC 4.2.1.183, supported by experimental evidence (ECO:0000269) from PubMed:26776054 (Gorina et al., 2016, Biochim. Biophys. Acta 1861:301-309). Two catalytic activities are confirmed: (13S)-hydroperoxy-(9Z,11E)-octadecadienoate → etheroleate + H2O and (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate → etherolenate + H2O, both under EC 4.2.1.183.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model might recognize P450-like features (sequence length ~495 aa, aromatic-rich regions, potential heme-binding FxxGxxxCxG-like motif in the C-terminal region) to tentatively classify this as a cytochrome P450. CYP74-family P450s function as hydro-lyases (EC 4.2.1.x) on fatty acid hydroperoxides, which could eliminate the transferase options B (2.3.1.319) and D (2.1.2.1). However, this still leaves two hydro-lyase options (A: 4.2.1.70 and C: 4.2.1.183), and distinguishing between them requires knowing the specific CYP74 subfamily (M vs A vs B) and its assigned product specificity (divinyl ether vs allene oxide vs vinyl ether vs other).


**Missing item-specific fact**

> The specific EC number assignment 4.2.1.183 to CYP74M (divinyl ether synthase) versus other CYP74 subfamily EC numbers (e.g., 4.2.1.92 for allene oxide synthase, 4.2.1.182 for vinyl ether synthase) is a database/literature annotation fact. Without knowing that this particular sequence belongs to the CYP74M subfamily and that this subfamily is assigned EC 4.2.1.183, the sequence alone does not reveal the exact product (etheroleate/etherolenate) to distinguish it from other hydro-lyase EC numbers.


**Reason**

> The question provides only a raw amino acid sequence with no organism context, no substrate information, and no functional annotation. While broad P450 recognition might narrow the class, the final step—choosing 4.2.1.183 over 4.2.1.70—depends entirely on memorizing or looking up the specific EC assignment for CYP74M divinyl ether synthase. No general biochemical reasoning from the sequence determines the exact 4-digit EC suffix.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> If one accepts the premise that this is a CYP74 hydro-lyase, only option C (4.2.1.183) corresponds to a known CYP74M/divinyl ether synthase EC number. Option A (4.2.1.70) does not correspond to a well-characterized CYP74 enzyme in standard EC databases. Options B and D are transferases inconsistent with P450 catalysis. Thus, among the four choices, C is the only one consistent with a CYP74-family hydro-lyase, reducing ambiguity if P450 recognition is achieved.


### Important caveats

- The EC number 4.2.1.183 was assigned relatively recently (entry first public 2025-06-18 per current UniProt; the supporting paper is from 2016). The author's source snapshot date is unknown, but the historical entry (v68, released Jan 2026) already contains this annotation.
- The evidence code ECO:0000269 indicates experimental determination (heterologous expression and product analysis in the cited paper), not mere computational prediction.
- Option A (4.2.1.70) may not correspond to a valid or well-known EC number, making it a weak distractor for a knowledgeable model but potentially confusing for one relying on pattern-matching of EC number formats.
- Sequence identity to D8QZ31 is exact (SHA-256 match), confirming the annotation applies to this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model might recognize P450-like features (sequence length ~495 aa, aromatic-rich regions, potential heme-binding FxxGxxxCxG-like motif in the C-terminal region) to tentatively classify this as a cytochrome P450. CYP74-family P450s function as hydro-lyases (EC 4.2.1.x) on fatty acid hydroperoxides, which could eliminate the transferase options B (2.3.1.319) and D (2.1.2.1). However, this still leaves two hydro-lyase options (A: 4.2.1.70 and C: 4.2.1.183), and distinguishing between them requires knowing the specific CYP74 subfamily (M vs A vs B) and its assigned product specificity (divinyl ether vs allene oxide vs vinyl ether vs other).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific EC number assignment 4.2.1.183 to CYP74M (divinyl ether synthase) versus other CYP74 subfamily EC numbers (e.g., 4.2.1.92 for allene oxide synthase, 4.2.1.182 for vinyl ether synthase) is a database/literature annotation fact. Without knowing that this particular sequence belongs to the CYP74M subfamily and that this subfamily is assigned EC 4.2.1.183, the sequence alone does not reveal the exact product (etheroleate/etherolenate) to distinguish it from other hydro-lyase EC numbers.",
    "reason": "The question provides only a raw amino acid sequence with no organism context, no substrate information, and no functional annotation. While broad P450 recognition might narrow the class, the final step—choosing 4.2.1.183 over 4.2.1.70—depends entirely on memorizing or looking up the specific EC assignment for CYP74M divinyl ether synthase. No general biochemical reasoning from the sequence determines the exact 4-digit EC suffix."
  },
  "case_id": "EC_number_0046",
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
    "reason": "The sequence matches UniProt entry D8QZ31 (C74M3_SELML, Selaginella moellendorffii, 495 AA). The entry is annotated as 'Divinyl ether synthase CYP74M3' with EC 4.2.1.183, supported by experimental evidence (ECO:0000269) from PubMed:26776054 (Gorina et al., 2016, Biochim. Biophys. Acta 1861:301-309). Two catalytic activities are confirmed: (13S)-hydroperoxy-(9Z,11E)-octadecadienoate → etheroleate + H2O and (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate → etherolenate + H2O, both under EC 4.2.1.183."
  },
  "important_caveats": [
    "The EC number 4.2.1.183 was assigned relatively recently (entry first public 2025-06-18 per current UniProt; the supporting paper is from 2016). The author's source snapshot date is unknown, but the historical entry (v68, released Jan 2026) already contains this annotation.",
    "The evidence code ECO:0000269 indicates experimental determination (heterologous expression and product analysis in the cited paper), not mere computational prediction.",
    "Option A (4.2.1.70) may not correspond to a valid or well-known EC number, making it a weak distractor for a knowledgeable model but potentially confusing for one relying on pattern-matching of EC number formats.",
    "Sequence identity to D8QZ31 is exact (SHA-256 match), confirming the annotation applies to this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "If one accepts the premise that this is a CYP74 hydro-lyase, only option C (4.2.1.183) corresponds to a known CYP74M/divinyl ether synthase EC number. Option A (4.2.1.70) does not correspond to a well-characterized CYP74 enzyme in standard EC databases. Options B and D are transferases inconsistent with P450 catalysis. Thus, among the four choices, C is the only one consistent with a CYP74-family hydro-lyase, reducing ambiguity if P450 recognition is achieved."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"EC_number_0046","expected_answer_check":{"judgment":"supported","reason":"The sequence matches UniProt entry D8QZ31 (C74M3_SELML, Selaginella moellendorffii, 495 AA). The entry is annotated as 'Divinyl ether synthase CYP74M3' with EC 4.2.1.183, supported by experimental evidence (ECO:0000269) from PubMed:26776054 (Gorina et al., 2016, Biochim. Biophys. Acta 1861:301-309). Two catalytic activities are confirmed: (13S)-hydroperoxy-(9Z,11E)-octadecadienoate → etheroleate + H2O and (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate → etherolenate + H2O, both under EC 4.2.1.183.","evidence_ids":["C1","C4","C5","C6","C7","H1","H2","H3","H4","H5"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"A knowledgeable model might recognize P450-like features (sequence length ~495 aa, aromatic-rich regions, potential heme-binding FxxGxxxCxG-like motif in the C-terminal region) to tentatively classify this as a cytochrome P450. CYP74-family P450s function as hydro-lyases (EC 4.2.1.x) on fatty acid hydroperoxides, which could eliminate the transferase options B (2.3.1.319) and D (2.1.2.1). However, this still leaves two hydro-lyase options (A: 4.2.1.70 and C: 4.2.1.183), and distinguishing between them requires knowing the specific CYP74 subfamily (M vs A vs B) and its assigned product specificity (divinyl ether vs allene oxide vs vinyl ether vs other).","missing_item_specific_fact":"The specific EC number assignment 4.2.1.183 to CYP74M (divinyl ether synthase) versus other CYP74 subfamily EC numbers (e.g., 4.2.1.92 for allene oxide synthase, 4.2.1.182 for vinyl ether synthase) is a database/literature annotation fact. Without knowing that this particular sequence belongs to the CYP74M subfamily and that this subfamily is assigned EC 4.2.1.183, the sequence alone does not reveal the exact product (etheroleate/etherolenate) to distinguish it from other hydro-lyase EC numbers.","reason":"The question provides only a raw amino acid sequence with no organism context, no substrate information, and no functional annotation. While broad P450 recognition might narrow the class, the final step—choosing 4.2.1.183 over 4.2.1.70—depends entirely on memorizing or looking up the specific EC assignment for CYP74M divinyl ether synthase. No general biochemical reasoning from the sequence determines the exact 4-digit EC suffix."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"If one accepts the premise that this is a CYP74 hydro-lyase, only option C (4.2.1.183) corresponds to a known CYP74M/divinyl ether synthase EC number. Option A (4.2.1.70) does not correspond to a well-characterized CYP74 enzyme in standard EC databases. Options B and D are transferases inconsistent with P450 catalysis. Thus, among the four choices, C is the only one consistent with a CYP74-family hydro-lyase, reducing ambiguity if P450 recognition is achieved."},"important_caveats":["The EC number 4.2.1.183 was assigned relatively recently (entry first public 2025-06-18 per current UniProt; the supporting paper is from 2016). The author's source snapshot date is unknown, but the historical entry (v68, released Jan 2026) already contains this annotation.","The evidence code ECO:0000269 indicates experimental determination (heterologous expression and product analysis in the cited paper), not mere computational prediction.","Option A (4.2.1.70) may not correspond to a valid or well-known EC number, making it a weak distractor for a knowledgeable model but potentially confusing for one relying on pattern-matching of EC number formats.","Sequence identity to D8QZ31 is exact (SHA-256 match), confirming the annotation applies to this exact protein."]}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `D8QZ31` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 68. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:50.224082+00:00.  

```json
"D8QZ31"
```

Source SHA-256: `bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:50.224082+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26776054","source":"PubMed"}],"value":"4.2.1.183"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"26776054","source":"PubMed"}],"value":"Etheroleic acid synthase CYP74M3"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26776054","source":"PubMed"}],"value":"Divinyl ether synthase CYP74M3"}}}
```

Source SHA-256: `bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:50.224082+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"26776054","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79276"}}],"reaction":{"ecNumber":"4.2.1.183","evidences":[{"evidenceCode":"ECO:0000269","id":"26776054","source":"PubMed"}],"name":"(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79275"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:57466"},{"database":"ChEBI","id":"CHEBI:229759"}]}}
```

Source SHA-256: `bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:50.224082+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"26776054","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79272"}}],"reaction":{"ecNumber":"4.2.1.183","evidences":[{"evidenceCode":"ECO:0000269","id":"26776054","source":"PubMed"}],"name":"(13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79271"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:58757"},{"database":"ChEBI","id":"CHEBI:229758"}]}}
```

Source SHA-256: `bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:50.224082+00:00.  

```json
{"citation":{"authors":["Gorina S.S.","Toporkova Y.Y.","Mukhtarova L.S.","Smirnova E.O.","Chechetkin I.R.","Khairutdinov B.I.","Gogolev Y.V.","Grechkin A.N."],"citationCrossReferences":[{"database":"PubMed","id":"26776054"},{"database":"DOI","id":"10.1016/j.bbalip.2016.01.001"}],"citationType":"journal article","firstPage":"301","id":"26776054","journal":"Biochim. Biophys. Acta","lastPage":"309","publicationDate":"2016","title":"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular cloning and identification of divinyl ether synthases CYP74M1 and CYP74M3.","volume":"1861"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:27:52.203972+00:00.  

```text
ID   C74M3_SELML             Reviewed;         495 AA.
AC   D8QZ31;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-OCT-2010, sequence version 1.
DT   28-JAN-2026, entry version 68.
DE   RecName: Full=Divinyl ether synthase CYP74M3 {ECO:0000303|PubMed:26776054};
DE   AltName: Full=Etheroleic acid synthase CYP74M3 {ECO:0000305|PubMed:26776054};
DE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};
GN   Name=CYP74M3 {ECO:0000303|PubMed:26776054};
GN   Synonyms=DES2 {ECO:0000303|PubMed:26776054};
GN   ORFNames=SELMODRAFT_81998 {ECO:0000312|EMBL:EFJ34345.1};
OS   Selaginella moellendorffii (Spikemoss).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Lycopodiopsida; Selaginellales; Selaginellaceae; Selaginella.
OX   NCBI_TaxID=88036;
```

Source SHA-256: `446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:27:52.203972+00:00.  

```text
DE   RecName: Full=Divinyl ether synthase CYP74M3 {ECO:0000303|PubMed:26776054};
DE   AltName: Full=Etheroleic acid synthase CYP74M3 {ECO:0000305|PubMed:26776054};
DE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};
```

Source SHA-256: `446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)  
**Locator:** `lines 40-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:27:52.203972+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.
RX   PubMed=26776054; DOI=10.1016/j.bbalip.2016.01.001;
RA   Gorina S.S., Toporkova Y.Y., Mukhtarova L.S., Smirnova E.O.,
RA   Chechetkin I.R., Khairutdinov B.I., Gogolev Y.V., Grechkin A.N.;
RT   "Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular
RT   cloning and identification of divinyl ether synthases CYP74M1 and
RT   CYP74M3.";
RL   Biochim. Biophys. Acta 1861:301-309(2016).
```

Source SHA-256: `446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)  
**Locator:** `lines 56-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:27:52.203972+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate +
CC         H2O; Xref=Rhea:RHEA:79275, ChEBI:CHEBI:15377, ChEBI:CHEBI:57466,
CC         ChEBI:CHEBI:229759; EC=4.2.1.183;
CC         Evidence={ECO:0000269|PubMed:26776054};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79276;
CC         Evidence={ECO:0000305|PubMed:26776054};
```

Source SHA-256: `446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)  
**Locator:** `lines 63-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:27:52.203972+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate =
CC         etherolenate + H2O; Xref=Rhea:RHEA:79271, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:58757, ChEBI:CHEBI:229758; EC=4.2.1.183;
CC         Evidence={ECO:0000269|PubMed:26776054};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79272;
CC         Evidence={ECO:0000305|PubMed:26776054};
```

Source SHA-256: `446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 46. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
