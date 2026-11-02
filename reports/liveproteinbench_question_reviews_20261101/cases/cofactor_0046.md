# cofactor_0046

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLEILADESVGGNSPTVIINRGAKKMQWPFIGCGGLGFSKTAHFTCFDSMTQLCEEDIPCIHLPPQHRSVYKMSTENKMRAVVFHSPYKVAVEERPIPKIQDSGDIVVKVTYTALCGSDLHTFRGIEPAGTGFVMGHEVTGEVVEVGSGVKSIQKGDMVVSAFTTSCGECFYCKQGFSSRCEKSVLFGCDHLDGAQAEYVRIPNADGTVMKAPEGVEEKYLVLMADIFPTGYFAASNAFKGYTPEQISEQTVVLIGCGPVGLCALINALEFKPKHLLAVDSIPSRLELARSLGAEPWNFQQDREGLDKRVKELTNGRGADAVIEVVGLSPALRTGFDLLRPWGTISSVGVHNGEIPWAGNDAYDKNLRIQMGRCPVRSVSPQALDVLKKNQHKLGFMADKIMPLSQAVEGYELFNAMKVQKVIFKAGE

[Multiple Choices]
A. Zn(2+)
B. Co(2+)
C. Mo-bis(molybdopterin guanine dinucleotide)
D. Cu(2+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact sequence is matched to a zinc-type alcohol dehydrogenase annotation listing Zn(2+), including two Zn(2+) ions per subunit. The cofactor annotation is transferred by similarity from UniProtKB:P11766, so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a zinc-dependent alcohol dehydrogenase: its ADH-like enzyme sequence includes histidine- and cysteine-rich regions compatible with metal-binding sites. That family-level signal meaningfully favors Zn over the listed Mo and Cu options, and over Co.


**Missing item-specific fact**

> No direct experimental measurement of the cofactor for this exact protein is supplied; identifying it confidently would otherwise benefit from a protein-family annotation or biochemical characterization.


**Reason**

> The sequence provides a recognizable family-level basis for favoring Zn, rather than requiring recall of this exact protein's database entry. That inference is not equivalent to direct experimental confirmation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct, and the zinc-dependent alcohol dehydrogenase sequence features favor Zn. The evidence does not establish that another listed metal could never substitute under other conditions.


### Important caveats

- The sequence matches the cited UniProt record, but the cofactor annotation is similarity-transferred from P11766 rather than shown here as experimentally established for this exact protein.
- The historical matched record also lists Zn(2+); the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a zinc-dependent alcohol dehydrogenase: its ADH-like enzyme sequence includes histidine- and cysteine-rich regions compatible with metal-binding sites. That family-level signal meaningfully favors Zn over the listed Mo and Cu options, and over Co.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No direct experimental measurement of the cofactor for this exact protein is supplied; identifying it confidently would otherwise benefit from a protein-family annotation or biochemical characterization.",
    "reason": "The sequence provides a recognizable family-level basis for favoring Zn, rather than requiring recall of this exact protein's database entry. That inference is not equivalent to direct experimental confirmation."
  },
  "case_id": "cofactor_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence is matched to a zinc-type alcohol dehydrogenase annotation listing Zn(2+), including two Zn(2+) ions per subunit. The cofactor annotation is transferred by similarity from UniProtKB:P11766, so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the cofactor annotation is similarity-transferred from P11766 rather than shown here as experimentally established for this exact protein.",
    "The historical matched record also lists Zn(2+); the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct, and the zinc-dependent alcohol dehydrogenase sequence features favor Zn. The evidence does not establish that another listed metal could never substitute under other conditions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence is matched to a zinc-type alcohol dehydrogenase annotation listing Zn(2+), including two Zn(2+) ions per subunit. The cofactor annotation is transferred by similarity from UniProtKB:P11766, so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a zinc-dependent alcohol dehydrogenase: its ADH-like enzyme sequence includes histidine- and cysteine-rich regions compatible with metal-binding sites. That family-level signal meaningfully favors Zn over the listed Mo and Cu options, and over Co.",
    "missing_item_specific_fact": "No direct experimental measurement of the cofactor for this exact protein is supplied; identifying it confidently would otherwise benefit from a protein-family annotation or biochemical characterization.",
    "reason": "The sequence provides a recognizable family-level basis for favoring Zn, rather than requiring recall of this exact protein's database entry. That inference is not equivalent to direct experimental confirmation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct, and the zinc-dependent alcohol dehydrogenase sequence features favor Zn. The evidence does not establish that another listed metal could never substitute under other conditions."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the cofactor annotation is similarity-transferred from P11766 rather than shown here as experimentally established for this exact protein.",
    "The historical matched record also lists Zn(2+); the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7U2MMF3) explicitly annotates the protein as 'Zinc-type alcohol dehydrogenase B' (EC 1.1.1.1) with a COFACTOR comment stating 'Zn(2+); Binds 2 Zn(2+) ions per subunit.' The cofactor evidence code is ECO:0000250 (inferred by similarity to P11766), so the Zn assignment is by annotation transfer rather than direct experimental measurement on this specific protein. However, the protein name itself ('Zinc-type alcohol dehydrogenase') and the EC 1.1.1.1 classification independently and strongly support Zn(2+) as the cofactor, and the PubMed reference (39601562) provides experimental evidence for catalytic function. The sequence match is confirmed (428 aa, SHA256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 428-aa sequence exhibits hallmarks of the long-chain alcohol dehydrogenase (ADH) superfamily: (1) an N-terminal Rossmann-fold-like NAD(P)-binding region (e.g., 'GCGGLGFSKT' containing a GxGxxG-type motif), (2) a catalytic domain with clustered Cys/His residues forming the canonical zinc-binding site (e.g., 'CGSDLHTFRG', 'CGECFYCKQGFSSRCEKSVLFGCDHLDG', 'CGPVGLCALINALEFKPKHLL'), and (3) a two-domain architecture typical of Zn-ADHs. Among the four choices, Zn(2+) is the defining cofactor of EC 1.1.1.1 alcohol dehydrogenases; Mo-bis(MGD) is restricted to molybdoenzymes (nitrate reductases, xanthine oxidases); Co(2+) appears only in rare isomutases; Cu(2+) is found in oxidases (SOD, laccase, tyrosinase) with different structural motifs. The Cys-rich 'CG' cluster pattern is a well-established sequence signature of the Zn-ADH zinc site and is inconsistent with the coordination geometry of the other three cofactors.


**Missing item-specific fact**

> None critical. A model need not know the exact UniProt accession; recognizing the Zn-ADH Cys-cluster signature and the NAD-binding Rossmann fold from the sequence, combined with general knowledge that EC 1.1.1.1 is Zn-dependent, provides a defensible reasoning path to Zn(2+).


**Reason**

> The sequence contains identifiable structural motifs (Rossmann fold, Zn-ADH Cys/His clusters) that allow elimination of Mo-bis(MGD), Co(2+), and Cu(2+) through general biochemical knowledge about cofactor specificity and metal-binding site architecture. This is not pure memorization of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent structurally and mechanistically distinct cofactor classes (Zn in dehydrogenases, Co in isomutases, Cu in oxidases, Mo-bis-MGD in molybdoenzymes). The sequence features and enzyme-family assignment uniquely point to Zn(2+); no other option is biochemically plausible for a long-chain alcohol dehydrogenase.


### Important caveats

- The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to P11766, a yeast ADH), meaning it is a computational/transfer annotation rather than a direct experimental measurement on this Aspergillus flavus protein. The protein name 'Zinc-type alcohol dehydrogenase B' and EC 1.1.1.1 independently corroborate Zn-dependence.
- The UniProt entry was first publicly released on 2025-04-09; the historical Swiss-Prot snapshot (entry version 6, 2026-01-28) confirms the same annotation, so the key was available at the benchmark construction date.
- The cofactor comment is transferred from P11766; the PubMed 39601562 study provides experimental evidence for catalytic activity and function but the specific Zn-binding stoichiometry (2 ions/subunit) is by similarity.
- All reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence features and general biochemical knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 428-aa sequence exhibits hallmarks of the long-chain alcohol dehydrogenase (ADH) superfamily: (1) an N-terminal Rossmann-fold-like NAD(P)-binding region (e.g., 'GCGGLGFSKT' containing a GxGxxG-type motif), (2) a catalytic domain with clustered Cys/His residues forming the canonical zinc-binding site (e.g., 'CGSDLHTFRG', 'CGECFYCKQGFSSRCEKSVLFGCDHLDG', 'CGPVGLCALINALEFKPKHLL'), and (3) a two-domain architecture typical of Zn-ADHs. Among the four choices, Zn(2+) is the defining cofactor of EC 1.1.1.1 alcohol dehydrogenases; Mo-bis(MGD) is restricted to molybdoenzymes (nitrate reductases, xanthine oxidases); Co(2+) appears only in rare isomutases; Cu(2+) is found in oxidases (SOD, laccase, tyrosinase) with different structural motifs. The Cys-rich 'CG' cluster pattern is a well-established sequence signature of the Zn-ADH zinc site and is inconsistent with the coordination geometry of the other three cofactors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. A model need not know the exact UniProt accession; recognizing the Zn-ADH Cys-cluster signature and the NAD-binding Rossmann fold from the sequence, combined with general knowledge that EC 1.1.1.1 is Zn-dependent, provides a defensible reasoning path to Zn(2+).",
    "reason": "The sequence contains identifiable structural motifs (Rossmann fold, Zn-ADH Cys/His clusters) that allow elimination of Mo-bis(MGD), Co(2+), and Cu(2+) through general biochemical knowledge about cofactor specificity and metal-binding site architecture. This is not pure memorization of a database entry."
  },
  "case_id": "cofactor_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7U2MMF3) explicitly annotates the protein as 'Zinc-type alcohol dehydrogenase B' (EC 1.1.1.1) with a COFACTOR comment stating 'Zn(2+); Binds 2 Zn(2+) ions per subunit.' The cofactor evidence code is ECO:0000250 (inferred by similarity to P11766), so the Zn assignment is by annotation transfer rather than direct experimental measurement on this specific protein. However, the protein name itself ('Zinc-type alcohol dehydrogenase') and the EC 1.1.1.1 classification independently and strongly support Zn(2+) as the cofactor, and the PubMed reference (39601562) provides experimental evidence for catalytic function. The sequence match is confirmed (428 aa, SHA256 identical)."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to P11766, a yeast ADH), meaning it is a computational/transfer annotation rather than a direct experimental measurement on this Aspergillus flavus protein. The protein name 'Zinc-type alcohol dehydrogenase B' and EC 1.1.1.1 independently corroborate Zn-dependence.",
    "The UniProt entry was first publicly released on 2025-04-09; the historical Swiss-Prot snapshot (entry version 6, 2026-01-28) confirms the same annotation, so the key was available at the benchmark construction date.",
    "The cofactor comment is transferred from P11766; the PubMed 39601562 study provides experimental evidence for catalytic activity and function but the specific Zn-binding stoichiometry (2 ions/subunit) is by similarity.",
    "All reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence features and general biochemical knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and mechanistically distinct cofactor classes (Zn in dehydrogenases, Co in isomutases, Cu in oxidases, Mo-bis-MGD in molybdoenzymes). The sequence features and enzyme-family assignment uniquely point to Zn(2+); no other option is biochemically plausible for a long-chain alcohol dehydrogenase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7U2MMF3) explicitly annotates the protein as 'Zinc-type alcohol dehydrogenase B' (EC 1.1.1.1) with a COFACTOR comment stating 'Zn(2+); Binds 2 Zn(2+) ions per subunit.' The cofactor evidence code is ECO:0000250 (inferred by similarity to P11766), so the Zn assignment is by annotation transfer rather than direct experimental measurement on this specific protein. However, the protein name itself ('Zinc-type alcohol dehydrogenase') and the EC 1.1.1.1 classification independently and strongly support Zn(2+) as the cofactor, and the PubMed reference (39601562) provides experimental evidence for catalytic function. The sequence match is confirmed (428 aa, SHA256 identical).",
    "evidence_ids": ["C4", "C5", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 428-aa sequence exhibits hallmarks of the long-chain alcohol dehydrogenase (ADH) superfamily: (1) an N-terminal Rossmann-fold-like NAD(P)-binding region (e.g., 'GCGGLGFSKT' containing a GxGxxG-type motif), (2) a catalytic domain with clustered Cys/His residues forming the canonical zinc-binding site (e.g., 'CGSDLHTFRG', 'CGECFYCKQGFSSRCEKSVLFGCDHLDG', 'CGPVGLCALINALEFKPKHLL'), and (3) a two-domain architecture typical of Zn-ADHs. Among the four choices, Zn(2+) is the defining cofactor of EC 1.1.1.1 alcohol dehydrogenases; Mo-bis(MGD) is restricted to molybdoenzymes (nitrate reductases, xanthine oxidases); Co(2+) appears only in rare isomutases; Cu(2+) is found in oxidases (SOD, laccase, tyrosinase) with different structural motifs. The Cys-rich 'CG' cluster pattern is a well-established sequence signature of the Zn-ADH zinc site and is inconsistent with the coordination geometry of the other three cofactors.",
    "missing_item_specific_fact": "None critical. A model need not know the exact UniProt accession; recognizing the Zn-ADH Cys-cluster signature and the NAD-binding Rossmann fold from the sequence, combined with general knowledge that EC 1.1.1.1 is Zn-dependent, provides a defensible reasoning path to Zn(2+).",
    "reason": "The sequence contains identifiable structural motifs (Rossmann fold, Zn-ADH Cys/His clusters) that allow elimination of Mo-bis(MGD), Co(2+), and Cu(2+) through general biochemical knowledge about cofactor specificity and metal-binding site architecture. This is not pure memorization of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and mechanistically distinct cofactor classes (Zn in dehydrogenases, Co in isomutases, Cu in oxidases, Mo-bis-MGD in molybdoenzymes). The sequence features and enzyme-family assignment uniquely point to Zn(2+); no other option is biochemically plausible for a long-chain alcohol dehydrogenase."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to P11766, a yeast ADH), meaning it is a computational/transfer annotation rather than a direct experimental measurement on this Aspergillus flavus protein. The protein name 'Zinc-type alcohol dehydrogenase B' and EC 1.1.1.1 independently corroborate Zn-dependence.",
    "The UniProt entry was first publicly released on 2025-04-09; the historical Swiss-Prot snapshot (entry version 6, 2026-01-28) confirms the same annotation, so the key was available at the benchmark construction date.",
    "The cofactor comment is transferred from P11766; the PubMed 39601562 study provides experimental evidence for catalytic activity and function but the specific Zn-binding stoichiometry (2 ions/subunit) is by similarity.",
    "All reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence features and general biochemical knowledge."
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

**Accession:** `A0A7U2MMF3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 6. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MMF3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.417589+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39601562","source":"PubMed"}],"value":"1.1.1.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39601562","source":"PubMed"}],"value":"Zinc-type alcohol dehydrogenase B"}}}
```

Source SHA-256: `e46822396e66b1f6560085f9592ff59bbb63670635ea2594ff88b97769995e9b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MMF3.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.417589+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P11766","source":"UniProtKB"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P11766","source":"UniProtKB"}],"value":"Binds 2 Zn(2+) ions per subunit."}]}}
```

Source SHA-256: `e46822396e66b1f6560085f9592ff59bbb63670635ea2594ff88b97769995e9b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MMF3?format=txt&versions=6)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-02T04:25:55.240936+00:00.  

```text
DE   RecName: Full=Zinc-type alcohol dehydrogenase B {ECO:0000303|PubMed:39601562};
DE            EC=1.1.1.1 {ECO:0000269|PubMed:39601562};
```

Source SHA-256: `7d4faaa36f941085d4c1a6051f22ec6d1c6e4b6f59555b76c64575e9cff75ee7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MMF3?format=txt&versions=6)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-02T04:25:55.240936+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BENZOYLATION AT LYS-393, MUTAGENESIS OF
RP   LYS-393, AND DISRUPTION PHENOTYPE.
RX   PubMed=39601562; DOI=10.1128/mbio.02665-24;
RA   Chen X., Wu L., Zhang Y., Wang S., Wang S.;
RT   "Importance of benzoyltransferase GcnE and lysine benzoylation of alcohol
RT   dehydrogenase AdhB in pathogenesis and aflatoxin production in Aspergillus
RT   flavus.";
RL   MBio 16:e0266524-e0266524(2025).
```

Source SHA-256: `7d4faaa36f941085d4c1a6051f22ec6d1c6e4b6f59555b76c64575e9cff75ee7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MMF3?format=txt&versions=6)  
**Locator:** `lines 54-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-02T04:25:55.240936+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000250|UniProtKB:P11766};
CC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000250|UniProtKB:P11766};
```

Source SHA-256: `7d4faaa36f941085d4c1a6051f22ec6d1c6e4b6f59555b76c64575e9cff75ee7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 46. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
