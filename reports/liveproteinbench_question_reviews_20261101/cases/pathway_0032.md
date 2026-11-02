# pathway_0032

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Lipid metabolism

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSKPAAAAPSDPSKPSKPLKEVPGSYGLPVLGAVKDRLDFYWFQGDTEFFRIRMEQHKSTVFRVNYSPGPPGYPDSRGIILLDQKSFSVLLDNSKVDKSDTLLGPYIPNLAFTGGYRVLPYLDTSEAKHTAYKDLIFELLHVNSSRIIPEYNKVFAETAGSWEERIAKSGKAEVFASSDSMITKFLLRTIVHKDPAEPGPASLGPKFRDTYQLWTGVNFAGIAHTPLPHFLEELLFHTFRLPPFLVKKQYKALANFYRTHATEVLDLAEKKYGLDREETVHQLILILGINARLGLHKMIPALIYYLGLLGEDFQAKIAAEVRSAVHKNRAQGEEGVNITTQALLEMPLLRSTVLETLRLTPSIFYIYGRAREDMVIESHDAAFQIKKGELLGGHQYFVMRDPEVFEEPHKFVADRFLGERGKAVLPYLVWSNGRETESPSSSNKQCPAKDVAELITMQFVAEMFLRYDSFEITKDSFINTTELNVHLKSLKKRSV

[Multiple Choices]
A. 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2. .
B. Steroid biosynthesis
C. Lipid metabolism
D. Lipid metabolism. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence match is annotated as divinyl ether synthase CYP74M3, with the pathway listed as lipid metabolism (oxylipin biosynthesis). The pathway annotation carries experimental-evidence code ECO:0000269 and cites a study on this enzyme.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying a cytochrome P450-type enzyme, but that broad family identity does not distinguish lipid/oxylipin metabolism from steroid biosynthesis.


**Missing item-specific fact**

> The protein-specific identification and functional evidence that this sequence is CYP74M3, a divinyl ether synthase in oxylipin biosynthesis.


**Reason**

> Choosing lipid metabolism over steroid biosynthesis depends on protein-specific functional knowledge not provided in the question. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> C and D both say lipid metabolism, so they are equivalent choices; the input provides no basis to distinguish between them.


### Important caveats

- The sequence-matched pathway annotation is reviewer-only evidence and was not supplied to the evaluated model.
- The exact author data-source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying a cytochrome P450-type enzyme, but that broad family identity does not distinguish lipid/oxylipin metabolism from steroid biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional evidence that this sequence is CYP74M3, a divinyl ether synthase in oxylipin biosynthesis.",
    "reason": "Choosing lipid metabolism over steroid biosynthesis depends on protein-specific functional knowledge not provided in the question. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "pathway_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as divinyl ether synthase CYP74M3, with the pathway listed as lipid metabolism (oxylipin biosynthesis). The pathway annotation carries experimental-evidence code ECO:0000269 and cites a study on this enzyme."
  },
  "important_caveats": [
    "The sequence-matched pathway annotation is reviewer-only evidence and was not supplied to the evaluated model.",
    "The exact author data-source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "C and D both say lipid metabolism, so they are equivalent choices; the input provides no basis to distinguish between them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as divinyl ether synthase CYP74M3, with the pathway listed as lipid metabolism (oxylipin biosynthesis). The pathway annotation carries experimental-evidence code ECO:0000269 and cites a study on this enzyme.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying a cytochrome P450-type enzyme, but that broad family identity does not distinguish lipid/oxylipin metabolism from steroid biosynthesis.",
    "missing_item_specific_fact": "The protein-specific identification and functional evidence that this sequence is CYP74M3, a divinyl ether synthase in oxylipin biosynthesis.",
    "reason": "Choosing lipid metabolism over steroid biosynthesis depends on protein-specific functional knowledge not provided in the question. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "C and D both say lipid metabolism, so they are equivalent choices; the input provides no basis to distinguish between them."
  },
  "important_caveats": [
    "The sequence-matched pathway annotation is reviewer-only evidence and was not supplied to the evaluated model.",
    "The exact author data-source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry D8QZ31 (Divinyl ether synthase CYP74M3, EC 4.2.1.183) from Selaginella moellendorffii is explicitly annotated with PATHWAY: 'Lipid metabolism; oxylipin biosynthesis' (evidence codes ECO:0000269, PubMed:26776054 — experimental). The protein converts fatty acid hydroperoxides to divinyl ethers, a lipid-derived reaction. The expected answer 'Lipid metabolism' matches the annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can reason from the sequence that this is a cytochrome P450 (heme-binding FGAGIAHTPLPH motif, ~495 aa, C-terminal transmembrane anchor), and that P450s participate in multiple pathways including steroid biosynthesis (B) and lipid metabolism (C/D). However, distinguishing 'Lipid metabolism' (oxylipin/divinyl ether biosynthesis from fatty acid hydroperoxides) from 'Steroid biosynthesis' (also P450-catalyzed) requires knowing that this specific enzyme belongs to the CYP74 family, which acts on fatty acid hydroperoxides rather than sterol intermediates. That family assignment is an item-specific database annotation, not derivable from general sequence features alone.


**Missing item-specific fact**

> The specific CYP74 family assignment and its substrate specificity (fatty acid hydroperoxide → divinyl ether) that distinguishes this P450 from steroid-biosynthesizing P450s. Without knowing the exact CYP family or having memorized the CYP74→oxylipin association, a model cannot reliably choose lipid metabolism over steroid biosynthesis from sequence alone.


**Reason**

> The sequence identifies the protein as a P450, which is consistent with both lipid metabolism and steroid biosynthesis. The critical discriminator — that CYP74 enzymes specifically act on fatty acid hydroperoxides in the oxylipin pathway — is an item-specific annotation fact not inferable from general biological reasoning about P450 sequences.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Options C ('Lipid metabolism') and D ('Lipid metabolism. .') are textually identical apart from a trailing period and space, which appear to be formatting artifacts. Both are equally correct and indistinguishable, making the question defective as a single-answer multiple-choice item.


### Important caveats

- Options C and D are functionally identical, rendering the question unsolvable as a unique-answer task. Any model choosing either C or D is correct.
- The UniProt annotation is experimentally supported (ECO:0000269, PubMed:26776054), not merely computational inference.
- The entry was first publicly released in 2025-06-18; the author's source snapshot is unknown but the sequence matches across versions.
- Option A (dihydropteroate synthase / folate pathway) is a clearly incorrect distractor with no structural or functional resemblance to a P450.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can reason from the sequence that this is a cytochrome P450 (heme-binding FGAGIAHTPLPH motif, ~495 aa, C-terminal transmembrane anchor), and that P450s participate in multiple pathways including steroid biosynthesis (B) and lipid metabolism (C/D). However, distinguishing 'Lipid metabolism' (oxylipin/divinyl ether biosynthesis from fatty acid hydroperoxides) from 'Steroid biosynthesis' (also P450-catalyzed) requires knowing that this specific enzyme belongs to the CYP74 family, which acts on fatty acid hydroperoxides rather than sterol intermediates. That family assignment is an item-specific database annotation, not derivable from general sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific CYP74 family assignment and its substrate specificity (fatty acid hydroperoxide → divinyl ether) that distinguishes this P450 from steroid-biosynthesizing P450s. Without knowing the exact CYP family or having memorized the CYP74→oxylipin association, a model cannot reliably choose lipid metabolism over steroid biosynthesis from sequence alone.",
    "reason": "The sequence identifies the protein as a P450, which is consistent with both lipid metabolism and steroid biosynthesis. The critical discriminator — that CYP74 enzymes specifically act on fatty acid hydroperoxides in the oxylipin pathway — is an item-specific annotation fact not inferable from general biological reasoning about P450 sequences."
  },
  "case_id": "pathway_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry D8QZ31 (Divinyl ether synthase CYP74M3, EC 4.2.1.183) from Selaginella moellendorffii is explicitly annotated with PATHWAY: 'Lipid metabolism; oxylipin biosynthesis' (evidence codes ECO:0000269, PubMed:26776054 — experimental). The protein converts fatty acid hydroperoxides to divinyl ethers, a lipid-derived reaction. The expected answer 'Lipid metabolism' matches the annotation."
  },
  "important_caveats": [
    "Options C and D are functionally identical, rendering the question unsolvable as a unique-answer task. Any model choosing either C or D is correct.",
    "The UniProt annotation is experimentally supported (ECO:0000269, PubMed:26776054), not merely computational inference.",
    "The entry was first publicly released in 2025-06-18; the author's source snapshot is unknown but the sequence matches across versions.",
    "Option A (dihydropteroate synthase / folate pathway) is a clearly incorrect distractor with no structural or functional resemblance to a P450."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Options C ('Lipid metabolism') and D ('Lipid metabolism. .') are textually identical apart from a trailing period and space, which appear to be formatting artifacts. Both are equally correct and indistinguishable, making the question defective as a single-answer multiple-choice item."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry D8QZ31 (Divinyl ether synthase CYP74M3, EC 4.2.1.183) from Selaginella moellendorffii is explicitly annotated with PATHWAY: 'Lipid metabolism; oxylipin biosynthesis' (evidence codes ECO:0000269, PubMed:26776054 — experimental). The protein converts fatty acid hydroperoxides to divinyl ethers, a lipid-derived reaction. The expected answer 'Lipid metabolism' matches the annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can reason from the sequence that this is a cytochrome P450 (heme-binding FGAGIAHTPLPH motif, ~495 aa, C-terminal transmembrane anchor), and that P450s participate in multiple pathways including steroid biosynthesis (B) and lipid metabolism (C/D). However, distinguishing 'Lipid metabolism' (oxylipin/divinyl ether biosynthesis from fatty acid hydroperoxides) from 'Steroid biosynthesis' (also P450-catalyzed) requires knowing that this specific enzyme belongs to the CYP74 family, which acts on fatty acid hydroperoxides rather than sterol intermediates. That family assignment is an item-specific database annotation, not derivable from general sequence features alone.",
    "missing_item_specific_fact": "The specific CYP74 family assignment and its substrate specificity (fatty acid hydroperoxide → divinyl ether) that distinguishes this P450 from steroid-biosynthesizing P450s. Without knowing the exact CYP family or having memorized the CYP74→oxylipin association, a model cannot reliably choose lipid metabolism over steroid biosynthesis from sequence alone.",
    "reason": "The sequence identifies the protein as a P450, which is consistent with both lipid metabolism and steroid biosynthesis. The critical discriminator — that CYP74 enzymes specifically act on fatty acid hydroperoxides in the oxylipin pathway — is an item-specific annotation fact not inferable from general biological reasoning about P450 sequences."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Options C ('Lipid metabolism') and D ('Lipid metabolism. .') are textually identical apart from a trailing period and space, which appear to be formatting artifacts. Both are equally correct and indistinguishable, making the question defective as a single-answer multiple-choice item."
  },
  "important_caveats": [
    "Options C and D are functionally identical, rendering the question unsolvable as a unique-answer task. Any model choosing either C or D is correct.",
    "The UniProt annotation is experimentally supported (ECO:0000269, PubMed:26776054), not merely computational inference.",
    "The entry was first publicly released in 2025-06-18; the author's source snapshot is unknown but the sequence matches across versions.",
    "Option A (dihydropteroate synthase / folate pathway) is a clearly incorrect distractor with no structural or functional resemblance to a P450."
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

**Accession:** `D8QZ31` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 68. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:50.224082+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26776054","source":"PubMed"}],"value":"4.2.1.183"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"26776054","source":"PubMed"}],"value":"Etheroleic acid synthase CYP74M3"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26776054","source":"PubMed"}],"value":"Divinyl ether synthase CYP74M3"}}}
```

Source SHA-256: `bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:50.224082+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26776054","source":"PubMed"}],"value":"Lipid metabolism; oxylipin biosynthesis"}]}
```

Source SHA-256: `bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:50.224082+00:00.  

```json
{"citation":{"authors":["Gorina S.S.","Toporkova Y.Y.","Mukhtarova L.S.","Smirnova E.O.","Chechetkin I.R.","Khairutdinov B.I.","Gogolev Y.V.","Grechkin A.N."],"citationCrossReferences":[{"database":"PubMed","id":"26776054"},{"database":"DOI","id":"10.1016/j.bbalip.2016.01.001"}],"citationType":"journal article","firstPage":"301","id":"26776054","journal":"Biochim. Biophys. Acta","lastPage":"309","publicationDate":"2016","title":"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular cloning and identification of divinyl ether synthases CYP74M1 and CYP74M3.","volume":"1861"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:27:52.203972+00:00.  

```text
ID   C74M3_SELML             Reviewed;         495 AA.
AC   D8QZ31;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-OCT-2010, sequence version 1.
DT   28-JAN-2026, entry version 68.
DE   RecName: Full=Divinyl ether synthase CYP74M3 {ECO:0000303|PubMed:26776054};
DE   AltName: Full=Etheroleic acid synthase CYP74M3 {ECO:0000305|PubMed:26776054};
DE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};
GN   Name=CYP74M3 {ECO:0000303|PubMed:26776054};
GN   Synonyms=DES2 {ECO:0000303|PubMed:26776054};
GN   ORFNames=SELMODRAFT_81998 {ECO:0000312|EMBL:EFJ34345.1};
OS   Selaginella moellendorffii (Spikemoss).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Lycopodiopsida; Selaginellales; Selaginellaceae; Selaginella.
OX   NCBI_TaxID=88036;
```

Source SHA-256: `446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)  
**Locator:** `lines 40-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:27:52.203972+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.
RX   PubMed=26776054; DOI=10.1016/j.bbalip.2016.01.001;
RA   Gorina S.S., Toporkova Y.Y., Mukhtarova L.S., Smirnova E.O.,
RA   Chechetkin I.R., Khairutdinov B.I., Gogolev Y.V., Grechkin A.N.;
RT   "Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular
RT   cloning and identification of divinyl ether synthases CYP74M1 and
RT   CYP74M3.";
RL   Biochim. Biophys. Acta 1861:301-309(2016).
```

Source SHA-256: `446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)  
**Locator:** `lines 83-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:27:52.203972+00:00.  

```text
CC   -!- PATHWAY: Lipid metabolism; oxylipin biosynthesis.
CC       {ECO:0000269|PubMed:26776054}.
```

Source SHA-256: `446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
