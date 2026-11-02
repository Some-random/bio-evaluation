# transmembrane_0129

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 406..426; 574..594; 653..673; 678..698; 761..781; 791..811

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQPPTRAPFFPFSLLRGRKARETCTCRSVASTEGPNTFGPRARPGCHAHQVAPSKESFHSSAFQLVSASRLSPLMSSCFVSFLRYPSFRPSAPFSAPPSSSTVPISTPSDFSHSAPASWRCVPTAPSALHAPFSFTTQAAHLSSCVFDGCSRLPCSEPGSPQTLQRALATTSATAFLRTACMSHRLRRRPDAWTSGCSGQTDNATASPCVRPLLRPPVDTASRAAANDKDAPQPTCFWRNARTSRAVHRNQTDMNFSSFSCSLRPCRHTLAKAAGHHAPLSRHSLQSLPESRIRGGTVSRGDSPGSLTLSPRNMSSDAMPVHPLYFPSAVPFSTTSGSNSSTFSCPSPSSSTSSTSSTSSTSSTSSTSSTSSTSSTSSTSSTSSPFLLSRSHSVDCRACPVSRAPPNPTSLQLLFSLFPFLWPTALKDRLRVLGSVACLVTAKVLTIQAPLLLANLVDAFQVLPHNSPLSPSGASPSSGDTSLLASSGETSSSLSPSAAPAEGAREAGKSGESAGRERRDEGSTVRLSPLAEGPASPATEERTAAGKAGTSVGGRDAGAVHALDTEHLRNTAQIVSVPLGVVCGFPVARIAATGFNELRSTLFTRVSQNASCDFSCHAFLHLHALALFHDKRAGELSVLISRGMKSVTALLNVLLFQMVPTALEFALVLYLLGSKVGGPVACITSLTMAVYVAFTAAVTARRTKIRKEMIAAEQQSVGLLVDSLANAEAVRFFTAEKGELSRFEAVQRRYAEKHVSVNQSLAFLNFGQQLIFNVGVLGSLAYTASQVAAGLLPVGHIVLVSSLLLQLAVPLNFVGTIYRETSLNLADLEKLYELMNHHPPIVNPPDARPFVLKGGAVAFENVRFAYPPSPLRPGSLPSKTGDDEKPEASRMLLDDVSFSVDAGKKVAIVGPSGVGKSTLIKLLFRMFDPASGTVRIDDQDVKELDLHSFRRQIGVVPQDMVLFNDTIEFNIKYGCPSATDEEMRAAAKQAEIDDVIMRMPQGYSTVVGERGLKLSGGERQRIGIARCLLRNPAIAVFDEATSALDSHTEQKILKAFRAMARGRTTLVIAHRLSTISDADKIIYLKEGKIAEMGTHAELLEKERGLYRALWESQQHQEQEEAVSTPDLTLS

[Multiple Choices]
A. 406..426; 574..594; 653..673; 678..698; 761..781; 791..811
B. 406..426; 574..594; 653..673; 678..698; 761..781
C. 406..426; 574..595; 653..673; 678..698; 761..781; 791..811
D. 65..85; 137..157; 158..178; 187..207; 216..236; 250..270; 334..354; 367..387; 392..412; 423..443; 455..475; 489..509
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The exact sequence matches UniProt entry S8EXU2, whose annotated transmembrane regions are the six intervals listed in A. These annotations are computational (ECO:0000255), not evidence of direct experimental measurement.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains hydrophobic stretches consistent with membrane-spanning helices, and the ABC-transporter context makes multiple transmembrane helices plausible. This can support broad region identification but does not determine exact residue boundaries.


**Missing item-specific fact**

> The protein-specific annotated boundaries, especially whether the 574-region ends at residue 594 or 595, are not supplied. The supporting database annotations are computational rather than experimental.


**Reason**

> The sequence permits general hydropathy-based inference, but distinguishing the nearly identical coordinate sets requires protein-specific boundary information unavailable in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A and C differ only by one residue at the end of the 574-region. Both identify the same plausible membrane-spanning segment biologically, although the matching UniProt annotation specifies 574..594.


### Important caveats

- Reviewer-only database evidence supports the key but was not provided to the evaluated model.
- The source annotations identify predicted helical transmembrane regions; they do not establish experimentally measured boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hydrophobic stretches consistent with membrane-spanning helices, and the ABC-transporter context makes multiple transmembrane helices plausible. This can support broad region identification but does not determine exact residue boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotated boundaries, especially whether the 574-region ends at residue 594 or 595, are not supplied. The supporting database annotations are computational rather than experimental.",
    "reason": "The sequence permits general hydropathy-based inference, but distinguishing the nearly identical coordinate sets requires protein-specific boundary information unavailable in the question."
  },
  "case_id": "transmembrane_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry S8EXU2, whose annotated transmembrane regions are the six intervals listed in A. These annotations are computational (ECO:0000255), not evidence of direct experimental measurement."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not provided to the evaluated model.",
    "The source annotations identify predicted helical transmembrane regions; they do not establish experimentally measured boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A and C differ only by one residue at the end of the 574-region. Both identify the same plausible membrane-spanning segment biologically, although the matching UniProt annotation specifies 574..594."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry S8EXU2, whose annotated transmembrane regions are the six intervals listed in A. These annotations are computational (ECO:0000255), not evidence of direct experimental measurement.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "C8", "C9", "C10", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains hydrophobic stretches consistent with membrane-spanning helices, and the ABC-transporter context makes multiple transmembrane helices plausible. This can support broad region identification but does not determine exact residue boundaries.",
    "missing_item_specific_fact": "The protein-specific annotated boundaries, especially whether the 574-region ends at residue 594 or 595, are not supplied. The supporting database annotations are computational rather than experimental.",
    "reason": "The sequence permits general hydropathy-based inference, but distinguishing the nearly identical coordinate sets requires protein-specific boundary information unavailable in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A and C differ only by one residue at the end of the 574-region. Both identify the same plausible membrane-spanning segment biologically, although the matching UniProt annotation specifies 574..594."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not provided to the evaluated model.",
    "The source annotations identify predicted helical transmembrane regions; they do not establish experimentally measured boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry S8EXU2 (ATM1_TOXGM, Toxoplasma gondii ABC transporter ATM1) annotates exactly six transmembrane helical regions at 406-426, 574-594, 653-673, 678-698, 761-781, and 791-811, matching Choice A precisely. The sequence SHA256 matches the benchmark input. Evidence codes are ECO:0000255 (inferred from sequence/structural similarity) and PROSITE-ProRule PRU00441, indicating computational/predictive annotation rather than experimental determination, but the annotation is consistent and complete for this entry.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical ABC transporter motifs: a Walker A motif (GPSGVGKST around ~880) and an ABC signature motif (LILKEGKIAEMGTHAELLEKERGLYRALWESQ around ~990). ABC transporters have a well-known architecture of six transmembrane helices (three per nucleotide-binding domain half). This eliminates Choice D (12 TM regions, incompatible with ABC architecture) and Choice B (only 5 TM regions, one short of the expected six). The A-vs-C distinction (574-594 vs 574-595) hinges on the identity of residue 595; if it is a charged lysine (as the sequence context '…VTARRTK…' suggests), a charged residue is incompatible with the hydrophobic core of a lipid bilayer-spanning helix, favoring the 594 endpoint. This is a valid hydrophobicity/boundary argument grounded in membrane biology.


**Missing item-specific fact**

> None strictly required. The ABC-transporter motif recognition and the charged-residue-at-boundary argument are general biological reasoning. However, the single-residue boundary (594 vs 595) is at the limit of precision achievable from sequence alone without a dedicated TM predictor, making it the weakest link in the reasoning chain.


**Reason**

> The primary discrimination (6 TM helices for an ABC transporter, eliminating B and D) rests on recognizing conserved ABC motifs in the sequence and applying general knowledge of ABC-transporter topology. The secondary discrimination (A vs C) relies on the biological principle that a charged lysine cannot stably reside within the hydrophobic core of a transmembrane helix. Both are defensible general biological arguments rather than item-specific database lookups.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the ABC-transporter architecture (6 TM helices), Choice D (12 helices) and Choice B (5 helices) are clearly excluded. The A-vs-C distinction is resolvable by the charged-residue argument at position 595. No two choices are equally defensible under standard membrane-biology reasoning.


### Important caveats

- All UniProt transmembrane annotations for this entry carry ECO:0000255 (inferred from sequence or structural similarity) and/or PROSITE-ProRule evidence; none are experimental. The 'correct' boundaries are computational predictions, not experimentally validated.
- The 594-vs-595 boundary distinction is extremely fine-grained. While the charged-residue argument is biologically valid, in practice TM-helix boundary prediction tools routinely disagree by 1–3 residues, so this is the most fragile part of the reasoning chain.
- The UniProt accession S8EXU2 and its metadata were reviewer-only and absent from the evaluated model input; the model must infer the protein identity from sequence motifs alone.
- The entry was first public on 2025-04-09; the author's source snapshot date is unknown, though the sequence has been stable since 2013-10-16 (sequence version 1).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical ABC transporter motifs: a Walker A motif (GPSGVGKST around ~880) and an ABC signature motif (LILKEGKIAEMGTHAELLEKERGLYRALWESQ around ~990). ABC transporters have a well-known architecture of six transmembrane helices (three per nucleotide-binding domain half). This eliminates Choice D (12 TM regions, incompatible with ABC architecture) and Choice B (only 5 TM regions, one short of the expected six). The A-vs-C distinction (574-594 vs 574-595) hinges on the identity of residue 595; if it is a charged lysine (as the sequence context '…VTARRTK…' suggests), a charged residue is incompatible with the hydrophobic core of a lipid bilayer-spanning helix, favoring the 594 endpoint. This is a valid hydrophobicity/boundary argument grounded in membrane biology.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The ABC-transporter motif recognition and the charged-residue-at-boundary argument are general biological reasoning. However, the single-residue boundary (594 vs 595) is at the limit of precision achievable from sequence alone without a dedicated TM predictor, making it the weakest link in the reasoning chain.",
    "reason": "The primary discrimination (6 TM helices for an ABC transporter, eliminating B and D) rests on recognizing conserved ABC motifs in the sequence and applying general knowledge of ABC-transporter topology. The secondary discrimination (A vs C) relies on the biological principle that a charged lysine cannot stably reside within the hydrophobic core of a transmembrane helix. Both are defensible general biological arguments rather than item-specific database lookups."
  },
  "case_id": "transmembrane_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry S8EXU2 (ATM1_TOXGM, Toxoplasma gondii ABC transporter ATM1) annotates exactly six transmembrane helical regions at 406-426, 574-594, 653-673, 678-698, 761-781, and 791-811, matching Choice A precisely. The sequence SHA256 matches the benchmark input. Evidence codes are ECO:0000255 (inferred from sequence/structural similarity) and PROSITE-ProRule PRU00441, indicating computational/predictive annotation rather than experimental determination, but the annotation is consistent and complete for this entry."
  },
  "important_caveats": [
    "All UniProt transmembrane annotations for this entry carry ECO:0000255 (inferred from sequence or structural similarity) and/or PROSITE-ProRule evidence; none are experimental. The 'correct' boundaries are computational predictions, not experimentally validated.",
    "The 594-vs-595 boundary distinction is extremely fine-grained. While the charged-residue argument is biologically valid, in practice TM-helix boundary prediction tools routinely disagree by 1–3 residues, so this is the most fragile part of the reasoning chain.",
    "The UniProt accession S8EXU2 and its metadata were reviewer-only and absent from the evaluated model input; the model must infer the protein identity from sequence motifs alone.",
    "The entry was first public on 2025-04-09; the author's source snapshot date is unknown, though the sequence has been stable since 2013-10-16 (sequence version 1)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the ABC-transporter architecture (6 TM helices), Choice D (12 helices) and Choice B (5 helices) are clearly excluded. The A-vs-C distinction is resolvable by the charged-residue argument at position 595. No two choices are equally defensible under standard membrane-biology reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry S8EXU2 (ATM1_TOXGM, Toxoplasma gondii ABC transporter ATM1) annotates exactly six transmembrane helical regions at 406-426, 574-594, 653-673, 678-698, 761-781, and 791-811, matching Choice A precisely. The sequence SHA256 matches the benchmark input. Evidence codes are ECO:0000255 (inferred from sequence/structural similarity) and PROSITE-ProRule PRU00441, indicating computational/predictive annotation rather than experimental determination, but the annotation is consistent and complete for this entry.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical ABC transporter motifs: a Walker A motif (GPSGVGKST around ~880) and an ABC signature motif (LILKEGKIAEMGTHAELLEKERGLYRALWESQ around ~990). ABC transporters have a well-known architecture of six transmembrane helices (three per nucleotide-binding domain half). This eliminates Choice D (12 TM regions, incompatible with ABC architecture) and Choice B (only 5 TM regions, one short of the expected six). The A-vs-C distinction (574-594 vs 574-595) hinges on the identity of residue 595; if it is a charged lysine (as the sequence context '…VTARRTK…' suggests), a charged residue is incompatible with the hydrophobic core of a lipid bilayer-spanning helix, favoring the 594 endpoint. This is a valid hydrophobicity/boundary argument grounded in membrane biology.",
    "missing_item_specific_fact": "None strictly required. The ABC-transporter motif recognition and the charged-residue-at-boundary argument are general biological reasoning. However, the single-residue boundary (594 vs 595) is at the limit of precision achievable from sequence alone without a dedicated TM predictor, making it the weakest link in the reasoning chain.",
    "reason": "The primary discrimination (6 TM helices for an ABC transporter, eliminating B and D) rests on recognizing conserved ABC motifs in the sequence and applying general knowledge of ABC-transporter topology. The secondary discrimination (A vs C) relies on the biological principle that a charged lysine cannot stably reside within the hydrophobic core of a transmembrane helix. Both are defensible general biological arguments rather than item-specific database lookups."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the ABC-transporter architecture (6 TM helices), Choice D (12 helices) and Choice B (5 helices) are clearly excluded. The A-vs-C distinction is resolvable by the charged-residue argument at position 595. No two choices are equally defensible under standard membrane-biology reasoning."
  },
  "important_caveats": [
    "All UniProt transmembrane annotations for this entry carry ECO:0000255 (inferred from sequence or structural similarity) and/or PROSITE-ProRule evidence; none are experimental. The 'correct' boundaries are computational predictions, not experimentally validated.",
    "The 594-vs-595 boundary distinction is extremely fine-grained. While the charged-residue argument is biologically valid, in practice TM-helix boundary prediction tools routinely disagree by 1–3 residues, so this is the most fragile part of the reasoning chain.",
    "The UniProt accession S8EXU2 and its metadata were reviewer-only and absent from the evaluated model input; the model must infer the protein identity from sequence motifs alone.",
    "The entry was first public on 2025-04-09; the author's source snapshot date is unknown, though the sequence has been stable since 2013-10-16 (sequence version 1)."
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

**Accession:** `S8EXU2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 59. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
"S8EXU2"
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":426},"start":{"modifier":"EXACT","value":406}},"type":"Transmembrane"}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":594},"start":{"modifier":"EXACT","value":574}},"type":"Transmembrane"}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":673},"start":{"modifier":"EXACT","value":653}},"type":"Transmembrane"}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":698},"start":{"modifier":"EXACT","value":678}},"type":"Transmembrane"}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":781},"start":{"modifier":"EXACT","value":761}},"type":"Transmembrane"}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":811},"start":{"modifier":"EXACT","value":791}},"type":"Transmembrane"}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)  
**Locator:** `lines 118-120`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:34:03.453043+00:00.  

```text
FT   TRANSMEM        406..426
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)  
**Locator:** `lines 121-123`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:34:03.453043+00:00.  

```text
FT   TRANSMEM        574..594
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)  
**Locator:** `lines 124-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:34:03.453043+00:00.  

```text
FT   TRANSMEM        653..673
FT                   /note="Helical"
FT                   /evidence="ECO:0000255, ECO:0000255|PROSITE-
FT                   ProRule:PRU00441"
```

Source SHA-256: `04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)  
**Locator:** `lines 128-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:34:03.453043+00:00.  

```text
FT   TRANSMEM        678..698
FT                   /note="Helical"
FT                   /evidence="ECO:0000255, ECO:0000255|PROSITE-
FT                   ProRule:PRU00441"
```

Source SHA-256: `04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)  
**Locator:** `lines 132-135`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:34:03.453043+00:00.  

```text
FT   TRANSMEM        761..781
FT                   /note="Helical"
FT                   /evidence="ECO:0000255, ECO:0000255|PROSITE-
FT                   ProRule:PRU00441"
```

Source SHA-256: `04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)  
**Locator:** `lines 136-139`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:34:03.453043+00:00.  

```text
FT   TRANSMEM        791..811
FT                   /note="Helical"
FT                   /evidence="ECO:0000255, ECO:0000255|PROSITE-
FT                   ProRule:PRU00441"
```

Source SHA-256: `04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
