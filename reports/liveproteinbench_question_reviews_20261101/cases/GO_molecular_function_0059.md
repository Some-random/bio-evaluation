# GO_molecular_function_0059

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — 2 iron, 2 sulfur cluster binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. collagen binding
B. D-alanine-D-alanine ligase activity
C. 2 iron, 2 sulfur cluster binding
D. trichodiene synthase activity
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

> The exact sequence matches a UniProt record annotated with 2 iron, 2 sulfur cluster binding, although that GO annotation is IEA:UniProtKB-KW rather than direct experimental evidence in the supplied excerpts. The record also reports experimentally supported dihydroxy-acid dehydratase activity, which is not among the choices.

Citations as saved: [H6](#evidence-h6), [C5](#evidence-c5), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence does not provide an unambiguous, general sequence-based clue that distinguishes 2Fe-2S binding from the other listed functions. Identifying the protein as a dihydroxy-acid dehydratase and knowing its cofactor would distinguish the choice, but requires protein-specific knowledge.


**Missing item-specific fact**

> That this particular protein is annotated as binding a 2Fe-2S cluster; the available supporting record labels this as a UniProt keyword-derived annotation.


**Reason**

> The required cofactor assignment is not supplied in the question, and recognizing the exact sequence or its database entry would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, C is supported by the matched sequence's GO annotation. However, the record's experimentally supported catalytic function is absent from the options, so C should not be mistaken for the protein's catalytic activity.


### Important caveats

- The historical source record matches the sequence, but the author's exact source snapshot is unknown.
- The evidence for 2Fe-2S binding cited here is computational annotation, not a direct experimental measurement in the excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence does not provide an unambiguous, general sequence-based clue that distinguishes 2Fe-2S binding from the other listed functions. Identifying the protein as a dihydroxy-acid dehydratase and knowing its cofactor would distinguish the choice, but requires protein-specific knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular protein is annotated as binding a 2Fe-2S cluster; the available supporting record labels this as a UniProt keyword-derived annotation.",
    "reason": "The required cofactor assignment is not supplied in the question, and recognizing the exact sequence or its database entry would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "GO_molecular_function_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "C5",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated with 2 iron, 2 sulfur cluster binding, although that GO annotation is IEA:UniProtKB-KW rather than direct experimental evidence in the supplied excerpts. The record also reports experimentally supported dihydroxy-acid dehydratase activity, which is not among the choices."
  },
  "important_caveats": [
    "The historical source record matches the sequence, but the author's exact source snapshot is unknown.",
    "The evidence for 2Fe-2S binding cited here is computational annotation, not a direct experimental measurement in the excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, C is supported by the matched sequence's GO annotation. However, the record's experimentally supported catalytic function is absent from the options, so C should not be mistaken for the protein's catalytic activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated with 2 iron, 2 sulfur cluster binding, although that GO annotation is IEA:UniProtKB-KW rather than direct experimental evidence in the supplied excerpts. The record also reports experimentally supported dihydroxy-acid dehydratase activity, which is not among the choices.",
    "evidence_ids": ["H6", "C5", "C8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence does not provide an unambiguous, general sequence-based clue that distinguishes 2Fe-2S binding from the other listed functions. Identifying the protein as a dihydroxy-acid dehydratase and knowing its cofactor would distinguish the choice, but requires protein-specific knowledge.",
    "missing_item_specific_fact": "That this particular protein is annotated as binding a 2Fe-2S cluster; the available supporting record labels this as a UniProt keyword-derived annotation.",
    "reason": "The required cofactor assignment is not supplied in the question, and recognizing the exact sequence or its database entry would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, C is supported by the matched sequence's GO annotation. However, the record's experimentally supported catalytic function is absent from the options, so C should not be mistaken for the protein's catalytic activity."
  },
  "important_caveats": [
    "The historical source record matches the sequence, but the author's exact source snapshot is unknown.",
    "The evidence for 2Fe-2S binding cited here is computational annotation, not a direct experimental measurement in the excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q0CPG9, DHAD astD from Aspergillus terreus, EC 4.2.1.9) carries the GO annotation GO:0051537 '2 iron, 2 sulfur cluster binding' in UniProt (evidence: IEA:UniProtKB-KW, i.e., keyword-based computational inference). This is biochemically well-founded: DHAD/IlvD-family enzymes are known to coordinate a &#91;2Fe-2S&#93; cluster essential for catalysis, and the sequence contains cysteine-rich motifs consistent with cluster ligation. While the PRIMARY catalytic function is dihydroxy-acid dehydratase activity (GO:0004160, EXP evidence), that term is not among the options. Among the four choices, C is the only one actually annotated for this protein; A (collagen binding), B (D-Ala-D-Ala ligase), and D (trichodiene synthase) are entirely unrelated to this enzyme. The answer is supported but represents a cofactor-binding aspect rather than the primary catalytic activity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H6](#evidence-h6), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 598 aa, contains mitochondrial-targeting N-terminal features, and displays sequence motifs (cysteine clusters, overall length/composition) consistent with the DHAD/IlvD enzyme family. General biochemistry establishes that DHAD enzymes (EC 4.2.1.9) are &#91;2Fe-2S&#93; cluster-dependent. The distractors are eliminable by general reasoning: collagen binding (A) applies to animal extracellular proteins, not fungal mitochondrial enzymes; D-Ala-D-Ala ligase (B) is a bacterial peptidoglycan enzyme absent from eukaryotes; trichodiene synthase (D) is a ~350-aa alpha-helical terpene cyclase with a completely different fold. Thus, identifying the protein as a DHAD-family member and knowing DHADs require a 2Fe-2S cluster provides a reasoning path to C.


**Missing item-specific fact**

> Precise identification of this specific sequence as a DHAD/IlvD family member from raw sequence alone (without database search) requires recognizing family-specific catalytic motifs, which is a non-trivial sequence-recognition step though supported by general enzyme-family knowledge.


**Reason**

> The elimination of A, B, and D relies on straightforward general biology (kingdom specificity, enzyme class/fold differences). The positive identification of C requires: (1) recognizing the sequence as a DHAD-family enzyme (supported by length, composition, and cysteine motifs), and (2) knowing that DHADs are &#91;2Fe-2S&#93; enzymes (textbook biochemistry). This constitutes a defensible reasoning chain, though the family-recognition step is non-trivial from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are clearly incompatible with a fungal mitochondrial DHAD enzyme. Only C is an actual GO annotation for this protein. Although the question asks for the 'primary molecular function' and the true primary function (dihydroxy-acid dehydratase activity) is not listed, C is unambiguously the best answer among the provided choices. No other option is defensible.


### Important caveats

- The 2Fe-2S cluster binding annotation carries IEA (Inferred from Electronic Annotation) evidence via UniProt keyword, not direct experimental evidence. However, the &#91;2Fe-2S&#93; cofactor in DHAD enzymes is well-established in the broader biochemical literature.
- The question asks for 'primary molecular function,' but the true primary function (dihydroxy-acid dehydratase activity, GO:0004160, EXP evidence) is absent from the options. C represents a cofactor-binding molecular function integral to catalysis but is a secondary descriptor of the protein's activity.
- The sequence-to-DHAD family assignment from raw sequence alone is non-trivial and may partially depend on trained pattern recognition rather than purely deductive reasoning from first principles.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 598 aa, contains mitochondrial-targeting N-terminal features, and displays sequence motifs (cysteine clusters, overall length/composition) consistent with the DHAD/IlvD enzyme family. General biochemistry establishes that DHAD enzymes (EC 4.2.1.9) are [2Fe-2S] cluster-dependent. The distractors are eliminable by general reasoning: collagen binding (A) applies to animal extracellular proteins, not fungal mitochondrial enzymes; D-Ala-D-Ala ligase (B) is a bacterial peptidoglycan enzyme absent from eukaryotes; trichodiene synthase (D) is a ~350-aa alpha-helical terpene cyclase with a completely different fold. Thus, identifying the protein as a DHAD-family member and knowing DHADs require a 2Fe-2S cluster provides a reasoning path to C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of this specific sequence as a DHAD/IlvD family member from raw sequence alone (without database search) requires recognizing family-specific catalytic motifs, which is a non-trivial sequence-recognition step though supported by general enzyme-family knowledge.",
    "reason": "The elimination of A, B, and D relies on straightforward general biology (kingdom specificity, enzyme class/fold differences). The positive identification of C requires: (1) recognizing the sequence as a DHAD-family enzyme (supported by length, composition, and cysteine motifs), and (2) knowing that DHADs are [2Fe-2S] enzymes (textbook biochemistry). This constitutes a defensible reasoning chain, though the family-recognition step is non-trivial from sequence alone."
  },
  "case_id": "GO_molecular_function_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H6",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein (Q0CPG9, DHAD astD from Aspergillus terreus, EC 4.2.1.9) carries the GO annotation GO:0051537 '2 iron, 2 sulfur cluster binding' in UniProt (evidence: IEA:UniProtKB-KW, i.e., keyword-based computational inference). This is biochemically well-founded: DHAD/IlvD-family enzymes are known to coordinate a [2Fe-2S] cluster essential for catalysis, and the sequence contains cysteine-rich motifs consistent with cluster ligation. While the PRIMARY catalytic function is dihydroxy-acid dehydratase activity (GO:0004160, EXP evidence), that term is not among the options. Among the four choices, C is the only one actually annotated for this protein; A (collagen binding), B (D-Ala-D-Ala ligase), and D (trichodiene synthase) are entirely unrelated to this enzyme. The answer is supported but represents a cofactor-binding aspect rather than the primary catalytic activity."
  },
  "important_caveats": [
    "The 2Fe-2S cluster binding annotation carries IEA (Inferred from Electronic Annotation) evidence via UniProt keyword, not direct experimental evidence. However, the [2Fe-2S] cofactor in DHAD enzymes is well-established in the broader biochemical literature.",
    "The question asks for 'primary molecular function,' but the true primary function (dihydroxy-acid dehydratase activity, GO:0004160, EXP evidence) is absent from the options. C represents a cofactor-binding molecular function integral to catalysis but is a secondary descriptor of the protein's activity.",
    "The sequence-to-DHAD family assignment from raw sequence alone is non-trivial and may partially depend on trained pattern recognition rather than purely deductive reasoning from first principles."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly incompatible with a fungal mitochondrial DHAD enzyme. Only C is an actual GO annotation for this protein. Although the question asks for the 'primary molecular function' and the true primary function (dihydroxy-acid dehydratase activity) is not listed, C is unambiguously the best answer among the provided choices. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q0CPG9, DHAD astD from Aspergillus terreus, EC 4.2.1.9) carries the GO annotation GO:0051537 '2 iron, 2 sulfur cluster binding' in UniProt (evidence: IEA:UniProtKB-KW, i.e., keyword-based computational inference). This is biochemically well-founded: DHAD/IlvD-family enzymes are known to coordinate a [2Fe-2S] cluster essential for catalysis, and the sequence contains cysteine-rich motifs consistent with cluster ligation. While the PRIMARY catalytic function is dihydroxy-acid dehydratase activity (GO:0004160, EXP evidence), that term is not among the options. Among the four choices, C is the only one actually annotated for this protein; A (collagen binding), B (D-Ala-D-Ala ligase), and D (trichodiene synthase) are entirely unrelated to this enzyme. The answer is supported but represents a cofactor-binding aspect rather than the primary catalytic activity.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H6", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 598 aa, contains mitochondrial-targeting N-terminal features, and displays sequence motifs (cysteine clusters, overall length/composition) consistent with the DHAD/IlvD enzyme family. General biochemistry establishes that DHAD enzymes (EC 4.2.1.9) are [2Fe-2S] cluster-dependent. The distractors are eliminable by general reasoning: collagen binding (A) applies to animal extracellular proteins, not fungal mitochondrial enzymes; D-Ala-D-Ala ligase (B) is a bacterial peptidoglycan enzyme absent from eukaryotes; trichodiene synthase (D) is a ~350-aa alpha-helical terpene cyclase with a completely different fold. Thus, identifying the protein as a DHAD-family member and knowing DHADs require a 2Fe-2S cluster provides a reasoning path to C.",
    "missing_item_specific_fact": "Precise identification of this specific sequence as a DHAD/IlvD family member from raw sequence alone (without database search) requires recognizing family-specific catalytic motifs, which is a non-trivial sequence-recognition step though supported by general enzyme-family knowledge.",
    "reason": "The elimination of A, B, and D relies on straightforward general biology (kingdom specificity, enzyme class/fold differences). The positive identification of C requires: (1) recognizing the sequence as a DHAD-family enzyme (supported by length, composition, and cysteine motifs), and (2) knowing that DHADs are [2Fe-2S] enzymes (textbook biochemistry). This constitutes a defensible reasoning chain, though the family-recognition step is non-trivial from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly incompatible with a fungal mitochondrial DHAD enzyme. Only C is an actual GO annotation for this protein. Although the question asks for the 'primary molecular function' and the true primary function (dihydroxy-acid dehydratase activity) is not listed, C is unambiguously the best answer among the provided choices. No other option is defensible."
  },
  "important_caveats": [
    "The 2Fe-2S cluster binding annotation carries IEA (Inferred from Electronic Annotation) evidence via UniProt keyword, not direct experimental evidence. However, the [2Fe-2S] cofactor in DHAD enzymes is well-established in the broader biochemical literature.",
    "The question asks for 'primary molecular function,' but the true primary function (dihydroxy-acid dehydratase activity, GO:0004160, EXP evidence) is absent from the options. C represents a cofactor-binding molecular function integral to catalysis but is a secondary descriptor of the protein's activity.",
    "The sequence-to-DHAD family assignment from raw sequence alone is non-trivial and may partially depend on trained pattern recognition rather than purely deductive reasoning from first principles."
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

**Accession:** `Q0CPG9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 90. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
"Q0CPG9"
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein D"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"value":"4.2.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Dihydroxy-acid dehydratase astD, mitochondrial"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"DHAD astD"}]}}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"value":"Dihydroxyacid dehydratase; part of the gene cluster that mediates the biosynthesis of the sesquiterpenoid aspterric acid (AA), an inhibitor of dihydroxy-acid dehydratase (DHAD) effective as an herbicide (PubMed:29995859). Performs the third step in the common pathway leading to biosynthesis of branched-chain amino acids (PubMed:29995859). Catalyzes the dehydration of (2R,3R)-2,3-dihydroxy-3-methylpentanoate (2,3-dihydroxy-3-methylvalerate) into 2-oxo-3-methylpentanoate (2-oxo-3-methylvalerate) and of (2R)-2,3-dihydroxy-3-methylbutanoate (2,3-dihydroxyisovalerate) into 2-oxo-3-methylbutanoate (2-oxoisovalerate), the penultimate precursor to L-isoleucine and L-valine, respectively (PubMed:29995859). AstD confers self-resistance in the presence of the dihydroxyacid dehydratase inhibitor aspterric acid (AA) produced by the ast cluster (PubMed:29995859)"}]}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"id":"GO:0004160","properties":[{"key":"GoTerm","value":"F:dihydroxy-acid dehydratase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 114-114`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
DR   GO; GO:0051537; F:2 iron, 2 sulfur cluster binding; IEA:UniProtKB-KW.
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 327878-327891`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0051537
name: 2 iron, 2 sulfur cluster binding
namespace: molecular_function
def: "Binding to a 2 iron, 2 sulfur (2Fe-2S) cluster; this cluster consists of two iron atoms, with two inorganic sulfur atoms found between the irons and acting as bridging ligands." [GOC:ai, PMID:15952888, Wikipedia:Iron-sulfur_cluster]
synonym: "2 Fe 2 S cluster binding" EXACT []
synonym: "2 iron, 2 sulphur cluster binding" EXACT []
synonym: "2Fe-2S cluster binding" EXACT []
synonym: "diiron disulfide cluster binding" EXACT []
synonym: "diiron disulphide cluster binding" EXACT []
synonym: "iron-sulfur cluster 2Fe-2S binding" EXACT []
synonym: "iron-sulphur cluster 2Fe-2S binding" EXACT []
is_a: GO:0051536 ! iron-sulfur cluster binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 59. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
