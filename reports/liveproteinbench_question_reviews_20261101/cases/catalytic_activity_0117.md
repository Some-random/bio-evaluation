# catalytic_activity_0117

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3&#x27;-5&#x27; direction.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDINTLLNTPDEDVLSLFTPQVARWFKEKYKVFTPPQKGAIPLIKKGKNVLVSSPTGSGKTLAAFLGILDTLIDLGYKNELNKQIYAIYISPLRALNNDMRRNLIEPLTELRNLYPDLPEISIGVRTSDTSSYEKQKMLKKPPHILITTPESFGISLVSPKFREKLSDVKWVIVDEIHELANSKRGAYLAGLLELYKSFIAKNNFVRIGLSATISPLEEVAKFLVGGNGDYEIIDARFVKPTDIQVVSPVKDLVHATEEEVNIGIYSYLVDEIKKHKTTLIFTNTRHAAERVAYKLRKMFEDQNIFDSDLVAAHHSSLSRDVRLEVEEKLKRGELKVVVSSTSLELGIDIGYIDLVTLLSSPKSVSRLLQRVGRAGHHIREVSKGRVVVVDRDDLVECTVLAKLAIDRKIDNIHVPENPLDVLTQLIVAASLITPIEKDKLYEIIKNVYNFRSLSYDEYNNVAEYLAGNYGLDSNKVYAKIRIKDGMISPKRGTRMIFFLNSGTIPDEAMIPVKMENGGYVGNLEEEFVEILAPGDIFVLAGKTYEFIRSEGNSVIVKKSEGQRPTVPSWFSEMLPLAFDSAIEIGKFRGKIAEAIMNEVPKDEVISSIMSEYNLSRFAALSIYNYVKEELLFTGGIVPTDKLLLIEVYDDDDQNRNFIFHGLYGRRTVDALSRAIAYIISKDLNMDVRIAITDNGFAITVPGKQEYEISKVFDKLEPDKMYEILSDVILRTEMIKRRFRHCAERSFMLLKRYKGRETSIDRRQINSEVLLGVVRQIEHFPVLKETVREILEDYMDIKRAIEIVEKIRNGDIKVATIGPNQVPSPFAHNILVKQYTDVVLAEDKRELLKELHNKVIEFLRNKGIDIDLEYTEAGIK

[Multiple Choices]
A. Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction.
B. dopamine + S-adenosyl-L-methionine = 3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)
C. okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)
D. guanosine(in) + H(+)(in) = guanosine(out) + H(+)(out)
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

> The exact supplied sequence matches the UniProt entry for an ATP-dependent DNA helicase, whose annotated catalytic activity is the reaction in A. The annotation cites experimental evidence, though the primary study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a P-loop-like ATP-binding motif, which can support an ATPase/helicase inference and make A more plausible than the chemically unrelated alternatives. But this does not establish that this particular protein unwinds duplex DNA in the 3'-to-5' direction.


**Missing item-specific fact**

> The protein-specific helicase function and translocation polarity are not given in the prompt; identifying them requires an annotation or experimental result.


**Reason**

> Sequence features may narrow the choices to a helicase-like reaction, but the precise reaction wording in A depends on the protein-specific directionality.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, A is the only helicase reaction and is supported by the matched-sequence annotation. The sequence alone does not establish its directional detail.


### Important caveats

- The reviewer-only database evidence was not supplied to the evaluated model.
- The cited annotation is linked to a publication and carries experimental-evidence coding, but the primary paper was not independently checked.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a P-loop-like ATP-binding motif, which can support an ATPase/helicase inference and make A more plausible than the chemically unrelated alternatives. But this does not establish that this particular protein unwinds duplex DNA in the 3'-to-5' direction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific helicase function and translocation polarity are not given in the prompt; identifying them requires an annotation or experimental result.",
    "reason": "Sequence features may narrow the choices to a helicase-like reaction, but the precise reaction wording in A depends on the protein-specific directionality."
  },
  "case_id": "catalytic_activity_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry for an ATP-dependent DNA helicase, whose annotated catalytic activity is the reaction in A. The annotation cites experimental evidence, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not supplied to the evaluated model.",
    "The cited annotation is linked to a publication and carries experimental-evidence coding, but the primary paper was not independently checked."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, A is the only helicase reaction and is supported by the matched-sequence annotation. The sequence alone does not establish its directional detail."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry for an ATP-dependent DNA helicase, whose annotated catalytic activity is the reaction in A. The annotation cites experimental evidence, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a P-loop-like ATP-binding motif, which can support an ATPase/helicase inference and make A more plausible than the chemically unrelated alternatives. But this does not establish that this particular protein unwinds duplex DNA in the 3'-to-5' direction.",
    "missing_item_specific_fact": "The protein-specific helicase function and translocation polarity are not given in the prompt; identifying them requires an annotation or experimental result.",
    "reason": "Sequence features may narrow the choices to a helicase-like reaction, but the precise reaction wording in A depends on the protein-specific directionality."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, A is the only helicase reaction and is supported by the matched-sequence annotation. The sequence alone does not establish its directional detail."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not supplied to the evaluated model.",
    "The cited annotation is linked to a publication and carries experimental-evidence coding, but the primary paper was not independently checked."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q4J8R1 (LHRC_SULAC, 876 AA, exact SHA-256 match). The UniProt entry annotates the protein as 'ATP-dependent helicase Lhr-Core' (EC 5.6.2.4) with the catalytic activity 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction,' supported by experimental evidence (ECO:0000269, PubMed:26148716, van Wolferen et al. 2015, J. Bacteriol.). The reference explicitly documents 'FUNCTION AS A HELICASE, CATALYTIC ACTIVITY.' The expected answer text matches the annotation verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Walker A (P-loop) motif 'GSGKT' (within 'SPTGSGKTLAA'), a hallmark of ATP-binding proteins. Among the four choices, only A involves ATP hydrolysis as the driving reaction. Choice B (methyltransferase) requires SAM and a Rossmann-like fold; Choice C (cytochrome P450 monooxygenase) requires a heme-binding motif (FxxGxxxCxG) absent here; Choice D (proton-coupled nucleoside transporter) involves no ATP hydrolysis and would require transmembrane helices not present in this soluble protein. The Walker A motif thus provides a concrete, general biological argument eliminating B, C, and D and pointing to an ATP-dependent enzyme, which uniquely matches A.


**Missing item-specific fact**

> The specific 3'-5' translocation directionality and DNA substrate specificity cannot be determined from the Walker A motif alone; these require family-level or item-specific knowledge. However, since only one choice involves ATP hydrolysis coupled to nucleic acid processing, the Walker A motif is sufficient to select A among these four highly distinct enzyme classes.


**Reason**

> The Walker A motif is a well-known, generalizable sequence feature that a knowledgeable biologist can identify and link to ATP-dependent activity. The four distractors represent entirely different enzyme/transport classes (methyltransferase, P450 monooxygenase, proton-coupled transporter) that lack Walker A motifs and do not involve ATP hydrolysis. This provides a meaningful reasoning path without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span fundamentally different protein classes (helicase, methyltransferase, P450, transporter). The presence of a Walker A motif and absence of heme-binding motifs, SAM-binding signatures, or transmembrane segments make A the only defensible choice. No other option is biologically plausible given the sequence features.


### Important caveats

- The specific '3'-5' directionality in the answer text is a property that cannot be inferred from the Walker A motif alone; it would require recognition of the helicase subfamily or prior knowledge. However, since no alternative ATP-dependent helicase option is offered, this does not create ambiguity among the given choices.
- The annotation evidence code ECO:0000269 indicates direct experimental evidence from PubMed:26148716, not computational inference.
- The sequence match is exact (SHA-256 confirmed) to UniProt Q4J8R1, entry version 118/120, sequence version 1.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Walker A (P-loop) motif 'GSGKT' (within 'SPTGSGKTLAA'), a hallmark of ATP-binding proteins. Among the four choices, only A involves ATP hydrolysis as the driving reaction. Choice B (methyltransferase) requires SAM and a Rossmann-like fold; Choice C (cytochrome P450 monooxygenase) requires a heme-binding motif (FxxGxxxCxG) absent here; Choice D (proton-coupled nucleoside transporter) involves no ATP hydrolysis and would require transmembrane helices not present in this soluble protein. The Walker A motif thus provides a concrete, general biological argument eliminating B, C, and D and pointing to an ATP-dependent enzyme, which uniquely matches A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific 3'-5' translocation directionality and DNA substrate specificity cannot be determined from the Walker A motif alone; these require family-level or item-specific knowledge. However, since only one choice involves ATP hydrolysis coupled to nucleic acid processing, the Walker A motif is sufficient to select A among these four highly distinct enzyme classes.",
    "reason": "The Walker A motif is a well-known, generalizable sequence feature that a knowledgeable biologist can identify and link to ATP-dependent activity. The four distractors represent entirely different enzyme/transport classes (methyltransferase, P450 monooxygenase, proton-coupled transporter) that lack Walker A motifs and do not involve ATP hydrolysis. This provides a meaningful reasoning path without requiring memorization of this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q4J8R1 (LHRC_SULAC, 876 AA, exact SHA-256 match). The UniProt entry annotates the protein as 'ATP-dependent helicase Lhr-Core' (EC 5.6.2.4) with the catalytic activity 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction,' supported by experimental evidence (ECO:0000269, PubMed:26148716, van Wolferen et al. 2015, J. Bacteriol.). The reference explicitly documents 'FUNCTION AS A HELICASE, CATALYTIC ACTIVITY.' The expected answer text matches the annotation verbatim."
  },
  "important_caveats": [
    "The specific '3'-5' directionality in the answer text is a property that cannot be inferred from the Walker A motif alone; it would require recognition of the helicase subfamily or prior knowledge. However, since no alternative ATP-dependent helicase option is offered, this does not create ambiguity among the given choices.",
    "The annotation evidence code ECO:0000269 indicates direct experimental evidence from PubMed:26148716, not computational inference.",
    "The sequence match is exact (SHA-256 confirmed) to UniProt Q4J8R1, entry version 118/120, sequence version 1."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span fundamentally different protein classes (helicase, methyltransferase, P450, transporter). The presence of a Walker A motif and absence of heme-binding motifs, SAM-binding signatures, or transmembrane segments make A the only defensible choice. No other option is biologically plausible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q4J8R1 (LHRC_SULAC, 876 AA, exact SHA-256 match). The UniProt entry annotates the protein as 'ATP-dependent helicase Lhr-Core' (EC 5.6.2.4) with the catalytic activity 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction,' supported by experimental evidence (ECO:0000269, PubMed:26148716, van Wolferen et al. 2015, J. Bacteriol.). The reference explicitly documents 'FUNCTION AS A HELICASE, CATALYTIC ACTIVITY.' The expected answer text matches the annotation verbatim.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Walker A (P-loop) motif 'GSGKT' (within 'SPTGSGKTLAA'), a hallmark of ATP-binding proteins. Among the four choices, only A involves ATP hydrolysis as the driving reaction. Choice B (methyltransferase) requires SAM and a Rossmann-like fold; Choice C (cytochrome P450 monooxygenase) requires a heme-binding motif (FxxGxxxCxG) absent here; Choice D (proton-coupled nucleoside transporter) involves no ATP hydrolysis and would require transmembrane helices not present in this soluble protein. The Walker A motif thus provides a concrete, general biological argument eliminating B, C, and D and pointing to an ATP-dependent enzyme, which uniquely matches A.",
    "missing_item_specific_fact": "The specific 3'-5' translocation directionality and DNA substrate specificity cannot be determined from the Walker A motif alone; these require family-level or item-specific knowledge. However, since only one choice involves ATP hydrolysis coupled to nucleic acid processing, the Walker A motif is sufficient to select A among these four highly distinct enzyme classes.",
    "reason": "The Walker A motif is a well-known, generalizable sequence feature that a knowledgeable biologist can identify and link to ATP-dependent activity. The four distractors represent entirely different enzyme/transport classes (methyltransferase, P450 monooxygenase, proton-coupled transporter) that lack Walker A motifs and do not involve ATP hydrolysis. This provides a meaningful reasoning path without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span fundamentally different protein classes (helicase, methyltransferase, P450, transporter). The presence of a Walker A motif and absence of heme-binding motifs, SAM-binding signatures, or transmembrane segments make A the only defensible choice. No other option is biologically plausible given the sequence features."
  },
  "important_caveats": [
    "The specific '3'-5' directionality in the answer text is a property that cannot be inferred from the Walker A motif alone; it would require recognition of the helicase subfamily or prior knowledge. However, since no alternative ATP-dependent helicase option is offered, this does not create ambiguity among the given choices.",
    "The annotation evidence code ECO:0000269 indicates direct experimental evidence from PubMed:26148716, not computational inference.",
    "The sequence match is exact (SHA-256 confirmed) to UniProt Q4J8R1, entry version 118/120, sequence version 1."
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

**Accession:** `Q4J8R1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 118. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.183785+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"DNA 3'-5' helicase Lhr-Core"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26148716","source":"PubMed"}],"value":"DNA 3'-5' helicase Saci_1500"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26148716","source":"PubMed"}],"value":"5.6.2.4"}],"fullName":{"value":"ATP-dependent helicase Lhr-Core"}}}
```

Source SHA-256: `5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.183785+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.6.2.4","evidences":[{"evidenceCode":"ECO:0000269","id":"26148716","source":"PubMed"}],"name":"Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction."}}
```

Source SHA-256: `5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.183785+00:00.  

```json
{"citation":{"authors":["van Wolferen M.","Ma X.","Albers S.V."],"citationCrossReferences":[{"database":"PubMed","id":"26148716"},{"database":"DOI","id":"10.1128/jb.00344-15"}],"citationType":"journal article","firstPage":"2941","id":"26148716","journal":"J. Bacteriol.","lastPage":"2951","publicationDate":"2015","title":"DNA Processing Proteins Involved in the UV-Induced Stress Response of Sulfolobales.","volume":"197"},"referenceComments":[{"type":"STRAIN","value":"ATCC 33909 / DSM 639 / JCM 8929 / NBRC 15157 / NCIMB 11770"}],"referenceNumber":2,"referencePositions":["FUNCTION AS A HELICASE","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE","DNA-BINDING","MUTAGENESIS OF LYS-60"]}
```

Source SHA-256: `5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:33.887619+00:00.  

```text
DE   RecName: Full=ATP-dependent helicase Lhr-Core;
DE            EC=5.6.2.4 {ECO:0000269|PubMed:26148716};
DE   AltName: Full=DNA 3'-5' helicase Lhr-Core {ECO:0000305};
DE   AltName: Full=DNA 3'-5' helicase Saci_1500 {ECO:0000303|PubMed:26148716};
```

Source SHA-256: `e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:33.887619+00:00.  

```text
RN   [2]
RP   FUNCTION AS A HELICASE, CATALYTIC ACTIVITY, DISRUPTION PHENOTYPE,
RP   DNA-BINDING, AND MUTAGENESIS OF LYS-60.
RC   STRAIN=ATCC 33909 / DSM 639 / JCM 8929 / NBRC 15157 / NCIMB 11770;
RX   PubMed=26148716; DOI=10.1128/jb.00344-15;
RA   van Wolferen M., Ma X., Albers S.V.;
RT   "DNA Processing Proteins Involved in the UV-Induced Stress Response of
RT   Sulfolobales.";
RL   J. Bacteriol. 197:2941-2951(2015).
```

Source SHA-256: `e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)  
**Locator:** `lines 45-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:33.887619+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Couples ATP hydrolysis with the unwinding of duplex DNA by
CC         translocating in the 3'-5' direction.; EC=5.6.2.4;
CC         Evidence={ECO:0000269|PubMed:26148716};
```

Source SHA-256: `e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
