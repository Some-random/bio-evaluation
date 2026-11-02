# GO_biological_process_0077

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — heparan sulfate proteoglycan biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGLLRIMMPPKLQLLAVVAFAVAMLFLENQIQKLEESRAKLERAIARHEVREIEQRHTMDGPRQDAAVDEEEDIVIIYNRVPKTASTSFTNIAYDLCAKNRYHVLHINTTKNNPVMSLQDQVRFVKNITTWNEMKPGFYHGHISYLDFAKFGVKKKPIYINVIRDPIERLVSYYYFLRFGDDYRPGLRRRKQGDKKTFDECVAEGGSDCAPEKLWLQIPFFCGHSSECWNVGSRWAMDQAKYNLINEYFLVGVTEELEDFIMLLEAALPRFFRGATDLYRTGKKSHLRKTTEKKLPTKQTIAKLQQSDIWKMENEFYEFALEQFQFIRAHAVREKDGDLYILAQNFFYEKIYPKSN

[Multiple Choices]
A. defense response to tumor cell
B. lipid biosynthetic process
C. viral RNA genome replication
D. heparan sulfate proteoglycan biosynthetic process
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

> The exact sequence matches a UniProt entry annotated as heparan sulfate 2-O-sulfotransferase, whose stated function is to transfer sulfate within heparan sulfate and participate in its biosynthesis. The corresponding GO annotation is heparan sulfate proteoglycan biosynthetic process, although that GO annotation is computationally assigned.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a membrane-anchored enzyme, and sulfotransferase-like catalytic features could suggest modification of a cellular substrate. Those clues do not establish that the substrate is heparan sulfate rather than another substrate.


**Missing item-specific fact**

> The protein-specific identification as heparan sulfate 2-O-sulfotransferase, including its substrate specificity, is not supplied in the question.


**Reason**

> The sequence may support an enzyme-family inference, but selecting the precise heparan sulfate biosynthetic process depends on the absent substrate-specific assignment. The other options are not enough to establish that assignment from the input alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is supported by the matched protein annotation and stated enzymatic function; the supplied evidence does not support another listed process as a comparable choice.


### Important caveats

- The GO annotation for D is marked IEA:Ensembl, a computational annotation.
- The function description combines evidence by similarity with a cited experimental study; the supplied excerpts do not establish that the cited experiment was performed on this Chinese hamster protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a membrane-anchored enzyme, and sulfotransferase-like catalytic features could suggest modification of a cellular substrate. Those clues do not establish that the substrate is heparan sulfate rather than another substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as heparan sulfate 2-O-sulfotransferase, including its substrate specificity, is not supplied in the question.",
    "reason": "The sequence may support an enzyme-family inference, but selecting the precise heparan sulfate biosynthetic process depends on the absent substrate-specific assignment. The other options are not enough to establish that assignment from the input alone."
  },
  "case_id": "GO_biological_process_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as heparan sulfate 2-O-sulfotransferase, whose stated function is to transfer sulfate within heparan sulfate and participate in its biosynthesis. The corresponding GO annotation is heparan sulfate proteoglycan biosynthetic process, although that GO annotation is computationally assigned."
  },
  "important_caveats": [
    "The GO annotation for D is marked IEA:Ensembl, a computational annotation.",
    "The function description combines evidence by similarity with a cited experimental study; the supplied excerpts do not establish that the cited experiment was performed on this Chinese hamster protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is supported by the matched protein annotation and stated enzymatic function; the supplied evidence does not support another listed process as a comparable choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as heparan sulfate 2-O-sulfotransferase, whose stated function is to transfer sulfate within heparan sulfate and participate in its biosynthesis. The corresponding GO annotation is heparan sulfate proteoglycan biosynthetic process, although that GO annotation is computationally assigned.",
    "evidence_ids": ["C1", "C5", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a membrane-anchored enzyme, and sulfotransferase-like catalytic features could suggest modification of a cellular substrate. Those clues do not establish that the substrate is heparan sulfate rather than another substrate.",
    "missing_item_specific_fact": "The protein-specific identification as heparan sulfate 2-O-sulfotransferase, including its substrate specificity, is not supplied in the question.",
    "reason": "The sequence may support an enzyme-family inference, but selecting the precise heparan sulfate biosynthetic process depends on the absent substrate-specific assignment. The other options are not enough to establish that assignment from the input alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is supported by the matched protein annotation and stated enzymatic function; the supplied evidence does not support another listed process as a comparable choice."
  },
  "important_caveats": [
    "The GO annotation for D is marked IEA:Ensembl, a computational annotation.",
    "The function description combines evidence by similarity with a cited experimental study; the supplied excerpts do not establish that the cited experiment was performed on this Chinese hamster protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A8C2LVE3 (HS2ST_CRIGR), annotated as Heparan sulfate 2-O-sulfotransferase 1. The FUNCTION comment (C5/H3) states it 'participates in HS biosynthesis' and catalyzes sulfation of iduronic/glucuronic acid within the heparan sulfate chain, supported by experimental evidence (PubMed:17227754, ECO:0000269). The GO annotation GO:0015012 (heparan sulfate proteoglycan biosynthetic process) is assigned to this entry (H5, IEA:Ensembl). The GO term definition (GO3) explicitly includes sulfation of HS chains as part of HS proteoglycan biosynthesis. The expected answer D is directly supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmarks of a Golgi-resident type II membrane sulfotransferase: an N-terminal hydrophobic signal/transmembrane anchor (MGLLRIMMPPKLQLLAVVAFAVAMLFLEN), a small overall size (~356 aa), and conserved motifs consistent with the sulfotransferase fold (e.g., PAPS-binding region with 'GXG' and conserved His/Arg residues). This enzyme class modifies glycosaminoglycan chains in the Golgi. Among the four choices, only D (heparan sulfate proteoglycan biosynthetic process) is compatible with a Golgi sulfotransferase acting on a carbohydrate polymer. Option A (defense response to tumor cell) requires immune-signaling architecture absent here; B (lipid biosynthetic process) requires acyltransferase or lipid-synthase domains absent here; C (viral RNA genome replication) requires RNA-dependent polymerase motifs entirely absent here. Thus, recognizing the enzyme class from sequence architecture is sufficient to eliminate A, B, and C.


**Missing item-specific fact**

> Specifically distinguishing heparan sulfate 2-O-sulfotransferase from chondroitin sulfate 2-O-sulfotransferase or other GAG sulfotransferases would require substrate-specific knowledge or database lookup. However, no alternative GAG option is presented among the choices, so this distinction does not affect answer selection.


**Reason**

> The sequence architecture (signal peptide, transmembrane anchor, sulfotransferase-like fold, small Golgi-enzyme size) provides grounds to identify the protein as a glycosaminoglycan-modifying transferase. Once this class is recognized, the three distractors are categorically incompatible with any sulfotransferase, leaving D as the only viable option. This constitutes a meaningful biological reasoning pathway from sequence features to answer, even though the precise substrate (heparan sulfate vs. other GAGs) would require additional domain knowledge not strictly needed to eliminate the other choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are categorically incompatible with a Golgi-resident sulfotransferase modifying glycosaminoglycans. No alternative GAG biosynthesis option is present that could compete with D. The answer is unambiguous given the enzyme class.


### Important caveats

- The GO annotation GO:0015012 on this entry is IEA (Inferred from Electronic Annotation via Ensembl), not an independent experimental GO assignment. However, the underlying FUNCTION annotation is supported by experimental evidence (PubMed:17227754, ECO:0000269).
- The protein name and much of the annotation derive by similarity (ECO:0000250) from mouse/rat orthologs Q8R3H7 and Q7LGA3, though the mutational study (PubMed:17227754) provides direct experimental support for the catalytic function.
- The specific identification of 'heparan sulfate' (as opposed to chondroitin sulfate) as the substrate would require additional sequence-specific knowledge beyond general sulfotransferase recognition, but this does not affect the answer given the available choices.
- The UniProt entry was first public in Feb 2025; the benchmark author's source snapshot is unknown. Sequence match is confirmed across versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmarks of a Golgi-resident type II membrane sulfotransferase: an N-terminal hydrophobic signal/transmembrane anchor (MGLLRIMMPPKLQLLAVVAFAVAMLFLEN), a small overall size (~356 aa), and conserved motifs consistent with the sulfotransferase fold (e.g., PAPS-binding region with 'GXG' and conserved His/Arg residues). This enzyme class modifies glycosaminoglycan chains in the Golgi. Among the four choices, only D (heparan sulfate proteoglycan biosynthetic process) is compatible with a Golgi sulfotransferase acting on a carbohydrate polymer. Option A (defense response to tumor cell) requires immune-signaling architecture absent here; B (lipid biosynthetic process) requires acyltransferase or lipid-synthase domains absent here; C (viral RNA genome replication) requires RNA-dependent polymerase motifs entirely absent here. Thus, recognizing the enzyme class from sequence architecture is sufficient to eliminate A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Specifically distinguishing heparan sulfate 2-O-sulfotransferase from chondroitin sulfate 2-O-sulfotransferase or other GAG sulfotransferases would require substrate-specific knowledge or database lookup. However, no alternative GAG option is presented among the choices, so this distinction does not affect answer selection.",
    "reason": "The sequence architecture (signal peptide, transmembrane anchor, sulfotransferase-like fold, small Golgi-enzyme size) provides grounds to identify the protein as a glycosaminoglycan-modifying transferase. Once this class is recognized, the three distractors are categorically incompatible with any sulfotransferase, leaving D as the only viable option. This constitutes a meaningful biological reasoning pathway from sequence features to answer, even though the precise substrate (heparan sulfate vs. other GAGs) would require additional domain knowledge not strictly needed to eliminate the other choices."
  },
  "case_id": "GO_biological_process_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A8C2LVE3 (HS2ST_CRIGR), annotated as Heparan sulfate 2-O-sulfotransferase 1. The FUNCTION comment (C5/H3) states it 'participates in HS biosynthesis' and catalyzes sulfation of iduronic/glucuronic acid within the heparan sulfate chain, supported by experimental evidence (PubMed:17227754, ECO:0000269). The GO annotation GO:0015012 (heparan sulfate proteoglycan biosynthetic process) is assigned to this entry (H5, IEA:Ensembl). The GO term definition (GO3) explicitly includes sulfation of HS chains as part of HS proteoglycan biosynthesis. The expected answer D is directly supported."
  },
  "important_caveats": [
    "The GO annotation GO:0015012 on this entry is IEA (Inferred from Electronic Annotation via Ensembl), not an independent experimental GO assignment. However, the underlying FUNCTION annotation is supported by experimental evidence (PubMed:17227754, ECO:0000269).",
    "The protein name and much of the annotation derive by similarity (ECO:0000250) from mouse/rat orthologs Q8R3H7 and Q7LGA3, though the mutational study (PubMed:17227754) provides direct experimental support for the catalytic function.",
    "The specific identification of 'heparan sulfate' (as opposed to chondroitin sulfate) as the substrate would require additional sequence-specific knowledge beyond general sulfotransferase recognition, but this does not affect the answer given the available choices.",
    "The UniProt entry was first public in Feb 2025; the benchmark author's source snapshot is unknown. Sequence match is confirmed across versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are categorically incompatible with a Golgi-resident sulfotransferase modifying glycosaminoglycans. No alternative GAG biosynthesis option is present that could compete with D. The answer is unambiguous given the enzyme class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A8C2LVE3 (HS2ST_CRIGR), annotated as Heparan sulfate 2-O-sulfotransferase 1. The FUNCTION comment (C5/H3) states it 'participates in HS biosynthesis' and catalyzes sulfation of iduronic/glucuronic acid within the heparan sulfate chain, supported by experimental evidence (PubMed:17227754, ECO:0000269). The GO annotation GO:0015012 (heparan sulfate proteoglycan biosynthetic process) is assigned to this entry (H5, IEA:Ensembl). The GO term definition (GO3) explicitly includes sulfation of HS chains as part of HS proteoglycan biosynthesis. The expected answer D is directly supported.",
    "evidence_ids": ["C4", "C5", "H3", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmarks of a Golgi-resident type II membrane sulfotransferase: an N-terminal hydrophobic signal/transmembrane anchor (MGLLRIMMPPKLQLLAVVAFAVAMLFLEN), a small overall size (~356 aa), and conserved motifs consistent with the sulfotransferase fold (e.g., PAPS-binding region with 'GXG' and conserved His/Arg residues). This enzyme class modifies glycosaminoglycan chains in the Golgi. Among the four choices, only D (heparan sulfate proteoglycan biosynthetic process) is compatible with a Golgi sulfotransferase acting on a carbohydrate polymer. Option A (defense response to tumor cell) requires immune-signaling architecture absent here; B (lipid biosynthetic process) requires acyltransferase or lipid-synthase domains absent here; C (viral RNA genome replication) requires RNA-dependent polymerase motifs entirely absent here. Thus, recognizing the enzyme class from sequence architecture is sufficient to eliminate A, B, and C.",
    "missing_item_specific_fact": "Specifically distinguishing heparan sulfate 2-O-sulfotransferase from chondroitin sulfate 2-O-sulfotransferase or other GAG sulfotransferases would require substrate-specific knowledge or database lookup. However, no alternative GAG option is presented among the choices, so this distinction does not affect answer selection.",
    "reason": "The sequence architecture (signal peptide, transmembrane anchor, sulfotransferase-like fold, small Golgi-enzyme size) provides grounds to identify the protein as a glycosaminoglycan-modifying transferase. Once this class is recognized, the three distractors are categorically incompatible with any sulfotransferase, leaving D as the only viable option. This constitutes a meaningful biological reasoning pathway from sequence features to answer, even though the precise substrate (heparan sulfate vs. other GAGs) would require additional domain knowledge not strictly needed to eliminate the other choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are categorically incompatible with a Golgi-resident sulfotransferase modifying glycosaminoglycans. No alternative GAG biosynthesis option is present that could compete with D. The answer is unambiguous given the enzyme class."
  },
  "important_caveats": [
    "The GO annotation GO:0015012 on this entry is IEA (Inferred from Electronic Annotation via Ensembl), not an independent experimental GO assignment. However, the underlying FUNCTION annotation is supported by experimental evidence (PubMed:17227754, ECO:0000269).",
    "The protein name and much of the annotation derive by similarity (ECO:0000250) from mouse/rat orthologs Q8R3H7 and Q7LGA3, though the mutational study (PubMed:17227754) provides direct experimental support for the catalytic function.",
    "The specific identification of 'heparan sulfate' (as opposed to chondroitin sulfate) as the substrate would require additional sequence-specific knowledge beyond general sulfotransferase recognition, but this does not affect the answer given the available choices.",
    "The UniProt entry was first public in Feb 2025; the benchmark author's source snapshot is unknown. Sequence match is confirmed across versions."
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

**Accession:** `A0A8C2LVE3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:56.866768+00:00.  

```json
"A0A8C2LVE3"
```

Source SHA-256: `0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:56.866768+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"}],"value":"2-O-sulfotransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"}],"value":"2-OST"},{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q76KB1","source":"UniProtKB"}],"value":"2OST"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"}],"value":"HS 2-O-sulfotransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"}],"value":"Heparan sulfate 2-sulfotransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"}],"value":"2.8.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q7LGA3","source":"UniProtKB"}],"value":"Heparan sulfate 2-O-sulfotransferase 1"}}}
```

Source SHA-256: `0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:56.866768+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"17227754","source":"PubMed"}],"value":"Catalyzes the transfer of a sulfo group from 3'-phospho-5'-adenylyl sulfate (PAPS) to the 2-OH position of iduronic acid (IdoA) or glucuronic acid (GlcA) within the heparan sulfate (HS) chain and participates in HS biosynthesis (PubMed:17227754). Required for metanephric development of kidney formation, suggesting that 2-O-sulfation within HS is essential for signaling between ureteric bud and metanephric mesenchyme (By similarity)"}]}
```

Source SHA-256: `0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)  
**Locator:** `lines 45-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.260576+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the transfer of a sulfo group from 3'-phospho-5'-
CC       adenylyl sulfate (PAPS) to the 2-OH position of iduronic acid (IdoA) or
CC       glucuronic acid (GlcA) within the heparan sulfate (HS) chain and
CC       participates in HS biosynthesis (PubMed:17227754). Required for
CC       metanephric development of kidney formation, suggesting that 2-O-
CC       sulfation within HS is essential for signaling between ureteric bud and
CC       metanephric mesenchyme (By similarity). {ECO:0000250|UniProtKB:Q8R3H7,
CC       ECO:0000269|PubMed:17227754}.
```

Source SHA-256: `c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)  
**Locator:** `lines 77-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.260576+00:00.  

```text
DR   GO; GO:0015012; P:heparan sulfate proteoglycan biosynthetic process; IEA:Ensembl.
```

Source SHA-256: `c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 113352-113369`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0015012
name: heparan sulfate proteoglycan biosynthetic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the formation of heparan sulfate proteoglycans, which consist of a core protein linked to a heparan sulfate glycosaminoglycan. The heparan sulfate chain is composed of the repeating disaccharide unit beta-(1,4)-N-acetyl-D-glucosamine-alpha-(1,4)-hexuronic acid, the former being either sulfated or deacetylated on its amino group as well as sulfated on one of its hydroxyl groups, and the latter being e a mixture of sulfated and nonsulfated D-glucuronic and L-iduronic acids. Heparan sulfate chains are covalently linked to serine/threonine residues (O-linked) of the core protein via a tetrasaccharide linker sequence (xylose-galactose-galactose-glucuronate)." [PMID:27241222]
synonym: "heparan sulfate proteoglycan anabolism" EXACT []
synonym: "heparan sulfate proteoglycan biosynthesis" EXACT []
synonym: "heparan sulfate proteoglycan formation" EXACT []
synonym: "heparan sulfate proteoglycan synthesis" EXACT []
synonym: "heparan sulphate proteoglycan biosynthesis" EXACT []
synonym: "heparan sulphate proteoglycan biosynthetic process" EXACT []
synonym: "heparin proteoglycan biosynthetic process" RELATED []
xref: MetaCyc:PWY-6558
xref: Reactome:R-HSA-2022928 "HS-GAG biosynthesis"
is_a: GO:0030166 ! proteoglycan biosynthetic process
is_a: GO:0030201 ! heparan sulfate proteoglycan metabolic process
is_a: GO:0180064 ! protein O-linked glycosylation via xylose

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 77. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
