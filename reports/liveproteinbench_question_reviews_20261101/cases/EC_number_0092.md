# EC_number_0092

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.1.1.122

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAAVTRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRALEQELSGTVFIPGDVTQERDLQTLVSETLSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEVNLLGTYTLIKLALPHLRKSRGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRHGVRVNCISPGNIWTPLWEELAASTSDPRATILEGTLAQPLGRMGQPAEVAAAAVFLASEATFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH

[Multiple Choices]
A. 1.1.1.195
B. 1.1.1.122
C. 2.3.1.319
D. 4.1.1.128
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

> The exact sequence matches the mouse UniProt entry annotated with EC 1.1.1.122. However, the annotation and catalytic-reaction entries cite evidence transferred from another UniProt entry (ECO:0000250), so this supports the key as a database annotation rather than establishing direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an oxidoreductase family, but the provided sequence and choices do not meaningfully establish the precise substrate specificity needed to distinguish these complete EC numbers.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental substrate/reaction evidence identifying this enzyme with EC 1.1.1.122 is absent from the input.


**Reason**

> Choosing the exact four-digit EC number requires item-specific functional information; recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The input does not provide enough evidence to justify any exact EC option, but that lack of discrimination alone does not establish that another listed option is correct.


### Important caveats

- The reviewer-only sequence match establishes applicability of the cited database record, not that the evaluated model had access to that identity or annotation.
- The EC assignment is supported by transferred annotation; direct experimental validation for this exact mouse protein is not established by the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an oxidoreductase family, but the provided sequence and choices do not meaningfully establish the precise substrate specificity needed to distinguish these complete EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental substrate/reaction evidence identifying this enzyme with EC 1.1.1.122 is absent from the input.",
    "reason": "Choosing the exact four-digit EC number requires item-specific functional information; recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from the supplied evidence."
  },
  "case_id": "EC_number_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the mouse UniProt entry annotated with EC 1.1.1.122. However, the annotation and catalytic-reaction entries cite evidence transferred from another UniProt entry (ECO:0000250), so this supports the key as a database annotation rather than establishing direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The reviewer-only sequence match establishes applicability of the cited database record, not that the evaluated model had access to that identity or annotation.",
    "The EC assignment is supported by transferred annotation; direct experimental validation for this exact mouse protein is not established by the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The input does not provide enough evidence to justify any exact EC option, but that lack of discrimination alone does not establish that another listed option is correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the mouse UniProt entry annotated with EC 1.1.1.122. However, the annotation and catalytic-reaction entries cite evidence transferred from another UniProt entry (ECO:0000250), so this supports the key as a database annotation rather than establishing direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an oxidoreductase family, but the provided sequence and choices do not meaningfully establish the precise substrate specificity needed to distinguish these complete EC numbers.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental substrate/reaction evidence identifying this enzyme with EC 1.1.1.122 is absent from the input.",
    "reason": "Choosing the exact four-digit EC number requires item-specific functional information; recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The input does not provide enough evidence to justify any exact EC option, but that lack of discrimination alone does not establish that another listed option is correct."
  },
  "important_caveats": [
    "The reviewer-only sequence match establishes applicability of the cited database record, not that the evaluated model had access to that identity or annotation.",
    "The EC assignment is supported by transferred annotation; direct experimental validation for this exact mouse protein is not established by the supplied evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 273-aa sequence matches UniProt entry E9Q3D4 (DHB14_MOUSE, Hydroxysteroid 17-beta dehydrogenase 14) exactly. The UniProt annotation assigns EC 1.1.1.122 (L-fucose dehydrogenase) with catalytic activities for L-fucose, D-arabinose, and L-galactose oxidation. However, all annotations carry evidence code ECO:0000250 (inferred by similarity to Q9BPX1, the human ortholog), not direct experimental evidence for this mouse protein. The key is supported as the database annotation for this exact sequence, though it is computational inference by homology rather than experimentally verified activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal Rossmann-fold motif (VVVTGGSRGIGAAIVRAF, a GxGxxG pattern) and the overall ~273-aa short-chain dehydrogenase/reductase (SDR) architecture allow reasoning to EC class 1 (oxidoreductase), which eliminates C (2.3.1.319, a transferase) and D (4.1.1.128, a lyase). However, both remaining choices A (1.1.1.195) and B (1.1.1.122) are NAD⁺-dependent dehydrogenases acting on the CH-OH group (EC 1.1.1.x). Distinguishing the specific 4-digit number requires knowing the exact substrate (L-fucose for 122 vs. whatever substrate 195 acts on), which is a protein-specific fact not derivable from general fold-level sequence features.


**Missing item-specific fact**

> The specific substrate-binding-site residues or the exact protein identity (E9Q3D4 / HSD17B14) that determine whether the enzyme acts on L-fucose (EC 1.1.1.122) versus the substrate of EC 1.1.1.195. The sequence alone does not reveal which of two closely related EC 1.1.1.x dehydrogenases this is without database lookup or memorization of this particular protein's annotation.


**Reason**

> General biological reasoning (Rossmann fold → oxidoreductase) narrows four choices to two, but the final 4-digit EC number (122 vs 195) depends on a protein-specific annotation inferred by homology in UniProt, not on a feature discernible from the raw sequence by general biochemical logic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (1.1.1.195) and B (1.1.1.122) fall within EC 1.1.1 (oxidoreductases acting on the CH-OH group of donors with NAD⁺ as acceptor), consistent with the Rossmann-fold SDR architecture visible in the sequence. Without the specific substrate-binding-site information or the UniProt annotation, a solver cannot definitively exclude 1.1.1.195 on sequence grounds alone. C and D are clearly eliminable by fold reasoning, but A vs. B is not.


### Important caveats

- The UniProt annotation for E9Q3D4 (EC 1.1.1.122) is entirely inferred by similarity (ECO:0000250) from the human ortholog Q9BPX1; no direct experimental activity data for the mouse protein is cited in the retrieved evidence.
- The protein's gene name (Hsd17b14, Hydroxysteroid 17-beta dehydrogenase 14) might mislead a solver toward a hydroxysteroid dehydrogenase EC number (e.g., 1.1.1.51), which is not among the choices, adding a naming-vs-function mismatch that complicates reasoning-based approaches.
- The identity of EC 1.1.1.195 was not independently verified; if it is an obsolete or very obscure entry, the A-vs-B distinction may be easier than assumed, but this cannot be confirmed from the supplied evidence.
- All reviewer evidence is current-snapshot or historical-archived UniProt data; the author's exact source snapshot and annotation state at question-construction time are unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal Rossmann-fold motif (VVVTGGSRGIGAAIVRAF, a GxGxxG pattern) and the overall ~273-aa short-chain dehydrogenase/reductase (SDR) architecture allow reasoning to EC class 1 (oxidoreductase), which eliminates C (2.3.1.319, a transferase) and D (4.1.1.128, a lyase). However, both remaining choices A (1.1.1.195) and B (1.1.1.122) are NAD⁺-dependent dehydrogenases acting on the CH-OH group (EC 1.1.1.x). Distinguishing the specific 4-digit number requires knowing the exact substrate (L-fucose for 122 vs. whatever substrate 195 acts on), which is a protein-specific fact not derivable from general fold-level sequence features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate-binding-site residues or the exact protein identity (E9Q3D4 / HSD17B14) that determine whether the enzyme acts on L-fucose (EC 1.1.1.122) versus the substrate of EC 1.1.1.195. The sequence alone does not reveal which of two closely related EC 1.1.1.x dehydrogenases this is without database lookup or memorization of this particular protein's annotation.",
    "reason": "General biological reasoning (Rossmann fold → oxidoreductase) narrows four choices to two, but the final 4-digit EC number (122 vs 195) depends on a protein-specific annotation inferred by homology in UniProt, not on a feature discernible from the raw sequence by general biochemical logic."
  },
  "case_id": "EC_number_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied 273-aa sequence matches UniProt entry E9Q3D4 (DHB14_MOUSE, Hydroxysteroid 17-beta dehydrogenase 14) exactly. The UniProt annotation assigns EC 1.1.1.122 (L-fucose dehydrogenase) with catalytic activities for L-fucose, D-arabinose, and L-galactose oxidation. However, all annotations carry evidence code ECO:0000250 (inferred by similarity to Q9BPX1, the human ortholog), not direct experimental evidence for this mouse protein. The key is supported as the database annotation for this exact sequence, though it is computational inference by homology rather than experimentally verified activity."
  },
  "important_caveats": [
    "The UniProt annotation for E9Q3D4 (EC 1.1.1.122) is entirely inferred by similarity (ECO:0000250) from the human ortholog Q9BPX1; no direct experimental activity data for the mouse protein is cited in the retrieved evidence.",
    "The protein's gene name (Hsd17b14, Hydroxysteroid 17-beta dehydrogenase 14) might mislead a solver toward a hydroxysteroid dehydrogenase EC number (e.g., 1.1.1.51), which is not among the choices, adding a naming-vs-function mismatch that complicates reasoning-based approaches.",
    "The identity of EC 1.1.1.195 was not independently verified; if it is an obsolete or very obscure entry, the A-vs-B distinction may be easier than assumed, but this cannot be confirmed from the supplied evidence.",
    "All reviewer evidence is current-snapshot or historical-archived UniProt data; the author's exact source snapshot and annotation state at question-construction time are unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (1.1.1.195) and B (1.1.1.122) fall within EC 1.1.1 (oxidoreductases acting on the CH-OH group of donors with NAD⁺ as acceptor), consistent with the Rossmann-fold SDR architecture visible in the sequence. Without the specific substrate-binding-site information or the UniProt annotation, a solver cannot definitively exclude 1.1.1.195 on sequence grounds alone. C and D are clearly eliminable by fold reasoning, but A vs. B is not."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 273-aa sequence matches UniProt entry E9Q3D4 (DHB14_MOUSE, Hydroxysteroid 17-beta dehydrogenase 14) exactly. The UniProt annotation assigns EC 1.1.1.122 (L-fucose dehydrogenase) with catalytic activities for L-fucose, D-arabinose, and L-galactose oxidation. However, all annotations carry evidence code ECO:0000250 (inferred by similarity to Q9BPX1, the human ortholog), not direct experimental evidence for this mouse protein. The key is supported as the database annotation for this exact sequence, though it is computational inference by homology rather than experimentally verified activity.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal Rossmann-fold motif (VVVTGGSRGIGAAIVRAF, a GxGxxG pattern) and the overall ~273-aa short-chain dehydrogenase/reductase (SDR) architecture allow reasoning to EC class 1 (oxidoreductase), which eliminates C (2.3.1.319, a transferase) and D (4.1.1.128, a lyase). However, both remaining choices A (1.1.1.195) and B (1.1.1.122) are NAD⁺-dependent dehydrogenases acting on the CH-OH group (EC 1.1.1.x). Distinguishing the specific 4-digit number requires knowing the exact substrate (L-fucose for 122 vs. whatever substrate 195 acts on), which is a protein-specific fact not derivable from general fold-level sequence features.",
    "missing_item_specific_fact": "The specific substrate-binding-site residues or the exact protein identity (E9Q3D4 / HSD17B14) that determine whether the enzyme acts on L-fucose (EC 1.1.1.122) versus the substrate of EC 1.1.1.195. The sequence alone does not reveal which of two closely related EC 1.1.1.x dehydrogenases this is without database lookup or memorization of this particular protein's annotation.",
    "reason": "General biological reasoning (Rossmann fold → oxidoreductase) narrows four choices to two, but the final 4-digit EC number (122 vs 195) depends on a protein-specific annotation inferred by homology in UniProt, not on a feature discernible from the raw sequence by general biochemical logic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (1.1.1.195) and B (1.1.1.122) fall within EC 1.1.1 (oxidoreductases acting on the CH-OH group of donors with NAD⁺ as acceptor), consistent with the Rossmann-fold SDR architecture visible in the sequence. Without the specific substrate-binding-site information or the UniProt annotation, a solver cannot definitively exclude 1.1.1.195 on sequence grounds alone. C and D are clearly eliminable by fold reasoning, but A vs. B is not."
  },
  "important_caveats": [
    "The UniProt annotation for E9Q3D4 (EC 1.1.1.122) is entirely inferred by similarity (ECO:0000250) from the human ortholog Q9BPX1; no direct experimental activity data for the mouse protein is cited in the retrieved evidence.",
    "The protein's gene name (Hsd17b14, Hydroxysteroid 17-beta dehydrogenase 14) might mislead a solver toward a hydroxysteroid dehydrogenase EC number (e.g., 1.1.1.51), which is not among the choices, adding a naming-vs-function mismatch that complicates reasoning-based approaches.",
    "The identity of EC 1.1.1.195 was not independently verified; if it is an obsolete or very obscure entry, the A-vs-B distinction may be easier than assumed, but this cannot be confirmed from the supplied evidence.",
    "All reviewer evidence is current-snapshot or historical-archived UniProt data; the author's exact source snapshot and annotation state at question-construction time are unknown."
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

**Accession:** `E9Q3D4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 95. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
"E9Q3D4"
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Hydroxysteroid 17-beta dehydrogenase 14"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"value":"1.1.1.122"}],"fullName":{"value":"L-fucose dehydrogenase"}}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81516"}}],"reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"name":"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81515"},{"database":"ChEBI","id":"CHEBI:2181"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:81457"}]}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"name":"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81519"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:46994"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:194242"}]}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"name":"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81523"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:37619"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:182410"}]}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:17.926007+00:00.  

```text
ID   DHB14_MOUSE             Reviewed;         273 AA.
AC   E9Q3D4;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-APR-2011, sequence version 1.
DT   28-JAN-2026, entry version 95.
DE   RecName: Full=L-fucose dehydrogenase;
DE            EC=1.1.1.122 {ECO:0000250|UniProtKB:Q9BPX1};
DE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;
GN   Name=Hsd17b14 {ECO:0000312|MGI:MGI:1913315}; Synonyms=Dhrs10, retSDR3;
OS   Mus musculus (Mouse).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Mus; Mus.
OX   NCBI_TaxID=10090;
```

Source SHA-256: `e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:17.926007+00:00.  

```text
DE   RecName: Full=L-fucose dehydrogenase;
DE            EC=1.1.1.122 {ECO:0000250|UniProtKB:Q9BPX1};
DE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;
```

Source SHA-256: `e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:17.926007+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);
CC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;
CC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;
CC         Evidence={ECO:0000250|UniProtKB:Q9BPX1};
```

Source SHA-256: `e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)  
**Locator:** `lines 41-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:17.926007+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+);
CC         Xref=Rhea:RHEA:81519, ChEBI:CHEBI:15378, ChEBI:CHEBI:46994,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:194242;
CC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};
```

Source SHA-256: `e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)  
**Locator:** `lines 46-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:17.926007+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+);
CC         Xref=Rhea:RHEA:81523, ChEBI:CHEBI:15378, ChEBI:CHEBI:37619,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:182410;
CC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};
```

Source SHA-256: `e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 92. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
