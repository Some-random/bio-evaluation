# pathway_0112

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKSPLKLYFLPYISPGHMIPLSEMARLFANQGHHVTIITTTSNATLLQKYTTATLSLHLIPLPTKEAGLPDGLENFISVNDLETAGKLYYALSLLQPVIEEFITSNPPDCIVSDMFYPWTADLASQLQVPRMVFHAACIFAMCMKESMRGPDAPHLKVSSDYELFEVKGLPDPVFMTRAQLPDYVRTPNGYTQLMEMWREAEKKSYGVMVNNFYELDPAYTEHYSKIMGHKVWNIGPAAQILHRGSGDKIERVHKAVVGENQCLSWLDTKEPNSVFYVCFGSAIRFPDDQLYEIASALESSGAQFIWAVLGKDSDNSDSNSDSEWLPAGFEEKMKETGRGMIIRGWAPQVLILDHPSVGGFMTHCGWNSTIEGVSAGVGMVTWPLYAEQFYNEKLITQVLKIGVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGGSSHRNLMALIEDLQRIRDDKMSKVAN

[Multiple Choices]
A. Secondary metabolite biosynthesis
B. Pyrimidine metabolism
C. protein glycosylation. .
D. LPS O-antigen biosynthesis. .
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

> The supplied sequence exactly matches the UniProt entry for UDP-glucosyl transferase 73CC6, whose pathway annotation is secondary metabolite biosynthesis (including terpenoid biosynthesis). The annotation is linked to a publication with experimental evidence; this supports choice A, though it does not independently establish every detail of the underlying experiments.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a UDP-dependent glycosyltransferase, but that general activity does not identify its biological substrate or pathway. It therefore does not establish that this enzyme acts in secondary-metabolite biosynthesis rather than another glycosylation context.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental finding that this enzyme participates in secondary-metabolite, particularly terpenoid/saponin, biosynthesis.


**Reason**

> That pathway assignment is supported by reviewer-only database evidence, but the needed substrate and pathway information is not supplied in the question. Recognizing the exact protein or recalling its annotation would be lookup or memorization, not reasoning from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone leaves the pathway assignment underdetermined, but the reviewer-only evidence supports A; it does not make another listed option comparably supported.


### Important caveats

- The sequence match is exact, and the historical UniProt record also contains the pathway annotation.
- The database annotation is linked to experimental evidence, but the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a UDP-dependent glycosyltransferase, but that general activity does not identify its biological substrate or pathway. It therefore does not establish that this enzyme acts in secondary-metabolite biosynthesis rather than another glycosylation context.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this enzyme participates in secondary-metabolite, particularly terpenoid/saponin, biosynthesis.",
    "reason": "That pathway assignment is supported by reviewer-only database evidence, but the needed substrate and pathway information is not supplied in the question. Recognizing the exact protein or recalling its annotation would be lookup or memorization, not reasoning from the input."
  },
  "case_id": "pathway_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for UDP-glucosyl transferase 73CC6, whose pathway annotation is secondary metabolite biosynthesis (including terpenoid biosynthesis). The annotation is linked to a publication with experimental evidence; this supports choice A, though it does not independently establish every detail of the underlying experiments."
  },
  "important_caveats": [
    "The sequence match is exact, and the historical UniProt record also contains the pathway annotation.",
    "The database annotation is linked to experimental evidence, but the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone leaves the pathway assignment underdetermined, but the reviewer-only evidence supports A; it does not make another listed option comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for UDP-glucosyl transferase 73CC6, whose pathway annotation is secondary metabolite biosynthesis (including terpenoid biosynthesis). The annotation is linked to a publication with experimental evidence; this supports choice A, though it does not independently establish every detail of the underlying experiments.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a UDP-dependent glycosyltransferase, but that general activity does not identify its biological substrate or pathway. It therefore does not establish that this enzyme acts in secondary-metabolite biosynthesis rather than another glycosylation context.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this enzyme participates in secondary-metabolite, particularly terpenoid/saponin, biosynthesis.",
    "reason": "That pathway assignment is supported by reviewer-only database evidence, but the needed substrate and pathway information is not supplied in the question. Recognizing the exact protein or recalling its annotation would be lookup or memorization, not reasoning from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone leaves the pathway assignment underdetermined, but the reviewer-only evidence supports A; it does not make another listed option comparably supported."
  },
  "important_caveats": [
    "The sequence match is exact, and the historical UniProt record also contains the pathway annotation.",
    "The database annotation is linked to experimental evidence, but the primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAW1J9R8 (SoUGT73CC6, a UDP-glucosyl transferase from Saponaria officinalis) is explicitly annotated with the pathway 'Secondary metabolite biosynthesis; terpenoid biosynthesis' under evidence code ECO:0000269 (inferred from direct assay, PubMed:39043959). The protein catalyzes glycosylation of triterpenoid saponin intermediates, which are secondary metabolites. The expected answer 'Secondary metabolite biosynthesis' matches the UniProt pathway annotation exactly.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H3](#evidence-h3), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence contains the PSPG (Plant Secondary Product Glycosyltransferase) motif (e.g., 'GVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGGSSHRNLMALIEDLQRIRDDKMSKVAN'), which is the hallmark of plant UDP-glycosyltransferases. Plant UGTs are overwhelmingly involved in secondary metabolite biosynthesis (glycosylating triterpenoids, flavonoids, phenylpropanoids, etc.), making option A the natural pathway assignment. The other options can be eliminated by enzyme-family mismatch: pyrimidine metabolism enzymes (carbamoyl phosphate synthetase, dihydroorotate dehydrogenase, etc.) have entirely different folds and catalytic mechanisms; protein glycosylation involves oligosaccharyltransferases and Golgi-resident glycosyltransferases with distinct architectures; LPS O-antigen biosynthesis is a bacterial pathway inconsistent with the plant-like sequence features.


**Missing item-specific fact**

> The specific sub-pathway (terpenoid/saponin biosynthesis) and the exact acceptor substrate require experimental characterization (PubMed:39043959). However, the question only asks for the broad pathway category, for which the general association of plant UGTs with secondary metabolite biosynthesis suffices.


**Reason**

> A knowledgeable model can identify the PSPG motif, recognize the protein as a plant UGT, and apply the well-established general principle that plant UGTs function in secondary metabolite biosynthesis. The remaining three options are eliminated by clear enzyme-family and organism-context mismatches. The reasoning does not require memorizing this particular protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct biological processes (secondary metabolism, nucleotide metabolism, protein modification, bacterial cell-wall synthesis) that map to very different enzyme families. The PSPG motif and plant-UGT architecture uniquely point to option A. Option C ('protein glycosylation') might superficially attract attention due to the word 'glycosyl' in 'glycosyltransferase,' but protein glycosylation specifically refers to co/post-translational modification of proteins by OST/Golgi machinery, not small-molecule glycosylation by UGTs.


### Important caveats

- The UniProt pathway annotation is experimentally supported (ECO:0000269) but was published in 2025 (PubMed:39043959); the entry was first public in June 2025. Depending on the author's data-construction date, this annotation may or may not have been available at benchmark creation time.
- The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence features and general biological knowledge.
- The broad category 'Secondary metabolite biosynthesis' is well-supported for plant UGTs in general, but the specific terpenoid/saponin sub-pathway would require item-specific knowledge of this enzyme's substrate.
- The sequence-match between the benchmark sequence and UniProt A0AAW1J9R8 is confirmed (SHA-256 match, 487 aa).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence contains the PSPG (Plant Secondary Product Glycosyltransferase) motif (e.g., 'GVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGGSSHRNLMALIEDLQRIRDDKMSKVAN'), which is the hallmark of plant UDP-glycosyltransferases. Plant UGTs are overwhelmingly involved in secondary metabolite biosynthesis (glycosylating triterpenoids, flavonoids, phenylpropanoids, etc.), making option A the natural pathway assignment. The other options can be eliminated by enzyme-family mismatch: pyrimidine metabolism enzymes (carbamoyl phosphate synthetase, dihydroorotate dehydrogenase, etc.) have entirely different folds and catalytic mechanisms; protein glycosylation involves oligosaccharyltransferases and Golgi-resident glycosyltransferases with distinct architectures; LPS O-antigen biosynthesis is a bacterial pathway inconsistent with the plant-like sequence features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific sub-pathway (terpenoid/saponin biosynthesis) and the exact acceptor substrate require experimental characterization (PubMed:39043959). However, the question only asks for the broad pathway category, for which the general association of plant UGTs with secondary metabolite biosynthesis suffices.",
    "reason": "A knowledgeable model can identify the PSPG motif, recognize the protein as a plant UGT, and apply the well-established general principle that plant UGTs function in secondary metabolite biosynthesis. The remaining three options are eliminated by clear enzyme-family and organism-context mismatches. The reasoning does not require memorizing this particular protein's database entry."
  },
  "case_id": "pathway_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H3",
      "C6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1J9R8 (SoUGT73CC6, a UDP-glucosyl transferase from Saponaria officinalis) is explicitly annotated with the pathway 'Secondary metabolite biosynthesis; terpenoid biosynthesis' under evidence code ECO:0000269 (inferred from direct assay, PubMed:39043959). The protein catalyzes glycosylation of triterpenoid saponin intermediates, which are secondary metabolites. The expected answer 'Secondary metabolite biosynthesis' matches the UniProt pathway annotation exactly."
  },
  "important_caveats": [
    "The UniProt pathway annotation is experimentally supported (ECO:0000269) but was published in 2025 (PubMed:39043959); the entry was first public in June 2025. Depending on the author's data-construction date, this annotation may or may not have been available at benchmark creation time.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence features and general biological knowledge.",
    "The broad category 'Secondary metabolite biosynthesis' is well-supported for plant UGTs in general, but the specific terpenoid/saponin sub-pathway would require item-specific knowledge of this enzyme's substrate.",
    "The sequence-match between the benchmark sequence and UniProt A0AAW1J9R8 is confirmed (SHA-256 match, 487 aa)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct biological processes (secondary metabolism, nucleotide metabolism, protein modification, bacterial cell-wall synthesis) that map to very different enzyme families. The PSPG motif and plant-UGT architecture uniquely point to option A. Option C ('protein glycosylation') might superficially attract attention due to the word 'glycosyl' in 'glycosyltransferase,' but protein glycosylation specifically refers to co/post-translational modification of proteins by OST/Golgi machinery, not small-molecule glycosylation by UGTs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1J9R8 (SoUGT73CC6, a UDP-glucosyl transferase from Saponaria officinalis) is explicitly annotated with the pathway 'Secondary metabolite biosynthesis; terpenoid biosynthesis' under evidence code ECO:0000269 (inferred from direct assay, PubMed:39043959). The protein catalyzes glycosylation of triterpenoid saponin intermediates, which are secondary metabolites. The expected answer 'Secondary metabolite biosynthesis' matches the UniProt pathway annotation exactly.",
    "evidence_ids": ["C5", "C4", "H3", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence contains the PSPG (Plant Secondary Product Glycosyltransferase) motif (e.g., 'GVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGGSSHRNLMALIEDLQRIRDDKMSKVAN'), which is the hallmark of plant UDP-glycosyltransferases. Plant UGTs are overwhelmingly involved in secondary metabolite biosynthesis (glycosylating triterpenoids, flavonoids, phenylpropanoids, etc.), making option A the natural pathway assignment. The other options can be eliminated by enzyme-family mismatch: pyrimidine metabolism enzymes (carbamoyl phosphate synthetase, dihydroorotate dehydrogenase, etc.) have entirely different folds and catalytic mechanisms; protein glycosylation involves oligosaccharyltransferases and Golgi-resident glycosyltransferases with distinct architectures; LPS O-antigen biosynthesis is a bacterial pathway inconsistent with the plant-like sequence features.",
    "missing_item_specific_fact": "The specific sub-pathway (terpenoid/saponin biosynthesis) and the exact acceptor substrate require experimental characterization (PubMed:39043959). However, the question only asks for the broad pathway category, for which the general association of plant UGTs with secondary metabolite biosynthesis suffices.",
    "reason": "A knowledgeable model can identify the PSPG motif, recognize the protein as a plant UGT, and apply the well-established general principle that plant UGTs function in secondary metabolite biosynthesis. The remaining three options are eliminated by clear enzyme-family and organism-context mismatches. The reasoning does not require memorizing this particular protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct biological processes (secondary metabolism, nucleotide metabolism, protein modification, bacterial cell-wall synthesis) that map to very different enzyme families. The PSPG motif and plant-UGT architecture uniquely point to option A. Option C ('protein glycosylation') might superficially attract attention due to the word 'glycosyl' in 'glycosyltransferase,' but protein glycosylation specifically refers to co/post-translational modification of proteins by OST/Golgi machinery, not small-molecule glycosylation by UGTs."
  },
  "important_caveats": [
    "The UniProt pathway annotation is experimentally supported (ECO:0000269) but was published in 2025 (PubMed:39043959); the entry was first public in June 2025. Depending on the author's data-construction date, this annotation may or may not have been available at benchmark creation time.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence features and general biological knowledge.",
    "The broad category 'Secondary metabolite biosynthesis' is well-supported for plant UGTs in general, but the specific terpenoid/saponin sub-pathway would require item-specific knowledge of this enzyme's substrate.",
    "The sequence-match between the benchmark sequence and UniProt A0AAW1J9R8 is confirmed (SHA-256 match, 487 aa)."
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

**Accession:** `A0AAW1J9R8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.561717+00:00.  

```json
"A0AAW1J9R8"
```

Source SHA-256: `d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.561717+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"2.4.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"UDP-glucosyl transferase 73CC6"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoUGT73CC6"}]}}
```

Source SHA-256: `d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.561717+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.561717+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48156.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5)  
**Locator:** `lines 50-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.480726+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `9a59059b7ffd1f6c1fad31864cf878dfa9b156b29abca47f100f1fefa03ca58c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
