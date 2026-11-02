# catalytic_activity_0009

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — 2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDNISNHAFNYPVLVLNKGLLPEHDDIALARYLFSALALAVSRITQNEEMIVGFHLHPQEITRWKDDECIRQYILPLNIRFNSATPIAGFIREIMTWMTPDAIHQKNAMGASVLTLGPQHALHDIFDLEISWQPPVESEPVQALTCHVASREDALVLTLRFNPARFSATQMQKLPEVWRQITASAAKNGAETLRDIGLIDDAERQRVLHAFNQTEQAWDGETTVAARLKNRAQRHPEQTAVVFRDETLSYRQLYQQAGALAHYLNALETERERCVGLFVEPSLTLMTGVWGILLSGNAYLPLSPEYPEDRLAYMLENSQTRIIVTQPHLRERLLALAPPGIQVVTSDDVDAFMRQHAHSLPDAPQNDIAPHHLAYVIYTSGSTGKPKGVMIEHHSVLNQMNWLAQTVGLNQETVILQKTPMSFDAAQWEILSPACGCRVVMGEPGVYRNPEQLVDMLAEYRVTTLQCVPTLLQALLDTERLTHCPALRQIFSGGEALQKHLAQACLETLPDCELINLYGPTECTINNSAFRVDPVSVRQGPDTLSIGAPVANTRYYILDNCLTPVAVGQIGELYIGGDGVARGYLNRDDLTAERFIVDPFAPAGSGRRLYQTGDIASWNPDGTVQYAGRADNQVKLRGYRVELDEIRSAIETHEWVKAAAVIVRNDPFTGYQNLISFIELNAREAALMDQGNHGSHHQSKADKAQVMLQLANKGCREFPAASQPYTLDLPGKQPDEKQRLTAFSRKTYRFYDGGAVSREDILSLLHEPLLTAISRQPDALTLDELGHWLRYLGQFTSAERLLPKYTYASPGALYATQVFLELNGVAGLTAGHYYYQPVHHQLVRVSEQAAVTPGSLRLHFVGKKSAIEPIYKNNIREVLQMEMGHIIGMLDIILPDYGLGVALCDAAALDPTPLAIDLDDDYLGACDVLSGPRLPTDDDLDIYVQTAGANIADLPVGTYRYVRGDLQHIADDVIDKKHVIAINQAVYERSSFGISVASRTEGWAGYVHVGRKLQRLQMNPLNIGLMSSGYSSETGNDLPAARRFWQILGHRTGPYYFFIGGRISDEQKYSEGMREDAVHMKGPAEMIRDDLAAFMPDYMMPNKVLILDEMPLTANGKIDMKALANINVELKHKTIVAPRNPLEHQVMAIWQAKLKREEMSVDDNFFESGGNSLIAVSLINELNATLNASLPLQVLFQAPTVEKLAAWLSRARREPVSRLVQLQPKGRQAPIYCWPGLGGYCMNLRLLARQLGAERPFFGIQAHGINPDETPYATIGEMAARDIELIRQHQPHGPYTLWGYSFGARVAFETAWQLELAGEVVENLYLLAPGSPKLRDERVAAMNRKADFDNPGYLTILFSVFIGSITDPELERCLETVRDEESFVAFITGLNPALDDGLVRRITRIVAQTFEFTYTFSELQQRQLNAPVTIIKAQGDDYSFIENHGGFSAQPPTVLELMADHYSMLKAPGIDELTSVIQYQQSPPSLVG

[Multiple Choices]
A. pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)
B. enterobactin + 3 H2O = 3 N-(2,3-dihydroxybenzoyl)-L-serine + 2 H(+)
C. 2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O
D. a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in mRNA + ADP + phosphate + CoA + H(+)
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

> The supplied sequence exactly matches the 1488-aa UniProt entry for indigoidine synthase, and that entry annotates the reaction in choice C, citing a paper on the protein's function. This supports the key, though the cited annotation is curated evidence rather than an independently reviewed assay here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a large protein, consistent broadly with a biosynthetic enzyme, but that general feature does not identify indigoidine synthesis or distinguish it from the specific reactions in the other choices.


**Missing item-specific fact**

> The protein's identity or functional annotation as indigoidine synthase, or equivalent protein-specific experimental evidence, is absent from the input.


**Reason**

> Choosing C requires knowing this sequence's particular enzyme function; the reviewer-only sequence-matched annotation supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reactions, and the sequence-matched annotation supports choice C.


### Important caveats

- The current and historical UniProt entries match the supplied sequence; the annotation cites a 2002 paper, but that primary study was not independently retrieved or validated here.
- The exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a large protein, consistent broadly with a biosynthetic enzyme, but that general feature does not identify indigoidine synthesis or distinguish it from the specific reactions in the other choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity or functional annotation as indigoidine synthase, or equivalent protein-specific experimental evidence, is absent from the input.",
    "reason": "Choosing C requires knowing this sequence's particular enzyme function; the reviewer-only sequence-matched annotation supports the key but was not supplied to the evaluated model."
  },
  "case_id": "catalytic_activity_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1488-aa UniProt entry for indigoidine synthase, and that entry annotates the reaction in choice C, citing a paper on the protein's function. This supports the key, though the cited annotation is curated evidence rather than an independently reviewed assay here."
  },
  "important_caveats": [
    "The current and historical UniProt entries match the supplied sequence; the annotation cites a 2002 paper, but that primary study was not independently retrieved or validated here.",
    "The exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the sequence-matched annotation supports choice C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1488-aa UniProt entry for indigoidine synthase, and that entry annotates the reaction in choice C, citing a paper on the protein's function. This supports the key, though the cited annotation is curated evidence rather than an independently reviewed assay here.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a large protein, consistent broadly with a biosynthetic enzyme, but that general feature does not identify indigoidine synthesis or distinguish it from the specific reactions in the other choices.",
    "missing_item_specific_fact": "The protein's identity or functional annotation as indigoidine synthase, or equivalent protein-specific experimental evidence, is absent from the input.",
    "reason": "Choosing C requires knowing this sequence's particular enzyme function; the reviewer-only sequence-matched annotation supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the sequence-matched annotation supports choice C."
  },
  "important_caveats": [
    "The current and historical UniProt entries match the supplied sequence; the annotation cites a 2002 paper, but that primary study was not independently retrieved or validated here.",
    "The exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9L391 (sequence SHA256 matched, 1488 aa) is annotated as Indigoidine synthase (EC 4.3.3.9) from Dickeya dadantii 3937. The curated catalytic activity (C5, H4) reads exactly: '2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O', matching choice C verbatim. The evidence code is ECO:0000305 (curator inference) supported by PubMed:11790734 (Reverchon et al. 2002, J. Bacteriol.), which characterized the indC gene as encoding indigoidine synthase. The reaction is further decomposed into two half-reactions (C6, C7) consistent with the overall equation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark adenylation (A) domain motif 'TSGSTGK' (≈residue 500) and associated A-domain features ('YGPTEC', 'GAPVAN'), plus a putative NAD(P)-dependent reductase domain ('NDPFTGY', 'GYSFGA'). This multi-domain architecture is diagnostic of a non-ribosomal peptide synthetase (NRPS) or NRPS-like enzyme. NRPS enzymes catalyze amino-acid activation and condensation using ATP and, in reductase-type modules, a flavin cofactor (FMN/FAD) and O2. Among the four choices, only C describes an NRPS-type condensation/oxidation reaction (FMN + L-glutamine + ATP + O2 → indigoidine). Choices A and B describe hydrolase (esterase/amidase) reactions on small-molecule substrates, and D describes an acetyltransferase modifying RNA. The presence of NRPS domain motifs therefore provides a concrete, general-biochemistry argument that excludes A, B, and D and points to C.


**Missing item-specific fact**

> While the NRPS architecture narrows the enzyme class, the specific identification of the product as 'indigoidine' and the cofactor as FMN (rather than FAD or NADPH) is a protein-specific detail. However, among the four provided choices, no other option is consistent with NRPS chemistry, so the domain-architecture argument is sufficient to select C without memorizing the exact UniProt entry.


**Reason**

> The SGSTGK adenylation motif and reductase-domain features are general, widely-taught biochemistry knowledge (not sequence-identity lookup). Recognizing an NRPS-type enzyme and knowing that NRPS enzymes catalyze amino-acid condensation with ATP/flavin/O2 is sufficient to eliminate the three hydrolase/acetyltransferase distractors and select the single NRPS-type reaction (C). This constitutes a meaningful biological argument derivable from the sequence and general knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A (pyrrolizixenacetamide hydrolase), B (enterobactin esterase), and D (N4-acetylcytidine acetyltransferase) describe enzyme classes fundamentally incompatible with the NRPS domain architecture present in the sequence. Only C is mechanistically consistent with a flavin-dependent NRPS-like condensation enzyme. No ambiguity remains among the four options.


### Important caveats

- The UniProt annotation evidence code is ECO:0000305 (curator inference from PubMed:11790734), not direct in-vitro enzymatic assay of the purified protein; the 2002 paper characterized gene function by heterologous expression and pigment phenotype.
- The entry was first public in UniProt on 2025-02-05 (sequence version 2); the author's construction date is unknown, so the annotation may not have existed at benchmark-creation time, though the underlying biology (indC = indigoidine synthase) was published in 2002.
- The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence-recognizable domain motifs and general NRPS biochemistry.
- The specific product name 'indigoidine' and cofactor 'FMN' are protein-specific facts; the reasoning argument narrows to the NRPS reaction class but does not independently derive the exact product name from first principles.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark adenylation (A) domain motif 'TSGSTGK' (≈residue 500) and associated A-domain features ('YGPTEC', 'GAPVAN'), plus a putative NAD(P)-dependent reductase domain ('NDPFTGY', 'GYSFGA'). This multi-domain architecture is diagnostic of a non-ribosomal peptide synthetase (NRPS) or NRPS-like enzyme. NRPS enzymes catalyze amino-acid activation and condensation using ATP and, in reductase-type modules, a flavin cofactor (FMN/FAD) and O2. Among the four choices, only C describes an NRPS-type condensation/oxidation reaction (FMN + L-glutamine + ATP + O2 → indigoidine). Choices A and B describe hydrolase (esterase/amidase) reactions on small-molecule substrates, and D describes an acetyltransferase modifying RNA. The presence of NRPS domain motifs therefore provides a concrete, general-biochemistry argument that excludes A, B, and D and points to C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "While the NRPS architecture narrows the enzyme class, the specific identification of the product as 'indigoidine' and the cofactor as FMN (rather than FAD or NADPH) is a protein-specific detail. However, among the four provided choices, no other option is consistent with NRPS chemistry, so the domain-architecture argument is sufficient to select C without memorizing the exact UniProt entry.",
    "reason": "The SGSTGK adenylation motif and reductase-domain features are general, widely-taught biochemistry knowledge (not sequence-identity lookup). Recognizing an NRPS-type enzyme and knowing that NRPS enzymes catalyze amino-acid condensation with ATP/flavin/O2 is sufficient to eliminate the three hydrolase/acetyltransferase distractors and select the single NRPS-type reaction (C). This constitutes a meaningful biological argument derivable from the sequence and general knowledge."
  },
  "case_id": "catalytic_activity_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9L391 (sequence SHA256 matched, 1488 aa) is annotated as Indigoidine synthase (EC 4.3.3.9) from Dickeya dadantii 3937. The curated catalytic activity (C5, H4) reads exactly: '2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O', matching choice C verbatim. The evidence code is ECO:0000305 (curator inference) supported by PubMed:11790734 (Reverchon et al. 2002, J. Bacteriol.), which characterized the indC gene as encoding indigoidine synthase. The reaction is further decomposed into two half-reactions (C6, C7) consistent with the overall equation."
  },
  "important_caveats": [
    "The UniProt annotation evidence code is ECO:0000305 (curator inference from PubMed:11790734), not direct in-vitro enzymatic assay of the purified protein; the 2002 paper characterized gene function by heterologous expression and pigment phenotype.",
    "The entry was first public in UniProt on 2025-02-05 (sequence version 2); the author's construction date is unknown, so the annotation may not have existed at benchmark-creation time, though the underlying biology (indC = indigoidine synthase) was published in 2002.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence-recognizable domain motifs and general NRPS biochemistry.",
    "The specific product name 'indigoidine' and cofactor 'FMN' are protein-specific facts; the reasoning argument narrows to the NRPS reaction class but does not independently derive the exact product name from first principles."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A (pyrrolizixenacetamide hydrolase), B (enterobactin esterase), and D (N4-acetylcytidine acetyltransferase) describe enzyme classes fundamentally incompatible with the NRPS domain architecture present in the sequence. Only C is mechanistically consistent with a flavin-dependent NRPS-like condensation enzyme. No ambiguity remains among the four options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9L391 (sequence SHA256 matched, 1488 aa) is annotated as Indigoidine synthase (EC 4.3.3.9) from Dickeya dadantii 3937. The curated catalytic activity (C5, H4) reads exactly: '2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O', matching choice C verbatim. The evidence code is ECO:0000305 (curator inference) supported by PubMed:11790734 (Reverchon et al. 2002, J. Bacteriol.), which characterized the indC gene as encoding indigoidine synthase. The reaction is further decomposed into two half-reactions (C6, C7) consistent with the overall equation.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark adenylation (A) domain motif 'TSGSTGK' (≈residue 500) and associated A-domain features ('YGPTEC', 'GAPVAN'), plus a putative NAD(P)-dependent reductase domain ('NDPFTGY', 'GYSFGA'). This multi-domain architecture is diagnostic of a non-ribosomal peptide synthetase (NRPS) or NRPS-like enzyme. NRPS enzymes catalyze amino-acid activation and condensation using ATP and, in reductase-type modules, a flavin cofactor (FMN/FAD) and O2. Among the four choices, only C describes an NRPS-type condensation/oxidation reaction (FMN + L-glutamine + ATP + O2 → indigoidine). Choices A and B describe hydrolase (esterase/amidase) reactions on small-molecule substrates, and D describes an acetyltransferase modifying RNA. The presence of NRPS domain motifs therefore provides a concrete, general-biochemistry argument that excludes A, B, and D and points to C.",
    "missing_item_specific_fact": "While the NRPS architecture narrows the enzyme class, the specific identification of the product as 'indigoidine' and the cofactor as FMN (rather than FAD or NADPH) is a protein-specific detail. However, among the four provided choices, no other option is consistent with NRPS chemistry, so the domain-architecture argument is sufficient to select C without memorizing the exact UniProt entry.",
    "reason": "The SGSTGK adenylation motif and reductase-domain features are general, widely-taught biochemistry knowledge (not sequence-identity lookup). Recognizing an NRPS-type enzyme and knowing that NRPS enzymes catalyze amino-acid condensation with ATP/flavin/O2 is sufficient to eliminate the three hydrolase/acetyltransferase distractors and select the single NRPS-type reaction (C). This constitutes a meaningful biological argument derivable from the sequence and general knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A (pyrrolizixenacetamide hydrolase), B (enterobactin esterase), and D (N4-acetylcytidine acetyltransferase) describe enzyme classes fundamentally incompatible with the NRPS domain architecture present in the sequence. Only C is mechanistically consistent with a flavin-dependent NRPS-like condensation enzyme. No ambiguity remains among the four options."
  },
  "important_caveats": [
    "The UniProt annotation evidence code is ECO:0000305 (curator inference from PubMed:11790734), not direct in-vitro enzymatic assay of the purified protein; the 2002 paper characterized gene function by heterologous expression and pigment phenotype.",
    "The entry was first public in UniProt on 2025-02-05 (sequence version 2); the author's construction date is unknown, so the annotation may not have existed at benchmark-creation time, though the underlying biology (indC = indigoidine synthase) was published in 2002.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence-recognizable domain motifs and general NRPS biochemistry.",
    "The specific product name 'indigoidine' and cofactor 'FMN' are protein-specific facts; the reasoning argument narrows to the NRPS reaction class but does not independently derive the exact product name from first principles."
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

**Accession:** `Q9L391` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 107. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
"Q9L391"
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"11790734","source":"PubMed"}],"value":"4.3.3.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Indigoidine synthase"}}}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"11790734","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81500"}}],"reaction":{"ecNumber":"4.3.3.9","evidences":[{"evidenceCode":"ECO:0000305","id":"11790734","source":"PubMed"}],"name":"2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81499"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:58359"},{"database":"ChEBI","id":"CHEBI:79296"},{"database":"ChEBI","id":"CHEBI:456215"}]}}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q1MWN4","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81504"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q1MWN4","source":"UniProtKB"}],"name":"FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-dione + FMNH2 + AMP + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81503"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:58359"},{"database":"ChEBI","id":"CHEBI:231893"},{"database":"ChEBI","id":"CHEBI:456215"}]}}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q1MWN4","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81508"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q1MWN4","source":"UniProtKB"}],"name":"2 3-amino-1,5-dihydropyridine-2,6-dione + O2 = indigoidine + 2 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81507"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:79296"},{"database":"ChEBI","id":"CHEBI:231893"}]}}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"citation":{"authors":["Reverchon S.","Rouanet C.","Expert D.","Nasser W."],"citationCrossReferences":[{"database":"PubMed","id":"11790734"},{"database":"DOI","id":"10.1128/jb.184.3.654-665.2002"}],"citationType":"journal article","firstPage":"654","id":"11790734","journal":"J. Bacteriol.","lastPage":"665","publicationDate":"2002","title":"Characterization of indigoidine biosynthetic genes in Erwinia chrysanthemi and role of this blue pigment in pathogenicity.","volume":"184"},"evidences":[{"evidenceCode":"ECO:0000312","id":"CAB87990.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"3937"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION AS AN INDIGOIDINE SYNTHASE","PATHWAY","INDUCTION","DOMAIN"]}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 2.  
**Retrieved:** 2026-11-02T04:33:06.750542+00:00.  

```text
DE   RecName: Full=Indigoidine synthase {ECO:0000305};
DE            EC=4.3.3.9 {ECO:0000305|PubMed:11790734};
```

Source SHA-256: `8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)  
**Locator:** `lines 44-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 2.  
**Retrieved:** 2026-11-02T04:33:06.750542+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2
CC         AMP + 2 diphosphate + 2 H2O; Xref=Rhea:RHEA:81499, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:30616, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:58359,
CC         ChEBI:CHEBI:79296, ChEBI:CHEBI:456215; EC=4.3.3.9;
CC         Evidence={ECO:0000305|PubMed:11790734};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81500;
CC         Evidence={ECO:0000305|PubMed:11790734};
```

Source SHA-256: `8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
