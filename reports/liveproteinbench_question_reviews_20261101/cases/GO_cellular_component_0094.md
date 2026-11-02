# GO_cellular_component_0094

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MARLSSIVFIICLLLCNNAISDEVIESPSSGGTLSGGGSGTDTVTGTQDGKGKSEGKGNEGGQTDQKGKENPENGQNSDSTGDSSLGSTGSNGSQPAPTTPKEPEPTTPKEPESATPKASEPVTPQKTAETASGKQVSPTPSENPPSKDTPKPESSSEKKVNSALATPPAPEVSKAQEGAGLATQKEQTPSKRAKRSPPPQVNNITDMESYLMKNYDGVKVIGLCGVYFRVQFSPHLLLYGLTTFSIIQIEPFFEGVRIDFEHQHPIRNKCAPGKAFAFISYVKDNILILKWKVFAPPSDLFANDEVSKQILSAVSVTSDAESSVVDVRKYRLPQLDRPFTSIQVYKANPKQGLLETKNYILKNAIPEKCSKISMNCFLNGNVNIENCFKCTLLVQNAKPTDECFQYLPSDMKNNLNEIKVTAQSDEDSKENDLIESIEILLNSFYKADKKAKKLSLITMDDFDDVLRAELFNYCKLLKELDTKKTLENAELGNEIDIFNNLLRLLKTNEEESKHNLYKKLRNTAICLKDVNKWAEKKRGLILPEEVTQDQMAIGQNEEPYDEDPDDRVDLLELFDDNQNENIVDKDGIIDMSIAIKYAKLKSPYFNSSKYCNYEYCDRWQDKTSCISNIDVEEQGNCSLCWLFASKLHLETIRCMRGYGHNRSSALYVANCSKRTAEEICNDGSNPLEFLKILEKNKFLPLESNYPYLWKNVSGKCPNPQNDWTNLWGNTKLLYNNMFGQFIKHRGYIVYSSRFFAKNMNVFIDIIKREIRNKGSVIAYIKTQGVIDYDFNGRYISNICGHNHPDHAVNIIGYGNYISESGEKRSYWLIRNSWGYYWGHEGNFKVDVLGPDNCVHNVIHTAIVFKIDMEPDSDSNNNNAIKNRDQLIDEDNKSYFPQLSSNFYHSLYYNNYEGYEAKNDDENDQNYGNLDVSGQSENHQNDPKNPQPQANSTVTQLGVCPAENQRTADSNPNAQSTPSPNTTVTDTVNSNTANSNTANSNTASANAASIEKKIQILHVLKHIEKYKMTRGFVKYDNLNDTKNDYTCARSYSYDPKNHNECKQFCEENWERCKNHYSPGYCLTTLSGKNKCLFCYV

[Multiple Choices]
A. peptidoglycan-based cell wall
B. plasma membrane
C. perinuclear region of cytoplasm
D. kinetoplast
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates cell membrane localization, corresponding to plasma membrane (B). This is similarity-transferred evidence, not direct experimental confirmation of the protein's primary location; the record also lists other locations.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a signal peptide and a secretory route, making a cell-surface destination plausible and the bacterial cell-wall and kinetoplast choices poor fits. That signal alone does not establish plasma membrane residence or that it is the primary location.


**Missing item-specific fact**

> Protein-specific localization or trafficking evidence establishing plasma membrane localization and prioritizing it over secretion or other destinations.


**Reason**

> The sequence supports a broad secretory-pathway inference, but distinguishing the specific primary compartment requires protein-specific information absent from the input. The supporting database annotation is reviewer-only and similarity-transferred.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotation lists multiple locations, but among the offered choices only plasma membrane is explicitly supported; host cytoplasm does not specifically establish the perinuclear region.


### Important caveats

- The membrane annotation is transferred by similarity and should not be presented as direct experimental evidence for this sequence.
- The evidence supports plasma membrane as a location but does not rank it as the protein's primary location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide and a secretory route, making a cell-surface destination plausible and the bacterial cell-wall and kinetoplast choices poor fits. That signal alone does not establish plasma membrane residence or that it is the primary location.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Protein-specific localization or trafficking evidence establishing plasma membrane localization and prioritizing it over secretion or other destinations.",
    "reason": "The sequence supports a broad secretory-pathway inference, but distinguishing the specific primary compartment requires protein-specific information absent from the input. The supporting database annotation is reviewer-only and similarity-transferred."
  },
  "case_id": "GO_cellular_component_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H4",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates cell membrane localization, corresponding to plasma membrane (B). This is similarity-transferred evidence, not direct experimental confirmation of the protein's primary location; the record also lists other locations."
  },
  "important_caveats": [
    "The membrane annotation is transferred by similarity and should not be presented as direct experimental evidence for this sequence.",
    "The evidence supports plasma membrane as a location but does not rank it as the protein's primary location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation lists multiple locations, but among the offered choices only plasma membrane is explicitly supported; host cytoplasm does not specifically establish the perinuclear region."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates cell membrane localization, corresponding to plasma membrane (B). This is similarity-transferred evidence, not direct experimental confirmation of the protein's primary location; the record also lists other locations.",
    "evidence_ids": ["C5", "C8", "H4", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide and a secretory route, making a cell-surface destination plausible and the bacterial cell-wall and kinetoplast choices poor fits. That signal alone does not establish plasma membrane residence or that it is the primary location.",
    "missing_item_specific_fact": "Protein-specific localization or trafficking evidence establishing plasma membrane localization and prioritizing it over secretion or other destinations.",
    "reason": "The sequence supports a broad secretory-pathway inference, but distinguishing the specific primary compartment requires protein-specific information absent from the input. The supporting database annotation is reviewer-only and similarity-transferred."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation lists multiple locations, but among the offered choices only plasma membrane is explicitly supported; host cytoplasm does not specifically establish the perinuclear region."
  },
  "important_caveats": [
    "The membrane annotation is transferred by similarity and should not be presented as direct experimental evidence for this sequence.",
    "The evidence supports plasma membrane as a location but does not rank it as the protein's primary location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A509AC44 (P. berghei SERA3) explicitly annotates GO:0005886 (plasma membrane) as a cellular component (C8/H7), and the subcellular location comment lists 'Cell membrane; Peripheral membrane protein' (C5/H4). GO:0005886 has 'cell membrane' as an EXACT synonym (GO1). However, the evidence code is ECO:0000250 (inferred by similarity to P. falciparum SERA5, Q9TY95) and the GO annotation is IEA (Inferred from Electronic Annotation). The only experimental evidence (ECO:0000269, PubMed:18419771) supports 'Host cytoplasm,' not plasma membrane specifically. The answer is database-supported but computationally transferred rather than directly experimentally validated for this protein.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4), [H7](#evidence-h7), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General reasoning can eliminate A (Plasmodium is eukaryotic, no peptidoglycan) and D (kinetoplasts are exclusive to kinetoplastids, not apicomplexans). The N-terminal signal peptide (MARLSSIVFIICLLLCNNAISDE...) suggests secretion/export, weakening C (perinuclear cytoplasm) as the primary location. However, a signal peptide indicates the protein exits the cell but does not specifically predict 'plasma membrane' over extracellular space, parasitophorous vacuole, or host cytoplasm. The specific assignment to plasma membrane (as a peripheral membrane protein) requires knowledge that SERA-family proteins associate with the host erythrocyte/cell membrane after secretion—an item-specific fact about SERA protein biology not derivable from sequence features alone.


**Missing item-specific fact**

> The knowledge that Plasmodium SERA proteins, after secretion into the parasitophorous vacuole, associate peripherally with the host cell plasma membrane (as documented for P. falciparum SERA5 and transferred to P. berghei SERA3). The actual experimental evidence for SERA3 points to 'Host cytoplasm,' not plasma membrane.


**Reason**

> While elimination of A and D is straightforward and the signal peptide weakly argues against C, the specific selection of 'plasma membrane' over other secreted/extracellular localizations depends on knowing SERA protein membrane-association biology. The annotation itself is IEA/similarity-based, and the experimental data support a different primary location (host cytoplasm). A model cannot determine from the sequence alone that this secreted protease specifically localizes to the plasma membrane rather than remaining in the parasitophorous vacuole or host cytoplasm.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The experimental evidence (PubMed:18419771) places SERA3 in 'Host cytoplasm,' which could be loosely mapped to 'perinuclear region of cytoplasm' (C) if interpreted as the cytoplasm of the infected host cell. Meanwhile, 'plasma membrane' (B) is only supported by computational transfer. Among the four choices, B is the most defensible by elimination, but the question's framing of 'primary Cellular Component' is somewhat misleading given that the protein's experimentally determined primary location is the host cytoplasm/parasitophorous vacuole, not the plasma membrane.


### Important caveats

- The 'Cell membrane; Peripheral membrane protein' annotation is ECO:0000250 (similarity to P. falciparum SERA5), not direct experimental evidence for P. berghei SERA3.
- The GO:0005886 annotation carries IEA evidence (Inferred from Electronic Annotation), the lowest-confidence evidence class.
- The only experimental subcellular location evidence (ECO:0000269, PubMed:18419771) supports 'Host cytoplasm,' which is not among the answer choices.
- The protein is a secreted protease (papain-like Cys protease domain) with serine repeats; its membrane association is peripheral and context-dependent (erythrocyte membrane during blood stage, hepatocyte membrane during liver stage).
- The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General reasoning can eliminate A (Plasmodium is eukaryotic, no peptidoglycan) and D (kinetoplasts are exclusive to kinetoplastids, not apicomplexans). The N-terminal signal peptide (MARLSSIVFIICLLLCNNAISDE...) suggests secretion/export, weakening C (perinuclear cytoplasm) as the primary location. However, a signal peptide indicates the protein exits the cell but does not specifically predict 'plasma membrane' over extracellular space, parasitophorous vacuole, or host cytoplasm. The specific assignment to plasma membrane (as a peripheral membrane protein) requires knowledge that SERA-family proteins associate with the host erythrocyte/cell membrane after secretion—an item-specific fact about SERA protein biology not derivable from sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The knowledge that Plasmodium SERA proteins, after secretion into the parasitophorous vacuole, associate peripherally with the host cell plasma membrane (as documented for P. falciparum SERA5 and transferred to P. berghei SERA3). The actual experimental evidence for SERA3 points to 'Host cytoplasm,' not plasma membrane.",
    "reason": "While elimination of A and D is straightforward and the signal peptide weakly argues against C, the specific selection of 'plasma membrane' over other secreted/extracellular localizations depends on knowing SERA protein membrane-association biology. The annotation itself is IEA/similarity-based, and the experimental data support a different primary location (host cytoplasm). A model cannot determine from the sequence alone that this secreted protease specifically localizes to the plasma membrane rather than remaining in the parasitophorous vacuole or host cytoplasm."
  },
  "case_id": "GO_cellular_component_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H4",
      "H7",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A509AC44 (P. berghei SERA3) explicitly annotates GO:0005886 (plasma membrane) as a cellular component (C8/H7), and the subcellular location comment lists 'Cell membrane; Peripheral membrane protein' (C5/H4). GO:0005886 has 'cell membrane' as an EXACT synonym (GO1). However, the evidence code is ECO:0000250 (inferred by similarity to P. falciparum SERA5, Q9TY95) and the GO annotation is IEA (Inferred from Electronic Annotation). The only experimental evidence (ECO:0000269, PubMed:18419771) supports 'Host cytoplasm,' not plasma membrane specifically. The answer is database-supported but computationally transferred rather than directly experimentally validated for this protein."
  },
  "important_caveats": [
    "The 'Cell membrane; Peripheral membrane protein' annotation is ECO:0000250 (similarity to P. falciparum SERA5), not direct experimental evidence for P. berghei SERA3.",
    "The GO:0005886 annotation carries IEA evidence (Inferred from Electronic Annotation), the lowest-confidence evidence class.",
    "The only experimental subcellular location evidence (ECO:0000269, PubMed:18419771) supports 'Host cytoplasm,' which is not among the answer choices.",
    "The protein is a secreted protease (papain-like Cys protease domain) with serine repeats; its membrane association is peripheral and context-dependent (erythrocyte membrane during blood stage, hepatocyte membrane during liver stage).",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The experimental evidence (PubMed:18419771) places SERA3 in 'Host cytoplasm,' which could be loosely mapped to 'perinuclear region of cytoplasm' (C) if interpreted as the cytoplasm of the infected host cell. Meanwhile, 'plasma membrane' (B) is only supported by computational transfer. Among the four choices, B is the most defensible by elimination, but the question's framing of 'primary Cellular Component' is somewhat misleading given that the protein's experimentally determined primary location is the host cytoplasm/parasitophorous vacuole, not the plasma membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A509AC44 (P. berghei SERA3) explicitly annotates GO:0005886 (plasma membrane) as a cellular component (C8/H7), and the subcellular location comment lists 'Cell membrane; Peripheral membrane protein' (C5/H4). GO:0005886 has 'cell membrane' as an EXACT synonym (GO1). However, the evidence code is ECO:0000250 (inferred by similarity to P. falciparum SERA5, Q9TY95) and the GO annotation is IEA (Inferred from Electronic Annotation). The only experimental evidence (ECO:0000269, PubMed:18419771) supports 'Host cytoplasm,' not plasma membrane specifically. The answer is database-supported but computationally transferred rather than directly experimentally validated for this protein.",
    "evidence_ids": ["C5", "C8", "H4", "H7", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General reasoning can eliminate A (Plasmodium is eukaryotic, no peptidoglycan) and D (kinetoplasts are exclusive to kinetoplastids, not apicomplexans). The N-terminal signal peptide (MARLSSIVFIICLLLCNNAISDE...) suggests secretion/export, weakening C (perinuclear cytoplasm) as the primary location. However, a signal peptide indicates the protein exits the cell but does not specifically predict 'plasma membrane' over extracellular space, parasitophorous vacuole, or host cytoplasm. The specific assignment to plasma membrane (as a peripheral membrane protein) requires knowledge that SERA-family proteins associate with the host erythrocyte/cell membrane after secretion—an item-specific fact about SERA protein biology not derivable from sequence features alone.",
    "missing_item_specific_fact": "The knowledge that Plasmodium SERA proteins, after secretion into the parasitophorous vacuole, associate peripherally with the host cell plasma membrane (as documented for P. falciparum SERA5 and transferred to P. berghei SERA3). The actual experimental evidence for SERA3 points to 'Host cytoplasm,' not plasma membrane.",
    "reason": "While elimination of A and D is straightforward and the signal peptide weakly argues against C, the specific selection of 'plasma membrane' over other secreted/extracellular localizations depends on knowing SERA protein membrane-association biology. The annotation itself is IEA/similarity-based, and the experimental data support a different primary location (host cytoplasm). A model cannot determine from the sequence alone that this secreted protease specifically localizes to the plasma membrane rather than remaining in the parasitophorous vacuole or host cytoplasm."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The experimental evidence (PubMed:18419771) places SERA3 in 'Host cytoplasm,' which could be loosely mapped to 'perinuclear region of cytoplasm' (C) if interpreted as the cytoplasm of the infected host cell. Meanwhile, 'plasma membrane' (B) is only supported by computational transfer. Among the four choices, B is the most defensible by elimination, but the question's framing of 'primary Cellular Component' is somewhat misleading given that the protein's experimentally determined primary location is the host cytoplasm/parasitophorous vacuole, not the plasma membrane."
  },
  "important_caveats": [
    "The 'Cell membrane; Peripheral membrane protein' annotation is ECO:0000250 (similarity to P. falciparum SERA5), not direct experimental evidence for P. berghei SERA3.",
    "The GO:0005886 annotation carries IEA evidence (Inferred from Electronic Annotation), the lowest-confidence evidence class.",
    "The only experimental subcellular location evidence (ECO:0000269, PubMed:18419771) supports 'Host cytoplasm,' which is not among the answer choices.",
    "The protein is a secreted protease (papain-like Cys protease domain) with serine repeats; its membrane association is peripheral and context-dependent (erythrocyte membrane during blood stage, hepatocyte membrane during liver stage).",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot is unknown."
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

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.524185+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9TY95","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9TY95","source":"UniProtKB"}],"id":"SL-9903","value":"Peripheral membrane protein"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9TY95","source":"UniProtKB"}],"id":"SL-0194","value":"Parasitophorous vacuole"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9TY95","source":"UniProtKB"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"18419771","source":"PubMed"}],"id":"SL-0381","value":"Host cytoplasm"}}]}
```

Source SHA-256: `5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.524185+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)  
**Locator:** `lines 55-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:26.529482+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:Q9TY95};
CC       Peripheral membrane protein {ECO:0000250|UniProtKB:Q9TY95}.
CC       Parasitophorous vacuole {ECO:0000250|UniProtKB:Q9TY95}. Secreted
CC       {ECO:0000250|UniProtKB:Q9TY95}. Host cytoplasm
CC       {ECO:0000269|PubMed:18419771}.
```

Source SHA-256: `35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)  
**Locator:** `lines 89-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:26.529482+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 94. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
