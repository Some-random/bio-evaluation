# catalytic_activity_0144

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — inosine(in) = inosine(out)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTSSDSAMVNHTPSPWYKFGFKSFAEFNTYVTFVFLGMSIMMVASAVTSAPDFLTRYYVYATGDPDAVAETPLFWNNANTFYNAGTYVLQVLTELFSLTPFMRRIPLSVRLFVGLGIPFAELLLIIIVPAATIKSQHGAIAVIMVVACVGGFSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALLMSIIQIILKVSMGTSFHDILTMSRIYFGICIGIQLFAIFELAILRFNPFAQKYIAEYRAGAQRNAQNNESTLEETAPSMNEPAAGDIADLPATVDDKERALNEEEGDEVRAVTSEEFHVKRGAVLTATGDADKMVDLDQTGNITSTEQLLRASAASVFKRVYPMLVCVFLIYFTSLLTFPGVFFLVSTTSGWYMTVIVTLFNAGDFISRMVLMFRPLRPSPKVVVAGTLGRLIIIPFLVLCVRGIIRGEALPYVLITLLGLTNGYFGCMACIHCPRTTTLRYAGERSLAAMLSGISIMLGLCFGSNLSLAITLTH

[Multiple Choices]
A. lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol
B. inosine(in) = inosine(out)
C. Mg(2+)(in) = Mg(2+)(out)
D. a primary alcohol + NAD(+) = an aldehyde + NADH + H(+)
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

> The exact 502-aa sequence matches the UniProt entry for Crithidia fasciculata nucleoside transporter 2. That entry annotates inosine transport and cites experimental evidence from two publications, supporting choice B for this sequence. The cited papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic and consistent with a multipass membrane transporter, which weighs against the soluble-enzyme reactions in A and D. That does not distinguish inosine transport in B from magnesium transport in C.


**Missing item-specific fact**

> The protein's specific transported substrate—inosine—requires protein-specific functional annotation or experimental evidence absent from the input.


**Reason**

> General sequence features suggest membrane transport, but do not establish this transporter's substrate specificity; identifying the exact sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports B; it does not support another listed choice. The sequence alone, however, does not resolve the distinction between B and another transport reaction such as C.


### Important caveats

- Choice B describes translocation, not a conventional chemical transformation, so the task's label “Enzymatic Reaction Prediction” is imprecise.
- The database annotation cites experimental evidence, but the underlying papers were not independently validated here; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multipass membrane transporter, which weighs against the soluble-enzyme reactions in A and D. That does not distinguish inosine transport in B from magnesium transport in C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific transported substrate—inosine—requires protein-specific functional annotation or experimental evidence absent from the input.",
    "reason": "General sequence features suggest membrane transport, but do not establish this transporter's substrate specificity; identifying the exact sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "case_id": "catalytic_activity_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact 502-aa sequence matches the UniProt entry for Crithidia fasciculata nucleoside transporter 2. That entry annotates inosine transport and cites experimental evidence from two publications, supporting choice B for this sequence. The cited papers were not independently reviewed here."
  },
  "important_caveats": [
    "Choice B describes translocation, not a conventional chemical transformation, so the task's label “Enzymatic Reaction Prediction” is imprecise.",
    "The database annotation cites experimental evidence, but the underlying papers were not independently validated here; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports B; it does not support another listed choice. The sequence alone, however, does not resolve the distinction between B and another transport reaction such as C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 502-aa sequence matches the UniProt entry for Crithidia fasciculata nucleoside transporter 2. That entry annotates inosine transport and cites experimental evidence from two publications, supporting choice B for this sequence. The cited papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multipass membrane transporter, which weighs against the soluble-enzyme reactions in A and D. That does not distinguish inosine transport in B from magnesium transport in C.",
    "missing_item_specific_fact": "The protein's specific transported substrate—inosine—requires protein-specific functional annotation or experimental evidence absent from the input.",
    "reason": "General sequence features suggest membrane transport, but do not establish this transporter's substrate specificity; identifying the exact sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports B; it does not support another listed choice. The sequence alone, however, does not resolve the distinction between B and another transport reaction such as C."
  },
  "important_caveats": [
    "Choice B describes translocation, not a conventional chemical transformation, so the task's label “Enzymatic Reaction Prediction” is imprecise.",
    "The database annotation cites experimental evidence, but the underlying papers were not independently validated here; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9GTP4 (NT2_CRIFA, Nucleoside transporter 2 / CfNT2 from Crithidia fasciculata) explicitly lists 'inosine(in) = inosine(out)' as a CATALYTIC ACTIVITY with experimental evidence codes ECO:0000269 (inferred from direct assay) from PubMed:15694482 and PubMed:20037157. The sequence matches exactly (502 AA, SHA256 match). The annotation is experimentally supported, not merely computational.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C1](#evidence-c1), [C4](#evidence-c4), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a polytopic membrane protein with approximately 11 transmembrane helices (readily identifiable from the long hydrophobic stretches). Among the four choices: (D) alcohol dehydrogenase is a soluble cytoplasmic enzyme with no TM domains — ruled out; (A) lipid A phosphoethanolamine transferase (EptA-type) is a single-pass membrane protein with a large cytoplasmic catalytic domain — inconsistent with 11 TM domains; (C) Mg2+ transporters of the well-characterized CorA (2 TM) and MgtE (5 TM) families have far fewer TM domains — inconsistent. The 11-TM topology with characteristic motifs (e.g., the 'GTLG' motif near the C-terminal region, N-terminal 'NANTFY' segment) is the hallmark of the Equilibrative Nucleoside Transporter (ENT) family, whose defining function is equilibrative nucleoside translocation (e.g., inosine transport). Thus the topology and motif pattern provide a concrete biological argument favoring B over A, C, and D.


**Missing item-specific fact**

> None essential. While precise substrate specificity (inosine vs. guanosine vs. adenosine) within the ENT family would require experimental data, the question only requires distinguishing a nucleoside transporter from an ion transporter, a lipid-modifying enzyme, and a dehydrogenase — a distinction achievable from topology and family-level motifs.


**Reason**

> A biologist familiar with membrane protein topology can count ~11 TM helices from the hydrophobicity pattern and match this to the ENT family architecture, thereby eliminating the single-pass (A), low-TM (C), and soluble (D) alternatives. This constitutes a concrete, general biological argument rather than a protein-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry also lists guanosine transport as a catalytic activity, this is not among the four choices. Among A–D, only B is consistent with the protein's topology and family assignment. No ambiguity among the provided options.


### Important caveats

- The UniProt annotation for inosine transport is experimentally supported (ECO:0000269, direct assay), not merely inferred by similarity.
- The 11-TM topology argument requires familiarity with ENT family architecture; a model without this knowledge would struggle, but this is general membrane-protein biology, not a protein-specific lookup.
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning argument stands independently from the sequence data.
- The historical UniProt record (entry version 55, first released 2026-01-28) post-dates the original sequence submission (2001-03-01); the author's source snapshot is unknown, but the sequence itself has been unchanged since 2001.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a polytopic membrane protein with approximately 11 transmembrane helices (readily identifiable from the long hydrophobic stretches). Among the four choices: (D) alcohol dehydrogenase is a soluble cytoplasmic enzyme with no TM domains — ruled out; (A) lipid A phosphoethanolamine transferase (EptA-type) is a single-pass membrane protein with a large cytoplasmic catalytic domain — inconsistent with 11 TM domains; (C) Mg2+ transporters of the well-characterized CorA (2 TM) and MgtE (5 TM) families have far fewer TM domains — inconsistent. The 11-TM topology with characteristic motifs (e.g., the 'GTLG' motif near the C-terminal region, N-terminal 'NANTFY' segment) is the hallmark of the Equilibrative Nucleoside Transporter (ENT) family, whose defining function is equilibrative nucleoside translocation (e.g., inosine transport). Thus the topology and motif pattern provide a concrete biological argument favoring B over A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None essential. While precise substrate specificity (inosine vs. guanosine vs. adenosine) within the ENT family would require experimental data, the question only requires distinguishing a nucleoside transporter from an ion transporter, a lipid-modifying enzyme, and a dehydrogenase — a distinction achievable from topology and family-level motifs.",
    "reason": "A biologist familiar with membrane protein topology can count ~11 TM helices from the hydrophobicity pattern and match this to the ENT family architecture, thereby eliminating the single-pass (A), low-TM (C), and soluble (D) alternatives. This constitutes a concrete, general biological argument rather than a protein-specific database lookup."
  },
  "case_id": "catalytic_activity_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C1",
      "C4",
      "C7",
      "C8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9GTP4 (NT2_CRIFA, Nucleoside transporter 2 / CfNT2 from Crithidia fasciculata) explicitly lists 'inosine(in) = inosine(out)' as a CATALYTIC ACTIVITY with experimental evidence codes ECO:0000269 (inferred from direct assay) from PubMed:15694482 and PubMed:20037157. The sequence matches exactly (502 AA, SHA256 match). The annotation is experimentally supported, not merely computational."
  },
  "important_caveats": [
    "The UniProt annotation for inosine transport is experimentally supported (ECO:0000269, direct assay), not merely inferred by similarity.",
    "The 11-TM topology argument requires familiarity with ENT family architecture; a model without this knowledge would struggle, but this is general membrane-protein biology, not a protein-specific lookup.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning argument stands independently from the sequence data.",
    "The historical UniProt record (entry version 55, first released 2026-01-28) post-dates the original sequence submission (2001-03-01); the author's source snapshot is unknown, but the sequence itself has been unchanged since 2001."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry also lists guanosine transport as a catalytic activity, this is not among the four choices. Among A–D, only B is consistent with the protein's topology and family assignment. No ambiguity among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9GTP4 (NT2_CRIFA, Nucleoside transporter 2 / CfNT2 from Crithidia fasciculata) explicitly lists 'inosine(in) = inosine(out)' as a CATALYTIC ACTIVITY with experimental evidence codes ECO:0000269 (inferred from direct assay) from PubMed:15694482 and PubMed:20037157. The sequence matches exactly (502 AA, SHA256 match). The annotation is experimentally supported, not merely computational.",
    "evidence_ids": ["C5", "H5", "C1", "C4", "C7", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence encodes a polytopic membrane protein with approximately 11 transmembrane helices (readily identifiable from the long hydrophobic stretches). Among the four choices: (D) alcohol dehydrogenase is a soluble cytoplasmic enzyme with no TM domains — ruled out; (A) lipid A phosphoethanolamine transferase (EptA-type) is a single-pass membrane protein with a large cytoplasmic catalytic domain — inconsistent with 11 TM domains; (C) Mg2+ transporters of the well-characterized CorA (2 TM) and MgtE (5 TM) families have far fewer TM domains — inconsistent. The 11-TM topology with characteristic motifs (e.g., the 'GTLG' motif near the C-terminal region, N-terminal 'NANTFY' segment) is the hallmark of the Equilibrative Nucleoside Transporter (ENT) family, whose defining function is equilibrative nucleoside translocation (e.g., inosine transport). Thus the topology and motif pattern provide a concrete biological argument favoring B over A, C, and D.",
    "missing_item_specific_fact": "None essential. While precise substrate specificity (inosine vs. guanosine vs. adenosine) within the ENT family would require experimental data, the question only requires distinguishing a nucleoside transporter from an ion transporter, a lipid-modifying enzyme, and a dehydrogenase — a distinction achievable from topology and family-level motifs.",
    "reason": "A biologist familiar with membrane protein topology can count ~11 TM helices from the hydrophobicity pattern and match this to the ENT family architecture, thereby eliminating the single-pass (A), low-TM (C), and soluble (D) alternatives. This constitutes a concrete, general biological argument rather than a protein-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry also lists guanosine transport as a catalytic activity, this is not among the four choices. Among A–D, only B is consistent with the protein's topology and family assignment. No ambiguity among the provided options."
  },
  "important_caveats": [
    "The UniProt annotation for inosine transport is experimentally supported (ECO:0000269, direct assay), not merely inferred by similarity.",
    "The 11-TM topology argument requires familiarity with ENT family architecture; a model without this knowledge would struggle, but this is general membrane-protein biology, not a protein-specific lookup.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning argument stands independently from the sequence data.",
    "The historical UniProt record (entry version 55, first released 2026-01-28) post-dates the original sequence submission (2001-03-01); the author's source snapshot is unknown, but the sequence itself has been unchanged since 2001."
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

**Accession:** `Q9GTP4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 55. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
"Q9GTP4"
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAG22611.1","source":"EMBL"}],"lineage":["Eukaryota","Discoba","Euglenozoa","Kinetoplastea","Metakinetoplastina","Trypanosomatida","Trypanosomatidae","Leishmaniinae","Crithidia"],"scientificName":"Crithidia fasciculata","taxonId":5656}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20037157","source":"PubMed"}],"value":"Equilibrative nucleoside transporter 2"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"15694482","source":"PubMed"}],"value":"Nucleoside transporter 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"15694482","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"20037157","source":"PubMed"}],"value":"CfNT2"}]}}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"15694482","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"20037157","source":"PubMed"}],"name":"inosine(in) = inosine(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:75375"},{"database":"ChEBI","id":"CHEBI:17596"}]}}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"citation":{"authors":["Liu W.","Arendt C.S.","Gessford S.K.","Ntaba D.","Carter N.S.","Ullman B."],"citationCrossReferences":[{"database":"PubMed","id":"15694482"},{"database":"DOI","id":"10.1016/j.molbiopara.2004.11.018"}],"citationType":"journal article","firstPage":"1","id":"15694482","journal":"Mol. Biochem. Parasitol.","lastPage":"12","publicationDate":"2005","title":"Identification and characterization of purine nucleoside transporters from Crithidia fasciculata.","volume":"140"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","TRANSPORTER ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","INDUCTION"]}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"citation":{"authors":["Arendt C.S.","Ullman B."],"citationCrossReferences":[{"database":"PubMed","id":"20037157"},{"database":"DOI","id":"10.1074/jbc.m109.074351"}],"citationType":"journal article","firstPage":"6024","id":"20037157","journal":"J. Biol. Chem.","lastPage":"6035","publicationDate":"2010","title":"Role of transmembrane domain 4 in ligand permeation by Crithidia fasciculata equilibrative nucleoside transporter 2 (CfNT2).","volume":"285"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","TRANSPORTER ACTIVITY","SUBCELLULAR LOCATION","MUTAGENESIS OF VAL-89; HIS-138; GLY-139; ALA-140; ILE-141; ALA-142; VAL-143; ILE-144; MET-145; VAL-146; VAL-147; ALA-148; VAL-150; GLY-151; GLY-152; PHE-153; SER-154; LYS-155; ALA-156; LEU-157; ASP-159; SER-160; THR-162; ASN-163; ALA-164; LEU-165; VAL-166; GLY-167; PRO-168; PHE-169; PRO-170; THR-171 AND LYS-172"]}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 41-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=inosine(in) = inosine(out); Xref=Rhea:RHEA:75375,
CC         ChEBI:CHEBI:17596; Evidence={ECO:0000269|PubMed:15694482,
CC         ECO:0000269|PubMed:20037157};
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 144. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
