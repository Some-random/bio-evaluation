# GO_biological_process_0159

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — mitochondrial respiratory chain complex I assembly

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLRYRQVVGLLQRRNFSAGATSNGSGSSGGDKSGEDLHPIRRTLRLLGNDMRKVKEFFVPKEPETEKVPIPTQSQFHFSGERDKSKEATVPDDFQTHCDVLIIGGGGVGSSIAYWLKEKARDGLNVVVVEKDDTYAQSATRVSVGGLCQQFSLPENIQMSLFAADFLRSARKHFGEEVPLQFTPHGHLMLAGEEHAESLKRSSQLQNELGARNELLTADRLTARFPWLNTKGIALGCLGLEKEGWFNPLALLSNFRRSASGYGAHFISGQVVDFEFKSQTDISVVTDLGSNEGAYTGLEKAVIQLPDGTRRTCKFALCVISAGASSEQIARLARIGVGPGILRVPLPINARKRYMYAINSQAQSAPGMNMPMTIDPSGIFIRRDGLGGNYICVQDSTEEYNSAMIDPQYFAQHIRPHLYNRIPVLGEAQVVDSWAGCYDHNVYDENGILGAHPYYNNLYLATGFSGHGVQQSLAVGRAISELIMDGQFRTIDLSRLSFDRLIVDQPMFELNNVLS

[Multiple Choices]
A. positive regulation of interleukin-12 production
B. nickel cation transport
C. stress-activated MAPK cascade
D. mitochondrial respiratory chain complex I assembly
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt entry annotated as involved in mitochondrial respiratory chain complex I assembly, and that entry carries the matching GO term. The functional annotation cites a paper, while the GO annotation is IBA; this supports the key but is not, by itself, direct experimental validation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support broad protein-family or localization hypotheses, but it does not provide a clear basis for assigning the specific biological process of complex I assembly rather than the other listed processes.


**Missing item-specific fact**

> The protein-specific functional annotation linking this sequence to complex I assembly, or equivalent experimental evidence, is absent from the model input.


**Reason**

> The matching identity and process annotation come from reviewer-only database evidence. The sequence alone does not meaningfully distinguish this specific assembly role among the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct processes, and the matched annotation supports D. The input’s lack of a process-specific clue makes the item lookup-dependent, but does not establish that another option is also biologically correct.


### Important caveats

- The source annotation applies to an exact sequence match, but the accession and annotation were not supplied to the evaluated model.
- The cited UniProt functional statement uses ECO:0000305, and the GO term uses IBA; neither excerpt alone establishes direct experimental confirmation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support broad protein-family or localization hypotheses, but it does not provide a clear basis for assigning the specific biological process of complex I assembly rather than the other listed processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation linking this sequence to complex I assembly, or equivalent experimental evidence, is absent from the model input.",
    "reason": "The matching identity and process annotation come from reviewer-only database evidence. The sequence alone does not meaningfully distinguish this specific assembly role among the choices."
  },
  "case_id": "GO_biological_process_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as involved in mitochondrial respiratory chain complex I assembly, and that entry carries the matching GO term. The functional annotation cites a paper, while the GO annotation is IBA; this supports the key but is not, by itself, direct experimental validation."
  },
  "important_caveats": [
    "The source annotation applies to an exact sequence match, but the accession and annotation were not supplied to the evaluated model.",
    "The cited UniProt functional statement uses ECO:0000305, and the GO term uses IBA; neither excerpt alone establishes direct experimental confirmation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct processes, and the matched annotation supports D. The input’s lack of a process-specific clue makes the item lookup-dependent, but does not establish that another option is also biologically correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as involved in mitochondrial respiratory chain complex I assembly, and that entry carries the matching GO term. The functional annotation cites a paper, while the GO annotation is IBA; this supports the key but is not, by itself, direct experimental validation.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support broad protein-family or localization hypotheses, but it does not provide a clear basis for assigning the specific biological process of complex I assembly rather than the other listed processes.",
    "missing_item_specific_fact": "The protein-specific functional annotation linking this sequence to complex I assembly, or equivalent experimental evidence, is absent from the model input.",
    "reason": "The matching identity and process annotation come from reviewer-only database evidence. The sequence alone does not meaningfully distinguish this specific assembly role among the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct processes, and the matched annotation supports D. The input’s lack of a process-specific clue makes the item lookup-dependent, but does not establish that another option is also biologically correct."
  },
  "important_caveats": [
    "The source annotation applies to an exact sequence match, but the accession and annotation were not supplied to the evaluated model.",
    "The cited UniProt functional statement uses ECO:0000305, and the GO term uses IBA; neither excerpt alone establishes direct experimental confirmation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9VJ10 (dFOXRED1, Drosophila melanogaster). The UniProt FUNCTION comment (ECO:0000305, citing PubMed:34386730) states 'Involved in the assembly of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I).' The GO annotation GO:0032981 'mitochondrial respiratory chain complex I assembly' is present (evidence code IBA:GO_Central). The primary reference (Murari et al. 2021, IScience) reports experimental work on NDUFAF3/NDUFAF4 homologs in complex I biogenesis. The FAD-binding Rossmann-fold motif (GGGVGSSIAYWLKEKARDGLNVVVVE) is consistent with FOXRED1's oxidoreductase domain. The expected answer D is supported by both the curated function statement and the GO annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical FAD-binding Rossmann-fold motif (GGGVGSSIAYWLKEKARDGLNVVVVE), indicating an oxidoreductase. Option A (positive regulation of IL-12 production) can be eliminated because Drosophila melanogaster lacks interleukin-12, a mammalian-specific cytokine; no immune-signaling motifs are present. Option B (nickel cation transport) requires transmembrane helices and His-rich metal-binding motifs, neither of which appear in this soluble protein. Option C (stress-activated MAPK cascade) requires protein-kinase domain motifs (e.g., VAIK, HRD, DFG), which are absent. By elimination, option D (mitochondrial respiratory chain complex I assembly) is the only remaining choice consistent with an FAD-dependent oxidoreductase in a eukaryotic organism, as FAD is a cofactor in Complex I and assembly factors often retain oxidoreductase domains.


**Missing item-specific fact**

> The specific assignment to 'assembly' (as opposed to catalytic NADH dehydrogenase activity or another FAD-dependent process) relies on knowing that FOXRED1 acts as an assembly factor rather than a structural subunit. However, since the other three options are eliminable by general biological reasoning, the correct answer can be reached by elimination without this item-specific fact.


**Reason**

> Three of four options can be robustly eliminated using general biological knowledge: A is impossible in Drosophila (no IL-12), B requires transmembrane topology absent here, C requires kinase domains absent here. The FAD-binding domain is consistent with mitochondrial electron-transport-chain biology, making D the only viable remaining option. While positive identification of 'assembly' specifically benefits from knowing FOXRED1's annotated role, the elimination pathway provides meaningful grounds to select D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are clearly incompatible with the sequence features and organism. Option D is the only remaining biologically plausible choice. No two options are simultaneously defensible.


### Important caveats

- The GO annotation for GO:0032981 uses evidence code IBA:GO_Central (computational inference by association), not direct experimental evidence on this specific protein. The FUNCTION comment uses ECO:0000305 (curator inference from a primary paper).
- The accession Q9VJ10 was inferred by the reviewer from dataset metadata, not provided to the evaluated model. The model must identify the protein from sequence alone.
- The FAD-binding motif is shared across many oxidoreductases; the specific link to 'complex I assembly' rather than another FAD-dependent process is strengthened by elimination of the other three options but is not uniquely derivable from the FAD motif alone.
- The historical entry (version 178, released 2026-01) already contains the function annotation and GO term, so the answer was available in the source database at or before the benchmark construction date.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical FAD-binding Rossmann-fold motif (GGGVGSSIAYWLKEKARDGLNVVVVE), indicating an oxidoreductase. Option A (positive regulation of IL-12 production) can be eliminated because Drosophila melanogaster lacks interleukin-12, a mammalian-specific cytokine; no immune-signaling motifs are present. Option B (nickel cation transport) requires transmembrane helices and His-rich metal-binding motifs, neither of which appear in this soluble protein. Option C (stress-activated MAPK cascade) requires protein-kinase domain motifs (e.g., VAIK, HRD, DFG), which are absent. By elimination, option D (mitochondrial respiratory chain complex I assembly) is the only remaining choice consistent with an FAD-dependent oxidoreductase in a eukaryotic organism, as FAD is a cofactor in Complex I and assembly factors often retain oxidoreductase domains.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific assignment to 'assembly' (as opposed to catalytic NADH dehydrogenase activity or another FAD-dependent process) relies on knowing that FOXRED1 acts as an assembly factor rather than a structural subunit. However, since the other three options are eliminable by general biological reasoning, the correct answer can be reached by elimination without this item-specific fact.",
    "reason": "Three of four options can be robustly eliminated using general biological knowledge: A is impossible in Drosophila (no IL-12), B requires transmembrane topology absent here, C requires kinase domains absent here. The FAD-binding domain is consistent with mitochondrial electron-transport-chain biology, making D the only viable remaining option. While positive identification of 'assembly' specifically benefits from knowing FOXRED1's annotated role, the elimination pathway provides meaningful grounds to select D."
  },
  "case_id": "GO_biological_process_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VJ10 (dFOXRED1, Drosophila melanogaster). The UniProt FUNCTION comment (ECO:0000305, citing PubMed:34386730) states 'Involved in the assembly of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I).' The GO annotation GO:0032981 'mitochondrial respiratory chain complex I assembly' is present (evidence code IBA:GO_Central). The primary reference (Murari et al. 2021, IScience) reports experimental work on NDUFAF3/NDUFAF4 homologs in complex I biogenesis. The FAD-binding Rossmann-fold motif (GGGVGSSIAYWLKEKARDGLNVVVVE) is consistent with FOXRED1's oxidoreductase domain. The expected answer D is supported by both the curated function statement and the GO annotation."
  },
  "important_caveats": [
    "The GO annotation for GO:0032981 uses evidence code IBA:GO_Central (computational inference by association), not direct experimental evidence on this specific protein. The FUNCTION comment uses ECO:0000305 (curator inference from a primary paper).",
    "The accession Q9VJ10 was inferred by the reviewer from dataset metadata, not provided to the evaluated model. The model must identify the protein from sequence alone.",
    "The FAD-binding motif is shared across many oxidoreductases; the specific link to 'complex I assembly' rather than another FAD-dependent process is strengthened by elimination of the other three options but is not uniquely derivable from the FAD motif alone.",
    "The historical entry (version 178, released 2026-01) already contains the function annotation and GO term, so the answer was available in the source database at or before the benchmark construction date."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with the sequence features and organism. Option D is the only remaining biologically plausible choice. No two options are simultaneously defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VJ10 (dFOXRED1, Drosophila melanogaster). The UniProt FUNCTION comment (ECO:0000305, citing PubMed:34386730) states 'Involved in the assembly of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I).' The GO annotation GO:0032981 'mitochondrial respiratory chain complex I assembly' is present (evidence code IBA:GO_Central). The primary reference (Murari et al. 2021, IScience) reports experimental work on NDUFAF3/NDUFAF4 homologs in complex I biogenesis. The FAD-binding Rossmann-fold motif (GGGVGSSIAYWLKEKARDGLNVVVVE) is consistent with FOXRED1's oxidoreductase domain. The expected answer D is supported by both the curated function statement and the GO annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical FAD-binding Rossmann-fold motif (GGGVGSSIAYWLKEKARDGLNVVVVE), indicating an oxidoreductase. Option A (positive regulation of IL-12 production) can be eliminated because Drosophila melanogaster lacks interleukin-12, a mammalian-specific cytokine; no immune-signaling motifs are present. Option B (nickel cation transport) requires transmembrane helices and His-rich metal-binding motifs, neither of which appear in this soluble protein. Option C (stress-activated MAPK cascade) requires protein-kinase domain motifs (e.g., VAIK, HRD, DFG), which are absent. By elimination, option D (mitochondrial respiratory chain complex I assembly) is the only remaining choice consistent with an FAD-dependent oxidoreductase in a eukaryotic organism, as FAD is a cofactor in Complex I and assembly factors often retain oxidoreductase domains.",
    "missing_item_specific_fact": "The specific assignment to 'assembly' (as opposed to catalytic NADH dehydrogenase activity or another FAD-dependent process) relies on knowing that FOXRED1 acts as an assembly factor rather than a structural subunit. However, since the other three options are eliminable by general biological reasoning, the correct answer can be reached by elimination without this item-specific fact.",
    "reason": "Three of four options can be robustly eliminated using general biological knowledge: A is impossible in Drosophila (no IL-12), B requires transmembrane topology absent here, C requires kinase domains absent here. The FAD-binding domain is consistent with mitochondrial electron-transport-chain biology, making D the only viable remaining option. While positive identification of 'assembly' specifically benefits from knowing FOXRED1's annotated role, the elimination pathway provides meaningful grounds to select D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with the sequence features and organism. Option D is the only remaining biologically plausible choice. No two options are simultaneously defensible."
  },
  "important_caveats": [
    "The GO annotation for GO:0032981 uses evidence code IBA:GO_Central (computational inference by association), not direct experimental evidence on this specific protein. The FUNCTION comment uses ECO:0000305 (curator inference from a primary paper).",
    "The accession Q9VJ10 was inferred by the reviewer from dataset metadata, not provided to the evaluated model. The model must identify the protein from sequence alone.",
    "The FAD-binding motif is shared across many oxidoreductases; the specific link to 'complex I assembly' rather than another FAD-dependent process is strengthened by elimination of the other three options but is not uniquely derivable from the FAD motif alone.",
    "The historical entry (version 178, released 2026-01) already contains the function annotation and GO term, so the answer was available in the source database at or before the benchmark construction date."
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

**Accession:** `Q9VJ10` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 178. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
"Q9VJ10"
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0002021","source":"FlyBase"}],"value":"Protein lethal (2) 37Bb"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34386730","source":"PubMed"}],"value":"FAD-dependent oxidoreductase domain-containing protein 1 homolog"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34386730","source":"PubMed"}],"value":"dFOXRED1"}]}}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"34386730","source":"PubMed"}],"value":"Involved in the assembly of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I)"}]}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/uniProtKBCrossReferences/29`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"database":"GO","id":"GO:0032981","properties":[{"key":"GoTerm","value":"P:mitochondrial respiratory chain complex I assembly"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"citation":{"authors":["Murari A.","Rhooms S.K.","Garcia C.","Liu T.","Li H.","Mishra B.","Deshong C.","Owusu-Ansah E."],"citationCrossReferences":[{"database":"PubMed","id":"34386730"},{"database":"DOI","id":"10.1016/j.isci.2021.102869"}],"citationType":"journal article","firstPage":"102869","id":"34386730","journal":"IScience","lastPage":"102869","publicationDate":"2021","title":"Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in mitochondrial complex I biogenesis.","volume":"24"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","INTERACTION WITH COMPLEX 1"]}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)  
**Locator:** `lines 81-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:33:26.250109+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, AND INTERACTION WITH COMPLEX 1.
RX   PubMed=34386730; DOI=10.1016/j.isci.2021.102869;
RA   Murari A., Rhooms S.K., Garcia C., Liu T., Li H., Mishra B., Deshong C.,
RA   Owusu-Ansah E.;
RT   "Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in
RT   mitochondrial complex I biogenesis.";
RL   IScience 24:102869-102869(2021).
```

Source SHA-256: `4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:33:26.250109+00:00.  

```text
CC   -!- FUNCTION: Involved in the assembly of the mitochondrial membrane
CC       respiratory chain NADH dehydrogenase (Complex I).
CC       {ECO:0000305|PubMed:34386730}.
```

Source SHA-256: `4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)  
**Locator:** `lines 132-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:33:26.250109+00:00.  

```text
DR   GO; GO:0032981; P:mitochondrial respiratory chain complex I assembly; IBA:GO_Central.
```

Source SHA-256: `4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 159. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
