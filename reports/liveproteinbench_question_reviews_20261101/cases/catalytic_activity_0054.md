# catalytic_activity_0054

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — inosine(in) + H(+)(in) = inosine(out) + H(+)(out)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTGQSAAVEGSNSALPWYRMGFHTLAEFNTYVTFVLLGMSIMMVTSAVTSAPDFVTKYFIYATGDPDAVAETPLFWNNANTFYNAGTYAMQVVTEIASLTPFMRSIPLGIRLFLGLGIPFVELVVIIAVPAATIPTQNGAIAVIMVVAMMGGLSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALFMSIIQIILQVSMGSTFQDVLTISRIYFGIGIGIQVMAIAALVLLRYNPFAQKYIAEFRAAALRRRGHVEPEESQDSKEPATGDVAEAPKAGEKEVTLDAMEEADEVRAVPSDAFVAKSGAVLQATGDADRMVDLDQTKNITSTEQMLRASVWSVFKRIYPMLLCAFTIFFTTLLVFPGVFFLVPARSGWYMTIIVTLFNAGDFVARVLLMIRVLRPSPKLVIVGTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITLTY

[Multiple Choices]
A. inosine(in) + H(+)(in) = inosine(out) + H(+)(out)
B. selenite + a quinone + H2O = selenate + a quinol
C. aminoacetaldehyde + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + glycine + 3 H(+)
D. 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence matches the Leishmania donovani nucleoside transporter entry, which annotates inosine transport coupled to proton transport with experimental evidence codes citing multiple publications.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C5](#evidence-c5), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic, multipass sequence is consistent with a membrane transporter, favoring the transport-type choice over the enzyme reactions in B–D. But that broad inference does not identify inosine as the substrate or establish proton coupling.


**Missing item-specific fact**

> That this particular transporter transports inosine together with H+.


**Reason**

> Selecting A's precise reaction requires protein-specific functional information absent from the sequence and choices; recognizing or retrieving the protein annotation would supply it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is supported for the asked reaction among the listed options; the other choices describe distinct chemical transformations.


### Important caveats

- The supporting annotation is linked to experimental evidence, but the reviewer-only database and literature information was not supplied to the evaluated model.
- The sequence match establishes source applicability, not that the model could infer the specific substrate from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic, multipass sequence is consistent with a membrane transporter, favoring the transport-type choice over the enzyme reactions in B–D. But that broad inference does not identify inosine as the substrate or establish proton coupling.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular transporter transports inosine together with H+.",
    "reason": "Selecting A's precise reaction requires protein-specific functional information absent from the sequence and choices; recognizing or retrieving the protein annotation would supply it."
  },
  "case_id": "catalytic_activity_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C5",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Leishmania donovani nucleoside transporter entry, which annotates inosine transport coupled to proton transport with experimental evidence codes citing multiple publications."
  },
  "important_caveats": [
    "The supporting annotation is linked to experimental evidence, but the reviewer-only database and literature information was not supplied to the evaluated model.",
    "The sequence match establishes source applicability, not that the model could infer the specific substrate from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is supported for the asked reaction among the listed options; the other choices describe distinct chemical transformations."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Leishmania donovani nucleoside transporter entry, which annotates inosine transport coupled to proton transport with experimental evidence codes citing multiple publications.",
    "evidence_ids": ["C1", "C3", "C5", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic, multipass sequence is consistent with a membrane transporter, favoring the transport-type choice over the enzyme reactions in B–D. But that broad inference does not identify inosine as the substrate or establish proton coupling.",
    "missing_item_specific_fact": "That this particular transporter transports inosine together with H+.",
    "reason": "Selecting A's precise reaction requires protein-specific functional information absent from the sequence and choices; recognizing or retrieving the protein annotation would supply it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is supported for the asked reaction among the listed options; the other choices describe distinct chemical transformations."
  },
  "important_caveats": [
    "The supporting annotation is linked to experimental evidence, but the reviewer-only database and literature information was not supplied to the evaluated model.",
    "The sequence match establishes source applicability, not that the model could infer the specific substrate from sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q9NBV4 (NT2_LEIDO, Leishmania donovani Nucleoside transporter 2/LdNT2) has the exact sequence match (499 AA, SHA256 confirmed). The catalytic activity 'inosine(in) + H(+)(in) = inosine(out) + H(+)(out)' is annotated with ECO:0000269 (direct assay evidence) supported by five independent PubMed publications (10783393, 12807872, 12835315, 15501825, 16464630). The protein is also named 'Inosine-guanosine nucleoside transporter' and 'Equilibrative nucleoside transporter 2.' The expected answer exactly matches the primary annotated transport reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains numerous long hydrophobic stretches (e.g., 'FVLLGMSIMMVTSAVTSAPDFVTKYFIYATGDPDAVAETPLFWNNANTFYNAGTYAMQVVTEIASLTPFMRSIPLGIRLFLGLGIPFVELVVIIAVPAATIPTQNGAIAVIMVVAMMGGLSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALFMSIIQIILQVSMGSTFQDVLTISRIYFGIGIGIQVMAIAALVLLRYNPFAQKYIAEFRAAALRRRGHVEPEESQDSKEPATGDVAEAPKAGEKEVTLDAMEEADEVRAVPSDAFVAKSGAVLQATGDADRMVDLDQTKNITSTEQMLRASVWSVFKRIYPMLLCAFTIFFTTLLVFPGVFFLVPARSGWYMTIIVTLFNAGDFVARVLLMIRVLRPSPKLVIVGTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITL') characteristic of a polytopic membrane transporter with ~11+ TM helices. Option A is a membrane transport reaction (substrate moving across a membrane with proton symport), while options B, C, and D are soluble enzymatic reactions requiring specific cofactors: B needs quinone/FAD-type redox chemistry, C needs &#91;4Fe-4S&#93; cluster-binding cysteine motifs (absent—no CxxC or CxxxC clusters), and D needs CoA-binding motifs. The absence of these cofactor-binding signatures combined with the clear multi-TM architecture provides a defensible reasoning path to select the transport reaction (A) over the three soluble enzyme reactions.


**Missing item-specific fact**

> None strictly required. The membrane-topology reasoning distinguishes A from B/C/D without needing to identify the specific ENT family or the exact nucleoside specificity. However, confirming it transports inosine specifically (vs. guanosine or xanthosine, which are also annotated) would require database lookup, though this does not affect the answer since only inosine transport appears among the choices.


**Reason**

> The multi-TM membrane architecture is directly observable from the hydrophobic sequence stretches. The three distractors (B, C, D) are soluble enzyme reactions requiring cofactors (quinone, Fe-S clusters, CoA) whose binding motifs are absent from the sequence. This provides a concrete biological argument to eliminate B, C, D and select the membrane transport reaction A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry also annotates guanosine and xanthosine transport, neither appears among the four choices. Only option A corresponds to any annotated activity of this protein. The distractors (B, C, D) are catalytic activities of entirely different enzyme classes with no relationship to this sequence.


### Important caveats

- The UniProt entry is flagged as 'Fragment' (499 AA); the full-length protein may have additional domains, but this does not alter the annotated transport activity.
- The term 'catalytic activity' is used by UniProt for transport reactions; this is a transporter, not a classical enzyme, but the reaction notation is standard.
- ECO:0000269 evidence codes indicate direct experimental assay evidence from five publications, making this a well-supported annotation rather than computational inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic stretches (e.g., 'FVLLGMSIMMVTSAVTSAPDFVTKYFIYATGDPDAVAETPLFWNNANTFYNAGTYAMQVVTEIASLTPFMRSIPLGIRLFLGLGIPFVELVVIIAVPAATIPTQNGAIAVIMVVAMMGGLSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALFMSIIQIILQVSMGSTFQDVLTISRIYFGIGIGIQVMAIAALVLLRYNPFAQKYIAEFRAAALRRRGHVEPEESQDSKEPATGDVAEAPKAGEKEVTLDAMEEADEVRAVPSDAFVAKSGAVLQATGDADRMVDLDQTKNITSTEQMLRASVWSVFKRIYPMLLCAFTIFFTTLLVFPGVFFLVPARSGWYMTIIVTLFNAGDFVARVLLMIRVLRPSPKLVIVGTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITL') characteristic of a polytopic membrane transporter with ~11+ TM helices. Option A is a membrane transport reaction (substrate moving across a membrane with proton symport), while options B, C, and D are soluble enzymatic reactions requiring specific cofactors: B needs quinone/FAD-type redox chemistry, C needs [4Fe-4S] cluster-binding cysteine motifs (absent—no CxxC or CxxxC clusters), and D needs CoA-binding motifs. The absence of these cofactor-binding signatures combined with the clear multi-TM architecture provides a defensible reasoning path to select the transport reaction (A) over the three soluble enzyme reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The membrane-topology reasoning distinguishes A from B/C/D without needing to identify the specific ENT family or the exact nucleoside specificity. However, confirming it transports inosine specifically (vs. guanosine or xanthosine, which are also annotated) would require database lookup, though this does not affect the answer since only inosine transport appears among the choices.",
    "reason": "The multi-TM membrane architecture is directly observable from the hydrophobic sequence stretches. The three distractors (B, C, D) are soluble enzyme reactions requiring cofactors (quinone, Fe-S clusters, CoA) whose binding motifs are absent from the sequence. This provides a concrete biological argument to eliminate B, C, D and select the membrane transport reaction A."
  },
  "case_id": "catalytic_activity_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H1",
      "H9"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9NBV4 (NT2_LEIDO, Leishmania donovani Nucleoside transporter 2/LdNT2) has the exact sequence match (499 AA, SHA256 confirmed). The catalytic activity 'inosine(in) + H(+)(in) = inosine(out) + H(+)(out)' is annotated with ECO:0000269 (direct assay evidence) supported by five independent PubMed publications (10783393, 12807872, 12835315, 15501825, 16464630). The protein is also named 'Inosine-guanosine nucleoside transporter' and 'Equilibrative nucleoside transporter 2.' The expected answer exactly matches the primary annotated transport reaction."
  },
  "important_caveats": [
    "The UniProt entry is flagged as 'Fragment' (499 AA); the full-length protein may have additional domains, but this does not alter the annotated transport activity.",
    "The term 'catalytic activity' is used by UniProt for transport reactions; this is a transporter, not a classical enzyme, but the reaction notation is standard.",
    "ECO:0000269 evidence codes indicate direct experimental assay evidence from five publications, making this a well-supported annotation rather than computational inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry also annotates guanosine and xanthosine transport, neither appears among the four choices. Only option A corresponds to any annotated activity of this protein. The distractors (B, C, D) are catalytic activities of entirely different enzyme classes with no relationship to this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"catalytic_activity_0054","expected_answer_check":{"judgment":"supported","reason":"UniProt Q9NBV4 (NT2_LEIDO, Leishmania donovani Nucleoside transporter 2/LdNT2) has the exact sequence match (499 AA, SHA256 confirmed). The catalytic activity 'inosine(in) + H(+)(in) = inosine(out) + H(+)(out)' is annotated with ECO:0000269 (direct assay evidence) supported by five independent PubMed publications (10783393, 12807872, 12835315, 15501825, 16464630). The protein is also named 'Inosine-guanosine nucleoside transporter' and 'Equilibrative nucleoside transporter 2.' The expected answer exactly matches the primary annotated transport reaction.","evidence_ids":["C1","C4","C5","C8","H1","H9"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The sequence contains numerous long hydrophobic stretches (e.g., 'FVLLGMSIMMVTSAVTSAPDFVTKYFIYATGDPDAVAETPLFWNNANTFYNAGTYAMQVVTEIASLTPFMRSIPLGIRLFLGLGIPFVELVVIIAVPAATIPTQNGAIAVIMVVAMMGGLSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALFMSIIQIILQVSMGSTFQDVLTISRIYFGIGIGIQVMAIAALVLLRYNPFAQKYIAEFRAAALRRRGHVEPEESQDSKEPATGDVAEAPKAGEKEVTLDAMEEADEVRAVPSDAFVAKSGAVLQATGDADRMVDLDQTKNITSTEQMLRASVWSVFKRIYPMLLCAFTIFFTTLLVFPGVFFLVPARSGWYMTIIVTLFNAGDFVARVLLMIRVLRPSPKLVIVGTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITL') characteristic of a polytopic membrane transporter with ~11+ TM helices. Option A is a membrane transport reaction (substrate moving across a membrane with proton symport), while options B, C, and D are soluble enzymatic reactions requiring specific cofactors: B needs quinone/FAD-type redox chemistry, C needs [4Fe-4S] cluster-binding cysteine motifs (absent—no CxxC or CxxxC clusters), and D needs CoA-binding motifs. The absence of these cofactor-binding signatures combined with the clear multi-TM architecture provides a defensible reasoning path to select the transport reaction (A) over the three soluble enzyme reactions.","missing_item_specific_fact":"None strictly required. The membrane-topology reasoning distinguishes A from B/C/D without needing to identify the specific ENT family or the exact nucleoside specificity. However, confirming it transports inosine specifically (vs. guanosine or xanthosine, which are also annotated) would require database lookup, though this does not affect the answer since only inosine transport appears among the choices.","reason":"The multi-TM membrane architecture is directly observable from the hydrophobic sequence stretches. The three distractors (B, C, D) are soluble enzyme reactions requiring cofactors (quinone, Fe-S clusters, CoA) whose binding motifs are absent from the sequence. This provides a concrete biological argument to eliminate B, C, D and select the membrane transport reaction A."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"Although the UniProt entry also annotates guanosine and xanthosine transport, neither appears among the four choices. Only option A corresponds to any annotated activity of this protein. The distractors (B, C, D) are catalytic activities of entirely different enzyme classes with no relationship to this sequence."},"important_caveats":["The UniProt entry is flagged as 'Fragment' (499 AA); the full-length protein may have additional domains, but this does not alter the annotated transport activity.","The term 'catalytic activity' is used by UniProt for transport reactions; this is a transporter, not a classical enzyme, but the reaction notation is standard.","ECO:0000269 evidence codes indicate direct experimental assay evidence from five publications, making this a well-supported annotation rather than computational inference."]}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q9NBV4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 62. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
"Q9NBV4"
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAF74264.1","source":"EMBL"}],"lineage":["Eukaryota","Discoba","Euglenozoa","Kinetoplastea","Metakinetoplastina","Trypanosomatida","Trypanosomatidae","Leishmaniinae","Leishmania"],"scientificName":"Leishmania donovani","taxonId":5661}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"12835315","source":"PubMed"}],"value":"Equilibrative nucleoside transporter 2"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAF74264.1","source":"EMBL"}],"value":"Inosine-guanosine nucleoside transporter"}}],"flag":"Fragment","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10783393","source":"PubMed"}],"value":"Nucleoside transporter 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"10783393","source":"PubMed"}],"value":"LdNT2"}]}}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"10783393","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"12807872","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"12835315","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"15501825","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"16464630","source":"PubMed"}],"name":"inosine(in) + H(+)(in) = inosine(out) + H(+)(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:29963"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17596"}]}}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"citation":{"authors":["Carter N.S.","Drew M.E.","Sanchez M.","Vasudevan G.","Landfear S.M.","Ullman B."],"citationCrossReferences":[{"database":"PubMed","id":"10783393"},{"database":"DOI","id":"10.1074/jbc.m002418200"}],"citationType":"journal article","firstPage":"20935","id":"10783393","journal":"J. Biol. Chem.","lastPage":"20941","publicationDate":"2000","title":"Cloning of a novel inosine-guanosine transporter gene from Leishmania donovani by functional rescue of a transport-deficient mutant.","volume":"275"},"evidences":[{"evidenceCode":"ECO:0000312","id":"AAF74264.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","TRANSPORTER ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
ID   NT2_LEIDO               Reviewed;         499 AA.
AC   Q9NBV4;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2000, sequence version 1.
DT   18-JUN-2025, entry version 62.
DE   RecName: Full=Nucleoside transporter 2 {ECO:0000303|PubMed:10783393};
DE            Short=LdNT2 {ECO:0000303|PubMed:10783393};
DE   AltName: Full=Equilibrative nucleoside transporter 2 {ECO:0000303|PubMed:12835315};
DE   AltName: Full=Inosine-guanosine nucleoside transporter {ECO:0000312|EMBL:AAF74264.1};
DE   Flags: Fragment;
GN   Name=NT2 {ECO:0000312|EMBL:AAF74264.1};
OS   Leishmania donovani.
OC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;
OC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Leishmania.
OX   NCBI_TaxID=5661 {ECO:0000312|EMBL:AAF74264.1};
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 71-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=inosine(in) + H(+)(in) = inosine(out) + H(+)(out);
CC         Xref=Rhea:RHEA:29963, ChEBI:CHEBI:15378, ChEBI:CHEBI:17596;
CC         Evidence={ECO:0000269|PubMed:10783393, ECO:0000269|PubMed:12807872,
CC         ECO:0000269|PubMed:12835315, ECO:0000269|PubMed:15501825,
CC         ECO:0000269|PubMed:16464630};
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 54. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
