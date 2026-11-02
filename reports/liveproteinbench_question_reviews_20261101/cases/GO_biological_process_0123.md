# GO_biological_process_0123

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — sterol biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGLSHSGEIVYIHPSSPVDLFTTCASLPTKPPPSFSDMPSPLFLVSGFLGVCVAYAVANIIRQLLFPNAKEPPVVFHWFPWLGSALTYGKDPYKFLFAARAKYGDVFTFVLLGRNVTVHLGVAGNDFVFNGKETHMNAEEIYGPLCNPVFGEGVVYDCPNSKLMEQKKFVKFGLTTDALKAHVRLIEHEVVNYIKSSRDFKGPSGVINVPPVMAQITIFTAAIALQGPEVRSKLTNEFASLYHDLDGGFSPINFVLPHAPFPHNIKRDRAQLKMRKIYEAIIAERRAGKIPPTTDMISHLMQCSYKNGRPIPDSEISNMMITILMAGQHNSSNIASWIMLHLANEPQLCEELYQEQLDQLADEHGNLPELELHTVEKLKLHSSVVKETLRMHNAIHSIMRLVKQPLPVPNTSWTVPPGHAVLASPGVSANSNEYFLNPTKWDPHRWDDRVIEEDDESEMVDYGYGRTSRGTKSAYLPFGGGRHRCIGEKFAYLNLEVITAVMVRNFRFKNVDGRVDVPGTDYSTMFSRPLEPAEICWERR

[Multiple Choices]
A. sterol biosynthetic process
B. epidermal growth factor receptor signaling pathway
C. venom-mediated fibrinolysis
D. mechanosensory behavior
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated as sterol 14-alpha demethylase, an enzyme critical to ergosterol biosynthesis. This supports sterol biosynthetic process (A).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a eukaryotic cytochrome P450, making a biosynthetic enzyme more plausible than the signaling, venom, or behavior choices. But that family-level inference does not identify its substrate or biological pathway.


**Missing item-specific fact**

> Identifying this protein specifically as sterol 14-alpha demethylase (CYP51), rather than another P450, requires protein-specific annotation or experimental knowledge not provided in the question.


**Reason**

> The key is supported by reviewer-only, sequence-matched annotation, but the precise pathway cannot be reliably inferred from general sequence features alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, sterol biosynthesis is supported for this protein; the other options describe unrelated processes.


### Important caveats

- The UniProt function annotation cites PubMed evidence with ECO:0000269, while the GO sterol-biosynthesis annotation is electronically inferred; these are different evidence types.
- Reviewer-only accession and annotation information was absent from the evaluated model input, and the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a eukaryotic cytochrome P450, making a biosynthetic enzyme more plausible than the signaling, venom, or behavior choices. But that family-level inference does not identify its substrate or biological pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this protein specifically as sterol 14-alpha demethylase (CYP51), rather than another P450, requires protein-specific annotation or experimental knowledge not provided in the question.",
    "reason": "The key is supported by reviewer-only, sequence-matched annotation, but the precise pathway cannot be reliably inferred from general sequence features alone."
  },
  "case_id": "GO_biological_process_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as sterol 14-alpha demethylase, an enzyme critical to ergosterol biosynthesis. This supports sterol biosynthetic process (A)."
  },
  "important_caveats": [
    "The UniProt function annotation cites PubMed evidence with ECO:0000269, while the GO sterol-biosynthesis annotation is electronically inferred; these are different evidence types.",
    "Reviewer-only accession and annotation information was absent from the evaluated model input, and the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, sterol biosynthesis is supported for this protein; the other options describe unrelated processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as sterol 14-alpha demethylase, an enzyme critical to ergosterol biosynthesis. This supports sterol biosynthetic process (A).",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a eukaryotic cytochrome P450, making a biosynthetic enzyme more plausible than the signaling, venom, or behavior choices. But that family-level inference does not identify its substrate or biological pathway.",
    "missing_item_specific_fact": "Identifying this protein specifically as sterol 14-alpha demethylase (CYP51), rather than another P450, requires protein-specific annotation or experimental knowledge not provided in the question.",
    "reason": "The key is supported by reviewer-only, sequence-matched annotation, but the precise pathway cannot be reliably inferred from general sequence features alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, sterol biosynthesis is supported for this protein; the other options describe unrelated processes."
  },
  "important_caveats": [
    "The UniProt function annotation cites PubMed evidence with ECO:0000269, while the GO sterol-biosynthesis annotation is electronically inferred; these are different evidence types.",
    "Reviewer-only accession and annotation information was absent from the evaluated model input, and the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt P0DXV0 (540 aa, exact SHA-256 match). The entry is annotated as Sterol 14-alpha demethylase (EC 1.14.14.154), a cytochrome P450 monooxygenase. The FUNCTION comment (ECO:0000269, direct assay from PubMed:33857369) states it 'plays a critical role in the biosynthesis of ergosterol, the major sterol component in fungal membranes.' The PATHWAY annotation reads 'Steroid biosynthesis; sterol biosynthesis' (ECO:0000250 by similarity). GO:0016126 'sterol biosynthetic process' is directly cross-referenced. The expected answer A is well-supported.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region contains a recognizable cytochrome P450 heme-binding motif (FGGGRHRC, consistent with the degenerate FxxGxxxCxG signature), and the overall ~540-aa architecture with an N-terminal hydrophobic membrane-anchor is characteristic of microsomal P450s. Among the four options, only 'sterol biosynthetic process' involves P450 enzymes (CYP51/lanosterol 14α-demethylase is the canonical P450 of the ergosterol/cholesterol pathway). EGFR signaling requires receptor tyrosine kinases; venom-mediated fibrinolysis requires secreted proteases (serine or metalloproteases); mechanosensory behavior requires ion channels or mechanotransduction complexes. None of these protein classes carry a P450 heme-ligating cysteine motif. Thus, identifying the P450 signature and knowing that CYP51 is the P450 of sterol biosynthesis is sufficient to select A over B, C, and D.


**Missing item-specific fact**

> None critical. The specific identity as a self-resistant CYP51 within the lanomycin biosynthesis gene cluster of Pyrenophora dematioidea is an item-specific annotation detail, but it is not needed to distinguish A from B/C/D; general P450→sterol-biosynthesis reasoning suffices.


**Reason**

> A model that recognizes the P450 heme-binding motif and recalls that CYP51 (sterol 14α-demethylase) is the P450 enzyme of the sterol biosynthesis pathway can eliminate B (RTK), C (protease), and D (mechanosensor) on the basis of protein-family incompatibility. This is a concrete, general-biochemistry argument derivable from the sequence and standard knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options map to mutually exclusive protein families (P450, RTK, protease, mechanosensor). The P450 motif in the sequence uniquely points to option A. No other option is biologically plausible for a cytochrome P450.


### Important caveats

- The GO annotation is IEA (Inferred from Electronic Annotation / UniPathway), and the pathway comment is ECO:0000250 (by similarity to Q4WNT5). The direct experimental evidence (ECO:0000269) supports the enzymatic function (sterol 14α-demethylation) but the GO BP assignment is computational transfer.
- This CYP51 is embedded in the lanomycin biosynthetic gene cluster and is a self-resistant variant; one could argue its biological context is 'lanomycin biosynthesis' rather than canonical ergosterol biosynthesis. However, its enzymatic activity is sterol 14α-demethylation, and the GO annotation assigns it to sterol biosynthetic process.
- The heme-binding motif (FGGGRHRC) is somewhat degenerate relative to the textbook FxxGxxxCxG; a model relying solely on exact motif matching might miss it, though the broader P450 architecture is recognizable.
- All UniProt evidence is reviewer-only and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains a recognizable cytochrome P450 heme-binding motif (FGGGRHRC, consistent with the degenerate FxxGxxxCxG signature), and the overall ~540-aa architecture with an N-terminal hydrophobic membrane-anchor is characteristic of microsomal P450s. Among the four options, only 'sterol biosynthetic process' involves P450 enzymes (CYP51/lanosterol 14α-demethylase is the canonical P450 of the ergosterol/cholesterol pathway). EGFR signaling requires receptor tyrosine kinases; venom-mediated fibrinolysis requires secreted proteases (serine or metalloproteases); mechanosensory behavior requires ion channels or mechanotransduction complexes. None of these protein classes carry a P450 heme-ligating cysteine motif. Thus, identifying the P450 signature and knowing that CYP51 is the P450 of sterol biosynthesis is sufficient to select A over B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific identity as a self-resistant CYP51 within the lanomycin biosynthesis gene cluster of Pyrenophora dematioidea is an item-specific annotation detail, but it is not needed to distinguish A from B/C/D; general P450→sterol-biosynthesis reasoning suffices.",
    "reason": "A model that recognizes the P450 heme-binding motif and recalls that CYP51 (sterol 14α-demethylase) is the P450 enzyme of the sterol biosynthesis pathway can eliminate B (RTK), C (protease), and D (mechanosensor) on the basis of protein-family incompatibility. This is a concrete, general-biochemistry argument derivable from the sequence and standard knowledge."
  },
  "case_id": "GO_biological_process_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DXV0 (540 aa, exact SHA-256 match). The entry is annotated as Sterol 14-alpha demethylase (EC 1.14.14.154), a cytochrome P450 monooxygenase. The FUNCTION comment (ECO:0000269, direct assay from PubMed:33857369) states it 'plays a critical role in the biosynthesis of ergosterol, the major sterol component in fungal membranes.' The PATHWAY annotation reads 'Steroid biosynthesis; sterol biosynthesis' (ECO:0000250 by similarity). GO:0016126 'sterol biosynthetic process' is directly cross-referenced. The expected answer A is well-supported."
  },
  "important_caveats": [
    "The GO annotation is IEA (Inferred from Electronic Annotation / UniPathway), and the pathway comment is ECO:0000250 (by similarity to Q4WNT5). The direct experimental evidence (ECO:0000269) supports the enzymatic function (sterol 14α-demethylation) but the GO BP assignment is computational transfer.",
    "This CYP51 is embedded in the lanomycin biosynthetic gene cluster and is a self-resistant variant; one could argue its biological context is 'lanomycin biosynthesis' rather than canonical ergosterol biosynthesis. However, its enzymatic activity is sterol 14α-demethylation, and the GO annotation assigns it to sterol biosynthetic process.",
    "The heme-binding motif (FGGGRHRC) is somewhat degenerate relative to the textbook FxxGxxxCxG; a model relying solely on exact motif matching might miss it, though the broader P450 architecture is recognizable.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options map to mutually exclusive protein families (P450, RTK, protease, mechanosensor). The P450 motif in the sequence uniquely points to option A. No other option is biologically plausible for a cytochrome P450."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DXV0 (540 aa, exact SHA-256 match). The entry is annotated as Sterol 14-alpha demethylase (EC 1.14.14.154), a cytochrome P450 monooxygenase. The FUNCTION comment (ECO:0000269, direct assay from PubMed:33857369) states it 'plays a critical role in the biosynthesis of ergosterol, the major sterol component in fungal membranes.' The PATHWAY annotation reads 'Steroid biosynthesis; sterol biosynthesis' (ECO:0000250 by similarity). GO:0016126 'sterol biosynthetic process' is directly cross-referenced. The expected answer A is well-supported.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region contains a recognizable cytochrome P450 heme-binding motif (FGGGRHRC, consistent with the degenerate FxxGxxxCxG signature), and the overall ~540-aa architecture with an N-terminal hydrophobic membrane-anchor is characteristic of microsomal P450s. Among the four options, only 'sterol biosynthetic process' involves P450 enzymes (CYP51/lanosterol 14α-demethylase is the canonical P450 of the ergosterol/cholesterol pathway). EGFR signaling requires receptor tyrosine kinases; venom-mediated fibrinolysis requires secreted proteases (serine or metalloproteases); mechanosensory behavior requires ion channels or mechanotransduction complexes. None of these protein classes carry a P450 heme-ligating cysteine motif. Thus, identifying the P450 signature and knowing that CYP51 is the P450 of sterol biosynthesis is sufficient to select A over B, C, and D.",
    "missing_item_specific_fact": "None critical. The specific identity as a self-resistant CYP51 within the lanomycin biosynthesis gene cluster of Pyrenophora dematioidea is an item-specific annotation detail, but it is not needed to distinguish A from B/C/D; general P450→sterol-biosynthesis reasoning suffices.",
    "reason": "A model that recognizes the P450 heme-binding motif and recalls that CYP51 (sterol 14α-demethylase) is the P450 enzyme of the sterol biosynthesis pathway can eliminate B (RTK), C (protease), and D (mechanosensor) on the basis of protein-family incompatibility. This is a concrete, general-biochemistry argument derivable from the sequence and standard knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options map to mutually exclusive protein families (P450, RTK, protease, mechanosensor). The P450 motif in the sequence uniquely points to option A. No other option is biologically plausible for a cytochrome P450."
  },
  "important_caveats": [
    "The GO annotation is IEA (Inferred from Electronic Annotation / UniPathway), and the pathway comment is ECO:0000250 (by similarity to Q4WNT5). The direct experimental evidence (ECO:0000269) supports the enzymatic function (sterol 14α-demethylation) but the GO BP assignment is computational transfer.",
    "This CYP51 is embedded in the lanomycin biosynthetic gene cluster and is a self-resistant variant; one could argue its biological context is 'lanomycin biosynthesis' rather than canonical ergosterol biosynthesis. However, its enzymatic activity is sterol 14α-demethylation, and the GO annotation assigns it to sterol biosynthetic process.",
    "The heme-binding motif (FGGGRHRC) is somewhat degenerate relative to the textbook FxxGxxxCxG; a model relying solely on exact motif matching might miss it, though the broader P450 architecture is recognizable.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model."
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

**Accession:** `P0DXV0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
"P0DXV0"
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Ergosterol biosynthesis protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Lanomycin biosynthesis cluster protein 1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"1.14.14.154"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Sterol 14-alpha demethylase"}}}
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"Sterol 14-alpha demethylase; part of the gene cluster that mediates the biosynthesis of tetrahydropyranyl antifungal agent lanomycin that acts as an inhibitor of CYP51 and blocks the ergosterol biosynthesis (PubMed:33857369). Sterol 14-alpha-demethylase plays a critical role in the biosynthesis of ergosterol, the major sterol component in fungal membranes that participates in a variety of functions. Acts as a self-resistant CYP51 that contains mutations found in CYP51s isolated from azole resistance strains and that is not inhibited by the final product of the cluster, lanomycin (PubMed:33857369)"}]}
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)  
**Locator:** `/comments/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"value":"Steroid biosynthesis; sterol biosynthesis"}]}
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
{"database":"GO","id":"GO:0016126","properties":[{"key":"GoTerm","value":"P:sterol biosynthetic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniPathway"}]}
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 26-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

```text
CC   -!- FUNCTION: Sterol 14-alpha demethylase; part of the gene cluster that
CC       mediates the biosynthesis of tetrahydropyranyl antifungal agent
CC       lanomycin that acts as an inhibitor of CYP51 and blocks the ergosterol
CC       biosynthesis (PubMed:33857369). Sterol 14-alpha-demethylase plays a
CC       critical role in the biosynthesis of ergosterol, the major sterol
CC       component in fungal membranes that participates in a variety of
CC       functions. Acts as a self-resistant CYP51 that contains mutations found
CC       in CYP51s isolated from azole resistance strains and that is not
CC       inhibited by the final product of the cluster, lanomycin
CC       (PubMed:33857369). {ECO:0000269|PubMed:33857369}.
```

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 158-159`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

```text
CC   -!- PATHWAY: Steroid biosynthesis; sterol biosynthesis.
CC       {ECO:0000250|UniProtKB:Q4WNT5}.
```

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 174-174`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

```text
DR   GO; GO:0016126; P:sterol biosynthetic process; IEA:UniProtKB-KW.
```

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 123. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
