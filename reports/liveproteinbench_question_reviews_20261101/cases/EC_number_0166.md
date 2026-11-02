# EC_number_0166

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.1.1.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLEILADESVGGNSPTVIINRGAKKMQWPFIGCGGLGFSKTAHFTCFDSMTQLCEEDIPCIHLPPQHRSVYKMSTENKMRAVVFHSPYKVAVEERPIPKIQDSGDIVVKVTYTALCGSDLHTFRGIEPAGTGFVMGHEVTGEVVEVGSGVKSIQKGDMVVSAFTTSCGECFYCKQGFSSRCEKSVLFGCDHLDGAQAEYVRIPNADGTVMKAPEGVEEKYLVLMADIFPTGYFAASNAFKGYTPEQISEQTVVLIGCGPVGLCALINALEFKPKHLLAVDSIPSRLELARSLGAEPWNFQQDREGLDKRVKELTNGRGADAVIEVVGLSPALRTGFDLLRPWGTISSVGVHNGEIPWAGNDAYDKNLRIQMGRCPVRSVSPQALDVLKKNQHKLGFMADKIMPLSQAVEGYELFNAMKVQKVIFKAGE

[Multiple Choices]
A. 1.1.1.122
B. 1.1.1.1
C. 4.2.1.121
D. 2.7.11.1
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

> The exact sequence matches a UniProt entry annotated as zinc-type alcohol dehydrogenase B with EC 1.1.1.1; the EC annotation cites experimental evidence. The listed catalytic reactions are supported by transfer from another UniProt entry, so they are not independent direct measurements for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a zinc-type alcohol dehydrogenase, which helps distinguish it from the kinase and enolase choices. That broad identification does not establish the precise EC number among potentially related oxidoreductases.


**Missing item-specific fact**

> The protein-specific reaction classification—especially substrate specificity needed to distinguish EC 1.1.1.1 from a related oxidoreductase EC—requires an annotation, homolog-specific fact, or experimental characterization absent from the input.


**Reason**

> Sequence-based family recognition can narrow the choices, but the exact four-part EC assignment depends on item-specific functional knowledge rather than a sufficiently discriminating argument from the supplied sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched database record supports choice B; the evidence does not establish another listed EC as a competing classification for this sequence.


### Important caveats

- The reviewer-only UniProt accession and annotations were not supplied to the evaluated model.
- The cited EC annotation has an experimental evidence code, but the primary paper was not independently reviewed here; the detailed catalytic-reaction annotations cite evidence transferred from another UniProt entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a zinc-type alcohol dehydrogenase, which helps distinguish it from the kinase and enolase choices. That broad identification does not establish the precise EC number among potentially related oxidoreductases.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific reaction classification—especially substrate specificity needed to distinguish EC 1.1.1.1 from a related oxidoreductase EC—requires an annotation, homolog-specific fact, or experimental characterization absent from the input.",
    "reason": "Sequence-based family recognition can narrow the choices, but the exact four-part EC assignment depends on item-specific functional knowledge rather than a sufficiently discriminating argument from the supplied sequence alone."
  },
  "case_id": "EC_number_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as zinc-type alcohol dehydrogenase B with EC 1.1.1.1; the EC annotation cites experimental evidence. The listed catalytic reactions are supported by transfer from another UniProt entry, so they are not independent direct measurements for this sequence."
  },
  "important_caveats": [
    "The reviewer-only UniProt accession and annotations were not supplied to the evaluated model.",
    "The cited EC annotation has an experimental evidence code, but the primary paper was not independently reviewed here; the detailed catalytic-reaction annotations cite evidence transferred from another UniProt entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database record supports choice B; the evidence does not establish another listed EC as a competing classification for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as zinc-type alcohol dehydrogenase B with EC 1.1.1.1; the EC annotation cites experimental evidence. The listed catalytic reactions are supported by transfer from another UniProt entry, so they are not independent direct measurements for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a zinc-type alcohol dehydrogenase, which helps distinguish it from the kinase and enolase choices. That broad identification does not establish the precise EC number among potentially related oxidoreductases.",
    "missing_item_specific_fact": "The protein-specific reaction classification—especially substrate specificity needed to distinguish EC 1.1.1.1 from a related oxidoreductase EC—requires an annotation, homolog-specific fact, or experimental characterization absent from the input.",
    "reason": "Sequence-based family recognition can narrow the choices, but the exact four-part EC assignment depends on item-specific functional knowledge rather than a sufficiently discriminating argument from the supplied sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database record supports choice B; the evidence does not establish another listed EC as a competing classification for this sequence."
  },
  "important_caveats": [
    "The reviewer-only UniProt accession and annotations were not supplied to the evaluated model.",
    "The cited EC annotation has an experimental evidence code, but the primary paper was not independently reviewed here; the detailed catalytic-reaction annotations cite evidence transferred from another UniProt entry."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7U2MMF3 (ADHB_ASPFN, Aspergillus flavus) is annotated with EC 1.1.1.1 (Zinc-type alcohol dehydrogenase B) with experimental evidence code ECO:0000269 from PubMed:39601562. Catalytic activity comments confirm NAD-dependent oxidation of primary and secondary alcohols. The benchmark sequence (428 aa) matches the UniProt sequence exactly. The author key B (1.1.1.1) is consistent with the database annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a zinc-binding cysteine cluster (CGECFYCKQGFSSRCEKSVLFGCDHLDG) and a Rossmann-fold motif (GCGPVGLCALINALEFKPKHLL), which together support classification as a zinc-dependent alcohol dehydrogenase (EC 1.1.1.x), effectively eliminating C (lyase, EC 4.2.1.121) and D (kinase, EC 2.7.11.1). However, distinguishing EC 1.1.1.1 (NAD+) from EC 1.1.1.122 (NADP+) requires knowledge of specific cofactor-binding pocket residues that discriminate the 2'-phosphate of NADP+, or knowledge of which structural subfamily this particular enzyme belongs to. The sequence-level features (zinc coordination pattern, Rossmann fold) are broadly consistent with classical zinc ADHs but do not unambiguously resolve the 4th digit without item-specific structural or experimental knowledge.


**Missing item-specific fact**

> The specific cofactor preference (NAD+ vs NADP+) of this Aspergillus flavus AdhB enzyme, determined experimentally (PubMed:39601562), is the decisive fact. Without knowing whether this particular enzyme has residues in its cofactor-binding pocket that accommodate or exclude the 2'-phosphate of NADP+, the 4th digit (1 vs 122) cannot be reliably assigned from sequence alone.


**Reason**

> The broader EC class (1.1.1.x, oxidoreductase acting on CH-OH with NAD/NADP) is inferable from zinc-binding motifs and Rossmann fold. But the final digit distinguishing NAD+ (1) from NADP+ (122) preference is a fine biochemical distinction that depends on the specific 3D arrangement of residues in the cofactor pocket, which is not reliably readable from the linear sequence without specialized structural knowledge of this particular enzyme family member.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (1.1.1.122, alcohol dehydrogenase NADP+) and B (1.1.1.1, alcohol dehydrogenase NAD+) are zinc-dependent alcohol dehydrogenases with similar overall architecture. From the linear sequence alone, without knowledge of the specific cofactor-binding pocket geometry, a model could reasonably select either. The zinc-binding cysteine clusters and Rossmann fold are present in both classes. The distinction requires item-specific knowledge of this enzyme's experimentally determined cofactor preference.


### Important caveats

- The UniProt annotation for the catalytic activity comments uses evidence code ECO:0000250 (transferred from UniProtKB:P11766, horse liver ADH) for the reaction equations, while the EC number assignment itself uses ECO:0000269 (experimental evidence from PubMed:39601562). The primary experimental evidence is from the 2025 MBio paper.
- The sequence was first publicly released in April 2025; the benchmark may have been constructed before or after this annotation was available, affecting whether the answer was accessible via database lookup at construction time.
- The identity origin (accession inferred from dataset image-path metadata) is reviewer-only and was not available to the evaluated model.
- Distractors C (4.2.1.121, lyase) and D (2.7.11.1, kinase) are clearly eliminable by any model recognizing oxidoreductase features, making the effective discrimination between A and B the core challenge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a zinc-binding cysteine cluster (CGECFYCKQGFSSRCEKSVLFGCDHLDG) and a Rossmann-fold motif (GCGPVGLCALINALEFKPKHLL), which together support classification as a zinc-dependent alcohol dehydrogenase (EC 1.1.1.x), effectively eliminating C (lyase, EC 4.2.1.121) and D (kinase, EC 2.7.11.1). However, distinguishing EC 1.1.1.1 (NAD+) from EC 1.1.1.122 (NADP+) requires knowledge of specific cofactor-binding pocket residues that discriminate the 2'-phosphate of NADP+, or knowledge of which structural subfamily this particular enzyme belongs to. The sequence-level features (zinc coordination pattern, Rossmann fold) are broadly consistent with classical zinc ADHs but do not unambiguously resolve the 4th digit without item-specific structural or experimental knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific cofactor preference (NAD+ vs NADP+) of this Aspergillus flavus AdhB enzyme, determined experimentally (PubMed:39601562), is the decisive fact. Without knowing whether this particular enzyme has residues in its cofactor-binding pocket that accommodate or exclude the 2'-phosphate of NADP+, the 4th digit (1 vs 122) cannot be reliably assigned from sequence alone.",
    "reason": "The broader EC class (1.1.1.x, oxidoreductase acting on CH-OH with NAD/NADP) is inferable from zinc-binding motifs and Rossmann fold. But the final digit distinguishing NAD+ (1) from NADP+ (122) preference is a fine biochemical distinction that depends on the specific 3D arrangement of residues in the cofactor pocket, which is not reliably readable from the linear sequence without specialized structural knowledge of this particular enzyme family member."
  },
  "case_id": "EC_number_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A7U2MMF3 (ADHB_ASPFN, Aspergillus flavus) is annotated with EC 1.1.1.1 (Zinc-type alcohol dehydrogenase B) with experimental evidence code ECO:0000269 from PubMed:39601562. Catalytic activity comments confirm NAD-dependent oxidation of primary and secondary alcohols. The benchmark sequence (428 aa) matches the UniProt sequence exactly. The author key B (1.1.1.1) is consistent with the database annotation."
  },
  "important_caveats": [
    "The UniProt annotation for the catalytic activity comments uses evidence code ECO:0000250 (transferred from UniProtKB:P11766, horse liver ADH) for the reaction equations, while the EC number assignment itself uses ECO:0000269 (experimental evidence from PubMed:39601562). The primary experimental evidence is from the 2025 MBio paper.",
    "The sequence was first publicly released in April 2025; the benchmark may have been constructed before or after this annotation was available, affecting whether the answer was accessible via database lookup at construction time.",
    "The identity origin (accession inferred from dataset image-path metadata) is reviewer-only and was not available to the evaluated model.",
    "Distractors C (4.2.1.121, lyase) and D (2.7.11.1, kinase) are clearly eliminable by any model recognizing oxidoreductase features, making the effective discrimination between A and B the core challenge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (1.1.1.122, alcohol dehydrogenase NADP+) and B (1.1.1.1, alcohol dehydrogenase NAD+) are zinc-dependent alcohol dehydrogenases with similar overall architecture. From the linear sequence alone, without knowledge of the specific cofactor-binding pocket geometry, a model could reasonably select either. The zinc-binding cysteine clusters and Rossmann fold are present in both classes. The distinction requires item-specific knowledge of this enzyme's experimentally determined cofactor preference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7U2MMF3 (ADHB_ASPFN, Aspergillus flavus) is annotated with EC 1.1.1.1 (Zinc-type alcohol dehydrogenase B) with experimental evidence code ECO:0000269 from PubMed:39601562. Catalytic activity comments confirm NAD-dependent oxidation of primary and secondary alcohols. The benchmark sequence (428 aa) matches the UniProt sequence exactly. The author key B (1.1.1.1) is consistent with the database annotation.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a zinc-binding cysteine cluster (CGECFYCKQGFSSRCEKSVLFGCDHLDG) and a Rossmann-fold motif (GCGPVGLCALINALEFKPKHLL), which together support classification as a zinc-dependent alcohol dehydrogenase (EC 1.1.1.x), effectively eliminating C (lyase, EC 4.2.1.121) and D (kinase, EC 2.7.11.1). However, distinguishing EC 1.1.1.1 (NAD+) from EC 1.1.1.122 (NADP+) requires knowledge of specific cofactor-binding pocket residues that discriminate the 2'-phosphate of NADP+, or knowledge of which structural subfamily this particular enzyme belongs to. The sequence-level features (zinc coordination pattern, Rossmann fold) are broadly consistent with classical zinc ADHs but do not unambiguously resolve the 4th digit without item-specific structural or experimental knowledge.",
    "missing_item_specific_fact": "The specific cofactor preference (NAD+ vs NADP+) of this Aspergillus flavus AdhB enzyme, determined experimentally (PubMed:39601562), is the decisive fact. Without knowing whether this particular enzyme has residues in its cofactor-binding pocket that accommodate or exclude the 2'-phosphate of NADP+, the 4th digit (1 vs 122) cannot be reliably assigned from sequence alone.",
    "reason": "The broader EC class (1.1.1.x, oxidoreductase acting on CH-OH with NAD/NADP) is inferable from zinc-binding motifs and Rossmann fold. But the final digit distinguishing NAD+ (1) from NADP+ (122) preference is a fine biochemical distinction that depends on the specific 3D arrangement of residues in the cofactor pocket, which is not reliably readable from the linear sequence without specialized structural knowledge of this particular enzyme family member."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (1.1.1.122, alcohol dehydrogenase NADP+) and B (1.1.1.1, alcohol dehydrogenase NAD+) are zinc-dependent alcohol dehydrogenases with similar overall architecture. From the linear sequence alone, without knowledge of the specific cofactor-binding pocket geometry, a model could reasonably select either. The zinc-binding cysteine clusters and Rossmann fold are present in both classes. The distinction requires item-specific knowledge of this enzyme's experimentally determined cofactor preference."
  },
  "important_caveats": [
    "The UniProt annotation for the catalytic activity comments uses evidence code ECO:0000250 (transferred from UniProtKB:P11766, horse liver ADH) for the reaction equations, while the EC number assignment itself uses ECO:0000269 (experimental evidence from PubMed:39601562). The primary experimental evidence is from the 2025 MBio paper.",
    "The sequence was first publicly released in April 2025; the benchmark may have been constructed before or after this annotation was available, affecting whether the answer was accessible via database lookup at construction time.",
    "The identity origin (accession inferred from dataset image-path metadata) is reviewer-only and was not available to the evaluated model.",
    "Distractors C (4.2.1.121, lyase) and D (2.7.11.1, kinase) are clearly eliminable by any model recognizing oxidoreductase features, making the effective discrimination between A and B the core challenge."
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

**Accession:** `A0A7U2MMF3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 6. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MMF3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.417589+00:00.  

```json
"A0A7U2MMF3"
```

Source SHA-256: `e46822396e66b1f6560085f9592ff59bbb63670635ea2594ff88b97769995e9b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MMF3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.417589+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39601562","source":"PubMed"}],"value":"1.1.1.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39601562","source":"PubMed"}],"value":"Zinc-type alcohol dehydrogenase B"}}}
```

Source SHA-256: `e46822396e66b1f6560085f9592ff59bbb63670635ea2594ff88b97769995e9b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MMF3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.417589+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P11766","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:10737"}}],"reaction":{"ecNumber":"1.1.1.1","evidences":[{"evidenceCode":"ECO:0000250","id":"P11766","source":"UniProtKB"}],"name":"a primary alcohol + NAD(+) = an aldehyde + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:10736"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15734"},{"database":"ChEBI","id":"CHEBI:17478"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"}]}}
```

Source SHA-256: `e46822396e66b1f6560085f9592ff59bbb63670635ea2594ff88b97769995e9b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MMF3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.417589+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P11766","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:10741"}}],"reaction":{"ecNumber":"1.1.1.1","evidences":[{"evidenceCode":"ECO:0000250","id":"P11766","source":"UniProtKB"}],"name":"a secondary alcohol + NAD(+) = a ketone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:10740"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17087"},{"database":"ChEBI","id":"CHEBI:35681"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"}]}}
```

Source SHA-256: `e46822396e66b1f6560085f9592ff59bbb63670635ea2594ff88b97769995e9b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MMF3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.417589+00:00.  

```json
{"citation":{"authors":["Chen X.","Wu L.","Zhang Y.","Wang S.","Wang S."],"citationCrossReferences":[{"database":"PubMed","id":"39601562"},{"database":"DOI","id":"10.1128/mbio.02665-24"}],"citationType":"journal article","firstPage":"e0266524","id":"39601562","journal":"MBio","lastPage":"e0266524","publicationDate":"2025","title":"Importance of benzoyltransferase GcnE and lysine benzoylation of alcohol dehydrogenase AdhB in pathogenesis and aflatoxin production in Aspergillus flavus.","volume":"16"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BENZOYLATION AT LYS-393","MUTAGENESIS OF LYS-393","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `e46822396e66b1f6560085f9592ff59bbb63670635ea2594ff88b97769995e9b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MMF3?format=txt&versions=6)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-02T04:25:55.240936+00:00.  

```text
ID   ADHB_ASPFN              Reviewed;         428 AA.
AC   A0A7U2MMF3;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-MAY-2024, sequence version 1.
DT   28-JAN-2026, entry version 6.
DE   RecName: Full=Zinc-type alcohol dehydrogenase B {ECO:0000303|PubMed:39601562};
DE            EC=1.1.1.1 {ECO:0000269|PubMed:39601562};
GN   Name=adhB {ECO:0000303|PubMed:39601562}; ORFNames=F9C07_7207;
OS   Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357
OS   / JCM 12722 / SRRC 167).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=332952;
```

Source SHA-256: `7d4faaa36f941085d4c1a6051f22ec6d1c6e4b6f59555b76c64575e9cff75ee7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MMF3?format=txt&versions=6)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-02T04:25:55.240936+00:00.  

```text
DE   RecName: Full=Zinc-type alcohol dehydrogenase B {ECO:0000303|PubMed:39601562};
DE            EC=1.1.1.1 {ECO:0000269|PubMed:39601562};
```

Source SHA-256: `7d4faaa36f941085d4c1a6051f22ec6d1c6e4b6f59555b76c64575e9cff75ee7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MMF3?format=txt&versions=6)  
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-02T04:25:55.240936+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a primary alcohol + NAD(+) = an aldehyde + NADH + H(+);
CC         Xref=Rhea:RHEA:10736, ChEBI:CHEBI:15378, ChEBI:CHEBI:15734,
CC         ChEBI:CHEBI:17478, ChEBI:CHEBI:57540, ChEBI:CHEBI:57945; EC=1.1.1.1;
CC         Evidence={ECO:0000250|UniProtKB:P11766};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:10737;
CC         Evidence={ECO:0000250|UniProtKB:P11766};
```

Source SHA-256: `7d4faaa36f941085d4c1a6051f22ec6d1c6e4b6f59555b76c64575e9cff75ee7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MMF3?format=txt&versions=6)  
**Locator:** `lines 47-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-02T04:25:55.240936+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a secondary alcohol + NAD(+) = a ketone + NADH + H(+);
CC         Xref=Rhea:RHEA:10740, ChEBI:CHEBI:15378, ChEBI:CHEBI:17087,
CC         ChEBI:CHEBI:35681, ChEBI:CHEBI:57540, ChEBI:CHEBI:57945; EC=1.1.1.1;
CC         Evidence={ECO:0000250|UniProtKB:P11766};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:10741;
CC         Evidence={ECO:0000250|UniProtKB:P11766};
```

Source SHA-256: `7d4faaa36f941085d4c1a6051f22ec6d1c6e4b6f59555b76c64575e9cff75ee7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 166. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
