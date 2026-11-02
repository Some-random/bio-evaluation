# GO_molecular_function_0186

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — DNA-binding transcription factor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDLAKTAQRRALRSSGSARPDEDVPAPNRRGNRLPRDERRGQLLVVASDVFVDRGYHAAGMDEIADRAGVSKPVLYQHFSSKLELYLAVLHRHVENLVSGVHQALSTTTDNRQRLHVAVQAFFDFIEHDSQGYRLIFENDFVTEPEVAAQVRVATESCIDAVFALISADSGLDPHRARMIAVGLVGMSVDCARYWLDADKPISKSDAVEGTVQFAWGGLSHVPLTRS

[Multiple Choices]
A. DNA-binding transcription factor activity
B. zinc ion binding
C. nicotinamide-nucleotide adenylyltransferase activity
D. structural constituent of nuclear pore
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

> The exact sequence matches the UniProt entry for M. tuberculosis FasR. Its cited functional annotation identifies it as a transcriptional activator that binds promoter operators, supporting DNA-binding transcription factor activity. The GO annotation itself is IBA, while the functional annotation cites experimental evidence.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The bacterial sequence is inconsistent with a nuclear-pore constituent, and it lacks an obvious zinc-finger motif or clear NAD adenylyltransferase catalytic signature. Those observations make A plausible among the choices, but do not establish sequence-specific DNA binding or transcription-regulator activity.


**Missing item-specific fact**

> The identification of this particular sequence as FasR, an experimentally characterized transcriptional activator that binds operator DNA.


**Reason**

> The supplied sequence alone does not unambiguously establish the precise molecular function. Selecting A confidently requires protein-specific identity or functional annotation rather than merely recognizing that the other options seem less plausible.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports A; no alternative listed choice is comparably supported.


### Important caveats

- The sequence match is exact, but the accession and organism identity were not supplied to the evaluated model.
- The GO term annotation is computationally inferred (IBA); separate cited functional annotations provide experimental support.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The bacterial sequence is inconsistent with a nuclear-pore constituent, and it lacks an obvious zinc-finger motif or clear NAD adenylyltransferase catalytic signature. Those observations make A plausible among the choices, but do not establish sequence-specific DNA binding or transcription-regulator activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this particular sequence as FasR, an experimentally characterized transcriptional activator that binds operator DNA.",
    "reason": "The supplied sequence alone does not unambiguously establish the precise molecular function. Selecting A confidently requires protein-specific identity or functional annotation rather than merely recognizing that the other options seem less plausible."
  },
  "case_id": "GO_molecular_function_0186",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for M. tuberculosis FasR. Its cited functional annotation identifies it as a transcriptional activator that binds promoter operators, supporting DNA-binding transcription factor activity. The GO annotation itself is IBA, while the functional annotation cites experimental evidence."
  },
  "important_caveats": [
    "The sequence match is exact, but the accession and organism identity were not supplied to the evaluated model.",
    "The GO term annotation is computationally inferred (IBA); separate cited functional annotations provide experimental support."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports A; no alternative listed choice is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0186",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for M. tuberculosis FasR. Its cited functional annotation identifies it as a transcriptional activator that binds promoter operators, supporting DNA-binding transcription factor activity. The GO annotation itself is IBA, while the functional annotation cites experimental evidence.",
    "evidence_ids": ["C1", "C3", "C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The bacterial sequence is inconsistent with a nuclear-pore constituent, and it lacks an obvious zinc-finger motif or clear NAD adenylyltransferase catalytic signature. Those observations make A plausible among the choices, but do not establish sequence-specific DNA binding or transcription-regulator activity.",
    "missing_item_specific_fact": "The identification of this particular sequence as FasR, an experimentally characterized transcriptional activator that binds operator DNA.",
    "reason": "The supplied sequence alone does not unambiguously establish the precise molecular function. Selecting A confidently requires protein-specific identity or functional annotation rather than merely recognizing that the other options seem less plausible."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports A; no alternative listed choice is comparably supported."
  },
  "important_caveats": [
    "The sequence match is exact, but the accession and organism identity were not supplied to the evaluated model.",
    "The GO term annotation is computationally inferred (IBA); separate cited functional annotations provide experimental support."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry O05858 (FASR_MYCTU) is annotated as 'HTH-type transcriptional activator FasR' (C4). The FUNCTION comment (C5, H5) states it is a 'Transcriptional activator' that 'Specifically binds to three conserved operator sequences present in the fas-acpS promoter region.' GO:0003700 (DNA-binding transcription factor activity) is directly annotated (C6, H6). Experimental evidence includes DNA-binding assays (C8, H2: PubMed:23721164) and X-ray crystallography at 1.63 Å in complex with DNA (C10, H4: PubMed:32710080, PDB 6O6N/6O6O/6O6P). The sequence matches the benchmark exactly (228 aa, SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [H5](#evidence-h5), [H6](#evidence-h6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Elimination of D (nuclear pore) is straightforward: this is a bacterial protein (Mycobacterium tuberculosis), so nuclear pore complex membership is biologically impossible. Elimination of B (zinc ion binding) is supported by absence of canonical Zn-binding motifs (Cys₂His₂ or similar) in the sequence. Elimination of C (NMNAT activity) is supported by absence of the conserved NMNAT catalytic motifs. However, positively identifying option A requires recognizing the HTH (helix-turn-helix) DNA-binding domain architecture from primary sequence, which is not trivially unambiguous from a 228-aa string without secondary-structure prediction or domain database lookup.


**Missing item-specific fact**

> Recognition of the specific HTH domain fold and its placement in the N-terminal region of this protein, or identification of the C-terminal thioesterase-like regulatory domain, to positively assign 'DNA-binding transcription factor activity' rather than a generic small-protein function. The HTH motif is not unambiguously identifiable from primary sequence alone without structural context or prior knowledge of the protein family.


**Reason**

> While the three distractors can be eliminated by general biological reasoning (bacterial origin excludes D; absence of metal-binding and nucleotidyltransferase motifs weakens B and C), the positive identification of A as 'DNA-binding transcription factor activity' depends on recognizing the HTH domain architecture from primary sequence. This is a specific structural/biochemical annotation that is difficult to extract unambiguously from 228 residues without domain-prediction tools or memorization of this protein family. The question is not purely lookup (elimination reasoning helps), but the final positive assignment leans on item-specific domain knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors are clearly non-overlapping: D is impossible for a bacterium, B and C lack supporting sequence motifs, and A is the only option consistent with a small bacterial HTH-type regulator. No two options are simultaneously defensible.


### Important caveats

- The GO:0003700 annotation uses evidence code IBA:GO_Central (inferred by biological aspect), but the underlying experimental evidence (DNA-binding assays, X-ray crystallography with DNA) independently supports the function.
- The sequence is a bacterial protein; the nuclear pore option (D) is a strong, easily eliminable distractor that may reduce the effective difficulty of the question.
- The C-terminal region of FasR contains a thioesterase-like domain that binds fatty acyl-CoA effectors; a model might incorrectly associate this with enzymatic activity, but it functions as a ligand-sensing domain, not a catalytic domain.
- The reviewer-only evidence confirms the protein identity via sequence match; the evaluated model had no access to the accession or UniProt annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Elimination of D (nuclear pore) is straightforward: this is a bacterial protein (Mycobacterium tuberculosis), so nuclear pore complex membership is biologically impossible. Elimination of B (zinc ion binding) is supported by absence of canonical Zn-binding motifs (Cys₂His₂ or similar) in the sequence. Elimination of C (NMNAT activity) is supported by absence of the conserved NMNAT catalytic motifs. However, positively identifying option A requires recognizing the HTH (helix-turn-helix) DNA-binding domain architecture from primary sequence, which is not trivially unambiguous from a 228-aa string without secondary-structure prediction or domain database lookup.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition of the specific HTH domain fold and its placement in the N-terminal region of this protein, or identification of the C-terminal thioesterase-like regulatory domain, to positively assign 'DNA-binding transcription factor activity' rather than a generic small-protein function. The HTH motif is not unambiguously identifiable from primary sequence alone without structural context or prior knowledge of the protein family.",
    "reason": "While the three distractors can be eliminated by general biological reasoning (bacterial origin excludes D; absence of metal-binding and nucleotidyltransferase motifs weakens B and C), the positive identification of A as 'DNA-binding transcription factor activity' depends on recognizing the HTH domain architecture from primary sequence. This is a specific structural/biochemical annotation that is difficult to extract unambiguously from 228 residues without domain-prediction tools or memorization of this protein family. The question is not purely lookup (elimination reasoning helps), but the final positive assignment leans on item-specific domain knowledge."
  },
  "case_id": "GO_molecular_function_0186",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "C10",
      "H5",
      "H6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry O05858 (FASR_MYCTU) is annotated as 'HTH-type transcriptional activator FasR' (C4). The FUNCTION comment (C5, H5) states it is a 'Transcriptional activator' that 'Specifically binds to three conserved operator sequences present in the fas-acpS promoter region.' GO:0003700 (DNA-binding transcription factor activity) is directly annotated (C6, H6). Experimental evidence includes DNA-binding assays (C8, H2: PubMed:23721164) and X-ray crystallography at 1.63 Å in complex with DNA (C10, H4: PubMed:32710080, PDB 6O6N/6O6O/6O6P). The sequence matches the benchmark exactly (228 aa, SHA-256 confirmed)."
  },
  "important_caveats": [
    "The GO:0003700 annotation uses evidence code IBA:GO_Central (inferred by biological aspect), but the underlying experimental evidence (DNA-binding assays, X-ray crystallography with DNA) independently supports the function.",
    "The sequence is a bacterial protein; the nuclear pore option (D) is a strong, easily eliminable distractor that may reduce the effective difficulty of the question.",
    "The C-terminal region of FasR contains a thioesterase-like domain that binds fatty acyl-CoA effectors; a model might incorrectly associate this with enzymatic activity, but it functions as a ligand-sensing domain, not a catalytic domain.",
    "The reviewer-only evidence confirms the protein identity via sequence match; the evaluated model had no access to the accession or UniProt annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors are clearly non-overlapping: D is impossible for a bacterium, B and C lack supporting sequence motifs, and A is the only option consistent with a small bacterial HTH-type regulator. No two options are simultaneously defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0186",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry O05858 (FASR_MYCTU) is annotated as 'HTH-type transcriptional activator FasR' (C4). The FUNCTION comment (C5, H5) states it is a 'Transcriptional activator' that 'Specifically binds to three conserved operator sequences present in the fas-acpS promoter region.' GO:0003700 (DNA-binding transcription factor activity) is directly annotated (C6, H6). Experimental evidence includes DNA-binding assays (C8, H2: PubMed:23721164) and X-ray crystallography at 1.63 Å in complex with DNA (C10, H4: PubMed:32710080, PDB 6O6N/6O6O/6O6P). The sequence matches the benchmark exactly (228 aa, SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C8", "C10", "H5", "H6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Elimination of D (nuclear pore) is straightforward: this is a bacterial protein (Mycobacterium tuberculosis), so nuclear pore complex membership is biologically impossible. Elimination of B (zinc ion binding) is supported by absence of canonical Zn-binding motifs (Cys₂His₂ or similar) in the sequence. Elimination of C (NMNAT activity) is supported by absence of the conserved NMNAT catalytic motifs. However, positively identifying option A requires recognizing the HTH (helix-turn-helix) DNA-binding domain architecture from primary sequence, which is not trivially unambiguous from a 228-aa string without secondary-structure prediction or domain database lookup.",
    "missing_item_specific_fact": "Recognition of the specific HTH domain fold and its placement in the N-terminal region of this protein, or identification of the C-terminal thioesterase-like regulatory domain, to positively assign 'DNA-binding transcription factor activity' rather than a generic small-protein function. The HTH motif is not unambiguously identifiable from primary sequence alone without structural context or prior knowledge of the protein family.",
    "reason": "While the three distractors can be eliminated by general biological reasoning (bacterial origin excludes D; absence of metal-binding and nucleotidyltransferase motifs weakens B and C), the positive identification of A as 'DNA-binding transcription factor activity' depends on recognizing the HTH domain architecture from primary sequence. This is a specific structural/biochemical annotation that is difficult to extract unambiguously from 228 residues without domain-prediction tools or memorization of this protein family. The question is not purely lookup (elimination reasoning helps), but the final positive assignment leans on item-specific domain knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors are clearly non-overlapping: D is impossible for a bacterium, B and C lack supporting sequence motifs, and A is the only option consistent with a small bacterial HTH-type regulator. No two options are simultaneously defensible."
  },
  "important_caveats": [
    "The GO:0003700 annotation uses evidence code IBA:GO_Central (inferred by biological aspect), but the underlying experimental evidence (DNA-binding assays, X-ray crystallography with DNA) independently supports the function.",
    "The sequence is a bacterial protein; the nuclear pore option (D) is a strong, easily eliminable distractor that may reduce the effective difficulty of the question.",
    "The C-terminal region of FasR contains a thioesterase-like domain that binds fatty acyl-CoA effectors; a model might incorrectly associate this with enzymatic activity, but it functions as a ligand-sensing domain, not a catalytic domain.",
    "The reviewer-only evidence confirms the protein identity via sequence match; the evaluated model had no access to the accession or UniProt annotations."
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

**Accession:** `O05858` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 170. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.365865+00:00.  

```json
"O05858"
```

Source SHA-256: `fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.365865+00:00.  

```json
{"lineage":["Bacteria","Bacillati","Actinomycetota","Actinomycetes","Mycobacteriales","Mycobacteriaceae","Mycobacterium","Mycobacterium tuberculosis complex"],"scientificName":"Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv)","taxonId":83332}
```

Source SHA-256: `fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.365865+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23721164","source":"PubMed"}],"value":"Fatty acid synthesis regulator"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"HTH-type transcriptional activator FasR"}}}
```

Source SHA-256: `fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.365865+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23721164","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32710080","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"33193236","source":"PubMed"}],"value":"Transcriptional activator that plays a central role in sensing mycobacterial long-chain fatty acids and regulating lipid biosynthesis (PubMed:23721164, PubMed:32710080, PubMed:33193236). Activates the expression of the genes encoding the fatty acid synthase (fas) and the 4-phosphopantetheinyl transferase (acpS), whose products are involved in the fatty acid and mycolic acid biosynthesis (PubMed:23721164, PubMed:33193236). Specifically binds to three conserved operator sequences present in the fas-acpS promoter region (PubMed:23721164). Not essential for M.tuberculosis viability, although it is required for the optimal growth in vitro and for virulence in macrophages and in a mouse model of infection (PubMed:33193236)"}]}
```

Source SHA-256: `fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)  
**Locator:** `/uniProtKBCrossReferences/27`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.365865+00:00.  

```json
{"database":"GO","id":"GO:0003700","properties":[{"key":"GoTerm","value":"F:DNA-binding transcription factor activity"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.365865+00:00.  

```json
{"citation":{"authors":["Mondino S.","Gago G.","Gramajo H."],"citationCrossReferences":[{"database":"PubMed","id":"23721164"},{"database":"DOI","id":"10.1111/mmi.12282"}],"citationType":"journal article","firstPage":"372","id":"23721164","journal":"Mol. Microbiol.","lastPage":"387","publicationDate":"2013","title":"Transcriptional regulation of fatty acid biosynthesis in mycobacteria.","volume":"89"},"referenceComments":[{"type":"STRAIN","value":"H37Rv"}],"referenceNumber":3,"referencePositions":["FUNCTION","DNA-BINDING","ACTIVITY REGULATION","SUBUNIT"]}
```

Source SHA-256: `fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.365865+00:00.  

```json
{"citation":{"authors":["Lara J.","Diacovich L.","Trajtenberg F.","Larrieux N.","Malchiodi E.L.","Fernandez M.M.","Gago G.","Gramajo H.","Buschiazzo A."],"citationCrossReferences":[{"database":"PubMed","id":"32710080"},{"database":"DOI","id":"10.1038/s41467-020-17504-x"}],"citationType":"journal article","firstPage":"3703","id":"32710080","journal":"Nat. Commun.","lastPage":"3703","publicationDate":"2020","title":"Mycobacterium tuberculosis FasR senses long fatty acyl-CoA through a tunnel and a hydrophobic transmission spine.","volume":"11"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6O6N","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6O6O","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6O6P","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"H37Rv"}],"referenceNumber":5,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.63 ANGSTROMS) IN COMPLEX WITH ACYL EFFECTOR LIGANDS AND DNA","FUNCTION","ACTIVITY REGULATION","SUBUNIT","DOMAIN","MUTAGENESIS OF LEU-98; LEU-106 AND PHE-123"]}
```

Source SHA-256: `fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)  
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 170 / 1.  
**Retrieved:** 2026-11-02T04:29:12.681576+00:00.  

```text
RN   [3]
RP   FUNCTION, DNA-BINDING, ACTIVITY REGULATION, AND SUBUNIT.
RC   STRAIN=H37Rv;
RX   PubMed=23721164; DOI=10.1111/mmi.12282;
RA   Mondino S., Gago G., Gramajo H.;
RT   "Transcriptional regulation of fatty acid biosynthesis in mycobacteria.";
RL   Mol. Microbiol. 89:372-387(2013).
```

Source SHA-256: `91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)  
**Locator:** `lines 56-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 170 / 1.  
**Retrieved:** 2026-11-02T04:29:12.681576+00:00.  

```text
RN   [5] {ECO:0007744|PDB:6O6N, ECO:0007744|PDB:6O6O, ECO:0007744|PDB:6O6P}
RP   X-RAY CRYSTALLOGRAPHY (1.63 ANGSTROMS) IN COMPLEX WITH ACYL EFFECTOR
RP   LIGANDS AND DNA, FUNCTION, ACTIVITY REGULATION, SUBUNIT, DOMAIN, AND
RP   MUTAGENESIS OF LEU-98; LEU-106 AND PHE-123.
RC   STRAIN=H37Rv;
RX   PubMed=32710080; DOI=10.1038/s41467-020-17504-x;
RA   Lara J., Diacovich L., Trajtenberg F., Larrieux N., Malchiodi E.L.,
RA   Fernandez M.M., Gago G., Gramajo H., Buschiazzo A.;
RT   "Mycobacterium tuberculosis FasR senses long fatty acyl-CoA through a
RT   tunnel and a hydrophobic transmission spine.";
RL   Nat. Commun. 11:3703-3703(2020).
```

Source SHA-256: `91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)  
**Locator:** `lines 67-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 170 / 1.  
**Retrieved:** 2026-11-02T04:29:12.681576+00:00.  

```text
CC   -!- FUNCTION: Transcriptional activator that plays a central role in
CC       sensing mycobacterial long-chain fatty acids and regulating lipid
CC       biosynthesis (PubMed:23721164, PubMed:32710080, PubMed:33193236).
CC       Activates the expression of the genes encoding the fatty acid synthase
CC       (fas) and the 4-phosphopantetheinyl transferase (acpS), whose products
CC       are involved in the fatty acid and mycolic acid biosynthesis
CC       (PubMed:23721164, PubMed:33193236). Specifically binds to three
CC       conserved operator sequences present in the fas-acpS promoter region
CC       (PubMed:23721164). Not essential for M.tuberculosis viability, although
CC       it is required for the optimal growth in vitro and for virulence in
CC       macrophages and in a mouse model of infection (PubMed:33193236).
CC       {ECO:0000269|PubMed:23721164, ECO:0000269|PubMed:32710080,
CC       ECO:0000269|PubMed:33193236}.
```

Source SHA-256: `91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)  
**Locator:** `lines 137-137`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 170 / 1.  
**Retrieved:** 2026-11-02T04:29:12.681576+00:00.  

```text
DR   GO; GO:0003700; F:DNA-binding transcription factor activity; IBA:GO_Central.
```

Source SHA-256: `91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 186. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
