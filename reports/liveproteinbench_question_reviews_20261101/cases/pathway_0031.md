# pathway_0031

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Glycolipid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MWSLDPSQKEVLRFAVSCRILTLMLQALFNIIIPDHHADAFSPPRLASSCSVDQLVEGLLGGLSRWDAEHFLFIAEHGYLYEHNFAFFPGFPLALLMGTELLRPLQGLLSQRSCLLVSVALLNFLFSVLAAVTLHDLGCLVLGCPRQAFYAAMLFCLSPANVFLAAGYSEALFAFLTFSAMGQLERGRSWASGLLFALATGVRSNGLVSVGFLLHAQCRGFFSSLVVLNPLKPLFKLMASLCLSVLTVSLPFALFQYYAYTQFCLPGSAHSVPEPLVQLAVDKGYRITGGNEPPWCSWGLPLVYSYIQDVYWNVGFLRYYELRQVPNFLLATPVAVLVVWAAWTYVTTHPWLCLTLGLRRSKDSKKTLEKPHPGFLSPKVFVYLVHAAGLLLFGSLCMHVQVLTRLLCSSTPVVYWFPAHLLQNQEPLLRSVDTVPEKLLEKNSPPGQKAPRNCIMKLLYNWRACSPVTRCILGYFLTYWLLGLLLHCNFLPWT

[Multiple Choices]
A. Amino-acid biosynthesis
B. L-valine biosynthesis
C. Glycolipid biosynthesis
D. Glycan degradation
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

> The exact sequence matches the Chinese hamster PIGV entry, whose pathway annotation includes glycolipid biosynthesis and GPI-anchor biosynthesis. The annotation cites a publication as evidence; the supplied excerpts do not independently establish the experimental details.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic and likely multipass membrane protein, but that does not identify its specific pathway or distinguish glycolipid biosynthesis from other membrane-associated functions.


**Missing item-specific fact**

> The protein-specific identity and functional annotation as PIGV, a GPI mannosyltransferase associated with glycolipid/GPI-anchor biosynthesis, are absent from the input.


**Reason**

> Choosing C depends on knowing this sequence's particular protein identity or equivalent external functional evidence; generic sequence features do not distinguish the listed pathways.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports C for this protein, although the sequence and choices alone do not provide a biological basis for selecting it.


### Important caveats

- The reviewer-only database record matches the sequence exactly; that identity information was not supplied to the evaluated model.
- The pathway annotation cites experimental literature, but the excerpts are database annotations rather than an independent review of the underlying experiments.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and likely multipass membrane protein, but that does not identify its specific pathway or distinguish glycolipid biosynthesis from other membrane-associated functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and functional annotation as PIGV, a GPI mannosyltransferase associated with glycolipid/GPI-anchor biosynthesis, are absent from the input.",
    "reason": "Choosing C depends on knowing this sequence's particular protein identity or equivalent external functional evidence; generic sequence features do not distinguish the listed pathways."
  },
  "case_id": "pathway_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Chinese hamster PIGV entry, whose pathway annotation includes glycolipid biosynthesis and GPI-anchor biosynthesis. The annotation cites a publication as evidence; the supplied excerpts do not independently establish the experimental details."
  },
  "important_caveats": [
    "The reviewer-only database record matches the sequence exactly; that identity information was not supplied to the evaluated model.",
    "The pathway annotation cites experimental literature, but the excerpts are database annotations rather than an independent review of the underlying experiments."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports C for this protein, although the sequence and choices alone do not provide a biological basis for selecting it."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Chinese hamster PIGV entry, whose pathway annotation includes glycolipid biosynthesis and GPI-anchor biosynthesis. The annotation cites a publication as evidence; the supplied excerpts do not independently establish the experimental details.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and likely multipass membrane protein, but that does not identify its specific pathway or distinguish glycolipid biosynthesis from other membrane-associated functions.",
    "missing_item_specific_fact": "The protein-specific identity and functional annotation as PIGV, a GPI mannosyltransferase associated with glycolipid/GPI-anchor biosynthesis, are absent from the input.",
    "reason": "Choosing C depends on knowing this sequence's particular protein identity or equivalent external functional evidence; generic sequence features do not distinguish the listed pathways."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports C for this protein, although the sequence and choices alone do not provide a biological basis for selecting it."
  },
  "important_caveats": [
    "The reviewer-only database record matches the sequence exactly; that identity information was not supplied to the evaluated model.",
    "The pathway annotation cites experimental literature, but the excerpts are database annotations rather than an independent review of the underlying experiments."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A8C2M425 (PIGV_CRIGR, GPI alpha-1,6-mannosyltransferase 2) is explicitly annotated with pathway 'Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:23694781). The protein catalyzes mannosyl transfer in GPI-anchor assembly, a glycolipid biosynthesis pathway. The sequence matches exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a ~494-residue protein with multiple transmembrane segments (at least 6-7 predicted TM helices), characteristic of ER-membrane-resident glycolipid biosynthetic enzymes. This multi-TM architecture strongly disfavors glycan degradation (D), which typically involves soluble lysosomal glycosidases. It also disfavors amino-acid biosynthesis (A), whose mammalian enzymes are soluble cytosolic/mitochondrial proteins. L-valine biosynthesis (B) is impossible in mammals since valine is an essential amino acid. The multi-TM ER membrane topology combined with mammalian origin provides a concrete biological argument favoring glycolipid biosynthesis (C) over all three alternatives.


**Missing item-specific fact**

> None strictly required. Precise identification as a GPI mannosyltransferase (GT4-family mannosyltransferase motif) would strengthen confidence, but the TM-domain topology and mammalian context already meaningfully distinguish C from the other choices.


**Reason**

> The multi-TM membrane architecture is a general, interpretable feature of the supplied sequence that aligns with ER glycolipid biosynthesis machinery rather than soluble degradation or amino-acid biosynthesis enzymes. The mammalian source eliminates valine biosynthesis as a biological impossibility. These are general biological arguments derivable from the sequence and context without needing to recall this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices are well-separated by general biological reasoning: B is impossible in mammals, A involves soluble enzymes incompatible with multi-TM topology, and D involves lysosomal soluble enzymes. Only C is consistent with a multi-TM ER membrane glycolipid biosynthetic enzyme.


### Important caveats

- The pathway name in UniProt is 'Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis'; the option 'Glycolipid biosynthesis' is a valid abbreviation of this.
- The protein name annotation (GPI alpha-1,6-mannosyltransferase 2) is transferred by similarity (ECO:0000250 from Q9NUD9 human PIGV), but the pathway assignment is experimentally supported (ECO:0000269, PubMed:23694781).
- The multi-TM reasoning is a heuristic; a model without TM prediction tools might struggle to count helices accurately from raw sequence, though the hydrophobic stretches are visually apparent.
- The reviewer-only evidence confirms the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a ~494-residue protein with multiple transmembrane segments (at least 6-7 predicted TM helices), characteristic of ER-membrane-resident glycolipid biosynthetic enzymes. This multi-TM architecture strongly disfavors glycan degradation (D), which typically involves soluble lysosomal glycosidases. It also disfavors amino-acid biosynthesis (A), whose mammalian enzymes are soluble cytosolic/mitochondrial proteins. L-valine biosynthesis (B) is impossible in mammals since valine is an essential amino acid. The multi-TM ER membrane topology combined with mammalian origin provides a concrete biological argument favoring glycolipid biosynthesis (C) over all three alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Precise identification as a GPI mannosyltransferase (GT4-family mannosyltransferase motif) would strengthen confidence, but the TM-domain topology and mammalian context already meaningfully distinguish C from the other choices.",
    "reason": "The multi-TM membrane architecture is a general, interpretable feature of the supplied sequence that aligns with ER glycolipid biosynthesis machinery rather than soluble degradation or amino-acid biosynthesis enzymes. The mammalian source eliminates valine biosynthesis as a biological impossibility. These are general biological arguments derivable from the sequence and context without needing to recall this specific protein's database entry."
  },
  "case_id": "pathway_0031",
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
    "reason": "UniProt entry A0A8C2M425 (PIGV_CRIGR, GPI alpha-1,6-mannosyltransferase 2) is explicitly annotated with pathway 'Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:23694781). The protein catalyzes mannosyl transfer in GPI-anchor assembly, a glycolipid biosynthesis pathway. The sequence matches exactly."
  },
  "important_caveats": [
    "The pathway name in UniProt is 'Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis'; the option 'Glycolipid biosynthesis' is a valid abbreviation of this.",
    "The protein name annotation (GPI alpha-1,6-mannosyltransferase 2) is transferred by similarity (ECO:0000250 from Q9NUD9 human PIGV), but the pathway assignment is experimentally supported (ECO:0000269, PubMed:23694781).",
    "The multi-TM reasoning is a heuristic; a model without TM prediction tools might struggle to count helices accurately from raw sequence, though the hydrophobic stretches are visually apparent.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated by general biological reasoning: B is impossible in mammals, A involves soluble enzymes incompatible with multi-TM topology, and D involves lysosomal soluble enzymes. Only C is consistent with a multi-TM ER membrane glycolipid biosynthetic enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A8C2M425 (PIGV_CRIGR, GPI alpha-1,6-mannosyltransferase 2) is explicitly annotated with pathway 'Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:23694781). The protein catalyzes mannosyl transfer in GPI-anchor assembly, a glycolipid biosynthesis pathway. The sequence matches exactly.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence encodes a ~494-residue protein with multiple transmembrane segments (at least 6-7 predicted TM helices), characteristic of ER-membrane-resident glycolipid biosynthetic enzymes. This multi-TM architecture strongly disfavors glycan degradation (D), which typically involves soluble lysosomal glycosidases. It also disfavors amino-acid biosynthesis (A), whose mammalian enzymes are soluble cytosolic/mitochondrial proteins. L-valine biosynthesis (B) is impossible in mammals since valine is an essential amino acid. The multi-TM ER membrane topology combined with mammalian origin provides a concrete biological argument favoring glycolipid biosynthesis (C) over all three alternatives.",
    "missing_item_specific_fact": "None strictly required. Precise identification as a GPI mannosyltransferase (GT4-family mannosyltransferase motif) would strengthen confidence, but the TM-domain topology and mammalian context already meaningfully distinguish C from the other choices.",
    "reason": "The multi-TM membrane architecture is a general, interpretable feature of the supplied sequence that aligns with ER glycolipid biosynthesis machinery rather than soluble degradation or amino-acid biosynthesis enzymes. The mammalian source eliminates valine biosynthesis as a biological impossibility. These are general biological arguments derivable from the sequence and context without needing to recall this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated by general biological reasoning: B is impossible in mammals, A involves soluble enzymes incompatible with multi-TM topology, and D involves lysosomal soluble enzymes. Only C is consistent with a multi-TM ER membrane glycolipid biosynthetic enzyme."
  },
  "important_caveats": [
    "The pathway name in UniProt is 'Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis'; the option 'Glycolipid biosynthesis' is a valid abbreviation of this.",
    "The protein name annotation (GPI alpha-1,6-mannosyltransferase 2) is transferred by similarity (ECO:0000250 from Q9NUD9 human PIGV), but the pathway assignment is experimentally supported (ECO:0000269, PubMed:23694781).",
    "The multi-TM reasoning is a heuristic; a model without TM prediction tools might struggle to count helices accurately from raw sequence, though the hydrophobic stretches are visually apparent.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model."
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

**Accession:** `A0A8C2M425` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

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
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23694781","source":"PubMed"}],"value":"Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis"}]}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"citation":{"authors":["Hirata T.","Fujita M.","Kanzawa N.","Murakami Y.","Maeda Y.","Kinoshita T."],"citationCrossReferences":[{"database":"PubMed","id":"23694781"},{"database":"DOI","id":"10.1093/jb/mvt045"}],"citationType":"journal article","firstPage":"257","id":"23694781","journal":"J. Biochem.","lastPage":"264","publicationDate":"2013","title":"Glycosylphosphatidylinositol mannosyltransferase II is the rate-limiting enzyme in glycosylphosphatidylinositol biosynthesis under limited dolichol-phosphate mannose availability.","volume":"154"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
ID   PIGV_CRIGR              Reviewed;         494 AA.
AC   A0A8C2M425;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-JAN-2022, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=GPI alpha-1,6-mannosyltransferase 2 {ECO:0000250|UniProtKB:Q9NUD9};
DE            EC=2.4.1.- {ECO:0000269|PubMed:23694781};
DE   AltName: Full=GPI mannosyltransferase II;
DE            Short=GPI-MT-II {ECO:0000250|UniProtKB:Q9NUD9};
DE   AltName: Full=Phosphatidylinositol-glycan biosynthesis class V protein {ECO:0000250|UniProtKB:Q9NUD9};
DE            Short=PIG-V {ECO:0000250|UniProtKB:Q9NUD9};
GN   Name=PIGV {ECO:0000303|PubMed:23694781};
OS   Cricetulus griseus (Chinese hamster) (Cricetulus barabensis griseus).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea;
OC   Cricetidae; Cricetinae; Cricetulus.
OX   NCBI_TaxID=10029;
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 28-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RX   PubMed=23694781; DOI=10.1093/jb/mvt045;
RA   Hirata T., Fujita M., Kanzawa N., Murakami Y., Maeda Y., Kinoshita T.;
RT   "Glycosylphosphatidylinositol mannosyltransferase II is the rate-limiting
RT   enzyme in glycosylphosphatidylinositol biosynthesis under limited dolichol-
RT   phosphate mannose availability.";
RL   J. Biochem. 154:257-264(2013).
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 75-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
CC   -!- PATHWAY: Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor
CC       biosynthesis. {ECO:0000269|PubMed:23694781}.
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 31. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
