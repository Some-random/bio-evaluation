# GO_molecular_function_0104

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — metal ion binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSLLDIIYQLRQVPRWDGSFQFEKEDVSQHSFSVIAISHILCELKETLEGKKINKEKLLLYALYHDVTEVVSTHIISPVKKNSILKDPFNAFREQIKNSLFDNLPITLSDTLSTILNNNDLEIQEIVEHADHVDAYCKSCIEVHRGNKDFISIQRSLGDKLDNLTKEYPYLKEFQNLFLKDFPLENKNYRYLN

[Multiple Choices]
A. metal ion binding
B. N6-methyladenosine-containing RNA reader activity
C. serine-type endopeptidase activity
D. UDP-glycosyltransferase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched protein is annotated with metal ion binding, though that GO annotation is computational (IEA). Independent structural evidence reports crystal complexes with magnesium, supporting metal binding. Its characterized catalytic function is phosphohydrolase activity, which is not among the choices.

Citations as saved: [H4](#evidence-h4), [H8](#evidence-h8), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a histidine/aspartate-rich HD-like motif (including HADHVD). HD-domain phosphohydrolases commonly coordinate divalent metal ions, making metal binding a biologically grounded choice over RNA-reader, serine-protease, or UDP-glycosyltransferase activity.


**Missing item-specific fact**

> The exact protein identity and its experimentally characterized function are not supplied; they would confirm the inference but are not essential to favor metal binding from the motif and choices.


**Reason**

> The sequence provides a recognizable HD-like catalytic signature consistent with metal-dependent phosphohydrolase activity. This supports a meaningful inference for option A, while not establishing that metal binding is the protein’s principal molecular function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, metal ion binding is supported; the protein’s more specific phosphohydrolase activity is not offered as an option.


### Important caveats

- The GO metal-binding annotation cited is IEA, not itself experimental evidence.
- The magnesium-complex structures support metal binding, but the question’s use of “primary molecular function” is imprecise for a protein whose characterized catalytic activity is omitted.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a histidine/aspartate-rich HD-like motif (including HADHVD). HD-domain phosphohydrolases commonly coordinate divalent metal ions, making metal binding a biologically grounded choice over RNA-reader, serine-protease, or UDP-glycosyltransferase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein identity and its experimentally characterized function are not supplied; they would confirm the inference but are not essential to favor metal binding from the motif and choices.",
    "reason": "The sequence provides a recognizable HD-like catalytic signature consistent with metal-dependent phosphohydrolase activity. This supports a meaningful inference for option A, while not establishing that metal binding is the protein’s principal molecular function."
  },
  "case_id": "GO_molecular_function_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H8",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched protein is annotated with metal ion binding, though that GO annotation is computational (IEA). Independent structural evidence reports crystal complexes with magnesium, supporting metal binding. Its characterized catalytic function is phosphohydrolase activity, which is not among the choices."
  },
  "important_caveats": [
    "The GO metal-binding annotation cited is IEA, not itself experimental evidence.",
    "The magnesium-complex structures support metal binding, but the question’s use of “primary molecular function” is imprecise for a protein whose characterized catalytic activity is omitted."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, metal ion binding is supported; the protein’s more specific phosphohydrolase activity is not offered as an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched protein is annotated with metal ion binding, though that GO annotation is computational (IEA). Independent structural evidence reports crystal complexes with magnesium, supporting metal binding. Its characterized catalytic function is phosphohydrolase activity, which is not among the choices.",
    "evidence_ids": ["H4", "H8", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a histidine/aspartate-rich HD-like motif (including HADHVD). HD-domain phosphohydrolases commonly coordinate divalent metal ions, making metal binding a biologically grounded choice over RNA-reader, serine-protease, or UDP-glycosyltransferase activity.",
    "missing_item_specific_fact": "The exact protein identity and its experimentally characterized function are not supplied; they would confirm the inference but are not essential to favor metal binding from the motif and choices.",
    "reason": "The sequence provides a recognizable HD-like catalytic signature consistent with metal-dependent phosphohydrolase activity. This supports a meaningful inference for option A, while not establishing that metal binding is the protein’s principal molecular function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, metal ion binding is supported; the protein’s more specific phosphohydrolase activity is not offered as an option."
  },
  "important_caveats": [
    "The GO metal-binding annotation cited is IEA, not itself experimental evidence.",
    "The magnesium-complex structures support metal binding, but the question’s use of “primary molecular function” is imprecise for a protein whose characterized catalytic activity is omitted."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (O24769, OxsA) is an HD-domain phosphohydrolase (EC 3.1.3.112) that binds Mg²⁺ as a catalytic cofactor, confirmed by X-ray crystallography in complexes with magnesium (PDB 5TK6-5TKA, evidence_id H4/C8). GO:0046872 (metal ion binding) is annotated in UniProt (evidence_id H8), albeit with IEA:UniProtKB-KW. The crystallographic data provide experimental support for Mg²⁺ coordination by the HD motif. Among the four options, metal ion binding is the only molecular function actually exhibited by this protein; the other three (m6A RNA reader, serine endopeptidase, UDP-glycosyltransferase) are entirely unrelated to a bacterial phosphatase. While the 'primary' catalytic function is phosphohydrolase activity (not offered as a choice), metal ion binding is a genuine and annotated molecular function of this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4), [H8](#evidence-h8), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~194 AA, bacterial origin) lacks all hallmarks of the three distractors: (1) no canonical serine protease catalytic triad or GDSGGP motif for option C; (2) no PSPG box or glycosyltransferase fold features for option D; (3) no YTH domain, RRM, or other RNA-binding architecture for option B. Positively, the sequence contains a conserved His-Asp pair in the region 'EIVEHADHVDAY' consistent with the HD-domain metal-coordinating motif found in phosphohydrolases, which binds divalent cations (Mg²⁺/Mn²⁺) for catalysis. A model with general biochemistry knowledge can identify the His-Asp metal-coordination signature and eliminate the three unrelated functions.


**Missing item-specific fact**

> None critical. Recognizing the HD domain superfamily by name is specialized, but the His-Asp metal-coordinating motif and the elimination of three clearly unrelated activities are accessible through general biological reasoning.


**Reason**

> The three incorrect options (m6A RNA reader, serine endopeptidase, UDP-glycosyltransferase) can be eliminated from a small bacterial protein sequence using general knowledge of catalytic motifs and domain architectures. The positive identification of metal-binding potential from the His-Asp pair in the sequence provides a concrete biological argument distinguishable without memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the question asks for 'primary molecular function' and the true primary catalytic activity (phosphohydrolase/hydrolase, GO:0016787) is not among the choices, 'metal ion binding' is the only option that is a true molecular function of this protein. The other three are categorically wrong for a bacterial HD-domain phosphatase. No reasonable biological argument supports B, C, or D.


### Important caveats

- The GO annotation for metal ion binding (GO:0046872) carries evidence code IEA:UniProtKB-KW (inferred from keyword), not direct experimental annotation. However, the crystal structures (5TK6-5TKA) in complexes with magnesium provide experimental corroboration.
- The question's phrasing 'primary molecular function' is slightly imprecise since the primary catalytic function is phosphatase activity, not metal binding per se. Metal binding is a cofactor-binding function supporting catalysis. This does not create answer ambiguity among the four given choices.
- The sequence match is confirmed (SHA256 identical across current and historical entries), so the evidence applies directly to the queried protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~194 AA, bacterial origin) lacks all hallmarks of the three distractors: (1) no canonical serine protease catalytic triad or GDSGGP motif for option C; (2) no PSPG box or glycosyltransferase fold features for option D; (3) no YTH domain, RRM, or other RNA-binding architecture for option B. Positively, the sequence contains a conserved His-Asp pair in the region 'EIVEHADHVDAY' consistent with the HD-domain metal-coordinating motif found in phosphohydrolases, which binds divalent cations (Mg²⁺/Mn²⁺) for catalysis. A model with general biochemistry knowledge can identify the His-Asp metal-coordination signature and eliminate the three unrelated functions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognizing the HD domain superfamily by name is specialized, but the His-Asp metal-coordinating motif and the elimination of three clearly unrelated activities are accessible through general biological reasoning.",
    "reason": "The three incorrect options (m6A RNA reader, serine endopeptidase, UDP-glycosyltransferase) can be eliminated from a small bacterial protein sequence using general knowledge of catalytic motifs and domain architectures. The positive identification of metal-binding potential from the His-Asp pair in the sequence provides a concrete biological argument distinguishable without memorizing this specific protein's database entry."
  },
  "case_id": "GO_molecular_function_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H4",
      "H8",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The protein (O24769, OxsA) is an HD-domain phosphohydrolase (EC 3.1.3.112) that binds Mg²⁺ as a catalytic cofactor, confirmed by X-ray crystallography in complexes with magnesium (PDB 5TK6-5TKA, evidence_id H4/C8). GO:0046872 (metal ion binding) is annotated in UniProt (evidence_id H8), albeit with IEA:UniProtKB-KW. The crystallographic data provide experimental support for Mg²⁺ coordination by the HD motif. Among the four options, metal ion binding is the only molecular function actually exhibited by this protein; the other three (m6A RNA reader, serine endopeptidase, UDP-glycosyltransferase) are entirely unrelated to a bacterial phosphatase. While the 'primary' catalytic function is phosphohydrolase activity (not offered as a choice), metal ion binding is a genuine and annotated molecular function of this protein."
  },
  "important_caveats": [
    "The GO annotation for metal ion binding (GO:0046872) carries evidence code IEA:UniProtKB-KW (inferred from keyword), not direct experimental annotation. However, the crystal structures (5TK6-5TKA) in complexes with magnesium provide experimental corroboration.",
    "The question's phrasing 'primary molecular function' is slightly imprecise since the primary catalytic function is phosphatase activity, not metal binding per se. Metal binding is a cofactor-binding function supporting catalysis. This does not create answer ambiguity among the four given choices.",
    "The sequence match is confirmed (SHA256 identical across current and historical entries), so the evidence applies directly to the queried protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for 'primary molecular function' and the true primary catalytic activity (phosphohydrolase/hydrolase, GO:0016787) is not among the choices, 'metal ion binding' is the only option that is a true molecular function of this protein. The other three are categorically wrong for a bacterial HD-domain phosphatase. No reasonable biological argument supports B, C, or D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (O24769, OxsA) is an HD-domain phosphohydrolase (EC 3.1.3.112) that binds Mg²⁺ as a catalytic cofactor, confirmed by X-ray crystallography in complexes with magnesium (PDB 5TK6-5TKA, evidence_id H4/C8). GO:0046872 (metal ion binding) is annotated in UniProt (evidence_id H8), albeit with IEA:UniProtKB-KW. The crystallographic data provide experimental support for Mg²⁺ coordination by the HD motif. Among the four options, metal ion binding is the only molecular function actually exhibited by this protein; the other three (m6A RNA reader, serine endopeptidase, UDP-glycosyltransferase) are entirely unrelated to a bacterial phosphatase. While the 'primary' catalytic function is phosphohydrolase activity (not offered as a choice), metal ion binding is a genuine and annotated molecular function of this protein.",
    "evidence_ids": ["C4", "C5", "C8", "H4", "H8", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~194 AA, bacterial origin) lacks all hallmarks of the three distractors: (1) no canonical serine protease catalytic triad or GDSGGP motif for option C; (2) no PSPG box or glycosyltransferase fold features for option D; (3) no YTH domain, RRM, or other RNA-binding architecture for option B. Positively, the sequence contains a conserved His-Asp pair in the region 'EIVEHADHVDAY' consistent with the HD-domain metal-coordinating motif found in phosphohydrolases, which binds divalent cations (Mg²⁺/Mn²⁺) for catalysis. A model with general biochemistry knowledge can identify the His-Asp metal-coordination signature and eliminate the three unrelated functions.",
    "missing_item_specific_fact": "None critical. Recognizing the HD domain superfamily by name is specialized, but the His-Asp metal-coordinating motif and the elimination of three clearly unrelated activities are accessible through general biological reasoning.",
    "reason": "The three incorrect options (m6A RNA reader, serine endopeptidase, UDP-glycosyltransferase) can be eliminated from a small bacterial protein sequence using general knowledge of catalytic motifs and domain architectures. The positive identification of metal-binding potential from the His-Asp pair in the sequence provides a concrete biological argument distinguishable without memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for 'primary molecular function' and the true primary catalytic activity (phosphohydrolase/hydrolase, GO:0016787) is not among the choices, 'metal ion binding' is the only option that is a true molecular function of this protein. The other three are categorically wrong for a bacterial HD-domain phosphatase. No reasonable biological argument supports B, C, or D."
  },
  "important_caveats": [
    "The GO annotation for metal ion binding (GO:0046872) carries evidence code IEA:UniProtKB-KW (inferred from keyword), not direct experimental annotation. However, the crystal structures (5TK6-5TKA) in complexes with magnesium provide experimental corroboration.",
    "The question's phrasing 'primary molecular function' is slightly imprecise since the primary catalytic function is phosphatase activity, not metal binding per se. Metal binding is a cofactor-binding function supporting catalysis. This does not create answer ambiguity among the four given choices.",
    "The sequence match is confirmed (SHA256 identical across current and historical entries), so the evidence applies directly to the queried protein."
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

**Accession:** `O24769` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 75. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28346939","source":"PubMed"}],"value":"HD-domain phosphohydrolase OxsA"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27849620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"}],"value":"3.1.3.112"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"4'-phosphooxetanocin A phosphatase"}}}
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27849620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"}],"value":"Phosphohydrolase involved in the biosynthesis of oxetanocin A (OXT-A), a nucleoside analog with antitumor, antiviral and antibacterial properties (PubMed:27849620, PubMed:28346939). Catalyzes the hydrolysis of phosphooxetanocin A (OXT-A-P) to generate oxetanocin A (OXT-A) and a molecule of inorganic phosphate (PubMed:27849620, PubMed:28346939). Can also bind and hydrolyze OXT triphosphate (OXT-A-PPP) and OXT diphosphate (OXT-A-PP), and thus catalyze the sequential hydrolysis of tri-, di- and mono-phosphorylated oxetanocin A compounds, releasing one molecule of inorganic phosphate at a time (PubMed:27849620). In vitro can also use dATP, dAMP and dADP (PubMed:27849620)"}]}
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
{"citation":{"authors":["Bridwell-Rabb J.","Kang G.","Zhong A.","Liu H.W.","Drennan C.L."],"citationCrossReferences":[{"database":"PubMed","id":"27849620"},{"database":"DOI","id":"10.1073/pnas.1613610113"}],"citationType":"journal article","firstPage":"13750","id":"27849620","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"13755","publicationDate":"2016","title":"An HD domain phosphohydrolase active site tailored for oxetanocin-A biosynthesis.","volume":"113"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5TK6","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TK7","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TK8","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TK9","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TKA","source":"PDB"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEXES WITH MAGNESIUM; OXETANOCIN A; OXETANOCIN A MONOPHOSPHATE; OXETANOCIN A DIPHOSPHATE AND OXETANOCIN A TRIPHOSPHATE","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN"]}
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:29:21.063065+00:00.  

```text
RN   [3] {ECO:0007744|PDB:5TK6, ECO:0007744|PDB:5TK7, ECO:0007744|PDB:5TK8, ECO:0007744|PDB:5TK9, ECO:0007744|PDB:5TKA}
RP   X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEXES WITH MAGNESIUM;
RP   OXETANOCIN A; OXETANOCIN A MONOPHOSPHATE; OXETANOCIN A DIPHOSPHATE AND
RP   OXETANOCIN A TRIPHOSPHATE, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND DOMAIN.
RX   PubMed=27849620; DOI=10.1073/pnas.1613610113;
RA   Bridwell-Rabb J., Kang G., Zhong A., Liu H.W., Drennan C.L.;
RT   "An HD domain phosphohydrolase active site tailored for oxetanocin-A
RT   biosynthesis.";
RL   Proc. Natl. Acad. Sci. U.S.A. 113:13750-13755(2016).
```

Source SHA-256: `bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)  
**Locator:** `lines 124-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:29:21.063065+00:00.  

```text
DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.
```

Source SHA-256: `bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 281280-281292`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0046872
name: metal ion binding
namespace: molecular_function
def: "Binding to a metal ion." [GOC:ai]
subset: goslim_agr
subset: goslim_drosophila
subset: goslim_flybase_ribbon
subset: goslim_metagenomics
synonym: "heavy metal binding" NARROW []
synonym: "metal binding" EXACT []
is_a: GO:0043169 ! cation binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 104. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
