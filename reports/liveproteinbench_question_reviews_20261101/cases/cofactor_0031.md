# cofactor_0031

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATDTAVTGAPETMQLRLASGNGPVTRTVLRTPLRDALPSEVPLIDISPIFSTSVADRKAVACKIHDAATNIGFFYIQNHRVPSRDTDMAYSASLDFFRQDMEAKMKADAKKGPFDSGYRGPGTQRVNPDEGADLRETYSILYDPMLDPTVPDPARIPEPASRFLHLGRAPFESTDTLPHFKDAFVRYFQACLALARALTRTFALSLDLPESAFDSKVQYPDASLEINFYPPISTGHAVSAPADPDTRVSIGSHTDFLLFTILWQDSNGGLQVLNREGQWIRASPVEGTFVVNIGDYLQRITNDKYVSTVHRAQNWSGRQRVSMPFFWGFGMHESCQVLESCCGEDGKSKYDEVRCVDWVSRRLGNLFDLSDKG

[Multiple Choices]
A. FAD
B. pantetheine 4'-phosphate
C. tungstopterin
D. Fe(2+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates one Fe(2+) ion per subunit, based on a PROSITE-ProRule inference. It identifies the protein as a 2-oxoglutarate-Fe(II)-type oxidoreductase; the cited paper title also describes the PPZ enzymes as iron(II), alpha-ketoglutarate-dependent. This supports Fe(2+), though the cofactor annotation excerpt is computational rather than direct experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include Fe(2+), consistent with the broad class of 2-oxoglutarate-dependent enzymes, but the input gives no protein function or pathway context that establishes this sequence's enzyme class.


**Missing item-specific fact**

> The protein-specific identification as PPZC, a 2-oxoglutarate-Fe(II)-type oxidoreductase, or an equivalent annotation identifying its required cofactor.


**Reason**

> The reviewer-only annotation supports the key, but it was not supplied to the evaluated model. No sufficiently distinctive cofactor-determining motif or other sequence argument is established by the question itself; recognizing the exact sequence or consulting its entry would supply the needed fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied choices ask for a specific cofactor, and the sequence-matched annotation supports Fe(2+). The lack of context makes the answer lookup-dependent, but does not establish another listed choice as defensible.


### Important caveats

- The Fe(2+) cofactor annotation is attributed to a PROSITE-ProRule computational inference; the cited literature title is supportive context, not by itself proof of a direct cofactor measurement.
- Reviewer-only sources establish support for the key and were absent from the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include Fe(2+), consistent with the broad class of 2-oxoglutarate-dependent enzymes, but the input gives no protein function or pathway context that establishes this sequence's enzyme class.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as PPZC, a 2-oxoglutarate-Fe(II)-type oxidoreductase, or an equivalent annotation identifying its required cofactor.",
    "reason": "The reviewer-only annotation supports the key, but it was not supplied to the evaluated model. No sufficiently distinctive cofactor-determining motif or other sequence argument is established by the question itself; recognizing the exact sequence or consulting its entry would supply the needed fact."
  },
  "case_id": "cofactor_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates one Fe(2+) ion per subunit, based on a PROSITE-ProRule inference. It identifies the protein as a 2-oxoglutarate-Fe(II)-type oxidoreductase; the cited paper title also describes the PPZ enzymes as iron(II), alpha-ketoglutarate-dependent. This supports Fe(2+), though the cofactor annotation excerpt is computational rather than direct experimental evidence."
  },
  "important_caveats": [
    "The Fe(2+) cofactor annotation is attributed to a PROSITE-ProRule computational inference; the cited literature title is supportive context, not by itself proof of a direct cofactor measurement.",
    "Reviewer-only sources establish support for the key and were absent from the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied choices ask for a specific cofactor, and the sequence-matched annotation supports Fe(2+). The lack of context makes the answer lookup-dependent, but does not establish another listed choice as defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates one Fe(2+) ion per subunit, based on a PROSITE-ProRule inference. It identifies the protein as a 2-oxoglutarate-Fe(II)-type oxidoreductase; the cited paper title also describes the PPZ enzymes as iron(II), alpha-ketoglutarate-dependent. This supports Fe(2+), though the cofactor annotation excerpt is computational rather than direct experimental evidence.",
    "evidence_ids": ["C4", "C5", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include Fe(2+), consistent with the broad class of 2-oxoglutarate-dependent enzymes, but the input gives no protein function or pathway context that establishes this sequence's enzyme class.",
    "missing_item_specific_fact": "The protein-specific identification as PPZC, a 2-oxoglutarate-Fe(II)-type oxidoreductase, or an equivalent annotation identifying its required cofactor.",
    "reason": "The reviewer-only annotation supports the key, but it was not supplied to the evaluated model. No sufficiently distinctive cofactor-determining motif or other sequence argument is established by the question itself; recognizing the exact sequence or consulting its entry would supply the needed fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied choices ask for a specific cofactor, and the sequence-matched annotation supports Fe(2+). The lack of context makes the answer lookup-dependent, but does not establish another listed choice as defensible."
  },
  "important_caveats": [
    "The Fe(2+) cofactor annotation is attributed to a PROSITE-ProRule computational inference; the cited literature title is supportive context, not by itself proof of a direct cofactor measurement.",
    "Reviewer-only sources establish support for the key and were absent from the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A455ZKR7 (PPZC_METMF) matches the supplied 374-aa sequence exactly. The protein is named '2-oxoglutarate-Fe(II) type oxidoreductase ppzC' with EC 1.14.11.- assigned under experimental evidence (ECO:0000269, PubMed:38578094, JACS 2024). The COFACTOR comment explicitly lists Fe(2+) (ChEBI:29033), noting 'Binds 1 Fe(2+) ion per subunit.' The 2024 JACS paper title itself states 'Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes…', providing direct experimental confirmation of Fe(II) dependence. The cofactor annotation line uses ECO:0000255 (PROSITE-ProRule PRU00805), a protein-rule-based code, but the 2-OG/Fe(II) oxidoreductase family's Fe(II) requirement is among the most firmly established facts in biochemistry, and the experimental paper independently confirms it.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several general biochemical arguments distinguish D from A, B, and C. (1) The sequence lacks any recognizable FAD-binding Rossmann-fold motif (no GxGxxG or similar dinucleotide-binding pattern), making FAD unlikely. (2) There are no acyl-carrier-protein or pantetheine-4'-phosphate-binding motifs (no conserved Ser-ACP or ACP helix), ruling out B. (3) There are no tungsten/pterin-specific motifs (no Cys-rich tungstopterin clusters, no Mo/W-bisPGD signature), ruling out C. (4) The sequence contains multiple His residues including an H-D-A pattern near position 45 ('IHDAAT') and additional His residues in the C-terminal half (e.g., 'HRA', 'HES'), consistent with the 2-His-1-carboxylate facial triad (H-X-D/E…H) that coordinates Fe(II) in the 2-oxoglutarate/Fe(II) oxidoreductase superfamily. (5) The protein is 374 aa, within the typical size range for 2-OG/Fe(II) enzymes, and is from a fungal secondary-metabolite biosynthetic gene cluster, a context in which 2-OG/Fe(II) oxidoreductases are extremely common. Together, motif elimination and the facial-triad pattern provide a defensible reasoning path to Fe(2+).


**Missing item-specific fact**

> Precise identification of the HxD/E…H facial triad residues and their spacing in this specific 374-aa sequence is non-trivial from raw sequence alone; the exact register of the 2-His-1-carboxylate triad in ppzC is not trivially obvious without alignment to characterized 2-OG/Fe(II) family members. However, the broader argument (absence of FAD/pantetheine/tungstopterin motifs, presence of His-rich regions, fungal BGC context) is available from general biochemical knowledge.


**Reason**

> The question can be addressed through elimination of three options based on absent cofactor-binding motifs and positive identification of features consistent with the 2-OG/Fe(II) facial triad. While pinpointing the exact triad residues in a raw sequence is challenging, the combination of motif absence (FAD, pantetheine, tungstopterin) and motif presence (HxD/E…H pattern, His-rich C-terminal region, fungal BGC context) constitutes a meaningful biological reasoning chain rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent cofactors from structurally and functionally distinct enzyme classes (flavoprotein oxidoreductase, acyltransferase/ACP pathway, tungsten aldehyde oxidoreductase, 2-OG/Fe(II) oxidoreductase). The sequence lacks motifs diagnostic of A, B, or C, and contains features consistent with D. No other option is defensible for this sequence.


### Important caveats

- The UniProt COFACTOR annotation uses ECO:0000255 (PROSITE-ProRule), a computational/protein-rule evidence code, not direct experimental measurement of Fe(II) binding to this specific protein. However, the protein's assignment to the 2-OG/Fe(II) oxidoreductase family is backed by experimental evidence (ECO:0000269, JACS 2024), and Fe(II) is the obligate cofactor of this superfamily.
- The reviewer-only UniProt accession and annotations were not available to the evaluated model; the model must reason from the raw sequence and general biochemistry.
- Identifying the 2-His-1-carboxylate facial triad from a 374-residue sequence without alignment tools is the most demanding step in the reasoning chain and may not be reliably performed by all models.
- The sequence-match is confirmed (SHA-256 identical) between the benchmark input and both the current and historical (entry version 21) UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several general biochemical arguments distinguish D from A, B, and C. (1) The sequence lacks any recognizable FAD-binding Rossmann-fold motif (no GxGxxG or similar dinucleotide-binding pattern), making FAD unlikely. (2) There are no acyl-carrier-protein or pantetheine-4'-phosphate-binding motifs (no conserved Ser-ACP or ACP helix), ruling out B. (3) There are no tungsten/pterin-specific motifs (no Cys-rich tungstopterin clusters, no Mo/W-bisPGD signature), ruling out C. (4) The sequence contains multiple His residues including an H-D-A pattern near position 45 ('IHDAAT') and additional His residues in the C-terminal half (e.g., 'HRA', 'HES'), consistent with the 2-His-1-carboxylate facial triad (H-X-D/E…H) that coordinates Fe(II) in the 2-oxoglutarate/Fe(II) oxidoreductase superfamily. (5) The protein is 374 aa, within the typical size range for 2-OG/Fe(II) enzymes, and is from a fungal secondary-metabolite biosynthetic gene cluster, a context in which 2-OG/Fe(II) oxidoreductases are extremely common. Together, motif elimination and the facial-triad pattern provide a defensible reasoning path to Fe(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the HxD/E…H facial triad residues and their spacing in this specific 374-aa sequence is non-trivial from raw sequence alone; the exact register of the 2-His-1-carboxylate triad in ppzC is not trivially obvious without alignment to characterized 2-OG/Fe(II) family members. However, the broader argument (absence of FAD/pantetheine/tungstopterin motifs, presence of His-rich regions, fungal BGC context) is available from general biochemical knowledge.",
    "reason": "The question can be addressed through elimination of three options based on absent cofactor-binding motifs and positive identification of features consistent with the 2-OG/Fe(II) facial triad. While pinpointing the exact triad residues in a raw sequence is challenging, the combination of motif absence (FAD, pantetheine, tungstopterin) and motif presence (HxD/E…H pattern, His-rich C-terminal region, fungal BGC context) constitutes a meaningful biological reasoning chain rather than pure lookup."
  },
  "case_id": "cofactor_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A455ZKR7 (PPZC_METMF) matches the supplied 374-aa sequence exactly. The protein is named '2-oxoglutarate-Fe(II) type oxidoreductase ppzC' with EC 1.14.11.- assigned under experimental evidence (ECO:0000269, PubMed:38578094, JACS 2024). The COFACTOR comment explicitly lists Fe(2+) (ChEBI:29033), noting 'Binds 1 Fe(2+) ion per subunit.' The 2024 JACS paper title itself states 'Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes…', providing direct experimental confirmation of Fe(II) dependence. The cofactor annotation line uses ECO:0000255 (PROSITE-ProRule PRU00805), a protein-rule-based code, but the 2-OG/Fe(II) oxidoreductase family's Fe(II) requirement is among the most firmly established facts in biochemistry, and the experimental paper independently confirms it."
  },
  "important_caveats": [
    "The UniProt COFACTOR annotation uses ECO:0000255 (PROSITE-ProRule), a computational/protein-rule evidence code, not direct experimental measurement of Fe(II) binding to this specific protein. However, the protein's assignment to the 2-OG/Fe(II) oxidoreductase family is backed by experimental evidence (ECO:0000269, JACS 2024), and Fe(II) is the obligate cofactor of this superfamily.",
    "The reviewer-only UniProt accession and annotations were not available to the evaluated model; the model must reason from the raw sequence and general biochemistry.",
    "Identifying the 2-His-1-carboxylate facial triad from a 374-residue sequence without alignment tools is the most demanding step in the reasoning chain and may not be reliably performed by all models.",
    "The sequence-match is confirmed (SHA-256 identical) between the benchmark input and both the current and historical (entry version 21) UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent cofactors from structurally and functionally distinct enzyme classes (flavoprotein oxidoreductase, acyltransferase/ACP pathway, tungsten aldehyde oxidoreductase, 2-OG/Fe(II) oxidoreductase). The sequence lacks motifs diagnostic of A, B, or C, and contains features consistent with D. No other option is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A455ZKR7 (PPZC_METMF) matches the supplied 374-aa sequence exactly. The protein is named '2-oxoglutarate-Fe(II) type oxidoreductase ppzC' with EC 1.14.11.- assigned under experimental evidence (ECO:0000269, PubMed:38578094, JACS 2024). The COFACTOR comment explicitly lists Fe(2+) (ChEBI:29033), noting 'Binds 1 Fe(2+) ion per subunit.' The 2024 JACS paper title itself states 'Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes…', providing direct experimental confirmation of Fe(II) dependence. The cofactor annotation line uses ECO:0000255 (PROSITE-ProRule PRU00805), a protein-rule-based code, but the 2-OG/Fe(II) oxidoreductase family's Fe(II) requirement is among the most firmly established facts in biochemistry, and the experimental paper independently confirms it.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several general biochemical arguments distinguish D from A, B, and C. (1) The sequence lacks any recognizable FAD-binding Rossmann-fold motif (no GxGxxG or similar dinucleotide-binding pattern), making FAD unlikely. (2) There are no acyl-carrier-protein or pantetheine-4'-phosphate-binding motifs (no conserved Ser-ACP or ACP helix), ruling out B. (3) There are no tungsten/pterin-specific motifs (no Cys-rich tungstopterin clusters, no Mo/W-bisPGD signature), ruling out C. (4) The sequence contains multiple His residues including an H-D-A pattern near position 45 ('IHDAAT') and additional His residues in the C-terminal half (e.g., 'HRA', 'HES'), consistent with the 2-His-1-carboxylate facial triad (H-X-D/E…H) that coordinates Fe(II) in the 2-oxoglutarate/Fe(II) oxidoreductase superfamily. (5) The protein is 374 aa, within the typical size range for 2-OG/Fe(II) enzymes, and is from a fungal secondary-metabolite biosynthetic gene cluster, a context in which 2-OG/Fe(II) oxidoreductases are extremely common. Together, motif elimination and the facial-triad pattern provide a defensible reasoning path to Fe(2+).",
    "missing_item_specific_fact": "Precise identification of the HxD/E…H facial triad residues and their spacing in this specific 374-aa sequence is non-trivial from raw sequence alone; the exact register of the 2-His-1-carboxylate triad in ppzC is not trivially obvious without alignment to characterized 2-OG/Fe(II) family members. However, the broader argument (absence of FAD/pantetheine/tungstopterin motifs, presence of His-rich regions, fungal BGC context) is available from general biochemical knowledge.",
    "reason": "The question can be addressed through elimination of three options based on absent cofactor-binding motifs and positive identification of features consistent with the 2-OG/Fe(II) facial triad. While pinpointing the exact triad residues in a raw sequence is challenging, the combination of motif absence (FAD, pantetheine, tungstopterin) and motif presence (HxD/E…H pattern, His-rich C-terminal region, fungal BGC context) constitutes a meaningful biological reasoning chain rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent cofactors from structurally and functionally distinct enzyme classes (flavoprotein oxidoreductase, acyltransferase/ACP pathway, tungsten aldehyde oxidoreductase, 2-OG/Fe(II) oxidoreductase). The sequence lacks motifs diagnostic of A, B, or C, and contains features consistent with D. No other option is defensible for this sequence."
  },
  "important_caveats": [
    "The UniProt COFACTOR annotation uses ECO:0000255 (PROSITE-ProRule), a computational/protein-rule evidence code, not direct experimental measurement of Fe(II) binding to this specific protein. However, the protein's assignment to the 2-OG/Fe(II) oxidoreductase family is backed by experimental evidence (ECO:0000269, JACS 2024), and Fe(II) is the obligate cofactor of this superfamily.",
    "The reviewer-only UniProt accession and annotations were not available to the evaluated model; the model must reason from the raw sequence and general biochemistry.",
    "Identifying the 2-His-1-carboxylate facial triad from a 374-residue sequence without alignment tools is the most demanding step in the reasoning chain and may not be reliably performed by all models.",
    "The sequence-match is confirmed (SHA-256 identical) between the benchmark input and both the current and historical (entry version 21) UniProt records."
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

**Accession:** `A0A455ZKR7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 21. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.380201+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"Pyrrolopyrazine biosynthesis cluster protein C"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"value":"1.14.11.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"2-oxoglutarate-Fe(II) type oxidoreductase ppzC"}}}
```

Source SHA-256: `6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.380201+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29033"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00805","source":"PROSITE-ProRule"}],"name":"Fe(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00805","source":"PROSITE-ProRule"}],"value":"Binds 1 Fe(2+) ion per subunit."}]}}
```

Source SHA-256: `6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.380201+00:00.  

```json
{"citation":{"authors":["Rothchild K.W.","Hagar M.","Berry D.","Ryan K.S."],"citationCrossReferences":[{"database":"PubMed","id":"38578094"},{"database":"DOI","id":"10.1021/jacs.4c01419"}],"citationType":"journal article","firstPage":"10263","id":"38578094","journal":"J. Am. Chem. Soc.","lastPage":"10267","publicationDate":"2024","title":"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.","volume":"146"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:18.441147+00:00.  

```text
DE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzC {ECO:0000303|PubMed:30452111};
DE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};
DE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein C {ECO:0000303|PubMed:30452111};
```

Source SHA-256: `a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)  
**Locator:** `lines 24-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:18.441147+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RX   PubMed=38578094; DOI=10.1021/jacs.4c01419;
RA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;
RT   "Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ
RT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.";
RL   J. Am. Chem. Soc. 146:10263-10267(2024).
```

Source SHA-256: `a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)  
**Locator:** `lines 58-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:18.441147+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00805};
CC       Note=Binds 1 Fe(2+) ion per subunit. {ECO:0000255|PROSITE-
CC       ProRule:PRU00805};
```

Source SHA-256: `a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 31. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
