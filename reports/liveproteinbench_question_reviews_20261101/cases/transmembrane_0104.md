# transmembrane_0104

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 36..56; 494..514; 525..549; 555..582; 588..619; 623..659; 1075..1098; 1301..1334; 1338..1361; 1368..1394; 1400..1431; 1435..1466

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFVKNFIHKLKELKQKSLDKFANLLYDYGGYVYDRPCTFIICSLICCLLLTCGFYFKEHEKDIYKLYSISNSYAYETNETINDFFYKSRRCFILVESNVNLLKPKILRELQKFEEGTKDIEVDLSEINECKTNSELPPEQSHVAKELYKTLIQRSEENLKSGKINGSLFDYSDLDENGKSVLSLAGKENNDDTLIEGDNKNDEETSANNNNNEDDNNEDDNNEDDNNEDDNNENDNNNNNEDDNNNDDDDDEDNEEEDEEKQKSLREKLYRKIYEMLKKKKENIVLDENNPNVNFTDYKDDVFYPYQYIPPMLIKADRCKLQNVFGDKNLNIDLREASDGLKKQITYTLEDICEKKYGDCNFSSLFLYYEKGNGYIDYPIKVDNLDFYVNRRTYKEMMFKGILGNMVYEKSGSKYIIKSANAIMTVIPLLNSHTYEPYALAYEKKLIDYVRFYNLDDIIQDEETNDDNDPFIRFHVFTDRSLEDEVDRISKIDNLTRLLLLIGVLLIFMYALFNNVTSVLYRSKPLCAVMGIFCGFLGFLSGSGFLYFLGVKSVPPAETVPFLVIGVGVDDVFVILNSYSLLFMVKDNKKRIQMCLKDSALAITVTTLTNIIAFLISAISPFYSICAFSLFTASSLFFGYLMVLTFLLSFLCIEAKLEKKKRNIFTGTFHLFRSIFMKSSKKNKKENKENNIHDDGDNDNDEKKKDLSLEVKNNEDDYENISIYEWIHNLYLFEESINKKKKNAALVYASNNGMSSNLNNVNEDGFPNPSKIVSMEDVKKRNIKKDDAYINKEDEEGGGYYNKDDNKKKDILGKKQKKNNNNVTLVSKKGEDNELDVYYENLDEKTNDKYKMNNIKSSKLKYDNDKKDGAIINNRPSSDEEYKEEKDKNKINILNDVFNDITIKPNENILLDRGDVIKSSGYDSSYNDLQSSSLPNPSSNEVLNKTTMVYNETDLKDNKKEIKSSKKNVKDIKKSDMIHDDTYDIINSNNKNILLSSNEINNNSNNTNKFNNNSTELATKDTQQFINGHDKNIYLLSSHDNALFYKYIYEEPKGNIGKYFRSLVKNYYVPFLSSRFGKTIVYIMFTIIIAMSIYGCTLMKKGIKYDKAFPVDSYVRRFTTAKIKYFPDFGDFIEVYYFDKHFINKYRGLEKNTKEAASSFLYSDLTDRQIMNSPKINKNVHWENTNLQEELINMHNTLESQEFVTSVANGFTFFLNKNKSSLRKENPQEFYEIFANWLKKDFVGNLFKNDFVFLNGKLVAWRFHYFQKNVDDSEISSKWLKACKQITKLENHNVQMVCFHLSSIFNETDESIIEVTLINLGITILTILVVTAYIIKGFYSCVIIALIIFLIDLCIFGFMCLCGITMNIISMVILVLSVGFSIDHTSHIVQAFSHSMGRTRDEKMKESLHLMIGPVLHSGLSTWFVISTLFFSNKDFTVIFFQTLSLVLFFSITFSSMFLPVLLSSFGPLH

[Multiple Choices]
A. 36..56; 494..514; 525..549; 588..619; 623..659; 1075..1098; 1301..1334; 1338..1361; 1368..1394; 1400..1431; 1435..1466
B. 36..56; 494..514; 525..549; 555..582; 588..619; 623..659; 1075..1098; 1301..1334; 1338..1361; 1368..1394; 1400..1431; 1435..1466
C. 36..56; 494..514; 525..549; 555..582; 593..624; 623..659; 1075..1098; 1301..1334; 1338..1361; 1368..1394; 1400..1431; 1435..1466
D. 13..35
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

> The supplied sequence exactly matches the 1470-aa sequence in the historical UniProt entry. Its annotated transmembrane intervals match choice B, with cited experimental and PDB evidence for these features. The separate intramembrane regions are not annotated as membrane-spanning helices.

Citations as saved: [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H23](#evidence-h23), [H25](#evidence-h25), [H27](#evidence-h27), [H29](#evidence-h29), [H31](#evidence-h31), [H33](#evidence-h33).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Hydrophobic sequence stretches can suggest membrane helices, but several listed choices differ in specific helix inclusion or exact endpoints; the sequence alone does not establish those precise boundaries reliably.


**Missing item-specific fact**

> The protein-specific transmembrane topology and annotated helix boundaries, supported here by structural and literature evidence, are not supplied in the question.


**Reason**

> Choosing the complete set and distinguishing close alternatives—especially the omitted or shifted intervals—depends on exact protein-specific annotation or structural knowledge, not merely the general tendency of membrane helices to be hydrophobic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, B matches the annotated transmembrane intervals. D corresponds roughly to an N-terminal intramembrane region, which is distinct from a segment that crosses the membrane.


### Important caveats

- The reviewer-only evidence establishes support for the key but was not available to the evaluated model.
- The matched historical entry is sequence-identical, but the author's exact source snapshot is unknown.
- Database feature annotations cite a paper and structures; they are not all equivalent to independent direct experimental measurements of each boundary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Hydrophobic sequence stretches can suggest membrane helices, but several listed choices differ in specific helix inclusion or exact endpoints; the sequence alone does not establish those precise boundaries reliably.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane topology and annotated helix boundaries, supported here by structural and literature evidence, are not supplied in the question.",
    "reason": "Choosing the complete set and distinguishing close alternatives—especially the omitted or shifted intervals—depends on exact protein-specific annotation or structural knowledge, not merely the general tendency of membrane helices to be hydrophobic."
  },
  "case_id": "transmembrane_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17",
      "H23",
      "H25",
      "H27",
      "H29",
      "H31",
      "H33"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1470-aa sequence in the historical UniProt entry. Its annotated transmembrane intervals match choice B, with cited experimental and PDB evidence for these features. The separate intramembrane regions are not annotated as membrane-spanning helices."
  },
  "important_caveats": [
    "The reviewer-only evidence establishes support for the key but was not available to the evaluated model.",
    "The matched historical entry is sequence-identical, but the author's exact source snapshot is unknown.",
    "Database feature annotations cite a paper and structures; they are not all equivalent to independent direct experimental measurements of each boundary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, B matches the annotated transmembrane intervals. D corresponds roughly to an N-terminal intramembrane region, which is distinct from a segment that crosses the membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1470-aa sequence in the historical UniProt entry. Its annotated transmembrane intervals match choice B, with cited experimental and PDB evidence for these features. The separate intramembrane regions are not annotated as membrane-spanning helices.",
    "evidence_ids": ["H7", "H9", "H11", "H13", "H15", "H17", "H23", "H25", "H27", "H29", "H31", "H33"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Hydrophobic sequence stretches can suggest membrane helices, but several listed choices differ in specific helix inclusion or exact endpoints; the sequence alone does not establish those precise boundaries reliably.",
    "missing_item_specific_fact": "The protein-specific transmembrane topology and annotated helix boundaries, supported here by structural and literature evidence, are not supplied in the question.",
    "reason": "Choosing the complete set and distinguishing close alternatives—especially the omitted or shifted intervals—depends on exact protein-specific annotation or structural knowledge, not merely the general tendency of membrane helices to be hydrophobic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, B matches the annotated transmembrane intervals. D corresponds roughly to an N-terminal intramembrane region, which is distinct from a segment that crosses the membrane."
  },
  "important_caveats": [
    "The reviewer-only evidence establishes support for the key but was not available to the evaluated model.",
    "The matched historical entry is sequence-identical, but the author's exact source snapshot is unknown.",
    "Database feature annotations cite a paper and structures; they are not all equivalent to independent direct experimental measurements of each boundary."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q8I266 (NCR1 transporter, Plasmodium falciparum, 1470 aa) lists exactly 12 transmembrane helices at positions 36..56, 494..514, 525..549, 555..582, 588..619, 623..659, 1075..1098, 1301..1334, 1338..1361, 1368..1394, 1400..1431, 1435..1466, all annotated as 'Helical' with experimental evidence from cryo-EM structures (PDB 8V0G, 8V12, 8V1G) and PubMed 39693420. Option B matches these coordinates exactly. Option A omits 555..582; option C shifts the 588..619 segment to 593..624; option D (13..35) corresponds to an intramembrane region, not a transmembrane helix.

Citations as saved: [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C24](#evidence-c24), [C26](#evidence-c26), [C28](#evidence-c28), [C30](#evidence-c30), [C32](#evidence-c32), [C34](#evidence-c34), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H23](#evidence-h23), [H25](#evidence-h25), [H27](#evidence-h27), [H29](#evidence-h29), [H31](#evidence-h31), [H33](#evidence-h33).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model scanning the 1470-residue sequence for hydrophobic stretches of ~20+ residues could plausibly identify the presence of a substantial hydrophobic segment around positions 555-582 (28 residues), thereby distinguishing B from A. However, distinguishing B from C requires resolving a 5-residue boundary shift (588..619 vs 593..624) for one helix. Transmembrane helix boundaries in the lipid bilayer are determined by the protein-lipid interface geometry, not solely by sequence hydrophobicity, making this 5-residue precision beyond reliable sequence-based inference.


**Missing item-specific fact**

> The exact N- and C-terminal boundaries of the transmembrane helix at ~588-619 as determined by cryo-EM structure (PDB 8V0G/8V12/8V1G, 2.98 Å resolution). The 5-residue shift between 588..619 and 593..624 falls within the uncertainty of hydrophobicity-based boundary prediction and cannot be resolved from sequence alone.


**Reason**

> While the general identification of transmembrane segments and the presence/absence of the 555..582 helix are amenable to hydrophobicity reasoning (distinguishing A from B), the precise boundary distinctions required to select B over C depend on item-specific structural data from cryo-EM experiments not derivable from the amino acid sequence. The correct answer requires exact knowledge of helix termini as measured experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D is clearly wrong (single segment, wrong type). Option A is missing a 28-residue hydrophobic segment. The B vs C distinction, while very fine, is resolved by experimental structural data. No two options are equally defensible given the full evidence.


### Important caveats

- The UniProt annotations derive from cryo-EM structures (2.98 Å) and are marked with ECO:0000269 (experimental) and ECO:0007744 (PDB), representing high-confidence experimental evidence rather than computational prediction.
- The benchmark sequence matches the UniProt entry exactly (SHA-256 confirmed), so coordinate numbering is consistent.
- The 5-residue boundary difference between B and C (588..619 vs 593..624) is within the typical error range of sequence-based TM predictors, making this distinction effectively impossible to resolve without structural data.
- The author's source snapshot is unknown; however, the historical entry (v124, released 2026-01-28) already contains these annotations, and the sequence has been unchanged since 2003.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model scanning the 1470-residue sequence for hydrophobic stretches of ~20+ residues could plausibly identify the presence of a substantial hydrophobic segment around positions 555-582 (28 residues), thereby distinguishing B from A. However, distinguishing B from C requires resolving a 5-residue boundary shift (588..619 vs 593..624) for one helix. Transmembrane helix boundaries in the lipid bilayer are determined by the protein-lipid interface geometry, not solely by sequence hydrophobicity, making this 5-residue precision beyond reliable sequence-based inference.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact N- and C-terminal boundaries of the transmembrane helix at ~588-619 as determined by cryo-EM structure (PDB 8V0G/8V12/8V1G, 2.98 Å resolution). The 5-residue shift between 588..619 and 593..624 falls within the uncertainty of hydrophobicity-based boundary prediction and cannot be resolved from sequence alone.",
    "reason": "While the general identification of transmembrane segments and the presence/absence of the 555..582 helix are amenable to hydrophobicity reasoning (distinguishing A from B), the precise boundary distinctions required to select B over C depend on item-specific structural data from cryo-EM experiments not derivable from the amino acid sequence. The correct answer requires exact knowledge of helix termini as measured experimentally."
  },
  "case_id": "transmembrane_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C24",
      "C26",
      "C28",
      "C30",
      "C32",
      "C34",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17",
      "H23",
      "H25",
      "H27",
      "H29",
      "H31",
      "H33"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8I266 (NCR1 transporter, Plasmodium falciparum, 1470 aa) lists exactly 12 transmembrane helices at positions 36..56, 494..514, 525..549, 555..582, 588..619, 623..659, 1075..1098, 1301..1334, 1338..1361, 1368..1394, 1400..1431, 1435..1466, all annotated as 'Helical' with experimental evidence from cryo-EM structures (PDB 8V0G, 8V12, 8V1G) and PubMed 39693420. Option B matches these coordinates exactly. Option A omits 555..582; option C shifts the 588..619 segment to 593..624; option D (13..35) corresponds to an intramembrane region, not a transmembrane helix."
  },
  "important_caveats": [
    "The UniProt annotations derive from cryo-EM structures (2.98 Å) and are marked with ECO:0000269 (experimental) and ECO:0007744 (PDB), representing high-confidence experimental evidence rather than computational prediction.",
    "The benchmark sequence matches the UniProt entry exactly (SHA-256 confirmed), so coordinate numbering is consistent.",
    "The 5-residue boundary difference between B and C (588..619 vs 593..624) is within the typical error range of sequence-based TM predictors, making this distinction effectively impossible to resolve without structural data.",
    "The author's source snapshot is unknown; however, the historical entry (v124, released 2026-01-28) already contains these annotations, and the sequence has been unchanged since 2003."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is clearly wrong (single segment, wrong type). Option A is missing a 28-residue hydrophobic segment. The B vs C distinction, while very fine, is resolved by experimental structural data. No two options are equally defensible given the full evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8I266 (NCR1 transporter, Plasmodium falciparum, 1470 aa) lists exactly 12 transmembrane helices at positions 36..56, 494..514, 525..549, 555..582, 588..619, 623..659, 1075..1098, 1301..1334, 1338..1361, 1368..1394, 1400..1431, 1435..1466, all annotated as 'Helical' with experimental evidence from cryo-EM structures (PDB 8V0G, 8V12, 8V1G) and PubMed 39693420. Option B matches these coordinates exactly. Option A omits 555..582; option C shifts the 588..619 segment to 593..624; option D (13..35) corresponds to an intramembrane region, not a transmembrane helix.",
    "evidence_ids": ["C8", "C10", "C12", "C14", "C16", "C18", "C24", "C26", "C28", "C30", "C32", "C34", "H7", "H9", "H11", "H13", "H15", "H17", "H23", "H25", "H27", "H29", "H31", "H33"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model scanning the 1470-residue sequence for hydrophobic stretches of ~20+ residues could plausibly identify the presence of a substantial hydrophobic segment around positions 555-582 (28 residues), thereby distinguishing B from A. However, distinguishing B from C requires resolving a 5-residue boundary shift (588..619 vs 593..624) for one helix. Transmembrane helix boundaries in the lipid bilayer are determined by the protein-lipid interface geometry, not solely by sequence hydrophobicity, making this 5-residue precision beyond reliable sequence-based inference.",
    "missing_item_specific_fact": "The exact N- and C-terminal boundaries of the transmembrane helix at ~588-619 as determined by cryo-EM structure (PDB 8V0G/8V12/8V1G, 2.98 Å resolution). The 5-residue shift between 588..619 and 593..624 falls within the uncertainty of hydrophobicity-based boundary prediction and cannot be resolved from sequence alone.",
    "reason": "While the general identification of transmembrane segments and the presence/absence of the 555..582 helix are amenable to hydrophobicity reasoning (distinguishing A from B), the precise boundary distinctions required to select B over C depend on item-specific structural data from cryo-EM experiments not derivable from the amino acid sequence. The correct answer requires exact knowledge of helix termini as measured experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is clearly wrong (single segment, wrong type). Option A is missing a 28-residue hydrophobic segment. The B vs C distinction, while very fine, is resolved by experimental structural data. No two options are equally defensible given the full evidence."
  },
  "important_caveats": [
    "The UniProt annotations derive from cryo-EM structures (2.98 Å) and are marked with ECO:0000269 (experimental) and ECO:0007744 (PDB), representing high-confidence experimental evidence rather than computational prediction.",
    "The benchmark sequence matches the UniProt entry exactly (SHA-256 confirmed), so coordinate numbering is consistent.",
    "The 5-residue boundary difference between B and C (588..619 vs 593..624) is within the typical error range of sequence-based TM predictors, making this distinction effectively impossible to resolve without structural data.",
    "The author's source snapshot is unknown; however, the historical entry (v124, released 2026-01-28) already contains these annotations, and the sequence has been unchanged since 2003."
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

**Accession:** `Q8I266` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 124. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":56},"start":{"modifier":"EXACT","value":36}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":514},"start":{"modifier":"EXACT","value":494}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":549},"start":{"modifier":"EXACT","value":525}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":582},"start":{"modifier":"EXACT","value":555}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":619},"start":{"modifier":"EXACT","value":588}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":659},"start":{"modifier":"EXACT","value":623}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":1098},"start":{"modifier":"EXACT","value":1075}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":1334},"start":{"modifier":"EXACT","value":1301}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/24`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":1361},"start":{"modifier":"EXACT","value":1338}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C30

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/26`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":1394},"start":{"modifier":"EXACT","value":1368}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C32

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/28`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":1431},"start":{"modifier":"EXACT","value":1400}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C34

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/features/30`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":1466},"start":{"modifier":"EXACT","value":1435}},"type":"Transmembrane"}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 156-160`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        36..56
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 164-168`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        494..514
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 172-176`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        525..549
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 180-184`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        555..582
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 188-192`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        588..619
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 196-200`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        623..659
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 218-222`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        1075..1098
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 226-230`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        1301..1334
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 234-238`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        1338..1361
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H29

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 242-246`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        1368..1394
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H31

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 250-254`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        1400..1431
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H33

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 258-262`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
FT   TRANSMEM        1435..1466
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:39693420,
FT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,
FT                   ECO:0007744|PDB:8V1G"
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 104. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
