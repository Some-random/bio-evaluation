# GO_biological_process_0150

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — transmembrane transport

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSFYNKCFTNKLISAHSLFCQHVSTLKNNKKECFEDVKRSNRISDEFYSSFLYHSYIENLKSTKEYVYFIYLQDIYYNINIFKNKGRLYISNNGLCNDKLKDNNNNNNINSNNFGNSYNAYTKKKSFYHSFNDLNEAKEIRKKRKNEKSEKNIVEYLLCNIINPNENYHIQNIYNHNLNNNVSIEIHKKNDSVMYHYNNEKKTKTSKMTTDIKLKQINNVYIKYVPYKNKIITLACPNKYYPTLYRYFSSHTNKKEDAEENDKNKNININNVDNRYKEDFMYGCENKNDSEKHKKTTNNNFGDEFEKLKVKELDKILNKLEMLYDNKNNKMNINVKILGYIFKNFLLKNKELKRKIFCSLFFLLCSKMAIIYTPILLSTFIENVNLQKSLSNNIDIYSTNKSSVLLLCAYVFSRVLSSTMNELRNSVFSNISQKISTFVSKLFFYKIHNLNLTYILSKKNGELSFIFNRGCKSITNLLNVMVFQIIPIIIEFILYLYILTYKIHYTVSLVTCFNMFLYVLFTTLITKRRTIIRKHMNKAEQNTFNIFLDSIQNVEQVKYYTNEIHELKKFIKEQKKYEKEAINVQKSLSFLNFGQQIILNTNLFLCMYLTYLNIANDIFPFSYLILVNTLLFQLAMPLNMFGTIYRETKLSLVDIESMIKILVKKIKSPDYGNQMLIKNGNIKFENVYFKYPLNEDINGLEQNYQAKEKDPNIINNINNINNINNINNINNINSINNIYTFESNVKNISSTNMITSSINKLKKWYLDKVKDNKKNVQYNNNDVKKTNPNITKNLNKEIKENINTHLKNHKIINNSPNYNNNNYLFQNFTCNIENGEKVAIIGKSGSGKSSLIKLLLKFYEVNSGNIYIDNKNIDDIDLYTLRKNISVVPQDTILFNNTISYNIKYGNFQCTDKQMIQASIKAELHDKIMKMENKYDTIVGERGTKLSIGEKQRICIARCFLKDSKIIVLDEHASNLDNENKKAIEKALTKLCMGKTTFIITHVMENLKHMDKIIFFCGKNIYVGSHKNLMDDNHFYREYYDSKNNKML

[Multiple Choices]
A. positive regulation of dendrite morphogenesis
B. transmembrane transport
C. positive regulation of epithelial cell migration
D. regulation of alternative mRNA splicing, via spliceosome
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

> The exact sequence match is annotated as an ATP-dependent transporter of glutathione-coordinated iron-sulfur clusters, and the matched historical record assigns transmembrane transport. The function annotation cites experimental evidence, though the primary study was not independently assessed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple hydrophobic stretches consistent with membrane-spanning segments and a C-terminal ABC-family ATPase nucleotide-binding region, including a Walker A-like GxxxxGKS motif. This architecture supports a membrane transporter and distinguishes option B from the neuronal, epithelial-migration, and spliceosome-related choices.


**Missing item-specific fact**

> The precise transported substrate and the experimentally established function of this particular protein are not provided, but those facts are not needed to favor the broad transmembrane transport option from the sequence architecture.


**Reason**

> The sequence provides meaningful biological grounds for selecting transmembrane transport; this is not based solely on recognizing a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed processes, transmembrane transport is the one supported by the protein's membrane-spanning and ABC-transporter features.


### Important caveats

- The reviewer-only UniProt records match the supplied sequence; their annotations were not available to the evaluated model.
- The historical record includes a GO annotation with IBA evidence, while the functional description cites a publication with ECO:0000269 evidence; the primary publication was not independently reviewed.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches consistent with membrane-spanning segments and a C-terminal ABC-family ATPase nucleotide-binding region, including a Walker A-like GxxxxGKS motif. This architecture supports a membrane transporter and distinguishes option B from the neuronal, epithelial-migration, and spliceosome-related choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise transported substrate and the experimentally established function of this particular protein are not provided, but those facts are not needed to favor the broad transmembrane transport option from the sequence architecture.",
    "reason": "The sequence provides meaningful biological grounds for selecting transmembrane transport; this is not based solely on recognizing a database entry."
  },
  "case_id": "GO_biological_process_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as an ATP-dependent transporter of glutathione-coordinated iron-sulfur clusters, and the matched historical record assigns transmembrane transport. The function annotation cites experimental evidence, though the primary study was not independently assessed here."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence; their annotations were not available to the evaluated model.",
    "The historical record includes a GO annotation with IBA evidence, while the functional description cites a publication with ECO:0000269 evidence; the primary publication was not independently reviewed.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed processes, transmembrane transport is the one supported by the protein's membrane-spanning and ABC-transporter features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as an ATP-dependent transporter of glutathione-coordinated iron-sulfur clusters, and the matched historical record assigns transmembrane transport. The function annotation cites experimental evidence, though the primary study was not independently assessed here.",
    "evidence_ids": ["C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches consistent with membrane-spanning segments and a C-terminal ABC-family ATPase nucleotide-binding region, including a Walker A-like GxxxxGKS motif. This architecture supports a membrane transporter and distinguishes option B from the neuronal, epithelial-migration, and spliceosome-related choices.",
    "missing_item_specific_fact": "The precise transported substrate and the experimentally established function of this particular protein are not provided, but those facts are not needed to favor the broad transmembrane transport option from the sequence architecture.",
    "reason": "The sequence provides meaningful biological grounds for selecting transmembrane transport; this is not based solely on recognizing a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed processes, transmembrane transport is the one supported by the protein's membrane-spanning and ABC-transporter features."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence; their annotations were not available to the evaluated model.",
    "The historical record includes a GO annotation with IBA evidence, while the functional description cites a publication with ECO:0000269 evidence; the primary publication was not independently reviewed.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q8IDH9, PfATM1) is an ABC transporter that experimentally transports glutathione-coordinated &#91;4Fe-4S&#93; clusters in an ATP-dependent manner (ECO:0000269, PubMed:39348385). UniProt assigns GO:0055085 (transmembrane transport) via IBA:GO_Central, consistent with the ABC transporter family classification. The GO:0055085 definition ('transport of a solute across a lipid bilayer') and its NARROW synonym 'ATP hydrolysis coupled transmembrane transport' directly match the experimentally confirmed function. The expected answer B is well-supported by both the experimental transport evidence and the family-level annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region contains the canonical ABC transporter Walker A motif (GKSGSGKS in 'AIIGKSGSGKSSLIKLLLKFYEV') and the ABC transporter signature (IIVLDEH in 'IIVLDEHASN'), while the middle region contains multiple long hydrophobic stretches characteristic of transmembrane helices. General biological knowledge establishes that ABC transporters are transmembrane proteins that use ATP hydrolysis to move solutes across lipid bilayers. The distractors are incompatible: dendrite morphogenesis (A) and epithelial cell migration (C) are multicellular/neuronal processes irrelevant to a single-cell parasite's transporter, and alternative mRNA splicing (D) is a nuclear RNA-processing function with no structural or functional connection to a membrane-bound ATPase.


**Missing item-specific fact**

> None required. The ABC transporter motifs are directly readable from the supplied sequence, and the mapping from 'ABC transporter with transmembrane domains' to 'transmembrane transport' is standard textbook knowledge.


**Reason**

> A model with general knowledge of ABC transporter architecture (Walker A motif, ABC signature, transmembrane domains) can identify the protein as a membrane transporter and select 'transmembrane transport' over the three clearly incompatible distractors without needing to look up the specific UniProt entry or recall this protein's exact annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span entirely different functional categories (neural morphogenesis, cell migration, RNA splicing, membrane transport). Only B is consistent with a protein bearing ABC transporter motifs and transmembrane domains. No other option is defensible.


### Important caveats

- The GO:0055085 annotation is IBA (Inferred by Biological aspect of Ancestor) from GO_Central, i.e., a family-level computational inference rather than a direct experimental GO assignment for this specific protein. However, the underlying experimental evidence (PubMed:39348385) independently confirms ATP-dependent transmembrane transport.
- The organism (Plasmodium falciparum) is not explicitly stated in the user input but is inferable from poly-asparagine stretches and sequence composition; even without this, the ABC transporter motifs suffice to eliminate the multicellular-process distractors.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark input and UniProt Q8IDH9.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains the canonical ABC transporter Walker A motif (GKSGSGKS in 'AIIGKSGSGKSSLIKLLLKFYEV') and the ABC transporter signature (IIVLDEH in 'IIVLDEHASN'), while the middle region contains multiple long hydrophobic stretches characteristic of transmembrane helices. General biological knowledge establishes that ABC transporters are transmembrane proteins that use ATP hydrolysis to move solutes across lipid bilayers. The distractors are incompatible: dendrite morphogenesis (A) and epithelial cell migration (C) are multicellular/neuronal processes irrelevant to a single-cell parasite's transporter, and alternative mRNA splicing (D) is a nuclear RNA-processing function with no structural or functional connection to a membrane-bound ATPase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The ABC transporter motifs are directly readable from the supplied sequence, and the mapping from 'ABC transporter with transmembrane domains' to 'transmembrane transport' is standard textbook knowledge.",
    "reason": "A model with general knowledge of ABC transporter architecture (Walker A motif, ABC signature, transmembrane domains) can identify the protein as a membrane transporter and select 'transmembrane transport' over the three clearly incompatible distractors without needing to look up the specific UniProt entry or recall this protein's exact annotation."
  },
  "case_id": "GO_biological_process_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein (Q8IDH9, PfATM1) is an ABC transporter that experimentally transports glutathione-coordinated [4Fe-4S] clusters in an ATP-dependent manner (ECO:0000269, PubMed:39348385). UniProt assigns GO:0055085 (transmembrane transport) via IBA:GO_Central, consistent with the ABC transporter family classification. The GO:0055085 definition ('transport of a solute across a lipid bilayer') and its NARROW synonym 'ATP hydrolysis coupled transmembrane transport' directly match the experimentally confirmed function. The expected answer B is well-supported by both the experimental transport evidence and the family-level annotation."
  },
  "important_caveats": [
    "The GO:0055085 annotation is IBA (Inferred by Biological aspect of Ancestor) from GO_Central, i.e., a family-level computational inference rather than a direct experimental GO assignment for this specific protein. However, the underlying experimental evidence (PubMed:39348385) independently confirms ATP-dependent transmembrane transport.",
    "The organism (Plasmodium falciparum) is not explicitly stated in the user input but is inferable from poly-asparagine stretches and sequence composition; even without this, the ABC transporter motifs suffice to eliminate the multicellular-process distractors.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark input and UniProt Q8IDH9."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different functional categories (neural morphogenesis, cell migration, RNA splicing, membrane transport). Only B is consistent with a protein bearing ABC transporter motifs and transmembrane domains. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q8IDH9, PfATM1) is an ABC transporter that experimentally transports glutathione-coordinated [4Fe-4S] clusters in an ATP-dependent manner (ECO:0000269, PubMed:39348385). UniProt assigns GO:0055085 (transmembrane transport) via IBA:GO_Central, consistent with the ABC transporter family classification. The GO:0055085 definition ('transport of a solute across a lipid bilayer') and its NARROW synonym 'ATP hydrolysis coupled transmembrane transport' directly match the experimentally confirmed function. The expected answer B is well-supported by both the experimental transport evidence and the family-level annotation.",
    "evidence_ids": ["C4", "C5", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region contains the canonical ABC transporter Walker A motif (GKSGSGKS in 'AIIGKSGSGKSSLIKLLLKFYEV') and the ABC transporter signature (IIVLDEH in 'IIVLDEHASN'), while the middle region contains multiple long hydrophobic stretches characteristic of transmembrane helices. General biological knowledge establishes that ABC transporters are transmembrane proteins that use ATP hydrolysis to move solutes across lipid bilayers. The distractors are incompatible: dendrite morphogenesis (A) and epithelial cell migration (C) are multicellular/neuronal processes irrelevant to a single-cell parasite's transporter, and alternative mRNA splicing (D) is a nuclear RNA-processing function with no structural or functional connection to a membrane-bound ATPase.",
    "missing_item_specific_fact": "None required. The ABC transporter motifs are directly readable from the supplied sequence, and the mapping from 'ABC transporter with transmembrane domains' to 'transmembrane transport' is standard textbook knowledge.",
    "reason": "A model with general knowledge of ABC transporter architecture (Walker A motif, ABC signature, transmembrane domains) can identify the protein as a membrane transporter and select 'transmembrane transport' over the three clearly incompatible distractors without needing to look up the specific UniProt entry or recall this protein's exact annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different functional categories (neural morphogenesis, cell migration, RNA splicing, membrane transport). Only B is consistent with a protein bearing ABC transporter motifs and transmembrane domains. No other option is defensible."
  },
  "important_caveats": [
    "The GO:0055085 annotation is IBA (Inferred by Biological aspect of Ancestor) from GO_Central, i.e., a family-level computational inference rather than a direct experimental GO assignment for this specific protein. However, the underlying experimental evidence (PubMed:39348385) independently confirms ATP-dependent transmembrane transport.",
    "The organism (Plasmodium falciparum) is not explicitly stated in the user input but is inferable from poly-asparagine stretches and sequence composition; even without this, the ABC transporter motifs suffice to eliminate the multicellular-process distractors.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark input and UniProt Q8IDH9."
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

**Accession:** `Q8IDH9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 148. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"CAD52642.1","source":"EMBL"}],"value":"ABC transporter B family member 6, putative"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39348385","source":"PubMed"}],"value":"PfABCB6"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39348385","source":"PubMed"}],"value":"PfMDR6"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39348385","source":"PubMed"}],"value":"7.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"ABC transporter ATM1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39348385","source":"PubMed"}],"value":"PfATM1"}]}}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39348385","source":"PubMed"}],"value":"Transports glutathione-coordinated [4Fe-4S] iron-sulfur clusters in an ATP-dependent manner (PubMed:39348385). Required for optimal parasite growth during erythrocytic stages (PubMed:39348385)"}]}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 65-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
CC   -!- FUNCTION: Transports glutathione-coordinated [4Fe-4S] iron-sulfur
CC       clusters in an ATP-dependent manner (PubMed:39348385). Required for
CC       optimal parasite growth during erythrocytic stages (PubMed:39348385).
CC       {ECO:0000269|PubMed:39348385}.
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 123-123`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
DR   GO; GO:0055085; P:transmembrane transport; IBA:GO_Central.
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 343246-343266`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0055085
name: transmembrane transport
namespace: biological_process
alt_id: GO:0090662
def: "The process in which a solute is transported across a lipid bilayer, from one side of a membrane to the other." [GOC:dph, GOC:jid]
comment: Transmembrane transport is the transport of a solute across a lipid bilayer. Note that transport through the nuclear pore complex is not transmembrane because the nuclear membrane is a double membrane and is not traversed. For transport through the nuclear pore, consider instead the term 'nucleocytoplasmic transport ; GO:0006913' and its children. Note also that this term is not intended for use in annotating lateral movement within membranes.
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_pombe
subset: goslim_yeast
synonym: "ATP hydrolysis coupled transmembrane transport" NARROW []
synonym: "membrane transport" EXACT []
xref: Reactome:R-HSA-382556 "ABC-family proteins mediated transport"
xref: Reactome:R-HSA-425407 "SLC-mediated transmembrane transport"
xref: Reactome:R-HSA-5223345 "Miscellaneous transport and binding events"
is_a: GO:0006810 ! transport
is_a: GO:0009987 ! cellular process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 150. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
