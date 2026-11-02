# EC_number_0150

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 4.3.1.12

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFMREIELKGHIIDSFILAKVFDRTLELGGDYKVLEFDIGKKKIDTSYAKLLISGDTQQHLDQILEELQNVGANIPEIENANLKPALKDSVLPDGFYSTTNHPTHVKVNDEWIEVANPKMDAVIVVYPEEKRAETKVIRKVKKGDFVLIGHNGIRVMPPEKSREAGQLFEFMNSEVSSEKPKEAIIKRIAKEMHEIREEYKKTGTGGIAIVGGPAIIHTGGGPALAKMVELGYIQAILAGNALATHDIESALYGTSLGVNIKTAKPVTGGHKHHIYAINAINDAGNIKNAVESGVLKEGIMYQCIKNNIPYVLAGSIRDDGPIPDVITDSMVAQDKMRTTVMDKKMVIMLSTLLHSVATGNLMPSYIKTVCVDIQPSTVTKLMDRGTSQAIGVVTDVGVFLVLLLKELERLELQE

[Multiple Choices]
A. 4.2.3.1
B. 1.1.1.122
C. 4.4.1.11
D. 4.3.1.12
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

> The supplied sequence exactly matches the reviewed UniProt entry annotated as ornithine cyclodeaminase, EC 4.3.1.12. The entry assigns the catalytic reaction L-ornithine = L-proline + NH4(+) and attributes the EC annotation to experimental evidence (ECO:0000269). This supports choice D, though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence gives no supplied biological context or experimentally observed reaction that establishes which of these specific EC activities the protein catalyzes. Recognizing it as a particular enzyme would require protein-specific identification, not a general sequence-based argument that distinguishes the listed EC numbers.


**Missing item-specific fact**

> The protein's identity as ornithine cyclodeaminase and its experimentally attributed L-ornithine-to-L-proline reaction are absent from the question.


**Reason**

> The exact EC assignment depends on protein-specific functional annotation or experimental knowledge. The reviewer-only sequence-matched database evidence supports the key but was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports D for this sequence. The sequence-only input does not itself establish another listed EC number, so there is no evidence here that multiple choices are scientifically correct.


### Important caveats

- The UniProt annotation cites experimental evidence, but the primary paper was not independently retrieved or validated for this assessment.
- The cited publication title refers to an enzyme in Anabaena, whereas the sequence-matched UniProt entry identifies a Methanococcus maripaludis protein; retain this source/context distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence gives no supplied biological context or experimentally observed reaction that establishes which of these specific EC activities the protein catalyzes. Recognizing it as a particular enzyme would require protein-specific identification, not a general sequence-based argument that distinguishes the listed EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as ornithine cyclodeaminase and its experimentally attributed L-ornithine-to-L-proline reaction are absent from the question.",
    "reason": "The exact EC assignment depends on protein-specific functional annotation or experimental knowledge. The reviewer-only sequence-matched database evidence supports the key but was not available to the evaluated model."
  },
  "case_id": "EC_number_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry annotated as ornithine cyclodeaminase, EC 4.3.1.12. The entry assigns the catalytic reaction L-ornithine = L-proline + NH4(+) and attributes the EC annotation to experimental evidence (ECO:0000269). This supports choice D, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary paper was not independently retrieved or validated for this assessment.",
    "The cited publication title refers to an enzyme in Anabaena, whereas the sequence-matched UniProt entry identifies a Methanococcus maripaludis protein; retain this source/context distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D for this sequence. The sequence-only input does not itself establish another listed EC number, so there is no evidence here that multiple choices are scientifically correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry annotated as ornithine cyclodeaminase, EC 4.3.1.12. The entry assigns the catalytic reaction L-ornithine = L-proline + NH4(+) and attributes the EC annotation to experimental evidence (ECO:0000269). This supports choice D, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence gives no supplied biological context or experimentally observed reaction that establishes which of these specific EC activities the protein catalyzes. Recognizing it as a particular enzyme would require protein-specific identification, not a general sequence-based argument that distinguishes the listed EC numbers.",
    "missing_item_specific_fact": "The protein's identity as ornithine cyclodeaminase and its experimentally attributed L-ornithine-to-L-proline reaction are absent from the question.",
    "reason": "The exact EC assignment depends on protein-specific functional annotation or experimental knowledge. The reviewer-only sequence-matched database evidence supports the key but was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D for this sequence. The sequence-only input does not itself establish another listed EC number, so there is no evidence here that multiple choices are scientifically correct."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary paper was not independently retrieved or validated for this assessment.",
    "The cited publication title refers to an enzyme in Anabaena, whereas the sequence-matched UniProt entry identifies a Methanococcus maripaludis protein; retain this source/context distinction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q6LXX7 (AOCD_METMP) exactly (SHA256 confirmed, 415 aa). UniProt annotates it as Ornithine cyclodeaminase, EC 4.3.1.12, with experimental evidence (ECO:0000269, PubMed:30636068, Burnat et al. 2019). The catalytic activity L-ornithine = L-proline + NH4(+) is experimentally characterized. The expected answer D (4.3.1.12) is directly supported by experimental annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the GHNG motif (in 'GHNGIRVMPPEK') and the GGPAIIHTGGG motif, both hallmarks of the glutamate dehydrogenase / ornithine cyclodeaminase (GDH/OCD) superfamily's NAD+-binding domain. This allows elimination of: (A) EC 4.2.3.1 terpene cyclase — a completely different fold with no NAD-binding motif; (C) EC 4.4.1.11 cystathionine beta-lyase — a PLP-dependent enzyme with a distinct fold and no GHNG/NAD-binding signature; (B) EC 1.1.1.122 alcohol dehydrogenase — which uses a canonical Rossmann GxGxxG NAD-binding motif rather than the GHNG motif specific to the GDH/OCD superfamily. Among the four choices, only D (4.3.1.12) belongs to the GDH/OCD superfamily, making the GHNG motif a concrete structural-biochemical discriminator.


**Missing item-specific fact**

> While the GHNG motif identifies the superfamily, the precise assignment to ornithine cyclodeaminase (4.3.1.12) versus other GDH/OCD superfamily members (e.g., glutamate dehydrogenase 1.4.1.2) would require additional knowledge. However, no other GDH/OCD superfamily member appears among the four choices, so the superfamily identification is sufficient to select D within this option set.


**Reason**

> A knowledgeable model can identify the GHNG NAD-binding motif as diagnostic of the GDH/OCD superfamily and use this to eliminate the three non-superfamily distractors. This is a general biochemistry argument, not a lookup of the specific UniProt entry. The reasoning chain is concrete and grounded in well-known structural biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GHNG motif cleanly separates the GDH/OCD superfamily (choice D) from the other three options, which belong to entirely different enzyme families (terpene cyclase, alcohol dehydrogenase, PLP-dependent lyase). No other choice is defensible given the motif evidence.


### Important caveats

- The UniProt annotation (EC 4.3.1.12) is backed by experimental evidence (ECO:0000269, PubMed:30636068), not merely computational transfer.
- The sequence was integrated into Swiss-Prot on 2025-04-09; the author's source snapshot is unknown but the sequence version has been unchanged since 2004-07-05.
- The GHNG motif argument distinguishes the superfamily but not the exact EC number within it; this is sufficient here only because no other GDH/OCD superfamily member is offered as a distractor.
- Ornithine cyclodeaminase is a relatively uncommon enzyme; a model without training on the GDH/OCD superfamily's motif signatures might default to the more common alcohol dehydrogenase (B) based on the general NAD-binding context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the GHNG motif (in 'GHNGIRVMPPEK') and the GGPAIIHTGGG motif, both hallmarks of the glutamate dehydrogenase / ornithine cyclodeaminase (GDH/OCD) superfamily's NAD+-binding domain. This allows elimination of: (A) EC 4.2.3.1 terpene cyclase — a completely different fold with no NAD-binding motif; (C) EC 4.4.1.11 cystathionine beta-lyase — a PLP-dependent enzyme with a distinct fold and no GHNG/NAD-binding signature; (B) EC 1.1.1.122 alcohol dehydrogenase — which uses a canonical Rossmann GxGxxG NAD-binding motif rather than the GHNG motif specific to the GDH/OCD superfamily. Among the four choices, only D (4.3.1.12) belongs to the GDH/OCD superfamily, making the GHNG motif a concrete structural-biochemical discriminator.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "While the GHNG motif identifies the superfamily, the precise assignment to ornithine cyclodeaminase (4.3.1.12) versus other GDH/OCD superfamily members (e.g., glutamate dehydrogenase 1.4.1.2) would require additional knowledge. However, no other GDH/OCD superfamily member appears among the four choices, so the superfamily identification is sufficient to select D within this option set.",
    "reason": "A knowledgeable model can identify the GHNG NAD-binding motif as diagnostic of the GDH/OCD superfamily and use this to eliminate the three non-superfamily distractors. This is a general biochemistry argument, not a lookup of the specific UniProt entry. The reasoning chain is concrete and grounded in well-known structural biology."
  },
  "case_id": "EC_number_0150",
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
    "reason": "The sequence matches UniProt Q6LXX7 (AOCD_METMP) exactly (SHA256 confirmed, 415 aa). UniProt annotates it as Ornithine cyclodeaminase, EC 4.3.1.12, with experimental evidence (ECO:0000269, PubMed:30636068, Burnat et al. 2019). The catalytic activity L-ornithine = L-proline + NH4(+) is experimentally characterized. The expected answer D (4.3.1.12) is directly supported by experimental annotation."
  },
  "important_caveats": [
    "The UniProt annotation (EC 4.3.1.12) is backed by experimental evidence (ECO:0000269, PubMed:30636068), not merely computational transfer.",
    "The sequence was integrated into Swiss-Prot on 2025-04-09; the author's source snapshot is unknown but the sequence version has been unchanged since 2004-07-05.",
    "The GHNG motif argument distinguishes the superfamily but not the exact EC number within it; this is sufficient here only because no other GDH/OCD superfamily member is offered as a distractor.",
    "Ornithine cyclodeaminase is a relatively uncommon enzyme; a model without training on the GDH/OCD superfamily's motif signatures might default to the more common alcohol dehydrogenase (B) based on the general NAD-binding context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GHNG motif cleanly separates the GDH/OCD superfamily (choice D) from the other three options, which belong to entirely different enzyme families (terpene cyclase, alcohol dehydrogenase, PLP-dependent lyase). No other choice is defensible given the motif evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q6LXX7 (AOCD_METMP) exactly (SHA256 confirmed, 415 aa). UniProt annotates it as Ornithine cyclodeaminase, EC 4.3.1.12, with experimental evidence (ECO:0000269, PubMed:30636068, Burnat et al. 2019). The catalytic activity L-ornithine = L-proline + NH4(+) is experimentally characterized. The expected answer D (4.3.1.12) is directly supported by experimental annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the GHNG motif (in 'GHNGIRVMPPEK') and the GGPAIIHTGGG motif, both hallmarks of the glutamate dehydrogenase / ornithine cyclodeaminase (GDH/OCD) superfamily's NAD+-binding domain. This allows elimination of: (A) EC 4.2.3.1 terpene cyclase — a completely different fold with no NAD-binding motif; (C) EC 4.4.1.11 cystathionine beta-lyase — a PLP-dependent enzyme with a distinct fold and no GHNG/NAD-binding signature; (B) EC 1.1.1.122 alcohol dehydrogenase — which uses a canonical Rossmann GxGxxG NAD-binding motif rather than the GHNG motif specific to the GDH/OCD superfamily. Among the four choices, only D (4.3.1.12) belongs to the GDH/OCD superfamily, making the GHNG motif a concrete structural-biochemical discriminator.",
    "missing_item_specific_fact": "While the GHNG motif identifies the superfamily, the precise assignment to ornithine cyclodeaminase (4.3.1.12) versus other GDH/OCD superfamily members (e.g., glutamate dehydrogenase 1.4.1.2) would require additional knowledge. However, no other GDH/OCD superfamily member appears among the four choices, so the superfamily identification is sufficient to select D within this option set.",
    "reason": "A knowledgeable model can identify the GHNG NAD-binding motif as diagnostic of the GDH/OCD superfamily and use this to eliminate the three non-superfamily distractors. This is a general biochemistry argument, not a lookup of the specific UniProt entry. The reasoning chain is concrete and grounded in well-known structural biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GHNG motif cleanly separates the GDH/OCD superfamily (choice D) from the other three options, which belong to entirely different enzyme families (terpene cyclase, alcohol dehydrogenase, PLP-dependent lyase). No other choice is defensible given the motif evidence."
  },
  "important_caveats": [
    "The UniProt annotation (EC 4.3.1.12) is backed by experimental evidence (ECO:0000269, PubMed:30636068), not merely computational transfer.",
    "The sequence was integrated into Swiss-Prot on 2025-04-09; the author's source snapshot is unknown but the sequence version has been unchanged since 2004-07-05.",
    "The GHNG motif argument distinguishes the superfamily but not the exact EC number within it; this is sufficient here only because no other GDH/OCD superfamily member is offered as a distractor.",
    "Ornithine cyclodeaminase is a relatively uncommon enzyme; a model without training on the GDH/OCD superfamily's motif signatures might default to the more common alcohol dehydrogenase (B) based on the general NAD-binding context."
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

**Accession:** `Q6LXX7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 100. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:35.053650+00:00.  

```json
"Q6LXX7"
```

Source SHA-256: `3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:35.053650+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30636068","source":"PubMed"}],"value":"Archaeal ornithine cyclodeaminase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30636068","source":"PubMed"}],"value":"Mls2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30636068","source":"PubMed"}],"value":"4.3.1.12"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30636068","source":"PubMed"}],"value":"Ornithine cyclodeaminase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"OCD"}]}}
```

Source SHA-256: `3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:35.053650+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"4.3.1.12","evidences":[{"evidenceCode":"ECO:0000269","id":"30636068","source":"PubMed"}],"name":"L-ornithine = L-proline + NH4(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24368"},{"database":"ChEBI","id":"CHEBI:28938"},{"database":"ChEBI","id":"CHEBI:46911"},{"database":"ChEBI","id":"CHEBI:60039"}]}}
```

Source SHA-256: `3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:35.053650+00:00.  

```json
{"citation":{"authors":["Burnat M.","Picossi S.","Valladares A.","Herrero A.","Flores E."],"citationCrossReferences":[{"database":"PubMed","id":"30636068"},{"database":"DOI","id":"10.1111/mmi.14203"}],"citationType":"journal article","firstPage":"883","id":"30636068","journal":"Mol. Microbiol.","lastPage":"897","publicationDate":"2019","title":"Catabolic pathway of arginine in Anabaena involves a novel bifunctional enzyme that produces proline from arginine.","volume":"111"},"referenceComments":[{"type":"STRAIN","value":"DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:37.153182+00:00.  

```text
ID   AOCD_METMP              Reviewed;         415 AA.
AC   Q6LXX7;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2004, sequence version 1.
DT   28-JAN-2026, entry version 100.
DE   RecName: Full=Ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};
DE            Short=OCD {ECO:0000305};
DE            EC=4.3.1.12 {ECO:0000269|PubMed:30636068};
DE   AltName: Full=Archaeal ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};
DE   AltName: Full=Mls2 {ECO:0000303|PubMed:30636068};
GN   OrderedLocusNames=MMP1218 {ECO:0000312|EMBL:CAF30774.1};
OS   Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2
OS   / LL).
OC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;
OC   Methanococci; Methanococcales; Methanococcaceae; Methanococcus.
OX   NCBI_TaxID=267377;
```

Source SHA-256: `fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:37.153182+00:00.  

```text
DE   RecName: Full=Ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};
DE            Short=OCD {ECO:0000305};
DE            EC=4.3.1.12 {ECO:0000269|PubMed:30636068};
DE   AltName: Full=Archaeal ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};
DE   AltName: Full=Mls2 {ECO:0000303|PubMed:30636068};
```

Source SHA-256: `fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)  
**Locator:** `lines 30-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:37.153182+00:00.  

```text
RN   [2]
RP   FUNCTION, AND CATALYTIC ACTIVITY.
RC   STRAIN=DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL;
RX   PubMed=30636068; DOI=10.1111/mmi.14203;
RA   Burnat M., Picossi S., Valladares A., Herrero A., Flores E.;
RT   "Catabolic pathway of arginine in Anabaena involves a novel bifunctional
RT   enzyme that produces proline from arginine.";
RL   Mol. Microbiol. 111:883-897(2019).
```

Source SHA-256: `fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)  
**Locator:** `lines 46-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:37.153182+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-ornithine = L-proline + NH4(+); Xref=Rhea:RHEA:24368,
CC         ChEBI:CHEBI:28938, ChEBI:CHEBI:46911, ChEBI:CHEBI:60039; EC=4.3.1.12;
CC         Evidence={ECO:0000269|PubMed:30636068};
```

Source SHA-256: `fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 150. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
