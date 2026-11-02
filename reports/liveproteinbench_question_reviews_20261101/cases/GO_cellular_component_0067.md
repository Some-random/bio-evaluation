# GO_cellular_component_0067

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — Ndc80 complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAAPGLPQPGSLSTLAGYPSSTYSSQNSPFFPSADRGGRMTLEEIKRDFTKHKLECPDTMWREPQPEQVQGLYSFAIESIFGLTVNDVRIEEVTGDVRSCLPSIDSLQFLSQDGRLHAKAIGNLRFIRLCQRLNRVLGLPEFSRETFASPTASGVQRFASAVCMLLRLRESLCRQFESQIQQRASLQQSLQKLSQNAQLVEQELLRFRAERQTQQPLAQRQKQQQSELEEELRQRHSELGALMEEFKERQAVHGRLELELGDLVLELMNLKQEREELHDQVVHSPEKLMERRDELRVQQKHLDAQLQELENLAASQQKLLLAFAKAVKKAKKAMEILSAHRDQVLAPHLGFRSDMRTREKLFRELGEQKEQLSKAVQDLQAEREELARQLEDQERKKDEEETELRGHLARAKREVEERKKALADQQDMTAAFLREAEKLEEKLAEQKQRHKLLVDAIEEEIQKVYAAFLTYVSQMQFIRSQMPLSLDLSQSASFLAEHSEKTHRGSPLACEREENDDFLASLLAESSPSSLGEEKENLPQSRPTAAADAERRLADFSPEKGRKRLSCLDEETEEEARMHERERESDRLFPAAREPREDGDFPMYGHAE

[Multiple Choices]
A. nuclear pore
B. periplasmic space
C. Ndc80 complex
D. tRNA methyltransferase complex
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

> The exact sequence matches the Toxoplasma gondii NUF2 entry. That entry annotates the protein to the Ndc80 complex (GO:0031262), though this annotation is computational (IEA:InterPro). A cited experimental subcellular-location annotation places it at the centromere/kinetochore and reports colocalization with NDC80, supporting the biological context of choice C.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long, coiled-coil-rich sequence is compatible with a structural protein, but that general feature does not identify NUF2 or distinguish the Ndc80 complex from other protein complexes in the choices.


**Missing item-specific fact**

> The protein-specific identity as NUF2 and its association with the Ndc80 complex are not provided in the question; recognizing them requires an external annotation or other protein-specific knowledge.


**Reason**

> The sequence alone does not provide a sufficiently specific signal for the listed complex. The reviewer-only annotation supports the key but was absent from the evaluated model input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, Ndc80 complex is supported by the matched protein annotation and its kinetochore localization; the alternatives are not comparably supported.


### Important caveats

- The GO annotation to Ndc80 complex is computational (IEA:InterPro), not direct experimental evidence of complex membership in the cited excerpts.
- The subcellular-location evidence is experimental, but it establishes centromere/kinetochore localization and colocalization with NDC80 rather than independently proving the GO complex annotation.
- The exact source snapshot used by the original author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, coiled-coil-rich sequence is compatible with a structural protein, but that general feature does not identify NUF2 or distinguish the Ndc80 complex from other protein complexes in the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity as NUF2 and its association with the Ndc80 complex are not provided in the question; recognizing them requires an external annotation or other protein-specific knowledge.",
    "reason": "The sequence alone does not provide a sufficiently specific signal for the listed complex. The reviewer-only annotation supports the key but was absent from the evaluated model input."
  },
  "case_id": "GO_cellular_component_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Toxoplasma gondii NUF2 entry. That entry annotates the protein to the Ndc80 complex (GO:0031262), though this annotation is computational (IEA:InterPro). A cited experimental subcellular-location annotation places it at the centromere/kinetochore and reports colocalization with NDC80, supporting the biological context of choice C."
  },
  "important_caveats": [
    "The GO annotation to Ndc80 complex is computational (IEA:InterPro), not direct experimental evidence of complex membership in the cited excerpts.",
    "The subcellular-location evidence is experimental, but it establishes centromere/kinetochore localization and colocalization with NDC80 rather than independently proving the GO complex annotation.",
    "The exact source snapshot used by the original author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, Ndc80 complex is supported by the matched protein annotation and its kinetochore localization; the alternatives are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Toxoplasma gondii NUF2 entry. That entry annotates the protein to the Ndc80 complex (GO:0031262), though this annotation is computational (IEA:InterPro). A cited experimental subcellular-location annotation places it at the centromere/kinetochore and reports colocalization with NDC80, supporting the biological context of choice C.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long, coiled-coil-rich sequence is compatible with a structural protein, but that general feature does not identify NUF2 or distinguish the Ndc80 complex from other protein complexes in the choices.",
    "missing_item_specific_fact": "The protein-specific identity as NUF2 and its association with the Ndc80 complex are not provided in the question; recognizing them requires an external annotation or other protein-specific knowledge.",
    "reason": "The sequence alone does not provide a sufficiently specific signal for the listed complex. The reviewer-only annotation supports the key but was absent from the evaluated model input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, Ndc80 complex is supported by the matched protein annotation and its kinetochore localization; the alternatives are not comparably supported."
  },
  "important_caveats": [
    "The GO annotation to Ndc80 complex is computational (IEA:InterPro), not direct experimental evidence of complex membership in the cited excerpts.",
    "The subcellular-location evidence is experimental, but it establishes centromere/kinetochore localization and colocalization with NDC80 rather than independently proving the GO complex annotation.",
    "The exact source snapshot used by the original author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt S8EV69 (NUF2_TOXGM, Toxoplasma gondii Kinetochore protein NUF2). Experimental evidence (ECO:0000269, PubMed:24015880) shows subcellular localization to 'Chromosome, centromere, kinetochore' with co-localization with NDC80 throughout the cell cycle. The GO:0031262 (Ndc80 complex) annotation is present as IEA:InterPro. NUF2 is a canonical, well-established subunit of the Ndc80 complex in all eukaryotes. The experimental kinetochore/NDC80 co-localization data and the conserved NUF2 identity support the Ndc80 complex assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option B (periplasmic space) is a prokaryotic/fungal compartment (GO:0042597 defined for Gram-negative bacteria and fungi) and is inapplicable to a eukaryotic protein with no signal peptide or prokaryotic export features. Option D (tRNA methyltransferase complex) requires methyltransferase catalytic domains, which are absent from this sequence. Option A (nuclear pore) requires FG-repeat nucleoporin motifs, transmembrane domains, or specific nucleoporin architecture, none of which are present. The sequence is dominated by a very long (~300+ residue) coiled-coil domain (heptad repeat pattern of E/R/L/Q residues spanning roughly residues 100–450), which is the hallmark structural feature of Ndc80 complex subunits (NDC80, NUF2, SPC24, SPC25). By elimination and by the distinctive long coiled-coil architecture, C is the most defensible choice.


**Missing item-specific fact**

> None strictly required; however, positive confirmation that this specific coiled-coil protein is NUF2 (rather than another coiled-coil protein) relies on recognizing the full domain architecture or knowing the protein's identity. The coiled-coil alone is not uniquely diagnostic of Ndc80 complex.


**Reason**

> The elimination of B (wrong organism type) and D (no methyltransferase domains) is straightforward. The distinction between A and C rests on the absence of nucleoporin-specific features and the presence of a long coiled-coil characteristic of Ndc80 complex proteins. This provides a concrete biological reasoning path, though the positive identification is somewhat indirect.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B and D are clearly eliminated by organism type and domain content. A is weakly plausible but lacks supporting sequence features (no FG repeats, no transmembrane segments). C is the only option with positive structural support (long coiled-coil). No genuine ambiguity among defensible choices.


### Important caveats

- The GO:0031262 (Ndc80 complex) annotation in UniProt is IEA:InterPro (computational inference from InterPro domain matching), not a direct experimental assignment of complex membership. The experimental evidence (ECO:0000269) establishes kinetochore localization and NDC80 co-localization but does not directly prove Ndc80 complex incorporation.
- The protein is from Toxoplasma gondii, an apicomplexan. NUF2 orthologs in divergent eukaryotes may have somewhat reduced sequence conservation, making domain-based identification harder than in model organisms.
- The coiled-coil argument for Ndc80 complex is consistent but not uniquely diagnostic; many nuclear and cytoplasmic proteins contain long coiled-coils. The reasoning path relies primarily on elimination of clearly wrong options.
- The UniProt entry was first public in 2025-06-18; the benchmark author's source snapshot is unknown but the sequence matches at all checked versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option B (periplasmic space) is a prokaryotic/fungal compartment (GO:0042597 defined for Gram-negative bacteria and fungi) and is inapplicable to a eukaryotic protein with no signal peptide or prokaryotic export features. Option D (tRNA methyltransferase complex) requires methyltransferase catalytic domains, which are absent from this sequence. Option A (nuclear pore) requires FG-repeat nucleoporin motifs, transmembrane domains, or specific nucleoporin architecture, none of which are present. The sequence is dominated by a very long (~300+ residue) coiled-coil domain (heptad repeat pattern of E/R/L/Q residues spanning roughly residues 100–450), which is the hallmark structural feature of Ndc80 complex subunits (NDC80, NUF2, SPC24, SPC25). By elimination and by the distinctive long coiled-coil architecture, C is the most defensible choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, positive confirmation that this specific coiled-coil protein is NUF2 (rather than another coiled-coil protein) relies on recognizing the full domain architecture or knowing the protein's identity. The coiled-coil alone is not uniquely diagnostic of Ndc80 complex.",
    "reason": "The elimination of B (wrong organism type) and D (no methyltransferase domains) is straightforward. The distinction between A and C rests on the absence of nucleoporin-specific features and the presence of a long coiled-coil characteristic of Ndc80 complex proteins. This provides a concrete biological reasoning path, though the positive identification is somewhat indirect."
  },
  "case_id": "GO_cellular_component_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt S8EV69 (NUF2_TOXGM, Toxoplasma gondii Kinetochore protein NUF2). Experimental evidence (ECO:0000269, PubMed:24015880) shows subcellular localization to 'Chromosome, centromere, kinetochore' with co-localization with NDC80 throughout the cell cycle. The GO:0031262 (Ndc80 complex) annotation is present as IEA:InterPro. NUF2 is a canonical, well-established subunit of the Ndc80 complex in all eukaryotes. The experimental kinetochore/NDC80 co-localization data and the conserved NUF2 identity support the Ndc80 complex assignment."
  },
  "important_caveats": [
    "The GO:0031262 (Ndc80 complex) annotation in UniProt is IEA:InterPro (computational inference from InterPro domain matching), not a direct experimental assignment of complex membership. The experimental evidence (ECO:0000269) establishes kinetochore localization and NDC80 co-localization but does not directly prove Ndc80 complex incorporation.",
    "The protein is from Toxoplasma gondii, an apicomplexan. NUF2 orthologs in divergent eukaryotes may have somewhat reduced sequence conservation, making domain-based identification harder than in model organisms.",
    "The coiled-coil argument for Ndc80 complex is consistent but not uniquely diagnostic; many nuclear and cytoplasmic proteins contain long coiled-coils. The reasoning path relies primarily on elimination of clearly wrong options.",
    "The UniProt entry was first public in 2025-06-18; the benchmark author's source snapshot is unknown but the sequence matches at all checked versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and D are clearly eliminated by organism type and domain content. A is weakly plausible but lacks supporting sequence features (no FG repeats, no transmembrane segments). C is the only option with positive structural support (long coiled-coil). No genuine ambiguity among defensible choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt S8EV69 (NUF2_TOXGM, Toxoplasma gondii Kinetochore protein NUF2). Experimental evidence (ECO:0000269, PubMed:24015880) shows subcellular localization to 'Chromosome, centromere, kinetochore' with co-localization with NDC80 throughout the cell cycle. The GO:0031262 (Ndc80 complex) annotation is present as IEA:InterPro. NUF2 is a canonical, well-established subunit of the Ndc80 complex in all eukaryotes. The experimental kinetochore/NDC80 co-localization data and the conserved NUF2 identity support the Ndc80 complex assignment.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option B (periplasmic space) is a prokaryotic/fungal compartment (GO:0042597 defined for Gram-negative bacteria and fungi) and is inapplicable to a eukaryotic protein with no signal peptide or prokaryotic export features. Option D (tRNA methyltransferase complex) requires methyltransferase catalytic domains, which are absent from this sequence. Option A (nuclear pore) requires FG-repeat nucleoporin motifs, transmembrane domains, or specific nucleoporin architecture, none of which are present. The sequence is dominated by a very long (~300+ residue) coiled-coil domain (heptad repeat pattern of E/R/L/Q residues spanning roughly residues 100–450), which is the hallmark structural feature of Ndc80 complex subunits (NDC80, NUF2, SPC24, SPC25). By elimination and by the distinctive long coiled-coil architecture, C is the most defensible choice.",
    "missing_item_specific_fact": "None strictly required; however, positive confirmation that this specific coiled-coil protein is NUF2 (rather than another coiled-coil protein) relies on recognizing the full domain architecture or knowing the protein's identity. The coiled-coil alone is not uniquely diagnostic of Ndc80 complex.",
    "reason": "The elimination of B (wrong organism type) and D (no methyltransferase domains) is straightforward. The distinction between A and C rests on the absence of nucleoporin-specific features and the presence of a long coiled-coil characteristic of Ndc80 complex proteins. This provides a concrete biological reasoning path, though the positive identification is somewhat indirect."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and D are clearly eliminated by organism type and domain content. A is weakly plausible but lacks supporting sequence features (no FG repeats, no transmembrane segments). C is the only option with positive structural support (long coiled-coil). No genuine ambiguity among defensible choices."
  },
  "important_caveats": [
    "The GO:0031262 (Ndc80 complex) annotation in UniProt is IEA:InterPro (computational inference from InterPro domain matching), not a direct experimental assignment of complex membership. The experimental evidence (ECO:0000269) establishes kinetochore localization and NDC80 co-localization but does not directly prove Ndc80 complex incorporation.",
    "The protein is from Toxoplasma gondii, an apicomplexan. NUF2 orthologs in divergent eukaryotes may have somewhat reduced sequence conservation, making domain-based identification harder than in model organisms.",
    "The coiled-coil argument for Ndc80 complex is consistent but not uniquely diagnostic; many nuclear and cytoplasmic proteins contain long coiled-coils. The reasoning path relies primarily on elimination of clearly wrong options.",
    "The UniProt entry was first public in 2025-06-18; the benchmark author's source snapshot is unknown but the sequence matches at all checked versions."
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

**Accession:** `S8EV69` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 39. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.410089+00:00.  

```json
"S8EV69"
```

Source SHA-256: `21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.410089+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Kinetochore protein NUF2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"24015880","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"30865554","source":"PubMed"}],"value":"TgNuf2"}]}}
```

Source SHA-256: `21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.410089+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24015880","source":"PubMed"}],"value":"Co-localizes with NDC80 throughout the cell cycle"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"24015880","source":"PubMed"}],"id":"SL-0149","value":"Chromosome, centromere, kinetochore"}}]}
```

Source SHA-256: `21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.410089+00:00.  

```json
{"database":"GO","id":"GO:0031262","properties":[{"key":"GoTerm","value":"C:Ndc80 complex"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39)  
**Locator:** `lines 39-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:34:00.721786+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Chromosome, centromere, kinetochore
CC       {ECO:0000269|PubMed:24015880}. Note=Co-localizes with NDC80 throughout
CC       the cell cycle. {ECO:0000269|PubMed:24015880}.
```

Source SHA-256: `665a5d577c22b6c288b850d0d50c4d6f885ae6321f4d7320b54fc9362f20bc3a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39)  
**Locator:** `lines 67-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:34:00.721786+00:00.  

```text
DR   GO; GO:0031262; C:Ndc80 complex; IEA:InterPro.
```

Source SHA-256: `665a5d577c22b6c288b850d0d50c4d6f885ae6321f4d7320b54fc9362f20bc3a`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 174616-174624`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031262
name: Ndc80 complex
namespace: cellular_component
def: "An essential outer kinetochore complex involved in the attachment of microtubule ends to the chromosomes during mitosis." [GOC:vw, PMID:28502666, PMID:34810257]
synonym: "Nuf2-Ndc80 complex" EXACT []
is_a: GO:0032991 ! protein-containing complex
relationship: part_of GO:0000940 ! outer kinetochore

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
