# active_site_0032

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 215 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVMKFTWRSIIPRCSKGIEEPEAEAEAEPETKKQDSKQGSFSRLAMIDLSYPSSRFTEDLSTSLAGSNLYVFTLEELKVITQCFSSANFLGEGGFGPVHKGFIDDNLRPGLEAQPVAVKLLDLEGLQGHREWLTEVVFLAQLSHPHLVKLIGYCCEDEHRLLVYEYMPRGSLENQLFAKYSVPLPWSTRMKIALGAAKGLAYLHEAEKPVIYRDFKASNILLDSDYSAKLSDFGLAKDGPEGDKTHVSTRVMGTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRSLDKSRSPREQNLAEWARPMLNESRRLARIMDPKLEGQYSETGARKAAALAYQCLSHRAKQRPKMSDVVNILEPLLDYEETSVGTFVYTVPTHQNGGSPPKDDTDTKECEAKTELKKENGDHHNRHHHRRSHKSRDGHRHRNKSSSQSSVHSENYTSKQTLENGSNEECNID

[Multiple Choices]
A. Position 124 (Charge relay)
B. Position 277 (Nucleophile)
C. Position 215 (Proton acceptor)
D. Position 206 (For beta-ketoacyl synthase 1 activity)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

### Expected-answer support: contradicted

> The matched UniProt record annotates position 215 as a proton acceptor, but this sequence has Arg at position 215 and Asp at 216. For a protein kinase, the catalytic proton-accepting role is associated with the conserved Asp, so the annotation does not support the stated position as a scientifically reliable assignment. The annotation is rule-based, not experimental validation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a protein kinase, but kinase-family knowledge points to a catalytic Asp; here the Asp is at 216, not the keyed position 215. That does not provide a sound biological argument for choosing C as written.


**Missing item-specific fact**

> The specific UniProt/PROSITE active-site annotation assigning a proton-acceptor role to position 215 is absent from the question input.


**Reason**

> Identifying the kinase family is possible from the sequence, but it does not justify the keyed residue and position. Selection of C depends on an item-specific annotation, which itself conflicts with the sequence residue at that coordinate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No listed option is supported by the sequence as a correctly positioned catalytic residue: the annotated proton-accepting Asp-like residue is at 216, while option C specifies 215.


### Important caveats

- The matched UniProt record and its archived version both contain the position-215 annotation, but cite PROSITE rules rather than experimental evidence.
- The precise author source snapshot is unknown; the archived annotation establishes that the database assignment existed by the historical cutoff, not that it was experimentally validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a protein kinase, but kinase-family knowledge points to a catalytic Asp; here the Asp is at 216, not the keyed position 215. That does not provide a sound biological argument for choosing C as written.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt/PROSITE active-site annotation assigning a proton-acceptor role to position 215 is absent from the question input.",
    "reason": "Identifying the kinase family is possible from the sequence, but it does not justify the keyed residue and position. Selection of C depends on an item-specific annotation, which itself conflicts with the sequence residue at that coordinate."
  },
  "case_id": "active_site_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "contradicted",
    "reason": "The matched UniProt record annotates position 215 as a proton acceptor, but this sequence has Arg at position 215 and Asp at 216. For a protein kinase, the catalytic proton-accepting role is associated with the conserved Asp, so the annotation does not support the stated position as a scientifically reliable assignment. The annotation is rule-based, not experimental validation."
  },
  "important_caveats": [
    "The matched UniProt record and its archived version both contain the position-215 annotation, but cite PROSITE rules rather than experimental evidence.",
    "The precise author source snapshot is unknown; the archived annotation establishes that the database assignment existed by the historical cutoff, not that it was experimentally validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No listed option is supported by the sequence as a correctly positioned catalytic residue: the annotated proton-accepting Asp-like residue is at 216, while option C specifies 215."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0032",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The matched UniProt record annotates position 215 as a proton acceptor, but this sequence has Arg at position 215 and Asp at 216. For a protein kinase, the catalytic proton-accepting role is associated with the conserved Asp, so the annotation does not support the stated position as a scientifically reliable assignment. The annotation is rule-based, not experimental validation.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a protein kinase, but kinase-family knowledge points to a catalytic Asp; here the Asp is at 216, not the keyed position 215. That does not provide a sound biological argument for choosing C as written.",
    "missing_item_specific_fact": "The specific UniProt/PROSITE active-site annotation assigning a proton-acceptor role to position 215 is absent from the question input.",
    "reason": "Identifying the kinase family is possible from the sequence, but it does not justify the keyed residue and position. Selection of C depends on an item-specific annotation, which itself conflicts with the sequence residue at that coordinate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No listed option is supported by the sequence as a correctly positioned catalytic residue: the annotated proton-accepting Asp-like residue is at 216, while option C specifies 215."
  },
  "important_caveats": [
    "The matched UniProt record and its archived version both contain the position-215 annotation, but cite PROSITE rules rather than experimental evidence.",
    "The precise author source snapshot is unknown; the archived annotation establishes that the database assignment existed by the historical cutoff, not that it was experimentally validated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A5J5T2N2 (GbEIR5A, a serine/threonine protein kinase, EC 2.7.11.1) annotates position 215 as 'Active site' with description 'Proton acceptor' (evidence C5/H3). The residue at position 215 in the supplied sequence is D (Aspartate), consistent with the catalytic aspartate in the kinase catalytic loop (here YRD at positions 213-215). The annotation derives from PROSITE-ProRule (ECO:0000255), i.e., computational/profiling-based rather than direct experimental measurement, but it is consistent with well-established protein kinase biochemistry where the HRD/YRD aspartate acts as the catalytic base accepting a proton from the substrate hydroxyl during phosphotransfer.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable protein kinase motifs: a glycine-rich P-loop (GEGGFGP, ~positions 92-98), a catalytic loop with YRD at positions 213-215 (variant of the canonical HRD motif), and a DFG motif at positions 233-235. General knowledge of protein kinase catalysis establishes that the aspartate in the HRD/YRD catalytic loop serves as the proton acceptor (catalytic base) that deprotonates the substrate hydroxyl during phosphoryl transfer. Distractor D (beta-ketoacyl synthase) refers to an entirely different enzyme class. Distractor A invokes 'charge relay,' a serine-protease concept, and position 124 is Leucine. Distractor B labels a nucleophile, but in kinases the nucleophile is the substrate's -OH, not a kinase residue; position 277 is Serine in the APE region, not a catalytic nucleophile. These eliminations plus the catalytic-loop identification make C the uniquely defensible answer.


**Missing item-specific fact**

> None critical. Exact residue-numbering requires counting, but the motif architecture (G-rich loop → catalytic loop → DFG) provides positional anchors. The YRD variant of HRD is slightly non-canonical but still identifiable as the catalytic loop.


**Reason**

> A model with general knowledge of protein kinase catalytic mechanisms can identify the kinase fold from sequence motifs, locate the catalytic-loop aspartate, and apply the established principle that this Asp is the proton acceptor. The distractors are eliminable through enzyme-class and mechanism reasoning without needing to recall a specific UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are each wrong for distinct, non-overlapping reasons (wrong enzyme class, wrong mechanism terminology, wrong residue identity), leaving C as the only biochemically coherent answer for a serine/threonine protein kinase.


### Important caveats

- The position-215 annotation is computational (PROSITE-ProRule ECO:0000255), not derived from direct experimental measurement such as mutagenesis of the catalytic Asp. The PubMed reference (39488762) reports mutagenesis of Ser residues and Tyr-165/167 but does not specifically validate the catalytic Asp at 215.
- The catalytic loop motif here is YRD rather than the canonical HRD; while the aspartate role is conserved, the non-canonical first residue could marginally increase identification difficulty.
- The UniProt entry is Swiss-Prot (reviewed) but the active-site feature itself carries only PROSITE-ProRule evidence, so it is a profile-transfer annotation rather than a curated experimental assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable protein kinase motifs: a glycine-rich P-loop (GEGGFGP, ~positions 92-98), a catalytic loop with YRD at positions 213-215 (variant of the canonical HRD motif), and a DFG motif at positions 233-235. General knowledge of protein kinase catalysis establishes that the aspartate in the HRD/YRD catalytic loop serves as the proton acceptor (catalytic base) that deprotonates the substrate hydroxyl during phosphoryl transfer. Distractor D (beta-ketoacyl synthase) refers to an entirely different enzyme class. Distractor A invokes 'charge relay,' a serine-protease concept, and position 124 is Leucine. Distractor B labels a nucleophile, but in kinases the nucleophile is the substrate's -OH, not a kinase residue; position 277 is Serine in the APE region, not a catalytic nucleophile. These eliminations plus the catalytic-loop identification make C the uniquely defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Exact residue-numbering requires counting, but the motif architecture (G-rich loop → catalytic loop → DFG) provides positional anchors. The YRD variant of HRD is slightly non-canonical but still identifiable as the catalytic loop.",
    "reason": "A model with general knowledge of protein kinase catalytic mechanisms can identify the kinase fold from sequence motifs, locate the catalytic-loop aspartate, and apply the established principle that this Asp is the proton acceptor. The distractors are eliminable through enzyme-class and mechanism reasoning without needing to recall a specific UniProt annotation."
  },
  "case_id": "active_site_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A5J5T2N2 (GbEIR5A, a serine/threonine protein kinase, EC 2.7.11.1) annotates position 215 as 'Active site' with description 'Proton acceptor' (evidence C5/H3). The residue at position 215 in the supplied sequence is D (Aspartate), consistent with the catalytic aspartate in the kinase catalytic loop (here YRD at positions 213-215). The annotation derives from PROSITE-ProRule (ECO:0000255), i.e., computational/profiling-based rather than direct experimental measurement, but it is consistent with well-established protein kinase biochemistry where the HRD/YRD aspartate acts as the catalytic base accepting a proton from the substrate hydroxyl during phosphotransfer."
  },
  "important_caveats": [
    "The position-215 annotation is computational (PROSITE-ProRule ECO:0000255), not derived from direct experimental measurement such as mutagenesis of the catalytic Asp. The PubMed reference (39488762) reports mutagenesis of Ser residues and Tyr-165/167 but does not specifically validate the catalytic Asp at 215.",
    "The catalytic loop motif here is YRD rather than the canonical HRD; while the aspartate role is conserved, the non-canonical first residue could marginally increase identification difficulty.",
    "The UniProt entry is Swiss-Prot (reviewed) but the active-site feature itself carries only PROSITE-ProRule evidence, so it is a profile-transfer annotation rather than a curated experimental assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are each wrong for distinct, non-overlapping reasons (wrong enzyme class, wrong mechanism terminology, wrong residue identity), leaving C as the only biochemically coherent answer for a serine/threonine protein kinase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A5J5T2N2 (GbEIR5A, a serine/threonine protein kinase, EC 2.7.11.1) annotates position 215 as 'Active site' with description 'Proton acceptor' (evidence C5/H3). The residue at position 215 in the supplied sequence is D (Aspartate), consistent with the catalytic aspartate in the kinase catalytic loop (here YRD at positions 213-215). The annotation derives from PROSITE-ProRule (ECO:0000255), i.e., computational/profiling-based rather than direct experimental measurement, but it is consistent with well-established protein kinase biochemistry where the HRD/YRD aspartate acts as the catalytic base accepting a proton from the substrate hydroxyl during phosphotransfer.",
    "evidence_ids": ["C5", "H3", "C4", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable protein kinase motifs: a glycine-rich P-loop (GEGGFGP, ~positions 92-98), a catalytic loop with YRD at positions 213-215 (variant of the canonical HRD motif), and a DFG motif at positions 233-235. General knowledge of protein kinase catalysis establishes that the aspartate in the HRD/YRD catalytic loop serves as the proton acceptor (catalytic base) that deprotonates the substrate hydroxyl during phosphoryl transfer. Distractor D (beta-ketoacyl synthase) refers to an entirely different enzyme class. Distractor A invokes 'charge relay,' a serine-protease concept, and position 124 is Leucine. Distractor B labels a nucleophile, but in kinases the nucleophile is the substrate's -OH, not a kinase residue; position 277 is Serine in the APE region, not a catalytic nucleophile. These eliminations plus the catalytic-loop identification make C the uniquely defensible answer.",
    "missing_item_specific_fact": "None critical. Exact residue-numbering requires counting, but the motif architecture (G-rich loop → catalytic loop → DFG) provides positional anchors. The YRD variant of HRD is slightly non-canonical but still identifiable as the catalytic loop.",
    "reason": "A model with general knowledge of protein kinase catalytic mechanisms can identify the kinase fold from sequence motifs, locate the catalytic-loop aspartate, and apply the established principle that this Asp is the proton acceptor. The distractors are eliminable through enzyme-class and mechanism reasoning without needing to recall a specific UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are each wrong for distinct, non-overlapping reasons (wrong enzyme class, wrong mechanism terminology, wrong residue identity), leaving C as the only biochemically coherent answer for a serine/threonine protein kinase."
  },
  "important_caveats": [
    "The position-215 annotation is computational (PROSITE-ProRule ECO:0000255), not derived from direct experimental measurement such as mutagenesis of the catalytic Asp. The PubMed reference (39488762) reports mutagenesis of Ser residues and Tyr-165/167 but does not specifically validate the catalytic Asp at 215.",
    "The catalytic loop motif here is YRD rather than the canonical HRD; while the aspartate role is conserved, the non-canonical first residue could marginally increase identification difficulty.",
    "The UniProt entry is Swiss-Prot (reviewed) but the active-site feature itself carries only PROSITE-ProRule evidence, so it is a profile-transfer annotation rather than a curated experimental assignment."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `model_residue_identity_error`.

> The original frozen sequence uses1-based D215 and F216, not R215 and D216. C5/H3 annotate215 as proton acceptor. The model contradiction argument relies on an incorrect residue read.

**Remaining uncertainty:** This invalidates that stated argument only; source annotation is rule-based and does not become experimental proof or a new final key verdict.

**Direct check of the original sequence:**

```json
{
  "indexing": "1-based",
  "length": 462,
  "residues": {
    "215": "D",
    "216": "F"
  },
  "sha256": "42162c00b0c88b29ae0a2c6b6adef777a99920387ab33bc301c1b0921d93ed86"
}
```

Evidence checked: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A5J5T2N2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 17. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.786512+00:00.  

```json
"A0A5J5T2N2"
```

Source SHA-256: `2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6`.

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
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.786512+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"},{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":215},"start":{"modifier":"EXACT","value":215}},"type":"Active site"}
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)  
**Locator:** `lines 142-145`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:25:31.043989+00:00.  

```text
FT   ACT_SITE        215
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00159,
FT                   ECO:0000255|PROSITE-ProRule:PRU10027"
```

Source SHA-256: `a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
