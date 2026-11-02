# GO_molecular_function_0039

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — D-threo-aldose 1-dehydrogenase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAAVTRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRALEQELSGTVFIPGDVTQERDLQTLVSETLSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEVNLLGTYTLIKLALPHLRKSRGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRHGVRVNCISPGNIWTPLWEELAASTSDPRATILEGTLAQPLGRMGQPAEVAAAAVFLASEATFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH

[Multiple Choices]
A. D-threo-aldose 1-dehydrogenase activity
B. UDP-N-acetylglucosamine 2-epimerase activity
C. tau protein binding
D. type 1 parathyroid hormone receptor binding
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the mouse UniProt entry, which annotates L-fucose dehydrogenase, EC 1.1.1.122, and describes NAD+-dependent oxidation of L-fucose. GO:0047834 names the corresponding D-threo-aldose 1-dehydrogenase activity, supporting choice A. The functional annotation is transferred by similarity rather than presented as direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a nucleotide-binding-like motif consistent with an oxidoreductase, but that general clue does not establish its specific substrate or distinguish the listed activities reliably.


**Missing item-specific fact**

> The protein-specific functional assignment that this sequence is an L-fucose/D-threo-aldose dehydrogenase, supported here by an annotation transferred from a homolog.


**Reason**

> Choosing A over the other options requires the specific enzyme-function assignment, which is not supplied in the question. Inferring a broad enzyme class from sequence features would not establish the precise molecular function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence's functional annotation supports A; the other choices describe different activities. The supplied evidence does not suggest another listed option is comparably supported.


### Important caveats

- The UniProt functional and GO annotations cite similarity-based evidence (ECO:0000250 and ISS), not direct experimental validation of this mouse sequence in the provided evidence.
- The historical and current records match the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a nucleotide-binding-like motif consistent with an oxidoreductase, but that general clue does not establish its specific substrate or distinguish the listed activities reliably.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment that this sequence is an L-fucose/D-threo-aldose dehydrogenase, supported here by an annotation transferred from a homolog.",
    "reason": "Choosing A over the other options requires the specific enzyme-function assignment, which is not supplied in the question. Inferring a broad enzyme class from sequence features would not establish the precise molecular function."
  },
  "case_id": "GO_molecular_function_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C9",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mouse UniProt entry, which annotates L-fucose dehydrogenase, EC 1.1.1.122, and describes NAD+-dependent oxidation of L-fucose. GO:0047834 names the corresponding D-threo-aldose 1-dehydrogenase activity, supporting choice A. The functional annotation is transferred by similarity rather than presented as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The UniProt functional and GO annotations cite similarity-based evidence (ECO:0000250 and ISS), not direct experimental validation of this mouse sequence in the provided evidence.",
    "The historical and current records match the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's functional annotation supports A; the other choices describe different activities. The supplied evidence does not suggest another listed option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mouse UniProt entry, which annotates L-fucose dehydrogenase, EC 1.1.1.122, and describes NAD+-dependent oxidation of L-fucose. GO:0047834 names the corresponding D-threo-aldose 1-dehydrogenase activity, supporting choice A. The functional annotation is transferred by similarity rather than presented as direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C9", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a nucleotide-binding-like motif consistent with an oxidoreductase, but that general clue does not establish its specific substrate or distinguish the listed activities reliably.",
    "missing_item_specific_fact": "The protein-specific functional assignment that this sequence is an L-fucose/D-threo-aldose dehydrogenase, supported here by an annotation transferred from a homolog.",
    "reason": "Choosing A over the other options requires the specific enzyme-function assignment, which is not supplied in the question. Inferring a broad enzyme class from sequence features would not establish the precise molecular function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's functional annotation supports A; the other choices describe different activities. The supplied evidence does not suggest another listed option is comparably supported."
  },
  "important_caveats": [
    "The UniProt functional and GO annotations cite similarity-based evidence (ECO:0000250 and ISS), not direct experimental validation of this mouse sequence in the provided evidence.",
    "The historical and current records match the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt E9Q3D4 (DHB14_MOUSE, mouse L-fucose dehydrogenase / HSD17B14) is annotated with GO:0047834 (D-threo-aldose 1-dehydrogenase activity, EC 1.1.1.122). The GO term definition matches the protein's catalytic activity (NAD+-dependent oxidation of D-threo-aldoses including L-fucose, D-arabinose, L-galactose). The evidence code is ISS:UniProtKB (sequence similarity to human Q9BPX1), so this is computational inference rather than direct experimental characterization of the mouse protein, but the annotation is present and consistent with the EC assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD-binding motif (VVVVTGGSRGIGAAIVRAF, i.e. GxGxxG pattern) and is 273 amino acids long with an SDR (short-chain dehydrogenase/reductase) architecture. This identifies the protein as an NAD-dependent oxidoreductase. Among the four choices, only A (D-threo-aldose 1-dehydrogenase activity, EC 1.1.1.122) is a dehydrogenase/oxidoreductase. Option B (UDP-GlcNAc 2-epimerase, GNE) is a ~700-aa protein with a completely different domain architecture; options C and D are protein/receptor binding activities requiring no catalytic cofactor-binding motifs. A biologist recognizing the Rossmann fold and SDR-like length can eliminate B, C, and D without database lookup.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides identifiable structural motifs (Rossmann fold) and family-level architecture (273-aa SDR) that are sufficient to classify the protein as an NAD-dependent dehydrogenase. Since only one option among the four is a dehydrogenase activity, the functional class can be determined by general enzymology knowledge without needing to memorize the specific UniProt annotation for E9Q3D4.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D represent fundamentally different functional classes (epimerase, cytoskeletal protein binding, receptor binding) that are incompatible with the visible Rossmann-fold/NAD-binding architecture and SDR-like length of the sequence. Only option A is consistent with a dehydrogenase.


### Important caveats

- The GO annotation for this protein is ISS (Inferred from Sequence Similarity to human Q9BPX1), not direct experimental evidence on the mouse protein itself.
- The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot date is unknown.
- The sequence is 273 aa and matches the canonical UniProt entry exactly (SHA-256 confirmed).
- The reasoning path relies on recognizing the Rossmann fold and SDR family architecture, which is standard structural biology knowledge but still requires pattern recognition from the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD-binding motif (VVVVTGGSRGIGAAIVRAF, i.e. GxGxxG pattern) and is 273 amino acids long with an SDR (short-chain dehydrogenase/reductase) architecture. This identifies the protein as an NAD-dependent oxidoreductase. Among the four choices, only A (D-threo-aldose 1-dehydrogenase activity, EC 1.1.1.122) is a dehydrogenase/oxidoreductase. Option B (UDP-GlcNAc 2-epimerase, GNE) is a ~700-aa protein with a completely different domain architecture; options C and D are protein/receptor binding activities requiring no catalytic cofactor-binding motifs. A biologist recognizing the Rossmann fold and SDR-like length can eliminate B, C, and D without database lookup.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides identifiable structural motifs (Rossmann fold) and family-level architecture (273-aa SDR) that are sufficient to classify the protein as an NAD-dependent dehydrogenase. Since only one option among the four is a dehydrogenase activity, the functional class can be determined by general enzymology knowledge without needing to memorize the specific UniProt annotation for E9Q3D4."
  },
  "case_id": "GO_molecular_function_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt E9Q3D4 (DHB14_MOUSE, mouse L-fucose dehydrogenase / HSD17B14) is annotated with GO:0047834 (D-threo-aldose 1-dehydrogenase activity, EC 1.1.1.122). The GO term definition matches the protein's catalytic activity (NAD+-dependent oxidation of D-threo-aldoses including L-fucose, D-arabinose, L-galactose). The evidence code is ISS:UniProtKB (sequence similarity to human Q9BPX1), so this is computational inference rather than direct experimental characterization of the mouse protein, but the annotation is present and consistent with the EC assignment."
  },
  "important_caveats": [
    "The GO annotation for this protein is ISS (Inferred from Sequence Similarity to human Q9BPX1), not direct experimental evidence on the mouse protein itself.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot date is unknown.",
    "The sequence is 273 aa and matches the canonical UniProt entry exactly (SHA-256 confirmed).",
    "The reasoning path relies on recognizing the Rossmann fold and SDR family architecture, which is standard structural biology knowledge but still requires pattern recognition from the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D represent fundamentally different functional classes (epimerase, cytoskeletal protein binding, receptor binding) that are incompatible with the visible Rossmann-fold/NAD-binding architecture and SDR-like length of the sequence. Only option A is consistent with a dehydrogenase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt E9Q3D4 (DHB14_MOUSE, mouse L-fucose dehydrogenase / HSD17B14) is annotated with GO:0047834 (D-threo-aldose 1-dehydrogenase activity, EC 1.1.1.122). The GO term definition matches the protein's catalytic activity (NAD+-dependent oxidation of D-threo-aldoses including L-fucose, D-arabinose, L-galactose). The evidence code is ISS:UniProtKB (sequence similarity to human Q9BPX1), so this is computational inference rather than direct experimental characterization of the mouse protein, but the annotation is present and consistent with the EC assignment.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "H1", "H2", "H3", "H4", "H5", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD-binding motif (VVVVTGGSRGIGAAIVRAF, i.e. GxGxxG pattern) and is 273 amino acids long with an SDR (short-chain dehydrogenase/reductase) architecture. This identifies the protein as an NAD-dependent oxidoreductase. Among the four choices, only A (D-threo-aldose 1-dehydrogenase activity, EC 1.1.1.122) is a dehydrogenase/oxidoreductase. Option B (UDP-GlcNAc 2-epimerase, GNE) is a ~700-aa protein with a completely different domain architecture; options C and D are protein/receptor binding activities requiring no catalytic cofactor-binding motifs. A biologist recognizing the Rossmann fold and SDR-like length can eliminate B, C, and D without database lookup.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides identifiable structural motifs (Rossmann fold) and family-level architecture (273-aa SDR) that are sufficient to classify the protein as an NAD-dependent dehydrogenase. Since only one option among the four is a dehydrogenase activity, the functional class can be determined by general enzymology knowledge without needing to memorize the specific UniProt annotation for E9Q3D4."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D represent fundamentally different functional classes (epimerase, cytoskeletal protein binding, receptor binding) that are incompatible with the visible Rossmann-fold/NAD-binding architecture and SDR-like length of the sequence. Only option A is consistent with a dehydrogenase."
  },
  "important_caveats": [
    "The GO annotation for this protein is ISS (Inferred from Sequence Similarity to human Q9BPX1), not direct experimental evidence on the mouse protein itself.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot date is unknown.",
    "The sequence is 273 aa and matches the canonical UniProt entry exactly (SHA-256 confirmed).",
    "The reasoning path relies on recognizing the Rossmann fold and SDR family architecture, which is standard structural biology knowledge but still requires pattern recognition from the raw sequence."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"value":"Catalyzes the NAD(+)-dependent oxidation of L-fucose, yielding L-fucono-1,5-lactone, which rapidly converts spontaneously to L-fucone-1,4-lactone. Can also act on D-arabinose and L-galactose, with lower catalytic efficiency. Does not use NADPH. May be the initial enzyme of the putative L-fucose degradation pathway in mammals"}]}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81516"}}],"reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"name":"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81515"},{"database":"ChEBI","id":"CHEBI:2181"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:81457"}]}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"name":"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81519"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:46994"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:194242"}]}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BPX1","source":"UniProtKB"}],"name":"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81523"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:37619"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:182410"}]}}
```

Source SHA-256: `bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)  
**Locator:** `/uniProtKBCrossReferences/37`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:08.225634+00:00.  

```json
{"database":"GO","id":"GO:0047834","properties":[{"key":"GoTerm","value":"F:D-threo-aldose 1-dehydrogenase activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
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
**Locator:** `lines 28-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:17.926007+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the NAD(+)-dependent oxidation of L-fucose,
CC       yielding L-fucono-1,5-lactone, which rapidly converts spontaneously to
CC       L-fucone-1,4-lactone. Can also act on D-arabinose and L-galactose, with
CC       lower catalytic efficiency. Does not use NADPH. May be the initial
CC       enzyme of the putative L-fucose degradation pathway in mammals.
CC       {ECO:0000250|UniProtKB:Q9BPX1}.
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

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)  
**Locator:** `lines 102-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:17.926007+00:00.  

```text
DR   GO; GO:0047834; F:D-threo-aldose 1-dehydrogenase activity; ISS:UniProtKB.
```

Source SHA-256: `e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 296916-296938`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0047834
name: D-threo-aldose 1-dehydrogenase activity
namespace: molecular_function
def: "Catalysis of the reaction: a D-threo-aldose + NAD+ = a D-threo-aldono-1,5-lactone + NADH." [EC:1.1.1.122, MetaCyc:D-THREO-ALDOSE-1-DEHYDROGENASE-RXN]
synonym: "(2S,3R)-aldose dehydrogenase activity" RELATED [EC:1.1.1.122]
synonym: "D-threo-aldose:NAD+ 1-oxidoreductase activity" RELATED [EC:1.1.1.122]
synonym: "dehydrogenase, L-fucose" RELATED [EC:1.1.1.122]
synonym: "L-fucose (D-arabinose) dehydrogenase activity" RELATED [EC:1.1.1.122]
synonym: "L-fucose dehydrogenase activity" RELATED [EC:1.1.1.122]
xref: EC:1.1.1.122
xref: MetaCyc:D-THREO-ALDOSE-1-DEHYDROGENASE-RXN
xref: RHEA:19645
xref: RHEA:81515
xref: RHEA:81519
xref: RHEA:81523
is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
property_value: skos:exactMatch EC:1.1.1.122
property_value: skos:exactMatch RHEA:19645
property_value: skos:narrowMatch RHEA:81515
property_value: skos:narrowMatch RHEA:81519
property_value: skos:narrowMatch RHEA:81523

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 39. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
