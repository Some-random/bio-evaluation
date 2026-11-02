# EC_number_0034

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.1.1.122

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASGARYAGKVVVVTGAARGIGAGIARAFVDSGAQVVICDKDERGGRALEQELRGAVFIRCDVTREEDVRALLSDTVHRFGRLDCVVNNAGSHPPLQPLEETTAQGFRELLELNLLGTYTLCKLAFPHLRRSRGNIINISTLVGAVGQLQGVPYAATKGAVTALTKALALDESQYGVRVNCISPGNIWTPLWQELAALAPDPRAAIREGAMAQPLGRMGQPAEVGAAAVFLASEASFCTGLELFVTGGAELGSGPENFFRSLGLCVVPEDVPPPTSRPRICSYK

[Multiple Choices]
A. 1.1.1.122
B. 1.1.1.1
C. 2.3.1.318
D. 3.1.3.16
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

> The exact sequence matches the rabbit UniProt entry annotated EC 1.1.1.122. Its catalytic-activity annotation assigns this EC to L-fucose oxidation and cites experimental evidence (ECO:0000269, PubMed 38944119), supporting choice A. The archived entry also contains the annotation before the stated historical cutoff.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains features consistent with an NAD(P)-dependent oxidoreductase, which may broadly favor an EC 1.- option, but those features do not establish the enzyme's substrate or distinguish the precise EC number.


**Missing item-specific fact**

> The protein-specific catalytic activity—particularly its oxidation of L-fucose and related sugars, rather than the alternative substrates/reactions represented by the other EC choices—is not supplied in the question.


**Reason**

> Assigning the complete EC number requires protein-specific functional knowledge or experimental/annotation lookup. General sequence-family inference cannot securely distinguish the listed oxidoreductases at this specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Reviewer-only evidence supports A for the sequence-matched protein; no competing listed EC is supported by the supplied evidence.


### Important caveats

- The functional assignment is reported in UniProt with an experimental-evidence code and a cited 2024 publication; the primary study was not independently reviewed here.
- Reviewer-only identity and annotation evidence support the key but were not present in the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features consistent with an NAD(P)-dependent oxidoreductase, which may broadly favor an EC 1.- option, but those features do not establish the enzyme's substrate or distinguish the precise EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—particularly its oxidation of L-fucose and related sugars, rather than the alternative substrates/reactions represented by the other EC choices—is not supplied in the question.",
    "reason": "Assigning the complete EC number requires protein-specific functional knowledge or experimental/annotation lookup. General sequence-family inference cannot securely distinguish the listed oxidoreductases at this specificity."
  },
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the rabbit UniProt entry annotated EC 1.1.1.122. Its catalytic-activity annotation assigns this EC to L-fucose oxidation and cites experimental evidence (ECO:0000269, PubMed 38944119), supporting choice A. The archived entry also contains the annotation before the stated historical cutoff."
  },
  "important_caveats": [
    "The functional assignment is reported in UniProt with an experimental-evidence code and a cited 2024 publication; the primary study was not independently reviewed here.",
    "Reviewer-only identity and annotation evidence support the key but were not present in the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports A for the sequence-matched protein; no competing listed EC is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the rabbit UniProt entry annotated EC 1.1.1.122. Its catalytic-activity annotation assigns this EC to L-fucose oxidation and cites experimental evidence (ECO:0000269, PubMed 38944119), supporting choice A. The archived entry also contains the annotation before the stated historical cutoff.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains features consistent with an NAD(P)-dependent oxidoreductase, which may broadly favor an EC 1.- option, but those features do not establish the enzyme's substrate or distinguish the precise EC number.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—particularly its oxidation of L-fucose and related sugars, rather than the alternative substrates/reactions represented by the other EC choices—is not supplied in the question.",
    "reason": "Assigning the complete EC number requires protein-specific functional knowledge or experimental/annotation lookup. General sequence-family inference cannot securely distinguish the listed oxidoreductases at this specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports A for the sequence-matched protein; no competing listed EC is supported by the supplied evidence."
  },
  "important_caveats": [
    "The functional assignment is reported in UniProt with an experimental-evidence code and a cited 2024 publication; the primary study was not independently reviewed here.",
    "Reviewer-only identity and annotation evidence support the key but were not present in the evaluated model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAT9JA24 (DHB14_RABIT, sequence matched, 284 aa) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, J. Biol. Chem. 2024). The catalytic activity comments confirm three NAD+-dependent sugar oxidations (L-fucose, D-arabinose, L-galactose) all classified under EC 1.1.1.122. The benchmark sequence matches the source sequence exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD(P)-binding motif (VVVVTGAARGIGAGIA, GxGxxG pattern), establishing the protein as an NAD-dependent oxidoreductase and eliminating EC 2.3.1.318 (acyltransferase, no NAD-binding) and EC 3.1.3.16 (phosphatase, no NAD-binding). The protein is 284 aa, lacks the zinc-binding Cys clusters (Cys-X2-Cys…Cys-X2-Cys) characteristic of classical alcohol dehydrogenase (EC 1.1.1.1, typically ~370–400 aa, Zn-dependent), and displays short-chain dehydrogenase/reductase (SDR) family architecture. These features eliminate EC 1.1.1.1 and leave EC 1.1.1.122 (an SDR-family sugar dehydrogenase) as the only viable option among the four choices.


**Missing item-specific fact**

> None critical. Within the constrained MCQ set, the structural/biochemical reasoning (Rossmann fold, SDR architecture, absence of zinc, protein length) sufficiently eliminates B, C, and D. The specific assignment to 1.1.1.122 among all possible SDR EC numbers is handled by the choice set containing only one SDR option.


**Reason**

> A general biologist can reason from the NAD-binding Rossmann fold to class 1.1.1, then use the absence of zinc-binding motifs and the ~284-aa SDR-length architecture to reject classical ADH (1.1.1.1), leaving 1.1.1.122 as the only oxidoreductase option consistent with SDR family features. Transferase and phosphatase classes are excluded by the absence of relevant catalytic motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different EC classes (1, 2, 3) and within class 1 distinguish SDR (1.1.1.122) from classical Zn-ADH (1.1.1.1). The sequence features unambiguously place the protein in the SDR oxidoreductase category, making only option A defensible.


### Important caveats

- The UniProt annotation is based on a single 2024 experimental study (PubMed:38944119); the enzyme was previously known only as HSD17B14 with uncertain function.
- The specific EC number 1.1.1.122 (rather than another SDR-family EC number) is not derivable from sequence motifs alone in an open-ended setting; it is identifiable here only because the MCQ provides a single SDR option.
- The entry was first publicly released in 2025-04-09 (Swiss-Prot), so the experimental annotation postdates many earlier database snapshots; the author's source snapshot is unknown.
- The protein also shows activity toward D-arabinose and L-galactose under the same EC 1.1.1.122 classification, indicating broad sugar dehydrogenase specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif (VVVVTGAARGIGAGIA, GxGxxG pattern), establishing the protein as an NAD-dependent oxidoreductase and eliminating EC 2.3.1.318 (acyltransferase, no NAD-binding) and EC 3.1.3.16 (phosphatase, no NAD-binding). The protein is 284 aa, lacks the zinc-binding Cys clusters (Cys-X2-Cys…Cys-X2-Cys) characteristic of classical alcohol dehydrogenase (EC 1.1.1.1, typically ~370–400 aa, Zn-dependent), and displays short-chain dehydrogenase/reductase (SDR) family architecture. These features eliminate EC 1.1.1.1 and leave EC 1.1.1.122 (an SDR-family sugar dehydrogenase) as the only viable option among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Within the constrained MCQ set, the structural/biochemical reasoning (Rossmann fold, SDR architecture, absence of zinc, protein length) sufficiently eliminates B, C, and D. The specific assignment to 1.1.1.122 among all possible SDR EC numbers is handled by the choice set containing only one SDR option.",
    "reason": "A general biologist can reason from the NAD-binding Rossmann fold to class 1.1.1, then use the absence of zinc-binding motifs and the ~284-aa SDR-length architecture to reject classical ADH (1.1.1.1), leaving 1.1.1.122 as the only oxidoreductase option consistent with SDR family features. Transferase and phosphatase classes are excluded by the absence of relevant catalytic motifs."
  },
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAT9JA24 (DHB14_RABIT, sequence matched, 284 aa) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, J. Biol. Chem. 2024). The catalytic activity comments confirm three NAD+-dependent sugar oxidations (L-fucose, D-arabinose, L-galactose) all classified under EC 1.1.1.122. The benchmark sequence matches the source sequence exactly."
  },
  "important_caveats": [
    "The UniProt annotation is based on a single 2024 experimental study (PubMed:38944119); the enzyme was previously known only as HSD17B14 with uncertain function.",
    "The specific EC number 1.1.1.122 (rather than another SDR-family EC number) is not derivable from sequence motifs alone in an open-ended setting; it is identifiable here only because the MCQ provides a single SDR option.",
    "The entry was first publicly released in 2025-04-09 (Swiss-Prot), so the experimental annotation postdates many earlier database snapshots; the author's source snapshot is unknown.",
    "The protein also shows activity toward D-arabinose and L-galactose under the same EC 1.1.1.122 classification, indicating broad sugar dehydrogenase specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC classes (1, 2, 3) and within class 1 distinguish SDR (1.1.1.122) from classical Zn-ADH (1.1.1.1). The sequence features unambiguously place the protein in the SDR oxidoreductase category, making only option A defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0AAT9JA24 (DHB14_RABIT, sequence matched, 284 aa) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, J. Biol. Chem. 2024). The catalytic activity comments confirm three NAD+-dependent sugar oxidations (L-fucose, D-arabinose, L-galactose) all classified under EC 1.1.1.122. The benchmark sequence matches the source sequence exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif (VVVVTGAARGIGAGIA, GxGxxG pattern), establishing the protein as an NAD-dependent oxidoreductase and eliminating EC 2.3.1.318 (acyltransferase, no NAD-binding) and EC 3.1.3.16 (phosphatase, no NAD-binding). The protein is 284 aa, lacks the zinc-binding Cys clusters (Cys-X2-Cys…Cys-X2-Cys) characteristic of classical alcohol dehydrogenase (EC 1.1.1.1, typically ~370–400 aa, Zn-dependent), and displays short-chain dehydrogenase/reductase (SDR) family architecture. These features eliminate EC 1.1.1.1 and leave EC 1.1.1.122 (an SDR-family sugar dehydrogenase) as the only viable option among the four choices.",
    "missing_item_specific_fact": "None critical. Within the constrained MCQ set, the structural/biochemical reasoning (Rossmann fold, SDR architecture, absence of zinc, protein length) sufficiently eliminates B, C, and D. The specific assignment to 1.1.1.122 among all possible SDR EC numbers is handled by the choice set containing only one SDR option.",
    "reason": "A general biologist can reason from the NAD-binding Rossmann fold to class 1.1.1, then use the absence of zinc-binding motifs and the ~284-aa SDR-length architecture to reject classical ADH (1.1.1.1), leaving 1.1.1.122 as the only oxidoreductase option consistent with SDR family features. Transferase and phosphatase classes are excluded by the absence of relevant catalytic motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC classes (1, 2, 3) and within class 1 distinguish SDR (1.1.1.122) from classical Zn-ADH (1.1.1.1). The sequence features unambiguously place the protein in the SDR oxidoreductase category, making only option A defensible."
  },
  "important_caveats": [
    "The UniProt annotation is based on a single 2024 experimental study (PubMed:38944119); the enzyme was previously known only as HSD17B14 with uncertain function.",
    "The specific EC number 1.1.1.122 (rather than another SDR-family EC number) is not derivable from sequence motifs alone in an open-ended setting; it is identifiable here only because the MCQ provides a single SDR option.",
    "The entry was first publicly released in 2025-04-09 (Swiss-Prot), so the experimental annotation postdates many earlier database snapshots; the author's source snapshot is unknown.",
    "The protein also shows activity toward D-arabinose and L-galactose under the same EC 1.1.1.122 classification, indicating broad sugar dehydrogenase specificity."
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

**Accession:** `A0AAT9JA24` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
"A0AAT9JA24"
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Hydroxysteroid 17-beta dehydrogenase 14"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"value":"1.1.1.122"}],"fullName":{"value":"L-fucose dehydrogenase"}}}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"38944119","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81516"}}],"reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"name":"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81515"},{"database":"ChEBI","id":"CHEBI:2181"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:81457"}]}}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"38944119","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81520"}}],"reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"name":"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81519"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:46994"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:194242"}]}}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"38944119","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81524"}}],"reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"name":"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81523"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:37619"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:182410"}]}}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"citation":{"authors":["Witecka A.","Kazak V.","Kwiatkowski S.","Kiersztan A.","Jagielski A.K.","Kozminski W.","Augustyniak R.","Drozak J."],"citationCrossReferences":[{"database":"PubMed","id":"38944119"},{"database":"DOI","id":"10.1016/j.jbc.2024.107501"}],"citationType":"journal article","firstPage":"107501","id":"38944119","journal":"J. Biol. Chem.","lastPage":"107501","publicationDate":"2024","title":"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway.","volume":"300"},"referenceNumber":2,"referencePositions":["IDENTIFICATION","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF TYR-154"]}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
ID   DHB14_RABIT             Reviewed;         284 AA.
AC   A0AAT9JA24; A0A5F9CLT4;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 2.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=L-fucose dehydrogenase;
DE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};
DE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;
GN   Name=HSD17B14;
OS   Oryctolagus cuniculus (Rabbit).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Lagomorpha; Leporidae; Oryctolagus.
OX   NCBI_TaxID=9986;
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
DE   RecName: Full=L-fucose dehydrogenase;
DE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};
DE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 35-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
RN   [2]
RP   IDENTIFICATION, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL
RP   PROPERTIES, AND MUTAGENESIS OF TYR-154.
RX   PubMed=38944119; DOI=10.1016/j.jbc.2024.107501;
RA   Witecka A., Kazak V., Kwiatkowski S., Kiersztan A., Jagielski A.K.,
RA   Kozminski W., Augustyniak R., Drozak J.;
RT   "Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose
RT   dehydrogenase, the initial enzyme of the L-fucose degradation pathway.";
RL   J. Biol. Chem. 300:107501-107501(2024).
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 50-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);
CC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;
CC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;
CC         Evidence={ECO:0000305|PubMed:38944119};
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 57-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+);
CC         Xref=Rhea:RHEA:81519, ChEBI:CHEBI:15378, ChEBI:CHEBI:46994,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:194242;
CC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81520;
CC         Evidence={ECO:0000305|PubMed:38944119};
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 64-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+);
CC         Xref=Rhea:RHEA:81523, ChEBI:CHEBI:15378, ChEBI:CHEBI:37619,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:182410;
CC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81524;
CC         Evidence={ECO:0000305|PubMed:38944119};
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
