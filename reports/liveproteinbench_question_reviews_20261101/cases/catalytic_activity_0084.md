# catalytic_activity_0084

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — okaramine C + 2 reduced &#91;NADPH--hemoprotein reductase&#93; + 2 O2 = okaramine A + 2 oxidized &#91;NADPH--hemoprotein reductase&#93; + 4 H2O + 2 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLLRPAKYQLPLPPGPRGLPIIGNLHQAPKEKAWEVYKQWSDRYGPIMSVNNGGMITIIVSSHEVVKNFLEKNNAVFSSRPQLLVLERALYGFTTPALPYGEKWLKHRALRGAVLKPAMAVRYRGLQDLESKQLLRDLLYSEDFTQCMRRQAASLFLGIAYGNRFPEETPEIIDIDQAVAQLGGISESMFQGTGMLREFFPVLKYFPGYDKFLKQLDDVGERLANIYVRRFRDGLSTPAWNWAKEYSKRPEAQGMGELELSFCIGSTYQASLTPYEILRIILLAAICHPEEKARLQKEIDLVVGKDNLPGWEHKDRIQFVQAFIYEALRWHAFSPLGAPRAVSRDIEYKGYFIPKGATLVLNQWAMDHDENVYDNPFTFRPQRWIDNPDLPHVIFGFGLRGCPGQHLARDHLFINTARLFWAFNFGNAYENGKKVELDLDELMQPRGGGSAFNQVPSFKASVIIRSSERRQIVENEWDAVEKDEQKILAEAMPLPE

[Multiple Choices]
A. an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)
B. okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)
C. 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)
D. 2'-hydroxy-2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2',2'-dihydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
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

> The supplied sequence exactly matches the UniProt entry for cytochrome P450 monooxygenase okaD. That entry annotates the okaramine C-to-A reaction and cites experimental evidence (ECO:0000269, PubMed 28631282), supporting choice B.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable P450 heme-binding motif (around FGFGLRGCPG), and choice B is the option with NADPH-reductase-supported P450 monooxygenation chemistry. That provides a concrete family-level basis to distinguish B from the glycosylation, hydrolysis, and 2Fe-2S-dependent alternatives.


**Missing item-specific fact**

> The motif does not itself establish okaramine C as the substrate or okaramine A as the product; those exact substrate and product identities are protein-specific.


**Reason**

> The sequence and choices provide meaningful grounds for selecting the P450-compatible reaction, although the exact transformation is not derivable from the motif alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed reactions, B is the one consistent with the sequence's P450-family signal; the alternatives describe different enzyme classes or cofactor chemistry.


### Important caveats

- The sequence match is exact in both the current and historical UniProt records, but the author's source snapshot is unknown.
- The cited experimental evidence is reported in the UniProt annotation; the primary study was not independently retrieved or assessed here.
- Family-level sequence evidence supports choosing B among these options but does not independently establish its precise okaramine substrate and product.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable P450 heme-binding motif (around FGFGLRGCPG), and choice B is the option with NADPH-reductase-supported P450 monooxygenation chemistry. That provides a concrete family-level basis to distinguish B from the glycosylation, hydrolysis, and 2Fe-2S-dependent alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The motif does not itself establish okaramine C as the substrate or okaramine A as the product; those exact substrate and product identities are protein-specific.",
    "reason": "The sequence and choices provide meaningful grounds for selecting the P450-compatible reaction, although the exact transformation is not derivable from the motif alone."
  },
  "case_id": "catalytic_activity_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for cytochrome P450 monooxygenase okaD. That entry annotates the okaramine C-to-A reaction and cites experimental evidence (ECO:0000269, PubMed 28631282), supporting choice B."
  },
  "important_caveats": [
    "The sequence match is exact in both the current and historical UniProt records, but the author's source snapshot is unknown.",
    "The cited experimental evidence is reported in the UniProt annotation; the primary study was not independently retrieved or assessed here.",
    "Family-level sequence evidence supports choosing B among these options but does not independently establish its precise okaramine substrate and product."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, B is the one consistent with the sequence's P450-family signal; the alternatives describe different enzyme classes or cofactor chemistry."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for cytochrome P450 monooxygenase okaD. That entry annotates the okaramine C-to-A reaction and cites experimental evidence (ECO:0000269, PubMed 28631282), supporting choice B.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable P450 heme-binding motif (around FGFGLRGCPG), and choice B is the option with NADPH-reductase-supported P450 monooxygenation chemistry. That provides a concrete family-level basis to distinguish B from the glycosylation, hydrolysis, and 2Fe-2S-dependent alternatives.",
    "missing_item_specific_fact": "The motif does not itself establish okaramine C as the substrate or okaramine A as the product; those exact substrate and product identities are protein-specific.",
    "reason": "The sequence and choices provide meaningful grounds for selecting the P450-compatible reaction, although the exact transformation is not derivable from the motif alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, B is the one consistent with the sequence's P450-family signal; the alternatives describe different enzyme classes or cofactor chemistry."
  },
  "important_caveats": [
    "The sequence match is exact in both the current and historical UniProt records, but the author's source snapshot is unknown.",
    "The cited experimental evidence is reported in the UniProt annotation; the primary study was not independently retrieved or assessed here.",
    "Family-level sequence evidence supports choosing B among these options but does not independently establish its precise okaramine substrate and product."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A2Z5U6I9 (sequence matched exactly, 529 aa) annotates this protein as 'Cytochrome P450 monooxygenase okaD' (EC 1.14.99.-) from Penicillium ochrochloron. The CATALYTIC ACTIVITY comment explicitly states the reaction 'okaramine C + 2 reduced &#91;NADPH--hemoprotein reductase&#93; + 2 O2 = okaramine A + 2 oxidized &#91;NADPH--hemoprotein reductase&#93; + 4 H2O + 2 H(+)' with evidence code ECO:0000269 (experimental evidence) from PubMed:28631282 (Lai et al., 2017, Angew. Chem. Int. Ed. 56:9478-9482). The annotation is backed by experimental evidence from the primary literature.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could recognize P450-like sequence features (heme-binding region, ~500 aa length, fungal origin) to eliminate Choice A (mannosyltransferase/GT reaction) and Choice C (esterase/hydrolase reaction). Additionally, cofactor logic could partially distinguish B from D: fungal/microbial P450s typically use NADPH--hemoprotein reductase (Choice B), whereas &#91;2Fe-2S&#93;-ferredoxin-dependent P450s (Choice D) are characteristic of plant chloroplast systems. However, this reasoning cannot identify the specific substrates 'okaramine C' and 'okaramine A'—highly specialized indole alkaloid intermediates unique to the Penicillium ochrochloron okaramine biosynthetic pathway.


**Missing item-specific fact**

> The specific identity of this P450 as okaD and its experimentally determined substrate/product pair (okaramine C → okaramine A) from the 2017 biosynthetic pathway elucidation study. No general biological reasoning from the amino acid sequence can predict that this particular fungal P450 acts on okaramine intermediates rather than other fungal secondary metabolites.


**Reason**

> While P450 recognition and cofactor-type reasoning can narrow four choices to two (B vs D), the final identification of okaramine C as substrate and okaramine A as product is an item-specific experimental finding (PubMed:28631282) that cannot be deduced from sequence features alone. The substrate names appear nowhere in the sequence and are not inferable from general pathway logic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both B and D describe P450-type oxygenation reactions. A model recognizing P450 features could eliminate A (transferase) and C (hydrolase), but distinguishing B from D requires either (a) knowing the specific pathway (lookup) or (b) applying the heuristic that fungal P450s use NADPH-hemoprotein reductase while plant P450s use ferredoxin. The latter is a reasonable general-knowledge inference but does not confirm the specific okaramine substrates. Without the pathway-specific fact, D remains a superficially plausible P450 reaction.


### Important caveats

- The UniProt annotation carries ECO:0000269 (experimental evidence) from PubMed:28631282, so the key is experimentally grounded, not merely computational.
- The sequence-to-accession match is exact (SHA-256 identical), confirming the annotation applies to this exact protein.
- The first public date of this Swiss-Prot entry is 2025-02-05, meaning the curated annotation post-dates the 2017 primary paper by ~8 years; the benchmark may have been constructed from the primary paper directly or from the curated entry.
- The okaramine pathway is a narrow fungal natural-product biosynthesis topic; general enzymology knowledge provides cofactor-level discrimination but not substrate-level identification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could recognize P450-like sequence features (heme-binding region, ~500 aa length, fungal origin) to eliminate Choice A (mannosyltransferase/GT reaction) and Choice C (esterase/hydrolase reaction). Additionally, cofactor logic could partially distinguish B from D: fungal/microbial P450s typically use NADPH--hemoprotein reductase (Choice B), whereas [2Fe-2S]-ferredoxin-dependent P450s (Choice D) are characteristic of plant chloroplast systems. However, this reasoning cannot identify the specific substrates 'okaramine C' and 'okaramine A'—highly specialized indole alkaloid intermediates unique to the Penicillium ochrochloron okaramine biosynthetic pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this P450 as okaD and its experimentally determined substrate/product pair (okaramine C → okaramine A) from the 2017 biosynthetic pathway elucidation study. No general biological reasoning from the amino acid sequence can predict that this particular fungal P450 acts on okaramine intermediates rather than other fungal secondary metabolites.",
    "reason": "While P450 recognition and cofactor-type reasoning can narrow four choices to two (B vs D), the final identification of okaramine C as substrate and okaramine A as product is an item-specific experimental finding (PubMed:28631282) that cannot be deduced from sequence features alone. The substrate names appear nowhere in the sequence and are not inferable from general pathway logic."
  },
  "case_id": "catalytic_activity_0084",
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
    "reason": "The UniProt entry A0A2Z5U6I9 (sequence matched exactly, 529 aa) annotates this protein as 'Cytochrome P450 monooxygenase okaD' (EC 1.14.99.-) from Penicillium ochrochloron. The CATALYTIC ACTIVITY comment explicitly states the reaction 'okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)' with evidence code ECO:0000269 (experimental evidence) from PubMed:28631282 (Lai et al., 2017, Angew. Chem. Int. Ed. 56:9478-9482). The annotation is backed by experimental evidence from the primary literature."
  },
  "important_caveats": [
    "The UniProt annotation carries ECO:0000269 (experimental evidence) from PubMed:28631282, so the key is experimentally grounded, not merely computational.",
    "The sequence-to-accession match is exact (SHA-256 identical), confirming the annotation applies to this exact protein.",
    "The first public date of this Swiss-Prot entry is 2025-02-05, meaning the curated annotation post-dates the 2017 primary paper by ~8 years; the benchmark may have been constructed from the primary paper directly or from the curated entry.",
    "The okaramine pathway is a narrow fungal natural-product biosynthesis topic; general enzymology knowledge provides cofactor-level discrimination but not substrate-level identification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both B and D describe P450-type oxygenation reactions. A model recognizing P450 features could eliminate A (transferase) and C (hydrolase), but distinguishing B from D requires either (a) knowing the specific pathway (lookup) or (b) applying the heuristic that fungal P450s use NADPH-hemoprotein reductase while plant P450s use ferredoxin. The latter is a reasonable general-knowledge inference but does not confirm the specific okaramine substrates. Without the pathway-specific fact, D remains a superficially plausible P450 reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A2Z5U6I9 (sequence matched exactly, 529 aa) annotates this protein as 'Cytochrome P450 monooxygenase okaD' (EC 1.14.99.-) from Penicillium ochrochloron. The CATALYTIC ACTIVITY comment explicitly states the reaction 'okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)' with evidence code ECO:0000269 (experimental evidence) from PubMed:28631282 (Lai et al., 2017, Angew. Chem. Int. Ed. 56:9478-9482). The annotation is backed by experimental evidence from the primary literature.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could recognize P450-like sequence features (heme-binding region, ~500 aa length, fungal origin) to eliminate Choice A (mannosyltransferase/GT reaction) and Choice C (esterase/hydrolase reaction). Additionally, cofactor logic could partially distinguish B from D: fungal/microbial P450s typically use NADPH--hemoprotein reductase (Choice B), whereas [2Fe-2S]-ferredoxin-dependent P450s (Choice D) are characteristic of plant chloroplast systems. However, this reasoning cannot identify the specific substrates 'okaramine C' and 'okaramine A'—highly specialized indole alkaloid intermediates unique to the Penicillium ochrochloron okaramine biosynthetic pathway.",
    "missing_item_specific_fact": "The specific identity of this P450 as okaD and its experimentally determined substrate/product pair (okaramine C → okaramine A) from the 2017 biosynthetic pathway elucidation study. No general biological reasoning from the amino acid sequence can predict that this particular fungal P450 acts on okaramine intermediates rather than other fungal secondary metabolites.",
    "reason": "While P450 recognition and cofactor-type reasoning can narrow four choices to two (B vs D), the final identification of okaramine C as substrate and okaramine A as product is an item-specific experimental finding (PubMed:28631282) that cannot be deduced from sequence features alone. The substrate names appear nowhere in the sequence and are not inferable from general pathway logic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both B and D describe P450-type oxygenation reactions. A model recognizing P450 features could eliminate A (transferase) and C (hydrolase), but distinguishing B from D requires either (a) knowing the specific pathway (lookup) or (b) applying the heuristic that fungal P450s use NADPH-hemoprotein reductase while plant P450s use ferredoxin. The latter is a reasonable general-knowledge inference but does not confirm the specific okaramine substrates. Without the pathway-specific fact, D remains a superficially plausible P450 reaction."
  },
  "important_caveats": [
    "The UniProt annotation carries ECO:0000269 (experimental evidence) from PubMed:28631282, so the key is experimentally grounded, not merely computational.",
    "The sequence-to-accession match is exact (SHA-256 identical), confirming the annotation applies to this exact protein.",
    "The first public date of this Swiss-Prot entry is 2025-02-05, meaning the curated annotation post-dates the 2017 primary paper by ~8 years; the benchmark may have been constructed from the primary paper directly or from the curated entry.",
    "The okaramine pathway is a narrow fungal natural-product biosynthesis topic; general enzymology knowledge provides cofactor-level discrimination but not substrate-level identification."
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

**Accession:** `A0A2Z5U6I9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 23. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:54.111891+00:00.  

```json
"A0A2Z5U6I9"
```

Source SHA-256: `40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:54.111891+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Okaramines biosynthesis cluster protein D"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"value":"1.14.99.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase okaD"}}}
```

Source SHA-256: `40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:54.111891+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:82704"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"name":"okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:82703"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:193028"},{"database":"ChEBI","id":"CHEBI:232464"}]}}
```

Source SHA-256: `40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:54.111891+00:00.  

```json
{"citation":{"authors":["Lai C.Y.","Lo I.W.","Hewage R.T.","Chen Y.C.","Chen C.T.","Lee C.F.","Lin S.","Tang M.C.","Lin H.C."],"citationCrossReferences":[{"database":"PubMed","id":"28631282"},{"database":"DOI","id":"10.1002/anie.201705501"}],"citationType":"journal article","firstPage":"9478","id":"28631282","journal":"Angew. Chem. Int. Ed.","lastPage":"9482","publicationDate":"2017","title":"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise Pathway of Okaramines.","volume":"56"},"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:57.209412+00:00.  

```text
ID   OKAD_PENOH              Reviewed;         529 AA.
AC   A0A2Z5U6I9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-OCT-2018, sequence version 1.
DT   28-JAN-2026, entry version 23.
DE   RecName: Full=Cytochrome P450 monooxygenase okaD {ECO:0000303|PubMed:28631282};
DE            EC=1.14.99.- {ECO:0000269|PubMed:28631282};
DE   AltName: Full=Okaramines biosynthesis cluster protein D {ECO:0000303|PubMed:28631282};
GN   Name=okaD {ECO:0000303|PubMed:28631282};
OS   Penicillium ochrochloron.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=69780;
```

Source SHA-256: `325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:57.209412+00:00.  

```text
DE   RecName: Full=Cytochrome P450 monooxygenase okaD {ECO:0000303|PubMed:28631282};
DE            EC=1.14.99.- {ECO:0000269|PubMed:28631282};
DE   AltName: Full=Okaramines biosynthesis cluster protein D {ECO:0000303|PubMed:28631282};
```

Source SHA-256: `325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)  
**Locator:** `lines 24-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:57.209412+00:00.  

```text
RN   [2]
RP   FUNCTION, DISRUPTION PHENOTYPE, CATALYTIC ACTIVITY, AND PATHWAY.
RX   PubMed=28631282; DOI=10.1002/anie.201705501;
RA   Lai C.Y., Lo I.W., Hewage R.T., Chen Y.C., Chen C.T., Lee C.F., Lin S.,
RA   Tang M.C., Lin H.C.;
RT   "Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise
RT   Pathway of Okaramines.";
RL   Angew. Chem. Int. Ed. 56:9478-9482(2017).
```

Source SHA-256: `325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)  
**Locator:** `lines 58-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:57.209412+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2
CC         = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2
CC         H(+); Xref=Rhea:RHEA:82703, Rhea:RHEA-COMP:11964, Rhea:RHEA-
CC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:193028,
CC         ChEBI:CHEBI:232464; Evidence={ECO:0000269|PubMed:28631282};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82704;
CC         Evidence={ECO:0000269|PubMed:28631282};
```

Source SHA-256: `325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
