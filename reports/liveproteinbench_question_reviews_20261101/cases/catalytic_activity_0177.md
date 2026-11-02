# catalytic_activity_0177

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVMKFTWRSIIPRCSKGIEEPEAEAEAEPETKKQDSKQGSFSRLAMIDLSYPSSRFTEDLSTSLAGSNLYVFTLEELKVITQCFSSANFLGEGGFGPVHKGFIDDNLRPGLEAQPVAVKLLDLEGLQGHREWLTEVVFLAQLSHPHLVKLIGYCCEDEHRLLVYEYMPRGSLENQLFAKYSVPLPWSTRMKIALGAAKGLAYLHEAEKPVIYRDFKASNILLDSDYSAKLSDFGLAKDGPEGDKTHVSTRVMGTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRSLDKSRSPREQNLAEWARPMLNESRRLARIMDPKLEGQYSETGARKAAALAYQCLSHRAKQRPKMSDVVNILEPLLDYEETSVGTFVYTVPTHQNGGSPPKDDTDTKECEAKTELKKENGDHHNRHHHRRSHKSRDGHRHRNKSSSQSSVHSENYTSKQTLENGSNEECNID

[Multiple Choices]
A. a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)
B. L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)
C. aminoacetaldehyde + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + glycine + 3 H(+)
D. N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
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

> The exact sequence matches a UniProt entry annotated as a serine/threonine protein kinase, with the serine-phosphorylation reaction listed. That catalytic-activity annotation is attributed to a PROSITE rule, so it is computational support rather than direct experimental confirmation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable protein-kinase features, including a kinase-like catalytic Lys region and conserved DFG and APE motifs. ATP-dependent protein phosphorylation (B) fits this kinase architecture; the other options describe unrelated reaction classes.


**Missing item-specific fact**

> The exact protein-specific annotation and independent confirmation of serine versus threonine activity are not supplied. However, the listed choices make B the only protein-kinase reaction.


**Reason**

> The sequence supports identifying a protein kinase and distinguishes its reaction class from the distractors without requiring recognition of the exact protein. The specific residue-level annotation remains computationally inferred in the cited database evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B describes protein phosphorylation. The database also annotates threonine phosphorylation for this kinase, but that reaction is not among the choices.


### Important caveats

- The cited catalytic-activity evidence is a PROSITE-rule annotation, not direct experimental evidence.
- The sequence match is exact, but the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable protein-kinase features, including a kinase-like catalytic Lys region and conserved DFG and APE motifs. ATP-dependent protein phosphorylation (B) fits this kinase architecture; the other options describe unrelated reaction classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein-specific annotation and independent confirmation of serine versus threonine activity are not supplied. However, the listed choices make B the only protein-kinase reaction.",
    "reason": "The sequence supports identifying a protein kinase and distinguishes its reaction class from the distractors without requiring recognition of the exact protein. The specific residue-level annotation remains computationally inferred in the cited database evidence."
  },
  "case_id": "catalytic_activity_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a serine/threonine protein kinase, with the serine-phosphorylation reaction listed. That catalytic-activity annotation is attributed to a PROSITE rule, so it is computational support rather than direct experimental confirmation."
  },
  "important_caveats": [
    "The cited catalytic-activity evidence is a PROSITE-rule annotation, not direct experimental evidence.",
    "The sequence match is exact, but the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B describes protein phosphorylation. The database also annotates threonine phosphorylation for this kinase, but that reaction is not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a serine/threonine protein kinase, with the serine-phosphorylation reaction listed. That catalytic-activity annotation is attributed to a PROSITE rule, so it is computational support rather than direct experimental confirmation.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable protein-kinase features, including a kinase-like catalytic Lys region and conserved DFG and APE motifs. ATP-dependent protein phosphorylation (B) fits this kinase architecture; the other options describe unrelated reaction classes.",
    "missing_item_specific_fact": "The exact protein-specific annotation and independent confirmation of serine versus threonine activity are not supplied. However, the listed choices make B the only protein-kinase reaction.",
    "reason": "The sequence supports identifying a protein kinase and distinguishes its reaction class from the distractors without requiring recognition of the exact protein. The specific residue-level annotation remains computationally inferred in the cited database evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B describes protein phosphorylation. The database also annotates threonine phosphorylation for this kinase, but that reaction is not among the choices."
  },
  "important_caveats": [
    "The cited catalytic-activity evidence is a PROSITE-rule annotation, not direct experimental evidence.",
    "The sequence match is exact, but the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A5J5T2N2 (sequence SHA256 matched) annotates this protein as EC 2.7.11.1 (serine/threonine-protein kinase) with the explicit catalytic reaction 'L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)'. The evidence code is ECO:0000255 (PROSITE-ProRule:PRU10027), a computational family-rule annotation, but the protein name and kinase activity are corroborated by experimental work (PubMed:39488762) documenting phosphorylation at multiple serine residues. The sequence in the benchmark matches the annotated entry exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical protein kinase catalytic domain motifs: a glycine-rich loop (GGFGPV), the β3 lysine (VAVK), the catalytic-loop DFG motif (LSDFGLAK), and the APE motif (GYAAPE). These hallmarks unambiguously identify the protein as a protein kinase, eliminating the phospholipase (A), iron-sulfur oxidoreductase (C), and SAM-dependent methyltransferase (D) options. Since only a serine-phosphorylation kinase reaction is offered among the choices, the model can select B without needing to distinguish serine from threonine specificity.


**Missing item-specific fact**

> None required. The kinase fold motifs are visible in the supplied sequence and are sufficient to exclude the three non-kinase distractors.


**Reason**

> A model trained on protein structural biology can recognize the kinase catalytic domain from the sequence motifs and rule out the other three enzyme classes (hydrolase, oxidoreductase, transferase using SAM) on mechanistic grounds. No item-specific database lookup is needed to eliminate A, C, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is annotated as both a serine and threonine kinase (EC 2.7.11.1), but only the serine-phosphorylation reaction appears among the choices. The remaining three options belong to entirely different enzyme classes (phospholipase, ferredoxin-dependent oxidoreductase, N-methyltransferase) and are clearly incompatible with the kinase domain motifs present in the sequence. No ambiguity exists.


### Important caveats

- The EC assignment evidence is ECO:0000255 (PROSITE-ProRule), i.e., computational inference from protein-family rules, not direct in vitro kinetic measurement of this specific protein. However, the protein is experimentally characterized as a kinase in the cited PubMed study (phosphorylation at multiple Ser residues documented).
- The UniProt entry was first publicly released on 2025-06-18; the author's exact source snapshot is unknown, though the sequence has been unchanged since 2019-12-11.
- The protein also catalyzes threonine phosphorylation (C6/H5), but no threonine option is presented, so this does not affect answer selection.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical protein kinase catalytic domain motifs: a glycine-rich loop (GGFGPV), the β3 lysine (VAVK), the catalytic-loop DFG motif (LSDFGLAK), and the APE motif (GYAAPE). These hallmarks unambiguously identify the protein as a protein kinase, eliminating the phospholipase (A), iron-sulfur oxidoreductase (C), and SAM-dependent methyltransferase (D) options. Since only a serine-phosphorylation kinase reaction is offered among the choices, the model can select B without needing to distinguish serine from threonine specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The kinase fold motifs are visible in the supplied sequence and are sufficient to exclude the three non-kinase distractors.",
    "reason": "A model trained on protein structural biology can recognize the kinase catalytic domain from the sequence motifs and rule out the other three enzyme classes (hydrolase, oxidoreductase, transferase using SAM) on mechanistic grounds. No item-specific database lookup is needed to eliminate A, C, and D."
  },
  "case_id": "catalytic_activity_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A5J5T2N2 (sequence SHA256 matched) annotates this protein as EC 2.7.11.1 (serine/threonine-protein kinase) with the explicit catalytic reaction 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)'. The evidence code is ECO:0000255 (PROSITE-ProRule:PRU10027), a computational family-rule annotation, but the protein name and kinase activity are corroborated by experimental work (PubMed:39488762) documenting phosphorylation at multiple serine residues. The sequence in the benchmark matches the annotated entry exactly."
  },
  "important_caveats": [
    "The EC assignment evidence is ECO:0000255 (PROSITE-ProRule), i.e., computational inference from protein-family rules, not direct in vitro kinetic measurement of this specific protein. However, the protein is experimentally characterized as a kinase in the cited PubMed study (phosphorylation at multiple Ser residues documented).",
    "The UniProt entry was first publicly released on 2025-06-18; the author's exact source snapshot is unknown, though the sequence has been unchanged since 2019-12-11.",
    "The protein also catalyzes threonine phosphorylation (C6/H5), but no threonine option is presented, so this does not affect answer selection."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is annotated as both a serine and threonine kinase (EC 2.7.11.1), but only the serine-phosphorylation reaction appears among the choices. The remaining three options belong to entirely different enzyme classes (phospholipase, ferredoxin-dependent oxidoreductase, N-methyltransferase) and are clearly incompatible with the kinase domain motifs present in the sequence. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A5J5T2N2 (sequence SHA256 matched) annotates this protein as EC 2.7.11.1 (serine/threonine-protein kinase) with the explicit catalytic reaction 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)'. The evidence code is ECO:0000255 (PROSITE-ProRule:PRU10027), a computational family-rule annotation, but the protein name and kinase activity are corroborated by experimental work (PubMed:39488762) documenting phosphorylation at multiple serine residues. The sequence in the benchmark matches the annotated entry exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical protein kinase catalytic domain motifs: a glycine-rich loop (GGFGPV), the β3 lysine (VAVK), the catalytic-loop DFG motif (LSDFGLAK), and the APE motif (GYAAPE). These hallmarks unambiguously identify the protein as a protein kinase, eliminating the phospholipase (A), iron-sulfur oxidoreductase (C), and SAM-dependent methyltransferase (D) options. Since only a serine-phosphorylation kinase reaction is offered among the choices, the model can select B without needing to distinguish serine from threonine specificity.",
    "missing_item_specific_fact": "None required. The kinase fold motifs are visible in the supplied sequence and are sufficient to exclude the three non-kinase distractors.",
    "reason": "A model trained on protein structural biology can recognize the kinase catalytic domain from the sequence motifs and rule out the other three enzyme classes (hydrolase, oxidoreductase, transferase using SAM) on mechanistic grounds. No item-specific database lookup is needed to eliminate A, C, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is annotated as both a serine and threonine kinase (EC 2.7.11.1), but only the serine-phosphorylation reaction appears among the choices. The remaining three options belong to entirely different enzyme classes (phospholipase, ferredoxin-dependent oxidoreductase, N-methyltransferase) and are clearly incompatible with the kinase domain motifs present in the sequence. No ambiguity exists."
  },
  "important_caveats": [
    "The EC assignment evidence is ECO:0000255 (PROSITE-ProRule), i.e., computational inference from protein-family rules, not direct in vitro kinetic measurement of this specific protein. However, the protein is experimentally characterized as a kinase in the cited PubMed study (phosphorylation at multiple Ser residues documented).",
    "The UniProt entry was first publicly released on 2025-06-18; the author's exact source snapshot is unknown, though the sequence has been unchanged since 2019-12-11.",
    "The protein also catalyzes threonine phosphorylation (C6/H5), but no threonine option is presented, so this does not affect answer selection."
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

**Accession:** `A0A5J5T2N2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 17. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.786512+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39488762","source":"PubMed"}],"value":"EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5A"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39488762","source":"PubMed"}],"value":"GbEIR5A"}]}}
```

Source SHA-256: `2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.786512+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.786512+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.786512+00:00.  

```json
{"citation":{"authors":["Sun L.","Li X.","Zhong J.","Wang Y.","Li B.","Ye Z.","Zhang J."],"citationCrossReferences":[{"database":"PubMed","id":"39488762"},{"database":"DOI","id":"10.1002/advs.202407787"}],"citationType":"journal article","firstPage":"e2407787","id":"39488762","journal":"Adv. Sci.","lastPage":"e2407787","publicationDate":"2025","title":"Recognition of a fungal effector potentiates pathogen-associated molecular pattern-triggered immunity in cotton.","volume":"12"},"referenceComments":[{"type":"STRAIN","value":"cv. Hai7124"}],"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE","INTERACTION WITH V.DAHLIAE EPD1","INDUCTION BY V.DAHLIAE EPD1","TISSUE SPECIFICITY","PHOSPHORYLATION AT TYR-165 AND TYR-167","MUTAGENESIS OF TYR-165; TYR-167; SER-172; SER-219; SER-225; SER-291 AND SER-421"]}
```

Source SHA-256: `2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:25:31.043989+00:00.  

```text
ID   EIR5A_GOSBA             Reviewed;         462 AA.
AC   A0A5J5T2N2;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   11-DEC-2019, sequence version 1.
DT   28-JAN-2026, entry version 17.
DE   RecName: Full=EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5A {ECO:0000303|PubMed:39488762};
DE            Short=GbEIR5A {ECO:0000303|PubMed:39488762};
DE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};
GN   Name=EIR5A {ECO:0000303|PubMed:39488762};
GN   ORFNames=ES319_A13G211700v1 {ECO:0000312|EMBL:KAB2049947.1};
OS   Gossypium barbadense (Sea Island cotton) (Hibiscus barbadensis).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   rosids; malvids; Malvales; Malvaceae; Malvoideae; Gossypium.
OX   NCBI_TaxID=3634;
```

Source SHA-256: `a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:25:31.043989+00:00.  

```text
DE   RecName: Full=EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5A {ECO:0000303|PubMed:39488762};
DE            Short=GbEIR5A {ECO:0000303|PubMed:39488762};
DE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)  
**Locator:** `lines 52-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:25:31.043989+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)  
**Locator:** `lines 58-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:25:31.043989+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 177. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
