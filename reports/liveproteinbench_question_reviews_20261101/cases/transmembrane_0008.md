# transmembrane_0008

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 157..177; 412..432; 448..468; 478..498; 516..536; 545..565; 789..809; 986..1006; 1013..1033; 1037..1057; 1080..1100; 1114..1134

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEKNCNSVAGHAGTLVKASSRQADDKAGSRVPPGGHLLQTNKTESQLLPCASPSDPVHWTNEIVPVVADTSAPAEAAPDQTVSDGEQLTRAPDETYYQRSESLAEPPAENELPAGRSRRRRSRWCLGCGCFEQVKTVVLRMLMTGFEKYAGVVYDHPWLFIMVSLLATAGMSVGIFLRTPESDVYTLYSLSGSPSQVTKEHLLDVLPPDRLLFVLLTGTSNLVTRETVTRIDSLLQGIESITLRRDSVTTDEFNHRLVSHDRSPFPETITFQDICAKDGSGKCQVQSILDLYPSSSAWGVMPIASASWPVVTNPVTHKVSRLDAILGKITTSVRLAEQGSGRPALTVVEEAEAMLMRIDLRGETIWKPYTAAFEKLVLDYVLGQDFGPDISVTAKAERSSYDELKRVSTLDVVEWLRLCAAVLVVFLYTSVVNSSKTHRTKLVPSAMGALASLLGYLGGAGLVYLCGVRHTTPAEATPFLAIGIGVDDLFVIINAYSLTYLHPNPKERVVDAIRDAGLSITITTLTNVITFIIGALSPYYSISMFCIITAGALTWGYVLCLTFFLAGLSLDARREARKEPLSYSLFWRFMPRCCRKSSYEPQLSPPLPLTAAASGLEEMRNESEEIVTADQTPPTHGGDLLTTYQLAALMVLYKKHTCQSRSSQPARRLFDRRDGTGTEETMSTPVPEDSERDRTNQKSCGTQVSTGIVDVRETGQDAASQRRLSSHIRDMTTQESIMLLKNFEKEMEQNPEKLLKLYHPEPLGNPGRGSRRFFRDYYGRFLGNTFVKATVLVIFAAVTALAIYGATTLKFGLSLKNITPQASYLRDFYSLHEDLFPSYGDEVTVFFAENDRWEDREVQMRYLQMVKELSEQEWAVVVTDGMSLFLQHAMPSLHSGNRKEFLALLKTWLEGDPIGQNFSTFFKFSFDNLIVWQFRYWMPHRDNTTTLYYWLKEGKDIVSAGKPYFHGEVHTALAVIWESDPKILPFTLTNLSIALVCILAISLLLIPDLTSAIIVVLVVSLVDLWLFGFMALIDLPLSMISMVNLLISIGYSVDFTIHVAHTFTHCVGASRKDRMVETMIVMGAPVTHGMLSTLLSILALAGSPKYILEVFFKMMFMVIVFAYTAGMVLLPVVLTLLGPFHPHGKRESGKAIACDSSAQLIDMEPLHGTGKEEHGVGV

[Multiple Choices]
A. 157..177; 412..432; 448..468; 478..498; 516..536; 545..565; 789..809; 986..1006; 1013..1033; 1037..1057; 1080..1100; 1114..1134
B. 157..177; 412..432; 448..468; 478..498; 516..536; 545..565; 789..809; 988..1007; 1013..1033; 1037..1057; 1080..1100; 1114..1134
C. 308..328; 344..364; 474..494; 533..553; 640..660; 670..690; 731..751; 771..791; 807..827; 851..871; 937..957; 1162..1182; 1209..1229; 1244..1264; 1306..1326; 1381..1401; 1422..1442; 1498..1518; 1532..1552; 1561..1581; 1633..1653; 1671..1691; 1722..1742
D. 157..177; 448..468; 478..498; 516..536; 545..565; 789..809; 986..1006; 1013..1033; 1037..1057; 1080..1100; 1114..1134
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

> The exact supplied sequence matches the UniProt record, whose transmembrane feature annotations match every interval in A. These annotations carry ECO:0000255, indicating computational evidence rather than direct experimental determination.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Hydrophobic sequence stretches can support identifying likely membrane-spanning segments, but sequence-based reasoning does not establish the exact annotated endpoints of every helix.


**Missing item-specific fact**

> The protein-specific transmembrane assignments and their precise coordinates; in particular, whether the helix near residue 1000 is annotated as 986..1006 or 988..1007.


**Reason**

> The choices require a complete set of protein-specific intervals, including fine boundary distinctions that are not determined by general membrane biology alone. The reviewer-only annotation supports A but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A and B list the same putative transmembrane segments except for a two-residue shift in the interval near 1000. Both intervals overlap the same likely membrane-spanning helix, so the wording does not explain why one boundary convention should be preferred.


### Important caveats

- The supporting UniProt feature annotations are computationally evidenced (ECO:0000255), not established here as experimental measurements.
- The source sequence matches exactly, but the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Hydrophobic sequence stretches can support identifying likely membrane-spanning segments, but sequence-based reasoning does not establish the exact annotated endpoints of every helix.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane assignments and their precise coordinates; in particular, whether the helix near residue 1000 is annotated as 986..1006 or 988..1007.",
    "reason": "The choices require a complete set of protein-specific intervals, including fine boundary distinctions that are not determined by general membrane biology alone. The reviewer-only annotation supports A but was not supplied to the evaluated model."
  },
  "case_id": "transmembrane_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15",
      "C16"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt record, whose transmembrane feature annotations match every interval in A. These annotations carry ECO:0000255, indicating computational evidence rather than direct experimental determination."
  },
  "important_caveats": [
    "The supporting UniProt feature annotations are computationally evidenced (ECO:0000255), not established here as experimental measurements.",
    "The source sequence matches exactly, but the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A and B list the same putative transmembrane segments except for a two-residue shift in the interval near 1000. Both intervals overlap the same likely membrane-spanning helix, so the wording does not explain why one boundary convention should be preferred."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt record, whose transmembrane feature annotations match every interval in A. These annotations carry ECO:0000255, indicating computational evidence rather than direct experimental determination.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Hydrophobic sequence stretches can support identifying likely membrane-spanning segments, but sequence-based reasoning does not establish the exact annotated endpoints of every helix.",
    "missing_item_specific_fact": "The protein-specific transmembrane assignments and their precise coordinates; in particular, whether the helix near residue 1000 is annotated as 986..1006 or 988..1007.",
    "reason": "The choices require a complete set of protein-specific intervals, including fine boundary distinctions that are not determined by general membrane biology alone. The reviewer-only annotation supports A but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A and B list the same putative transmembrane segments except for a two-residue shift in the interval near 1000. Both intervals overlap the same likely membrane-spanning helix, so the wording does not explain why one boundary convention should be preferred."
  },
  "important_caveats": [
    "The supporting UniProt feature annotations are computationally evidenced (ECO:0000255), not established here as experimental measurements.",
    "The source sequence matches exactly, but the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A125YWU9 (NCR1_TOXGM, Toxoplasma gondii NPC1-related protein, 1178 AA) lists exactly 12 transmembrane helical regions at positions 157-177, 412-432, 448-468, 478-498, 516-536, 545-565, 789-809, 986-1006, 1013-1033, 1037-1057, 1080-1100, and 1114-1134, matching Choice A exactly. The sequence in the question matches the UniProt entry (SHA256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational/homology-based predictions rather than experimental measurements.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice C can be eliminated by reasoning: it lists TM positions (e.g., 1209, 1306, 1381, 1422, 1498, 1532, 1561, 1633, 1671, 1722) that exceed the 1178-residue protein length, making it physically impossible. Choice D (missing 412-432) could potentially be distinguished from A by verifying a hydrophobic 21-residue stretch at that position. However, the critical A vs B distinction (986..1006 vs 988..1007, a 2-residue shift in one TM helix) cannot be reliably resolved by general biological reasoning, as both are valid 21-residue hydrophobic segments and the exact boundary is an algorithmic annotation choice.


**Missing item-specific fact**

> The exact 2-residue boundary annotation for the TM region near position 986-1007 (whether UniProt records it as 986..1006 or 988..1007), which is a computational prediction artifact from the similarity-based annotation pipeline (ECO:0000255) rather than an experimentally determined boundary.


**Reason**

> While C is eliminable by length reasoning and D is potentially checkable by hydrophobicity inspection, the final A vs B choice hinges on a 2-residue annotation boundary that is within the uncertainty of any TM prediction algorithm. The ECO:0000255 evidence code confirms these boundaries are homology-inferred predictions, not experimental measurements. Distinguishing 986..1006 from 988..1007 requires knowing the specific database annotation rather than applying general biological principles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The only difference between A and B is a 2-residue shift in one TM helix (986..1006 vs 988..1007). Both represent valid hydrophobic transmembrane segments of identical length (21 residues). Given that the annotation evidence code is ECO:0000255 (similarity-based inference), the exact boundary is an algorithmic convention rather than a physically determined fact. A competent TM prediction tool might assign either boundary depending on its scoring function.


### Important caveats

- All 12 TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.
- The protein is TgNCR1 (Niemann-Pick type C1-related protein) from Toxoplasma gondii, a 12-TM protein related to human NPC1 (13 TM). The number 12 is biologically consistent with the NPC1/Patched family.
- Choice C's positions exceeding 1178 AA make it trivially eliminable, reducing the effective choice to A vs B vs D.
- The 2-residue difference between A and B is within the typical uncertainty range of TM prediction tools and does not reflect a meaningful biological distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice C can be eliminated by reasoning: it lists TM positions (e.g., 1209, 1306, 1381, 1422, 1498, 1532, 1561, 1633, 1671, 1722) that exceed the 1178-residue protein length, making it physically impossible. Choice D (missing 412-432) could potentially be distinguished from A by verifying a hydrophobic 21-residue stretch at that position. However, the critical A vs B distinction (986..1006 vs 988..1007, a 2-residue shift in one TM helix) cannot be reliably resolved by general biological reasoning, as both are valid 21-residue hydrophobic segments and the exact boundary is an algorithmic annotation choice.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact 2-residue boundary annotation for the TM region near position 986-1007 (whether UniProt records it as 986..1006 or 988..1007), which is a computational prediction artifact from the similarity-based annotation pipeline (ECO:0000255) rather than an experimentally determined boundary.",
    "reason": "While C is eliminable by length reasoning and D is potentially checkable by hydrophobicity inspection, the final A vs B choice hinges on a 2-residue annotation boundary that is within the uncertainty of any TM prediction algorithm. The ECO:0000255 evidence code confirms these boundaries are homology-inferred predictions, not experimental measurements. Distinguishing 986..1006 from 988..1007 requires knowing the specific database annotation rather than applying general biological principles."
  },
  "case_id": "transmembrane_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15",
      "C16",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A125YWU9 (NCR1_TOXGM, Toxoplasma gondii NPC1-related protein, 1178 AA) lists exactly 12 transmembrane helical regions at positions 157-177, 412-432, 448-468, 478-498, 516-536, 545-565, 789-809, 986-1006, 1013-1033, 1037-1057, 1080-1100, and 1114-1134, matching Choice A exactly. The sequence in the question matches the UniProt entry (SHA256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational/homology-based predictions rather than experimental measurements."
  },
  "important_caveats": [
    "All 12 TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.",
    "The protein is TgNCR1 (Niemann-Pick type C1-related protein) from Toxoplasma gondii, a 12-TM protein related to human NPC1 (13 TM). The number 12 is biologically consistent with the NPC1/Patched family.",
    "Choice C's positions exceeding 1178 AA make it trivially eliminable, reducing the effective choice to A vs B vs D.",
    "The 2-residue difference between A and B is within the typical uncertainty range of TM prediction tools and does not reflect a meaningful biological distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The only difference between A and B is a 2-residue shift in one TM helix (986..1006 vs 988..1007). Both represent valid hydrophobic transmembrane segments of identical length (21 residues). Given that the annotation evidence code is ECO:0000255 (similarity-based inference), the exact boundary is an algorithmic convention rather than a physically determined fact. A competent TM prediction tool might assign either boundary depending on its scoring function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A125YWU9 (NCR1_TOXGM, Toxoplasma gondii NPC1-related protein, 1178 AA) lists exactly 12 transmembrane helical regions at positions 157-177, 412-432, 448-468, 478-498, 516-536, 545-565, 789-809, 986-1006, 1013-1033, 1037-1057, 1080-1100, and 1114-1134, matching Choice A exactly. The sequence in the question matches the UniProt entry (SHA256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational/homology-based predictions rather than experimental measurements.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","C16","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13","H14"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice C can be eliminated by reasoning: it lists TM positions (e.g., 1209, 1306, 1381, 1422, 1498, 1532, 1561, 1633, 1671, 1722) that exceed the 1178-residue protein length, making it physically impossible. Choice D (missing 412-432) could potentially be distinguished from A by verifying a hydrophobic 21-residue stretch at that position. However, the critical A vs B distinction (986..1006 vs 988..1007, a 2-residue shift in one TM helix) cannot be reliably resolved by general biological reasoning, as both are valid 21-residue hydrophobic segments and the exact boundary is an algorithmic annotation choice.",
    "missing_item_specific_fact": "The exact 2-residue boundary annotation for the TM region near position 986-1007 (whether UniProt records it as 986..1006 or 988..1007), which is a computational prediction artifact from the similarity-based annotation pipeline (ECO:0000255) rather than an experimentally determined boundary.",
    "reason": "While C is eliminable by length reasoning and D is potentially checkable by hydrophobicity inspection, the final A vs B choice hinges on a 2-residue annotation boundary that is within the uncertainty of any TM prediction algorithm. The ECO:0000255 evidence code confirms these boundaries are homology-inferred predictions, not experimental measurements. Distinguishing 986..1006 from 988..1007 requires knowing the specific database annotation rather than applying general biological principles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The only difference between A and B is a 2-residue shift in one TM helix (986..1006 vs 988..1007). Both represent valid hydrophobic transmembrane segments of identical length (21 residues). Given that the annotation evidence code is ECO:0000255 (similarity-based inference), the exact boundary is an algorithmic convention rather than a physically determined fact. A competent TM prediction tool might assign either boundary depending on its scoring function."
  },
  "important_caveats": [
    "All 12 TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.",
    "The protein is TgNCR1 (Niemann-Pick type C1-related protein) from Toxoplasma gondii, a 12-TM protein related to human NPC1 (13 TM). The number 12 is biologically consistent with the NPC1/Patched family.",
    "Choice C's positions exceeding 1178 AA make it trivially eliminable, reducing the effective choice to A vs B vs D.",
    "The 2-residue difference between A and B is within the typical uncertainty range of TM prediction tools and does not reflect a meaningful biological distinction."
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

**Accession:** `A0A125YWU9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
"A0A125YWU9"
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":177},"start":{"modifier":"EXACT","value":157}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":432},"start":{"modifier":"EXACT","value":412}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":468},"start":{"modifier":"EXACT","value":448}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":498},"start":{"modifier":"EXACT","value":478}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":536},"start":{"modifier":"EXACT","value":516}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":565},"start":{"modifier":"EXACT","value":545}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":809},"start":{"modifier":"EXACT","value":789}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1006},"start":{"modifier":"EXACT","value":986}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1033},"start":{"modifier":"EXACT","value":1013}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1057},"start":{"modifier":"EXACT","value":1037}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1100},"start":{"modifier":"EXACT","value":1080}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.732042+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1134},"start":{"modifier":"EXACT","value":1114}},"type":"Transmembrane"}
```

Source SHA-256: `4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        157..177
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 92-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        412..432
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 95-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        448..468
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        478..498
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 101-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        516..536
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 104-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        545..565
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        789..809
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        986..1006
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 113-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        1013..1033
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 116-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        1037..1057
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        1080..1100
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)  
**Locator:** `lines 122-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:27:21.678924+00:00.  

```text
FT   TRANSMEM        1114..1134
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 8. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
