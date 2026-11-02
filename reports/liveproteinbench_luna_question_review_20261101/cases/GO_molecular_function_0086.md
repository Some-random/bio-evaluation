# GO_molecular_function_0086

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — phosphoprotein phosphatase activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| contradicted | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MRTTLTGTASVLDTTLTRLIDDVIENGSSFLADDENLQHYKQHLSHLETASKIALLRECLCVRPPLPLLPEDLLQNVDSILTRVRQHKILTPIFSLSPSRLIKHGDLGATRIHLWRGDITTLTGVTAITNAANSQGLGCFQPTHRCIDNIIHAEAGPRLREECFQRMQARGKELEPGEVLVTEGHALFASSVMHTVGPQLKRGASPTETERRQLAKCYESILEALELLPSDEDGSKSIALCCISTGLFAFPADEAAEIAVSTVTSWLQKHPSTTITDVIFNTFTQSDTEFYSKLLGPSHTKSISPVENTPQGSLSLAREWLSSADAVLVTAGAGLSAAEGLDYHSRDLFKRNFPGCLKFGLTSLYSVFGFNDWPSEEHRWGYFFTHLNMVANWSNTPTYQILIPWLRNFGQDAFVRTSNADGLFLANGWPKEQLSTPQGSYGYLQCLNNCRVDAVVPSAPLVADAMPHIDKATQKLMDPSKIPLCRFCGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKKNLVILELGVGMNTPGVLRWPNEDLVMRSDGRVKLIRVGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE

[Multiple Choices]
A. glucose-6-phosphate isomerase activity
B. chromatin DNA binding
C. phosphoprotein phosphatase activity
D. protein heterodimerization activity
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

### Expected-answer support: contradicted

> The exact sequence match is annotated as a probable ADP-ribosyl hydrolase/transferase, with experimental evidence for hydrolysis of ADP-ribosyl-glutamate bonds. That reaction is not phosphoprotein dephosphorylation, so choice C is not supported as the answer. The evidence does not exhaustively rule out an additional activity.

Cited evidence: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence offers no clear general biological argument for phosphoprotein phosphatase activity over the other choices; identifying its particular enzyme function requires protein-specific knowledge. The documented activity is not represented among the options.

**Missing item-specific fact**

> The protein-specific ADP-ribosyl hydrolase/transferase activity, established by annotation and reported experimental evidence, is absent from the input.

**Reason**

> A precise assignment cannot be justified merely from broad sequence features. Recognizing this protein or consulting a function annotation would supply the needed item-specific information, and would show that none of the listed activities accurately describes the documented catalytic function.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> No listed option matches the documented ADP-ribosyl hydrolase/transferase activity. The evidence does not establish that any option is a correct alternative.

### Important caveats

- The experimental evidence supports ADP-ribosyl hydrolase activity in vitro; the bifunctional hydrolase/transferase designation is qualified as probable.
- The sequence matches the cited UniProt record, but the author's exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0086",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The exact sequence match is annotated as a probable ADP-ribosyl hydrolase/transferase, with experimental evidence for hydrolysis of ADP-ribosyl-glutamate bonds. That reaction is not phosphoprotein dephosphorylation, so choice C is not supported as the answer. The evidence does not exhaustively rule out an additional activity.",
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence offers no clear general biological argument for phosphoprotein phosphatase activity over the other choices; identifying its particular enzyme function requires protein-specific knowledge. The documented activity is not represented among the options.",
    "missing_item_specific_fact": "The protein-specific ADP-ribosyl hydrolase/transferase activity, established by annotation and reported experimental evidence, is absent from the input.",
    "reason": "A precise assignment cannot be justified merely from broad sequence features. Recognizing this protein or consulting a function annotation would supply the needed item-specific information, and would show that none of the listed activities accurately describes the documented catalytic function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No listed option matches the documented ADP-ribosyl hydrolase/transferase activity. The evidence does not establish that any option is a correct alternative."
  },
  "important_caveats": [
    "The experimental evidence supports ADP-ribosyl hydrolase activity in vitro; the bifunctional hydrolase/transferase designation is qualified as probable.",
    "The sequence matches the cited UniProt record, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_definition_difference_traced`.

> C5/C6 and H3/H4 describe hydrolysis of ADP-ribosyl-glutamate, with explicit inability to hydrolyze an ADP-ribosyl-aspartate bond. This differs from phosphoprotein dephosphorylation.

**Remaining uncertainty:** The reported reaction is relevant; the supplied negative result concerns a different ADP-ribosyl bond, not an exhaustive phosphatase assay.

Evidence checked: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A559KX76`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 22. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:25.184799+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39270823","source":"PubMed"}],"value":"Foc1Mfs1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"WZU87063.1","source":"EMBL"}],"value":"Macrodomain-fused SirTM 1"}}],"includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"}],"value":"3.2.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Protein-ADP-ribose hydrolase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P0DN71","source":"UniProtKB"}],"value":"2.4.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Probable protein ADP-ribosyltransferase"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase"}}}
```

Source SHA-256: `52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:25.184799+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Is probably a bifunctional enzyme with ADP-ribosyltransferase and ADP-ribosylhydrolase activities (Probable). In vitro, can act as an ADP-ribosylhydrolase that hydrolyzes ADP-ribosyl-glutamate bonds (PubMed:39270823). It can remove the ADP-ribosyl modification from the human mono-ADP-ribosylated PARP1 E988Q mutant, which is primarily modified on glutamate site with only minor aspartate contribution (PubMed:39270823). It cannot hydrolyze the ADP-ribosyl-arpartate bond in ribosylated S.pyogenes GcvH-L (PubMed:39270823)"}]}
```

Source SHA-256: `52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:25.184799+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"}],"name":"5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58248"},{"database":"Rhea","id":"RHEA-COMP:10208"},{"database":"Rhea","id":"RHEA-COMP:15089"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29973"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:142540"}]}}
```

Source SHA-256: `52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 40-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
CC   -!- FUNCTION: Is probably a bifunctional enzyme with ADP-ribosyltransferase
CC       and ADP-ribosylhydrolase activities (Probable). In vitro, can act as an
CC       ADP-ribosylhydrolase that hydrolyzes ADP-ribosyl-glutamate bonds
CC       (PubMed:39270823). It can remove the ADP-ribosyl modification from the
CC       human mono-ADP-ribosylated PARP1 E988Q mutant, which is primarily
CC       modified on glutamate site with only minor aspartate contribution
CC       (PubMed:39270823). It cannot hydrolyze the ADP-ribosyl-arpartate bond
CC       in ribosylated S.pyogenes GcvH-L (PubMed:39270823).
CC       {ECO:0000269|PubMed:39270823, ECO:0000305}.
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 49-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-
CC         [protein] + ADP-D-ribose + H(+); Xref=Rhea:RHEA:58248, Rhea:RHEA-
CC         COMP:10208, Rhea:RHEA-COMP:15089, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29973, ChEBI:CHEBI:57967,
CC         ChEBI:CHEBI:142540; Evidence={ECO:0000269|PubMed:39270823};
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 86). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
