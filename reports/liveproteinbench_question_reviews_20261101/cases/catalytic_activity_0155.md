# catalytic_activity_0155

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — uridine in 28S rRNA + S-adenosyl-L-methionine = N(3)-methyluridine in 28S rRNA + S-adenosyl-L-homocysteine + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTMLAAPTASSNGRPIGPHKSWKKVNEERKALKRQRKQDKLLKELQQAKEAESQAGKAANEVQAKDKPNPSTLSIAVPGSILENAQSNELRAYVAGQIARAACIFRVNEVIVFDDVGIATARETKRSYEADGEGSSTGTVRSSSLQLARILQYLECPQYLRKYFFPLHKDLKYSGLLNPLDTPHHLRQQSKFRYREGVICDKKAKEGHSYANVGLLNDVLVDKAIEPGVRVTVKMEPQSESCRKQRGTLVSPDEPRRETGVYWGYQVRIAHSMSEIFTKSPYATGYDVTVGTSDRGTNVHEVPNRSYNFNHMLIVFGGLQGLESALANDEKLTVDDPELLFDHYVNVLPRQGSRTIRTEEALLIALAALQEKLQPQVADVEIDLTDLLPKSEDSGIAVRRDVLVSKKQKKRKQVEDTPDETVVDEPSFSKPLPKVARLTANPFADSSEELAKNTPAQDDFEVVSSTTVSGTSHSCADDDLSRFD

[Multiple Choices]
A. cholesterol(in) = cholesterol(out)
B. N(6)-acetyl-L-lysyl-[alpha-tubulin] + H2O = L-lysyl-[alpha-tubulin] + acetate
C. uridine in 28S rRNA + S-adenosyl-L-methionine = N(3)-methyluridine in 28S rRNA + S-adenosyl-L-homocysteine + H(+)
D. O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence matches the UniProt entry annotated as a 28S rRNA uridine-N(3)-methyltransferase, and the catalytic reaction in choice C is linked to experimental evidence (ECO:0000269) and a cited 2024 publication. The historical sequence-matched record also gives this reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying an enzyme family, but the supplied input does not establish the specific RNA substrate or the N(3) methylation site needed to distinguish choice C from other enzyme reactions.


**Missing item-specific fact**

> The protein-specific functional fact that this sequence’s enzyme methylates uridine in 28S rRNA at N(3), using S-adenosyl-L-methionine.


**Reason**

> Selecting the exact reaction depends on protein-specific substrate and modification-site information absent from the sequence prompt; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reaction types, and the matched functional annotation supports choice C specifically.


### Important caveats

- The annotation and literature evidence are reviewer-only and were not supplied to the evaluated model.
- The evidence establishes support for the keyed reaction, but does not make that specific substrate and modification site inferable from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying an enzyme family, but the supplied input does not establish the specific RNA substrate or the N(3) methylation site needed to distinguish choice C from other enzyme reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional fact that this sequence’s enzyme methylates uridine in 28S rRNA at N(3), using S-adenosyl-L-methionine.",
    "reason": "Selecting the exact reaction depends on protein-specific substrate and modification-site information absent from the sequence prompt; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from supplied context."
  },
  "case_id": "catalytic_activity_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as a 28S rRNA uridine-N(3)-methyltransferase, and the catalytic reaction in choice C is linked to experimental evidence (ECO:0000269) and a cited 2024 publication. The historical sequence-matched record also gives this reaction."
  },
  "important_caveats": [
    "The annotation and literature evidence are reviewer-only and were not supplied to the evaluated model.",
    "The evidence establishes support for the keyed reaction, but does not make that specific substrate and modification site inferable from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the matched functional annotation supports choice C specifically."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as a 28S rRNA uridine-N(3)-methyltransferase, and the catalytic reaction in choice C is linked to experimental evidence (ECO:0000269) and a cited 2024 publication. The historical sequence-matched record also gives this reaction.",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying an enzyme family, but the supplied input does not establish the specific RNA substrate or the N(3) methylation site needed to distinguish choice C from other enzyme reactions.",
    "missing_item_specific_fact": "The protein-specific functional fact that this sequence’s enzyme methylates uridine in 28S rRNA at N(3), using S-adenosyl-L-methionine.",
    "reason": "Selecting the exact reaction depends on protein-specific substrate and modification-site information absent from the sequence prompt; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the matched functional annotation supports choice C specifically."
  },
  "important_caveats": [
    "The annotation and literature evidence are reviewer-only and were not supplied to the evaluated model.",
    "The evidence establishes support for the keyed reaction, but does not make that specific substrate and modification site inferable from the sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A1Z830 (SPOUT_DROME) matches the 485-AA sequence exactly (SHA256 confirmed). The catalytic activity is annotated as 'uridine in 28S rRNA + S-adenosyl-L-methyltransferase' with EC 2.1.1.- and the exact reaction in option C is listed with ECO:0000269 (inferred from direct assay) evidence from PubMed:39671501 (Chen et al., Sci. Adv. 2024), which experimentally demonstrated that Ptch/SPOUT1 deposits m3U on 28S rRNA. The reaction text matches option C verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> In principle, if one could recognize SPOUT-domain methyltransferase signatures (e.g., SAM-binding motifs) in the raw sequence, one could narrow to C as the only methyltransferase (SAM-utilizing) reaction among the four options (A=transport, B=deacetylase/hydrolase, D=phosphatase/hydrolase). However, identifying SPOUT-domain features or canonical SAM-binding motifs from a 485-residue sequence without structural or domain-annotation context is extremely difficult and unreliable. The specific substrate (28S rRNA) and modification (N3-methyluridine) are item-specific facts not derivable from general sequence reasoning.


**Missing item-specific fact**

> The specific identification of this protein as a 28S rRNA (uridine-N3)-methyltransferase (Ptch/SPOUT1) requires either database lookup of UniProt A1Z830, memorization of the SPOUT1/Ptch family annotation, or knowledge of the 2024 experimental characterization (PubMed:39671501). No domain annotation, structural information, or contextual hint is provided in the question input.


**Reason**

> The question supplies only a raw amino acid sequence and four mechanistically distinct reactions. While C is the only methyltransferase option, reliably identifying methyltransferase activity from a raw sequence without annotation requires specialized domain recognition (SPOUT domain) that is effectively equivalent to memorizing the database entry. The specific rRNA substrate and N3-methyluridine product are item-specific experimental findings, not generalizable from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct enzyme classes (transport, deacetylase, methyltransferase, phosphatase). If one could identify methyltransferase activity, C is unambiguously the only SAM-dependent transferase reaction. No other option is defensible for this protein given the experimental evidence.


### Important caveats

- The UniProt annotation carries ECO:0000269 (direct assay) evidence from a 2024 paper, indicating experimental rather than purely computational support for the catalytic activity.
- The SPOUT domain name is embedded in the UniProt protein name (SPOUT_DROME) but is not provided to the evaluated model in the question input.
- The entry was first public in June 2025; the author's source snapshot date is unknown, so the annotation may not have been available at question-construction time.
- The reviewer-only evidence confirms sequence identity (SHA256 match) between the benchmark sequence and UniProt A1Z830, but this accession was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "In principle, if one could recognize SPOUT-domain methyltransferase signatures (e.g., SAM-binding motifs) in the raw sequence, one could narrow to C as the only methyltransferase (SAM-utilizing) reaction among the four options (A=transport, B=deacetylase/hydrolase, D=phosphatase/hydrolase). However, identifying SPOUT-domain features or canonical SAM-binding motifs from a 485-residue sequence without structural or domain-annotation context is extremely difficult and unreliable. The specific substrate (28S rRNA) and modification (N3-methyluridine) are item-specific facts not derivable from general sequence reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this protein as a 28S rRNA (uridine-N3)-methyltransferase (Ptch/SPOUT1) requires either database lookup of UniProt A1Z830, memorization of the SPOUT1/Ptch family annotation, or knowledge of the 2024 experimental characterization (PubMed:39671501). No domain annotation, structural information, or contextual hint is provided in the question input.",
    "reason": "The question supplies only a raw amino acid sequence and four mechanistically distinct reactions. While C is the only methyltransferase option, reliably identifying methyltransferase activity from a raw sequence without annotation requires specialized domain recognition (SPOUT domain) that is effectively equivalent to memorizing the database entry. The specific rRNA substrate and N3-methyluridine product are item-specific experimental findings, not generalizable from sequence alone."
  },
  "case_id": "catalytic_activity_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A1Z830 (SPOUT_DROME) matches the 485-AA sequence exactly (SHA256 confirmed). The catalytic activity is annotated as 'uridine in 28S rRNA + S-adenosyl-L-methyltransferase' with EC 2.1.1.- and the exact reaction in option C is listed with ECO:0000269 (inferred from direct assay) evidence from PubMed:39671501 (Chen et al., Sci. Adv. 2024), which experimentally demonstrated that Ptch/SPOUT1 deposits m3U on 28S rRNA. The reaction text matches option C verbatim."
  },
  "important_caveats": [
    "The UniProt annotation carries ECO:0000269 (direct assay) evidence from a 2024 paper, indicating experimental rather than purely computational support for the catalytic activity.",
    "The SPOUT domain name is embedded in the UniProt protein name (SPOUT_DROME) but is not provided to the evaluated model in the question input.",
    "The entry was first public in June 2025; the author's source snapshot date is unknown, so the annotation may not have been available at question-construction time.",
    "The reviewer-only evidence confirms sequence identity (SHA256 match) between the benchmark sequence and UniProt A1Z830, but this accession was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes (transport, deacetylase, methyltransferase, phosphatase). If one could identify methyltransferase activity, C is unambiguously the only SAM-dependent transferase reaction. No other option is defensible for this protein given the experimental evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A1Z830 (SPOUT_DROME) matches the 485-AA sequence exactly (SHA256 confirmed). The catalytic activity is annotated as 'uridine in 28S rRNA + S-adenosyl-L-methyltransferase' with EC 2.1.1.- and the exact reaction in option C is listed with ECO:0000269 (inferred from direct assay) evidence from PubMed:39671501 (Chen et al., Sci. Adv. 2024), which experimentally demonstrated that Ptch/SPOUT1 deposits m3U on 28S rRNA. The reaction text matches option C verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "In principle, if one could recognize SPOUT-domain methyltransferase signatures (e.g., SAM-binding motifs) in the raw sequence, one could narrow to C as the only methyltransferase (SAM-utilizing) reaction among the four options (A=transport, B=deacetylase/hydrolase, D=phosphatase/hydrolase). However, identifying SPOUT-domain features or canonical SAM-binding motifs from a 485-residue sequence without structural or domain-annotation context is extremely difficult and unreliable. The specific substrate (28S rRNA) and modification (N3-methyluridine) are item-specific facts not derivable from general sequence reasoning.",
    "missing_item_specific_fact": "The specific identification of this protein as a 28S rRNA (uridine-N3)-methyltransferase (Ptch/SPOUT1) requires either database lookup of UniProt A1Z830, memorization of the SPOUT1/Ptch family annotation, or knowledge of the 2024 experimental characterization (PubMed:39671501). No domain annotation, structural information, or contextual hint is provided in the question input.",
    "reason": "The question supplies only a raw amino acid sequence and four mechanistically distinct reactions. While C is the only methyltransferase option, reliably identifying methyltransferase activity from a raw sequence without annotation requires specialized domain recognition (SPOUT domain) that is effectively equivalent to memorizing the database entry. The specific rRNA substrate and N3-methyluridine product are item-specific experimental findings, not generalizable from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes (transport, deacetylase, methyltransferase, phosphatase). If one could identify methyltransferase activity, C is unambiguously the only SAM-dependent transferase reaction. No other option is defensible for this protein given the experimental evidence."
  },
  "important_caveats": [
    "The UniProt annotation carries ECO:0000269 (direct assay) evidence from a 2024 paper, indicating experimental rather than purely computational support for the catalytic activity.",
    "The SPOUT domain name is embedded in the UniProt protein name (SPOUT_DROME) but is not provided to the evaluated model in the question input.",
    "The entry was first public in June 2025; the author's source snapshot date is unknown, so the annotation may not have been available at question-construction time.",
    "The reviewer-only evidence confirms sequence identity (SHA256 match) between the benchmark sequence and UniProt A1Z830, but this accession was not provided to the evaluated model."
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

**Accession:** `A1Z830` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 122. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1Z830.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.725323+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39671501","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"value":"28S rRNA (uridine-N(3))-methyltransferase"}}}
```

Source SHA-256: `4de9be795c2a99805d6ce7ac0a27b66607b8b069286e0594a016112d990fb2ac`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1Z830.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.725323+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39671501","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:83636"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39671501","source":"PubMed"}],"name":"uridine in 28S rRNA + S-adenosyl-L-methionine = N(3)-methyluridine in 28S rRNA + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:83635"},{"database":"Rhea","id":"RHEA-COMP:20178"},{"database":"Rhea","id":"RHEA-COMP:20181"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:65315"},{"database":"ChEBI","id":"CHEBI:74502"}]}}
```

Source SHA-256: `4de9be795c2a99805d6ce7ac0a27b66607b8b069286e0594a016112d990fb2ac`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1Z830.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.725323+00:00.  

```json
{"citation":{"authors":["Chen J.","Bai Y.","Huang Y.","Cui M.","Wang Y.","Gu Z.","Wu X.","Li Y.","Rong Y.S."],"citationCrossReferences":[{"database":"PubMed","id":"39671501"},{"database":"DOI","id":"10.1126/sciadv.adr1743"}],"citationType":"journal article","firstPage":"eadr1743","id":"39671501","journal":"Sci. Adv.","lastPage":"eadr1743","publicationDate":"2024","title":"The Ptch/SPOUT1 methyltransferase deposits an m3U modification on 28S rRNA for normal ribosomal function in flies and humans.","volume":"10"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `4de9be795c2a99805d6ce7ac0a27b66607b8b069286e0594a016112d990fb2ac`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:26:49.361895+00:00.  

```text
ID   SPOUT_DROME             Reviewed;         485 AA.
AC   A1Z830;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   06-FEB-2007, sequence version 1.
DT   28-JAN-2026, entry version 122.
DE   RecName: Full=28S rRNA (uridine-N(3))-methyltransferase;
DE            EC=2.1.1.- {ECO:0000269|PubMed:39671501};
GN   Name=ptch {ECO:0000303|PubMed:39671501};
GN   ORFNames=CG12128 {ECO:0000312|EMBL:AAF58861.1};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227;
```

Source SHA-256: `104e9d6a622cdc871df72441a8a1c4c9cdae0ef3e255b6a18cf6297f273fb42c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:26:49.361895+00:00.  

```text
DE   RecName: Full=28S rRNA (uridine-N(3))-methyltransferase;
DE            EC=2.1.1.- {ECO:0000269|PubMed:39671501};
```

Source SHA-256: `104e9d6a622cdc871df72441a8a1c4c9cdae0ef3e255b6a18cf6297f273fb42c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122)  
**Locator:** `lines 68-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:26:49.361895+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, AND SUBCELLULAR LOCATION.
RX   PubMed=39671501; DOI=10.1126/sciadv.adr1743;
RA   Chen J., Bai Y., Huang Y., Cui M., Wang Y., Gu Z., Wu X., Li Y., Rong Y.S.;
RT   "The Ptch/SPOUT1 methyltransferase deposits an m3U modification on 28S rRNA
RT   for normal ribosomal function in flies and humans.";
RL   Sci. Adv. 10:eadr1743-eadr1743(2024).
```

Source SHA-256: `104e9d6a622cdc871df72441a8a1c4c9cdae0ef3e255b6a18cf6297f273fb42c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122)  
**Locator:** `lines 78-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:26:49.361895+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=uridine in 28S rRNA + S-adenosyl-L-methionine = N(3)-
CC         methyluridine in 28S rRNA + S-adenosyl-L-homocysteine + H(+);
CC         Xref=Rhea:RHEA:83635, Rhea:RHEA-COMP:20178, Rhea:RHEA-COMP:20181,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:65315, ChEBI:CHEBI:74502;
CC         Evidence={ECO:0000269|PubMed:39671501};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83636;
CC         Evidence={ECO:0000305|PubMed:39671501};
```

Source SHA-256: `104e9d6a622cdc871df72441a8a1c4c9cdae0ef3e255b6a18cf6297f273fb42c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 155. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
