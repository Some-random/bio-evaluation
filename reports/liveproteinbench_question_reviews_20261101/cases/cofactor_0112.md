# cofactor_0112

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — heme

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGLSHSGEIVYIHPSSPVDLFTTCASLPTKPPPSFSDMPSPLFLVSGFLGVCVAYAVANIIRQLLFPNAKEPPVVFHWFPWLGSALTYGKDPYKFLFAARAKYGDVFTFVLLGRNVTVHLGVAGNDFVFNGKETHMNAEEIYGPLCNPVFGEGVVYDCPNSKLMEQKKFVKFGLTTDALKAHVRLIEHEVVNYIKSSRDFKGPSGVINVPPVMAQITIFTAAIALQGPEVRSKLTNEFASLYHDLDGGFSPINFVLPHAPFPHNIKRDRAQLKMRKIYEAIIAERRAGKIPPTTDMISHLMQCSYKNGRPIPDSEISNMMITILMAGQHNSSNIASWIMLHLANEPQLCEELYQEQLDQLADEHGNLPELELHTVEKLKLHSSVVKETLRMHNAIHSIMRLVKQPLPVPNTSWTVPPGHAVLASPGVSANSNEYFLNPTKWDPHRWDDRVIEEDDESEMVDYGYGRTSRGTKSAYLPFGGGRHRCIGEKFAYLNLEVITAVMVRNFRFKNVDGRVDVPGTDYSTMFSRPLEPAEICWERR

[Multiple Choices]
A. Mg(2+)
B. heme
C. FMN
D. [2Fe-2S] cluster
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

> The exact-matched UniProt record annotates the protein as a sterol 14-alpha demethylase/cytochrome P450 and lists heme as its cofactor. The cofactor annotation is transferred by similarity (ECO:0000250), so this supports the key but is not direct experimental confirmation for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence includes a C-terminal cysteine-containing motif consistent with the conserved heme-binding region of cytochrome P450 enzymes (including the segment PFGGGRHRCI). P450 enzymes use heme, distinguishing that choice from Mg2+, FMN, and a &#91;2Fe-2S&#93; cluster.


**Missing item-specific fact**

> No protein-specific database annotation is strictly necessary if the P450-family motif is recognized; the direct experimental cofactor measurement for this particular protein is not supplied.


**Reason**

> A recognizable family-level sequence signature and the general P450-heme relationship provide a biological basis to select heme, rather than relying solely on memorizing this protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the P450-like sequence signature, heme is the distinguishable cofactor among the listed options.


### Important caveats

- The supporting UniProt cofactor annotation is similarity-transferred, not evidence of a direct experimental cofactor determination for this exact protein.
- The sequence match and annotation source establish applicability, but do not establish which source snapshot the question author used.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence includes a C-terminal cysteine-containing motif consistent with the conserved heme-binding region of cytochrome P450 enzymes (including the segment PFGGGRHRCI). P450 enzymes use heme, distinguishing that choice from Mg2+, FMN, and a [2Fe-2S] cluster.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific database annotation is strictly necessary if the P450-family motif is recognized; the direct experimental cofactor measurement for this particular protein is not supplied.",
    "reason": "A recognizable family-level sequence signature and the general P450-heme relationship provide a biological basis to select heme, rather than relying solely on memorizing this protein's database entry."
  },
  "case_id": "cofactor_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact-matched UniProt record annotates the protein as a sterol 14-alpha demethylase/cytochrome P450 and lists heme as its cofactor. The cofactor annotation is transferred by similarity (ECO:0000250), so this supports the key but is not direct experimental confirmation for this sequence."
  },
  "important_caveats": [
    "The supporting UniProt cofactor annotation is similarity-transferred, not evidence of a direct experimental cofactor determination for this exact protein.",
    "The sequence match and annotation source establish applicability, but do not establish which source snapshot the question author used."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the P450-like sequence signature, heme is the distinguishable cofactor among the listed options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched UniProt record annotates the protein as a sterol 14-alpha demethylase/cytochrome P450 and lists heme as its cofactor. The cofactor annotation is transferred by similarity (ECO:0000250), so this supports the key but is not direct experimental confirmation for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence includes a C-terminal cysteine-containing motif consistent with the conserved heme-binding region of cytochrome P450 enzymes (including the segment PFGGGRHRCI). P450 enzymes use heme, distinguishing that choice from Mg2+, FMN, and a [2Fe-2S] cluster.",
    "missing_item_specific_fact": "No protein-specific database annotation is strictly necessary if the P450-family motif is recognized; the direct experimental cofactor measurement for this particular protein is not supplied.",
    "reason": "A recognizable family-level sequence signature and the general P450-heme relationship provide a biological basis to select heme, rather than relying solely on memorizing this protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the P450-like sequence signature, heme is the distinguishable cofactor among the listed options."
  },
  "important_caveats": [
    "The supporting UniProt cofactor annotation is similarity-transferred, not evidence of a direct experimental cofactor determination for this exact protein.",
    "The sequence match and annotation source establish applicability, but do not establish which source snapshot the question author used."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXV0 explicitly annotates the cofactor as heme (ChEBI:CHEBI:30413), with evidence code ECO:0000250 (inferred by similarity from Q16850, a characterized CYP51). The protein is named 'Sterol 14-alpha demethylase' (EC 1.14.14.154) and 'Cytochrome P450 monooxygenase.' All cytochrome P450 enzymes use heme as their prosthetic group; this is a fundamental biochemical fact. The transferred evidence is well-justified given the conserved P450 heme-binding motif present in the sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical P450 heme-binding signature motif FxxGxxxCxG near the C-terminus ('FGGGRHRCIG'), where the invariant cysteine coordinates the heme iron. The N-terminal hydrophobic region is consistent with a transmembrane anchor typical of microsomal P450s (e.g., fungal CYP51). The overall length (~540 aa) matches fungal CYP51 enzymes. General biochemistry establishes that all cytochrome P450 monooxygenases require heme as their prosthetic group. The distractors are distinguishable: FMN is the cofactor of the NADPH-cytochrome P450 reductase (the electron-transfer partner, not the P450 itself); &#91;2Fe-2S&#93; clusters are found in adrenodoxin-type partners of mitochondrial P450s; Mg²⁺ is typical of kinases/nucleases, not P450s.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of the P450 superfamily can identify the FxxGxxxCxG motif in the sequence and infer heme as the cofactor from general enzymology. The distractors (FMN, &#91;2Fe-2S&#93;) correspond to P450 partner proteins rather than the P450 itself, providing a meaningful biological distinction. No item-specific database lookup is strictly required beyond recognizing the conserved motif and knowing P450 biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The FxxGxxxCxG motif unambiguously identifies this as a P450, and P450s universally use heme. FMN and &#91;2Fe-2S&#93; are cofactors of electron-transfer partners, not the P450 catalytic domain. Mg²⁺ has no established role in P450 catalysis. No alternative choice is defensible.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000250 (similarity transfer from Q16850), not direct experimental evidence for this specific protein. However, the heme dependence of P450s is a universal biochemical property, making the transfer highly reliable.
- The FxxGxxxCxG motif match is present but the spacing is slightly non-canonical (FGGGRHRCIG vs. ideal FxxGxxxCxG); nonetheless, the conserved Cys and flanking residues are clearly identifiable.
- The protein is a lanomycin biosynthesis cluster protein (ORF1) with CYP51-like sterol demethylase activity; its exact substrate specificity differs from canonical CYP51 but the heme cofactor requirement is unchanged.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding signature motif FxxGxxxCxG near the C-terminus ('FGGGRHRCIG'), where the invariant cysteine coordinates the heme iron. The N-terminal hydrophobic region is consistent with a transmembrane anchor typical of microsomal P450s (e.g., fungal CYP51). The overall length (~540 aa) matches fungal CYP51 enzymes. General biochemistry establishes that all cytochrome P450 monooxygenases require heme as their prosthetic group. The distractors are distinguishable: FMN is the cofactor of the NADPH-cytochrome P450 reductase (the electron-transfer partner, not the P450 itself); [2Fe-2S] clusters are found in adrenodoxin-type partners of mitochondrial P450s; Mg²⁺ is typical of kinases/nucleases, not P450s.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the P450 superfamily can identify the FxxGxxxCxG motif in the sequence and infer heme as the cofactor from general enzymology. The distractors (FMN, [2Fe-2S]) correspond to P450 partner proteins rather than the P450 itself, providing a meaningful biological distinction. No item-specific database lookup is strictly required beyond recognizing the conserved motif and knowing P450 biochemistry."
  },
  "case_id": "cofactor_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXV0 explicitly annotates the cofactor as heme (ChEBI:CHEBI:30413), with evidence code ECO:0000250 (inferred by similarity from Q16850, a characterized CYP51). The protein is named 'Sterol 14-alpha demethylase' (EC 1.14.14.154) and 'Cytochrome P450 monooxygenase.' All cytochrome P450 enzymes use heme as their prosthetic group; this is a fundamental biochemical fact. The transferred evidence is well-justified given the conserved P450 heme-binding motif present in the sequence."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (similarity transfer from Q16850), not direct experimental evidence for this specific protein. However, the heme dependence of P450s is a universal biochemical property, making the transfer highly reliable.",
    "The FxxGxxxCxG motif match is present but the spacing is slightly non-canonical (FGGGRHRCIG vs. ideal FxxGxxxCxG); nonetheless, the conserved Cys and flanking residues are clearly identifiable.",
    "The protein is a lanomycin biosynthesis cluster protein (ORF1) with CYP51-like sterol demethylase activity; its exact substrate specificity differs from canonical CYP51 but the heme cofactor requirement is unchanged."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The FxxGxxxCxG motif unambiguously identifies this as a P450, and P450s universally use heme. FMN and [2Fe-2S] are cofactors of electron-transfer partners, not the P450 catalytic domain. Mg²⁺ has no established role in P450 catalysis. No alternative choice is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXV0 explicitly annotates the cofactor as heme (ChEBI:CHEBI:30413), with evidence code ECO:0000250 (inferred by similarity from Q16850, a characterized CYP51). The protein is named 'Sterol 14-alpha demethylase' (EC 1.14.14.154) and 'Cytochrome P450 monooxygenase.' All cytochrome P450 enzymes use heme as their prosthetic group; this is a fundamental biochemical fact. The transferred evidence is well-justified given the conserved P450 heme-binding motif present in the sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding signature motif FxxGxxxCxG near the C-terminus ('FGGGRHRCIG'), where the invariant cysteine coordinates the heme iron. The N-terminal hydrophobic region is consistent with a transmembrane anchor typical of microsomal P450s (e.g., fungal CYP51). The overall length (~540 aa) matches fungal CYP51 enzymes. General biochemistry establishes that all cytochrome P450 monooxygenases require heme as their prosthetic group. The distractors are distinguishable: FMN is the cofactor of the NADPH-cytochrome P450 reductase (the electron-transfer partner, not the P450 itself); [2Fe-2S] clusters are found in adrenodoxin-type partners of mitochondrial P450s; Mg²⁺ is typical of kinases/nucleases, not P450s.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the P450 superfamily can identify the FxxGxxxCxG motif in the sequence and infer heme as the cofactor from general enzymology. The distractors (FMN, [2Fe-2S]) correspond to P450 partner proteins rather than the P450 itself, providing a meaningful biological distinction. No item-specific database lookup is strictly required beyond recognizing the conserved motif and knowing P450 biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The FxxGxxxCxG motif unambiguously identifies this as a P450, and P450s universally use heme. FMN and [2Fe-2S] are cofactors of electron-transfer partners, not the P450 catalytic domain. Mg²⁺ has no established role in P450 catalysis. No alternative choice is defensible."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (similarity transfer from Q16850), not direct experimental evidence for this specific protein. However, the heme dependence of P450s is a universal biochemical property, making the transfer highly reliable.",
    "The FxxGxxxCxG motif match is present but the spacing is slightly non-canonical (FGGGRHRCIG vs. ideal FxxGxxxCxG); nonetheless, the conserved Cys and flanking residues are clearly identifiable.",
    "The protein is a lanomycin biosynthesis cluster protein (ORF1) with CYP51-like sterol demethylase activity; its exact substrate specificity differs from canonical CYP51 but the heme cofactor requirement is unchanged."
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
**Locator:** `/comments/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:30413"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q16850","source":"UniProtKB"}],"name":"heme"}],"commentType":"COFACTOR"}
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

```text
ID   LAN1_PYRDE              Reviewed;         540 AA.
AC   P0DXV0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Sterol 14-alpha demethylase {ECO:0000303|PubMed:33857369};
DE            EC=1.14.14.154 {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Cytochrome P450 monooxygenase {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Ergosterol biosynthesis protein {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Lanomycin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};
GN   Name=ORF1 {ECO:0000303|PubMed:33857369};
OS   Pyrenophora dematioidea (Helminthosporium dematioideum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Pleosporomycetidae; Pleosporales; Pleosporineae; Pleosporaceae;
OC   Pyrenophora.
OX   NCBI_TaxID=139229;
```

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

```text
DE   RecName: Full=Sterol 14-alpha demethylase {ECO:0000303|PubMed:33857369};
DE            EC=1.14.14.154 {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Cytochrome P450 monooxygenase {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Ergosterol biosynthesis protein {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Lanomycin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};
```

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 155-157`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=heme; Xref=ChEBI:CHEBI:30413;
CC         Evidence={ECO:0000250|UniProtKB:Q16850};
```

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
