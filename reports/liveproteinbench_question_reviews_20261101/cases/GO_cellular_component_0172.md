# GO_cellular_component_0172

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDTTMLQNAMQTDQAESKDLMNLAFFVRIIGLGVLPSVLVAVAKVNYPTWGKGLIQRAMTWGVSLVLLLVPIGLFSSQYASFFRVHKPVRFYINPITPIYSVGKLASIEYKKATAPTDTIYHAKDAVQTTKPSERKPRLVVFVVGETARADHVQFNGYGRETFPQLAKVDGLANFSQVTSCGTSTAYSVPCMFSYLGQDDYDVDTAKYQENVLDTLDRLGVGILWRDNNSDSKGVMDKLPATQYFDYKSATNNTICNTNPYNECRDVGMLVGLDDYVSANNGKDMLIMLHQMGNHGPAYFKRYDEQFAKFTPVCEGNELAKCEHQSLINAYDNALLATDDFIAKSIDWLKTHEANYDVAMLYVSDHGESLGENGVYLHGMPNAFAPKEQRAVPAFFWSNNTTFKPTASDTVLTHDAITPTLLKLFDVTAGKVKDRAAFIQ

[Multiple Choices]
A. rhoptry
B. plasma membrane
C. endomembrane system
D. vitelline envelope
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated to the cell inner membrane and GO plasma membrane. This supports B, but the location annotation is transferred by similarity and the GO assignment is computational, not direct experimental localization evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Several strongly hydrophobic sequence regions support membrane association and make rhoptry or vitelline-envelope localization unlikely. They do not, by themselves, distinguish plasma membrane from other membrane-system locations.


**Missing item-specific fact**

> The protein's identity/function and its bacterial cell-inner-membrane localization, or equivalent protein-specific localization evidence, are absent from the input.


**Reason**

> The sequence offers a general membrane-protein clue, but selecting B over C requires additional context or a protein-specific annotation; recognizing the sequence or retrieving its database record would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The GO definition of endomembrane system includes the cell membrane, so C can overlap conceptually with B. For this bacterial protein, B is the more specific and supported choice, but the options are not strictly disjoint.


### Important caveats

- The supplied sequence does not identify the organism; its E. coli source is reviewer-only evidence.
- The matched historical record also supports the annotation, but the author's exact source snapshot is unknown.
- The available localization evidence is annotation-based and transferred by similarity, not verified here against primary experimental localization data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several strongly hydrophobic sequence regions support membrane association and make rhoptry or vitelline-envelope localization unlikely. They do not, by themselves, distinguish plasma membrane from other membrane-system locations.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity/function and its bacterial cell-inner-membrane localization, or equivalent protein-specific localization evidence, are absent from the input.",
    "reason": "The sequence offers a general membrane-protein clue, but selecting B over C requires additional context or a protein-specific annotation; recognizing the sequence or retrieving its database record would be lookup, not reasoning from the supplied input."
  },
  "case_id": "GO_cellular_component_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to the cell inner membrane and GO plasma membrane. This supports B, but the location annotation is transferred by similarity and the GO assignment is computational, not direct experimental localization evidence."
  },
  "important_caveats": [
    "The supplied sequence does not identify the organism; its E. coli source is reviewer-only evidence.",
    "The matched historical record also supports the annotation, but the author's exact source snapshot is unknown.",
    "The available localization evidence is annotation-based and transferred by similarity, not verified here against primary experimental localization data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The GO definition of endomembrane system includes the cell membrane, so C can overlap conceptually with B. For this bacterial protein, B is the more specific and supported choice, but the options are not strictly disjoint."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to the cell inner membrane and GO plasma membrane. This supports B, but the location annotation is transferred by similarity and the GO assignment is computational, not direct experimental localization evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Several strongly hydrophobic sequence regions support membrane association and make rhoptry or vitelline-envelope localization unlikely. They do not, by themselves, distinguish plasma membrane from other membrane-system locations.",
    "missing_item_specific_fact": "The protein's identity/function and its bacterial cell-inner-membrane localization, or equivalent protein-specific localization evidence, are absent from the input.",
    "reason": "The sequence offers a general membrane-protein clue, but selecting B over C requires additional context or a protein-specific annotation; recognizing the sequence or retrieving its database record would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The GO definition of endomembrane system includes the cell membrane, so C can overlap conceptually with B. For this bacterial protein, B is the more specific and supported choice, but the options are not strictly disjoint."
  },
  "important_caveats": [
    "The supplied sequence does not identify the organism; its E. coli source is reviewer-only evidence.",
    "The matched historical record also supports the annotation, but the author's exact source snapshot is unknown.",
    "The available localization evidence is annotation-based and transferred by similarity, not verified here against primary experimental localization data."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is MCR-2 (phosphatidylethanolamine transferase), a multi-pass membrane protein annotated at the 'Cell inner membrane' in UniProt (C5/H3). The GO cross-reference maps this to GO:0005886 'plasma membrane' (C6/H4), which explicitly includes 'bacterial inner membrane' as a NARROW synonym (GO1). The annotation evidence code is ISS (inferred from sequence similarity, ECO:0000250), not direct experimental localization, but the protein's multi-pass membrane topology (ECO:0000255) and structural characterization (PDB 6A7W, C7/H2) are consistent with plasma membrane localization. In bacteria, the plasma membrane IS the inner membrane, making 'plasma membrane' the correct GO cellular component term.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long hydrophobic stretches (e.g., residues ~12-30, ~55-75, ~85-110, ~120-145, ~155-180) consistent with multi-pass transmembrane topology, clearly indicating a membrane-embedded protein. Critically, there is no cleavable N-terminal signal peptide (the N-terminal hydrophobic region is followed by additional TM segments rather than a polar domain, inconsistent with signal peptide cleavage), no mitochondrial targeting sequence, no nuclear localization signal, and no ER-retention or Golgi-targeting motifs. The sequence composition (high hydrophobicity, absence of N-glycosylation sequons, prokaryotic-like amino acid distribution) is consistent with a bacterial membrane enzyme rather than a eukaryotic endomembrane component. Rhoptry (apicomplexan parasite organelle) and vitelline envelope (egg coat glycoprotein structure) are eliminable by general biological reasoning as they are highly specialized eukaryotic/parasite structures incompatible with a multi-pass membrane enzyme of bacterial character. The absence of eukaryotic targeting features argues against the endomembrane system (ER/Golgi/vesicle pathway) and in favor of direct plasma membrane insertion.


**Missing item-specific fact**

> The organism identity (Escherichia coli) is not provided in the input. Without this, the distinction between 'plasma membrane' and 'endomembrane system' is somewhat weakened because the GO definition of endomembrane system (GO2) technically includes 'cell membrane' as a component. However, the sequence's prokaryotic character and lack of eukaryotic targeting signals provide reasonable grounds to favor plasma membrane.


**Reason**

> The sequence provides concrete features (multiple TM domains, absence of signal peptide and eukaryotic targeting motifs, prokaryotic-like composition) that support a membrane-protein-at-plasma-membrane conclusion through general biological reasoning. The elimination of rhoptry and vitelline envelope is straightforward. The B-vs-C distinction is supported by the absence of eukaryotic secretory-pathway targeting features, though the GO definition overlap slightly weakens this.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the GO definition of endomembrane system (GO:0012505) includes 'cell membrane' as a component, in standard GO annotation practice, a multi-pass membrane protein in a prokaryotic-appearing sequence is annotated to 'plasma membrane' (GO:0005886) rather than the broader 'endomembrane system' term. The other two options (rhoptry, vitelline envelope) are clearly incompatible with the sequence characteristics. No other option is genuinely defensible.


### Important caveats

- The GO annotation evidence code is ISS (inferred from sequence similarity to A0A0R6L508), not direct experimental localization. The membrane topology annotation (ECO:0000255) is also inferred by similarity.
- The organism identity (E. coli) is not provided in the model input; the reasoning that this is a bacterial protein (and thus lacks an endomembrane system) relies on inferring prokaryotic character from sequence composition.
- The GO definition of 'endomembrane system' (GO:0012505) technically lists 'cell membrane' as a component, creating a minor definitional overlap with 'plasma membrane' that could theoretically make C partially defensible, though standard annotation practice resolves this in favor of B.
- The identity of this protein as MCR-2 was determined by reviewer-only accession lookup; the evaluated model only sees the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches (e.g., residues ~12-30, ~55-75, ~85-110, ~120-145, ~155-180) consistent with multi-pass transmembrane topology, clearly indicating a membrane-embedded protein. Critically, there is no cleavable N-terminal signal peptide (the N-terminal hydrophobic region is followed by additional TM segments rather than a polar domain, inconsistent with signal peptide cleavage), no mitochondrial targeting sequence, no nuclear localization signal, and no ER-retention or Golgi-targeting motifs. The sequence composition (high hydrophobicity, absence of N-glycosylation sequons, prokaryotic-like amino acid distribution) is consistent with a bacterial membrane enzyme rather than a eukaryotic endomembrane component. Rhoptry (apicomplexan parasite organelle) and vitelline envelope (egg coat glycoprotein structure) are eliminable by general biological reasoning as they are highly specialized eukaryotic/parasite structures incompatible with a multi-pass membrane enzyme of bacterial character. The absence of eukaryotic targeting features argues against the endomembrane system (ER/Golgi/vesicle pathway) and in favor of direct plasma membrane insertion.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The organism identity (Escherichia coli) is not provided in the input. Without this, the distinction between 'plasma membrane' and 'endomembrane system' is somewhat weakened because the GO definition of endomembrane system (GO2) technically includes 'cell membrane' as a component. However, the sequence's prokaryotic character and lack of eukaryotic targeting signals provide reasonable grounds to favor plasma membrane.",
    "reason": "The sequence provides concrete features (multiple TM domains, absence of signal peptide and eukaryotic targeting motifs, prokaryotic-like composition) that support a membrane-protein-at-plasma-membrane conclusion through general biological reasoning. The elimination of rhoptry and vitelline envelope is straightforward. The B-vs-C distinction is supported by the absence of eukaryotic secretory-pathway targeting features, though the GO definition overlap slightly weakens this."
  },
  "case_id": "GO_cellular_component_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The protein is MCR-2 (phosphatidylethanolamine transferase), a multi-pass membrane protein annotated at the 'Cell inner membrane' in UniProt (C5/H3). The GO cross-reference maps this to GO:0005886 'plasma membrane' (C6/H4), which explicitly includes 'bacterial inner membrane' as a NARROW synonym (GO1). The annotation evidence code is ISS (inferred from sequence similarity, ECO:0000250), not direct experimental localization, but the protein's multi-pass membrane topology (ECO:0000255) and structural characterization (PDB 6A7W, C7/H2) are consistent with plasma membrane localization. In bacteria, the plasma membrane IS the inner membrane, making 'plasma membrane' the correct GO cellular component term."
  },
  "important_caveats": [
    "The GO annotation evidence code is ISS (inferred from sequence similarity to A0A0R6L508), not direct experimental localization. The membrane topology annotation (ECO:0000255) is also inferred by similarity.",
    "The organism identity (E. coli) is not provided in the model input; the reasoning that this is a bacterial protein (and thus lacks an endomembrane system) relies on inferring prokaryotic character from sequence composition.",
    "The GO definition of 'endomembrane system' (GO:0012505) technically lists 'cell membrane' as a component, creating a minor definitional overlap with 'plasma membrane' that could theoretically make C partially defensible, though standard annotation practice resolves this in favor of B.",
    "The identity of this protein as MCR-2 was determined by reviewer-only accession lookup; the evaluated model only sees the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the GO definition of endomembrane system (GO:0012505) includes 'cell membrane' as a component, in standard GO annotation practice, a multi-pass membrane protein in a prokaryotic-appearing sequence is annotated to 'plasma membrane' (GO:0005886) rather than the broader 'endomembrane system' term. The other two options (rhoptry, vitelline envelope) are clearly incompatible with the sequence characteristics. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is MCR-2 (phosphatidylethanolamine transferase), a multi-pass membrane protein annotated at the 'Cell inner membrane' in UniProt (C5/H3). The GO cross-reference maps this to GO:0005886 'plasma membrane' (C6/H4), which explicitly includes 'bacterial inner membrane' as a NARROW synonym (GO1). The annotation evidence code is ISS (inferred from sequence similarity, ECO:0000250), not direct experimental localization, but the protein's multi-pass membrane topology (ECO:0000255) and structural characterization (PDB 6A7W, C7/H2) are consistent with plasma membrane localization. In bacteria, the plasma membrane IS the inner membrane, making 'plasma membrane' the correct GO cellular component term.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO1", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches (e.g., residues ~12-30, ~55-75, ~85-110, ~120-145, ~155-180) consistent with multi-pass transmembrane topology, clearly indicating a membrane-embedded protein. Critically, there is no cleavable N-terminal signal peptide (the N-terminal hydrophobic region is followed by additional TM segments rather than a polar domain, inconsistent with signal peptide cleavage), no mitochondrial targeting sequence, no nuclear localization signal, and no ER-retention or Golgi-targeting motifs. The sequence composition (high hydrophobicity, absence of N-glycosylation sequons, prokaryotic-like amino acid distribution) is consistent with a bacterial membrane enzyme rather than a eukaryotic endomembrane component. Rhoptry (apicomplexan parasite organelle) and vitelline envelope (egg coat glycoprotein structure) are eliminable by general biological reasoning as they are highly specialized eukaryotic/parasite structures incompatible with a multi-pass membrane enzyme of bacterial character. The absence of eukaryotic targeting features argues against the endomembrane system (ER/Golgi/vesicle pathway) and in favor of direct plasma membrane insertion.",
    "missing_item_specific_fact": "The organism identity (Escherichia coli) is not provided in the input. Without this, the distinction between 'plasma membrane' and 'endomembrane system' is somewhat weakened because the GO definition of endomembrane system (GO2) technically includes 'cell membrane' as a component. However, the sequence's prokaryotic character and lack of eukaryotic targeting signals provide reasonable grounds to favor plasma membrane.",
    "reason": "The sequence provides concrete features (multiple TM domains, absence of signal peptide and eukaryotic targeting motifs, prokaryotic-like composition) that support a membrane-protein-at-plasma-membrane conclusion through general biological reasoning. The elimination of rhoptry and vitelline envelope is straightforward. The B-vs-C distinction is supported by the absence of eukaryotic secretory-pathway targeting features, though the GO definition overlap slightly weakens this."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the GO definition of endomembrane system (GO:0012505) includes 'cell membrane' as a component, in standard GO annotation practice, a multi-pass membrane protein in a prokaryotic-appearing sequence is annotated to 'plasma membrane' (GO:0005886) rather than the broader 'endomembrane system' term. The other two options (rhoptry, vitelline envelope) are clearly incompatible with the sequence characteristics. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The GO annotation evidence code is ISS (inferred from sequence similarity to A0A0R6L508), not direct experimental localization. The membrane topology annotation (ECO:0000255) is also inferred by similarity.",
    "The organism identity (E. coli) is not provided in the model input; the reasoning that this is a bacterial protein (and thus lacks an endomembrane system) relies on inferring prokaryotic character from sequence composition.",
    "The GO definition of 'endomembrane system' (GO:0012505) technically lists 'cell membrane' as a component, creating a minor definitional overlap with 'plasma membrane' that could theoretically make C partially defensible, though standard annotation practice resolves this in favor of B.",
    "The identity of this protein as MCR-2 was determined by reviewer-only accession lookup; the evaluated model only sees the raw sequence."
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

**Accession:** `A0A1C3NEV1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0R6L508","source":"UniProtKB"}],"id":"SL-0037","value":"Cell inner membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"citation":{"authors":["Wang X.","Lu Q.","Qi J.","Chai Y.","Wang Y.","Gao G.F."],"citationCrossReferences":[{"database":"PubMed","id":"30194678"},{"database":"DOI","id":"10.1007/s11427-018-9363-4"}],"citationType":"journal article","firstPage":"1432","id":"30194678","journal":"Sci. China Life Sci.","lastPage":"1436","publicationDate":"2018","title":"Structural and functional insights into MCR-2 mediated colistin resistance.","volume":"61"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6A7W","source":"PDB"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"WHI04997.1","source":"EMBL"}],"type":"PLASMID","value":"unnamed5"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+)","DISULFIDE BONDS","FUNCTION","CATALYTIC ACTIVITY","MUTAGENESIS OF PHE-91; TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283; LYS-331 AND HIS-476"]}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 44-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
RN   [4] {ECO:0007744|PDB:6A7W}
RP   X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+),
RP   DISULFIDE BONDS, FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF PHE-91;
RP   TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283;
RP   LYS-331 AND HIS-476.
RC   PLASMID=unnamed5 {ECO:0000312|EMBL:WHI04997.1};
RX   PubMed=30194678; DOI=10.1007/s11427-018-9363-4;
RA   Wang X., Lu Q., Qi J., Chai Y., Wang Y., Gao G.F.;
RT   "Structural and functional insights into MCR-2 mediated colistin
RT   resistance.";
RL   Sci. China Life Sci. 61:1432-1436(2018).
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 80-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell inner membrane
CC       {ECO:0000250|UniProtKB:A0A0R6L508}; Multi-pass membrane protein
CC       {ECO:0000255}.
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 105-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 111059-111069`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0012505
name: endomembrane system
namespace: cellular_component
def: "A collection of membranous structures involved in transport within the cell. The main components of the endomembrane system are endoplasmic reticulum, Golgi bodies, vesicles, cell membrane and nuclear envelope. Members of the endomembrane system pass materials through each other or though the use of vesicles." [GOC:lh]
subset: goslim_candida
subset: goslim_flybase_ribbon
subset: goslim_yeast
xref: Wikipedia:Endomembrane_system
is_a: GO:0110165 ! cellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 172. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
