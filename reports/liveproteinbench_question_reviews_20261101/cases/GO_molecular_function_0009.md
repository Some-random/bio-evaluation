# GO_molecular_function_0009

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — metal ion binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDTTMLQNAMQTDQAESKDLMNLAFFVRIIGLGVLPSVLVAVAKVNYPTWGKGLIQRAMTWGVSLVLLLVPIGLFSSQYASFFRVHKPVRFYINPITPIYSVGKLASIEYKKATAPTDTIYHAKDAVQTTKPSERKPRLVVFVVGETARADHVQFNGYGRETFPQLAKVDGLANFSQVTSCGTSTAYSVPCMFSYLGQDDYDVDTAKYQENVLDTLDRLGVGILWRDNNSDSKGVMDKLPATQYFDYKSATNNTICNTNPYNECRDVGMLVGLDDYVSANNGKDMLIMLHQMGNHGPAYFKRYDEQFAKFTPVCEGNELAKCEHQSLINAYDNALLATDDFIAKSIDWLKTHEANYDVAMLYVSDHGESLGENGVYLHGMPNAFAPKEQRAVPAFFWSNNTTFKPTASDTVLTHDAITPTLLKLFDVTAGKVKDRAAFIQ

[Multiple Choices]
A. metal ion binding
B. betaine-homocysteine S-methyltransferase activity
C. glycosyltransferase activity
D. D-threo-aldose 1-dehydrogenase activity
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

> The exact sequence has a UniProt GO annotation for metal ion binding (IEA: UniProtKB-KW), and a cited crystal structure reports the protein in complex with Zn2+. These support option A, though the annotation is computational and the structure alone does not establish physiological metal dependence. The cited catalytic activity is phosphatidylethanolamine transfer to lipid A, which is not among the choices.

Citations as saved: [H2](#evidence-h2), [H5](#evidence-h5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly membrane-associated, which can make soluble-enzyme choices B and D less plausible, but its hydrophobic segments and residues alone do not establish metal-ion binding or distinguish it reliably from a membrane-associated transferase.


**Missing item-specific fact**

> The protein-specific metal-binding annotation or evidence such as the reported Zn2+-bound structure is needed to select A; the sequence does not establish that fact.


**Reason**

> The key distinction depends on protein-specific annotation or structural evidence absent from the prompt. Knowing the exact protein identity and its database or structure record would resolve it, but that is lookup or memorization rather than reasoning from the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A has supporting annotation and structural evidence, but it is not the protein's reported primary catalytic activity: phosphatidylethanolamine transfer to lipid A is not offered. The other listed enzymatic activities are not supported by the supplied evidence.


### Important caveats

- The GO metal-ion-binding annotation is IEA, not direct experimental evidence of physiological metal dependence.
- The catalytic activity evidence is attributed to a cited study; it should not be conflated with the evidence supporting the GO metal-binding term.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly membrane-associated, which can make soluble-enzyme choices B and D less plausible, but its hydrophobic segments and residues alone do not establish metal-ion binding or distinguish it reliably from a membrane-associated transferase.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific metal-binding annotation or evidence such as the reported Zn2+-bound structure is needed to select A; the sequence does not establish that fact.",
    "reason": "The key distinction depends on protein-specific annotation or structural evidence absent from the prompt. Knowing the exact protein identity and its database or structure record would resolve it, but that is lookup or memorization rather than reasoning from the supplied sequence."
  },
  "case_id": "GO_molecular_function_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence has a UniProt GO annotation for metal ion binding (IEA: UniProtKB-KW), and a cited crystal structure reports the protein in complex with Zn2+. These support option A, though the annotation is computational and the structure alone does not establish physiological metal dependence. The cited catalytic activity is phosphatidylethanolamine transfer to lipid A, which is not among the choices."
  },
  "important_caveats": [
    "The GO metal-ion-binding annotation is IEA, not direct experimental evidence of physiological metal dependence.",
    "The catalytic activity evidence is attributed to a cited study; it should not be conflated with the evidence supporting the GO metal-binding term."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A has supporting annotation and structural evidence, but it is not the protein's reported primary catalytic activity: phosphatidylethanolamine transfer to lipid A is not offered. The other listed enzymatic activities are not supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence has a UniProt GO annotation for metal ion binding (IEA: UniProtKB-KW), and a cited crystal structure reports the protein in complex with Zn2+. These support option A, though the annotation is computational and the structure alone does not establish physiological metal dependence. The cited catalytic activity is phosphatidylethanolamine transfer to lipid A, which is not among the choices.",
    "evidence_ids": ["H2", "H5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly membrane-associated, which can make soluble-enzyme choices B and D less plausible, but its hydrophobic segments and residues alone do not establish metal-ion binding or distinguish it reliably from a membrane-associated transferase.",
    "missing_item_specific_fact": "The protein-specific metal-binding annotation or evidence such as the reported Zn2+-bound structure is needed to select A; the sequence does not establish that fact.",
    "reason": "The key distinction depends on protein-specific annotation or structural evidence absent from the prompt. Knowing the exact protein identity and its database or structure record would resolve it, but that is lookup or memorization rather than reasoning from the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A has supporting annotation and structural evidence, but it is not the protein's reported primary catalytic activity: phosphatidylethanolamine transfer to lipid A is not offered. The other listed enzymatic activities are not supported by the supplied evidence."
  },
  "important_caveats": [
    "The GO metal-ion-binding annotation is IEA, not direct experimental evidence of physiological metal dependence.",
    "The catalytic activity evidence is attributed to a cited study; it should not be conflated with the evidence supporting the GO metal-binding term."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is MCR-2 (Phosphatidylethanolamine transferase, EC 2.7.8.43, UniProt A0A1C3NEV1). GO:0046872 (metal ion binding) is annotated in the UniProt entry (IEA:UniProtKB-KW, evidence_id H5), and X-ray crystallography of PDB 6A7W confirms the protein in complex with Zn2+ (evidence_id C8/H2). Among the four options, A is the only one with any connection to this protein: B (betaine-homocysteine S-methyltransferase, EC 2.1.1.5), C (glycosyltransferase, EC 2.4.-.-), and D (D-threo-aldose 1-dehydrogenase, EC 1.1.1.122) are entirely unrelated enzyme activities. However, the true primary molecular function is phosphotransferase/transferase activity (EC 2.7.8.43), not metal ion binding; zinc coordination is a cofactor role supporting catalysis. The key is defensible as the best available option but mislabels a secondary/auxiliary function as the 'primary' one.

Citations as saved: [H5](#evidence-h5), [C8](#evidence-c8), [H2](#evidence-h2), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Elimination reasoning provides partial support: the sequence shows multiple transmembrane helices indicating a membrane protein, which makes B (cytosolic S-methyltransferase) and D (soluble oxidoreductase) implausible. C (glycosyltransferase) is the wrong transferase subclass. This leaves A by elimination. However, this elimination path does not positively identify 'metal ion binding' as the PRIMARY molecular function; it merely identifies the least-wrong option.


**Missing item-specific fact**

> The protein's actual primary molecular function is phosphotransferase activity (EC 2.7.8.43, phosphatidylethanolamine transferase), which is not offered as an option. Confirming that zinc binding (rather than the transferase activity itself) is the intended 'primary' answer requires knowing the specific UniProt annotation for MCR-2 and that the benchmark selected the KW-based GO:0046872 entry. Without recognizing this as MCR-2 or knowing its annotation profile, a model that correctly infers transferase activity from sequence motifs would find no matching option and could not confidently select 'metal ion binding' as the primary function.


**Reason**

> The answer depends on item-specific annotation knowledge (this protein is MCR-2, annotated with GO:0046872 metal ion binding via KW). General reasoning can eliminate B, C, and D based on enzyme-class and membrane-protein context, but cannot positively establish 'metal ion binding' as the primary molecular function of an uncharacterized membrane protein. The correct primary function (phosphotransferase) is absent from the options, making the selection of A dependent on knowing the database annotation rather than on biological reasoning about the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B, C, and D are clearly incompatible with a multi-TM membrane protein and with the enzyme class of MCR-2. A is the only option with any experimental or annotation support. However, the question's framing ('primary molecular function') is misleading because metal ion binding is a cofactor/auxiliary function, not the primary catalytic function. This does not create a second defensible option among the choices, but it weakens the biological validity of the question.


### Important caveats

- The GO:0046872 annotation is IEA:UniProtKB-KW (computational keyword assignment), not an experimentally curated primary-function annotation. The Zn2+ binding is confirmed by X-ray crystallography (PDB 6A7W), but in the context of the catalytic mechanism.
- The protein's primary molecular function is phosphatidylethanolamine transferase (EC 2.7.8.43), a phosphotransferase. 'Metal ion binding' is a secondary/auxiliary molecular function. The question's phrasing ('primary molecular function') is therefore inaccurate for the selected key.
- The GO annotation for the actual primary function (GO:0016776, phosphotransferase activity) is IEA:TreeGrafter (computational), and is not offered as an option.
- The sequence-match is confirmed (SHA256 match, 538 aa, both current and historical entry version 38).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Elimination reasoning provides partial support: the sequence shows multiple transmembrane helices indicating a membrane protein, which makes B (cytosolic S-methyltransferase) and D (soluble oxidoreductase) implausible. C (glycosyltransferase) is the wrong transferase subclass. This leaves A by elimination. However, this elimination path does not positively identify 'metal ion binding' as the PRIMARY molecular function; it merely identifies the least-wrong option.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's actual primary molecular function is phosphotransferase activity (EC 2.7.8.43, phosphatidylethanolamine transferase), which is not offered as an option. Confirming that zinc binding (rather than the transferase activity itself) is the intended 'primary' answer requires knowing the specific UniProt annotation for MCR-2 and that the benchmark selected the KW-based GO:0046872 entry. Without recognizing this as MCR-2 or knowing its annotation profile, a model that correctly infers transferase activity from sequence motifs would find no matching option and could not confidently select 'metal ion binding' as the primary function.",
    "reason": "The answer depends on item-specific annotation knowledge (this protein is MCR-2, annotated with GO:0046872 metal ion binding via KW). General reasoning can eliminate B, C, and D based on enzyme-class and membrane-protein context, but cannot positively establish 'metal ion binding' as the primary molecular function of an uncharacterized membrane protein. The correct primary function (phosphotransferase) is absent from the options, making the selection of A dependent on knowing the database annotation rather than on biological reasoning about the sequence."
  },
  "case_id": "GO_molecular_function_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "C8",
      "H2",
      "C4",
      "C5",
      "C6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein is MCR-2 (Phosphatidylethanolamine transferase, EC 2.7.8.43, UniProt A0A1C3NEV1). GO:0046872 (metal ion binding) is annotated in the UniProt entry (IEA:UniProtKB-KW, evidence_id H5), and X-ray crystallography of PDB 6A7W confirms the protein in complex with Zn2+ (evidence_id C8/H2). Among the four options, A is the only one with any connection to this protein: B (betaine-homocysteine S-methyltransferase, EC 2.1.1.5), C (glycosyltransferase, EC 2.4.-.-), and D (D-threo-aldose 1-dehydrogenase, EC 1.1.1.122) are entirely unrelated enzyme activities. However, the true primary molecular function is phosphotransferase/transferase activity (EC 2.7.8.43), not metal ion binding; zinc coordination is a cofactor role supporting catalysis. The key is defensible as the best available option but mislabels a secondary/auxiliary function as the 'primary' one."
  },
  "important_caveats": [
    "The GO:0046872 annotation is IEA:UniProtKB-KW (computational keyword assignment), not an experimentally curated primary-function annotation. The Zn2+ binding is confirmed by X-ray crystallography (PDB 6A7W), but in the context of the catalytic mechanism.",
    "The protein's primary molecular function is phosphatidylethanolamine transferase (EC 2.7.8.43), a phosphotransferase. 'Metal ion binding' is a secondary/auxiliary molecular function. The question's phrasing ('primary molecular function') is therefore inaccurate for the selected key.",
    "The GO annotation for the actual primary function (GO:0016776, phosphotransferase activity) is IEA:TreeGrafter (computational), and is not offered as an option.",
    "The sequence-match is confirmed (SHA256 match, 538 aa, both current and historical entry version 38)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B, C, and D are clearly incompatible with a multi-TM membrane protein and with the enzyme class of MCR-2. A is the only option with any experimental or annotation support. However, the question's framing ('primary molecular function') is misleading because metal ion binding is a cofactor/auxiliary function, not the primary catalytic function. This does not create a second defensible option among the choices, but it weakens the biological validity of the question."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is MCR-2 (Phosphatidylethanolamine transferase, EC 2.7.8.43, UniProt A0A1C3NEV1). GO:0046872 (metal ion binding) is annotated in the UniProt entry (IEA:UniProtKB-KW, evidence_id H5), and X-ray crystallography of PDB 6A7W confirms the protein in complex with Zn2+ (evidence_id C8/H2). Among the four options, A is the only one with any connection to this protein: B (betaine-homocysteine S-methyltransferase, EC 2.1.1.5), C (glycosyltransferase, EC 2.4.-.-), and D (D-threo-aldose 1-dehydrogenase, EC 1.1.1.122) are entirely unrelated enzyme activities. However, the true primary molecular function is phosphotransferase/transferase activity (EC 2.7.8.43), not metal ion binding; zinc coordination is a cofactor role supporting catalysis. The key is defensible as the best available option but mislabels a secondary/auxiliary function as the 'primary' one.",
    "evidence_ids": ["H5", "C8", "H2", "C4", "C5", "C6", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Elimination reasoning provides partial support: the sequence shows multiple transmembrane helices indicating a membrane protein, which makes B (cytosolic S-methyltransferase) and D (soluble oxidoreductase) implausible. C (glycosyltransferase) is the wrong transferase subclass. This leaves A by elimination. However, this elimination path does not positively identify 'metal ion binding' as the PRIMARY molecular function; it merely identifies the least-wrong option.",
    "missing_item_specific_fact": "The protein's actual primary molecular function is phosphotransferase activity (EC 2.7.8.43, phosphatidylethanolamine transferase), which is not offered as an option. Confirming that zinc binding (rather than the transferase activity itself) is the intended 'primary' answer requires knowing the specific UniProt annotation for MCR-2 and that the benchmark selected the KW-based GO:0046872 entry. Without recognizing this as MCR-2 or knowing its annotation profile, a model that correctly infers transferase activity from sequence motifs would find no matching option and could not confidently select 'metal ion binding' as the primary function.",
    "reason": "The answer depends on item-specific annotation knowledge (this protein is MCR-2, annotated with GO:0046872 metal ion binding via KW). General reasoning can eliminate B, C, and D based on enzyme-class and membrane-protein context, but cannot positively establish 'metal ion binding' as the primary molecular function of an uncharacterized membrane protein. The correct primary function (phosphotransferase) is absent from the options, making the selection of A dependent on knowing the database annotation rather than on biological reasoning about the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B, C, and D are clearly incompatible with a multi-TM membrane protein and with the enzyme class of MCR-2. A is the only option with any experimental or annotation support. However, the question's framing ('primary molecular function') is misleading because metal ion binding is a cofactor/auxiliary function, not the primary catalytic function. This does not create a second defensible option among the choices, but it weakens the biological validity of the question."
  },
  "important_caveats": [
    "The GO:0046872 annotation is IEA:UniProtKB-KW (computational keyword assignment), not an experimentally curated primary-function annotation. The Zn2+ binding is confirmed by X-ray crystallography (PDB 6A7W), but in the context of the catalytic mechanism.",
    "The protein's primary molecular function is phosphatidylethanolamine transferase (EC 2.7.8.43), a phosphotransferase. 'Metal ion binding' is a secondary/auxiliary molecular function. The question's phrasing ('primary molecular function') is therefore inaccurate for the selected key.",
    "The GO annotation for the actual primary function (GO:0016776, phosphotransferase activity) is IEA:TreeGrafter (computational), and is not offered as an option.",
    "The sequence-match is confirmed (SHA256 match, 538 aa, both current and historical entry version 38)."
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

**Accession:** `A0A1C3NEV1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0R6L508","source":"UniProtKB"}],"value":"Polymyxin resistance protein MCR-2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30194678","source":"PubMed"}],"value":"2.7.8.43"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30194678","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"Ref.1","source":"Reference"}],"value":"Phosphatidylethanolamine transferase Mcr-2"}}}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0R6L508","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"30194678","source":"PubMed"}],"value":"Probably catalyzes the addition of a phosphoethanolamine moiety to lipid A (PubMed:30194678). Phosphoethanolamine modification of lipid A confers polymyxin resistance (By similarity). Confers resistance to polymyxin-type antibiotics such as colistin (PubMed:30194678)"}]}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.8.43","evidences":[{"evidenceCode":"ECO:0000305","id":"30194678","source":"PubMed"}],"name":"lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46900"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17815"},{"database":"ChEBI","id":"CHEBI:64612"},{"database":"ChEBI","id":"CHEBI:87097"},{"database":"ChEBI","id":"CHEBI:134257"}]}}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"citation":{"authors":["Wang X.","Lu Q.","Qi J.","Chai Y.","Wang Y.","Gao G.F."],"citationCrossReferences":[{"database":"PubMed","id":"30194678"},{"database":"DOI","id":"10.1007/s11427-018-9363-4"}],"citationType":"journal article","firstPage":"1432","id":"30194678","journal":"Sci. China Life Sci.","lastPage":"1436","publicationDate":"2018","title":"Structural and functional insights into MCR-2 mediated colistin resistance.","volume":"61"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6A7W","source":"PDB"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"WHI04997.1","source":"EMBL"}],"type":"PLASMID","value":"unnamed5"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+)","DISULFIDE BONDS","FUNCTION","CATALYTIC ACTIVITY","MUTAGENESIS OF PHE-91; TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283; LYS-331 AND HIS-476"]}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 44-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
RN   [4] {ECO:0007744|PDB:6A7W}
RP   X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+),
RP   DISULFIDE BONDS, FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF PHE-91;
RP   TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283;
RP   LYS-331 AND HIS-476.
RC   PLASMID=unnamed5 {ECO:0000312|EMBL:WHI04997.1};
RX   PubMed=30194678; DOI=10.1007/s11427-018-9363-4;
RA   Wang X., Lu Q., Qi J., Chai Y., Wang Y., Gao G.F.;
RT   "Structural and functional insights into MCR-2 mediated colistin
RT   resistance.";
RL   Sci. China Life Sci. 61:1432-1436(2018).
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 72-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-
CC         phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate)
CC         (E. coli) + a 1,2-diacyl-sn-glycerol; Xref=Rhea:RHEA:46900,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17815, ChEBI:CHEBI:64612,
CC         ChEBI:CHEBI:87097, ChEBI:CHEBI:134257; EC=2.7.8.43;
CC         Evidence={ECO:0000305|PubMed:30194678};
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 106-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 281280-281292`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0046872
name: metal ion binding
namespace: molecular_function
def: "Binding to a metal ion." [GOC:ai]
subset: goslim_agr
subset: goslim_drosophila
subset: goslim_flybase_ribbon
subset: goslim_metagenomics
synonym: "heavy metal binding" NARROW []
synonym: "metal binding" EXACT []
is_a: GO:0043169 ! cation binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
