# GO_cellular_component_0133

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — nucleoplasm

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAQRILQLAAEGSPERLQEALQGLTEGELGDMVTRQALRGRETAALLKGIFKGSPCSQQSGVLRRLQVYKHCVSLVESGDLHVGKVSEIIGLLMLEARQLPGHALAELATLFVEVIKRGSLSNGKSLELFSTVLTALSNSKESLAYGKGELNGEEFKKQLINTLCSSKWDPQCVIHLANMFRDIPLSGEELQFVVEKVLRMFSKLDLQEIPPLVYQLLLLSAKGSKKTVLEGIISFFNQLDKRQKEEQRVPQSADLEVATVPLDQLRHVEGTVILHIVSAINLDQDIGEELIKHLKTEQQKDPGKALCPFSVSLLLSTAVKHRLQEQIFDFLKTSITRSCKDLQILQASKFLQDLCPQQYDVTAVILEVVKNSAFGWDHVTQGLVDLGFSLMESYEPKKSFGGKAAETNLGLSKMPAQQACKLGASILLETFKVHEPIRSDILEQVLNRVLTKAASPVSHFIDLLSNIVVSAPLVLQNSSSRVTETFDNLSFLPIDTVQGLLRAVQPLLKVSMSVRDSLILVLQKAIFSRQLDARKAAVAGFLLLLRNFKILGSLTSSQCSQAIGATQVQADVHACYNSAANEAFCLEILGSLRRCLSQQADVRLMLYEGFYDVLRRNSQLASSIMETLLSQIKQYYLPQQDLLPPLKLEGCIMAQGDQIFLQEPLAHLLCCIQHCLAWYKSTVHLCKGAEDEEEEEDVGFEQNFEEMLESVTRRMIKSELEDFELDKSADFSPSSGVGVKNNIYAIQVMGICEVLIEYNFKIGNFSKNKFEDVLGLFTCYNKLSEILKEKAGKNKSTLGNRIARSFLSMGFVSTLLTALFRDNAQSHEESLAVLRSSTEFMRYAVSVALQKVQQLEEMGQTDGPDGQNPEKMFQNLCKITRVLLWRYTSIPTAVEESGKKKGKSISLLCLEGLLRIFNTMQQLYAARIPQFLQALDITDGDAEEADINVTEKAAFQIRQFQRSLVNQLSSAEDDFNSKETQLLITILSTLSKLLDPGSQQFLQFLTWTVKICKENALEDLSCCKGLLTLLFSLHVLYKSPVSLLRELAQDIHACLGDIDQDVEIESRSHFAIVNVKTAAPTVCLLVLGQADKVLEEVDWLIKRLTILGSDTSEDSTQASNQTQALEKGVILQLGTLLTVFHELVQTALPAGSCVDSLLRSLSKTYAILTSLIKHYIQACRSTSNTVPGRLEKLVKLSGSHLTPQCYSFITYVQNIHSESLSFAEEKKKKKKEDETAVVSTVMAKVLRDTKPIPNLIFAIEQYEKFLIHLSKKSKVNLMQYMKLSTSRDFRINASMLDSVLQEQNTEDAENEPDNNQSGTAEQPDENQEPQKKRRRKK

[Multiple Choices]
A. nucleoplasm
B. protein-containing complex
C. euchromatin
D. nuclear pore nuclear basket
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

> The supplied sequence exactly matches the chicken FANCI sequence, which has a UniProt GO annotation for nucleoplasm (TAS:Reactome). This supports A, though the annotation is not direct experimental evidence.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad inference of a nuclear DNA-repair protein, but it does not meaningfully distinguish nucleoplasm from association with a protein-containing complex.


**Missing item-specific fact**

> The protein-specific localization or GO annotation is needed to distinguish the listed choices; no such annotation or experimental localization evidence is included in the question.


**Reason**

> The supplied sequence alone does not establish which of these overlapping GO cellular-component descriptions should be selected as the primary one.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The matched protein is annotated both to nucleoplasm and, with IDA evidence, to the Fanconi anaemia nuclear complex, a specific nuclear protein-containing complex. Thus A and the broader B can both describe this protein; the question does not define how to choose a single primary term.


### Important caveats

- The nucleoplasm annotation is TAS:Reactome, whereas the Fanconi anaemia nuclear complex annotation is IDA:MGI.
- Reviewer-only accession and database evidence were not present in the evaluated input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad inference of a nuclear DNA-repair protein, but it does not meaningfully distinguish nucleoplasm from association with a protein-containing complex.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization or GO annotation is needed to distinguish the listed choices; no such annotation or experimental localization evidence is included in the question.",
    "reason": "The supplied sequence alone does not establish which of these overlapping GO cellular-component descriptions should be selected as the primary one."
  },
  "case_id": "GO_cellular_component_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the chicken FANCI sequence, which has a UniProt GO annotation for nucleoplasm (TAS:Reactome). This supports A, though the annotation is not direct experimental evidence."
  },
  "important_caveats": [
    "The nucleoplasm annotation is TAS:Reactome, whereas the Fanconi anaemia nuclear complex annotation is IDA:MGI.",
    "Reviewer-only accession and database evidence were not present in the evaluated input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The matched protein is annotated both to nucleoplasm and, with IDA evidence, to the Fanconi anaemia nuclear complex, a specific nuclear protein-containing complex. Thus A and the broader B can both describe this protein; the question does not define how to choose a single primary term."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the chicken FANCI sequence, which has a UniProt GO annotation for nucleoplasm (TAS:Reactome). This supports A, though the annotation is not direct experimental evidence.",
    "evidence_ids": ["C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad inference of a nuclear DNA-repair protein, but it does not meaningfully distinguish nucleoplasm from association with a protein-containing complex.",
    "missing_item_specific_fact": "The protein-specific localization or GO annotation is needed to distinguish the listed choices; no such annotation or experimental localization evidence is included in the question.",
    "reason": "The supplied sequence alone does not establish which of these overlapping GO cellular-component descriptions should be selected as the primary one."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The matched protein is annotated both to nucleoplasm and, with IDA evidence, to the Fanconi anaemia nuclear complex, a specific nuclear protein-containing complex. Thus A and the broader B can both describe this protein; the question does not define how to choose a single primary term."
  },
  "important_caveats": [
    "The nucleoplasm annotation is TAS:Reactome, whereas the Fanconi anaemia nuclear complex annotation is IDA:MGI.",
    "Reviewer-only accession and database evidence were not present in the evaluated input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B0I564 (FANCI_CHICK) carries a direct GO CC annotation of GO:0005654 (nucleoplasm) with evidence code TAS:Reactome (evidence C6/H3). The protein is also annotated with GO:0043240 (Fanconi anaemia nuclear complex, IDA:MGI, evidence C5/H2), which is_a nuclear protein-containing complex, which is_a protein-containing complex (option B). Thus nucleoplasm is explicitly annotated for this protein, supporting the expected answer, though option B is also ontology-supported.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3), [C5](#evidence-c5), [H2](#evidence-h2), [GO2](#evidence-go2), [GO4](#evidence-go4), [GO6](#evidence-go6), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence lacks mitochondrial/ER targeting signals and is large (~1338 AA), consistent with a nuclear protein. However, among the four nuclear options (nucleoplasm, protein-containing complex, euchromatin, nuclear pore nuclear basket), the sequence provides no clear distinguishing features. Coiled-coil-like regions hint at complex formation (favoring B), while the absence of nucleolar or nuclear-pore targeting motifs weakly disfavors D. Distinguishing nucleoplasm (A) from protein-containing complex (B) requires knowing this is FANCI and its specific GO annotation, not general sequence reasoning.


**Missing item-specific fact**

> The identity of the protein as FANCI (Fanconi anemia group I protein) and its specific UniProt/GO annotation assigning 'nucleoplasm' as a primary CC term (TAS:Reactome) rather than or in addition to 'protein-containing complex.' Without this item-specific annotation, the sequence alone cannot resolve A vs. B.


**Reason**

> All four options are nuclear/local nuclear terms. The sequence does not contain features (e.g., nucleolar localization signals, nuclear pore transmembrane domains, histone-like motifs) that would let general biological reasoning distinguish nucleoplasm from protein-containing complex for this particular protein. Selection of A over B depends on the specific database annotation for FANCI.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> FANCI is annotated with both GO:0005654 (nucleoplasm, TAS:Reactome) and GO:0043240 (Fanconi anaemia nuclear complex, IDA:MGI). The latter is_a nuclear protein-containing complex is_a protein-containing complex (option B). The word 'primary' in the prompt does not clearly resolve whether the compartment (nucleoplasm) or the complex membership (protein-containing complex) is the 'primary' annotation. Both A and B are defensible from the annotation record.


### Important caveats

- The nucleoplasm annotation (TAS:Reactome) is a traceable author statement, a lower evidence level than the IDA:MGI evidence for the FA nuclear complex annotation.
- The protein-containing complex annotation (option B) is supported via ontology hierarchy (Fanconi anaemia nuclear complex → nuclear protein-containing complex → protein-containing complex) rather than a direct annotation of GO:0032991.
- Sequence identity was confirmed (SHA-256 match) between the benchmark input and UniProt B0I564.
- The GO ontology version used by the benchmark authors is unknown; the reviewer consulted the current 2026 ontology.
- The identity origin (UniProt accession inferred from dataset metadata) was absent from the evaluated model's input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks mitochondrial/ER targeting signals and is large (~1338 AA), consistent with a nuclear protein. However, among the four nuclear options (nucleoplasm, protein-containing complex, euchromatin, nuclear pore nuclear basket), the sequence provides no clear distinguishing features. Coiled-coil-like regions hint at complex formation (favoring B), while the absence of nucleolar or nuclear-pore targeting motifs weakly disfavors D. Distinguishing nucleoplasm (A) from protein-containing complex (B) requires knowing this is FANCI and its specific GO annotation, not general sequence reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the protein as FANCI (Fanconi anemia group I protein) and its specific UniProt/GO annotation assigning 'nucleoplasm' as a primary CC term (TAS:Reactome) rather than or in addition to 'protein-containing complex.' Without this item-specific annotation, the sequence alone cannot resolve A vs. B.",
    "reason": "All four options are nuclear/local nuclear terms. The sequence does not contain features (e.g., nucleolar localization signals, nuclear pore transmembrane domains, histone-like motifs) that would let general biological reasoning distinguish nucleoplasm from protein-containing complex for this particular protein. Selection of A over B depends on the specific database annotation for FANCI."
  },
  "case_id": "GO_cellular_component_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3",
      "C5",
      "H2",
      "GO2",
      "GO4",
      "GO6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B0I564 (FANCI_CHICK) carries a direct GO CC annotation of GO:0005654 (nucleoplasm) with evidence code TAS:Reactome (evidence C6/H3). The protein is also annotated with GO:0043240 (Fanconi anaemia nuclear complex, IDA:MGI, evidence C5/H2), which is_a nuclear protein-containing complex, which is_a protein-containing complex (option B). Thus nucleoplasm is explicitly annotated for this protein, supporting the expected answer, though option B is also ontology-supported."
  },
  "important_caveats": [
    "The nucleoplasm annotation (TAS:Reactome) is a traceable author statement, a lower evidence level than the IDA:MGI evidence for the FA nuclear complex annotation.",
    "The protein-containing complex annotation (option B) is supported via ontology hierarchy (Fanconi anaemia nuclear complex → nuclear protein-containing complex → protein-containing complex) rather than a direct annotation of GO:0032991.",
    "Sequence identity was confirmed (SHA-256 match) between the benchmark input and UniProt B0I564.",
    "The GO ontology version used by the benchmark authors is unknown; the reviewer consulted the current 2026 ontology.",
    "The identity origin (UniProt accession inferred from dataset metadata) was absent from the evaluated model's input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "FANCI is annotated with both GO:0005654 (nucleoplasm, TAS:Reactome) and GO:0043240 (Fanconi anaemia nuclear complex, IDA:MGI). The latter is_a nuclear protein-containing complex is_a protein-containing complex (option B). The word 'primary' in the prompt does not clearly resolve whether the compartment (nucleoplasm) or the complex membership (protein-containing complex) is the 'primary' annotation. Both A and B are defensible from the annotation record."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B0I564 (FANCI_CHICK) carries a direct GO CC annotation of GO:0005654 (nucleoplasm) with evidence code TAS:Reactome (evidence C6/H3). The protein is also annotated with GO:0043240 (Fanconi anaemia nuclear complex, IDA:MGI, evidence C5/H2), which is_a nuclear protein-containing complex, which is_a protein-containing complex (option B). Thus nucleoplasm is explicitly annotated for this protein, supporting the expected answer, though option B is also ontology-supported.",
    "evidence_ids": ["C6", "H3", "C5", "H2", "GO2", "GO4", "GO6", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence lacks mitochondrial/ER targeting signals and is large (~1338 AA), consistent with a nuclear protein. However, among the four nuclear options (nucleoplasm, protein-containing complex, euchromatin, nuclear pore nuclear basket), the sequence provides no clear distinguishing features. Coiled-coil-like regions hint at complex formation (favoring B), while the absence of nucleolar or nuclear-pore targeting motifs weakly disfavors D. Distinguishing nucleoplasm (A) from protein-containing complex (B) requires knowing this is FANCI and its specific GO annotation, not general sequence reasoning.",
    "missing_item_specific_fact": "The identity of the protein as FANCI (Fanconi anemia group I protein) and its specific UniProt/GO annotation assigning 'nucleoplasm' as a primary CC term (TAS:Reactome) rather than or in addition to 'protein-containing complex.' Without this item-specific annotation, the sequence alone cannot resolve A vs. B.",
    "reason": "All four options are nuclear/local nuclear terms. The sequence does not contain features (e.g., nucleolar localization signals, nuclear pore transmembrane domains, histone-like motifs) that would let general biological reasoning distinguish nucleoplasm from protein-containing complex for this particular protein. Selection of A over B depends on the specific database annotation for FANCI."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "FANCI is annotated with both GO:0005654 (nucleoplasm, TAS:Reactome) and GO:0043240 (Fanconi anaemia nuclear complex, IDA:MGI). The latter is_a nuclear protein-containing complex is_a protein-containing complex (option B). The word 'primary' in the prompt does not clearly resolve whether the compartment (nucleoplasm) or the complex membership (protein-containing complex) is the 'primary' annotation. Both A and B are defensible from the annotation record."
  },
  "important_caveats": [
    "The nucleoplasm annotation (TAS:Reactome) is a traceable author statement, a lower evidence level than the IDA:MGI evidence for the FA nuclear complex annotation.",
    "The protein-containing complex annotation (option B) is supported via ontology hierarchy (Fanconi anaemia nuclear complex → nuclear protein-containing complex → protein-containing complex) rather than a direct annotation of GO:0032991.",
    "Sequence identity was confirmed (SHA-256 match) between the benchmark input and UniProt B0I564.",
    "The GO ontology version used by the benchmark authors is unknown; the reviewer consulted the current 2026 ontology.",
    "The identity origin (UniProt accession inferred from dataset metadata) was absent from the evaluated model's input."
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

**Accession:** `B0I564` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 72. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0I564.json)  
**Locator:** `/uniProtKBCrossReferences/30`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:13.236985+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"18931676","source":"PubMed"}],"id":"GO:0043240","properties":[{"key":"GoTerm","value":"C:Fanconi anaemia nuclear complex"},{"key":"GoEvidenceType","value":"IDA:MGI"}]}
```

Source SHA-256: `930b8c9dc8b101a42561b9ac061f1b2e0e96406be484cad8495768d62800c72f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0I564.json)  
**Locator:** `/uniProtKBCrossReferences/31`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:13.236985+00:00.  

```json
{"database":"GO","id":"GO:0005654","properties":[{"key":"GoTerm","value":"C:nucleoplasm"},{"key":"GoEvidenceType","value":"TAS:Reactome"}]}
```

Source SHA-256: `930b8c9dc8b101a42561b9ac061f1b2e0e96406be484cad8495768d62800c72f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0I564?format=txt&versions=72)  
**Locator:** `lines 117-117`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 72 / 1.  
**Retrieved:** 2026-11-02T04:27:15.248105+00:00.  

```text
DR   GO; GO:0043240; C:Fanconi anaemia nuclear complex; IDA:MGI.
```

Source SHA-256: `fdcce5f2431525c3d58eddd2017ac848c6453be87c533c91e1499a652021475c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0I564?format=txt&versions=72)  
**Locator:** `lines 118-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 72 / 1.  
**Retrieved:** 2026-11-02T04:27:15.248105+00:00.  

```text
DR   GO; GO:0005654; C:nucleoplasm; TAS:Reactome.
```

Source SHA-256: `fdcce5f2431525c3d58eddd2017ac848c6453be87c533c91e1499a652021475c`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58222-58234`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005654
name: nucleoplasm
namespace: cellular_component
def: "That part of the nuclear content other than the chromosomes or the nucleolus." [GOC:ma, ISBN:0124325653]
subset: goslim_chembl
subset: goslim_generic
subset: goslim_plant
xref: NIF_Subcellular:sao661522542
xref: Wikipedia:Nucleoplasm
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0031981 ! nuclear lumen

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 192667-192686`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0032991
name: protein-containing complex
namespace: cellular_component
alt_id: GO:0043234
def: "A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together." [GOC:dos, GOC:mah]
comment: A protein complex in this context is meant as a stable set of interacting proteins which can be co-purified by an acceptable method, and where the complex has been shown to exist as an isolated, functional unit in vivo. Acceptable experimental methods include stringent protein purification followed by detection of protein interaction. The following methods should be considered non-acceptable: simple immunoprecipitation, pull-down experiments from cell extracts without further purification, colocalization and 2-hybrid screening. Interactions that should not be captured as protein complexes include: 1) enzyme/substrate, receptor/ligand or any similar transient interactions, unless these are a critical part of the complex assembly or are required e.g. for the receptor to be functional; 2) proteins associated in a pull-down/co-immunoprecipitation assay with no functional link or any evidence that this is a defined biological entity rather than a loose-affinity complex; 3) any complex where the only evidence is based on genetic interaction data; 4) partial complexes, where some subunits (e.g. transmembrane ones) cannot be expressed as recombinant proteins and are excluded from experiments (in this case, independent evidence is necessary to find out the composition of the full complex, if known). Interactions that may be captured as protein complexes include: 1) enzyme/substrate or receptor/ligand if the complex can only assemble and become functional in the presence of both classes of subunits; 2) complexes where one of the members has not been shown to be physically linked to the other(s), but is a homologue of, and has the same functionality as, a protein that has been experimentally demonstrated to form a complex with the other member(s); 3) complexes whose existence is accepted based on localization and pharmacological studies, but for which experimental evidence is not yet available for the complex as a whole.
subset: goslim_agr
subset: goslim_chembl
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_mouse
subset: goslim_pir
synonym: "macromolecular complex" EXACT []
synonym: "macromolecule complex" EXACT []
synonym: "protein complex" NARROW []
synonym: "protein containing complex" EXACT []
synonym: "protein-protein complex" NARROW []
is_a: GO:0005575 ! cellular_component

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 245217-245227`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0043240
name: Fanconi anaemia nuclear complex
namespace: cellular_component
def: "A protein complex composed of the Fanconi anaemia (FA) proteins including A, C, E, G and F (FANCA-F). Functions in the activation of the downstream protein FANCD2 by monoubiquitylation, and is essential for protection against chromosome breakage." [GOC:jl, PMID:12093742]
synonym: "FA complex" EXACT []
synonym: "FA core complex" EXACT []
synonym: "FA nuclear complex" EXACT []
synonym: "Fanconi anaemia complex" EXACT []
is_a: GO:0140513 ! nuclear protein-containing complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 441123-441132`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0140513
name: nuclear protein-containing complex
namespace: cellular_component
def: "A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together in the nucleus." [GOC:pg]
subset: gocheck_do_not_annotate
synonym: "nuclear complex" EXACT []
is_a: GO:0032991 ! protein-containing complex
relationship: part_of GO:0005634 ! nucleus

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
