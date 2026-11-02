# GO_molecular_function_0013

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — cysteine-type peptidase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MARLSSIVFIICLLLCNNAISDEVIESPSSGGTLSGGGSGTDTVTGTQDGKGKSEGKGNEGGQTDQKGKENPENGQNSDSTGDSSLGSTGSNGSQPAPTTPKEPEPTTPKEPESATPKASEPVTPQKTAETASGKQVSPTPSENPPSKDTPKPESSSEKKVNSALATPPAPEVSKAQEGAGLATQKEQTPSKRAKRSPPPQVNNITDMESYLMKNYDGVKVIGLCGVYFRVQFSPHLLLYGLTTFSIIQIEPFFEGVRIDFEHQHPIRNKCAPGKAFAFISYVKDNILILKWKVFAPPSDLFANDEVSKQILSAVSVTSDAESSVVDVRKYRLPQLDRPFTSIQVYKANPKQGLLETKNYILKNAIPEKCSKISMNCFLNGNVNIENCFKCTLLVQNAKPTDECFQYLPSDMKNNLNEIKVTAQSDEDSKENDLIESIEILLNSFYKADKKAKKLSLITMDDFDDVLRAELFNYCKLLKELDTKKTLENAELGNEIDIFNNLLRLLKTNEEESKHNLYKKLRNTAICLKDVNKWAEKKRGLILPEEVTQDQMAIGQNEEPYDEDPDDRVDLLELFDDNQNENIVDKDGIIDMSIAIKYAKLKSPYFNSSKYCNYEYCDRWQDKTSCISNIDVEEQGNCSLCWLFASKLHLETIRCMRGYGHNRSSALYVANCSKRTAEEICNDGSNPLEFLKILEKNKFLPLESNYPYLWKNVSGKCPNPQNDWTNLWGNTKLLYNNMFGQFIKHRGYIVYSSRFFAKNMNVFIDIIKREIRNKGSVIAYIKTQGVIDYDFNGRYISNICGHNHPDHAVNIIGYGNYISESGEKRSYWLIRNSWGYYWGHEGNFKVDVLGPDNCVHNVIHTAIVFKIDMEPDSDSNNNNAIKNRDQLIDEDNKSYFPQLSSNFYHSLYYNNYEGYEAKNDDENDQNYGNLDVSGQSENHQNDPKNPQPQANSTVTQLGVCPAENQRTADSNPNAQSTPSPNTTVTDTVNSNTANSNTANSNTASANAASIEKKIQILHVLKHIEKYKMTRGFVKYDNLNDTKNDYTCARSYSYDPKNHNECKQFCEENWERCKNHYSPGYCLTTLSGKNKCLFCYV

[Multiple Choices]
A. cysteine-type peptidase activity
B. glycosaminoglycan binding
C. peptidyl-lysine 3-dioxygenase activity
D. dolichyl-phosphate-mannose-protein mannosyltransferase activity
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

> The exact sequence matches the Plasmodium berghei SERA3 record, which describes the protein as a putative cysteine protease and assigns cysteine-type peptidase activity. The GO assignment is computational (IEA:InterPro), so it supports the key but is not itself experimental validation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal signal peptide and large soluble protein are compatible with a secreted parasite antigen, but do not by themselves establish cysteine-type peptidase activity or distinguish an active protease from a related inactive protein.


**Missing item-specific fact**

> The SERA3-specific protease-family/domain assignment and evidence that this protein is a putative cysteine protease are not supplied in the question.


**Reason**

> The sequence may support computational family recognition, but the functional distinction relies on a protein-specific annotation or domain interpretation not made unambiguous by general biological reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence specifically supports option A; no other listed activity is supported for this sequence.


### Important caveats

- The function is described as putative.
- The GO annotation uses IEA:InterPro evidence, and the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal signal peptide and large soluble protein are compatible with a secreted parasite antigen, but do not by themselves establish cysteine-type peptidase activity or distinguish an active protease from a related inactive protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The SERA3-specific protease-family/domain assignment and evidence that this protein is a putative cysteine protease are not supplied in the question.",
    "reason": "The sequence may support computational family recognition, but the functional distinction relies on a protein-specific annotation or domain interpretation not made unambiguous by general biological reasoning from the provided input."
  },
  "case_id": "GO_molecular_function_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium berghei SERA3 record, which describes the protein as a putative cysteine protease and assigns cysteine-type peptidase activity. The GO assignment is computational (IEA:InterPro), so it supports the key but is not itself experimental validation."
  },
  "important_caveats": [
    "The function is described as putative.",
    "The GO annotation uses IEA:InterPro evidence, and the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence specifically supports option A; no other listed activity is supported for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium berghei SERA3 record, which describes the protein as a putative cysteine protease and assigns cysteine-type peptidase activity. The GO assignment is computational (IEA:InterPro), so it supports the key but is not itself experimental validation.",
    "evidence_ids": ["C1", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal signal peptide and large soluble protein are compatible with a secreted parasite antigen, but do not by themselves establish cysteine-type peptidase activity or distinguish an active protease from a related inactive protein.",
    "missing_item_specific_fact": "The SERA3-specific protease-family/domain assignment and evidence that this protein is a putative cysteine protease are not supplied in the question.",
    "reason": "The sequence may support computational family recognition, but the functional distinction relies on a protein-specific annotation or domain interpretation not made unambiguous by general biological reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence specifically supports option A; no other listed activity is supported for this sequence."
  },
  "important_caveats": [
    "The function is described as putative.",
    "The GO annotation uses IEA:InterPro evidence, and the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A509AC44 (SERA3_PLABA, sequence matched at 1096 AA) explicitly annotates GO:0008234 (cysteine-type peptidase activity) with evidence code IEA:InterPro (C6/H5), and the FUNCTION comment states 'Putative cysteine protease' supported by experimental evidence ECO:0000269|PubMed:30941868 (C5/H4). The 'putative' qualifier and IEA evidence code indicate the assignment is based on domain similarity (InterPro) corroborated by experimental functional context, rather than direct enzymatic assay of this specific protein. Nevertheless, the annotation directly supports choice A.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable papain-like cysteine protease domain: the motif 'CGHNHPDHAVNIIGYGNY' exhibits the canonical Cys-Gly-His-Asn arrangement of the papain superfamily catalytic triad (Cys nucleophile, His general base, Asn stabilizer). Additionally, the SERA (Serine-Repeat Antigen) family in Plasmodium is a well-known biological case where proteins named for serine-rich repeats actually possess cysteine protease catalytic machinery (the catalytic serine is replaced by cysteine). Recognizing the papain-like C.GH…HPD motif from the sequence and knowing the SERA family paradox provides concrete grounds to select cysteine-type peptidase activity over the unrelated binding (B), oxidase (C), or transferase (D) options.


**Missing item-specific fact**

> None strictly required; the papain-like domain architecture is identifiable from the sequence, and the SERA-family cysteine-protease biology is general parasitology knowledge. The IEA:InterPro evidence code confirms the domain-based annotation logic is consistent with sequence-level reasoning.


**Reason**

> The sequence displays a papain-like cysteine protease catalytic motif (CGHNHPD pattern with downstream conserved residues), and the SERA family's well-documented 'named serine, functions as cysteine protease' biology provides a reasoning pathway. The four options span entirely different GO branches (peptidase, binding, oxidase, transferase), so identifying the protease domain suffices to exclude B, C, and D without needing to memorize the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular function classes (peptidase, binding, dioxygenase, transferase). The presence of a papain-like catalytic domain in the sequence clearly points to peptidase activity and excludes the other three. No ambiguity among options.


### Important caveats

- The GO annotation is IEA:InterPro (computational), and the FUNCTION comment uses 'Putative cysteine protease,' indicating the assignment is not from a direct enzyme assay of SERA3 itself but from domain inference plus experimental context (PubMed:30941868).
- The SERA family nomenclature is historically misleading: 'serine-repeat' refers to a non-catalytic serine-rich region, while the catalytic residue is cysteine. This is a well-known feature of Plasmodium SERA biology but could confuse a model relying solely on the protein name.
- The protein is from Plasmodium berghei (strain Anka), a parasitic protist; the functional context (merozoite release from parasitophorous vacuole) is specific to liver-stage biology.
- Sequence match confirmed at both current (v27) and historical (v26) UniProt snapshots; benchmark sequence SHA256 matches source.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable papain-like cysteine protease domain: the motif 'CGHNHPDHAVNIIGYGNY' exhibits the canonical Cys-Gly-His-Asn arrangement of the papain superfamily catalytic triad (Cys nucleophile, His general base, Asn stabilizer). Additionally, the SERA (Serine-Repeat Antigen) family in Plasmodium is a well-known biological case where proteins named for serine-rich repeats actually possess cysteine protease catalytic machinery (the catalytic serine is replaced by cysteine). Recognizing the papain-like C.GH…HPD motif from the sequence and knowing the SERA family paradox provides concrete grounds to select cysteine-type peptidase activity over the unrelated binding (B), oxidase (C), or transferase (D) options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; the papain-like domain architecture is identifiable from the sequence, and the SERA-family cysteine-protease biology is general parasitology knowledge. The IEA:InterPro evidence code confirms the domain-based annotation logic is consistent with sequence-level reasoning.",
    "reason": "The sequence displays a papain-like cysteine protease catalytic motif (CGHNHPD pattern with downstream conserved residues), and the SERA family's well-documented 'named serine, functions as cysteine protease' biology provides a reasoning pathway. The four options span entirely different GO branches (peptidase, binding, oxidase, transferase), so identifying the protease domain suffices to exclude B, C, and D without needing to memorize the specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A509AC44 (SERA3_PLABA, sequence matched at 1096 AA) explicitly annotates GO:0008234 (cysteine-type peptidase activity) with evidence code IEA:InterPro (C6/H5), and the FUNCTION comment states 'Putative cysteine protease' supported by experimental evidence ECO:0000269|PubMed:30941868 (C5/H4). The 'putative' qualifier and IEA evidence code indicate the assignment is based on domain similarity (InterPro) corroborated by experimental functional context, rather than direct enzymatic assay of this specific protein. Nevertheless, the annotation directly supports choice A."
  },
  "important_caveats": [
    "The GO annotation is IEA:InterPro (computational), and the FUNCTION comment uses 'Putative cysteine protease,' indicating the assignment is not from a direct enzyme assay of SERA3 itself but from domain inference plus experimental context (PubMed:30941868).",
    "The SERA family nomenclature is historically misleading: 'serine-repeat' refers to a non-catalytic serine-rich region, while the catalytic residue is cysteine. This is a well-known feature of Plasmodium SERA biology but could confuse a model relying solely on the protein name.",
    "The protein is from Plasmodium berghei (strain Anka), a parasitic protist; the functional context (merozoite release from parasitophorous vacuole) is specific to liver-stage biology.",
    "Sequence match confirmed at both current (v27) and historical (v26) UniProt snapshots; benchmark sequence SHA256 matches source."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular function classes (peptidase, binding, dioxygenase, transferase). The presence of a papain-like catalytic domain in the sequence clearly points to peptidase activity and excludes the other three. No ambiguity among options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A509AC44 (SERA3_PLABA, sequence matched at 1096 AA) explicitly annotates GO:0008234 (cysteine-type peptidase activity) with evidence code IEA:InterPro (C6/H5), and the FUNCTION comment states 'Putative cysteine protease' supported by experimental evidence ECO:0000269|PubMed:30941868 (C5/H4). The 'putative' qualifier and IEA evidence code indicate the assignment is based on domain similarity (InterPro) corroborated by experimental functional context, rather than direct enzymatic assay of this specific protein. Nevertheless, the annotation directly supports choice A.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable papain-like cysteine protease domain: the motif 'CGHNHPDHAVNIIGYGNY' exhibits the canonical Cys-Gly-His-Asn arrangement of the papain superfamily catalytic triad (Cys nucleophile, His general base, Asn stabilizer). Additionally, the SERA (Serine-Repeat Antigen) family in Plasmodium is a well-known biological case where proteins named for serine-rich repeats actually possess cysteine protease catalytic machinery (the catalytic serine is replaced by cysteine). Recognizing the papain-like C.GH…HPD motif from the sequence and knowing the SERA family paradox provides concrete grounds to select cysteine-type peptidase activity over the unrelated binding (B), oxidase (C), or transferase (D) options.",
    "missing_item_specific_fact": "None strictly required; the papain-like domain architecture is identifiable from the sequence, and the SERA-family cysteine-protease biology is general parasitology knowledge. The IEA:InterPro evidence code confirms the domain-based annotation logic is consistent with sequence-level reasoning.",
    "reason": "The sequence displays a papain-like cysteine protease catalytic motif (CGHNHPD pattern with downstream conserved residues), and the SERA family's well-documented 'named serine, functions as cysteine protease' biology provides a reasoning pathway. The four options span entirely different GO branches (peptidase, binding, oxidase, transferase), so identifying the protease domain suffices to exclude B, C, and D without needing to memorize the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular function classes (peptidase, binding, dioxygenase, transferase). The presence of a papain-like catalytic domain in the sequence clearly points to peptidase activity and excludes the other three. No ambiguity among options."
  },
  "important_caveats": [
    "The GO annotation is IEA:InterPro (computational), and the FUNCTION comment uses 'Putative cysteine protease,' indicating the assignment is not from a direct enzyme assay of SERA3 itself but from domain inference plus experimental context (PubMed:30941868).",
    "The SERA family nomenclature is historically misleading: 'serine-repeat' refers to a non-catalytic serine-rich region, while the catalytic residue is cysteine. This is a well-known feature of Plasmodium SERA biology but could confuse a model relying solely on the protein name.",
    "The protein is from Plasmodium berghei (strain Anka), a parasitic protist; the functional context (merozoite release from parasitophorous vacuole) is specific to liver-stage biology.",
    "Sequence match confirmed at both current (v27) and historical (v26) UniProt snapshots; benchmark sequence SHA256 matches source."
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

**Accession:** `A0A509AC44` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.524185+00:00.  

```json
"A0A509AC44"
```

Source SHA-256: `5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.524185+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30941868","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"30941868","source":"PubMed"}],"value":"Putative cysteine protease (PubMed:30941868). Probably involved in merozoite release from the parasitophorous vacuole during liver stages (PubMed:30941868)"}]}
```

Source SHA-256: `5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.524185+00:00.  

```json
{"database":"GO","id":"GO:0008234","properties":[{"key":"GoTerm","value":"F:cysteine-type peptidase activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)  
**Locator:** `lines 51-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:26.529482+00:00.  

```text
CC   -!- FUNCTION: Putative cysteine protease (PubMed:30941868). Probably
CC       involved in merozoite release from the parasitophorous vacuole during
CC       liver stages (PubMed:30941868). {ECO:0000269|PubMed:30941868,
CC       ECO:0000303|PubMed:30941868}.
```

Source SHA-256: `35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)  
**Locator:** `lines 91-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:26.529482+00:00.  

```text
DR   GO; GO:0008234; F:cysteine-type peptidase activity; IEA:InterPro.
```

Source SHA-256: `35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 80941-80955`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008234
name: cysteine-type peptidase activity
namespace: molecular_function
alt_id: GO:0004220
def: "Catalysis of the hydrolysis of peptide bonds in a polypeptide chain by a mechanism in which the sulfhydryl group of a cysteine residue at the active center acts as a nucleophile." [GOC:mah, https://www.ebi.ac.uk/merops/about/glossary.shtml#CATTYPE]
synonym: "cysteine protease activity" NARROW []
synonym: "thiol protease activity" NARROW []
xref: Reactome:R-HSA-2022381 "Cathepsin Z (Cathepsin X) hydrolyzes AGT(25-34) (Angiotensin-(1-10)) to AGT(25-32) (Angiotensin-(1-8))"
xref: Reactome:R-HSA-2467775 "Autocleavage of ESPL1 (Separase)"
xref: Reactome:R-HSA-2467809 "ESPL1 (Separase) cleaves centromeric cohesin"
xref: Reactome:R-HSA-5660752 "USP9X deubiquitinates Ub-SNCA"
xref: Reactome:R-HSA-9757951 "CASP8 cleaves N4BP1 at D424, D490"
is_a: GO:0008233 ! peptidase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 13. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
