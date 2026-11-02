# EC_number_0198

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.97.1.14

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MENQHQKFISRRNFIKTSALLGGTAFLGTGLPNIKKTYSKELDYVGNFEYPLAKPENILYSACLQCTVACSIKVKINNGVCMKIDGNPYSAMNLGENLPYDLSPKEAVSIDGKLCPKGQAGIQHAYDPYRLRKVIKRDGPRGSGKWKTIPYDQAIDEIVNGGNIFKDIGENQNVEGLKDIFVLKDPKVAKAMADDVTKIRKKEMTVDEFKAKHKDNLDVLIDPNHPDLGPKNNQFLFQVGRIHNGRIEFTKRFVNDSFGSVNWIEKTTLCGQTSNKAWVHSTREYLEGKWTGGIKSPRPDHRNTEFLLVFGSIVFEANYGPVQETEPITEGLESGRLKIAVVDPRLTKVASKAWKWVPIKPGNDAAFALGMIRWIIENERYDTKFLQNATRLAATNSDEPSYSNATYLVKVEKDGRAAKHLRANEIGIGTEKEFVVISNGKPAAVDPENSNLAIQGELFVDTNLEGIKVKSPLQLIKEEAYSKELAEWAELSGAKQKDIEDISKEFTSHGKKAAVEFYRGAIKHTNGWYNGQALIVLNHLIGNMNWQGGISNTGGGWSYIGDKEGQPYPMANLHPNKLSKFGVPITKEGWKYEESTLFEGYPAKRPWYPFSGNVAQETWPSISDGYPYKIKAALISSHSPMYSLPGGHVQLKTLLDTEKVPLLIASDIVIGDSSQYVDYIFPDLTYLERWATPGQSHHIRVKVNQVRQPVIAPLTENATVFGEEVPISLEALMMSISEKVGLSGFGKDAFGPGKDLNRMEDFYLKLVANIASGNKQGELVKAADSEEMELFKSSHRHLPKTVYDIEKWQQTLTSDEWKRVVYVLNRGGRFASSDDAYEGSFIKKKIPGLARLYLEEIADSRNSISGNYFTGYPKYLPIMDMAENLINDEGEFHLITNKEVFGTQSRTITNYWAQLALQPENFVVLNSVDAKKLKVDNGDKVLVTSTSNPKGEHLIAADESRPTIGKVKIVEGIRPGVVAISTHYGHWGYGARDIQIDGEVVKGEEVRGLGIHPNPLFRLDDNLRGTTLSDPIGGSASYYDTRVNIQRV

[Multiple Choices]
A. 1.16.1.10
B. 4.2.3.1
C. 1.11.1.24
D. 1.97.1.14
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

> The exact supplied sequence matches the UniProt entry annotated as selenate reductase subunit A with EC 1.97.1.14. The entry links that assignment and the catalytic reaction to a published study, though the excerpts do not independently establish the study’s experimental methods or results.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a large enzyme and may support broad functional-family inferences, but the supplied input gives no reaction, organism, or other context that reliably distinguishes this exact EC classification from the choices.


**Missing item-specific fact**

> The protein-specific functional annotation or evidence that this subunit belongs to the selenate reductase catalyzing the annotated reaction is absent from the question.


**Reason**

> The key is supported by reviewer-only, sequence-matched database evidence, not by information provided to the evaluated model. Identifying the exact EC requires protein-specific functional knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports D; no supplied evidence supports another listed EC as an alternative for this sequence.


### Important caveats

- The UniProt annotation cites a publication, but the supplied excerpts are not an independent review of its experiments.
- The exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a large enzyme and may support broad functional-family inferences, but the supplied input gives no reaction, organism, or other context that reliably distinguishes this exact EC classification from the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or evidence that this subunit belongs to the selenate reductase catalyzing the annotated reaction is absent from the question.",
    "reason": "The key is supported by reviewer-only, sequence-matched database evidence, not by information provided to the evaluated model. Identifying the exact EC requires protein-specific functional knowledge."
  },
  "case_id": "EC_number_0198",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as selenate reductase subunit A with EC 1.97.1.14. The entry links that assignment and the catalytic reaction to a published study, though the excerpts do not independently establish the study’s experimental methods or results."
  },
  "important_caveats": [
    "The UniProt annotation cites a publication, but the supplied excerpts are not an independent review of its experiments.",
    "The exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D; no supplied evidence supports another listed EC as an alternative for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0198",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as selenate reductase subunit A with EC 1.97.1.14. The entry links that assignment and the catalytic reaction to a published study, though the excerpts do not independently establish the study’s experimental methods or results.",
    "evidence_ids": ["C4", "C5", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a large enzyme and may support broad functional-family inferences, but the supplied input gives no reaction, organism, or other context that reliably distinguishes this exact EC classification from the choices.",
    "missing_item_specific_fact": "The protein-specific functional annotation or evidence that this subunit belongs to the selenate reductase catalyzing the annotated reaction is absent from the question.",
    "reason": "The key is supported by reviewer-only, sequence-matched database evidence, not by information provided to the evaluated model. Identifying the exact EC requires protein-specific functional knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D; no supplied evidence supports another listed EC as an alternative for this sequence."
  },
  "important_caveats": [
    "The UniProt annotation cites a publication, but the supplied excerpts are not an independent review of its experiments.",
    "The exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0A8X0K1 (SRDA_MESS1) annotates this exact 1048-aa sequence (SHA-256 matched in both current and historical snapshots) as 'Selenate reductase subunit A' with EC 1.97.1.14. The annotation cites PubMed:21357486 (Kuroda et al., 2011, J. Bacteriol.), which describes molecular cloning and functional characterization of the srdBCA operon encoding the respiratory selenate reductase complex from Mesobacillus selenatarsenatis SF-1. The evidence code is ECO:0000305 (inferred by similarity to the characterized operon), but the underlying reference reports experimental functional data (disruption phenotype, subunit composition). The catalytic reaction 'selenite + a quinone + H2O = selenate + a quinol' is consistent with EC 1.97.1.14.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can partially eliminate distractors using general knowledge: EC 4.2.3.1 (a lyase/dehydratase) is inconsistent with a 1048-aa multi-domain protein bearing a signal peptide and lacking lyase catalytic motifs; EC 1.16.1.10 (ferritin oxidoreductase) is typically a small protein (~200 aa), inconsistent with this large multi-domain architecture. EC 1.11.1.24 (peroxidase) requires conserved heme-binding His/Cys motifs characteristic of peroxidases, which are not evident in this sequence. However, distinguishing EC 1.97.1.14 (selenate/selenite reductase, oxidized quinone) from other oxidoreductase subclasses (e.g., EC 1.97.x.x or other EC 1.x.x.x entries) based on sequence features alone is not feasible. The protein lacks a uniquely identifiable catalytic motif that maps specifically to selenite-to-selenate oxidation coupled to quinone reduction.


**Missing item-specific fact**

> The specific identity of this protein as Selenate reductase subunit A (srdA) of the srdBCA operon from Mesobacillus selenatarsenatis, and the assignment of EC 1.97.1.14, cannot be derived from sequence features alone. One must either recognize the sequence, know the srd operon annotation, or consult a database. The organism name, gene name, and operon context are absent from the question input.


**Reason**

> While general reasoning can eliminate the lyase (B) and likely the small ferritin oxidoreductase (A), and possibly the peroxidase (C) based on size and absence of heme motifs, the final selection of EC 1.97.1.14 over other oxidoreductase subclasses requires item-specific knowledge of this protein's annotation or its operon context. The sequence does not contain a distinctive catalytic signature that uniquely identifies selenite oxidation to selenate with quinone as electron acceptor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the specific protein identity is known, EC 1.97.1.14 is unambiguous. The distractors are in different EC subclasses (lyase, ferritin oxidoreductase, peroxidase) and are not defensible alternatives for this protein. The ambiguity lies in whether a solver can reach D without lookup, not in whether D is the correct answer.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the EC assignment for this specific subunit is based on similarity to the experimentally characterized srdBCA operon rather than direct assay of isolated subunit A alone.
- The organism (Mesobacillus selenatarsenatis, a selenate-reducing bacterium) is not provided in the question input, removing a contextual clue that might aid a knowledgeable solver.
- The entry was first released in 2025-02; the benchmark construction date is unknown, so the annotation may or may not have been available to the author at dataset creation time.
- EC 1.97.1.14 is a relatively obscure and recently defined EC number, making memorization-based recognition less likely than for well-known enzymes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can partially eliminate distractors using general knowledge: EC 4.2.3.1 (a lyase/dehydratase) is inconsistent with a 1048-aa multi-domain protein bearing a signal peptide and lacking lyase catalytic motifs; EC 1.16.1.10 (ferritin oxidoreductase) is typically a small protein (~200 aa), inconsistent with this large multi-domain architecture. EC 1.11.1.24 (peroxidase) requires conserved heme-binding His/Cys motifs characteristic of peroxidases, which are not evident in this sequence. However, distinguishing EC 1.97.1.14 (selenate/selenite reductase, oxidized quinone) from other oxidoreductase subclasses (e.g., EC 1.97.x.x or other EC 1.x.x.x entries) based on sequence features alone is not feasible. The protein lacks a uniquely identifiable catalytic motif that maps specifically to selenite-to-selenate oxidation coupled to quinone reduction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as Selenate reductase subunit A (srdA) of the srdBCA operon from Mesobacillus selenatarsenatis, and the assignment of EC 1.97.1.14, cannot be derived from sequence features alone. One must either recognize the sequence, know the srd operon annotation, or consult a database. The organism name, gene name, and operon context are absent from the question input.",
    "reason": "While general reasoning can eliminate the lyase (B) and likely the small ferritin oxidoreductase (A), and possibly the peroxidase (C) based on size and absence of heme motifs, the final selection of EC 1.97.1.14 over other oxidoreductase subclasses requires item-specific knowledge of this protein's annotation or its operon context. The sequence does not contain a distinctive catalytic signature that uniquely identifies selenite oxidation to selenate with quinone as electron acceptor."
  },
  "case_id": "EC_number_0198",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0A8X0K1 (SRDA_MESS1) annotates this exact 1048-aa sequence (SHA-256 matched in both current and historical snapshots) as 'Selenate reductase subunit A' with EC 1.97.1.14. The annotation cites PubMed:21357486 (Kuroda et al., 2011, J. Bacteriol.), which describes molecular cloning and functional characterization of the srdBCA operon encoding the respiratory selenate reductase complex from Mesobacillus selenatarsenatis SF-1. The evidence code is ECO:0000305 (inferred by similarity to the characterized operon), but the underlying reference reports experimental functional data (disruption phenotype, subunit composition). The catalytic reaction 'selenite + a quinone + H2O = selenate + a quinol' is consistent with EC 1.97.1.14."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the EC assignment for this specific subunit is based on similarity to the experimentally characterized srdBCA operon rather than direct assay of isolated subunit A alone.",
    "The organism (Mesobacillus selenatarsenatis, a selenate-reducing bacterium) is not provided in the question input, removing a contextual clue that might aid a knowledgeable solver.",
    "The entry was first released in 2025-02; the benchmark construction date is unknown, so the annotation may or may not have been available to the author at dataset creation time.",
    "EC 1.97.1.14 is a relatively obscure and recently defined EC number, making memorization-based recognition less likely than for well-known enzymes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the specific protein identity is known, EC 1.97.1.14 is unambiguous. The distractors are in different EC subclasses (lyase, ferritin oxidoreductase, peroxidase) and are not defensible alternatives for this protein. The ambiguity lies in whether a solver can reach D without lookup, not in whether D is the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0198",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0A8X0K1 (SRDA_MESS1) annotates this exact 1048-aa sequence (SHA-256 matched in both current and historical snapshots) as 'Selenate reductase subunit A' with EC 1.97.1.14. The annotation cites PubMed:21357486 (Kuroda et al., 2011, J. Bacteriol.), which describes molecular cloning and functional characterization of the srdBCA operon encoding the respiratory selenate reductase complex from Mesobacillus selenatarsenatis SF-1. The evidence code is ECO:0000305 (inferred by similarity to the characterized operon), but the underlying reference reports experimental functional data (disruption phenotype, subunit composition). The catalytic reaction 'selenite + a quinone + H2O = selenate + a quinol' is consistent with EC 1.97.1.14.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can partially eliminate distractors using general knowledge: EC 4.2.3.1 (a lyase/dehydratase) is inconsistent with a 1048-aa multi-domain protein bearing a signal peptide and lacking lyase catalytic motifs; EC 1.16.1.10 (ferritin oxidoreductase) is typically a small protein (~200 aa), inconsistent with this large multi-domain architecture. EC 1.11.1.24 (peroxidase) requires conserved heme-binding His/Cys motifs characteristic of peroxidases, which are not evident in this sequence. However, distinguishing EC 1.97.1.14 (selenate/selenite reductase, oxidized quinone) from other oxidoreductase subclasses (e.g., EC 1.97.x.x or other EC 1.x.x.x entries) based on sequence features alone is not feasible. The protein lacks a uniquely identifiable catalytic motif that maps specifically to selenite-to-selenate oxidation coupled to quinone reduction.",
    "missing_item_specific_fact": "The specific identity of this protein as Selenate reductase subunit A (srdA) of the srdBCA operon from Mesobacillus selenatarsenatis, and the assignment of EC 1.97.1.14, cannot be derived from sequence features alone. One must either recognize the sequence, know the srd operon annotation, or consult a database. The organism name, gene name, and operon context are absent from the question input.",
    "reason": "While general reasoning can eliminate the lyase (B) and likely the small ferritin oxidoreductase (A), and possibly the peroxidase (C) based on size and absence of heme motifs, the final selection of EC 1.97.1.14 over other oxidoreductase subclasses requires item-specific knowledge of this protein's annotation or its operon context. The sequence does not contain a distinctive catalytic signature that uniquely identifies selenite oxidation to selenate with quinone as electron acceptor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the specific protein identity is known, EC 1.97.1.14 is unambiguous. The distractors are in different EC subclasses (lyase, ferritin oxidoreductase, peroxidase) and are not defensible alternatives for this protein. The ambiguity lies in whether a solver can reach D without lookup, not in whether D is the correct answer."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the EC assignment for this specific subunit is based on similarity to the experimentally characterized srdBCA operon rather than direct assay of isolated subunit A alone.",
    "The organism (Mesobacillus selenatarsenatis, a selenate-reducing bacterium) is not provided in the question input, removing a contextual clue that might aid a knowledgeable solver.",
    "The entry was first released in 2025-02; the benchmark construction date is unknown, so the annotation may or may not have been available to the author at dataset creation time.",
    "EC 1.97.1.14 is a relatively obscure and recently defined EC number, making memorization-based recognition less likely than for well-known enzymes."
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

**Accession:** `A0A0A8X0K1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 39. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:55.467166+00:00.  

```json
"A0A0A8X0K1"
```

Source SHA-256: `d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:55.467166+00:00.  

```json
{"lineage":["Bacteria","Bacillati","Bacillota","Bacilli","Caryophanales","Bacillaceae","Mesobacillus"],"scientificName":"Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431 / SF-1)","taxonId":1321606}
```

Source SHA-256: `d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:55.467166+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"21357486","source":"PubMed"}],"value":"1.97.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Selenate reductase subunit A"}}}
```

Source SHA-256: `d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:55.467166+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.97.1.14","evidences":[{"evidenceCode":"ECO:0000305","id":"21357486","source":"PubMed"}],"name":"selenite + a quinone + H2O = selenate + a quinol","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:51636"},{"database":"ChEBI","id":"CHEBI:15075"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:18212"},{"database":"ChEBI","id":"CHEBI:24646"},{"database":"ChEBI","id":"CHEBI:132124"}]}}
```

Source SHA-256: `d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:55.467166+00:00.  

```json
{"citation":{"authors":["Kuroda M.","Yamashita M.","Miwa E.","Imao K.","Fujimoto N.","Ono H.","Nagano K.","Sei K.","Ike M."],"citationCrossReferences":[{"database":"PubMed","id":"21357486"},{"database":"DOI","id":"10.1128/jb.01197-10"}],"citationType":"journal article","firstPage":"2141","id":"21357486","journal":"J. Bacteriol.","lastPage":"2148","publicationDate":"2011","title":"Molecular cloning and characterization of the srdBCA operon, encoding the respiratory selenate reductase complex, from the selenate-reducing bacterium Bacillus selenatarsenatis SF-1.","volume":"193"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAJ83594.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"DSM 18680 / JCM 14380 / FERM P-15431 / SF-1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION AS A SELENATE REDUCTASE","SUBUNIT","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:23:57.438981+00:00.  

```text
ID   SRDA_MESS1              Reviewed;        1048 AA.
AC   A0A0A8X0K1; E9RFD1;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   04-MAR-2015, sequence version 1.
DT   09-APR-2025, entry version 39.
DE   RecName: Full=Selenate reductase subunit A {ECO:0000305};
DE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};
DE   Flags: Precursor;
GN   Name=srdA {ECO:0000303|PubMed:21357486};
GN   ORFNames=SAMD00020551_1552 {ECO:0000312|EMBL:GAM13408.1};
OS   Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431
OS   / SF-1).
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae;
OC   Mesobacillus.
OX   NCBI_TaxID=1321606;
```

Source SHA-256: `70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:23:57.438981+00:00.  

```text
DE   RecName: Full=Selenate reductase subunit A {ECO:0000305};
DE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};
DE   Flags: Precursor;
```

Source SHA-256: `70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39)  
**Locator:** `lines 16-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:23:57.438981+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAJ83594.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION AS A SELENATE REDUCTASE,
RP   SUBUNIT, AND DISRUPTION PHENOTYPE.
RC   STRAIN=DSM 18680 / JCM 14380 / FERM P-15431 / SF-1;
RX   PubMed=21357486; DOI=10.1128/jb.01197-10;
RA   Kuroda M., Yamashita M., Miwa E., Imao K., Fujimoto N., Ono H., Nagano K.,
RA   Sei K., Ike M.;
RT   "Molecular cloning and characterization of the srdBCA operon, encoding the
RT   respiratory selenate reductase complex, from the selenate-reducing
RT   bacterium Bacillus selenatarsenatis SF-1.";
RL   J. Bacteriol. 193:2141-2148(2011).
```

Source SHA-256: `70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39)  
**Locator:** `lines 41-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:23:57.438981+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=selenite + a quinone + H2O = selenate + a quinol;
CC         Xref=Rhea:RHEA:51636, ChEBI:CHEBI:15075, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:18212, ChEBI:CHEBI:24646, ChEBI:CHEBI:132124;
CC         EC=1.97.1.14; Evidence={ECO:0000305|PubMed:21357486};
```

Source SHA-256: `70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 198. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
