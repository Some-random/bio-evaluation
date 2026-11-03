# motif_position_0020: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/motif_position_0020.txt)

**Task:** `motif_position`  
**Author key, unchanged:** **D** — 165..168

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | no saved label | no saved label | output error (invalid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MAGLQLMTPASSPMGPFFGLPWQQEAIHDNIYTPRKYQVELLEAALDHNTIVCLNSGSGKTFIAVLLSKELSYQIRGDFSKNAKRTVFLVNSEKQVSQQVSAVRTHTDLKVGEYSDLQKTQCWAKEKWYQEFETRQVLVMTCHIFLNVLKSGNVSLSNINLLVFDECHLAIQDHPYREIMKICESCQPCPRILGLTASILNGKCDPRDLEEKIQKLEKILRSNAETATDLVVLDRYASQPCEIVLDCGPYVDRSGLFQRLLNELDEALNFLIDCNISTHSKERDSTIISKQILSDCRAVLLVLGPWCADKVAGMMVRELQKYIKHEQEELHRKFLLFTDTILRKIHALCEEHFSPASLDMKFVTPKVIKLLEILRKYKPYERQQFESVEWYNNRNQDNYVSWSDSEDDDDDEDEEIEEKEKTETSFPSPFTNILCGIIFVERRYTAVVLNRLIKEAGKQDPELAYISSNFITGHGIGKNQPRNKQMEVEFRKQEEVLRKFRAHETNLLIATSIVEEGVDIPKCNLVVRFDLPSEYRSYVQSKGRARAPISNYIMLADSDKIKTFEEDLKTYKAIEKILRNKCSKSIDCGNTESEPVVDDDEIFPPYVLRQDDGSPRVTINTAIGHINRYCARLPSDPFTHLAPKCKTREMSDGPYRSTLYLPINSPLRAPIVGPPMNCARLAERAVALICCKKLHEIGELDDHLMPVGKETVKYEEELDLHDEEETSVPGRPGSTKRRQCYPKAIPECLRNSYPKPGQPCYLYVIGMVLTTPLPDELNFRRRKLYPPEDTTRCFGILTAKPIPQIPHFPVYTRSGEVTISIELKKSGFTLNLEQLELITRLHQYIFSHILRLEKPALEFKPTVADCAYCVLPLNVVNDSGTLDIDFKFVEDIEKSEARTGIPNTQYSAESPFIFKLEDYQDAVIIPRYRNFDQPHRFYVADVYTDLTPLSKFPSPEYETFAEYYKTKYNLDLTNLNQPLLDVDHTSSRLNLLTPRHLNQKGKALPLSSAEKRKAKWESLQNKQILVPELCAIHPVPASLWRKAVCLPSILYRLHCLLTAEELRAQTAIDAGVGVKSLPEDFRYPNLDFGWKRSIDSKTFISSQSSSAVESEGDCRLNTTMVPDSATSSAANHVIYTQTNDQMSVNCTPLCQKSLSDLRGVCFSEDYKAINGVSCNGVTSDSEAESGVCFQKDERIACTQEIPEKSTSFHIQNLPKENQPILNECTLSKKFLDGNVSKPTSDECPSTCTSDMQYESGLSNGYSSKTLGPNPGLILQALTLSNASDGFNLERLEMLGDSFLKHAITTYLFCTYPDAHEGRLSYMRSKKVSNCNLYRLGKKKGSPSRMVVSIFDPPVNWLPPGYIVNQDKSSDKWESNETSGEGVMANGKIDEDFDDDDEEDEDLMWRNPKEETDFDDDFLEYDQEHIKFIDSMLMGSGAFVKKIPLSSFAPPDQNYEWRAPKKPLLESAQFPSEFDDFDYSSWDAMCYLDPSKAVEEDDFVVGFWNPSEENCGTDVGKQSISYDLHTEQCIADKSIADCVEALLGCYLTSCGERAAQLFLCSLGLKVLPQVRRSVTSTNSISASSSYQKTSTRDICTLNSELSSCKGVEYGYLKIPPRCMFEHPDAEKTLDHLISGFENFEKKINYPFKNKAYLLQAFTHASYHYNTITDCYQRLEFLGDAILDYLITKHLYEDPRQHSPGVLTDLRSALVNNTIFASLAVKYDYHKYFKAISPELFHVIDDFVQFQLEKNEMQGMDSELRRSEEDEEKEEDIEVPKAMGDIFESLAGAIYMDSGMSLETVWRVYYPMMHPLIEKFSANVPRSPVRELLEMEPETAKFSPAERTYDGKVRVTVEVVGKGKFKGVGRSYRIAKSAAARRALRSLKANQSQVPNS

[Multiple Choices]
A. 218..225
B. 326..340
C. 179..182
D. 165..168
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Motif Position Prediction, which is to identify the specific positions of a conserved motif within a protein sequence. A motif is a short, recurring pattern in protein sequences that is often associated with a specific function or structure. Based on the provided protein sequence, you will need to determine the start and end positions of the motif.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates a DECH box at residues 165–168, matching choice D. This supports the key as a database annotation, not as independently verified experimental evidence.

Citations as saved: [C15](#evidence-c15), [H12](#evidence-h12).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice D contains the sequence motif DECH, which is consistent with a conserved helicase motif. However, the question does not name the motif or otherwise establish that this is the motif being asked about.


**Missing item-specific fact**

> The intended motif identity—specifically, that the target is the DECH box annotated for this protein—and its position in this protein.


**Reason**

> Without the motif name or a defining pattern, the sequence and choices alone do not uniquely specify which conserved motif to locate. Selecting D depends on recognizing or looking up the protein-specific intended annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "C",
  "D"
]
```

> The question does not identify the motif whose position is requested. D is supported if the intended target is the DECH box, but the wording does not rule out other motifs or regions corresponding to the other intervals.


### Important caveats

- The reviewer-only UniProt record matches the supplied sequence; its motif annotation supports the expected answer but was not available to the evaluated model.
- The cited motif annotation does not itself establish experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice D contains the sequence motif DECH, which is consistent with a conserved helicase motif. However, the question does not name the motif or otherwise establish that this is the motif being asked about.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The intended motif identity—specifically, that the target is the DECH box annotated for this protein—and its position in this protein.",
    "reason": "Without the motif name or a defining pattern, the sequence and choices alone do not uniquely specify which conserved motif to locate. Selecting D depends on recognizing or looking up the protein-specific intended annotation."
  },
  "case_id": "motif_position_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C15",
      "H12"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a DECH box at residues 165–168, matching choice D. This supports the key as a database annotation, not as independently verified experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the supplied sequence; its motif annotation supports the expected answer but was not available to the evaluated model.",
    "The cited motif annotation does not itself establish experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "C",
      "D"
    ],
    "reason": "The question does not identify the motif whose position is requested. D is supported if the intended target is the DECH box, but the wording does not rule out other motifs or regions corresponding to the other intervals."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "motif_position_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a DECH box at residues 165–168, matching choice D. This supports the key as a database annotation, not as independently verified experimental evidence.",
    "evidence_ids": ["C15", "H12"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice D contains the sequence motif DECH, which is consistent with a conserved helicase motif. However, the question does not name the motif or otherwise establish that this is the motif being asked about.",
    "missing_item_specific_fact": "The intended motif identity—specifically, that the target is the DECH box annotated for this protein—and its position in this protein.",
    "reason": "Without the motif name or a defining pattern, the sequence and choices alone do not uniquely specify which conserved motif to locate. Selecting D depends on recognizing or looking up the protein-specific intended annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "C", "D"],
    "reason": "The question does not identify the motif whose position is requested. D is supported if the intended target is the DECH box, but the wording does not rule out other motifs or regions corresponding to the other intervals."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the supplied sequence; its motif annotation supports the expected answer but was not available to the evaluated model.",
    "The cited motif annotation does not itself establish experimental validation."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

**Validation errors:** `invalid_json:Unterminated string starting at: line 5 column 15 (char 110)`, `incomplete_or_non_native_termination`.

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "motif_position_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C15/H12) explicitly labels a 'DECH box'
```

</details>

**Saved parsed visible review:** `null`.

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence has the DECH motif at positions 165–168, and the UniProt annotation identifies that interval as the DECH box. This supports the key as a database motif annotation, not as independently established experimental evidence.

Citations as saved: [C15](#evidence-c15), [H12](#evidence-h12).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the conspicuous four-residue DECH pattern at option D. Transferable knowledge that DECH is a conserved motif in Dicer-like helicases makes this a credible match; the other offered intervals do not show that pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The exact target’s database record is not necessary to identify the distinctive motif in the supplied sequence, though recognizing its biological significance relies on family-level knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The prompt does not name the motif, which is a wording limitation, but the offered choices include a distinctive DECH sequence at D and no comparably clear competing motif.


### Important caveats

- The reviewer-only source annotation applies to the sequence-matched entry, but its annotation evidence does not establish experimental verification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conspicuous four-residue DECH pattern at option D. Transferable knowledge that DECH is a conserved motif in Dicer-like helicases makes this a credible match; the other offered intervals do not show that pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The exact target’s database record is not necessary to identify the distinctive motif in the supplied sequence, though recognizing its biological significance relies on family-level knowledge."
  },
  "case_id": "motif_position_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C15",
      "H12"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has the DECH motif at positions 165–168, and the UniProt annotation identifies that interval as the DECH box. This supports the key as a database motif annotation, not as independently established experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only source annotation applies to the sequence-matched entry, but its annotation evidence does not establish experimental verification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The prompt does not name the motif, which is a wording limitation, but the offered choices include a distinctive DECH sequence at D and no comparably clear competing motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "motif_position_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has the DECH motif at positions 165–168, and the UniProt annotation identifies that interval as the DECH box. This supports the key as a database motif annotation, not as independently established experimental evidence.",
    "evidence_ids": ["C15", "H12"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the conspicuous four-residue DECH pattern at option D. Transferable knowledge that DECH is a conserved motif in Dicer-like helicases makes this a credible match; the other offered intervals do not show that pattern.",
    "missing_item_specific_fact": "",
    "reason": "The exact target’s database record is not necessary to identify the distinctive motif in the supplied sequence, though recognizing its biological significance relies on family-level knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The prompt does not name the motif, which is a wording limitation, but the offered choices include a distinctive DECH sequence at D and no comparably clear competing motif."
  },
  "important_caveats": [
    "The reviewer-only source annotation applies to the sequence-matched entry, but its annotation evidence does not establish experimental verification."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C15/H12) explicitly labels positions 165..168 as a 'DECH box' motif. Direct inspection of the supplied sequence confirms residues 165-168 are D-E-C-H, matching the canonical DECH box of DExD/H-box helicases. The sequence is a 1891-aa Endoribonuclease Dicer-L (Xenopus laevis), a member of the DExD/H-box superfamily, and the DECH box is its defining short conserved motif within the helicase ATP-binding domain (annotated 41..217). The annotation is computational (PROSITE-ProRule based), but the motif identity is well-established for this protein family.

Citations as saved: [C15](#evidence-c15), [H12](#evidence-h12), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains a clear Walker A / P-loop motif 'GSGKT' at approximately positions 57-62, identifying this protein as a member of the DExD/H-box helicase superfamily. A defining feature of this family is the conserved DECH (or DEAH/DExH) box, a 4-residue motif located within the helicase ATP-binding domain. A knowledgeable model can (1) recognize the helicase family from the Walker A motif, (2) recall that the DECH box is the canonical short motif in this family, and (3) scan the sequence for the 'DECH' pattern, which appears uniquely at positions 165-168. The other options (218-225: KILRSNAE; 326-340: a linker-region segment; 179-182: IMKI) do not correspond to any recognized conserved motif pattern. Family-level knowledge of DExD/H-box helicases and their DECH box motif, combined with a straightforward subsequence search, meaningfully distinguishes option D from all alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DECH box is one of the most widely conserved and taught short motifs in molecular biology, present in hundreds of DExD/H-box helicases. Recognizing the Walker A motif in the input sequence establishes family membership, and the DECH pattern is identifiable by direct sequence search. No target-specific database lookup is required to distinguish the correct option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The question asks for 'a conserved motif' without specifying which one. However, only option D (165-168) corresponds to a recognizable conserved motif (DECH box). The other options contain no recognizable motif pattern. The DECH box is the most prominent short conserved motif in DExD/H-box helicases, making it the unambiguous intended answer.


### Important caveats

- The DECH box annotation in UniProt is computational (PROSITE-ProRule), not experimentally validated, but the motif is universally recognized across the DExD/H-box family.
- The question does not name the motif, relying on the solver to identify the most prominent conserved short motif; the DECH box is the only option matching a known motif.
- The protein is a Dicer homolog (Dicer-L) from Xenopus laevis, but this identity is not needed to find the DECH box; the helicase family signature suffices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains a clear Walker A / P-loop motif 'GSGKT' at approximately positions 57-62, identifying this protein as a member of the DExD/H-box helicase superfamily. A defining feature of this family is the conserved DECH (or DEAH/DExH) box, a 4-residue motif located within the helicase ATP-binding domain. A knowledgeable model can (1) recognize the helicase family from the Walker A motif, (2) recall that the DECH box is the canonical short motif in this family, and (3) scan the sequence for the 'DECH' pattern, which appears uniquely at positions 165-168. The other options (218-225: KILRSNAE; 326-340: a linker-region segment; 179-182: IMKI) do not correspond to any recognized conserved motif pattern. Family-level knowledge of DExD/H-box helicases and their DECH box motif, combined with a straightforward subsequence search, meaningfully distinguishes option D from all alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DECH box is one of the most widely conserved and taught short motifs in molecular biology, present in hundreds of DExD/H-box helicases. Recognizing the Walker A motif in the input sequence establishes family membership, and the DECH pattern is identifiable by direct sequence search. No target-specific database lookup is required to distinguish the correct option."
  },
  "case_id": "motif_position_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C15",
      "H12",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C15/H12) explicitly labels positions 165..168 as a 'DECH box' motif. Direct inspection of the supplied sequence confirms residues 165-168 are D-E-C-H, matching the canonical DECH box of DExD/H-box helicases. The sequence is a 1891-aa Endoribonuclease Dicer-L (Xenopus laevis), a member of the DExD/H-box superfamily, and the DECH box is its defining short conserved motif within the helicase ATP-binding domain (annotated 41..217). The annotation is computational (PROSITE-ProRule based), but the motif identity is well-established for this protein family."
  },
  "important_caveats": [
    "The DECH box annotation in UniProt is computational (PROSITE-ProRule), not experimentally validated, but the motif is universally recognized across the DExD/H-box family.",
    "The question does not name the motif, relying on the solver to identify the most prominent conserved short motif; the DECH box is the only option matching a known motif.",
    "The protein is a Dicer homolog (Dicer-L) from Xenopus laevis, but this identity is not needed to find the DECH box; the helicase family signature suffices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for 'a conserved motif' without specifying which one. However, only option D (165-168) corresponds to a recognizable conserved motif (DECH box). The other options contain no recognizable motif pattern. The DECH box is the most prominent short conserved motif in DExD/H-box helicases, making it the unambiguous intended answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "motif_position_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C15/H12) explicitly labels positions 165..168 as a 'DECH box' motif. Direct inspection of the supplied sequence confirms residues 165-168 are D-E-C-H, matching the canonical DECH box of DExD/H-box helicases. The sequence is a 1891-aa Endoribonuclease Dicer-L (Xenopus laevis), a member of the DExD/H-box superfamily, and the DECH box is its defining short conserved motif within the helicase ATP-binding domain (annotated 41..217). The annotation is computational (PROSITE-ProRule based), but the motif identity is well-established for this protein family.",
    "evidence_ids": ["C15", "H12", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence contains a clear Walker A / P-loop motif 'GSGKT' at approximately positions 57-62, identifying this protein as a member of the DExD/H-box helicase superfamily. A defining feature of this family is the conserved DECH (or DEAH/DExH) box, a 4-residue motif located within the helicase ATP-binding domain. A knowledgeable model can (1) recognize the helicase family from the Walker A motif, (2) recall that the DECH box is the canonical short motif in this family, and (3) scan the sequence for the 'DECH' pattern, which appears uniquely at positions 165-168. The other options (218-225: KILRSNAE; 326-340: a linker-region segment; 179-182: IMKI) do not correspond to any recognized conserved motif pattern. Family-level knowledge of DExD/H-box helicases and their DECH box motif, combined with a straightforward subsequence search, meaningfully distinguishes option D from all alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The DECH box is one of the most widely conserved and taught short motifs in molecular biology, present in hundreds of DExD/H-box helicases. Recognizing the Walker A motif in the input sequence establishes family membership, and the DECH pattern is identifiable by direct sequence search. No target-specific database lookup is required to distinguish the correct option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for 'a conserved motif' without specifying which one. However, only option D (165-168) corresponds to a recognizable conserved motif (DECH box). The other options contain no recognizable motif pattern. The DECH box is the most prominent short conserved motif in DExD/H-box helicases, making it the unambiguous intended answer."
  },
  "important_caveats": [
    "The DECH box annotation in UniProt is computational (PROSITE-ProRule), not experimentally validated, but the motif is universally recognized across the DExD/H-box family.",
    "The question does not name the motif, relying on the solver to identify the most prominent conserved short motif; the DECH box is the only option matching a known motif.",
    "The protein is a Dicer homolog (Dicer-L) from Xenopus laevis, but this identity is not needed to find the DECH box; the helicase family signature suffices."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0A974H8H3",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "f0d38653f552392ea0c0e2a67360b0747665e7fa5312e459ceb4a963f9fffff9",
  "benchmark_sequence_length": 1891,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 17,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-02-22",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "current_source_sequence_sha256": "f0d38653f552392ea0c0e2a67360b0747665e7fa5312e459ceb4a963f9fffff9",
  "current_source_sequence_length": 1891,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 15,
  "selected_historical_version": {
    "accession": "A0A974H8H3",
    "database": "Swiss-Prot",
    "entryVersion": 15,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DICRL_XENLA",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "selected_historical_source_sequence_sha256": "f0d38653f552392ea0c0e2a67360b0747665e7fa5312e459ceb4a963f9fffff9",
  "selected_historical_source_sequence_length": 1891,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 15,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A974H8H3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":17,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-02-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"African clawed frog\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Amphibia\",\"Batrachia\",\"Anura\",\"Pipoidea\",\"Pipidae\",\"Xenopodinae\",\"Xenopus\",\"Xenopus\"],\"scientificName\":\"Xenopus laevis\",\"taxonId\":8355}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"value\":\"3.1.26.3\"}],\"fullName\":{\"value\":\"Endoribonuclease Dicer-L\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Helicase ATP-binding\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00541\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":217},\"start\":{\"modifier\":\"EXACT\",\"value\":41}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helicase C-terminal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00542\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":594},\"start\":{\"modifier\":\"EXACT\",\"value\":425}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Dicer dsRNA-binding fold\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00657\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":714},\"start\":{\"modifier\":\"EXACT\",\"value\":622}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"PAZ\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00142\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1034},\"start\":{\"modifier\":\"EXACT\",\"value\":887}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"RNase III 1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00177\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1379},\"start\":{\"modifier\":\"EXACT\",\"value\":1248}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"RNase III 2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00177\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1793},\"start\":{\"modifier\":\"EXACT\",\"value\":1635}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"DRBM\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00266\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1883},\"start\":{\"modifier\":\"EXACT\",\"value\":1818}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":425},\"start\":{\"modifier\":\"EXACT\",\"value\":399}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":738},\"start\":{\"modifier\":\"EXACT\",\"value\":719}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1398},\"start\":{\"modifier\":\"EXACT\",\"value\":1367}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"DECH box\",\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":168},\"start\":{\"modifier\":\"EXACT\",\"value\":165}},\"type\":\"Motif\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   DICRL_XENLA             Reviewed;        1891 AA.\nAC   A0A974H8H3; A0A1L8F9L1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-FEB-2023, sequence version 1.\nDT   28-JAN-2026, entry version 15.\nDE   RecName: Full=Endoribonuclease Dicer-L;\nDE            EC=3.1.26.3;\nGN   Name=dicer1.L; Synonyms=dicer1;\nOS   Xenopus laevis (African clawed frog).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Amphibia;\nOC   Batrachia; Anura; Pipoidea; Pipidae; Xenopodinae; Xenopus; Xenopus.\nOX   NCBI_TaxID=8355;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 183-185",
  "excerpt": "FT   DOMAIN          41..217\nFT                   /note=\"Helicase ATP-binding\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00541\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 186-188",
  "excerpt": "FT   DOMAIN          425..594\nFT                   /note=\"Helicase C-terminal\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00542\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 189-191",
  "excerpt": "FT   DOMAIN          622..714\nFT                   /note=\"Dicer dsRNA-binding fold\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00657\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 192-194",
  "excerpt": "FT   DOMAIN          887..1034\nFT                   /note=\"PAZ\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00142\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 195-197",
  "excerpt": "FT   DOMAIN          1248..1379\nFT                   /note=\"RNase III 1\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00177\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 198-200",
  "excerpt": "FT   DOMAIN          1635..1793\nFT                   /note=\"RNase III 2\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00177\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 201-203",
  "excerpt": "FT   DOMAIN          1818..1883\nFT                   /note=\"DRBM\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00266\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 204-206",
  "excerpt": "FT   REGION          399..425\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 207-209",
  "excerpt": "FT   REGION          719..738\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 210-212",
  "excerpt": "FT   REGION          1367..1398\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "source_locator": "lines 213-214",
  "excerpt": "FT   MOTIF           165..168\nFT                   /note=\"DECH box\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/motif_position.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
