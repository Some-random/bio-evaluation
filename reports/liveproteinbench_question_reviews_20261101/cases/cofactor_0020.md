# cofactor_0020

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — heme

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDLLQILLAIAGLLAILLLQKQWRTKTSPGAKAGRKLPPEPAGAWPVIGHLHKLGGPNPIYRNLAEWSDKYGPVMTLKLGMQNAVVVSDREAIKECFTTNDKALADRPPSSIGLHLGFNYAAIGAAPYGPYWRDMRKLVLLEVLSSRRLEMLRNVRISEIGTSIKELYSNIIRSSGGSGPAKVVISHWIEQLTLNYILRTIAGRRFSDDSSKDAQYVKGVINDFMYFAGQFVVSDVIPIPLLRWLDPQGHLKGMKRVAKEVDTMCEAWIQEHVQRRMREKPGPGQEQDFIDVLLNNRDVMRKAQEEIDNHVGKERWVDETDLKHLVYLQAIVKEGLRLYPPGPLGAPHRAIEDCQVGGYFIPKGTQLLVNVWKLHRDPRVWSEPEKFMPERFLTRQAEVDVFGHHFELLPFGSGRRACPGITFAVQVMHLTVARLLQGFDMTTPSNLPVDMTEGPGVTMPKAHPVEVLMMPRLPSALYEP

[Multiple Choices]
A. Zn(2+)
B. Na(+)
C. tungstopterin
D. heme
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

> The supplied sequence exactly matches the UniProt entry annotated as a cytochrome P450, and that entry lists heme as its cofactor. The cofactor annotation is transferred by similarity (ECO:0000250), rather than direct experimental evidence in the cited entry; the P450 identity and conserved heme-binding motif nevertheless support heme.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a characteristic cytochrome P450 heme-binding region, including the conserved cysteine in the segment ...FGSGRRACPGIT.... P450s use this cysteine to coordinate heme, distinguishing heme from the listed alternatives.


**Missing item-specific fact**

> No protein-specific external fact is necessary for a defensible choice; recognizing the conserved P450 heme-binding motif is sufficient.


**Reason**

> The sequence supplies a recognizable family-specific motif with a direct biological link to heme binding, so the choices can be meaningfully distinguished without recalling this protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The conserved P450 heme-binding cysteine supports heme, and none of the other listed choices is comparably supported by the sequence.


### Important caveats

- The reviewer-only database cofactor annotation is similarity-transferred, not independent direct experimental confirmation for this exact sequence.
- The reviewer-only sequence comparison confirms an exact match to the cited entry, but that identity and annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a characteristic cytochrome P450 heme-binding region, including the conserved cysteine in the segment ...FGSGRRACPGIT.... P450s use this cysteine to coordinate heme, distinguishing heme from the listed alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific external fact is necessary for a defensible choice; recognizing the conserved P450 heme-binding motif is sufficient.",
    "reason": "The sequence supplies a recognizable family-specific motif with a direct biological link to heme binding, so the choices can be meaningfully distinguished without recalling this protein's database annotation."
  },
  "case_id": "cofactor_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as a cytochrome P450, and that entry lists heme as its cofactor. The cofactor annotation is transferred by similarity (ECO:0000250), rather than direct experimental evidence in the cited entry; the P450 identity and conserved heme-binding motif nevertheless support heme."
  },
  "important_caveats": [
    "The reviewer-only database cofactor annotation is similarity-transferred, not independent direct experimental confirmation for this exact sequence.",
    "The reviewer-only sequence comparison confirms an exact match to the cited entry, but that identity and annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved P450 heme-binding cysteine supports heme, and none of the other listed choices is comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as a cytochrome P450, and that entry lists heme as its cofactor. The cofactor annotation is transferred by similarity (ECO:0000250), rather than direct experimental evidence in the cited entry; the P450 identity and conserved heme-binding motif nevertheless support heme.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a characteristic cytochrome P450 heme-binding region, including the conserved cysteine in the segment ...FGSGRRACPGIT.... P450s use this cysteine to coordinate heme, distinguishing heme from the listed alternatives.",
    "missing_item_specific_fact": "No protein-specific external fact is necessary for a defensible choice; recognizing the conserved P450 heme-binding motif is sufficient.",
    "reason": "The sequence supplies a recognizable family-specific motif with a direct biological link to heme binding, so the choices can be meaningfully distinguished without recalling this protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved P450 heme-binding cysteine supports heme, and none of the other listed choices is comparably supported by the sequence."
  },
  "important_caveats": [
    "The reviewer-only database cofactor annotation is similarity-transferred, not independent direct experimental confirmation for this exact sequence.",
    "The reviewer-only sequence comparison confirms an exact match to the cited entry, but that identity and annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is annotated as Vinorine hydroxylase / Cytochrome P450 5437 (EC 1.14.14.104) from Rauvolfia serpentina. UniProt explicitly lists heme (CHEBI:30413) as the cofactor (evidence ECO:0000250, transferred from P04798). Although the cofactor annotation itself is by similarity, the protein's identity as a cytochrome P450 is experimentally confirmed (ECO:0000269 from PubMed 28654178 and 38212296). All cytochrome P450 enzymes universally require heme as the iron-protoporphyrin cofactor; this is textbook biochemistry. The FxxGxxxCxG heme-binding motif (FGSGRRACPG) is clearly present in the sequence. The answer is strongly supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif FxxGxxxCxG, specifically 'FGSGRRACPG' (F-G-S-G-R-R-A-C-P-G), where the invariant Cys is the axial ligand to the heme iron. This motif is the single most diagnostic feature of the P450 superfamily and is taught in standard biochemistry. Additionally, the N-terminal hydrophobic stretch (MDLLQILLAIAGLLAILLLQ) is consistent with a microsomal P450 membrane anchor. Recognizing the FxxGxxxCxG motif and knowing that all P450s require heme allows a model to select 'heme' without memorizing this specific UniProt entry. The distractors (Zn2+, Na+, tungstopterin) are cofactors for entirely unrelated enzyme classes (metallohydrolases, ion channels, tungsten-dependent oxidoreductases) and are clearly incompatible with a P450 fold.


**Missing item-specific fact**

> None required. The FxxGxxxCxG motif is directly observable in the supplied sequence, and the universal heme requirement of P450s is general biochemical knowledge.


**Reason**

> A knowledgeable reader can scan the 480-residue sequence, identify the FxxGxxxCxG heme-ligating motif, recognize the protein as a cytochrome P450, and conclude heme is the cofactor. This is a concrete structural-motif-based argument, not database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The FxxGxxxCxG motif unambiguously identifies a P450. Zn2+ is associated with metalloproteases/dehydrogenases, Na+ with ion channels/transporters, and tungstopterin with tungsten-containing enzymes (e.g., aldehyde oxidoreductases in anaerobic prokaryotes). None of these are compatible with a P450 fold. Only heme is defensible.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000250 (similarity-based transfer from P04798), not direct experimental measurement of heme binding for this specific protein. However, the P450 identity is experimentally confirmed, and heme dependence is universal for the superfamily.
- The reviewer-only evidence confirms sequence match (480 aa, SHA-256 identical) between the benchmark input and UniProt A0A218NGS0.
- The historical entry (v26, Swiss-Prot) and current entry (v27) both carry the same heme cofactor annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif FxxGxxxCxG, specifically 'FGSGRRACPG' (F-G-S-G-R-R-A-C-P-G), where the invariant Cys is the axial ligand to the heme iron. This motif is the single most diagnostic feature of the P450 superfamily and is taught in standard biochemistry. Additionally, the N-terminal hydrophobic stretch (MDLLQILLAIAGLLAILLLQ) is consistent with a microsomal P450 membrane anchor. Recognizing the FxxGxxxCxG motif and knowing that all P450s require heme allows a model to select 'heme' without memorizing this specific UniProt entry. The distractors (Zn2+, Na+, tungstopterin) are cofactors for entirely unrelated enzyme classes (metallohydrolases, ion channels, tungsten-dependent oxidoreductases) and are clearly incompatible with a P450 fold.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The FxxGxxxCxG motif is directly observable in the supplied sequence, and the universal heme requirement of P450s is general biochemical knowledge.",
    "reason": "A knowledgeable reader can scan the 480-residue sequence, identify the FxxGxxxCxG heme-ligating motif, recognize the protein as a cytochrome P450, and conclude heme is the cofactor. This is a concrete structural-motif-based argument, not database lookup."
  },
  "case_id": "cofactor_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The protein is annotated as Vinorine hydroxylase / Cytochrome P450 5437 (EC 1.14.14.104) from Rauvolfia serpentina. UniProt explicitly lists heme (CHEBI:30413) as the cofactor (evidence ECO:0000250, transferred from P04798). Although the cofactor annotation itself is by similarity, the protein's identity as a cytochrome P450 is experimentally confirmed (ECO:0000269 from PubMed 28654178 and 38212296). All cytochrome P450 enzymes universally require heme as the iron-protoporphyrin cofactor; this is textbook biochemistry. The FxxGxxxCxG heme-binding motif (FGSGRRACPG) is clearly present in the sequence. The answer is strongly supported."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (similarity-based transfer from P04798), not direct experimental measurement of heme binding for this specific protein. However, the P450 identity is experimentally confirmed, and heme dependence is universal for the superfamily.",
    "The reviewer-only evidence confirms sequence match (480 aa, SHA-256 identical) between the benchmark input and UniProt A0A218NGS0.",
    "The historical entry (v26, Swiss-Prot) and current entry (v27) both carry the same heme cofactor annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The FxxGxxxCxG motif unambiguously identifies a P450. Zn2+ is associated with metalloproteases/dehydrogenases, Na+ with ion channels/transporters, and tungstopterin with tungsten-containing enzymes (e.g., aldehyde oxidoreductases in anaerobic prokaryotes). None of these are compatible with a P450 fold. Only heme is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is annotated as Vinorine hydroxylase / Cytochrome P450 5437 (EC 1.14.14.104) from Rauvolfia serpentina. UniProt explicitly lists heme (CHEBI:30413) as the cofactor (evidence ECO:0000250, transferred from P04798). Although the cofactor annotation itself is by similarity, the protein's identity as a cytochrome P450 is experimentally confirmed (ECO:0000269 from PubMed 28654178 and 38212296). All cytochrome P450 enzymes universally require heme as the iron-protoporphyrin cofactor; this is textbook biochemistry. The FxxGxxxCxG heme-binding motif (FGSGRRACPG) is clearly present in the sequence. The answer is strongly supported.",
    "evidence_ids": ["C4", "C5", "H5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif FxxGxxxCxG, specifically 'FGSGRRACPG' (F-G-S-G-R-R-A-C-P-G), where the invariant Cys is the axial ligand to the heme iron. This motif is the single most diagnostic feature of the P450 superfamily and is taught in standard biochemistry. Additionally, the N-terminal hydrophobic stretch (MDLLQILLAIAGLLAILLLQ) is consistent with a microsomal P450 membrane anchor. Recognizing the FxxGxxxCxG motif and knowing that all P450s require heme allows a model to select 'heme' without memorizing this specific UniProt entry. The distractors (Zn2+, Na+, tungstopterin) are cofactors for entirely unrelated enzyme classes (metallohydrolases, ion channels, tungsten-dependent oxidoreductases) and are clearly incompatible with a P450 fold.",
    "missing_item_specific_fact": "None required. The FxxGxxxCxG motif is directly observable in the supplied sequence, and the universal heme requirement of P450s is general biochemical knowledge.",
    "reason": "A knowledgeable reader can scan the 480-residue sequence, identify the FxxGxxxCxG heme-ligating motif, recognize the protein as a cytochrome P450, and conclude heme is the cofactor. This is a concrete structural-motif-based argument, not database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The FxxGxxxCxG motif unambiguously identifies a P450. Zn2+ is associated with metalloproteases/dehydrogenases, Na+ with ion channels/transporters, and tungstopterin with tungsten-containing enzymes (e.g., aldehyde oxidoreductases in anaerobic prokaryotes). None of these are compatible with a P450 fold. Only heme is defensible."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (similarity-based transfer from P04798), not direct experimental measurement of heme binding for this specific protein. However, the P450 identity is experimentally confirmed, and heme dependence is universal for the superfamily.",
    "The reviewer-only evidence confirms sequence match (480 aa, SHA-256 identical) between the benchmark input and UniProt A0A218NGS0.",
    "The historical entry (v26, Swiss-Prot) and current entry (v27) both carry the same heme cofactor annotation."
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

**Accession:** `A0A218NGS0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
"A0A218NGS0"
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"ASG81458.1","source":"EMBL"}],"value":"Cytochrome P450 5437"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"ASG81458.1","source":"EMBL"}],"value":"RsCYP5437"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"}],"value":"Cytochrome P450 82S18"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"}],"value":"Perakine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"}],"value":"Vomilenine isomerase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28654178","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.14.14.104"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Vinorine hydroxylase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsVH"}]}}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:30413"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P04798","source":"UniProtKB"}],"name":"heme"}],"commentType":"COFACTOR"}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 6-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
DE   RecName: Full=Vinorine hydroxylase {ECO:0000303|PubMed:28654178, ECO:0000303|PubMed:38212296};
DE            Short=RsVH {ECO:0000303|PubMed:38212296};
DE            EC=1.14.14.104 {ECO:0000269|PubMed:28654178, ECO:0000269|PubMed:38212296};
DE   AltName: Full=Cytochrome P450 5437 {ECO:0000312|EMBL:ASG81458.1};
DE            Short=RsCYP5437 {ECO:0000312|EMBL:ASG81458.1};
DE   AltName: Full=Cytochrome P450 82S18 {ECO:0000303|PubMed:28654178};
DE   AltName: Full=Perakine synthase {ECO:0000303|PubMed:28654178};
DE            Short=Vomilenine isomerase {ECO:0000303|PubMed:28654178};
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 62-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=heme; Xref=ChEBI:CHEBI:30413;
CC         Evidence={ECO:0000250|UniProtKB:P04798};
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
