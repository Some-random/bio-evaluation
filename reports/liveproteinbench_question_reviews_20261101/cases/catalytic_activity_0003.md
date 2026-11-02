# catalytic_activity_0003

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — 2&#x27;-deoxyribonucleotide-(2&#x27;-deoxyribose 5&#x27;-phosphate)-2&#x27;-deoxyribonucleotide-DNA = a 3&#x27;-end 2&#x27;-deoxyribonucleotide-(2,3-dehydro-2,3-deoxyribose 5&#x27;-phosphate)-DNA + a 5&#x27;-end 5&#x27;-phospho-2&#x27;-deoxyribonucleoside-DNA + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPEGDTVFHTAAALRAALEGKTLTRCDVRVPRYATVDLSGAVVDEVLSRGKHLFIRAGSASIHSHLKMEGAWRIGHTKVAPHRIRIVLETADTRAIGIDLGILEVLDRGTDMDAVAYLGPDLLGPDWEPRVAADNLAADPDRPLAQALLDQRVMAGVGNVYCNELCFVFGRLPTAPVGTLKDPLRVVQRARDMLWLNRSRWNRTTTGDTRNGRQLWVYGRAGEPCRRCGTLIQTDRGGERVTYWCPVCQTAS

[Multiple Choices]
A. 2'-deoxyribonucleotide-(2'-deoxyribose 5'-phosphate)-2'-deoxyribonucleotide-DNA = a 3'-end 2'-deoxyribonucleotide-(2,3-dehydro-2,3-deoxyribose 5'-phosphate)-DNA + a 5'-end 5'-phospho-2'-deoxyribonucleoside-DNA + H(+)
B. O-phospho-L-homoserine + L-cysteine = L,L-cystathionine + phosphate
C. Mg(2+)(in) = Mg(2+)(out)
D. L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)
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

> The exact sequence matches a UniProt entry annotated as DNA-(apurinic or apyrimidinic site) lyase Nei2, with EC 4.2.99.18 and the reaction in choice A. The annotation cites both a PROSITE rule and publications marked with experimental evidence codes; the cited papers were not independently assessed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal Pro-Glu motif, internal GPD-containing region, and C-terminal cysteine-rich region are consistent with a Nei/Fpg-family DNA glycosylase/AP lyase. That family cleaves DNA at abasic sites, matching the DNA strand-cleavage reaction in A rather than the amino-acid transformations or ion transport in B–D.


**Missing item-specific fact**

> The precise Nei2 identity and experimentally characterized reaction are item-specific facts not explicitly supplied; family-level inference from the sequence motifs and reaction choices nevertheless meaningfully distinguishes A.


**Reason**

> The sequence contains recognizable family-level cues supporting a DNA repair lyase function, so selection need not rely solely on identifying the exact protein or retrieving its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based family inference points to DNA repair lyase activity, and only A describes cleavage of DNA.


### Important caveats

- Reviewer-only UniProt evidence confirms an exact sequence match; it was not available to the evaluated model.
- The database annotation combines computational rule evidence with cited experimental evidence, but the underlying publications were not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal Pro-Glu motif, internal GPD-containing region, and C-terminal cysteine-rich region are consistent with a Nei/Fpg-family DNA glycosylase/AP lyase. That family cleaves DNA at abasic sites, matching the DNA strand-cleavage reaction in A rather than the amino-acid transformations or ion transport in B–D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise Nei2 identity and experimentally characterized reaction are item-specific facts not explicitly supplied; family-level inference from the sequence motifs and reaction choices nevertheless meaningfully distinguishes A.",
    "reason": "The sequence contains recognizable family-level cues supporting a DNA repair lyase function, so selection need not rely solely on identifying the exact protein or retrieving its database entry."
  },
  "case_id": "catalytic_activity_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as DNA-(apurinic or apyrimidinic site) lyase Nei2, with EC 4.2.99.18 and the reaction in choice A. The annotation cites both a PROSITE rule and publications marked with experimental evidence codes; the cited papers were not independently assessed here."
  },
  "important_caveats": [
    "Reviewer-only UniProt evidence confirms an exact sequence match; it was not available to the evaluated model.",
    "The database annotation combines computational rule evidence with cited experimental evidence, but the underlying publications were not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference points to DNA repair lyase activity, and only A describes cleavage of DNA."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as DNA-(apurinic or apyrimidinic site) lyase Nei2, with EC 4.2.99.18 and the reaction in choice A. The annotation cites both a PROSITE rule and publications marked with experimental evidence codes; the cited papers were not independently assessed here.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal Pro-Glu motif, internal GPD-containing region, and C-terminal cysteine-rich region are consistent with a Nei/Fpg-family DNA glycosylase/AP lyase. That family cleaves DNA at abasic sites, matching the DNA strand-cleavage reaction in A rather than the amino-acid transformations or ion transport in B–D.",
    "missing_item_specific_fact": "The precise Nei2 identity and experimentally characterized reaction are item-specific facts not explicitly supplied; family-level inference from the sequence motifs and reaction choices nevertheless meaningfully distinguishes A.",
    "reason": "The sequence contains recognizable family-level cues supporting a DNA repair lyase function, so selection need not rely solely on identifying the exact protein or retrieving its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference points to DNA repair lyase activity, and only A describes cleavage of DNA."
  },
  "important_caveats": [
    "Reviewer-only UniProt evidence confirms an exact sequence match; it was not available to the evaluated model.",
    "The database annotation combines computational rule evidence with cited experimental evidence, but the underlying publications were not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0QT90 (END8B_MYCS2, Nei2 from Mycolicibacterium smegmatis) explicitly annotates the catalytic activity as EC 4.2.99.18 with the exact reaction text matching Choice A word-for-word. Evidence codes include ECO:0000269 (experimental evidence) from two independent publications (PubMed:36610794, 2023; PubMed:39012146, 2024) plus a crystal structure (PDB: 8TJG at 1.45 Å in complex with Zn²⁺). The sequence matches the benchmark input exactly (SHA-256 confirmed). The annotation is supported by both computational (PROSITE-ProRule PRU00392) and experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 252-residue sequence contains hallmark motifs of the HhH-GPD superfamily of DNA repair enzymes: (1) the 'GPD' tripeptide motif visible in 'GPDLLGPDWEPR', (2) a C-terminal zinc-binding cluster 'CPVCQTAS' characteristic of HhH-GPD glycosylases/AP lyases (Nth/Nei family), and (3) additional Cys residues forming a zinc-binding site. These motifs are well-established signatures of small DNA-repair enzymes. Among the four choices, only A describes a DNA-related reaction (AP lyase backbone β-elimination). Choices B (PLP-dependent cystathionine γ-synthase), C (Mg²⁺ transporter requiring transmembrane helices), and D (aspartate kinase, a large amino-acid biosynthetic enzyme) are structurally and functionally incompatible with a 252-residue protein bearing HhH-GPD zinc-binding motifs and no transmembrane segments. A model with general protein-family knowledge can reason from these motifs to a DNA repair enzyme and select the only DNA-cleavage option.


**Missing item-specific fact**

> None critical. Distinguishing this specific Nei2 AP lyase from other HhH-GPD members (e.g., Nth, MutY) would require finer annotation, but the question only requires identifying the correct reaction among four choices, three of which are entirely unrelated enzyme classes.


**Reason**

> The sequence provides recognizable superfamily-level motifs (GPD, C-terminal Zn-binding Cys cluster) that a model with standard biochemistry training can use to infer a DNA repair enzyme function, thereby eliminating the three non-DNA distractors. This constitutes a concrete biological argument from the supplied sequence rather than pure memorization of one accession's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein carries dual EC annotations (3.2.2.- glycosylase and 4.2.99.18 AP lyase), but only the AP lyase reaction (Choice A) appears among the options. The glycosylase reaction (N-glycosidic bond hydrolysis) is not listed. The three distractors (B, C, D) belong to entirely different enzyme classes and are clearly incompatible with the sequence's structural motifs. No ambiguity exists among the presented choices.


### Important caveats

- The UniProt entry was first publicly released on 2025-06-18; the benchmark construction date is unknown. If the question was authored before this date, the annotation may not have been available at construction time, though the sequence itself (submitted 2007) was.
- The EC 3.2.2.- glycosylase activity is also annotated but its reaction is not among the choices, so it does not create ambiguity.
- The reviewer-only evidence (UniProt accession, PubMed references, PDB structure) was not available to the evaluated model; the reasoning assessment is based solely on what the sequence and choices provide.
- The PROSITE-ProRule annotation (ECO:0000255) is computational; the two PubMed references (ECO:0000269) provide experimental support for the AP lyase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 252-residue sequence contains hallmark motifs of the HhH-GPD superfamily of DNA repair enzymes: (1) the 'GPD' tripeptide motif visible in 'GPDLLGPDWEPR', (2) a C-terminal zinc-binding cluster 'CPVCQTAS' characteristic of HhH-GPD glycosylases/AP lyases (Nth/Nei family), and (3) additional Cys residues forming a zinc-binding site. These motifs are well-established signatures of small DNA-repair enzymes. Among the four choices, only A describes a DNA-related reaction (AP lyase backbone β-elimination). Choices B (PLP-dependent cystathionine γ-synthase), C (Mg²⁺ transporter requiring transmembrane helices), and D (aspartate kinase, a large amino-acid biosynthetic enzyme) are structurally and functionally incompatible with a 252-residue protein bearing HhH-GPD zinc-binding motifs and no transmembrane segments. A model with general protein-family knowledge can reason from these motifs to a DNA repair enzyme and select the only DNA-cleavage option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Distinguishing this specific Nei2 AP lyase from other HhH-GPD members (e.g., Nth, MutY) would require finer annotation, but the question only requires identifying the correct reaction among four choices, three of which are entirely unrelated enzyme classes.",
    "reason": "The sequence provides recognizable superfamily-level motifs (GPD, C-terminal Zn-binding Cys cluster) that a model with standard biochemistry training can use to infer a DNA repair enzyme function, thereby eliminating the three non-DNA distractors. This constitutes a concrete biological argument from the supplied sequence rather than pure memorization of one accession's annotation."
  },
  "case_id": "catalytic_activity_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0QT90 (END8B_MYCS2, Nei2 from Mycolicibacterium smegmatis) explicitly annotates the catalytic activity as EC 4.2.99.18 with the exact reaction text matching Choice A word-for-word. Evidence codes include ECO:0000269 (experimental evidence) from two independent publications (PubMed:36610794, 2023; PubMed:39012146, 2024) plus a crystal structure (PDB: 8TJG at 1.45 Å in complex with Zn²⁺). The sequence matches the benchmark input exactly (SHA-256 confirmed). The annotation is supported by both computational (PROSITE-ProRule PRU00392) and experimental evidence."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-06-18; the benchmark construction date is unknown. If the question was authored before this date, the annotation may not have been available at construction time, though the sequence itself (submitted 2007) was.",
    "The EC 3.2.2.- glycosylase activity is also annotated but its reaction is not among the choices, so it does not create ambiguity.",
    "The reviewer-only evidence (UniProt accession, PubMed references, PDB structure) was not available to the evaluated model; the reasoning assessment is based solely on what the sequence and choices provide.",
    "The PROSITE-ProRule annotation (ECO:0000255) is computational; the two PubMed references (ECO:0000269) provide experimental support for the AP lyase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein carries dual EC annotations (3.2.2.- glycosylase and 4.2.99.18 AP lyase), but only the AP lyase reaction (Choice A) appears among the options. The glycosylase reaction (N-glycosidic bond hydrolysis) is not listed. The three distractors (B, C, D) belong to entirely different enzyme classes and are clearly incompatible with the sequence's structural motifs. No ambiguity exists among the presented choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0QT90 (END8B_MYCS2, Nei2 from Mycolicibacterium smegmatis) explicitly annotates the catalytic activity as EC 4.2.99.18 with the exact reaction text matching Choice A word-for-word. Evidence codes include ECO:0000269 (experimental evidence) from two independent publications (PubMed:36610794, 2023; PubMed:39012146, 2024) plus a crystal structure (PDB: 8TJG at 1.45 Å in complex with Zn²⁺). The sequence matches the benchmark input exactly (SHA-256 confirmed). The annotation is supported by both computational (PROSITE-ProRule PRU00392) and experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 252-residue sequence contains hallmark motifs of the HhH-GPD superfamily of DNA repair enzymes: (1) the 'GPD' tripeptide motif visible in 'GPDLLGPDWEPR', (2) a C-terminal zinc-binding cluster 'CPVCQTAS' characteristic of HhH-GPD glycosylases/AP lyases (Nth/Nei family), and (3) additional Cys residues forming a zinc-binding site. These motifs are well-established signatures of small DNA-repair enzymes. Among the four choices, only A describes a DNA-related reaction (AP lyase backbone β-elimination). Choices B (PLP-dependent cystathionine γ-synthase), C (Mg²⁺ transporter requiring transmembrane helices), and D (aspartate kinase, a large amino-acid biosynthetic enzyme) are structurally and functionally incompatible with a 252-residue protein bearing HhH-GPD zinc-binding motifs and no transmembrane segments. A model with general protein-family knowledge can reason from these motifs to a DNA repair enzyme and select the only DNA-cleavage option.",
    "missing_item_specific_fact": "None critical. Distinguishing this specific Nei2 AP lyase from other HhH-GPD members (e.g., Nth, MutY) would require finer annotation, but the question only requires identifying the correct reaction among four choices, three of which are entirely unrelated enzyme classes.",
    "reason": "The sequence provides recognizable superfamily-level motifs (GPD, C-terminal Zn-binding Cys cluster) that a model with standard biochemistry training can use to infer a DNA repair enzyme function, thereby eliminating the three non-DNA distractors. This constitutes a concrete biological argument from the supplied sequence rather than pure memorization of one accession's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein carries dual EC annotations (3.2.2.- glycosylase and 4.2.99.18 AP lyase), but only the AP lyase reaction (Choice A) appears among the options. The glycosylase reaction (N-glycosidic bond hydrolysis) is not listed. The three distractors (B, C, D) belong to entirely different enzyme classes and are clearly incompatible with the sequence's structural motifs. No ambiguity exists among the presented choices."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-06-18; the benchmark construction date is unknown. If the question was authored before this date, the annotation may not have been available at construction time, though the sequence itself (submitted 2007) was.",
    "The EC 3.2.2.- glycosylase activity is also annotated but its reaction is not among the choices, so it does not create ambiguity.",
    "The reviewer-only evidence (UniProt accession, PubMed references, PDB structure) was not available to the evaluated model; the reasoning assessment is based solely on what the sequence and choices provide.",
    "The PROSITE-ProRule annotation (ECO:0000255) is computational; the two PubMed references (ECO:0000269) provide experimental support for the AP lyase activity."
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

**Accession:** `A0QT90` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 140. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.186229+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P9WNC1","source":"UniProtKB"}],"value":"Endonuclease 8 2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00392","source":"PROSITE-ProRule"},{"evidenceCode":"ECO:0000269","id":"39012146","source":"PubMed"}],"value":"3.2.2.-"},{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00392","source":"PROSITE-ProRule"},{"evidenceCode":"ECO:0000269","id":"36610794","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39012146","source":"PubMed"}],"value":"4.2.99.18"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36610794","source":"PubMed"}],"value":"DNA-(apurinic or apyrimidinic site) lyase Nei2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36610794","source":"PubMed"}],"value":"AP lyase"}]}}
```

Source SHA-256: `b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.186229+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"4.2.99.18","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00392","source":"PROSITE-ProRule"},{"evidenceCode":"ECO:0000269","id":"36610794","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39012146","source":"PubMed"}],"name":"2'-deoxyribonucleotide-(2'-deoxyribose 5'-phosphate)-2'-deoxyribonucleotide-DNA = a 3'-end 2'-deoxyribonucleotide-(2,3-dehydro-2,3-deoxyribose 5'-phosphate)-DNA + a 5'-end 5'-phospho-2'-deoxyribonucleoside-DNA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:66592"},{"database":"Rhea","id":"RHEA-COMP:13180"},{"database":"Rhea","id":"RHEA-COMP:16897"},{"database":"Rhea","id":"RHEA-COMP:17067"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:136412"},{"database":"ChEBI","id":"CHEBI:157695"},{"database":"ChEBI","id":"CHEBI:167181"}]}}
```

Source SHA-256: `b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.186229+00:00.  

```json
{"citation":{"authors":["Warren G.M.","Ejaz A.","Fay A.","Glickman M.S.","Shuman S."],"citationCrossReferences":[{"database":"PubMed","id":"36610794"},{"database":"DOI","id":"10.1093/nar/gkac1222"}],"citationType":"journal article","firstPage":"218","id":"36610794","journal":"Nucleic Acids Res.","lastPage":"235","publicationDate":"2023","title":"Mycobacterial helicase Lhr abets resistance to DNA crosslinking agents mitomycin C and cisplatin.","volume":"51"},"referenceComments":[{"type":"STRAIN","value":"ATCC 700084 / mc(2)155"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PROBABLE ACTIVE SITE","SUBUNIT"]}
```

Source SHA-256: `b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.186229+00:00.  

```json
{"citation":{"authors":["Warren G.M.","Shuman S."],"citationCrossReferences":[{"database":"PubMed","id":"39012146"},{"database":"DOI","id":"10.1128/mbio.01248-24"}],"citationType":"journal article","firstPage":"e0124824","id":"39012146","journal":"MBio","lastPage":"e0124824","publicationDate":"2024","title":"Structure and in vivo psoralen DNA crosslink repair activity of mycobacterial Nei2.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8TJG","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 700084 / mc(2)155"}],"referenceNumber":5,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.45 ANGSTROMS) IN COMPLEX WITH ZN(2+)","FUNCTION","CATALYTIC ACTIVITY","PROBABLE ACTIVE SITE","COFACTOR","SUBUNIT","DISRUPTION PHENOTYPE","MUTAGENESIS OF PRO-2; GLU-3 AND LYS-51"]}
```

Source SHA-256: `b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 140 / 1.  
**Retrieved:** 2026-11-01T06:27:42.166883+00:00.  

```text
DE   RecName: Full=DNA-(apurinic or apyrimidinic site) lyase Nei2 {ECO:0000303|PubMed:36610794};
DE            Short=AP lyase {ECO:0000303|PubMed:36610794};
DE            EC=3.2.2.- {ECO:0000255|PROSITE-ProRule:PRU00392, ECO:0000269|PubMed:39012146};
DE            EC=4.2.99.18 {ECO:0000255|PROSITE-ProRule:PRU00392, ECO:0000269|PubMed:36610794, ECO:0000269|PubMed:39012146};
DE   AltName: Full=Endonuclease 8 2 {ECO:0000250|UniProtKB:P9WNC1};
```

Source SHA-256: `cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 140 / 1.  
**Retrieved:** 2026-11-01T06:27:42.166883+00:00.  

```text
RN   [4]
RP   FUNCTION, CATALYTIC ACTIVITY, PROBABLE ACTIVE SITE, AND SUBUNIT.
RC   STRAIN=ATCC 700084 / mc(2)155;
RX   PubMed=36610794; DOI=10.1093/nar/gkac1222;
RA   Warren G.M., Ejaz A., Fay A., Glickman M.S., Shuman S.;
RT   "Mycobacterial helicase Lhr abets resistance to DNA crosslinking agents
RT   mitomycin C and cisplatin.";
RL   Nucleic Acids Res. 51:218-235(2023).
```

Source SHA-256: `cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)  
**Locator:** `lines 50-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 140 / 1.  
**Retrieved:** 2026-11-01T06:27:42.166883+00:00.  

```text
RN   [5] {ECO:0007744|PDB:8TJG}
RP   X-RAY CRYSTALLOGRAPHY (1.45 ANGSTROMS) IN COMPLEX WITH ZN(2+), FUNCTION,
RP   CATALYTIC ACTIVITY, PROBABLE ACTIVE SITE, COFACTOR, SUBUNIT, DISRUPTION
RP   PHENOTYPE, AND MUTAGENESIS OF PRO-2; GLU-3 AND LYS-51.
RC   STRAIN=ATCC 700084 / mc(2)155;
RX   PubMed=39012146; DOI=10.1128/mbio.01248-24;
RA   Warren G.M., Shuman S.;
RT   "Structure and in vivo psoralen DNA crosslink repair activity of
RT   mycobacterial Nei2.";
RL   MBio 15:e0124824-e0124824(2024).
```

Source SHA-256: `cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)  
**Locator:** `lines 75-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 140 / 1.  
**Retrieved:** 2026-11-01T06:27:42.166883+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2'-deoxyribonucleotide-(2'-deoxyribose 5'-phosphate)-2'-
CC         deoxyribonucleotide-DNA = a 3'-end 2'-deoxyribonucleotide-(2,3-
CC         dehydro-2,3-deoxyribose 5'-phosphate)-DNA + a 5'-end 5'-phospho-2'-
CC         deoxyribonucleoside-DNA + H(+); Xref=Rhea:RHEA:66592, Rhea:RHEA-
CC         COMP:13180, Rhea:RHEA-COMP:16897, Rhea:RHEA-COMP:17067,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:136412, ChEBI:CHEBI:157695,
CC         ChEBI:CHEBI:167181; EC=4.2.99.18; Evidence={ECO:0000255|PROSITE-
CC         ProRule:PRU00392, ECO:0000269|PubMed:36610794,
CC         ECO:0000269|PubMed:39012146};
```

Source SHA-256: `cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
