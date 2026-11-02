# transmembrane_0103

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `boundary_alternative_not_independently_validated`.

> Cited PROSITE-ProRule Transmembrane features match keyC including317..337; optionD shifts that one interval to318..338.

**Remaining uncertainty:** The specific shift is present in the options. The source supports the keyed predicted interval, not experimental equivalence of the alternative boundaries.

Evidence checked: [C1](#evidence-c1), [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q7K6A5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 159. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
"Q7K6A5"
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":81},"start":{"modifier":"EXACT","value":61}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":111},"start":{"modifier":"EXACT","value":91}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":189},"start":{"modifier":"EXACT","value":169}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":212},"start":{"modifier":"EXACT","value":192}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":296},"start":{"modifier":"EXACT","value":276}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":337},"start":{"modifier":"EXACT","value":317}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":809},"start":{"modifier":"EXACT","value":789}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":850},"start":{"modifier":"EXACT","value":830}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":928},"start":{"modifier":"EXACT","value":908}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":949},"start":{"modifier":"EXACT","value":929}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":1053},"start":{"modifier":"EXACT","value":1033}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":1078},"start":{"modifier":"EXACT","value":1058}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C31

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"citation":{"authors":["Si K.","He X.","Chen L.","Zhang A.","Guo C.","Li M."],"citationCrossReferences":[{"database":"PubMed","id":"37527341"},{"database":"DOI","id":"10.1073/pnas.2219905120"}],"citationType":"journal article","firstPage":"e2219905120","id":"37527341","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"e2219905120","publicationDate":"2023","title":"The structure of <i>Plasmodium falciparum</i> multidrug resistance protein 1 reveals an N-terminal regulatory domain.","volume":"120"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8JVH","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8JW4","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8JWF","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8JWG","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8JWI","source":"PDB"}],"referenceNumber":6,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (2.94 ANGSTROMS) OF 38-1419 IN COMPLEX WITH ATP; MAGNESIUM ION AND MEFLOQUINE","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","R DOMAIN","MUTAGENESIS OF 1-MET--ASN-37; ASN-86; TYR-184; THR-199; LYS-217; LYS-220; LYS-221; PHE-331; GLU-588; SER-1034; ASN-1042; ASP-1246 AND GLU-1337"]}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 72-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
RN   [6] {ECO:0007744|PDB:8JVH, ECO:0007744|PDB:8JW4, ECO:0007744|PDB:8JWF, ECO:0007744|PDB:8JWG, ECO:0007744|PDB:8JWI}
RP   STRUCTURE BY ELECTRON MICROSCOPY (2.94 ANGSTROMS) OF 38-1419 IN COMPLEX
RP   WITH ATP; MAGNESIUM ION AND MEFLOQUINE, FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, R DOMAIN, AND MUTAGENESIS OF 1-MET--ASN-37;
RP   ASN-86; TYR-184; THR-199; LYS-217; LYS-220; LYS-221; PHE-331; GLU-588;
RP   SER-1034; ASN-1042; ASP-1246 AND GLU-1337.
RX   PubMed=37527341; DOI=10.1073/pnas.2219905120;
RA   Si K., He X., Chen L., Zhang A., Guo C., Li M.;
RT   "The structure of <i>Plasmodium falciparum</i> multidrug resistance protein
RT   1 reveals an N-terminal regulatory domain.";
RL   Proc. Natl. Acad. Sci. U.S.A. 120:e2219905120-e2219905120(2023).
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 222-224`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        61..81
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 228-230`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        91..111
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 234-236`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        169..189
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 240-242`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        192..212
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 246-248`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        276..296
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 252-254`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        317..337
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 258-260`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        789..809
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 264-266`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        830..850
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 270-272`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        908..928
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 273-275`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        929..949
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 279-281`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        1033..1053
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 285-287`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
FT   TRANSMEM        1058..1078
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00441"
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 103. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
