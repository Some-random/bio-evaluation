# GO_biological_process_0010

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — killing of cells of another organism

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQVTSLLILVCFIAAFQVFSRASSPVNCKWDSYGPWSECNGCTKTQTRRRSVAVYGQYGGYPCEGSAFETQSCKPERGCPTEEGCGDRFRCFSGQCISKSLVCNGDPDCEEDGADEDKCENVANPSCNIDKPPPNIELTGYGYNVVTGQGKKRVINTKSFGGQCRKVFSGDGKDFYRLSGNILSYTFQVKVDNDFNYEFYNSSWSYIKHTSTEQNTFYSWKGLFSHSRNTYGHGSAKEEIDTKMKSYKLLVVQNTVEVAQFTNNNPEFLQVAEPFWKELSHLPTLYDYSAYRRLIDQYGTHYLQSGSLGGEYRVLFYVDSGSAKETGFQSDQDNACSSADFQFLFTSSADQRCMKQLETEKSTSGNKGRLLRGKPLVRGGDSGFVADLSFLDLDNPAGNKQRYSSWAGSVTRLPQVIKEKLAPLYELVKEVPCASVKRLYLKRAIEEYFDEFDPCHCRPCQNGGLAIVVETQCQCLCKPYTFGSACEQGVLVGDQAGGVDGGWNCWSSWSPCVQGKRTRSRECNNPPPRDDGKSCLGETTESKQCEDQDLEKLRLLEPHCFHSSLAPKEFCLSPPALKDGFVQGEGTMVPVGQSVVYACDEGYSLIGDPVARCGEDLQWLVGEMHCQKLACVLPGEMNGMQSHPQKPFYMVGEKVTLSCVGGMSLEGPSTLLCGSSLKWSPELKDAKCVQKATSTPPPAAPACQPWEKLQNSKCICKMPYECGSSLDVCARDESRNKILSLTICKMHVVHCHKRNYTLVGKESCTLPSPAEKVCGACPIWSKCDAQNGKCICREASECQTAGYRICVEVNGKEETMSECEAGILRCRGQSISITAIKPCAEEAAQ

[Multiple Choices]
A. positive regulation of leukocyte adhesion to vascular endothelial cell
B. killing of cells of another organism
C. negative regulation of neuron projection development
D. DNA recombination
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

> The exact sequence matches mouse complement component C7. Its annotation assigns “killing of cells of another organism” to this protein, and the described role in the membrane attack complex provides a mechanistic basis: the complex forms pores in target-cell membranes and causes lysis. The GO assignment is IEA, and the function description is transferred from a human ortholog, so this supports the key without establishing direct experimental evidence for this mouse sequence.

Citations as saved: [H1](#evidence-h1), [H2](#evidence-h2), [H6](#evidence-h6), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a signal peptide and features consistent with a secreted extracellular protein, but those clues do not establish the specific process of killing another organism’s cells or reliably distinguish it from the other candidate processes.


**Missing item-specific fact**

> The identity and function of this particular protein as complement component C7, including its role as part of the membrane attack complex.


**Reason**

> Choosing B requires protein-specific functional knowledge or an annotation not supplied in the question. General sequence-based clues do not justify that precise biological-process assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, B is the one supported by the sequence-matched protein annotation and described function; the other options are not supported by the supplied sequence context.


### Important caveats

- The reviewer-only records match the supplied sequence, but the author’s exact source snapshot is unknown.
- The killing-process GO annotation is assigned by electronic inference; the functional description cites transfer from a human ortholog rather than direct experimental evidence for this mouse protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a signal peptide and features consistent with a secreted extracellular protein, but those clues do not establish the specific process of killing another organism’s cells or reliably distinguish it from the other candidate processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity and function of this particular protein as complement component C7, including its role as part of the membrane attack complex.",
    "reason": "Choosing B requires protein-specific functional knowledge or an annotation not supplied in the question. General sequence-based clues do not justify that precise biological-process assignment."
  },
  "case_id": "GO_biological_process_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H2",
      "H6",
      "C4",
      "C5",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches mouse complement component C7. Its annotation assigns “killing of cells of another organism” to this protein, and the described role in the membrane attack complex provides a mechanistic basis: the complex forms pores in target-cell membranes and causes lysis. The GO assignment is IEA, and the function description is transferred from a human ortholog, so this supports the key without establishing direct experimental evidence for this mouse sequence."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The killing-process GO annotation is assigned by electronic inference; the functional description cites transfer from a human ortholog rather than direct experimental evidence for this mouse protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B is the one supported by the sequence-matched protein annotation and described function; the other options are not supported by the supplied sequence context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches mouse complement component C7. Its annotation assigns “killing of cells of another organism” to this protein, and the described role in the membrane attack complex provides a mechanistic basis: the complex forms pores in target-cell membranes and causes lysis. The GO assignment is IEA, and the function description is transferred from a human ortholog, so this supports the key without establishing direct experimental evidence for this mouse sequence.",
    "evidence_ids": ["H1", "H2", "H6", "C4", "C5", "C8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a signal peptide and features consistent with a secreted extracellular protein, but those clues do not establish the specific process of killing another organism’s cells or reliably distinguish it from the other candidate processes.",
    "missing_item_specific_fact": "The identity and function of this particular protein as complement component C7, including its role as part of the membrane attack complex.",
    "reason": "Choosing B requires protein-specific functional knowledge or an annotation not supplied in the question. General sequence-based clues do not justify that precise biological-process assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B is the one supported by the sequence-matched protein annotation and described function; the other options are not supported by the supplied sequence context."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The killing-process GO annotation is assigned by electronic inference; the functional description cites transfer from a human ortholog rather than direct experimental evidence for this mouse protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt D3YXF5 (Complement component C7, mouse). The UniProt entry explicitly annotates GO:0031640 'killing of cells of another organism' (C8, current ISO:GO_Central; H6, historical IEA:UniProtKB-KW). The FUNCTION comment (C5, H2) describes C7 as a MAC component that 'inserts into a target cell membrane and forms a pore, leading to target cell membrane rupture and cell lysis,' which is mechanistically consistent with the GO:0031640 definition (GO3: 'results in the killing of cells of another organism'). The annotation is database-supported and functionally coherent.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If a model could recognize the MACPF (membrane attack complex/perforin) domain architecture and CCP/EGF-like/thrombospondin-type-1 repeat domains in the 845-aa sequence, it could reason: MACPF → membrane attack complex → pore formation → target cell lysis → killing of cells of another organism. Among the four choices, only B is consistent with complement/MAC biology; A (leukocyte adhesion), C (neuron projection), and D (DNA recombination) are unrelated to complement function.


**Missing item-specific fact**

> The critical bottleneck is identifying this 845-aa sequence as a complement/MAC component (specifically C7) from raw sequence alone. This requires either exact sequence memorization of D3YXF5 or specialized domain-recognition expertise (MACPF, CCP, TSP-1, EGF-like domains in the correct architecture). Without this identification step, the sequence provides no obvious feature that distinguishes B from A, C, or D. The annotation evidence codes (IEA:UniProtKB-KW historically, ISO:GO_Central currently) confirm this is a computational/transferred annotation, not an experimentally derived primary assignment.


**Reason**

> The reasoning chain from 'MAC protein' to 'killing cells' is biologically sound, but the prerequisite—identifying the protein family from 845 amino acids without tools—depends on specialized domain knowledge or exact sequence recall. General biological knowledge alone does not allow a model to extract MACPF/complement architecture from a raw sequence string. The question is answerable if the protein is correctly identified, but that identification step is lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only B (killing of cells of another organism) is consistent with complement/MAC biology. A (leukocyte adhesion to endothelium), C (neuron projection development), and D (DNA recombination) have no mechanistic connection to a secreted complement component. Although C7 is also annotated with 'complement activation' (GO:0006956), that term is not among the options. The author's choice of 'killing' over 'complement activation' as the 'primary' process is defensible given the MAC pore-forming/lytic function, but this distinction is moot since only B is present among the choices.


### Important caveats

- The GO:0031640 annotation uses computational evidence codes (IEA:UniProtKB-KW in the historical snapshot; ISO:GO_Central in the current entry), not direct experimental evidence specific to C7.
- The protein is also annotated with GO:0006956 'complement activation' (C6, H3), which is arguably a more specific process term. The author's selection of 'killing' as 'primary' is a judgment call, though it is the only complement-related option among the four choices.
- Sequence identity is confirmed (SHA-256 match, 845 aa), but the accession D3YXF5 was inferred from dataset metadata not available to the evaluated model.
- The MACPF domain is shared among C6, C7, C8α, C8β, and C9; distinguishing C7 specifically from other MAC components by sequence alone is extremely difficult without alignment tools.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If a model could recognize the MACPF (membrane attack complex/perforin) domain architecture and CCP/EGF-like/thrombospondin-type-1 repeat domains in the 845-aa sequence, it could reason: MACPF → membrane attack complex → pore formation → target cell lysis → killing of cells of another organism. Among the four choices, only B is consistent with complement/MAC biology; A (leukocyte adhesion), C (neuron projection), and D (DNA recombination) are unrelated to complement function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The critical bottleneck is identifying this 845-aa sequence as a complement/MAC component (specifically C7) from raw sequence alone. This requires either exact sequence memorization of D3YXF5 or specialized domain-recognition expertise (MACPF, CCP, TSP-1, EGF-like domains in the correct architecture). Without this identification step, the sequence provides no obvious feature that distinguishes B from A, C, or D. The annotation evidence codes (IEA:UniProtKB-KW historically, ISO:GO_Central currently) confirm this is a computational/transferred annotation, not an experimentally derived primary assignment.",
    "reason": "The reasoning chain from 'MAC protein' to 'killing cells' is biologically sound, but the prerequisite—identifying the protein family from 845 amino acids without tools—depends on specialized domain knowledge or exact sequence recall. General biological knowledge alone does not allow a model to extract MACPF/complement architecture from a raw sequence string. The question is answerable if the protein is correctly identified, but that identification step is lookup-dependent."
  },
  "case_id": "GO_biological_process_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H2",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt D3YXF5 (Complement component C7, mouse). The UniProt entry explicitly annotates GO:0031640 'killing of cells of another organism' (C8, current ISO:GO_Central; H6, historical IEA:UniProtKB-KW). The FUNCTION comment (C5, H2) describes C7 as a MAC component that 'inserts into a target cell membrane and forms a pore, leading to target cell membrane rupture and cell lysis,' which is mechanistically consistent with the GO:0031640 definition (GO3: 'results in the killing of cells of another organism'). The annotation is database-supported and functionally coherent."
  },
  "important_caveats": [
    "The GO:0031640 annotation uses computational evidence codes (IEA:UniProtKB-KW in the historical snapshot; ISO:GO_Central in the current entry), not direct experimental evidence specific to C7.",
    "The protein is also annotated with GO:0006956 'complement activation' (C6, H3), which is arguably a more specific process term. The author's selection of 'killing' as 'primary' is a judgment call, though it is the only complement-related option among the four choices.",
    "Sequence identity is confirmed (SHA-256 match, 845 aa), but the accession D3YXF5 was inferred from dataset metadata not available to the evaluated model.",
    "The MACPF domain is shared among C6, C7, C8α, C8β, and C9; distinguishing C7 specifically from other MAC components by sequence alone is extremely difficult without alignment tools."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only B (killing of cells of another organism) is consistent with complement/MAC biology. A (leukocyte adhesion to endothelium), C (neuron projection development), and D (DNA recombination) have no mechanistic connection to a secreted complement component. Although C7 is also annotated with 'complement activation' (GO:0006956), that term is not among the options. The author's choice of 'killing' over 'complement activation' as the 'primary' process is defensible given the MAC pore-forming/lytic function, but this distinction is moot since only B is present among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt D3YXF5 (Complement component C7, mouse). The UniProt entry explicitly annotates GO:0031640 'killing of cells of another organism' (C8, current ISO:GO_Central; H6, historical IEA:UniProtKB-KW). The FUNCTION comment (C5, H2) describes C7 as a MAC component that 'inserts into a target cell membrane and forms a pore, leading to target cell membrane rupture and cell lysis,' which is mechanistically consistent with the GO:0031640 definition (GO3: 'results in the killing of cells of another organism'). The annotation is database-supported and functionally coherent.",
    "evidence_ids": ["C4", "C5", "C8", "H2", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If a model could recognize the MACPF (membrane attack complex/perforin) domain architecture and CCP/EGF-like/thrombospondin-type-1 repeat domains in the 845-aa sequence, it could reason: MACPF → membrane attack complex → pore formation → target cell lysis → killing of cells of another organism. Among the four choices, only B is consistent with complement/MAC biology; A (leukocyte adhesion), C (neuron projection), and D (DNA recombination) are unrelated to complement function.",
    "missing_item_specific_fact": "The critical bottleneck is identifying this 845-aa sequence as a complement/MAC component (specifically C7) from raw sequence alone. This requires either exact sequence memorization of D3YXF5 or specialized domain-recognition expertise (MACPF, CCP, TSP-1, EGF-like domains in the correct architecture). Without this identification step, the sequence provides no obvious feature that distinguishes B from A, C, or D. The annotation evidence codes (IEA:UniProtKB-KW historically, ISO:GO_Central currently) confirm this is a computational/transferred annotation, not an experimentally derived primary assignment.",
    "reason": "The reasoning chain from 'MAC protein' to 'killing cells' is biologically sound, but the prerequisite—identifying the protein family from 845 amino acids without tools—depends on specialized domain knowledge or exact sequence recall. General biological knowledge alone does not allow a model to extract MACPF/complement architecture from a raw sequence string. The question is answerable if the protein is correctly identified, but that identification step is lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only B (killing of cells of another organism) is consistent with complement/MAC biology. A (leukocyte adhesion to endothelium), C (neuron projection development), and D (DNA recombination) have no mechanistic connection to a secreted complement component. Although C7 is also annotated with 'complement activation' (GO:0006956), that term is not among the options. The author's choice of 'killing' over 'complement activation' as the 'primary' process is defensible given the MAC pore-forming/lytic function, but this distinction is moot since only B is present among the choices."
  },
  "important_caveats": [
    "The GO:0031640 annotation uses computational evidence codes (IEA:UniProtKB-KW in the historical snapshot; ISO:GO_Central in the current entry), not direct experimental evidence specific to C7.",
    "The protein is also annotated with GO:0006956 'complement activation' (C6, H3), which is arguably a more specific process term. The author's selection of 'killing' as 'primary' is a judgment call, though it is the only complement-related option among the four choices.",
    "Sequence identity is confirmed (SHA-256 match, 845 aa), but the accession D3YXF5 was inferred from dataset metadata not available to the evaluated model.",
    "The MACPF domain is shared among C6, C7, C8α, C8β, and C9; distinguishing C7 specifically from other MAC components by sequence alone is extremely difficult without alignment tools."
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

**Accession:** `D3YXF5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 111. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Complement component C7"}}}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10643","source":"UniProtKB"}],"value":"Component of the membrane attack complex (MAC), a multiprotein complex activated by the complement cascade, which inserts into a target cell membrane and forms a pore, leading to target cell membrane rupture and cell lysis. The MAC is initiated by proteolytic cleavage of C5 into complement C5b in response to the classical, alternative, lectin and GZMK complement pathways. The complement pathways consist in a cascade of proteins that leads to phagocytosis and breakdown of pathogens and signaling that strengthens the adaptive immune system. C7 serves as a membrane anchor. During MAC assembly, associates with C5b and C6 to form the C5b-7 complex, a key lipophilic precursor of the MAC complex, which associates with the outer leaflet and reduces the energy for membrane bending"}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/uniProtKBCrossReferences/43`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"database":"GO","id":"GO:0006956","properties":[{"key":"GoTerm","value":"P:complement activation"},{"key":"GoEvidenceType","value":"ISO:GO_Central"}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/uniProtKBCrossReferences/44`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"database":"GO","id":"GO:0160257","properties":[{"key":"GoTerm","value":"P:complement activation, GZMK pathway"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/uniProtKBCrossReferences/45`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"database":"GO","id":"GO:0031640","properties":[{"key":"GoTerm","value":"P:killing of cells of another organism"},{"key":"GoEvidenceType","value":"ISO:GO_Central"}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/uniProtKBCrossReferences/46`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000303","id":"30552328","source":"PubMed"}],"id":"GO:0050778","properties":[{"key":"GoTerm","value":"P:positive regulation of immune response"},{"key":"GoEvidenceType","value":"NAS:ComplexPortal"}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 2.  
**Retrieved:** 2026-11-02T04:27:47.074801+00:00.  

```text
ID   CO7_MOUSE               Reviewed;         845 AA.
AC   D3YXF5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-OCT-2012, sequence version 2.
DT   28-JAN-2026, entry version 111.
DE   RecName: Full=Complement component C7 {ECO:0000305};
DE   Flags: Precursor;
GN   Name=C7 {ECO:0000312|MGI:MGI:88235};
OS   Mus musculus (Mouse).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Mus; Mus.
OX   NCBI_TaxID=10090;
```

Source SHA-256: `94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)  
**Locator:** `lines 27-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 2.  
**Retrieved:** 2026-11-02T04:27:47.074801+00:00.  

```text
CC   -!- FUNCTION: Component of the membrane attack complex (MAC), a
CC       multiprotein complex activated by the complement cascade, which inserts
CC       into a target cell membrane and forms a pore, leading to target cell
CC       membrane rupture and cell lysis. The MAC is initiated by proteolytic
CC       cleavage of C5 into complement C5b in response to the classical,
CC       alternative, lectin and GZMK complement pathways. The complement
CC       pathways consist in a cascade of proteins that leads to phagocytosis
CC       and breakdown of pathogens and signaling that strengthens the adaptive
CC       immune system. C7 serves as a membrane anchor. During MAC assembly,
CC       associates with C5b and C6 to form the C5b-7 complex, a key lipophilic
CC       precursor of the MAC complex, which associates with the outer leaflet
CC       and reduces the energy for membrane bending.
CC       {ECO:0000250|UniProtKB:P10643}.
```

Source SHA-256: `94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)  
**Locator:** `lines 102-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 2.  
**Retrieved:** 2026-11-02T04:27:47.074801+00:00.  

```text
DR   GO; GO:0006956; P:complement activation; ISO:GO_Central.
```

Source SHA-256: `94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)  
**Locator:** `lines 105-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 2.  
**Retrieved:** 2026-11-02T04:27:47.074801+00:00.  

```text
DR   GO; GO:0031640; P:killing of cells of another organism; IEA:UniProtKB-KW.
```

Source SHA-256: `94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 178549-178560`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031640
name: killing of cells of another organism
namespace: biological_process
alt_id: GO:0001908
alt_id: GO:0051852
def: "Any process in an organism that results in the killing of cells of another organism, including in some cases the death of the other organism. Killing here refers to the induction of death in one cell by another cell, not cell-autonomous death due to internal or other environmental conditions." [GOC:add]
subset: goslim_pir
synonym: "killing of cells of other organism" EXACT []
is_a: GO:0001906 ! cell killing
is_a: GO:0141061 ! disruption of cell in another organism

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
