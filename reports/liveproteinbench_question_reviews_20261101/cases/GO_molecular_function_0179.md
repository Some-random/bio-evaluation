# GO_molecular_function_0179

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — beta-glucosidase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGRNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAINSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPQSYSDFFGVAYDTPPKAHALKASRLLVPTTVARPSKPVRVFASTADPGTTTADQVYKVGHNLLLAHAAAIQVYRDKFQNTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQLLGPRLREFTPDQKKLLIGSYDYVGVNYYTATYVSSAQPPHDKKKAVFHTDGNFYTTDSKDGVLIGPLAGPAWLNIVPEGIYHVLHDIKENYEDPVIYITENGVYEVNDTAKTLSEARVDTTRLHYLQDHLSKVLEARHQGVRVQGYLVWSLMDNWELRAGYTSRFGLIHVDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKARPQEDDGAFDTPRKRLRKY

[Multiple Choices]
A. beta-glucosidase activity
B. molybdopterin cofactor binding
C. thioredoxin peroxidase activity
D. dol-P-Man:Man(8)GlcNAc(2)-PP-Dol alpha-1,2-mannosyltransferase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the 543-aa UniProt entry for Ipecac alkaloid beta-glucosidase 3. That entry reports beta-glucosidase activity and specific glucose-releasing reactions with experimental evidence attributed to a cited publication; its GO annotation is IDA. This supports choice A, while preserving that the evidence is an annotation reporting experimental findings rather than an independent review of the primary study.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the conserved catalytic-motif pattern characteristic of family-1 glycoside hydrolases, including an ENG motif, which supports a glucoside-hydrolyzing enzyme. Among the choices, beta-glucosidase activity is the compatible broad function; the other options describe unrelated cofactor binding, peroxidase, or membrane mannosyltransferase activities.


**Missing item-specific fact**

> The exact enzyme identity and experimentally tested substrate specificity are not supplied. Those would be needed to establish its particular physiological substrates, but are not necessary to favor the broad beta-glucosidase choice among these options.


**Reason**

> The sequence offers a defensible family-level biological signal that distinguishes the broad activity from the unrelated alternatives. The reviewer-only database identification and experimental annotation support the key, but are not being treated as information available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct functions, and the sequence's glycoside-hydrolase motif pattern supports A over the alternatives. More specific substrate-level claims would require additional evidence, but the selected option is broad.


### Important caveats

- The sequence match and cited experimental annotation support the answer, but the primary study was not independently retrieved or validated here.
- The exact author data snapshot is unknown; the historical entry and current entry both match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conserved catalytic-motif pattern characteristic of family-1 glycoside hydrolases, including an ENG motif, which supports a glucoside-hydrolyzing enzyme. Among the choices, beta-glucosidase activity is the compatible broad function; the other options describe unrelated cofactor binding, peroxidase, or membrane mannosyltransferase activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact enzyme identity and experimentally tested substrate specificity are not supplied. Those would be needed to establish its particular physiological substrates, but are not necessary to favor the broad beta-glucosidase choice among these options.",
    "reason": "The sequence offers a defensible family-level biological signal that distinguishes the broad activity from the unrelated alternatives. The reviewer-only database identification and experimental annotation support the key, but are not being treated as information available to the evaluated model."
  },
  "case_id": "GO_molecular_function_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 543-aa UniProt entry for Ipecac alkaloid beta-glucosidase 3. That entry reports beta-glucosidase activity and specific glucose-releasing reactions with experimental evidence attributed to a cited publication; its GO annotation is IDA. This supports choice A, while preserving that the evidence is an annotation reporting experimental findings rather than an independent review of the primary study."
  },
  "important_caveats": [
    "The sequence match and cited experimental annotation support the answer, but the primary study was not independently retrieved or validated here.",
    "The exact author data snapshot is unknown; the historical entry and current entry both match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct functions, and the sequence's glycoside-hydrolase motif pattern supports A over the alternatives. More specific substrate-level claims would require additional evidence, but the selected option is broad."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 543-aa UniProt entry for Ipecac alkaloid beta-glucosidase 3. That entry reports beta-glucosidase activity and specific glucose-releasing reactions with experimental evidence attributed to a cited publication; its GO annotation is IDA. This supports choice A, while preserving that the evidence is an annotation reporting experimental findings rather than an independent review of the primary study.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the conserved catalytic-motif pattern characteristic of family-1 glycoside hydrolases, including an ENG motif, which supports a glucoside-hydrolyzing enzyme. Among the choices, beta-glucosidase activity is the compatible broad function; the other options describe unrelated cofactor binding, peroxidase, or membrane mannosyltransferase activities.",
    "missing_item_specific_fact": "The exact enzyme identity and experimentally tested substrate specificity are not supplied. Those would be needed to establish its particular physiological substrates, but are not necessary to favor the broad beta-glucosidase choice among these options.",
    "reason": "The sequence offers a defensible family-level biological signal that distinguishes the broad activity from the unrelated alternatives. The reviewer-only database identification and experimental annotation support the key, but are not being treated as information available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct functions, and the sequence's glycoside-hydrolase motif pattern supports A over the alternatives. More specific substrate-level claims would require additional evidence, but the selected option is broad."
  },
  "important_caveats": [
    "The sequence match and cited experimental annotation support the answer, but the primary study was not independently retrieved or validated here.",
    "The exact author data snapshot is unknown; the historical entry and current entry both match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B6ZKM5 (GLU3_CARIP, Ipecac alkaloid beta-glucosidase 3) is annotated with GO:0008422 (beta-glucosidase activity) via IDA evidence from PubMed:18927081. The function comment explicitly states 'Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside,' and two catalytic activity reactions confirm hydrolysis of glycosidic bonds releasing D-glucose. The sequence match is confirmed (SHA-256 identical, 543 aa). The evidence is experimental (ECO:0000269, ECO:0000314), not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options span four distinct functional classes: (A) glycoside hydrolase, (B) cofactor binding, (C) peroxiredoxin/thioredoxin peroxidase, (D) glycosyltransferase. The supplied sequence (~543 aa) exhibits features consistent with a glycoside hydrolase TIM-barrel architecture: clustered aromatic residues (W, Y, F) in multiple stretches suggestive of a sugar-binding pocket, appropriate length for GH-family enzymes, and absence of the conserved peroxiredoxin TPxxC cysteine motif (eliminates C), absence of molybdopterin-binding domain signatures found in sulfite oxidase/xanthine dehydrogenase (eliminates B), and absence of GT-A/GT-B glycosyltransferase motifs (eliminates D). The remaining option A is the only glycosidase activity among the choices.


**Missing item-specific fact**

> Precise identification as beta-glucosidase (GO:0008422) rather than another GH1-family activity (e.g., alpha-glucosidase, beta-galactosidase) would require recognizing specific GH1 subfamily motifs or database lookup. However, since no alternative glycosidase is offered as a distractor, the elimination of the three non-hydrolase options is sufficient to select A.


**Reason**

> A knowledgeable model can eliminate B, C, and D by recognizing the absence of their hallmark domain features (Mo-co domain, peroxiredoxin fold, glycosyltransferase fold) and identify the sequence as consistent with a glycoside hydrolase based on fold architecture and aromatic-residue clustering. The positive assignment to 'beta-glucosidase' specifically is somewhat aided by general knowledge of plant GH1 beta-glucosidases but is primarily reached by elimination of clearly incompatible functional classes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular function classes (hydrolase, binding, peroxidase, transferase). The sequence lacks the defining features of options B, C, and D, leaving A as the only viable choice. No ambiguity among options is present.


### Important caveats

- The GO annotation evidence is experimental (IDA, ECO:0000314 from PubMed:18927081), providing strong support for the key.
- The protein is a plant-specific alkaloid beta-glucosidase; its substrate specificity (ipecac alkaloid glucosides) is narrower than the general GO term definition, but the molecular function (beta-glucosidase activity) is correctly assigned.
- The reasoning pathway relies primarily on elimination of incompatible functional classes rather than positive identification of GH1 beta-glucosidase catalytic motifs, which would be difficult to discern unambiguously from raw sequence alone.
- The UniProt entry was first publicly released in June 2025; the author's source snapshot date is unknown, though the sequence itself dates from 2009.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options span four distinct functional classes: (A) glycoside hydrolase, (B) cofactor binding, (C) peroxiredoxin/thioredoxin peroxidase, (D) glycosyltransferase. The supplied sequence (~543 aa) exhibits features consistent with a glycoside hydrolase TIM-barrel architecture: clustered aromatic residues (W, Y, F) in multiple stretches suggestive of a sugar-binding pocket, appropriate length for GH-family enzymes, and absence of the conserved peroxiredoxin TPxxC cysteine motif (eliminates C), absence of molybdopterin-binding domain signatures found in sulfite oxidase/xanthine dehydrogenase (eliminates B), and absence of GT-A/GT-B glycosyltransferase motifs (eliminates D). The remaining option A is the only glycosidase activity among the choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification as beta-glucosidase (GO:0008422) rather than another GH1-family activity (e.g., alpha-glucosidase, beta-galactosidase) would require recognizing specific GH1 subfamily motifs or database lookup. However, since no alternative glycosidase is offered as a distractor, the elimination of the three non-hydrolase options is sufficient to select A.",
    "reason": "A knowledgeable model can eliminate B, C, and D by recognizing the absence of their hallmark domain features (Mo-co domain, peroxiredoxin fold, glycosyltransferase fold) and identify the sequence as consistent with a glycoside hydrolase based on fold architecture and aromatic-residue clustering. The positive assignment to 'beta-glucosidase' specifically is somewhat aided by general knowledge of plant GH1 beta-glucosidases but is primarily reached by elimination of clearly incompatible functional classes."
  },
  "case_id": "GO_molecular_function_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H1",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B6ZKM5 (GLU3_CARIP, Ipecac alkaloid beta-glucosidase 3) is annotated with GO:0008422 (beta-glucosidase activity) via IDA evidence from PubMed:18927081. The function comment explicitly states 'Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside,' and two catalytic activity reactions confirm hydrolysis of glycosidic bonds releasing D-glucose. The sequence match is confirmed (SHA-256 identical, 543 aa). The evidence is experimental (ECO:0000269, ECO:0000314), not merely computational."
  },
  "important_caveats": [
    "The GO annotation evidence is experimental (IDA, ECO:0000314 from PubMed:18927081), providing strong support for the key.",
    "The protein is a plant-specific alkaloid beta-glucosidase; its substrate specificity (ipecac alkaloid glucosides) is narrower than the general GO term definition, but the molecular function (beta-glucosidase activity) is correctly assigned.",
    "The reasoning pathway relies primarily on elimination of incompatible functional classes rather than positive identification of GH1 beta-glucosidase catalytic motifs, which would be difficult to discern unambiguously from raw sequence alone.",
    "The UniProt entry was first publicly released in June 2025; the author's source snapshot date is unknown, though the sequence itself dates from 2009."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular function classes (hydrolase, binding, peroxidase, transferase). The sequence lacks the defining features of options B, C, and D, leaving A as the only viable choice. No ambiguity among options is present."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B6ZKM5 (GLU3_CARIP, Ipecac alkaloid beta-glucosidase 3) is annotated with GO:0008422 (beta-glucosidase activity) via IDA evidence from PubMed:18927081. The function comment explicitly states 'Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside,' and two catalytic activity reactions confirm hydrolysis of glycosidic bonds releasing D-glucose. The sequence match is confirmed (SHA-256 identical, 543 aa). The evidence is experimental (ECO:0000269, ECO:0000314), not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "H1", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options span four distinct functional classes: (A) glycoside hydrolase, (B) cofactor binding, (C) peroxiredoxin/thioredoxin peroxidase, (D) glycosyltransferase. The supplied sequence (~543 aa) exhibits features consistent with a glycoside hydrolase TIM-barrel architecture: clustered aromatic residues (W, Y, F) in multiple stretches suggestive of a sugar-binding pocket, appropriate length for GH-family enzymes, and absence of the conserved peroxiredoxin TPxxC cysteine motif (eliminates C), absence of molybdopterin-binding domain signatures found in sulfite oxidase/xanthine dehydrogenase (eliminates B), and absence of GT-A/GT-B glycosyltransferase motifs (eliminates D). The remaining option A is the only glycosidase activity among the choices.",
    "missing_item_specific_fact": "Precise identification as beta-glucosidase (GO:0008422) rather than another GH1-family activity (e.g., alpha-glucosidase, beta-galactosidase) would require recognizing specific GH1 subfamily motifs or database lookup. However, since no alternative glycosidase is offered as a distractor, the elimination of the three non-hydrolase options is sufficient to select A.",
    "reason": "A knowledgeable model can eliminate B, C, and D by recognizing the absence of their hallmark domain features (Mo-co domain, peroxiredoxin fold, glycosyltransferase fold) and identify the sequence as consistent with a glycoside hydrolase based on fold architecture and aromatic-residue clustering. The positive assignment to 'beta-glucosidase' specifically is somewhat aided by general knowledge of plant GH1 beta-glucosidases but is primarily reached by elimination of clearly incompatible functional classes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular function classes (hydrolase, binding, peroxidase, transferase). The sequence lacks the defining features of options B, C, and D, leaving A as the only viable choice. No ambiguity among options is present."
  },
  "important_caveats": [
    "The GO annotation evidence is experimental (IDA, ECO:0000314 from PubMed:18927081), providing strong support for the key.",
    "The protein is a plant-specific alkaloid beta-glucosidase; its substrate specificity (ipecac alkaloid glucosides) is narrower than the general GO term definition, but the molecular function (beta-glucosidase activity) is correctly assigned.",
    "The reasoning pathway relies primarily on elimination of incompatible functional classes rather than positive identification of GH1 beta-glucosidase catalytic motifs, which would be difficult to discern unambiguously from raw sequence alone.",
    "The UniProt entry was first publicly released in June 2025; the author's source snapshot date is unknown, though the sequence itself dates from 2009."
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

**Accession:** `B6ZKM5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
"B6ZKM5"
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"3.2.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Ipecac alkaloid beta-glucosidase 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"IpeGLU3"}]}}
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside"}]}
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:78764"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"name":"deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78763"},{"database":"ChEBI","id":"CHEBI:4167"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:58379"},{"database":"ChEBI","id":"CHEBI:229554"}]}}
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:78888"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"name":"deacetylisoipecoside + H2O = deacetylisoipecoside aglycone + D-glucose","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78887"},{"database":"ChEBI","id":"CHEBI:4167"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:58091"},{"database":"ChEBI","id":"CHEBI:229557"}]}}
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"18927081","source":"PubMed"}],"id":"GO:0008422","properties":[{"key":"GoTerm","value":"F:beta-glucosidase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
{"citation":{"authors":["Nomura T.","Quesada A.L.","Kutchan T.M."],"citationCrossReferences":[{"database":"PubMed","id":"18927081"},{"database":"DOI","id":"10.1074/jbc.m806953200"}],"citationType":"journal article","firstPage":"34650","id":"18927081","journal":"J. Biol. Chem.","lastPage":"34659","publicationDate":"2008","title":"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.","volume":"283"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAH02546.1","source":"EMBL"},{"evidenceCode":"ECO:0000312","id":"BAH02553.1","source":"EMBL"}],"referenceComments":[{"type":"TISSUE","value":"Root"},{"type":"TISSUE","value":"Shoot"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:27:26.233250+00:00.  

```text
ID   GLU3_CARIP              Reviewed;         543 AA.
AC   B6ZKM5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-FEB-2009, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Ipecac alkaloid beta-glucosidase 3 {ECO:0000303|PubMed:18927081};
DE            Short=IpeGLU3 {ECO:0000303|PubMed:18927081};
DE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};
GN   Name=GLU3 {ECO:0000303|PubMed:18927081};
OS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;
OC   Carapichea.
OX   NCBI_TaxID=77880;
```

Source SHA-256: `d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)  
**Locator:** `lines 24-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:27:26.233250+00:00.  

```text
CC   -!- FUNCTION: Beta-glucosidase catalyzing deglucosylation on N-
CC       deacetylisoipecoside and N-deacetylipecoside.
CC       {ECO:0000269|PubMed:18927081}.
```

Source SHA-256: `d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)  
**Locator:** `lines 27-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:27:26.233250+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=deacetylipecoside + H2O = deacetylipecoside aglycone + D-
CC         glucose; Xref=Rhea:RHEA:78763, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:58379, ChEBI:CHEBI:229554;
CC         Evidence={ECO:0000269|PubMed:18927081};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78764;
CC         Evidence={ECO:0000269|PubMed:18927081};
```

Source SHA-256: `d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:27:26.233250+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=deacetylisoipecoside + H2O = deacetylisoipecoside aglycone +
CC         D-glucose; Xref=Rhea:RHEA:78887, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:58091, ChEBI:CHEBI:229557;
CC         Evidence={ECO:0000269|PubMed:18927081};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78888;
CC         Evidence={ECO:0000269|PubMed:18927081};
```

Source SHA-256: `d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)  
**Locator:** `lines 54-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:27:26.233250+00:00.  

```text
DR   GO; GO:0008422; F:beta-glucosidase activity; IDA:UniProtKB.
```

Source SHA-256: `d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 179. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
