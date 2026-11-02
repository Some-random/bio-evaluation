# GO_molecular_function_0026

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — alpha-1,6-mannosyltransferase activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MWSLDPSQKEVLRFAVSCRILTLMLQALFNIIIPDHHADAFSPPRLASSCSVDQLVEGLLGGLSRWDAEHFLFIAEHGYLYEHNFAFFPGFPLALLMGTELLRPLQGLLSQRSCLLVSVALLNFLFSVLAAVTLHDLGCLVLGCPRQAFYAAMLFCLSPANVFLAAGYSEALFAFLTFSAMGQLERGRSWASGLLFALATGVRSNGLVSVGFLLHAQCRGFFSSLVVLNPLKPLFKLMASLCLSVLTVSLPFALFQYYAYTQFCLPGSAHSVPEPLVQLAVDKGYRITGGNEPPWCSWGLPLVYSYIQDVYWNVGFLRYYELRQVPNFLLATPVAVLVVWAAWTYVTTHPWLCLTLGLRRSKDSKKTLEKPHPGFLSPKVFVYLVHAAGLLLFGSLCMHVQVLTRLLCSSTPVVYWFPAHLLQNQEPLLRSVDTVPEKLLEKNSPPGQKAPRNCIMKLLYNWRACSPVTRCILGYFLTYWLLGLLLHCNFLPWT

[Multiple Choices]
A. 4 iron, 4 sulfur cluster binding
B. Hsp90 protein binding
C. NADPH dehydrogenase (quinone) activity
D. alpha-1,6-mannosyltransferase activity
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

## Luna’s full visible review

### Expected-answer support: supported

> The reviewer-only UniProt record matches the supplied 494-aa sequence and identifies the protein as GPI alpha-1,6-mannosyltransferase 2. Its functional and catalytic-activity annotations cite experimental evidence (ECO:0000269, PMID:23694781), supporting choice D. The evidence supports the enzyme activity, not merely a computational GO assignment.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic and consistent with a polytopic membrane protein, making a membrane-associated glycosylation role plausible; it does not show an obvious iron-sulfur-cluster-binding motif or a recognizable NADPH-binding domain. These clues can make some distractors less plausible but do not identify the alpha-1,6 linkage or its specific substrate.

**Missing item-specific fact**

> The protein-specific identity and experimentally characterized catalytic activity of this sequence as GPI mannosyltransferase II are needed to distinguish D confidently from other membrane-protein functions.

**Reason**

> General sequence features suggest membrane localization but do not establish the precise molecular function or substrate specificity. Selecting D therefore depends on protein-specific annotation, homology recognition, or experimental knowledge not supplied in the question.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The reviewer-only evidence supports D for the matched sequence. The sequence alone does not make the precise activity clear, but no alternative choice is comparably supported by the supplied information.

### Important caveats

- The UniProt annotation and its cited experimental evidence are reviewer-only and were absent from the evaluated model input.
- The source record matches the sequence, but the author's exact annotation snapshot is unknown; the matched historical record also supports the function.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only UniProt record matches the supplied 494-aa sequence and identifies the protein as GPI alpha-1,6-mannosyltransferase 2. Its functional and catalytic-activity annotations cite experimental evidence (ECO:0000269, PMID:23694781), supporting choice D. The evidence supports the enzyme activity, not merely a computational GO assignment.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a polytopic membrane protein, making a membrane-associated glycosylation role plausible; it does not show an obvious iron-sulfur-cluster-binding motif or a recognizable NADPH-binding domain. These clues can make some distractors less plausible but do not identify the alpha-1,6 linkage or its specific substrate.",
    "missing_item_specific_fact": "The protein-specific identity and experimentally characterized catalytic activity of this sequence as GPI mannosyltransferase II are needed to distinguish D confidently from other membrane-protein functions.",
    "reason": "General sequence features suggest membrane localization but do not establish the precise molecular function or substrate specificity. Selecting D therefore depends on protein-specific annotation, homology recognition, or experimental knowledge not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D for the matched sequence. The sequence alone does not make the precise activity clear, but no alternative choice is comparably supported by the supplied information."
  },
  "important_caveats": [
    "The UniProt annotation and its cited experimental evidence are reviewer-only and were absent from the evaluated model input.",
    "The source record matches the sequence, but the author's exact annotation snapshot is unknown; the matched historical record also supports the function."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A8C2M425`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 19. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
"A0A8C2M425"
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"GPI mannosyltransferase II"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9NUD9","source":"UniProtKB"}],"value":"GPI-MT-II"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9NUD9","source":"UniProtKB"}],"value":"Phosphatidylinositol-glycan biosynthesis class V protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9NUD9","source":"UniProtKB"}],"value":"PIG-V"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23694781","source":"PubMed"}],"value":"2.4.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9NUD9","source":"UniProtKB"}],"value":"GPI alpha-1,6-mannosyltransferase 2"}}}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23694781","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"23694781","source":"PubMed"}],"value":"Alpha-1,6-mannosyltransferase that catalyzes the transfer of the second mannose, via an alpha-1,6 bond, from a dolichol-phosphate-mannose (Dol-P-Man) to a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H2) intermediate to generate a 2-acyl-6-[alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H3) and participates in the seventh step of the glycosylphosphatidylinositol-anchor biosynthesis (PubMed:23694781). May also transfer the second mannose on a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H5), but less effectively (Probable)"}]}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"23694781","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:60489"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"23694781","source":"PubMed"}],"name":"a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a 2-acyl-6-[alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:60488"},{"database":"Rhea","id":"RHEA-COMP:19498"},{"database":"Rhea","id":"RHEA-COMP:19501"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57683"},{"database":"ChEBI","id":"CHEBI:58211"},{"database":"ChEBI","id":"CHEBI:143818"},{"database":"ChEBI","id":"CHEBI:144028"}]}}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 36-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
CC   -!- FUNCTION: Alpha-1,6-mannosyltransferase that catalyzes the transfer of
CC       the second mannose, via an alpha-1,6 bond, from a dolichol-phosphate-
CC       mannose (Dol-P-Man) to a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-
CC       glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol
CC       (also termed H2) intermediate to generate a 2-acyl-6-[alpha-D-mannosyl-
CC       (1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-
CC       sn-glycero-3-phospho)-1D-myo-inositol (also termed H3) and participates
CC       in the seventh step of the glycosylphosphatidylinositol-anchor
CC       biosynthesis (PubMed:23694781). May also transfer the second mannose on
CC       a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-
CC       glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol
CC       (also termed H5), but less effectively (Probable).
CC       {ECO:0000269|PubMed:23694781, ECO:0000305|PubMed:23694781}.
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 49-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-
CC         (1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-
CC         trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a 2-acyl-6-
CC         [alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-
CC         glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol
CC         + a di-trans,poly-cis-dolichyl phosphate + H(+);
CC         Xref=Rhea:RHEA:60488, Rhea:RHEA-COMP:19498, Rhea:RHEA-COMP:19501,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57683, ChEBI:CHEBI:58211,
CC         ChEBI:CHEBI:143818, ChEBI:CHEBI:144028;
CC         Evidence={ECO:0000269|PubMed:23694781};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:60489;
CC         Evidence={ECO:0000269|PubMed:23694781};
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 26). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
