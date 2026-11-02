# GO_cellular_component_0116

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — mitochondrion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLQRVSRRFPSLRRCGLRTASTVPTNQAQPGEVEEEVSATVKRIRSELAADKQKLKWRTPIGDRPEDWNSKLKLFSNAEQTSDFIVMMQKPIDLSPRNIRQWWENREERIERHMQQFVPERHKILGAELAAAHFILYRGGAVKFINDTHWRRASKDGEFKLPNKFDPRYKVEALRCDNMELYYEGLENLRCLDSLKFLSFHNVKSFDDWCLDRISGGGFPNLEVLDLSCTQITSNGLACLYRFPKLKLLILNDPKETLELELSTVMLEEAMPALKIVGADAIHS

[Multiple Choices]
A. mitochondrion
B. host cell plasma membrane
C. nematocyst
D. replisome
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

> The exact sequence matches a Drosophila protein with a mitochondrial GO annotation carrying IDA evidence (direct assay) from FlyBase. The historical entry also contains this annotation, although the author's precise source snapshot is unknown.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with an arginine-rich, acidic-residue-poor N-terminal region compatible with a mitochondrial targeting peptide. It lacks an obvious membrane-spanning segment or recognizable replisome-type sequence features, making mitochondrion the strongest choice among these options.


**Missing item-specific fact**

> Protein-specific localization evidence would provide stronger confirmation, but the sequence offers a meaningful targeting-signal clue that distinguishes the options.


**Reason**

> The N-terminal targeting-like region supports mitochondrial localization, while the alternatives are less compatible with the sequence. This is a defensible inference, not proof of localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Mitochondrion is the best-supported choice; the alternatives are not comparably supported by the supplied sequence.


### Important caveats

- The direct-assay annotation is reviewer-only evidence and was not supplied to the evaluated model.
- The exact author source snapshot is unknown; sequence identity is confirmed in the historical record available by the stated cutoff.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with an arginine-rich, acidic-residue-poor N-terminal region compatible with a mitochondrial targeting peptide. It lacks an obvious membrane-spanning segment or recognizable replisome-type sequence features, making mitochondrion the strongest choice among these options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Protein-specific localization evidence would provide stronger confirmation, but the sequence offers a meaningful targeting-signal clue that distinguishes the options.",
    "reason": "The N-terminal targeting-like region supports mitochondrial localization, while the alternatives are less compatible with the sequence. This is a defensible inference, not proof of localization."
  },
  "case_id": "GO_cellular_component_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a Drosophila protein with a mitochondrial GO annotation carrying IDA evidence (direct assay) from FlyBase. The historical entry also contains this annotation, although the author's precise source snapshot is unknown."
  },
  "important_caveats": [
    "The direct-assay annotation is reviewer-only evidence and was not supplied to the evaluated model.",
    "The exact author source snapshot is unknown; sequence identity is confirmed in the historical record available by the stated cutoff."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Mitochondrion is the best-supported choice; the alternatives are not comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a Drosophila protein with a mitochondrial GO annotation carrying IDA evidence (direct assay) from FlyBase. The historical entry also contains this annotation, although the author's precise source snapshot is unknown.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with an arginine-rich, acidic-residue-poor N-terminal region compatible with a mitochondrial targeting peptide. It lacks an obvious membrane-spanning segment or recognizable replisome-type sequence features, making mitochondrion the strongest choice among these options.",
    "missing_item_specific_fact": "Protein-specific localization evidence would provide stronger confirmation, but the sequence offers a meaningful targeting-signal clue that distinguishes the options.",
    "reason": "The N-terminal targeting-like region supports mitochondrial localization, while the alternatives are less compatible with the sequence. This is a defensible inference, not proof of localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Mitochondrion is the best-supported choice; the alternatives are not comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The direct-assay annotation is reviewer-only evidence and was not supplied to the evaluated model.",
    "The exact author source snapshot is unknown; sequence identity is confirmed in the historical record available by the stated cutoff."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q9VPC1 (DMAC2_DROME, Drosophila melanogaster) carries GO:0005739 (mitochondrion) with IDA:FlyBase evidence code (experimental direct assay, PubMed:34386730). The protein is named 'Distal membrane arm assembly component 2' with alternative name 'ATP synthase subunit s-like protein,' directly implicating the mitochondrial inner membrane ATP synthase (Complex V). The 2021 iScience paper documents its role in mitochondrial complex I biogenesis. Sequence matches the benchmark exactly (284 AA, SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2), [H1](#evidence-h1), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~26 residues (MLQRVSRRFPSLRRCGLRTASTVPTN) are enriched in Arg (6/26 ≈ 23%), Ser/Thr (6/26 ≈ 23%), and completely devoid of Asp/Glu — a pattern consistent with a mitochondrial targeting signal (MTS). Internal hydrophobic stretches (e.g., residues ~124–137: ILGAELAAAHFILYRGG) are consistent with mitochondrial inner-membrane transmembrane helices. The protein is small (284 AA ≈ 30 kDa), fitting a membrane subunit. Distractors can be eliminated by general knowledge: replisome components are DNA polymerases/helicases/primases (no such motifs here); nematocyst proteins are small Cys-rich cnidarian toxins (only 6 Cys in 284 AA, no toxin domain); 'host cell plasma membrane' is a virus-specific GO term (goslim_virus) and the sequence lacks a signal peptide or viral envelope features.


**Missing item-specific fact**

> The specific identification as 'ATP synthase subunit s-like protein / Distal membrane arm assembly component 2' is a database annotation fact. Without it, the MTS-like N-terminus is suggestive but not a textbook-perfect signal (contains Cys15, Phe9), and a model might hesitate between mitochondrion and another membrane compartment (e.g., ER).


**Reason**

> A concrete biological argument exists: N-terminal MTS-like composition (Arg/Ser/Thr-rich, acidic-free) plus internal hydrophobic stretches plus small size point toward a mitochondrial membrane protein, and the three distractors are eliminable by general domain knowledge (no polymerase motifs, not a Cys-rich cnidarian toxin, no viral signal peptide). The argument is moderate rather than airtight, but it provides meaningful grounds to distinguish the answer without requiring the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (nematocyst, host cell plasma membrane, replisome) are functionally and structurally distinct from what the sequence suggests. No other option is a plausible competitor once the MTS-like N-terminus and membrane-protein character are recognized.


### Important caveats

- The GO:0005739 annotation uses IDA (Inferred from Direct Assay) evidence, indicating experimental localization data, not mere computational inference.
- The N-terminal MTS-like region is suggestive but not a canonical textbook MTS (contains Cys and Phe); a model relying solely on strict MTS heuristics might not confidently assign mitochondrion.
- The protein was only integrated into Swiss-Prot on 2025-02-05; before that it was in TrEMBL. The 2021 experimental paper (PubMed:34386730) is the primary evidence source.
- The organism (Drosophila melanogaster) is not stated in the question, so eliminating nematocyst by taxonomic reasoning requires the model to infer non-cnidarian origin from sequence features alone.
- Reviewer-only evidence (UniProt accession, GO annotation, paper) was absent from the evaluated model input; the reasoning assessment considers only what a model could extract from the sequence and choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~26 residues (MLQRVSRRFPSLRRCGLRTASTVPTN) are enriched in Arg (6/26 ≈ 23%), Ser/Thr (6/26 ≈ 23%), and completely devoid of Asp/Glu — a pattern consistent with a mitochondrial targeting signal (MTS). Internal hydrophobic stretches (e.g., residues ~124–137: ILGAELAAAHFILYRGG) are consistent with mitochondrial inner-membrane transmembrane helices. The protein is small (284 AA ≈ 30 kDa), fitting a membrane subunit. Distractors can be eliminated by general knowledge: replisome components are DNA polymerases/helicases/primases (no such motifs here); nematocyst proteins are small Cys-rich cnidarian toxins (only 6 Cys in 284 AA, no toxin domain); 'host cell plasma membrane' is a virus-specific GO term (goslim_virus) and the sequence lacks a signal peptide or viral envelope features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific identification as 'ATP synthase subunit s-like protein / Distal membrane arm assembly component 2' is a database annotation fact. Without it, the MTS-like N-terminus is suggestive but not a textbook-perfect signal (contains Cys15, Phe9), and a model might hesitate between mitochondrion and another membrane compartment (e.g., ER).",
    "reason": "A concrete biological argument exists: N-terminal MTS-like composition (Arg/Ser/Thr-rich, acidic-free) plus internal hydrophobic stretches plus small size point toward a mitochondrial membrane protein, and the three distractors are eliminable by general domain knowledge (no polymerase motifs, not a Cys-rich cnidarian toxin, no viral signal peptide). The argument is moderate rather than airtight, but it provides meaningful grounds to distinguish the answer without requiring the specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H2",
      "H1",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9VPC1 (DMAC2_DROME, Drosophila melanogaster) carries GO:0005739 (mitochondrion) with IDA:FlyBase evidence code (experimental direct assay, PubMed:34386730). The protein is named 'Distal membrane arm assembly component 2' with alternative name 'ATP synthase subunit s-like protein,' directly implicating the mitochondrial inner membrane ATP synthase (Complex V). The 2021 iScience paper documents its role in mitochondrial complex I biogenesis. Sequence matches the benchmark exactly (284 AA, SHA-256 confirmed)."
  },
  "important_caveats": [
    "The GO:0005739 annotation uses IDA (Inferred from Direct Assay) evidence, indicating experimental localization data, not mere computational inference.",
    "The N-terminal MTS-like region is suggestive but not a canonical textbook MTS (contains Cys and Phe); a model relying solely on strict MTS heuristics might not confidently assign mitochondrion.",
    "The protein was only integrated into Swiss-Prot on 2025-02-05; before that it was in TrEMBL. The 2021 experimental paper (PubMed:34386730) is the primary evidence source.",
    "The organism (Drosophila melanogaster) is not stated in the question, so eliminating nematocyst by taxonomic reasoning requires the model to infer non-cnidarian origin from sequence features alone.",
    "Reviewer-only evidence (UniProt accession, GO annotation, paper) was absent from the evaluated model input; the reasoning assessment considers only what a model could extract from the sequence and choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (nematocyst, host cell plasma membrane, replisome) are functionally and structurally distinct from what the sequence suggests. No other option is a plausible competitor once the MTS-like N-terminus and membrane-protein character are recognized."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q9VPC1 (DMAC2_DROME, Drosophila melanogaster) carries GO:0005739 (mitochondrion) with IDA:FlyBase evidence code (experimental direct assay, PubMed:34386730). The protein is named 'Distal membrane arm assembly component 2' with alternative name 'ATP synthase subunit s-like protein,' directly implicating the mitochondrial inner membrane ATP synthase (Complex V). The 2021 iScience paper documents its role in mitochondrial complex I biogenesis. Sequence matches the benchmark exactly (284 AA, SHA-256 confirmed).",
    "evidence_ids": ["C5", "C6", "H3", "H2", "H1", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~26 residues (MLQRVSRRFPSLRRCGLRTASTVPTN) are enriched in Arg (6/26 ≈ 23%), Ser/Thr (6/26 ≈ 23%), and completely devoid of Asp/Glu — a pattern consistent with a mitochondrial targeting signal (MTS). Internal hydrophobic stretches (e.g., residues ~124–137: ILGAELAAAHFILYRGG) are consistent with mitochondrial inner-membrane transmembrane helices. The protein is small (284 AA ≈ 30 kDa), fitting a membrane subunit. Distractors can be eliminated by general knowledge: replisome components are DNA polymerases/helicases/primases (no such motifs here); nematocyst proteins are small Cys-rich cnidarian toxins (only 6 Cys in 284 AA, no toxin domain); 'host cell plasma membrane' is a virus-specific GO term (goslim_virus) and the sequence lacks a signal peptide or viral envelope features.",
    "missing_item_specific_fact": "The specific identification as 'ATP synthase subunit s-like protein / Distal membrane arm assembly component 2' is a database annotation fact. Without it, the MTS-like N-terminus is suggestive but not a textbook-perfect signal (contains Cys15, Phe9), and a model might hesitate between mitochondrion and another membrane compartment (e.g., ER).",
    "reason": "A concrete biological argument exists: N-terminal MTS-like composition (Arg/Ser/Thr-rich, acidic-free) plus internal hydrophobic stretches plus small size point toward a mitochondrial membrane protein, and the three distractors are eliminable by general domain knowledge (no polymerase motifs, not a Cys-rich cnidarian toxin, no viral signal peptide). The argument is moderate rather than airtight, but it provides meaningful grounds to distinguish the answer without requiring the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (nematocyst, host cell plasma membrane, replisome) are functionally and structurally distinct from what the sequence suggests. No other option is a plausible competitor once the MTS-like N-terminus and membrane-protein character are recognized."
  },
  "important_caveats": [
    "The GO:0005739 annotation uses IDA (Inferred from Direct Assay) evidence, indicating experimental localization data, not mere computational inference.",
    "The N-terminal MTS-like region is suggestive but not a canonical textbook MTS (contains Cys and Phe); a model relying solely on strict MTS heuristics might not confidently assign mitochondrion.",
    "The protein was only integrated into Swiss-Prot on 2025-02-05; before that it was in TrEMBL. The 2021 experimental paper (PubMed:34386730) is the primary evidence source.",
    "The organism (Drosophila melanogaster) is not stated in the question, so eliminating nematocyst by taxonomic reasoning requires the model to infer non-cnidarian origin from sequence features alone.",
    "Reviewer-only evidence (UniProt accession, GO annotation, paper) was absent from the evaluated model input; the reasoning assessment considers only what a model could extract from the sequence and choices."
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

**Accession:** `Q9VPC1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 171. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPC1.json)  
**Locator:** `/uniProtKBCrossReferences/32`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:28.296162+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"34386730","source":"PubMed"}],"id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `cff9a5addec44d1f5c0d47dfcf012c8e86da96b411751e2c86f4c19692dde8d1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPC1.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:28.296162+00:00.  

```json
{"citation":{"authors":["Murari A.","Rhooms S.K.","Garcia C.","Liu T.","Li H.","Mishra B.","Deshong C.","Owusu-Ansah E."],"citationCrossReferences":[{"database":"PubMed","id":"34386730"},{"database":"DOI","id":"10.1016/j.isci.2021.102869"}],"citationType":"journal article","firstPage":"102869","id":"34386730","journal":"IScience","lastPage":"102869","publicationDate":"2021","title":"Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in mitochondrial complex I biogenesis.","volume":"24"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","INTERACTION WITH COMPLEX 1"]}
```

Source SHA-256: `cff9a5addec44d1f5c0d47dfcf012c8e86da96b411751e2c86f4c19692dde8d1`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPC1?format=txt&versions=171)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 171 / 1.  
**Retrieved:** 2026-11-02T04:33:35.857277+00:00.  

```text
ID   DMAC2_DROME             Reviewed;         284 AA.
AC   Q9VPC1; Q8SYK3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 171.
DE   RecName: Full=Distal membrane arm assembly component 2 {ECO:0000312|FlyBase:FBgn0037018};
DE   AltName: Full=ATP synthase subunit s-like protein {ECO:0000250|UniProtKB:Q9NW81};
DE            Short=dATP5SL {ECO:0000303|PubMed:34386730};
GN   Name=Dmac2 {ECO:0000312|FlyBase:FBgn0037018};
GN   ORFNames=CG4042 {ECO:0000312|FlyBase:FBgn0037018};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `9b6c3e61b19c0a5bb0eeeb673ff97a1d0b61757779b439ac3cd1363b82313db9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPC1?format=txt&versions=171)  
**Locator:** `lines 83-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 171 / 1.  
**Retrieved:** 2026-11-02T04:33:35.857277+00:00.  

```text
RN   [5] {ECO:0000305}
RP   FUNCTION, AND INTERACTION WITH COMPLEX 1.
RX   PubMed=34386730; DOI=10.1016/j.isci.2021.102869;
RA   Murari A., Rhooms S.K., Garcia C., Liu T., Li H., Mishra B., Deshong C.,
RA   Owusu-Ansah E.;
RT   "Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in
RT   mitochondrial complex I biogenesis.";
RL   IScience 24:102869-102869(2021).
```

Source SHA-256: `9b6c3e61b19c0a5bb0eeeb673ff97a1d0b61757779b439ac3cd1363b82313db9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPC1?format=txt&versions=171)  
**Locator:** `lines 133-133`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 171 / 1.  
**Retrieved:** 2026-11-02T04:33:35.857277+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; IDA:FlyBase.
```

Source SHA-256: `9b6c3e61b19c0a5bb0eeeb673ff97a1d0b61757779b439ac3cd1363b82313db9`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58975-58998`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005739
name: mitochondrion
namespace: cellular_component
def: "A semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration." [GOC:giardia, ISBN:0198506732]
comment: Some anaerobic or microaerophilic organisms (e.g. Entamoeba histolytica, Giardia intestinalis and several Microsporidia species) do not have mitochondria, and contain mitochondrion-related organelles (MROs) instead, called mitosomes or hydrogenosomes, very likely derived from mitochondria. To annotate gene products located in these mitochondrial relics in species such as Entamoeba histolytica, Giardia intestinalis or others, please use GO:0032047 'mitosome' or GO:0042566 'hydrogenosome'. (See PMID:24316280 for a list of species currently known to contain mitochondrion-related organelles.)
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_yeast
synonym: "mitochondria" EXACT []
xref: NIF_Subcellular:sao1860313010
xref: Wikipedia:Mitochondrion
is_a: GO:0043231 ! intracellular membrane-bounded organelle
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 116. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
