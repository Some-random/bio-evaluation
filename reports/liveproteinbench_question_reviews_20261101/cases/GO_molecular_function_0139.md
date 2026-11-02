# GO_molecular_function_0139

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — metal ion binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEDFVRQCFNPMIVELAEKAMKEYGEDPKIETNKFAAICTHLEVCFMYSDFHFIDERGESIIVESGDPNALLKHRFEIIEGRDRIMAWTVVNSICNTTGVEKPKFLPDLYDYKENRFIEIGVTRREVHIYYLEKANKIKSEKTHIHIFSFTGEEMATKADYTLDEESRARIKTRLFTIRQEMASRSLWDSFRQSERGEETIEEKFEITGTMRKLADQSLPPNFPSLENFRAYVDGFEPNGCIEGKLSQMSKEVNAKIEPFLRTTPRPLRLPDGPLCHQRSKFLLMDALKLSIEDPSHEGEGIPLYDAIKCMKTFFGWKEPNIVKPHEKGINPNYLMAWKQVLAELQDIENEEKIPRTKNMKRTSQLKWALGENMAPEKVDFDDCKDVGDLKQYDSDEPEPRSLASWVQNEFNKACELTDSSWIELDEIGEDVAPIEHIASMRRNYFTAEVSHCRATEYIMKGVYINTALLNASCAAMDDFQLIPMISKCRTKEGRRKTNLYGFIIKGRSHLRNDTDVVNFVSMEFSLTDPRLEPHKWEKYCVLEIGDMLLRTAIGQVSRPMFLYVRTNGTSKIKMKWGMEMRRCLLQSLQQIESMIEAESSVKEKDMTKEFFENKSETWPIGESPRGVEEGSIGKVCRTLLAKSVFNSLYASPQLEGFSAESRKLLLIVQALRDNLEPGTFDLGGLYEAIEECLINDPWVLLNASWFNSFLTHALK

[Multiple Choices]
A. cyclosporin A binding
B. single-stranded DNA endodeoxyribonuclease activity
C. molecular condensate scaffold activity
D. metal ion binding
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

> The matched sequence has a UniProt GO annotation for metal ion binding (IEA:UniProtKB-KW). Its annotation describes an endonuclease function involved in viral cap-snatching, consistent with metal-dependent catalysis. The annotation is computationally assigned, not experimental proof. The DNA-specific wording of option B does not match the described cleavage of host capped pre-mRNAs.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently distinctive, reliable basis to infer this particular protein's metal-binding function and distinguish it from the listed alternatives; doing so requires identifying its protein-specific function.


**Missing item-specific fact**

> That the sequence is influenza A polymerase acidic protein, whose endonuclease activity is associated with metal-ion binding.


**Reason**

> The input supplies only a long sequence and choices, without viral or polymerase context. The reviewer-only identity and annotations support the key but were not available to the evaluated model; recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Metal ion binding is supported for this protein. Option B specifies single-stranded DNA endonuclease activity, whereas the protein's described endonuclease role is cleavage of host capped pre-mRNAs.


### Important caveats

- The metal ion binding GO annotation is computationally inferred (IEA:UniProtKB-KW), not direct experimental evidence in the supplied excerpts.
- The exact author source snapshot is unknown, although the sequence matches the current and archived UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently distinctive, reliable basis to infer this particular protein's metal-binding function and distinguish it from the listed alternatives; doing so requires identifying its protein-specific function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That the sequence is influenza A polymerase acidic protein, whose endonuclease activity is associated with metal-ion binding.",
    "reason": "The input supplies only a long sequence and choices, without viral or polymerase context. The reviewer-only identity and annotations support the key but were not available to the evaluated model; recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from supplied context."
  },
  "case_id": "GO_molecular_function_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt GO annotation for metal ion binding (IEA:UniProtKB-KW). Its annotation describes an endonuclease function involved in viral cap-snatching, consistent with metal-dependent catalysis. The annotation is computationally assigned, not experimental proof. The DNA-specific wording of option B does not match the described cleavage of host capped pre-mRNAs."
  },
  "important_caveats": [
    "The metal ion binding GO annotation is computationally inferred (IEA:UniProtKB-KW), not direct experimental evidence in the supplied excerpts.",
    "The exact author source snapshot is unknown, although the sequence matches the current and archived UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Metal ion binding is supported for this protein. Option B specifies single-stranded DNA endonuclease activity, whereas the protein's described endonuclease role is cleavage of host capped pre-mRNAs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt GO annotation for metal ion binding (IEA:UniProtKB-KW). Its annotation describes an endonuclease function involved in viral cap-snatching, consistent with metal-dependent catalysis. The annotation is computationally assigned, not experimental proof. The DNA-specific wording of option B does not match the described cleavage of host capped pre-mRNAs.",
    "evidence_ids": ["C5", "C8", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently distinctive, reliable basis to infer this particular protein's metal-binding function and distinguish it from the listed alternatives; doing so requires identifying its protein-specific function.",
    "missing_item_specific_fact": "That the sequence is influenza A polymerase acidic protein, whose endonuclease activity is associated with metal-ion binding.",
    "reason": "The input supplies only a long sequence and choices, without viral or polymerase context. The reviewer-only identity and annotations support the key but were not available to the evaluated model; recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Metal ion binding is supported for this protein. Option B specifies single-stranded DNA endonuclease activity, whereas the protein's described endonuclease role is cleavage of host capped pre-mRNAs."
  },
  "important_caveats": [
    "The metal ion binding GO annotation is computationally inferred (IEA:UniProtKB-KW), not direct experimental evidence in the supplied excerpts.",
    "The exact author source snapshot is unknown, although the sequence matches the current and archived UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Influenza A virus PA (Polymerase Acidic protein, UniProt C3W5S0). UniProt annotates GO:0046872 (metal ion binding, IEA:UniProtKB-KW) for this entry (evidence C8, H5). The PA subunit's endonuclease domain coordinates Mn²⁺/Mg²⁺ ions for cap-snatching cleavage of host capped pre-mRNAs, making metal ion binding a genuine molecular function. However, the true primary molecular function is endonuclease activity (GO:0004519, also annotated), not metal ion binding per se. Among the four offered choices, D is the only one actually annotated for this protein: A (cyclosporin A binding) is irrelevant to influenza PA; B (single-stranded DNA endodeoxyribonuclease activity, GO:0000014) specifies DNA substrate, whereas PA is an RNA endonuclease; C (molecular condensate scaffold activity) is not associated with PA. Thus D is the best available answer, though 'primary molecular function' is a loose descriptor since the primary catalytic activity (RNA endonuclease) is not among the choices.

Citations as saved: [C8](#evidence-c8), [H5](#evidence-h5), [C5](#evidence-c5), [H2](#evidence-h2), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO3](#evidence-go3), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Influenza A PA is a well-characterized metal-dependent endonuclease subunit of the viral RNA polymerase complex. Its cap-snatching endonuclease domain uses coordinated divalent metal ions (Mn²⁺/Mg²⁺) for catalysis, so metal ion binding is a direct consequence of its enzymatic mechanism. Option B can be eliminated because PA cleaves RNA (host capped pre-mRNAs), not single-stranded DNA; the GO term GO:0000014 specifically refers to DNA endodeoxyribonuclease activity. Option A (cyclosporin A binding) is associated with cyclophilin-family peptidyl-prolyl isomerases, entirely unrelated to viral polymerase subunits. Option C (molecular condensate scaffold activity) is not a recognized function of influenza PA. A model with general virology/biochemistry knowledge of influenza polymerase biology can reason through these eliminations without needing the specific GO annotation list.


**Missing item-specific fact**

> None strictly required. The general knowledge that PA is a metal-dependent RNA endonuclease (not a DNA endonuclease, not a cyclophilin, not a condensate scaffold) is standard virology textbook material and suffices to select D among the four options.


**Reason**

> The sequence is from the extremely well-studied Influenza A PA protein. General biological knowledge of its metal-dependent endonuclease mechanism, combined with the substrate-specificity distinction (RNA vs. DNA) that eliminates option B, provides a concrete reasoning path. The other distractors (A, C) are eliminated by category mismatch. No protein-specific experimental measurement or obscure annotation lookup is needed beyond standard virology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the question asks for the 'primary molecular function' and the true primary function (RNA endonuclease activity, GO:0004519) is not among the choices, the wording combined with the available options yields a unique defensible answer. B is wrong substrate (DNA vs RNA), A and C are unrelated protein categories. D is the only annotated molecular function among the four. The 'primary' qualifier is imprecise but does not create genuine ambiguity among the given choices.


### Important caveats

- The true primary molecular function of PA is endonuclease activity (GO:0004519), not metal ion binding. The question's use of 'primary molecular function' is imprecise; D is correct only because the actual primary function is absent from the choices.
- The GO annotation for metal ion binding carries evidence code IEA:UniProtKB-KW (inferred from keyword), not experimental evidence. The metal-dependence of PA endonuclease is well-established structurally and biochemically, but the specific GO annotation is computationally derived.
- The sequence is from the 2009 pandemic H1N1 strain (A/California/04/2009). PA function is conserved across influenza A strains, so this does not affect the answer.
- Option B (GO:0000014, single-stranded DNA endodeoxyribonuclease activity) is a deliberate near-miss: it captures 'endonuclease' but specifies DNA rather than RNA substrate. This tests substrate-specificity knowledge.
- The identity of the protein as Influenza A PA requires either sequence recognition or database lookup; however, the reasoning path from 'viral polymerase subunit' to 'metal-dependent endonuclease' is general virology knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Influenza A PA is a well-characterized metal-dependent endonuclease subunit of the viral RNA polymerase complex. Its cap-snatching endonuclease domain uses coordinated divalent metal ions (Mn²⁺/Mg²⁺) for catalysis, so metal ion binding is a direct consequence of its enzymatic mechanism. Option B can be eliminated because PA cleaves RNA (host capped pre-mRNAs), not single-stranded DNA; the GO term GO:0000014 specifically refers to DNA endodeoxyribonuclease activity. Option A (cyclosporin A binding) is associated with cyclophilin-family peptidyl-prolyl isomerases, entirely unrelated to viral polymerase subunits. Option C (molecular condensate scaffold activity) is not a recognized function of influenza PA. A model with general virology/biochemistry knowledge of influenza polymerase biology can reason through these eliminations without needing the specific GO annotation list.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The general knowledge that PA is a metal-dependent RNA endonuclease (not a DNA endonuclease, not a cyclophilin, not a condensate scaffold) is standard virology textbook material and suffices to select D among the four options.",
    "reason": "The sequence is from the extremely well-studied Influenza A PA protein. General biological knowledge of its metal-dependent endonuclease mechanism, combined with the substrate-specificity distinction (RNA vs. DNA) that eliminates option B, provides a concrete reasoning path. The other distractors (A, C) are eliminated by category mismatch. No protein-specific experimental measurement or obscure annotation lookup is needed beyond standard virology knowledge."
  },
  "case_id": "GO_molecular_function_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H5",
      "C5",
      "H2",
      "GO1",
      "GO2",
      "GO3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein is Influenza A virus PA (Polymerase Acidic protein, UniProt C3W5S0). UniProt annotates GO:0046872 (metal ion binding, IEA:UniProtKB-KW) for this entry (evidence C8, H5). The PA subunit's endonuclease domain coordinates Mn²⁺/Mg²⁺ ions for cap-snatching cleavage of host capped pre-mRNAs, making metal ion binding a genuine molecular function. However, the true primary molecular function is endonuclease activity (GO:0004519, also annotated), not metal ion binding per se. Among the four offered choices, D is the only one actually annotated for this protein: A (cyclosporin A binding) is irrelevant to influenza PA; B (single-stranded DNA endodeoxyribonuclease activity, GO:0000014) specifies DNA substrate, whereas PA is an RNA endonuclease; C (molecular condensate scaffold activity) is not associated with PA. Thus D is the best available answer, though 'primary molecular function' is a loose descriptor since the primary catalytic activity (RNA endonuclease) is not among the choices."
  },
  "important_caveats": [
    "The true primary molecular function of PA is endonuclease activity (GO:0004519), not metal ion binding. The question's use of 'primary molecular function' is imprecise; D is correct only because the actual primary function is absent from the choices.",
    "The GO annotation for metal ion binding carries evidence code IEA:UniProtKB-KW (inferred from keyword), not experimental evidence. The metal-dependence of PA endonuclease is well-established structurally and biochemically, but the specific GO annotation is computationally derived.",
    "The sequence is from the 2009 pandemic H1N1 strain (A/California/04/2009). PA function is conserved across influenza A strains, so this does not affect the answer.",
    "Option B (GO:0000014, single-stranded DNA endodeoxyribonuclease activity) is a deliberate near-miss: it captures 'endonuclease' but specifies DNA rather than RNA substrate. This tests substrate-specificity knowledge.",
    "The identity of the protein as Influenza A PA requires either sequence recognition or database lookup; however, the reasoning path from 'viral polymerase subunit' to 'metal-dependent endonuclease' is general virology knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for the 'primary molecular function' and the true primary function (RNA endonuclease activity, GO:0004519) is not among the choices, the wording combined with the available options yields a unique defensible answer. B is wrong substrate (DNA vs RNA), A and C are unrelated protein categories. D is the only annotated molecular function among the four. The 'primary' qualifier is imprecise but does not create genuine ambiguity among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Influenza A virus PA (Polymerase Acidic protein, UniProt C3W5S0). UniProt annotates GO:0046872 (metal ion binding, IEA:UniProtKB-KW) for this entry (evidence C8, H5). The PA subunit's endonuclease domain coordinates Mn²⁺/Mg²⁺ ions for cap-snatching cleavage of host capped pre-mRNAs, making metal ion binding a genuine molecular function. However, the true primary molecular function is endonuclease activity (GO:0004519, also annotated), not metal ion binding per se. Among the four offered choices, D is the only one actually annotated for this protein: A (cyclosporin A binding) is irrelevant to influenza PA; B (single-stranded DNA endodeoxyribonuclease activity, GO:0000014) specifies DNA substrate, whereas PA is an RNA endonuclease; C (molecular condensate scaffold activity) is not associated with PA. Thus D is the best available answer, though 'primary molecular function' is a loose descriptor since the primary catalytic activity (RNA endonuclease) is not among the choices.",
    "evidence_ids": ["C8", "H5", "C5", "H2", "GO1", "GO2", "GO3", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Influenza A PA is a well-characterized metal-dependent endonuclease subunit of the viral RNA polymerase complex. Its cap-snatching endonuclease domain uses coordinated divalent metal ions (Mn²⁺/Mg²⁺) for catalysis, so metal ion binding is a direct consequence of its enzymatic mechanism. Option B can be eliminated because PA cleaves RNA (host capped pre-mRNAs), not single-stranded DNA; the GO term GO:0000014 specifically refers to DNA endodeoxyribonuclease activity. Option A (cyclosporin A binding) is associated with cyclophilin-family peptidyl-prolyl isomerases, entirely unrelated to viral polymerase subunits. Option C (molecular condensate scaffold activity) is not a recognized function of influenza PA. A model with general virology/biochemistry knowledge of influenza polymerase biology can reason through these eliminations without needing the specific GO annotation list.",
    "missing_item_specific_fact": "None strictly required. The general knowledge that PA is a metal-dependent RNA endonuclease (not a DNA endonuclease, not a cyclophilin, not a condensate scaffold) is standard virology textbook material and suffices to select D among the four options.",
    "reason": "The sequence is from the extremely well-studied Influenza A PA protein. General biological knowledge of its metal-dependent endonuclease mechanism, combined with the substrate-specificity distinction (RNA vs. DNA) that eliminates option B, provides a concrete reasoning path. The other distractors (A, C) are eliminated by category mismatch. No protein-specific experimental measurement or obscure annotation lookup is needed beyond standard virology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for the 'primary molecular function' and the true primary function (RNA endonuclease activity, GO:0004519) is not among the choices, the wording combined with the available options yields a unique defensible answer. B is wrong substrate (DNA vs RNA), A and C are unrelated protein categories. D is the only annotated molecular function among the four. The 'primary' qualifier is imprecise but does not create genuine ambiguity among the given choices."
  },
  "important_caveats": [
    "The true primary molecular function of PA is endonuclease activity (GO:0004519), not metal ion binding. The question's use of 'primary molecular function' is imprecise; D is correct only because the actual primary function is absent from the choices.",
    "The GO annotation for metal ion binding carries evidence code IEA:UniProtKB-KW (inferred from keyword), not experimental evidence. The metal-dependence of PA endonuclease is well-established structurally and biochemically, but the specific GO annotation is computationally derived.",
    "The sequence is from the 2009 pandemic H1N1 strain (A/California/04/2009). PA function is conserved across influenza A strains, so this does not affect the answer.",
    "Option B (GO:0000014, single-stranded DNA endodeoxyribonuclease activity) is a deliberate near-miss: it captures 'endonuclease' but specifies DNA rather than RNA substrate. This tests substrate-specificity knowledge.",
    "The identity of the protein as Influenza A PA requires either sequence recognition or database lookup; however, the reasoning path from 'viral polymerase subunit' to 'metal-dependent endonuclease' is general virology knowledge."
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

**Accession:** `C3W5S0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 105. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C3W5S0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.548827+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_04063","source":"HAMAP-Rule"}],"value":"Plays an essential role in viral RNA transcription and replication by forming the heterotrimeric polymerase complex together with PB1 and PB2 subunits. The complex transcribes viral mRNAs by using a unique mechanism called cap-snatching. It consists in the hijacking and cleavage of host capped pre-mRNAs. These short capped RNAs are then used as primers for viral mRNAs. The PB2 subunit is responsible for the binding of the 5' cap of cellular pre-mRNAs which are subsequently cleaved after 10-13 nucleotides by the PA subunit that carries the endonuclease activity"}]}
```

Source SHA-256: `41de97cb89c07354676a2d9a707a158e2cc4d809c3ea945287a37298998ef378`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C3W5S0.json)  
**Locator:** `/uniProtKBCrossReferences/215`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.548827+00:00.  

```json
{"database":"GO","id":"GO:0046872","properties":[{"key":"GoTerm","value":"F:metal ion binding"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-KW"}]}
```

Source SHA-256: `41de97cb89c07354676a2d9a707a158e2cc4d809c3ea945287a37298998ef378`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C3W5S0?format=txt&versions=105)  
**Locator:** `lines 151-159`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:27:30.499324+00:00.  

```text
CC   -!- FUNCTION: Plays an essential role in viral RNA transcription and
CC       replication by forming the heterotrimeric polymerase complex together
CC       with PB1 and PB2 subunits. The complex transcribes viral mRNAs by using
CC       a unique mechanism called cap-snatching. It consists in the hijacking
CC       and cleavage of host capped pre-mRNAs. These short capped RNAs are then
CC       used as primers for viral mRNAs. The PB2 subunit is responsible for the
CC       binding of the 5' cap of cellular pre-mRNAs which are subsequently
CC       cleaved after 10-13 nucleotides by the PA subunit that carries the
CC       endonuclease activity. {ECO:0000255|HAMAP-Rule:MF_04063}.
```

Source SHA-256: `dd6527288091b8021cdd92a9500cb06cf91332794d3ed14c1592693b57498db5`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C3W5S0?format=txt&versions=105)  
**Locator:** `lines 404-404`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:27:30.499324+00:00.  

```text
DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.
```

Source SHA-256: `dd6527288091b8021cdd92a9500cb06cf91332794d3ed14c1592693b57498db5`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 159-169`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000014
name: single-stranded DNA endonuclease activity
namespace: molecular_function
def: "Catalysis of the hydrolysis of ester linkages within a single-stranded deoxyribonucleic acid molecule by creating internal breaks." [GOC:mah]
synonym: "single-stranded DNA endodeoxyribonuclease activity" EXACT []
synonym: "single-stranded DNA specific endodeoxyribonuclease activity" RELATED []
synonym: "ssDNA-specific endodeoxyribonuclease activity" RELATED [GOC:mah]
is_a: GO:0004520 ! DNA endonuclease activity
is_a: GO:0016788 ! hydrolase activity, acting on ester bonds

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 122608-122615`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016018
name: cyclosporin A binding
namespace: molecular_function
def: "Binding to cyclosporin A, a cyclic undecapeptide that contains several N-methylated and unusual amino acids." [GOC:mb]
synonym: "cyclophilin" RELATED []
is_a: GO:0005488 ! binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

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

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 442568-442576`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0140693
name: molecular condensate scaffold activity
namespace: molecular_function
def: "Binding and bringing together two or more macromolecules in contact, permitting those molecules to organize as a molecular condensate." [PMID:28225081]
synonym: "phase separation nucleation activity" EXACT []
synonym: "phase separation nucleator activity" EXACT []
is_a: GO:0030674 ! protein-macromolecule adaptor activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 139. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
