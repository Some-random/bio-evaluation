# catalytic_activity_0149

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — 5-O-(ADP-D-ribosyl)-L-glutamyl-&#91;protein&#93; + H2O = L-glutamyl-&#91;protein&#93; + ADP-D-ribose + H(+)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MRTTLTGTASVLDTTLTRLIDDVIENGSSFLADDENLQHYKQHLSHLETASKIALLRECLCVRPPLPLLPEDLLQNVDSILTRVRQHKILTPIFSLSPSRLIKHGDLGATRIHLWRGDITTLTGVTAITNAANSQGLGCFQPTHRCIDNIIHAEAGPRLREECFQRMQARGKELEPGEVLVTEGHALFASSVMHTVGPQLKRGASPTETERRQLAKCYESILEALELLPSDEDGSKSIALCCISTGLFAFPADEAAEIAVSTVTSWLQKHPSTTITDVIFNTFTQSDTEFYSKLLGPSHTKSISPVENTPQGSLSLAREWLSSADAVLVTAGAGLSAAEGLDYHSRDLFKRNFPGCLKFGLTSLYSVFGFNDWPSEEHRWGYFFTHLNMVANWSNTPTYQILIPWLRNFGQDAFVRTSNADGLFLANGWPKEQLSTPQGSYGYLQCLNNCRVDAVVPSAPLVADAMPHIDKATQKLMDPSKIPLCRFCGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKKNLVILELGVGMNTPGVLRWPNEDLVMRSDGRVKLIRVGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE

[Multiple Choices]
A. (2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O
B. deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose
C. dopamine + S-adenosyl-L-methionine = N-methyl-dopamine + S-adenosyl-L-homocysteine + H(+)
D. 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)
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

## Luna’s full visible review

### Expected-answer support: supported

> The supplied sequence exactly matches the reviewed protein sequence, and its catalytic-activity annotation gives the reaction in choice D with ECO:0000269 evidence linked to a 2024 publication. The source also cites structural and mutagenesis work. This supports D for this protein, while distinguishing the evidence as an annotation tied to published experimental work rather than something established from the sequence alone.

Cited evidence: [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a protein with ADP-ribose-related domains, but the input does not establish the specific substrate or hydrolysis of ADP-ribose from glutamylated protein. The precise reaction cannot be reliably selected from sequence inspection alone.

**Missing item-specific fact**

> The protein-specific catalytic activity: hydrolysis of 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein].

**Reason**

> Choosing D requires knowing this protein's experimentally characterized or database-annotated activity, which is absent from the question input; recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied evidence.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the listed reactions, D matches the supported catalytic activity; the other choices describe distinct reactions.

### Important caveats

- The reviewer-only source records an exact sequence match and an experimental-evidence code for the catalytic activity, but the primary paper was not independently reviewed here.
- The author’s exact source snapshot is unknown; the historical record checked also matches the sequence.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed protein sequence, and its catalytic-activity annotation gives the reaction in choice D with ECO:0000269 evidence linked to a 2024 publication. The source also cites structural and mutagenesis work. This supports D for this protein, while distinguishing the evidence as an annotation tied to published experimental work rather than something established from the sequence alone.",
    "evidence_ids": [
      "C5",
      "H3",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a protein with ADP-ribose-related domains, but the input does not establish the specific substrate or hydrolysis of ADP-ribose from glutamylated protein. The precise reaction cannot be reliably selected from sequence inspection alone.",
    "missing_item_specific_fact": "The protein-specific catalytic activity: hydrolysis of 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein].",
    "reason": "Choosing D requires knowing this protein's experimentally characterized or database-annotated activity, which is absent from the question input; recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, D matches the supported catalytic activity; the other choices describe distinct reactions."
  },
  "important_caveats": [
    "The reviewer-only source records an exact sequence match and an experimental-evidence code for the catalytic activity, but the primary paper was not independently reviewed here.",
    "The author’s exact source snapshot is unknown; the historical record checked also matches the sequence."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A559KX76`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 22. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

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
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
RN   [2] {ECO:0007744|PDB:8RSN}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS)
RP   IN COMPLEX WITH ZN(2+), FUNCTION AS AN HYDROLASE, CATALYTIC ACTIVITY,
RP   COFACTOR, SUBUNIT, AND MUTAGENESIS OF CYS-61 AND HIS-144.
RC   STRAIN=race 1 / IMI 141109;
RX   PubMed=39270823; DOI=10.1016/j.jbc.2024.107770;
RA   Ariza A., Liu Q., Cowieson N.P., Ahel I., Filippov D.V., Rack J.G.M.;
RT   "Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-
RT   dependent macrodomains.";
RL   J. Biol. Chem. 300:107770-107770(2024).
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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 149). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
