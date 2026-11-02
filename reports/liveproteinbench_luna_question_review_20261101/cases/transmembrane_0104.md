# transmembrane_0104

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 36..56; 494..514; 525..549; 555..582; 588..619; 623..659; 1075..1098; 1301..1334; 1338..1361; 1368..1394; 1400..1431; 1435..1466

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

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

## Luna’s full visible review

### Expected-answer support: supported

> The supplied sequence exactly matches the 1470-aa sequence in the historical UniProt entry. Its annotated transmembrane intervals match choice B, with cited experimental and PDB evidence for these features. The separate intramembrane regions are not annotated as membrane-spanning helices.

Cited evidence: [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H23](#evidence-h23), [H25](#evidence-h25), [H27](#evidence-h27), [H29](#evidence-h29), [H31](#evidence-h31), [H33](#evidence-h33).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Hydrophobic sequence stretches can suggest membrane helices, but several listed choices differ in specific helix inclusion or exact endpoints; the sequence alone does not establish those precise boundaries reliably.

**Missing item-specific fact**

> The protein-specific transmembrane topology and annotated helix boundaries, supported here by structural and literature evidence, are not supplied in the question.

**Reason**

> Choosing the complete set and distinguishing close alternatives—especially the omitted or shifted intervals—depends on exact protein-specific annotation or structural knowledge, not merely the general tendency of membrane helices to be hydrophobic.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the choices, B matches the annotated transmembrane intervals. D corresponds roughly to an N-terminal intramembrane region, which is distinct from a segment that crosses the membrane.

### Important caveats

- The reviewer-only evidence establishes support for the key but was not available to the evaluated model.
- The matched historical entry is sequence-identical, but the author's exact source snapshot is unknown.
- Database feature annotations cite a paper and structures; they are not all equivalent to independent direct experimental measurements of each boundary.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1470-aa sequence in the historical UniProt entry. Its annotated transmembrane intervals match choice B, with cited experimental and PDB evidence for these features. The separate intramembrane regions are not annotated as membrane-spanning helices.",
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
    ]
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

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q8I266`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 124. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 104). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
