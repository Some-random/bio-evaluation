# transmembrane_0103: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0103.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **C** — 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MGKEQKEKKDGNLSIKEEVEKELNKKSTAELFRKIKNEKISFFLPFKCLPAQHRKLLFISFVCAVLSGGTLPFFISVFGVILKNMNLGDDINPIILSLVSIGLVQFILSMISSYCMDVITSKILKTLKLEYLRSVFYQDGQFHDNNPGSKLRSDLDFYLEQVSSGIGTKFITIFTYASSFLGLYIWSLIKNARLTLCITCVFPLIYVCGVICNKKVKLNKKTSLLYNNNTMSIIEEALMGIRTVASYCGEKTILNKFNLSETFYSKYILKANFVEALHIGLINGLILVSYAFGFWYGTRIIINSATNQYPNNDFNGASVISILLGVLISMFMLTIILPNITEYMKALEATNSLYEIINRKPLVENNDDGETLPNIKKIEFKNVRFHYDTRKDVEIYKDLSFTLKEGKTYAFVGESGCGKSTILKLIERLYDPTEGDIIVNDSHNLKDINLKWWRSKIGVVSQDPLLFSNSIKNNIKYSLYSLKDLEAMENYYEENTNDTYENKNFSLISNSMTSNELLEMKKEYQTIKDSDVVDVSKKVLIHDFVSSLPDKYDTLVGSNASKLSGGQKQRISIARAIMRNPKILILDEATSSLDNKSEYLVQKTINNLKGNENRITIIIAHRLSTIRYANTIFVLSNRERSDNNNNNNNDDNNNNNNNNNNKINNEGSYIIEQGTHDSLMKNKNGIYHLMINNQKISSNKSSNNGNDNGSDNKSSAYKDSDTGNDADNMNSLSIHENENISNNRNCKNTAENEKEEKVPFFKRMFRRKKKAPNNLRIIYKEIFSYKKDVTIIFFSILVAGGLYPVFALLYARYVSTLFDFANLEYNSNKYSIYILLIAIAMFISETLKNYYNNKIGEKVEKTMKRRLFENILYQEMSFFDQDKNTPGVLSAHINRDVHLLKTGLVNNIVIFSHFIMLFLVSMVMSFYFCPIVAAVLTFIYFINMRVFAVRARLTKSKEIEKKENMSSGVFAFSSDDEMFKDPSFLIQEAFYNMHTVINYGLEDYFCNLIEKAIDYKNKGQKRRIIVNAALWGFSQSAQLFINSFAYWFGSFLIKRGTILVDDFMKSLFTFIFTGSYAGKLMSLKGDSENAKLSFEKYYPLMIRKSNIDVRDDGGIRINKNLIKGKVDIKDVNFRYISRPNVPIYKNLSFTCDSKKTTAIVGETGSGKSTFMNLLLRFYDLKNDHIILKNDMTNFQDYQNNNNNSLVLKNVNEFSNQSGSAEDYTVFNNNGEILLDDINICDYNLRDLRNLFSIVSQEPMLFNMSIYENIKFGREDATLEDVKRVSKFAAIDEFIESLPNKYDTNVGPYGKSLSGGQKQRIAIARALLREPKILLLDEATSSLDSNSEKLIEKTIVDIKDKADKTIITIAHRIASIKRSDKIVVFNNPDRNGTFVQSHGTHDELLSAQDGIYKKYVKLAK

[Multiple Choices]
A. 3..23
B. 61..81; 91..111; 169..189; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
C. 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
D. 61..81; 91..111; 169..189; 192..212; 276..296; 318..338; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates the transmembrane regions listed in C, including 192..212 and 317..337. These annotations are computational (PROSITE-ProRule), not independent experimental confirmation of every boundary.

Citations as saved: [C1](#evidence-c1), [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general pattern of regions in the choices and argues against A. That pattern does not reliably distinguish the one-residue boundary shift in D from C.


**Missing item-specific fact**

> The protein-specific transmembrane annotations or equivalent structure/topology evidence specifying the segment boundaries, especially the 317..337 versus 318..338 choice.


**Reason**

> Sequence hydrophobicity supports broad helix locations, but the choices ask for precise boundaries and differ in ways that general biological reasoning cannot settle reliably.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> C and D differ only by shifting the 317..337 segment by one residue; the supplied sequence alone does not establish that exact boundary distinction.


### Important caveats

- The reviewer-only records match the supplied sequence, but their accession and annotations were not provided in the question.
- The cited UniProt transmembrane features are computationally supported annotations, not direct experimental evidence for each exact endpoint.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general pattern of regions in the choices and argues against A. That pattern does not reliably distinguish the one-residue boundary shift in D from C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane annotations or equivalent structure/topology evidence specifying the segment boundaries, especially the 317..337 versus 318..338 choice.",
    "reason": "Sequence hydrophobicity supports broad helix locations, but the choices ask for precise boundaries and differ in ways that general biological reasoning cannot settle reliably."
  },
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C23",
      "C25",
      "C27"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the transmembrane regions listed in C, including 192..212 and 317..337. These annotations are computational (PROSITE-ProRule), not independent experimental confirmation of every boundary."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but their accession and annotations were not provided in the question.",
    "The cited UniProt transmembrane features are computationally supported annotations, not direct experimental evidence for each exact endpoint."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "C and D differ only by shifting the 317..337 segment by one residue; the supplied sequence alone does not establish that exact boundary distinction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the transmembrane regions listed in C, including 192..212 and 317..337. These annotations are computational (PROSITE-ProRule), not independent experimental confirmation of every boundary.",
    "evidence_ids": ["C1", "C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C23", "C25", "C27"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general pattern of regions in the choices and argues against A. That pattern does not reliably distinguish the one-residue boundary shift in D from C.",
    "missing_item_specific_fact": "The protein-specific transmembrane annotations or equivalent structure/topology evidence specifying the segment boundaries, especially the 317..337 versus 318..338 choice.",
    "reason": "Sequence hydrophobicity supports broad helix locations, but the choices ask for precise boundaries and differ in ways that general biological reasoning cannot settle reliably."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "C and D differ only by shifting the 317..337 segment by one residue; the supplied sequence alone does not establish that exact boundary distinction."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but their accession and annotations were not provided in the question.",
    "The cited UniProt transmembrane features are computationally supported annotations, not direct experimental evidence for each exact endpoint."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> Choice C lists 12 transmembrane segments (61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078) that exactly match the UniProt Q7K6A5 annotation for PfMDR1. All 12 TM boundaries are confirmed by PROSITE-ProRule pattern annotations (ECO:0000255) in both the current entry (v161) and the historical entry (v159). The sequence is confirmed as a 1419-residue match. The protein has also been structurally characterized by cryo-EM (PDB 8JVH etc., 2023), providing structural corroboration of the overall TM topology, though the specific residue boundaries in UniProt derive from PROSITE pattern matching rather than direct structural assignment.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H23](#evidence-h23), [H25](#evidence-h25), [H27](#evidence-h27), [C31](#evidence-c31), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The B-vs-C distinction (missing TM 192..212) has partial reasoning support: ABC transporters like PfMDR1 canonically contain 6 TMs per nucleotide-binding domain (12 total), so recognizing only 5 TMs in the N-terminal half (as in B) would be inconsistent with the expected ABC transporter fold. The 2-residue vacuolar loop between TMs 3 and 4 (190-191) is unusual but occurs in ABC transporters. However, the critical C-vs-D distinction (317..337 vs 318..338) is a single-residue boundary shift that cannot be resolved by general biological reasoning.


**Missing item-specific fact**

> The exact hydrophobic boundary of the 6th TM helix—specifically whether residue 317 or 318 is the first residue of the transmembrane segment. Both 317..337 and 318..338 are 21-residue helices of identical length. Distinguishing them requires the specific PROSITE-ProRule annotation boundary or the output of a particular TM prediction algorithm applied to this exact sequence. No general biological principle (hydrophobic thickness, helix length, topology) resolves a one-residue boundary shift.


**Reason**

> While the B-vs-C difference (presence of TM 192..212) can be partially reasoned from ABC transporter topology (6 TMs per half), the decisive C-vs-D distinction is a single-residue boundary shift (317 vs 318 start). This is an item-specific annotation boundary that requires either memorizing the UniProt entry or running a specific prediction tool. General knowledge of hydrophobic helix properties, membrane thickness, or ABC transporter architecture cannot distinguish a 21-residue helix starting at position 317 from one starting at 318.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The only difference between C and D is the 6th TM boundary (317..337 vs 318..338). Without access to the specific PROSITE-ProRule annotation or a defined TM prediction algorithm, a model examining hydrophobicity profiles could reasonably assign the boundary to either position. Both options describe a 21-residue helical segment in a plausible hydrophobic region. The question does not specify which prediction method defines the boundaries.


### Important caveats

- All TM annotations in UniProt Q7K6A5 are computational (ECO:0000255, PROSITE-ProRule:PRU00441), not experimentally determined. The 2023 cryo-EM structure (8JVH) covers residues 38-1419 and could in principle validate TM boundaries, but the UniProt annotation still cites PROSITE patterns.
- The identity of the protein (Q7K6A5, PfMDR1) was inferred from reviewer-only metadata absent from the model input; the model sees only the raw sequence.
- Choice A (3..23) is an obvious distractor targeting the N-terminal region and is trivially eliminable.
- The system prompt asks to identify 'a segment' (singular) but all substantive choices list 11-12 segments; this wording mismatch is a minor imperfection that does not affect answerability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The B-vs-C distinction (missing TM 192..212) has partial reasoning support: ABC transporters like PfMDR1 canonically contain 6 TMs per nucleotide-binding domain (12 total), so recognizing only 5 TMs in the N-terminal half (as in B) would be inconsistent with the expected ABC transporter fold. The 2-residue vacuolar loop between TMs 3 and 4 (190-191) is unusual but occurs in ABC transporters. However, the critical C-vs-D distinction (317..337 vs 318..338) is a single-residue boundary shift that cannot be resolved by general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact hydrophobic boundary of the 6th TM helix—specifically whether residue 317 or 318 is the first residue of the transmembrane segment. Both 317..337 and 318..338 are 21-residue helices of identical length. Distinguishing them requires the specific PROSITE-ProRule annotation boundary or the output of a particular TM prediction algorithm applied to this exact sequence. No general biological principle (hydrophobic thickness, helix length, topology) resolves a one-residue boundary shift.",
    "reason": "While the B-vs-C difference (presence of TM 192..212) can be partially reasoned from ABC transporter topology (6 TMs per half), the decisive C-vs-D distinction is a single-residue boundary shift (317 vs 318 start). This is an item-specific annotation boundary that requires either memorizing the UniProt entry or running a specific prediction tool. General knowledge of hydrophobic helix properties, membrane thickness, or ABC transporter architecture cannot distinguish a 21-residue helix starting at position 317 from one starting at 318."
  },
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C23",
      "C25",
      "C27",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H23",
      "H25",
      "H27",
      "C31",
      "H4"
    ],
    "judgment": "supported",
    "reason": "Choice C lists 12 transmembrane segments (61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078) that exactly match the UniProt Q7K6A5 annotation for PfMDR1. All 12 TM boundaries are confirmed by PROSITE-ProRule pattern annotations (ECO:0000255) in both the current entry (v161) and the historical entry (v159). The sequence is confirmed as a 1419-residue match. The protein has also been structurally characterized by cryo-EM (PDB 8JVH etc., 2023), providing structural corroboration of the overall TM topology, though the specific residue boundaries in UniProt derive from PROSITE pattern matching rather than direct structural assignment."
  },
  "important_caveats": [
    "All TM annotations in UniProt Q7K6A5 are computational (ECO:0000255, PROSITE-ProRule:PRU00441), not experimentally determined. The 2023 cryo-EM structure (8JVH) covers residues 38-1419 and could in principle validate TM boundaries, but the UniProt annotation still cites PROSITE patterns.",
    "The identity of the protein (Q7K6A5, PfMDR1) was inferred from reviewer-only metadata absent from the model input; the model sees only the raw sequence.",
    "Choice A (3..23) is an obvious distractor targeting the N-terminal region and is trivially eliminable.",
    "The system prompt asks to identify 'a segment' (singular) but all substantive choices list 11-12 segments; this wording mismatch is a minor imperfection that does not affect answerability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The only difference between C and D is the 6th TM boundary (317..337 vs 318..338). Without access to the specific PROSITE-ProRule annotation or a defined TM prediction algorithm, a model examining hydrophobicity profiles could reasonably assign the boundary to either position. Both options describe a 21-residue helical segment in a plausible hydrophobic region. The question does not specify which prediction method defines the boundaries."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice C lists 12 transmembrane segments (61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078) that exactly match the UniProt Q7K6A5 annotation for PfMDR1. All 12 TM boundaries are confirmed by PROSITE-ProRule pattern annotations (ECO:0000255) in both the current entry (v161) and the historical entry (v159). The sequence is confirmed as a 1419-residue match. The protein has also been structurally characterized by cryo-EM (PDB 8JVH etc., 2023), providing structural corroboration of the overall TM topology, though the specific residue boundaries in UniProt derive from PROSITE pattern matching rather than direct structural assignment.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C23", "C25", "C27", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H23", "H25", "H27", "C31", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The B-vs-C distinction (missing TM 192..212) has partial reasoning support: ABC transporters like PfMDR1 canonically contain 6 TMs per nucleotide-binding domain (12 total), so recognizing only 5 TMs in the N-terminal half (as in B) would be inconsistent with the expected ABC transporter fold. The 2-residue vacuolar loop between TMs 3 and 4 (190-191) is unusual but occurs in ABC transporters. However, the critical C-vs-D distinction (317..337 vs 318..338) is a single-residue boundary shift that cannot be resolved by general biological reasoning.",
    "missing_item_specific_fact": "The exact hydrophobic boundary of the 6th TM helix—specifically whether residue 317 or 318 is the first residue of the transmembrane segment. Both 317..337 and 318..338 are 21-residue helices of identical length. Distinguishing them requires the specific PROSITE-ProRule annotation boundary or the output of a particular TM prediction algorithm applied to this exact sequence. No general biological principle (hydrophobic thickness, helix length, topology) resolves a one-residue boundary shift.",
    "reason": "While the B-vs-C difference (presence of TM 192..212) can be partially reasoned from ABC transporter topology (6 TMs per half), the decisive C-vs-D distinction is a single-residue boundary shift (317 vs 318 start). This is an item-specific annotation boundary that requires either memorizing the UniProt entry or running a specific prediction tool. General knowledge of hydrophobic helix properties, membrane thickness, or ABC transporter architecture cannot distinguish a 21-residue helix starting at position 317 from one starting at 318."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The only difference between C and D is the 6th TM boundary (317..337 vs 318..338). Without access to the specific PROSITE-ProRule annotation or a defined TM prediction algorithm, a model examining hydrophobicity profiles could reasonably assign the boundary to either position. Both options describe a 21-residue helical segment in a plausible hydrophobic region. The question does not specify which prediction method defines the boundaries."
  },
  "important_caveats": [
    "All TM annotations in UniProt Q7K6A5 are computational (ECO:0000255, PROSITE-ProRule:PRU00441), not experimentally determined. The 2023 cryo-EM structure (8JVH) covers residues 38-1419 and could in principle validate TM boundaries, but the UniProt annotation still cites PROSITE patterns.",
    "The identity of the protein (Q7K6A5, PfMDR1) was inferred from reviewer-only metadata absent from the model input; the model sees only the raw sequence.",
    "Choice A (3..23) is an obvious distractor targeting the N-terminal region and is trivially eliminable.",
    "The system prompt asks to identify 'a segment' (singular) but all substantive choices list 11-12 segments; this wording mismatch is a minor imperfection that does not affect answerability."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched UniProt entry annotates the transmembrane intervals listed in C, including 192..212 and 317..337. These are principally computational PROSITE-ProRule annotations, so they support the keyed coordinates as database annotations but are not, by themselves, experimental validation of every boundary.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has repeated hydrophobic stretches consistent with the multi-pass membrane domains of an ABC transporter, separated by long soluble regions containing nucleotide-binding motifs. In particular, the strongly hydrophobic stretch around 192..212 supports C over B, which omits it. Around 317..337, the sequence is hydrophobic, whereas the next residue is polar, favoring C's boundary over D's one-residue-shifted endpoint. These sequence patterns provide a transferable basis for selecting C, although they do not establish every boundary with experimental precision.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of ABC-transporter architecture and hydropathy patterns distinguishes the main candidate sets and gives a sequence-based reason to prefer C over the near-duplicate D. Exact helix boundaries remain less certain than the broad transmembrane regions.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> C and D differ only by shifting one helix by one residue. Both intervals cover essentially the same hydrophobic membrane-spanning segment, so the wording does not make clear that this boundary-level distinction is biologically decisive.


### Important caveats

- The supporting database coordinates are computational annotations; the supplied reviewer evidence does not establish experimental validation of each endpoint.
- The sequence supports membrane-spanning helices, but predicted boundaries can vary by a residue.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with the multi-pass membrane domains of an ABC transporter, separated by long soluble regions containing nucleotide-binding motifs. In particular, the strongly hydrophobic stretch around 192..212 supports C over B, which omits it. Around 317..337, the sequence is hydrophobic, whereas the next residue is polar, favoring C's boundary over D's one-residue-shifted endpoint. These sequence patterns provide a transferable basis for selecting C, although they do not establish every boundary with experimental precision.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of ABC-transporter architecture and hydropathy patterns distinguishes the main candidate sets and gives a sequence-based reason to prefer C over the near-duplicate D. Exact helix boundaries remain less certain than the broad transmembrane regions."
  },
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C23",
      "C25",
      "C27"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates the transmembrane intervals listed in C, including 192..212 and 317..337. These are principally computational PROSITE-ProRule annotations, so they support the keyed coordinates as database annotations but are not, by themselves, experimental validation of every boundary."
  },
  "important_caveats": [
    "The supporting database coordinates are computational annotations; the supplied reviewer evidence does not establish experimental validation of each endpoint.",
    "The sequence supports membrane-spanning helices, but predicted boundaries can vary by a residue."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "C and D differ only by shifting one helix by one residue. Both intervals cover essentially the same hydrophobic membrane-spanning segment, so the wording does not make clear that this boundary-level distinction is biologically decisive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates the transmembrane intervals listed in C, including 192..212 and 317..337. These are principally computational PROSITE-ProRule annotations, so they support the keyed coordinates as database annotations but are not, by themselves, experimental validation of every boundary.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C23", "C25", "C27"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with the multi-pass membrane domains of an ABC transporter, separated by long soluble regions containing nucleotide-binding motifs. In particular, the strongly hydrophobic stretch around 192..212 supports C over B, which omits it. Around 317..337, the sequence is hydrophobic, whereas the next residue is polar, favoring C's boundary over D's one-residue-shifted endpoint. These sequence patterns provide a transferable basis for selecting C, although they do not establish every boundary with experimental precision.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of ABC-transporter architecture and hydropathy patterns distinguishes the main candidate sets and gives a sequence-based reason to prefer C over the near-duplicate D. Exact helix boundaries remain less certain than the broad transmembrane regions."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "C and D differ only by shifting one helix by one residue. Both intervals cover essentially the same hydrophobic membrane-spanning segment, so the wording does not make clear that this boundary-level distinction is biologically decisive."
  },
  "important_caveats": [
    "The supporting database coordinates are computational annotations; the supplied reviewer evidence does not establish experimental validation of each endpoint.",
    "The sequence supports membrane-spanning helices, but predicted boundaries can vary by a residue."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q7K6A5 (PfMDR1) lists exactly 12 transmembrane helices at 61..81, 91..111, 169..189, 192..212, 276..296, 317..337, 789..809, 830..850, 908..928, 929..949, 1033..1053, 1058..1078, matching option C precisely. All TM annotations carry evidence code ECO:0000255 (PROSITE-ProRule PRU00441), indicating computational/profiling annotation rather than direct experimental determination.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical ABC transporter motifs (Walker A: GESGCGKST at ~positions 380-390 and 1190-1200; ABC signature: LSGGQ at ~positions 455-460 and 1265-1270), identifying this as a P-glycoprotein/ABC transporter family member. ABC transporters have a canonical 6+6 TM topology (12 TM helices total, six per nucleotide-binding domain half). Option B lists only 11 TM regions (5 in the first half, missing 192..212), violating the canonical fold. Option A (a single 21-residue N-terminal segment) is incompatible with a multi-pass membrane transporter. For C vs D, the 6th TM boundary differs by one residue: C has 317..337, D has 318..338. Examining the sequence at these positions, residue 317 is A (hydrophobic), 318 is S (polar), 337 is L (hydrophobic), and 338 is P (helix-breaking). A TM helix should begin and end with hydrophobic residues and avoid a proline at the C-terminal boundary, favoring 317..337 (option C) over 318..338 (option D).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The ABC transporter family topology (6+6 TM) is well-established transferable knowledge that eliminates B. Hydrophobicity boundary analysis (A at 317 vs S at 318; L at 337 vs P at 338) provides a sequence-based argument favoring C over D. Option A is eliminated by the multi-pass membrane protein context. The reasoning chain uses family-level biology and standard hydrophobicity principles without requiring the exact database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While C vs D differs by only one residue at a TM boundary, the hydrophobicity argument (A/S at the N-terminus of the helix, L/P at the C-terminus) provides a reasonable sequence-based distinction. B is eliminated by the canonical 12-TM ABC transporter topology. No two options are equally defensible given the available evidence.


### Important caveats

- All TM annotations in the source are computational (PROSITE-ProRule PRU00441, ECO:0000255), not experimentally determined by crystallography or cryo-EM at single-residue resolution for each helix boundary.
- The C vs D distinction (1-residue shift at the 6th TM boundary) is within the typical uncertainty of hydrophobicity-based TM prediction; the argument relies on identifying a polar (S) and helix-breaking (P) residue at the proposed D boundaries.
- The 2023 cryo-EM structures (PDB 8JVH etc.) resolve the full protein but the UniProt TM boundaries are still annotated via PROSITE-ProRule profiling, not directly from the structure.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical ABC transporter motifs (Walker A: GESGCGKST at ~positions 380-390 and 1190-1200; ABC signature: LSGGQ at ~positions 455-460 and 1265-1270), identifying this as a P-glycoprotein/ABC transporter family member. ABC transporters have a canonical 6+6 TM topology (12 TM helices total, six per nucleotide-binding domain half). Option B lists only 11 TM regions (5 in the first half, missing 192..212), violating the canonical fold. Option A (a single 21-residue N-terminal segment) is incompatible with a multi-pass membrane transporter. For C vs D, the 6th TM boundary differs by one residue: C has 317..337, D has 318..338. Examining the sequence at these positions, residue 317 is A (hydrophobic), 318 is S (polar), 337 is L (hydrophobic), and 338 is P (helix-breaking). A TM helix should begin and end with hydrophobic residues and avoid a proline at the C-terminal boundary, favoring 317..337 (option C) over 318..338 (option D).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The ABC transporter family topology (6+6 TM) is well-established transferable knowledge that eliminates B. Hydrophobicity boundary analysis (A at 317 vs S at 318; L at 337 vs P at 338) provides a sequence-based argument favoring C over D. Option A is eliminated by the multi-pass membrane protein context. The reasoning chain uses family-level biology and standard hydrophobicity principles without requiring the exact database annotation."
  },
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C23",
      "C25",
      "C27"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q7K6A5 (PfMDR1) lists exactly 12 transmembrane helices at 61..81, 91..111, 169..189, 192..212, 276..296, 317..337, 789..809, 830..850, 908..928, 929..949, 1033..1053, 1058..1078, matching option C precisely. All TM annotations carry evidence code ECO:0000255 (PROSITE-ProRule PRU00441), indicating computational/profiling annotation rather than direct experimental determination."
  },
  "important_caveats": [
    "All TM annotations in the source are computational (PROSITE-ProRule PRU00441, ECO:0000255), not experimentally determined by crystallography or cryo-EM at single-residue resolution for each helix boundary.",
    "The C vs D distinction (1-residue shift at the 6th TM boundary) is within the typical uncertainty of hydrophobicity-based TM prediction; the argument relies on identifying a polar (S) and helix-breaking (P) residue at the proposed D boundaries.",
    "The 2023 cryo-EM structures (PDB 8JVH etc.) resolve the full protein but the UniProt TM boundaries are still annotated via PROSITE-ProRule profiling, not directly from the structure."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While C vs D differs by only one residue at a TM boundary, the hydrophobicity argument (A/S at the N-terminus of the helix, L/P at the C-terminus) provides a reasonable sequence-based distinction. B is eliminated by the canonical 12-TM ABC transporter topology. No two options are equally defensible given the available evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q7K6A5 (PfMDR1) lists exactly 12 transmembrane helices at 61..81, 91..111, 169..189, 192..212, 276..296, 317..337, 789..809, 830..850, 908..928, 929..949, 1033..1053, 1058..1078, matching option C precisely. All TM annotations carry evidence code ECO:0000255 (PROSITE-ProRule PRU00441), indicating computational/profiling annotation rather than direct experimental determination.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C23", "C25", "C27"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical ABC transporter motifs (Walker A: GESGCGKST at ~positions 380-390 and 1190-1200; ABC signature: LSGGQ at ~positions 455-460 and 1265-1270), identifying this as a P-glycoprotein/ABC transporter family member. ABC transporters have a canonical 6+6 TM topology (12 TM helices total, six per nucleotide-binding domain half). Option B lists only 11 TM regions (5 in the first half, missing 192..212), violating the canonical fold. Option A (a single 21-residue N-terminal segment) is incompatible with a multi-pass membrane transporter. For C vs D, the 6th TM boundary differs by one residue: C has 317..337, D has 318..338. Examining the sequence at these positions, residue 317 is A (hydrophobic), 318 is S (polar), 337 is L (hydrophobic), and 338 is P (helix-breaking). A TM helix should begin and end with hydrophobic residues and avoid a proline at the C-terminal boundary, favoring 317..337 (option C) over 318..338 (option D).",
    "missing_item_specific_fact": "",
    "reason": "The ABC transporter family topology (6+6 TM) is well-established transferable knowledge that eliminates B. Hydrophobicity boundary analysis (A at 317 vs S at 318; L at 337 vs P at 338) provides a sequence-based argument favoring C over D. Option A is eliminated by the multi-pass membrane protein context. The reasoning chain uses family-level biology and standard hydrophobicity principles without requiring the exact database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While C vs D differs by only one residue at a TM boundary, the hydrophobicity argument (A/S at the N-terminus of the helix, L/P at the C-terminus) provides a reasonable sequence-based distinction. B is eliminated by the canonical 12-TM ABC transporter topology. No two options are equally defensible given the available evidence."
  },
  "important_caveats": [
    "All TM annotations in the source are computational (PROSITE-ProRule PRU00441, ECO:0000255), not experimentally determined by crystallography or cryo-EM at single-residue resolution for each helix boundary.",
    "The C vs D distinction (1-residue shift at the 6th TM boundary) is within the typical uncertainty of hydrophobicity-based TM prediction; the argument relies on identifying a polar (S) and helix-breaking (P) residue at the proposed D boundaries.",
    "The 2023 cryo-EM structures (PDB 8JVH etc.) resolve the full protein but the UniProt TM boundaries are still annotated via PROSITE-ProRule profiling, not directly from the structure."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `boundary_alternative_not_independently_validated`.

> Cited PROSITE-ProRule Transmembrane features match keyC including317..337; optionD shifts that one interval to318..338.

**Remaining uncertainty:** The specific shift is present in the options. The source supports the keyed predicted interval, not experimental equivalence of the alternative boundaries.

Evidence checked: [C1](#evidence-c1), [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27).

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q7K6A5",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "814492b7a3ffcadbd0dde392964e9ba403451c8c63dbc1231fa05df226af501f",
  "benchmark_sequence_length": 1419,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 161,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "current_source_sequence_sha256": "814492b7a3ffcadbd0dde392964e9ba403451c8c63dbc1231fa05df226af501f",
  "current_source_sequence_length": 1419,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 159,
  "selected_historical_version": {
    "accession": "Q7K6A5",
    "database": "Swiss-Prot",
    "entryVersion": 159,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MDR_PLAF7",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "selected_historical_source_sequence_sha256": "814492b7a3ffcadbd0dde392964e9ba403451c8c63dbc1231fa05df226af501f",
  "selected_historical_source_sequence_length": 1419,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 159,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q7K6A5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":161,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"1674943\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"8097560\",\"source\":\"PubMed\"}],\"value\":\"P-glycoprotein homolog\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"1674943\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"8097560\",\"source\":\"PubMed\"}],\"value\":\"PGH1\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37527341\",\"source\":\"PubMed\"}],\"value\":\"7.6.2.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"1674943\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37527341\",\"source\":\"PubMed\"}],\"value\":\"Multidrug resistance protein 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"1674943\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37527341\",\"source\":\"PubMed\"}],\"value\":\"PfMDR1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":60},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":81},\"start\":{\"modifier\":\"EXACT\",\"value\":61}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":90},\"start\":{\"modifier\":\"EXACT\",\"value\":82}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":111},\"start\":{\"modifier\":\"EXACT\",\"value\":91}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":168},\"start\":{\"modifier\":\"EXACT\",\"value\":112}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":189},\"start\":{\"modifier\":\"EXACT\",\"value\":169}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":191},\"start\":{\"modifier\":\"EXACT\",\"value\":190}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":212},\"start\":{\"modifier\":\"EXACT\",\"value\":192}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":275},\"start\":{\"modifier\":\"EXACT\",\"value\":213}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":296},\"start\":{\"modifier\":\"EXACT\",\"value\":276}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":316},\"start\":{\"modifier\":\"EXACT\",\"value\":297}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":337},\"start\":{\"modifier\":\"EXACT\",\"value\":317}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":788},\"start\":{\"modifier\":\"EXACT\",\"value\":338}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":809},\"start\":{\"modifier\":\"EXACT\",\"value\":789}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":829},\"start\":{\"modifier\":\"EXACT\",\"value\":810}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":850},\"start\":{\"modifier\":\"EXACT\",\"value\":830}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C21",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/17",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":907},\"start\":{\"modifier\":\"EXACT\",\"value\":851}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C22",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":928},\"start\":{\"modifier\":\"EXACT\",\"value\":908}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C23",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/19",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":949},\"start\":{\"modifier\":\"EXACT\",\"value\":929}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C24",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/20",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1032},\"start\":{\"modifier\":\"EXACT\",\"value\":950}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C25",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/21",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1053},\"start\":{\"modifier\":\"EXACT\",\"value\":1033}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C26",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/22",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1057},\"start\":{\"modifier\":\"EXACT\",\"value\":1054}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C27",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/23",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1078},\"start\":{\"modifier\":\"EXACT\",\"value\":1058}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C28",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/features/24",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1419},\"start\":{\"modifier\":\"EXACT\",\"value\":1079}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C29",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Cowman A.F.\",\"Karcz S.\",\"Galatis D.\",\"Culvenor J.G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"1674943\"},{\"database\":\"DOI\",\"id\":\"10.1083/jcb.113.5.1033\"}],\"citationType\":\"journal article\",\"firstPage\":\"1033\",\"id\":\"1674943\",\"journal\":\"J. Cell Biol.\",\"lastPage\":\"1042\",\"publicationDate\":\"1991\",\"title\":\"A P-glycoprotein homologue of Plasmodium falciparum is localized on the digestive vacuole.\",\"volume\":\"113\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C30

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C30",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Karcz S.R.\",\"Galatis D.\",\"Cowman A.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"8097560\"},{\"database\":\"DOI\",\"id\":\"10.1016/0166-6851(93)90048-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"269\",\"id\":\"8097560\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"276\",\"publicationDate\":\"1993\",\"title\":\"Nucleotide binding properties of a P-glycoprotein homologue from Plasmodium falciparum.\",\"volume\":\"58\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C31

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)

```json
{
  "evidence_id": "C31",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q7K6A5.json",
  "source_sha256": "c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409",
  "retrieved_utc": "2026-11-02T04:31:50.920847+00:00",
  "json_pointer": "/references/5",
  "excerpt": "{\"citation\":{\"authors\":[\"Si K.\",\"He X.\",\"Chen L.\",\"Zhang A.\",\"Guo C.\",\"Li M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37527341\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.2219905120\"}],\"citationType\":\"journal article\",\"firstPage\":\"e2219905120\",\"id\":\"37527341\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"e2219905120\",\"publicationDate\":\"2023\",\"title\":\"The structure of <i>Plasmodium falciparum</i> multidrug resistance protein 1 reveals an N-terminal regulatory domain.\",\"volume\":\"120\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8JVH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8JW4\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8JWF\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8JWG\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8JWI\",\"source\":\"PDB\"}],\"referenceNumber\":6,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (2.94 ANGSTROMS) OF 38-1419 IN COMPLEX WITH ATP; MAGNESIUM ION AND MEFLOQUINE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"R DOMAIN\",\"MUTAGENESIS OF 1-MET--ASN-37; ASN-86; TYR-184; THR-199; LYS-217; LYS-220; LYS-221; PHE-331; GLU-588; SER-1034; ASN-1042; ASP-1246 AND GLU-1337\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   MDR_PLAF7               Reviewed;        1419 AA.\nAC   Q7K6A5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 159.\nDE   RecName: Full=Multidrug resistance protein 1 {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:37527341};\nDE            Short=PfMDR1 {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:37527341};\nDE            EC=7.6.2.2 {ECO:0000269|PubMed:37527341};\nDE   AltName: Full=P-glycoprotein homolog {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:8097560};\nDE            Short=PGH1 {ECO:0000303|PubMed:1674943, ECO:0000303|PubMed:8097560};\nGN   ORFNames=PF3D7_0523000 {ECO:0000312|EMBL:CAD51594.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 50-56",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   SUBCELLULAR LOCATION, AND DEVELOPMENTAL STAGE.\nRX   PubMed=1674943; DOI=10.1083/jcb.113.5.1033;\nRA   Cowman A.F., Karcz S., Galatis D., Culvenor J.G.;\nRT   \"A P-glycoprotein homologue of Plasmodium falciparum is localized on the\nRT   digestive vacuole.\";\nRL   J. Cell Biol. 113:1033-1042(1991).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 57-63",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   SUBCELLULAR LOCATION.\nRX   PubMed=8097560; DOI=10.1016/0166-6851(93)90048-3;\nRA   Karcz S.R., Galatis D., Cowman A.F.;\nRT   \"Nucleotide binding properties of a P-glycoprotein homologue from\nRT   Plasmodium falciparum.\";\nRL   Mol. Biochem. Parasitol. 58:269-276(1993).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 72-82",
  "excerpt": "RN   [6] {ECO:0007744|PDB:8JVH, ECO:0007744|PDB:8JW4, ECO:0007744|PDB:8JWF, ECO:0007744|PDB:8JWG, ECO:0007744|PDB:8JWI}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (2.94 ANGSTROMS) OF 38-1419 IN COMPLEX\nRP   WITH ATP; MAGNESIUM ION AND MEFLOQUINE, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, R DOMAIN, AND MUTAGENESIS OF 1-MET--ASN-37;\nRP   ASN-86; TYR-184; THR-199; LYS-217; LYS-220; LYS-221; PHE-331; GLU-588;\nRP   SER-1034; ASN-1042; ASP-1246 AND GLU-1337.\nRX   PubMed=37527341; DOI=10.1073/pnas.2219905120;\nRA   Si K., He X., Chen L., Zhang A., Guo C., Li M.;\nRT   \"The structure of <i>Plasmodium falciparum</i> multidrug resistance protein\nRT   1 reveals an N-terminal regulatory domain.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 120:e2219905120-e2219905120(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 219-221",
  "excerpt": "FT   TOPO_DOM        1..60\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 222-224",
  "excerpt": "FT   TRANSMEM        61..81\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 225-227",
  "excerpt": "FT   TOPO_DOM        82..90\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 228-230",
  "excerpt": "FT   TRANSMEM        91..111\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 231-233",
  "excerpt": "FT   TOPO_DOM        112..168\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 234-236",
  "excerpt": "FT   TRANSMEM        169..189\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 237-239",
  "excerpt": "FT   TOPO_DOM        190..191\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 240-242",
  "excerpt": "FT   TRANSMEM        192..212\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 243-245",
  "excerpt": "FT   TOPO_DOM        213..275\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 246-248",
  "excerpt": "FT   TRANSMEM        276..296\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 249-251",
  "excerpt": "FT   TOPO_DOM        297..316\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 252-254",
  "excerpt": "FT   TRANSMEM        317..337\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 255-257",
  "excerpt": "FT   TOPO_DOM        338..788\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 258-260",
  "excerpt": "FT   TRANSMEM        789..809\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H19",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 261-263",
  "excerpt": "FT   TOPO_DOM        810..829\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H20",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 264-266",
  "excerpt": "FT   TRANSMEM        830..850\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H21",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 267-269",
  "excerpt": "FT   TOPO_DOM        851..907\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H22",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 270-272",
  "excerpt": "FT   TRANSMEM        908..928\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H23",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 273-275",
  "excerpt": "FT   TRANSMEM        929..949\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H24",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 276-278",
  "excerpt": "FT   TOPO_DOM        950..1032\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H25",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 279-281",
  "excerpt": "FT   TRANSMEM        1033..1053\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H26",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 282-284",
  "excerpt": "FT   TOPO_DOM        1054..1057\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H27",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 285-287",
  "excerpt": "FT   TRANSMEM        1058..1078\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H28

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)

```json
{
  "evidence_id": "H28",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159",
  "source_sha256": "340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d",
  "retrieved_utc": "2026-11-02T04:31:59.503134+00:00",
  "source_locator": "lines 288-290",
  "excerpt": "FT   TOPO_DOM        1079..1419\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 159,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 103. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
