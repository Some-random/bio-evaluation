# catalytic_activity_0186

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — ATP + H2O = ADP + phosphate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPPKKSNARNASLLKEAVTNAGRSDTASTAREGSIAATFVSDSDSSTTASGPVDEKVAAVAELITTLTTNAASDKRQSAADDIAKFVEAEGVAQMVKTKILHGIATGLHNTKQPVAREGAITAIETLIKSPVSKQIEPYMITFIPVLLERLSDKAKTVCLAADSALKALITRLTPYATKQVLPLLLAGIEYSQKWQTKVGALELMQSLSKTAPRQMTTAVPDLVPPLSEVMHDTKAEAKNAGRQTMEAICELINNKDIEKFIPALIDTIANPEKVPDTVHLLGATTFVSEVLPPTLAIMVPLLSRGLNERQTAIKRKAAVIIINMCKLVEKPQIIAPFLPRLLPTLEKIQDDVADPECRQVCQNATKILTKVGIPAPGTVMDDSYEFKKLDDKALAYLKKAIGHQQITEIPEAYRPVLEYLEHIAAAMVADGNMDNDDWNGSIIPTLKAFIPTEGTVTNAVKEFRELSFGSNVKEAVAEEEEDDAEELCNCEFSLAYGARVLLNRTHLILKRGHRYGLTGANGSGKSTLMRAIANGQVEGFPPADQLKTVAVEHDLDGAHEHDNKEVQAFVLEDPVYAHLPKETVVNMLESVGFKGPMATRPVGQLSGGWRMKLALARAMLHNADILLLDEPTNHLDVINVAWLQDYLIGLKTVTSIIVSHDSSFLDIVCSDIIHLDNFKLKRYRGNLSKFVEAVPEAKAYYELGAAQQTFRFPEPGMLEGVKTKERAILKVQNAVFQYPGTDRRQLNGVTFQCSLGSRVAVVGPNGAGKSTLIKLLCGVIEPDNGVVWRHPNLRIAYVAQHAFEHIEKHTNLTPNQYIQWRYQTGEDREEMEKAARQISAEEEAAMKKVQVISGEKKVVDSVIGRRKLKNSYEYEVSWVGKLSNENSWLPRDTLIEMGFLKKVQEIDQAEAARQGLARPLTQKEIEKHLSDVGIDSEIGTHSHIRGLSGGQKVKVVIAGAMWQRPHLLVLDEPTNFLDRDSLGALKTAIDAYGGGVIMVTHSREFSEAICKEVWKVDNGELTPTGHNWVSGQGSGPRLEDKNKDEEVFDAFGNKIDVAKQKSKLSGKDLRKKRKEREARRKRGEEVSDDDE

[Multiple Choices]
A. a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+)
B. FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)
C. a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)
D. ATP + H2O = ADP + phosphate + H(+)
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

> The exact sequence matches the UniProt entry for elongation factor 3, whose catalytic-activity annotation is ATP + H2O = ADP + phosphate + H(+). The annotation is transferred by similarity (ECO:0000250), so it supports the key as a database annotation, not as independently verified experimental evidence for this particular protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple Walker A/P-loop-like motifs, including GANGSGKST and GPNGAGKST, consistent with nucleotide-binding ATPase domains. That provides a concrete basis to favor ATP hydrolysis (D) over the lipid, redox, and glycosyl-transfer reactions in the other choices.


**Missing item-specific fact**

> No protein-specific catalytic measurement or annotation is supplied; such evidence would be needed to establish the precise reaction experimentally, but the ATPase motifs meaningfully distinguish the choices.


**Reason**

> The sequence offers recognizable ATPase-domain evidence relevant to the listed alternatives, rather than requiring memorization of the exact database entry. The precise annotation is reviewer-only corroboration.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, the sequence's repeated ATPase-associated motifs support D; the other options describe unrelated reaction classes.


### Important caveats

- The cited UniProt catalytic-activity annotation is transferred by similarity from another entry and is not direct experimental evidence for this sequence.
- The database sequence match establishes annotation applicability, but that accession and annotation were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple Walker A/P-loop-like motifs, including GANGSGKST and GPNGAGKST, consistent with nucleotide-binding ATPase domains. That provides a concrete basis to favor ATP hydrolysis (D) over the lipid, redox, and glycosyl-transfer reactions in the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific catalytic measurement or annotation is supplied; such evidence would be needed to establish the precise reaction experimentally, but the ATPase motifs meaningfully distinguish the choices.",
    "reason": "The sequence offers recognizable ATPase-domain evidence relevant to the listed alternatives, rather than requiring memorization of the exact database entry. The precise annotation is reviewer-only corroboration."
  },
  "case_id": "catalytic_activity_0186",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for elongation factor 3, whose catalytic-activity annotation is ATP + H2O = ADP + phosphate + H(+). The annotation is transferred by similarity (ECO:0000250), so it supports the key as a database annotation, not as independently verified experimental evidence for this particular protein."
  },
  "important_caveats": [
    "The cited UniProt catalytic-activity annotation is transferred by similarity from another entry and is not direct experimental evidence for this sequence.",
    "The database sequence match establishes annotation applicability, but that accession and annotation were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, the sequence's repeated ATPase-associated motifs support D; the other options describe unrelated reaction classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0186",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for elongation factor 3, whose catalytic-activity annotation is ATP + H2O = ADP + phosphate + H(+). The annotation is transferred by similarity (ECO:0000250), so it supports the key as a database annotation, not as independently verified experimental evidence for this particular protein.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple Walker A/P-loop-like motifs, including GANGSGKST and GPNGAGKST, consistent with nucleotide-binding ATPase domains. That provides a concrete basis to favor ATP hydrolysis (D) over the lipid, redox, and glycosyl-transfer reactions in the other choices.",
    "missing_item_specific_fact": "No protein-specific catalytic measurement or annotation is supplied; such evidence would be needed to establish the precise reaction experimentally, but the ATPase motifs meaningfully distinguish the choices.",
    "reason": "The sequence offers recognizable ATPase-domain evidence relevant to the listed alternatives, rather than requiring memorization of the exact database entry. The precise annotation is reviewer-only corroboration."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, the sequence's repeated ATPase-associated motifs support D; the other options describe unrelated reaction classes."
  },
  "important_caveats": [
    "The cited UniProt catalytic-activity annotation is transferred by similarity from another entry and is not direct experimental evidence for this sequence.",
    "The database sequence match establishes annotation applicability, but that accession and annotation were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A139AVY4 (EF3_GONPJ, Elongation factor 3 from Gonapodya prolifera, EC 3.6.4.-) explicitly lists the catalytic activity as 'ATP + H2O = ADP + phosphate + H(+)' (RHEA:13065) in both the current and historical (v47) records. The sequence SHA256 matches. The evidence code is ECO:0000250 (inferred by similarity from P16521, a characterized fungal EF-3), so this is a similarity-based annotation rather than direct experimental measurement, but it is consistent with the well-established ATPase function of fungal EF-3. The expected answer D matches the annotation exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1092-aa sequence contains multiple canonical P-loop NTPase (Walker A) motifs — 'GNSGKST' and 'GNGAGKST' — together with Walker B motifs ('DEPTN' appearing twice), indicating a multi-domain AAA+ ATPase architecture. This strongly predicts ATP hydrolysis (option D). The other options are inconsistent with this architecture: cardiolipin synthase (A) is a small membrane-associated CDP-diacylglycerol transferase with no P-loop motifs; an FMN/NADPH oxidoreductase (B) would contain Rossmann-fold flavin-binding motifs and a much smaller size; a glycosyltransferase (C) would display GT-A/GT-B fold signatures. None of these match a large soluble protein with tandem Walker A/B domains.


**Missing item-specific fact**

> None critical. While identifying the protein specifically as EF-3 (vs. another AAA+ ATPase) would benefit from database lookup, the question asks for the catalytic reaction, and the P-loop NTPase signature in the sequence is sufficient to select ATP hydrolysis over the three non-ATPase alternatives.


**Reason**

> The sequence's multiple Walker A and Walker B motifs provide a concrete, general biological argument for ATPase activity that meaningfully distinguishes D from A, B, and C without requiring knowledge of the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D (ATP hydrolysis) is consistent with the observed P-loop NTPase domain architecture. The other three options describe completely different enzyme classes (phosphatidyltransferase, flavoprotein oxidoreductase, glycosyltransferase) whose sequence signatures are absent from this protein.


### Important caveats

- The UniProt annotation for this entry uses evidence code ECO:0000250 (similarity to P16521), meaning the catalytic activity assignment is transferred by homology rather than directly measured for this specific protein.
- EF-3 is functionally an ATP-dependent translation factor; the listed reaction (ATP + H2O = ADP + Pi + H+) captures the hydrolytic component but not the full mechanistic coupling to ribosomal translocation.
- The EC number 3.6.4.- is a legacy translocase classification (now largely superseded by EC 7); the reaction itself is simply ATP hydrolysis.
- The protein is from Gonapodya prolifera, a chytrid fungus; EF-3 is found in fungi and some protists but not in animals or plants, which is relevant for biological context but does not affect the catalytic-reaction answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1092-aa sequence contains multiple canonical P-loop NTPase (Walker A) motifs — 'GNSGKST' and 'GNGAGKST' — together with Walker B motifs ('DEPTN' appearing twice), indicating a multi-domain AAA+ ATPase architecture. This strongly predicts ATP hydrolysis (option D). The other options are inconsistent with this architecture: cardiolipin synthase (A) is a small membrane-associated CDP-diacylglycerol transferase with no P-loop motifs; an FMN/NADPH oxidoreductase (B) would contain Rossmann-fold flavin-binding motifs and a much smaller size; a glycosyltransferase (C) would display GT-A/GT-B fold signatures. None of these match a large soluble protein with tandem Walker A/B domains.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While identifying the protein specifically as EF-3 (vs. another AAA+ ATPase) would benefit from database lookup, the question asks for the catalytic reaction, and the P-loop NTPase signature in the sequence is sufficient to select ATP hydrolysis over the three non-ATPase alternatives.",
    "reason": "The sequence's multiple Walker A and Walker B motifs provide a concrete, general biological argument for ATPase activity that meaningfully distinguishes D from A, B, and C without requiring knowledge of the specific UniProt entry."
  },
  "case_id": "catalytic_activity_0186",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A139AVY4 (EF3_GONPJ, Elongation factor 3 from Gonapodya prolifera, EC 3.6.4.-) explicitly lists the catalytic activity as 'ATP + H2O = ADP + phosphate + H(+)' (RHEA:13065) in both the current and historical (v47) records. The sequence SHA256 matches. The evidence code is ECO:0000250 (inferred by similarity from P16521, a characterized fungal EF-3), so this is a similarity-based annotation rather than direct experimental measurement, but it is consistent with the well-established ATPase function of fungal EF-3. The expected answer D matches the annotation exactly."
  },
  "important_caveats": [
    "The UniProt annotation for this entry uses evidence code ECO:0000250 (similarity to P16521), meaning the catalytic activity assignment is transferred by homology rather than directly measured for this specific protein.",
    "EF-3 is functionally an ATP-dependent translation factor; the listed reaction (ATP + H2O = ADP + Pi + H+) captures the hydrolytic component but not the full mechanistic coupling to ribosomal translocation.",
    "The EC number 3.6.4.- is a legacy translocase classification (now largely superseded by EC 7); the reaction itself is simply ATP hydrolysis.",
    "The protein is from Gonapodya prolifera, a chytrid fungus; EF-3 is found in fungi and some protists but not in animals or plants, which is relevant for biological context but does not affect the catalytic-reaction answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D (ATP hydrolysis) is consistent with the observed P-loop NTPase domain architecture. The other three options describe completely different enzyme classes (phosphatidyltransferase, flavoprotein oxidoreductase, glycosyltransferase) whose sequence signatures are absent from this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0186",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A139AVY4 (EF3_GONPJ, Elongation factor 3 from Gonapodya prolifera, EC 3.6.4.-) explicitly lists the catalytic activity as 'ATP + H2O = ADP + phosphate + H(+)' (RHEA:13065) in both the current and historical (v47) records. The sequence SHA256 matches. The evidence code is ECO:0000250 (inferred by similarity from P16521, a characterized fungal EF-3), so this is a similarity-based annotation rather than direct experimental measurement, but it is consistent with the well-established ATPase function of fungal EF-3. The expected answer D matches the annotation exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1092-aa sequence contains multiple canonical P-loop NTPase (Walker A) motifs — 'GNSGKST' and 'GNGAGKST' — together with Walker B motifs ('DEPTN' appearing twice), indicating a multi-domain AAA+ ATPase architecture. This strongly predicts ATP hydrolysis (option D). The other options are inconsistent with this architecture: cardiolipin synthase (A) is a small membrane-associated CDP-diacylglycerol transferase with no P-loop motifs; an FMN/NADPH oxidoreductase (B) would contain Rossmann-fold flavin-binding motifs and a much smaller size; a glycosyltransferase (C) would display GT-A/GT-B fold signatures. None of these match a large soluble protein with tandem Walker A/B domains.",
    "missing_item_specific_fact": "None critical. While identifying the protein specifically as EF-3 (vs. another AAA+ ATPase) would benefit from database lookup, the question asks for the catalytic reaction, and the P-loop NTPase signature in the sequence is sufficient to select ATP hydrolysis over the three non-ATPase alternatives.",
    "reason": "The sequence's multiple Walker A and Walker B motifs provide a concrete, general biological argument for ATPase activity that meaningfully distinguishes D from A, B, and C without requiring knowledge of the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D (ATP hydrolysis) is consistent with the observed P-loop NTPase domain architecture. The other three options describe completely different enzyme classes (phosphatidyltransferase, flavoprotein oxidoreductase, glycosyltransferase) whose sequence signatures are absent from this protein."
  },
  "important_caveats": [
    "The UniProt annotation for this entry uses evidence code ECO:0000250 (similarity to P16521), meaning the catalytic activity assignment is transferred by homology rather than directly measured for this specific protein.",
    "EF-3 is functionally an ATP-dependent translation factor; the listed reaction (ATP + H2O = ADP + Pi + H+) captures the hydrolytic component but not the full mechanistic coupling to ribosomal translocation.",
    "The EC number 3.6.4.- is a legacy translocase classification (now largely superseded by EC 7); the reaction itself is simply ATP hydrolysis.",
    "The protein is from Gonapodya prolifera, a chytrid fungus; EF-3 is found in fungi and some protists but not in animals or plants, which is relevant for biological context but does not affect the catalytic-reaction answer."
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

**Accession:** `A0A139AVY4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 47. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A139AVY4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.720658+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Eukaryotic elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"eEF3"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P16521","source":"UniProtKB"}],"value":"3.6.4.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"EF-3"}]}}
```

Source SHA-256: `74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A139AVY4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.720658+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P16521","source":"UniProtKB"}],"name":"ATP + H2O = ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13065"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `74bd678f72991892cdc46146cb4a86fe3b0f7d2ae19032dcd8c7d805bcb0f848`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 47 / 1.  
**Retrieved:** 2026-11-02T04:24:29.778395+00:00.  

```text
DE   RecName: Full=Elongation factor 3 {ECO:0000305};
DE            Short=EF-3 {ECO:0000305};
DE            EC=3.6.4.- {ECO:0000250|UniProtKB:P16521};
DE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};
DE            Short=eEF3 {ECO:0000305};
```

Source SHA-256: `f5583d453bb640e57a634cad7f6f94f5135da55d2628b07b6202933300efe260`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A139AVY4?format=txt&versions=47)  
**Locator:** `lines 45-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 47 / 1.  
**Retrieved:** 2026-11-02T04:24:29.778395+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP + H2O = ADP + phosphate + H(+); Xref=Rhea:RHEA:13065,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000250|UniProtKB:P16521};
```

Source SHA-256: `f5583d453bb640e57a634cad7f6f94f5135da55d2628b07b6202933300efe260`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 186. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
