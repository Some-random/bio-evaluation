# EC_number_0014

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 4.3.3.9

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTLQETSVLEPTLQGTTTLPGLLAQRVAEHPEAIAVAYRDDKLTFRELASRSAALADYLEHLGVSADDCVGLFVEPSIDLMVGAWGILNAGAAYLPLSPEYPEDRLRYMIENSETKIILAQQRLVSRLRELAPKDVTIVTLRESEAFVRPEGTEAPAARSARPDTLAYVIYTSGSTGKPKGVMIEHRSIVNQLGWLRETYAIDRSKVILQKTPMSFDAAQWEILSPANGATVVMGAPGVYADPEGLIETIVKHNVTTLQCVPTLLQGLIDTEKFPECVSLQQIFSGGEALSRLLAIQTTQEMPGRALINVYGPTETTINSSSFPVDPADLDEGPQSISIGSPVHGTTYHILDKETLKPVGVGEIGELYIGGIQLARGYLHRDDLTAERFLEIELEEGAEPVRLYKTGDLGQWNNDGTVQFAGRADNQVKLRGYRVELDEISLAIENHDWVRNAAVIVKNDGRTGFQNLIACIELSEKEAALMDQGNHGSHHASKKSKLQVKAQLSNPGLRDDAELAARPAFDLEGAEPTPEQRARVFARKTYRFYEGGAVTQADLLGLLGATVTAGYSRKAADLAPAELGQILRWFGQYISEERLLPKYGYASPGALYATQMYFELEGVGGLKPGYYYYQPVRHQLVLISEREATGKATAQIHFIGKKSGIEPVYKNNILEVLEIETGHMVGLFEQILPAYGLDIHDRAYEPAVKDLLDVADEDYYLGTFELVPHAGARDDQAEVYVQTHGGKVAGLPEGQYRYENGELTRFSDDIVLKKHVIAINQSVYQAASFGISVYSRAEEEWLKYITLGKKLQHLMMNGLNLGFMSSGYSSKTGNPLPASRRMDAVLGANGVDSAPMYFFVGGRISDEQIGHEGMREDSVHMRGPAELIRDDLVSFLPDYMIPNRVVVFDRLPLSANGKIDVKALAASDQVNAELVERPFVAPRTETEKEIAAVWEKALRRENASVQDDFFESGGNSLIAVGLVRELNARLGVSLPLQSVLESPTIEKLARRLEREVAQESSRFVRLHAETGKARPVICWPGLGGYPMNLRSLAGEIGLGRSFYGVQSYGINEGETPYETITEMAKKDIEALKEIQPAGPYTLWGYSFGARVAFETAYQLEQAGEKVDNLFLIAPGSPKVRAENGKVWGREASFANRGYTTILFSVFTGTISGPDLDRCLETVTDEASFAEFISELKGIDVDLARRIISVVGQTYEFEYSFHELAERTLQAPISIFKAVGDDYSFLENSSGYSAEPPTVIDLDADHYSLLREDIGELVKHIRYLLGE

[Multiple Choices]
A. 4.3.1.12
B. 4.3.1.24
C. 4.2.3.1
D. 4.3.3.9
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

> The supplied sequence exactly matches the UniProt record for indigoidine synthase. That record assigns EC 4.3.3.9 and links the catalytic reaction producing indigoidine to experimental evidence (ECO:0000269, PubMed 17237222).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence is consistent with a multidomain nonribosomal peptide synthetase, which may suggest a biosynthetic enzyme, but that architecture does not establish its specific catalytic reaction or exact EC number among these choices.


**Missing item-specific fact**

> The protein-specific identification and experimentally characterized reaction of this sequence as indigoidine synthase are absent from the question.


**Reason**

> Choosing 4.3.3.9 requires knowing the enzyme's particular substrate-to-product chemistry; it cannot be reliably distinguished from the sequence and choices by general biological reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched curated record assigns the sequence to EC 4.3.3.9; the evidence provided does not support another listed option.


### Important caveats

- The EC assignment is supported by a curated database annotation linked to an experimental evidence code and publication; the primary paper was not independently reviewed here.
- The reviewer-only accession and annotation were not supplied to the evaluated model and do not make the question reasoning-supported.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is consistent with a multidomain nonribosomal peptide synthetase, which may suggest a biosynthetic enzyme, but that architecture does not establish its specific catalytic reaction or exact EC number among these choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and experimentally characterized reaction of this sequence as indigoidine synthase are absent from the question.",
    "reason": "Choosing 4.3.3.9 requires knowing the enzyme's particular substrate-to-product chemistry; it cannot be reliably distinguished from the sequence and choices by general biological reasoning alone."
  },
  "case_id": "EC_number_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt record for indigoidine synthase. That record assigns EC 4.3.3.9 and links the catalytic reaction producing indigoidine to experimental evidence (ECO:0000269, PubMed 17237222)."
  },
  "important_caveats": [
    "The EC assignment is supported by a curated database annotation linked to an experimental evidence code and publication; the primary paper was not independently reviewed here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model and do not make the question reasoning-supported."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched curated record assigns the sequence to EC 4.3.3.9; the evidence provided does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt record for indigoidine synthase. That record assigns EC 4.3.3.9 and links the catalytic reaction producing indigoidine to experimental evidence (ECO:0000269, PubMed 17237222).",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence is consistent with a multidomain nonribosomal peptide synthetase, which may suggest a biosynthetic enzyme, but that architecture does not establish its specific catalytic reaction or exact EC number among these choices.",
    "missing_item_specific_fact": "The protein-specific identification and experimentally characterized reaction of this sequence as indigoidine synthase are absent from the question.",
    "reason": "Choosing 4.3.3.9 requires knowing the enzyme's particular substrate-to-product chemistry; it cannot be reliably distinguished from the sequence and choices by general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched curated record assigns the sequence to EC 4.3.3.9; the evidence provided does not support another listed option."
  },
  "important_caveats": [
    "The EC assignment is supported by a curated database annotation linked to an experimental evidence code and publication; the primary paper was not independently reviewed here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model and do not make the question reasoning-supported."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q1MWN4 (INDGS_STRLA, Streptomyces lavendulae, 1282 aa, sequence matched) assigns EC 4.3.3.9 (Indigoidine synthase) with evidence code ECO:0000269 (experimental) from PubMed:17237222 (Takahashi et al., J. Biol. Chem. 2007). Both the current entry (C4, C5) and the historical archived entry (H1, H2, H4) confirm EC 4.3.3.9 with experimental catalytic-activity evidence. The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 → indigoidine + …) is explicitly annotated under this EC number.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a TSGSTGKPKG motif diagnostic of an adenylation (A) domain in non-ribosomal peptide synthetases (NRPS), along with condensation- and PCP-like features. However, NRPS enzymes are conventionally classified as ligases (EC 6.x.x.x), not lyases (EC 4.x.x.x). The fact that this particular single-module NRPS is reclassified as a C-N lyase (EC 4.3.3.9) is counterintuitive and cannot be inferred from domain architecture alone. Distinguishing 4.3.3.9 from 4.3.1.12, 4.3.1.24, and 4.2.3.1 requires knowing the exact substrate (L-glutamine + FMN), the specific bond cleaved, and the EC sub-subclass assignment (4.3.1 vs 4.3.3), none of which are derivable from sequence motifs.


**Missing item-specific fact**

> The specific annotation that this Streptomyces lavendulae protein is indigoidine synthase with EC 4.3.3.9, determined experimentally in Takahashi et al. 2007. The EC 4.3.3 sub-subclass (C-N lyases) and the fourth digit (9) are assigned to this exact enzyme; no general sequence heuristic distinguishes 4.3.3.9 from the other three lyase EC numbers provided as distractors.


**Reason**

> The question asks for a four-digit EC number from four plausible lyase-class options. The sequence reveals NRPS-like domain architecture, which would more naturally suggest a ligase (EC 6) classification. Recognizing this as EC 4.3.3.9 requires prior knowledge of the specific UniProt annotation or the 2007 experimental characterization. No general biological reasoning from the sequence distinguishes 4.3.3.9 from 4.3.1.12 or 4.3.1.24.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the four options are all EC 4 (lyase) numbers, only 4.3.3.9 is the experimentally verified annotation for this sequence. The other three (4.3.1.12, 4.3.1.24, 4.2.3.1) correspond to different enzymes (isochorismatase-type, other C-N hydro-lyases, copalyl diphosphate synthase) with different substrates and mechanisms. There is a single correct answer per the database, though none can be reached by reasoning from the sequence.


### Important caveats

- EC 4.3.3.9 is a recently assigned EC number; the UniProt entry was first public in February 2025. The experimental basis is a single 2007 J. Biol. Chem. paper.
- The NRPS-like domain architecture of this enzyme makes its EC 4 (lyase) classification non-obvious; a model relying on domain-function heuristics would likely predict EC 6.x.x.x (ligase) instead.
- All four distractors are in EC class 4 (lyases), which is atypical for an NRPS-type protein, making the question particularly dependent on memorized annotation rather than mechanistic reasoning.
- The sequence-to-accession match is confirmed (SHA-256 match, 1282 aa), so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a TSGSTGKPKG motif diagnostic of an adenylation (A) domain in non-ribosomal peptide synthetases (NRPS), along with condensation- and PCP-like features. However, NRPS enzymes are conventionally classified as ligases (EC 6.x.x.x), not lyases (EC 4.x.x.x). The fact that this particular single-module NRPS is reclassified as a C-N lyase (EC 4.3.3.9) is counterintuitive and cannot be inferred from domain architecture alone. Distinguishing 4.3.3.9 from 4.3.1.12, 4.3.1.24, and 4.2.3.1 requires knowing the exact substrate (L-glutamine + FMN), the specific bond cleaved, and the EC sub-subclass assignment (4.3.1 vs 4.3.3), none of which are derivable from sequence motifs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific annotation that this Streptomyces lavendulae protein is indigoidine synthase with EC 4.3.3.9, determined experimentally in Takahashi et al. 2007. The EC 4.3.3 sub-subclass (C-N lyases) and the fourth digit (9) are assigned to this exact enzyme; no general sequence heuristic distinguishes 4.3.3.9 from the other three lyase EC numbers provided as distractors.",
    "reason": "The question asks for a four-digit EC number from four plausible lyase-class options. The sequence reveals NRPS-like domain architecture, which would more naturally suggest a ligase (EC 6) classification. Recognizing this as EC 4.3.3.9 requires prior knowledge of the specific UniProt annotation or the 2007 experimental characterization. No general biological reasoning from the sequence distinguishes 4.3.3.9 from 4.3.1.12 or 4.3.1.24."
  },
  "case_id": "EC_number_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q1MWN4 (INDGS_STRLA, Streptomyces lavendulae, 1282 aa, sequence matched) assigns EC 4.3.3.9 (Indigoidine synthase) with evidence code ECO:0000269 (experimental) from PubMed:17237222 (Takahashi et al., J. Biol. Chem. 2007). Both the current entry (C4, C5) and the historical archived entry (H1, H2, H4) confirm EC 4.3.3.9 with experimental catalytic-activity evidence. The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 → indigoidine + …) is explicitly annotated under this EC number."
  },
  "important_caveats": [
    "EC 4.3.3.9 is a recently assigned EC number; the UniProt entry was first public in February 2025. The experimental basis is a single 2007 J. Biol. Chem. paper.",
    "The NRPS-like domain architecture of this enzyme makes its EC 4 (lyase) classification non-obvious; a model relying on domain-function heuristics would likely predict EC 6.x.x.x (ligase) instead.",
    "All four distractors are in EC class 4 (lyases), which is atypical for an NRPS-type protein, making the question particularly dependent on memorized annotation rather than mechanistic reasoning.",
    "The sequence-to-accession match is confirmed (SHA-256 match, 1282 aa), so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the four options are all EC 4 (lyase) numbers, only 4.3.3.9 is the experimentally verified annotation for this sequence. The other three (4.3.1.12, 4.3.1.24, 4.2.3.1) correspond to different enzymes (isochorismatase-type, other C-N hydro-lyases, copalyl diphosphate synthase) with different substrates and mechanisms. There is a single correct answer per the database, though none can be reached by reasoning from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q1MWN4 (INDGS_STRLA, Streptomyces lavendulae, 1282 aa, sequence matched) assigns EC 4.3.3.9 (Indigoidine synthase) with evidence code ECO:0000269 (experimental) from PubMed:17237222 (Takahashi et al., J. Biol. Chem. 2007). Both the current entry (C4, C5) and the historical archived entry (H1, H2, H4) confirm EC 4.3.3.9 with experimental catalytic-activity evidence. The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 → indigoidine + …) is explicitly annotated under this EC number.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a TSGSTGKPKG motif diagnostic of an adenylation (A) domain in non-ribosomal peptide synthetases (NRPS), along with condensation- and PCP-like features. However, NRPS enzymes are conventionally classified as ligases (EC 6.x.x.x), not lyases (EC 4.x.x.x). The fact that this particular single-module NRPS is reclassified as a C-N lyase (EC 4.3.3.9) is counterintuitive and cannot be inferred from domain architecture alone. Distinguishing 4.3.3.9 from 4.3.1.12, 4.3.1.24, and 4.2.3.1 requires knowing the exact substrate (L-glutamine + FMN), the specific bond cleaved, and the EC sub-subclass assignment (4.3.1 vs 4.3.3), none of which are derivable from sequence motifs.",
    "missing_item_specific_fact": "The specific annotation that this Streptomyces lavendulae protein is indigoidine synthase with EC 4.3.3.9, determined experimentally in Takahashi et al. 2007. The EC 4.3.3 sub-subclass (C-N lyases) and the fourth digit (9) are assigned to this exact enzyme; no general sequence heuristic distinguishes 4.3.3.9 from the other three lyase EC numbers provided as distractors.",
    "reason": "The question asks for a four-digit EC number from four plausible lyase-class options. The sequence reveals NRPS-like domain architecture, which would more naturally suggest a ligase (EC 6) classification. Recognizing this as EC 4.3.3.9 requires prior knowledge of the specific UniProt annotation or the 2007 experimental characterization. No general biological reasoning from the sequence distinguishes 4.3.3.9 from 4.3.1.12 or 4.3.1.24."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the four options are all EC 4 (lyase) numbers, only 4.3.3.9 is the experimentally verified annotation for this sequence. The other three (4.3.1.12, 4.3.1.24, 4.2.3.1) correspond to different enzymes (isochorismatase-type, other C-N hydro-lyases, copalyl diphosphate synthase) with different substrates and mechanisms. There is a single correct answer per the database, though none can be reached by reasoning from the sequence."
  },
  "important_caveats": [
    "EC 4.3.3.9 is a recently assigned EC number; the UniProt entry was first public in February 2025. The experimental basis is a single 2007 J. Biol. Chem. paper.",
    "The NRPS-like domain architecture of this enzyme makes its EC 4 (lyase) classification non-obvious; a model relying on domain-function heuristics would likely predict EC 6.x.x.x (ligase) instead.",
    "All four distractors are in EC class 4 (lyases), which is atypical for an NRPS-type protein, making the question particularly dependent on memorized annotation rather than mechanistic reasoning.",
    "The sequence-to-accession match is confirmed (SHA-256 match, 1282 aa), so the annotation applies directly to the supplied sequence."
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

**Accession:** `Q1MWN4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 86. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
"Q1MWN4"
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17237222","source":"PubMed"}],"value":"Blue pigment synthetase-encoding gene A"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17237222","source":"PubMed"}],"value":"Blue-pigment synthetase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17237222","source":"PubMed"}],"value":"4.3.3.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Indigoidine synthase"}}}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"17237222","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81500"}}],"reaction":{"ecNumber":"4.3.3.9","evidences":[{"evidenceCode":"ECO:0000269","id":"17237222","source":"PubMed"}],"name":"2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81499"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:58359"},{"database":"ChEBI","id":"CHEBI:79296"},{"database":"ChEBI","id":"CHEBI:456215"}]}}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
ID   INDGS_STRLA             Reviewed;        1282 AA.
AC   Q1MWN4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   30-MAY-2006, sequence version 1.
DT   28-JAN-2026, entry version 86.
DE   RecName: Full=Indigoidine synthase {ECO:0000305};
DE            EC=4.3.3.9 {ECO:0000269|PubMed:17237222};
DE   AltName: Full=Blue pigment synthetase-encoding gene A {ECO:0000303|PubMed:17237222};
DE   AltName: Full=Blue-pigment synthetase {ECO:0000303|PubMed:17237222};
GN   Name=bpsA {ECO:0000303|PubMed:17237222};
OS   Streptomyces lavendulae.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=1914;
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
DE   RecName: Full=Indigoidine synthase {ECO:0000305};
DE            EC=4.3.3.9 {ECO:0000269|PubMed:17237222};
DE   AltName: Full=Blue pigment synthetase-encoding gene A {ECO:0000303|PubMed:17237222};
DE   AltName: Full=Blue-pigment synthetase {ECO:0000303|PubMed:17237222};
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 30-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2
CC         AMP + 2 diphosphate + 2 H2O; Xref=Rhea:RHEA:81499, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:30616, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:58359,
CC         ChEBI:CHEBI:79296, ChEBI:CHEBI:456215; EC=4.3.3.9;
CC         Evidence={ECO:0000269|PubMed:17237222};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81500;
CC         Evidence={ECO:0000269|PubMed:17237222};
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 14. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
