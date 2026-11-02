# catalytic_activity_0154

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGVEEADKLKQLGNAAFSERKWHLAIDMYTKAIELTKTPTLFCNRALAELRAELPGAALADADAALGIEPTFAKAYYHKASAYLSLGKHKQALTNYKKVVDLAPQNSDAQAKVEFCKKEIRRINFENAIMTPDEAPLSQTIKLGSVRADYDGPRIENETVTVEFVEAMKEHFRLEKLIDRHDVIFILLEVQKILKKCPNFVSINVPVGEEITVCGDTHGQYYDLLNIFKLNGNPLETNRYLFNGDFVDRGSYSFENIMTLFAYKVLYPDHFFLSRGNHEGVSMNRMYGFEGEVTQKYNSEMFRLFTEVFNSLPIGHIINNEVFVVHGGLYSSDKVTLDDLQHPNRFRDIPESGLICESLWSDPQPMPGRAPSKRGVSCLSFGPDVTETFLNNNNLKLLVRSHEVKDEGYEIEHGGKCITVFSAPNYCDQMGNKGAFIRFTGGDMKPRFTTFTHVPHPGKRPMHYATGFGLF

[Multiple Choices]
A. luteothin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = aureothin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O
B. O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate
C. cytidine(in) = cytidine(out)
D. 4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NAD(+) + H2O
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

> The exact sequence is matched to a UniProt entry annotated as a serine/threonine protein phosphatase, with the reaction in B. The annotation cites a publication, although the supplied evidence does not independently establish what experiments were performed.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a protein-phosphatase catalytic domain, including a conserved catalytic-region motif (…VCGDTHG…), consistent with hydrolysis of phosphate from protein-bound residues. That distinguishes the protein-phosphatase reaction in B from the unrelated transformations in the other choices.


**Missing item-specific fact**

> No additional item-specific fact is needed to distinguish B from the listed alternatives. The exact serine-versus-threonine substrate scope is not uniquely determined by this broad inference.


**Reason**

> Recognizing the phosphatase family from its catalytic sequence features provides a concrete biological basis for selecting the protein dephosphorylation reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotation also lists phosphothreonine dephosphorylation, but that reaction is not a separate choice; among the listed options, B is the matching protein-phosphatase reaction.


### Important caveats

- The annotation supports B for the sequence-matched protein; it should not be treated as independent experimental validation beyond the cited annotation evidence.
- The enzyme is annotated for both serine- and threonine-phosphorylated protein substrates.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a protein-phosphatase catalytic domain, including a conserved catalytic-region motif (…VCGDTHG…), consistent with hydrolysis of phosphate from protein-bound residues. That distinguishes the protein-phosphatase reaction in B from the unrelated transformations in the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No additional item-specific fact is needed to distinguish B from the listed alternatives. The exact serine-versus-threonine substrate scope is not uniquely determined by this broad inference.",
    "reason": "Recognizing the phosphatase family from its catalytic sequence features provides a concrete biological basis for selecting the protein dephosphorylation reaction."
  },
  "case_id": "catalytic_activity_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence is matched to a UniProt entry annotated as a serine/threonine protein phosphatase, with the reaction in B. The annotation cites a publication, although the supplied evidence does not independently establish what experiments were performed."
  },
  "important_caveats": [
    "The annotation supports B for the sequence-matched protein; it should not be treated as independent experimental validation beyond the cited annotation evidence.",
    "The enzyme is annotated for both serine- and threonine-phosphorylated protein substrates."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation also lists phosphothreonine dephosphorylation, but that reaction is not a separate choice; among the listed options, B is the matching protein-phosphatase reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0154",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence is matched to a UniProt entry annotated as a serine/threonine protein phosphatase, with the reaction in B. The annotation cites a publication, although the supplied evidence does not independently establish what experiments were performed.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a protein-phosphatase catalytic domain, including a conserved catalytic-region motif (…VCGDTHG…), consistent with hydrolysis of phosphate from protein-bound residues. That distinguishes the protein-phosphatase reaction in B from the unrelated transformations in the other choices.",
    "missing_item_specific_fact": "No additional item-specific fact is needed to distinguish B from the listed alternatives. The exact serine-versus-threonine substrate scope is not uniquely determined by this broad inference.",
    "reason": "Recognizing the phosphatase family from its catalytic sequence features provides a concrete biological basis for selecting the protein dephosphorylation reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation also lists phosphothreonine dephosphorylation, but that reaction is not a separate choice; among the listed options, B is the matching protein-phosphatase reaction."
  },
  "important_caveats": [
    "The annotation supports B for the sequence-matched protein; it should not be treated as independent experimental validation beyond the cited annotation evidence.",
    "The enzyme is annotated for both serine- and threonine-phosphorylated protein substrates."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 472-aa sequence exactly matches UniProt Q388N2 (PPP5_TRYB2), a Serine/threonine-protein phosphatase T (EC 3.1.3.16) from Trypanosoma brucei. The UniProt entry explicitly lists the catalytic reaction 'O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate' (Rhea:RHEA:20629), supported by experimental characterization in PubMed:11290414 (Chaudhuri 2001). The expected answer B matches this annotation verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple conserved PPP-superfamily phosphatase catalytic motifs: GDTHG (GDxHG motif around position ~140), GDFVDRGS (GDxVDR motif), GPDVTETFL (GD motif), HGGLYSSDKV (HG motif), and GGKCITVFSAPNY (GG motif). These are the hallmark metal-binding and catalytic residues of the phosphoprotein phosphatase (PPP) family. Recognizing these motifs identifies the enzyme as a phosphatase. Among the four choices, only B describes a phosphatase reaction (hydrolysis of a phosphoester bond in a phosphoprotein); A is a monooxygenase/oxidase reaction, C is a transport reaction, and D is a reductase reaction. Thus, family-level motif recognition is sufficient to select B.


**Missing item-specific fact**

> None critical. The PPP-family catalytic motifs are directly observable in the supplied sequence, and the only phosphatase reaction among the choices is B.


**Reason**

> A model with knowledge of the PPP phosphatase superfamily can identify the GDxHG, GD, HG, and GG motifs in the sequence, infer the enzyme is a phosphatase, and eliminate the non-phosphatase distractors (oxidase, transporter, reductase). This constitutes a concrete biological argument grounded in the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only B is a phosphatase reaction. The protein also catalyzes threonine dephosphorylation (Rhea:RHEA:47004), but that reaction is not offered as an alternative. No other choice is defensible for a PPP-family phosphatase.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (curator inference from published paper PubMed:11290414), not ECO:0000269 (direct experimental evidence). The original paper characterized the enzyme biochemically, so the annotation is experimentally grounded.
- The protein also catalyzes O-phospho-L-threonyl-&#91;protein&#93; hydrolysis (C6/H5); the question selects only the serine-specific reaction, which is one of two documented activities but is the only phosphatase option presented.
- The PPP-family motif identification provides enzyme-class-level reasoning (phosphatase vs. oxidase/transporter/reductase), not residue-level mechanistic proof, but this is sufficient to discriminate among the given choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple conserved PPP-superfamily phosphatase catalytic motifs: GDTHG (GDxHG motif around position ~140), GDFVDRGS (GDxVDR motif), GPDVTETFL (GD motif), HGGLYSSDKV (HG motif), and GGKCITVFSAPNY (GG motif). These are the hallmark metal-binding and catalytic residues of the phosphoprotein phosphatase (PPP) family. Recognizing these motifs identifies the enzyme as a phosphatase. Among the four choices, only B describes a phosphatase reaction (hydrolysis of a phosphoester bond in a phosphoprotein); A is a monooxygenase/oxidase reaction, C is a transport reaction, and D is a reductase reaction. Thus, family-level motif recognition is sufficient to select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PPP-family catalytic motifs are directly observable in the supplied sequence, and the only phosphatase reaction among the choices is B.",
    "reason": "A model with knowledge of the PPP phosphatase superfamily can identify the GDxHG, GD, HG, and GG motifs in the sequence, infer the enzyme is a phosphatase, and eliminate the non-phosphatase distractors (oxidase, transporter, reductase). This constitutes a concrete biological argument grounded in the supplied sequence."
  },
  "case_id": "catalytic_activity_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 472-aa sequence exactly matches UniProt Q388N2 (PPP5_TRYB2), a Serine/threonine-protein phosphatase T (EC 3.1.3.16) from Trypanosoma brucei. The UniProt entry explicitly lists the catalytic reaction 'O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate' (Rhea:RHEA:20629), supported by experimental characterization in PubMed:11290414 (Chaudhuri 2001). The expected answer B matches this annotation verbatim."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (curator inference from published paper PubMed:11290414), not ECO:0000269 (direct experimental evidence). The original paper characterized the enzyme biochemically, so the annotation is experimentally grounded.",
    "The protein also catalyzes O-phospho-L-threonyl-[protein] hydrolysis (C6/H5); the question selects only the serine-specific reaction, which is one of two documented activities but is the only phosphatase option presented.",
    "The PPP-family motif identification provides enzyme-class-level reasoning (phosphatase vs. oxidase/transporter/reductase), not residue-level mechanistic proof, but this is sufficient to discriminate among the given choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only B is a phosphatase reaction. The protein also catalyzes threonine dephosphorylation (Rhea:RHEA:47004), but that reaction is not offered as an alternative. No other choice is defensible for a PPP-family phosphatase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0154",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 472-aa sequence exactly matches UniProt Q388N2 (PPP5_TRYB2), a Serine/threonine-protein phosphatase T (EC 3.1.3.16) from Trypanosoma brucei. The UniProt entry explicitly lists the catalytic reaction 'O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate' (Rhea:RHEA:20629), supported by experimental characterization in PubMed:11290414 (Chaudhuri 2001). The expected answer B matches this annotation verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple conserved PPP-superfamily phosphatase catalytic motifs: GDTHG (GDxHG motif around position ~140), GDFVDRGS (GDxVDR motif), GPDVTETFL (GD motif), HGGLYSSDKV (HG motif), and GGKCITVFSAPNY (GG motif). These are the hallmark metal-binding and catalytic residues of the phosphoprotein phosphatase (PPP) family. Recognizing these motifs identifies the enzyme as a phosphatase. Among the four choices, only B describes a phosphatase reaction (hydrolysis of a phosphoester bond in a phosphoprotein); A is a monooxygenase/oxidase reaction, C is a transport reaction, and D is a reductase reaction. Thus, family-level motif recognition is sufficient to select B.",
    "missing_item_specific_fact": "None critical. The PPP-family catalytic motifs are directly observable in the supplied sequence, and the only phosphatase reaction among the choices is B.",
    "reason": "A model with knowledge of the PPP phosphatase superfamily can identify the GDxHG, GD, HG, and GG motifs in the sequence, infer the enzyme is a phosphatase, and eliminate the non-phosphatase distractors (oxidase, transporter, reductase). This constitutes a concrete biological argument grounded in the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only B is a phosphatase reaction. The protein also catalyzes threonine dephosphorylation (Rhea:RHEA:47004), but that reaction is not offered as an alternative. No other choice is defensible for a PPP-family phosphatase."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (curator inference from published paper PubMed:11290414), not ECO:0000269 (direct experimental evidence). The original paper characterized the enzyme biochemically, so the annotation is experimentally grounded.",
    "The protein also catalyzes O-phospho-L-threonyl-[protein] hydrolysis (C6/H5); the question selects only the serine-specific reaction, which is one of two documented activities but is the only phosphatase option presented.",
    "The PPP-family motif identification provides enzyme-class-level reasoning (phosphatase vs. oxidase/transporter/reductase), not residue-level mechanistic proof, but this is sufficient to discriminate among the given choices."
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

**Accession:** `Q388N2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 114. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
"Q388N2"
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"11290414","source":"PubMed"}],"value":"TbPP5"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Serine/threonine-protein phosphatase T"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PPT"}]}}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:47005"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"name":"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:47004"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:61977"}]}}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"citation":{"authors":["Chaudhuri M."],"citationCrossReferences":[{"database":"PubMed","id":"11290414"},{"database":"DOI","id":"10.1016/s0378-1119(01)00367-5"}],"citationType":"journal article","firstPage":"1","id":"11290414","journal":"Gene","lastPage":"13","publicationDate":"2001","title":"Cloning and characterization of a novel serine/threonine protein phosphatase type 5 from Trypanosoma brucei.","volume":"266"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11290414","source":"PubMed"}],"type":"STRAIN","value":"LUMP 1026"}],"referenceNumber":2,"referencePositions":["CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
ID   PPP5_TRYB2              Reviewed;         472 AA.
AC   Q388N2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   22-NOV-2005, sequence version 1.
DT   28-JAN-2026, entry version 114.
DE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000305};
DE            Short=PPT {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000305|PubMed:11290414};
DE   AltName: Full=TbPP5 {ECO:0000303|PubMed:11290414};
GN   Name=PPT1 {ECO:0000305};
GN   ORFNames=Tb10.05.0110 {ECO:0000312|EMBL:EAN78738.1};
OS   Trypanosoma brucei brucei (strain 927/4 GUTat10.1).
OC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;
OC   Trypanosomatida; Trypanosomatidae; Trypanosoma.
OX   NCBI_TaxID=185431 {ECO:0000312|Proteomes:UP000008524};
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
DE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000305};
DE            Short=PPT {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000305|PubMed:11290414};
DE   AltName: Full=TbPP5 {ECO:0000303|PubMed:11290414};
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 40-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
RN   [2] {ECO:0000305}
RP   CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND
RP   SUBCELLULAR LOCATION.
RC   STRAIN=LUMP 1026 {ECO:0000303|PubMed:11290414};
RX   PubMed=11290414; DOI=10.1016/s0378-1119(01)00367-5;
RA   Chaudhuri M.;
RT   "Cloning and characterization of a novel serine/threonine protein
RT   phosphatase type 5 from Trypanosoma brucei.";
RL   Gene 266:1-13(2001).
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 51-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:11290414};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000305|PubMed:11290414};
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 59-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:61977; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:11290414};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;
CC         Evidence={ECO:0000305|PubMed:11290414};
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 154. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
