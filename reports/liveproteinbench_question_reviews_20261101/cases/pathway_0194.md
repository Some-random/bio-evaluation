# pathway_0194

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATSSIRSRALGLSRRARFETTRLPFIGRRYKSDETLNRISSKITQPKSQGASQAMLYATGLTEEDMSKAQVGISSVWFEGNPCNMHLNDLSGIVRDSVLRAGLVPMRFNSVGVSDGISMGTAGMRYSLQSRELIADGIETVMNAQWYDANISLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDETERFDIIRNACPGKGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKNMLREEIKPRDVMTRQAFENAMIVVNVLGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYSIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIQPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEKVVDLDVPTEELDARRKQWKAPPLRYQKGTLKKYCALVSDASHGCVTDGPI

[Multiple Choices]
A. Glycolipid biosynthesis
B. Amino-acid biosynthesis
C. L-threonine from L-aspartate: step 4/5. .
D. Secondary metabolite biosynthesis. .
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

> The matched sequence is annotated as dihydroxy-acid dehydratase, with pathway annotations for isoleucine and valine biosynthesis. Those annotations are transferred by similarity (ECO:0000250), so they support amino-acid biosynthesis but are not direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme, but the input provides no organism, gene identity, or pathway annotation that establishes which pathway role applies.


**Missing item-specific fact**

> The protein-specific identification as mitochondrial dihydroxy-acid dehydratase and its annotated roles in amino-acid biosynthesis and an aspterric-acid biosynthesis cluster.


**Reason**

> Distinguishing the broad pathway choices requires protein-specific functional or annotation information absent from the sequence-and-choices prompt; generic sequence reasoning does not establish the pathway role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B is supported by the isoleucine and valine pathway annotations. D is also defensible because the protein is identified as an aspterric-acid biosynthesis cluster protein, although the supplied evidence does not establish which role is primary.


### Important caveats

- The source sequence matches exactly, but the available pathway annotations for amino-acid biosynthesis are similarity-transferred.
- The precise evidence for a secondary-metabolite role here is the cited cluster-protein designation; it does not independently establish relative pathway importance.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but the input provides no organism, gene identity, or pathway annotation that establishes which pathway role applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as mitochondrial dihydroxy-acid dehydratase and its annotated roles in amino-acid biosynthesis and an aspterric-acid biosynthesis cluster.",
    "reason": "Distinguishing the broad pathway choices requires protein-specific functional or annotation information absent from the sequence-and-choices prompt; generic sequence reasoning does not establish the pathway role."
  },
  "case_id": "pathway_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as dihydroxy-acid dehydratase, with pathway annotations for isoleucine and valine biosynthesis. Those annotations are transferred by similarity (ECO:0000250), so they support amino-acid biosynthesis but are not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The source sequence matches exactly, but the available pathway annotations for amino-acid biosynthesis are similarity-transferred.",
    "The precise evidence for a secondary-metabolite role here is the cited cluster-protein designation; it does not independently establish relative pathway importance."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B is supported by the isoleucine and valine pathway annotations. D is also defensible because the protein is identified as an aspterric-acid biosynthesis cluster protein, although the supplied evidence does not establish which role is primary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as dihydroxy-acid dehydratase, with pathway annotations for isoleucine and valine biosynthesis. Those annotations are transferred by similarity (ECO:0000250), so they support amino-acid biosynthesis but are not direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but the input provides no organism, gene identity, or pathway annotation that establishes which pathway role applies.",
    "missing_item_specific_fact": "The protein-specific identification as mitochondrial dihydroxy-acid dehydratase and its annotated roles in amino-acid biosynthesis and an aspterric-acid biosynthesis cluster.",
    "reason": "Distinguishing the broad pathway choices requires protein-specific functional or annotation information absent from the sequence-and-choices prompt; generic sequence reasoning does not establish the pathway role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B is supported by the isoleucine and valine pathway annotations. D is also defensible because the protein is identified as an aspterric-acid biosynthesis cluster protein, although the supplied evidence does not establish which role is primary."
  },
  "important_caveats": [
    "The source sequence matches exactly, but the available pathway annotations for amino-acid biosynthesis are similarity-transferred.",
    "The precise evidence for a secondary-metabolite role here is the cited cluster-protein designation; it does not independently establish relative pathway importance."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence contains hallmark dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) motifs, including the Fe-S cluster-binding 'GAGLGQDVALLTDGRFSGG' and the 'ACPGKGACGG' signature. UniProt entry A0A0F7TWW9 (PBRD_PENBI) annotates the pathway as 'Amino-acid biosynthesis; L-isoleucine biosynthesis' and 'Amino-acid biosynthesis; L-valine biosynthesis' (evidence ECO:0000250, similarity-based). The recommended name is 'Dihydroxy-acid dehydratase pbrD, mitochondrial' with EC 4.2.1.9 (ECO:0000305, PubMed:39511739). Choice B ('Amino-acid biosynthesis') matches the UniProt pathway annotation. The alternative name 'Aspterric acid biosynthesis cluster protein D' links the protein to a secondary-metabolite gene cluster, but the enzymatic function and pathway assignment remain amino-acid biosynthesis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays canonical DHAD/IlvD domain signatures: the Fe-S cluster-binding motif 'GAGLGQDVALLTDGRFSGG' (residues ~470-490), the 'ACPGKGACGG' loop, and the overall ~250-residue catalytic fold. DHAD catalyzes the dehydration of 2,3-dihydroxy-isovalerate → 2-keto-isovalerate (valine pathway) and 2,3-dihydroxy-3-methylvalerate → 2-keto-3-methylvalerate (isoleucine pathway), both well-established steps in branched-chain amino-acid biosynthesis. This allows elimination of A (glycolipid biosynthesis involves glycosyltransferases, not dehydratases of this type) and C (threonine from aspartate involves homoserine dehydrogenase, homoserine kinase, threonine synthase — no DHAD step). Distinguishing B from D requires recognizing that while the gene sits in an aspterric-acid cluster, the enzyme's catalytic reaction is a canonical amino-acid biosynthetic dehydration.


**Missing item-specific fact**

> The specific organism (Penicillium brasilianum) and the fact that this DHAD paralog is embedded in an aspterric-acid secondary-metabolite gene cluster are not derivable from the sequence alone. However, the primary enzymatic function (DHAD → amino-acid biosynthesis) is inferable from the domain architecture without knowing the cluster context.


**Reason**

> A knowledgeable model can recognize the DHAD domain from conserved motifs and map it to branched-chain amino-acid biosynthesis using standard biochemistry. The B-vs-D distinction is somewhat subtle (the protein participates in a secondary-metabolite cluster) but the question asks for the 'primary metabolic pathway,' and DHAD's reaction is unambiguously an amino-acid biosynthetic step.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The protein is named 'Aspterric acid biosynthesis cluster protein D' (PubMed:39511739), placing it within a secondary-metabolite biosynthetic gene cluster. A model aware of this cluster context could argue for D (Secondary metabolite biosynthesis). However, the UniProt pathway annotation, the EC number (4.2.1.9), and the enzymatic reaction all point to amino-acid biosynthesis as the primary pathway. The question phrasing 'primary metabolic or signaling pathway' favors B, but the secondary-metabolite cluster context introduces mild ambiguity.


### Important caveats

- The UniProt pathway annotations carry evidence code ECO:0000250 (similarity-based inference from Q0CPG9), not direct experimental pathway assignment. The experimental evidence (ECO:0000305, PubMed:39511739) supports the DHAD enzymatic function but the specific pathway step assignment is by homology.
- The protein's role in the aspterric-acid secondary-metabolite cluster (alternative name, PubMed:39511739) means it may serve a repurposed function in secondary metabolism in P. brasilianum, adding nuance to the B-vs-D choice.
- The sequence match to UniProt A0A0F7TWW9 is exact (SHA-256 match confirmed in both current and historical snapshots), so the annotation applies directly.
- The entry was first publicly released in April 2025; the author's source snapshot date is unknown, so the annotation available to the benchmark author may differ from the current entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays canonical DHAD/IlvD domain signatures: the Fe-S cluster-binding motif 'GAGLGQDVALLTDGRFSGG' (residues ~470-490), the 'ACPGKGACGG' loop, and the overall ~250-residue catalytic fold. DHAD catalyzes the dehydration of 2,3-dihydroxy-isovalerate → 2-keto-isovalerate (valine pathway) and 2,3-dihydroxy-3-methylvalerate → 2-keto-3-methylvalerate (isoleucine pathway), both well-established steps in branched-chain amino-acid biosynthesis. This allows elimination of A (glycolipid biosynthesis involves glycosyltransferases, not dehydratases of this type) and C (threonine from aspartate involves homoserine dehydrogenase, homoserine kinase, threonine synthase — no DHAD step). Distinguishing B from D requires recognizing that while the gene sits in an aspterric-acid cluster, the enzyme's catalytic reaction is a canonical amino-acid biosynthetic dehydration.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific organism (Penicillium brasilianum) and the fact that this DHAD paralog is embedded in an aspterric-acid secondary-metabolite gene cluster are not derivable from the sequence alone. However, the primary enzymatic function (DHAD → amino-acid biosynthesis) is inferable from the domain architecture without knowing the cluster context.",
    "reason": "A knowledgeable model can recognize the DHAD domain from conserved motifs and map it to branched-chain amino-acid biosynthesis using standard biochemistry. The B-vs-D distinction is somewhat subtle (the protein participates in a secondary-metabolite cluster) but the question asks for the 'primary metabolic pathway,' and DHAD's reaction is unambiguously an amino-acid biosynthetic step."
  },
  "case_id": "pathway_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence contains hallmark dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) motifs, including the Fe-S cluster-binding 'GAGLGQDVALLTDGRFSGG' and the 'ACPGKGACGG' signature. UniProt entry A0A0F7TWW9 (PBRD_PENBI) annotates the pathway as 'Amino-acid biosynthesis; L-isoleucine biosynthesis' and 'Amino-acid biosynthesis; L-valine biosynthesis' (evidence ECO:0000250, similarity-based). The recommended name is 'Dihydroxy-acid dehydratase pbrD, mitochondrial' with EC 4.2.1.9 (ECO:0000305, PubMed:39511739). Choice B ('Amino-acid biosynthesis') matches the UniProt pathway annotation. The alternative name 'Aspterric acid biosynthesis cluster protein D' links the protein to a secondary-metabolite gene cluster, but the enzymatic function and pathway assignment remain amino-acid biosynthesis."
  },
  "important_caveats": [
    "The UniProt pathway annotations carry evidence code ECO:0000250 (similarity-based inference from Q0CPG9), not direct experimental pathway assignment. The experimental evidence (ECO:0000305, PubMed:39511739) supports the DHAD enzymatic function but the specific pathway step assignment is by homology.",
    "The protein's role in the aspterric-acid secondary-metabolite cluster (alternative name, PubMed:39511739) means it may serve a repurposed function in secondary metabolism in P. brasilianum, adding nuance to the B-vs-D choice.",
    "The sequence match to UniProt A0A0F7TWW9 is exact (SHA-256 match confirmed in both current and historical snapshots), so the annotation applies directly.",
    "The entry was first publicly released in April 2025; the author's source snapshot date is unknown, so the annotation available to the benchmark author may differ from the current entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The protein is named 'Aspterric acid biosynthesis cluster protein D' (PubMed:39511739), placing it within a secondary-metabolite biosynthetic gene cluster. A model aware of this cluster context could argue for D (Secondary metabolite biosynthesis). However, the UniProt pathway annotation, the EC number (4.2.1.9), and the enzymatic reaction all point to amino-acid biosynthesis as the primary pathway. The question phrasing 'primary metabolic or signaling pathway' favors B, but the secondary-metabolite cluster context introduces mild ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence contains hallmark dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) motifs, including the Fe-S cluster-binding 'GAGLGQDVALLTDGRFSGG' and the 'ACPGKGACGG' signature. UniProt entry A0A0F7TWW9 (PBRD_PENBI) annotates the pathway as 'Amino-acid biosynthesis; L-isoleucine biosynthesis' and 'Amino-acid biosynthesis; L-valine biosynthesis' (evidence ECO:0000250, similarity-based). The recommended name is 'Dihydroxy-acid dehydratase pbrD, mitochondrial' with EC 4.2.1.9 (ECO:0000305, PubMed:39511739). Choice B ('Amino-acid biosynthesis') matches the UniProt pathway annotation. The alternative name 'Aspterric acid biosynthesis cluster protein D' links the protein to a secondary-metabolite gene cluster, but the enzymatic function and pathway assignment remain amino-acid biosynthesis.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays canonical DHAD/IlvD domain signatures: the Fe-S cluster-binding motif 'GAGLGQDVALLTDGRFSGG' (residues ~470-490), the 'ACPGKGACGG' loop, and the overall ~250-residue catalytic fold. DHAD catalyzes the dehydration of 2,3-dihydroxy-isovalerate → 2-keto-isovalerate (valine pathway) and 2,3-dihydroxy-3-methylvalerate → 2-keto-3-methylvalerate (isoleucine pathway), both well-established steps in branched-chain amino-acid biosynthesis. This allows elimination of A (glycolipid biosynthesis involves glycosyltransferases, not dehydratases of this type) and C (threonine from aspartate involves homoserine dehydrogenase, homoserine kinase, threonine synthase — no DHAD step). Distinguishing B from D requires recognizing that while the gene sits in an aspterric-acid cluster, the enzyme's catalytic reaction is a canonical amino-acid biosynthetic dehydration.",
    "missing_item_specific_fact": "The specific organism (Penicillium brasilianum) and the fact that this DHAD paralog is embedded in an aspterric-acid secondary-metabolite gene cluster are not derivable from the sequence alone. However, the primary enzymatic function (DHAD → amino-acid biosynthesis) is inferable from the domain architecture without knowing the cluster context.",
    "reason": "A knowledgeable model can recognize the DHAD domain from conserved motifs and map it to branched-chain amino-acid biosynthesis using standard biochemistry. The B-vs-D distinction is somewhat subtle (the protein participates in a secondary-metabolite cluster) but the question asks for the 'primary metabolic pathway,' and DHAD's reaction is unambiguously an amino-acid biosynthetic step."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The protein is named 'Aspterric acid biosynthesis cluster protein D' (PubMed:39511739), placing it within a secondary-metabolite biosynthetic gene cluster. A model aware of this cluster context could argue for D (Secondary metabolite biosynthesis). However, the UniProt pathway annotation, the EC number (4.2.1.9), and the enzymatic reaction all point to amino-acid biosynthesis as the primary pathway. The question phrasing 'primary metabolic or signaling pathway' favors B, but the secondary-metabolite cluster context introduces mild ambiguity."
  },
  "important_caveats": [
    "The UniProt pathway annotations carry evidence code ECO:0000250 (similarity-based inference from Q0CPG9), not direct experimental pathway assignment. The experimental evidence (ECO:0000305, PubMed:39511739) supports the DHAD enzymatic function but the specific pathway step assignment is by homology.",
    "The protein's role in the aspterric-acid secondary-metabolite cluster (alternative name, PubMed:39511739) means it may serve a repurposed function in secondary metabolism in P. brasilianum, adding nuance to the B-vs-D choice.",
    "The sequence match to UniProt A0A0F7TWW9 is exact (SHA-256 match confirmed in both current and historical snapshots), so the annotation applies directly.",
    "The entry was first publicly released in April 2025; the author's source snapshot date is unknown, so the annotation available to the benchmark author may differ from the current entry."
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

**Accession:** `A0A0F7TWW9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein D"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39511739","source":"PubMed"}],"value":"4.2.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Dihydroxy-acid dehydratase pbrD, mitochondrial"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"DHAD astD"}]}}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/comments/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q0CPG9","source":"UniProtKB"}],"value":"Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4"}]}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/comments/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q0CPG9","source":"UniProtKB"}],"value":"Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4"}]}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
ID   PBRD_PENBI              Reviewed;         596 AA.
AC   A0A0F7TWW9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 2.
DT   28-JAN-2026, entry version 30.
DE   RecName: Full=Dihydroxy-acid dehydratase pbrD, mitochondrial {ECO:0000303|PubMed:39511739};
DE            Short=DHAD astD {ECO:0000303|PubMed:39511739};
DE            EC=4.2.1.9 {ECO:0000305|PubMed:39511739};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:39511739};
DE   Flags: Precursor;
GN   Name=pbrD {ECO:0000303|PubMed:39511739}; ORFNames=PMG11_09713;
OS   Penicillium brasilianum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=104259;
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 69-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-isoleucine biosynthesis; L-
CC       isoleucine from 2-oxobutanoate: step 3/4.
CC       {ECO:0000250|UniProtKB:Q0CPG9}.
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 72-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-valine biosynthesis; L-valine from
CC       pyruvate: step 3/4. {ECO:0000250|UniProtKB:Q0CPG9}.
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 194. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
