# pathway_0006

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Protein modification

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSTGQDSSTRQRKSRHNPQSPLQDSSATLKRGGKKGAVPHSSPNLAEVKKKGKMKKLSQPAEEDLIVGLQGLDLNSETRVPVGTGLVFDEQLNDFHCLWDDSFPENPERLHAIKEQLILEGLLGRCVSFQARFAEKEELMLVHSLEYIDLMETTQYMNEGELRVLAGTYDSVYLHPNSYSCACLATGSVLRLVDAVMGAEIRNGMAVIRPPGHHAQRSLMDGYCMFNHLAVAARYAQKKHRIQRILIVDWDVHHGQGTQFIFDQDPSVLYFSIHRYEHGRFWPHLKASNWSTTGFGQGQGYTINVPWNQVSFCSHKLSLACFPRGSREMTDYYIAFLCLQVGMRDADYIAAFLHILLPVAFEFQPQLVLVAAGFDALHGDPKGEMSATPAGFAHLTHFLMGLAGGKLILSLEGGYNLHALAKGVSGSLHTLLGDPCPMLESPVAPCASAQTSISCTLEALEPFWEVLERSVEPQDEDEVEGDMLEDEEEEGHWEATALPMDTWPLLQNRTGLVYDERMMSHCNLWDNHHPETPQRILRIMCHLEEVGLAARCLILPARPALDSELLTCHSAEYVERLRATEKMKTRDLHREGANFESIYICPSTFACAQLATGAACRLVEAVLSGEVLNGIAIVRPPGHHAEPDAACGFCFFNSVAVAARHAQVIAGRALRILIVDWDVHHGNGTQHIFEEDPSVLYVSLHRYDRGTFFPMGDEGASSQVGRAAGTGFTVNVPWNGPRMGDADYLATWHRLVLPIAYEFNPELVLISAGFDAAQGDPLGGCQVTPEGYAHLTHLLMGLAGGRIILILEGGYNLTSISESMAACTHSLLGDPPPQLTSLRPPQSGALASISEVIQVHRKYWRSLRLMKMEDKEERSSSRLVIKKLPQSASPVSAKGMTTPKGKVLEAGMRKPTAALPTKESTLGQAKAKTAKALLAQGQSSEQAAKGTTLDLATSKDTVGGATTDQCASVAATENSANQTTSGEEASGETESFGTSPSSNASKQTTGASPLHGAAAQQSPELGLSSTLELSSEAQEVQESEEGLLGEAAGGQDMNSLMLTQGFGDFNTQDVFYAVTPLSWCPHLMAVCPIPAAGLDVSQPCKTCGSVQENWVCLTCYQVYCSRYVNAHMVCHHEASEHPLVLSCVDLSTWCYLCQAYVHHEDLQDVKNAAHQNKFGEGMPHLQ

[Multiple Choices]
A. iron-sulfur cluster biosynthesis. .
B. protein ubiquitination. .
C. Protein modification
D. coenzyme A biosynthesis
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

> The matched UniProt record annotates the pathway as “Protein modification; protein ubiquitination,” supporting the keyed Protein modification option. The annotation is transferred by similarity rather than direct experimental evidence for this rat sequence.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two repeated histone-deacetylase-like catalytic domains, supporting a protein deacetylation function; deacetylation is a form of protein modification and makes C a biologically grounded choice over the unrelated iron-sulfur and coenzyme A pathways.


**Missing item-specific fact**

> Establishing that protein modification is the primary pathway rather than the also-annotated protein ubiquitination pathway requires protein-specific functional or pathway annotation.


**Reason**

> Sequence/domain reasoning meaningfully favors protein modification, but does not establish a unique primary pathway because the protein is also associated with ubiquitination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The matched UniProt pathway annotation lists both protein modification and protein ubiquitination, while the question gives no criterion for choosing a primary pathway; ubiquitination is also a type of protein modification.


### Important caveats

- The reviewer-only sequence match identifies the record as rat HDAC6; that identity and its database annotations were not provided to the evaluated model.
- The pathway annotation is supported by evidence transferred from human UniProt entry Q9UBN7, not by direct experimental evidence established here for the rat protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two repeated histone-deacetylase-like catalytic domains, supporting a protein deacetylation function; deacetylation is a form of protein modification and makes C a biologically grounded choice over the unrelated iron-sulfur and coenzyme A pathways.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Establishing that protein modification is the primary pathway rather than the also-annotated protein ubiquitination pathway requires protein-specific functional or pathway annotation.",
    "reason": "Sequence/domain reasoning meaningfully favors protein modification, but does not establish a unique primary pathway because the protein is also associated with ubiquitination."
  },
  "case_id": "pathway_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt record annotates the pathway as “Protein modification; protein ubiquitination,” supporting the keyed Protein modification option. The annotation is transferred by similarity rather than direct experimental evidence for this rat sequence."
  },
  "important_caveats": [
    "The reviewer-only sequence match identifies the record as rat HDAC6; that identity and its database annotations were not provided to the evaluated model.",
    "The pathway annotation is supported by evidence transferred from human UniProt entry Q9UBN7, not by direct experimental evidence established here for the rat protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The matched UniProt pathway annotation lists both protein modification and protein ubiquitination, while the question gives no criterion for choosing a primary pathway; ubiquitination is also a type of protein modification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record annotates the pathway as “Protein modification; protein ubiquitination,” supporting the keyed Protein modification option. The annotation is transferred by similarity rather than direct experimental evidence for this rat sequence.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two repeated histone-deacetylase-like catalytic domains, supporting a protein deacetylation function; deacetylation is a form of protein modification and makes C a biologically grounded choice over the unrelated iron-sulfur and coenzyme A pathways.",
    "missing_item_specific_fact": "Establishing that protein modification is the primary pathway rather than the also-annotated protein ubiquitination pathway requires protein-specific functional or pathway annotation.",
    "reason": "Sequence/domain reasoning meaningfully favors protein modification, but does not establish a unique primary pathway because the protein is also associated with ubiquitination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The matched UniProt pathway annotation lists both protein modification and protein ubiquitination, while the question gives no criterion for choosing a primary pathway; ubiquitination is also a type of protein modification."
  },
  "important_caveats": [
    "The reviewer-only sequence match identifies the record as rat HDAC6; that identity and its database annotations were not provided to the evaluated model.",
    "The pathway annotation is supported by evidence transferred from human UniProt entry Q9UBN7, not by direct experimental evidence established here for the rat protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt pathway annotation for HDAC6_RAT (A0A8I6GM68) reads 'Protein modification; protein ubiquitination' (C5, H2). Option C ('Protein modification') matches the parent category in this hierarchical annotation. Additionally, HDAC6's recommended name is 'Protein deacetylase HDAC6' (C4, H1), and deacetylation is a form of protein modification. However, option B ('protein ubiquitination') is the more specific sub-pathway in the same annotation, making it equally or more directly supported. The expected answer C is valid but not uniquely determined over B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains two DWD-motif catalytic domains characteristic of histone deacetylases, which could support reasoning toward 'protein modification' (deacetylation is a PTM). However, distinguishing option C ('Protein modification') from option B ('protein ubiquitination') requires knowing that UniProt's pathway annotation hierarchy places 'protein ubiquitination' as the specific pathway under the 'Protein modification' umbrella, or knowing that HDAC6's primary annotation emphasizes ubiquitination as its specific pathway while deacetylation is its primary enzymatic activity. This is an annotation-hierarchy fact, not derivable from sequence features alone.


**Missing item-specific fact**

> The UniProt pathway annotation hierarchy ('Protein modification; protein ubiquitination') and the decision to report the parent category rather than the specific sub-pathway as the 'primary pathway' answer. Also, HDAC6's dual identity as both a deacetylase and an E3 ubiquitin ligase is a protein-specific fact needed to weigh B vs. C.


**Reason**

> While the HDAC domains are recognizable from the sequence and could lead a model to 'protein modification,' the specific choice between B (protein ubiquitination, the sub-pathway) and C (Protein modification, the parent category) depends on the UniProt annotation structure and the benchmark's convention of selecting the broader category. This is an item-specific annotation fact rather than a general biological inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The UniProt pathway annotation 'Protein modification; protein ubiquitination' contains both option C (parent category) and option B (specific sub-pathway). Both are directly present in the annotation. HDAC6's primary enzymatic activity is deacetylation (a protein modification, supporting C), while its annotated specific pathway is protein ubiquitination (supporting B). The question asks for 'the primary pathway' but the annotation provides a hierarchical pair, making both B and C defensible depending on whether one reads 'primary' as the broad category or the specific sub-pathway.


### Important caveats

- The UniProt pathway annotation uses evidence code ECO:0000250 (similarity to Q9UBN7, the human HDAC6), meaning it is transferred by similarity rather than experimentally determined for the rat ortholog.
- HDAC6's recommended name is 'Protein deacetylase HDAC6' (EC 3.5.1.-), with E3 ubiquitin ligase activity (EC 2.3.2.-) listed as an alternative name. The pathway annotation emphasizing ubiquitination may not reflect the protein's dominant biological role.
- Option C uses a capital 'P' in 'Protein modification' matching UniProt's formatting, while option B uses lowercase 'protein ubiquitination', suggesting both were copied from the same annotation string.
- The question stem asks for 'the primary metabolic or signaling pathway,' but the UniProt annotation gives a single hierarchical pathway entry rather than distinguishing a 'primary' from a 'secondary' pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two DWD-motif catalytic domains characteristic of histone deacetylases, which could support reasoning toward 'protein modification' (deacetylation is a PTM). However, distinguishing option C ('Protein modification') from option B ('protein ubiquitination') requires knowing that UniProt's pathway annotation hierarchy places 'protein ubiquitination' as the specific pathway under the 'Protein modification' umbrella, or knowing that HDAC6's primary annotation emphasizes ubiquitination as its specific pathway while deacetylation is its primary enzymatic activity. This is an annotation-hierarchy fact, not derivable from sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The UniProt pathway annotation hierarchy ('Protein modification; protein ubiquitination') and the decision to report the parent category rather than the specific sub-pathway as the 'primary pathway' answer. Also, HDAC6's dual identity as both a deacetylase and an E3 ubiquitin ligase is a protein-specific fact needed to weigh B vs. C.",
    "reason": "While the HDAC domains are recognizable from the sequence and could lead a model to 'protein modification,' the specific choice between B (protein ubiquitination, the sub-pathway) and C (Protein modification, the parent category) depends on the UniProt annotation structure and the benchmark's convention of selecting the broader category. This is an item-specific annotation fact rather than a general biological inference."
  },
  "case_id": "pathway_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for HDAC6_RAT (A0A8I6GM68) reads 'Protein modification; protein ubiquitination' (C5, H2). Option C ('Protein modification') matches the parent category in this hierarchical annotation. Additionally, HDAC6's recommended name is 'Protein deacetylase HDAC6' (C4, H1), and deacetylation is a form of protein modification. However, option B ('protein ubiquitination') is the more specific sub-pathway in the same annotation, making it equally or more directly supported. The expected answer C is valid but not uniquely determined over B."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses evidence code ECO:0000250 (similarity to Q9UBN7, the human HDAC6), meaning it is transferred by similarity rather than experimentally determined for the rat ortholog.",
    "HDAC6's recommended name is 'Protein deacetylase HDAC6' (EC 3.5.1.-), with E3 ubiquitin ligase activity (EC 2.3.2.-) listed as an alternative name. The pathway annotation emphasizing ubiquitination may not reflect the protein's dominant biological role.",
    "Option C uses a capital 'P' in 'Protein modification' matching UniProt's formatting, while option B uses lowercase 'protein ubiquitination', suggesting both were copied from the same annotation string.",
    "The question stem asks for 'the primary metabolic or signaling pathway,' but the UniProt annotation gives a single hierarchical pathway entry rather than distinguishing a 'primary' from a 'secondary' pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The UniProt pathway annotation 'Protein modification; protein ubiquitination' contains both option C (parent category) and option B (specific sub-pathway). Both are directly present in the annotation. HDAC6's primary enzymatic activity is deacetylation (a protein modification, supporting C), while its annotated specific pathway is protein ubiquitination (supporting B). The question asks for 'the primary pathway' but the annotation provides a hierarchical pair, making both B and C defensible depending on whether one reads 'primary' as the broad category or the specific sub-pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for HDAC6_RAT (A0A8I6GM68) reads 'Protein modification; protein ubiquitination' (C5, H2). Option C ('Protein modification') matches the parent category in this hierarchical annotation. Additionally, HDAC6's recommended name is 'Protein deacetylase HDAC6' (C4, H1), and deacetylation is a form of protein modification. However, option B ('protein ubiquitination') is the more specific sub-pathway in the same annotation, making it equally or more directly supported. The expected answer C is valid but not uniquely determined over B.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains two DWD-motif catalytic domains characteristic of histone deacetylases, which could support reasoning toward 'protein modification' (deacetylation is a PTM). However, distinguishing option C ('Protein modification') from option B ('protein ubiquitination') requires knowing that UniProt's pathway annotation hierarchy places 'protein ubiquitination' as the specific pathway under the 'Protein modification' umbrella, or knowing that HDAC6's primary annotation emphasizes ubiquitination as its specific pathway while deacetylation is its primary enzymatic activity. This is an annotation-hierarchy fact, not derivable from sequence features alone.",
    "missing_item_specific_fact": "The UniProt pathway annotation hierarchy ('Protein modification; protein ubiquitination') and the decision to report the parent category rather than the specific sub-pathway as the 'primary pathway' answer. Also, HDAC6's dual identity as both a deacetylase and an E3 ubiquitin ligase is a protein-specific fact needed to weigh B vs. C.",
    "reason": "While the HDAC domains are recognizable from the sequence and could lead a model to 'protein modification,' the specific choice between B (protein ubiquitination, the sub-pathway) and C (Protein modification, the parent category) depends on the UniProt annotation structure and the benchmark's convention of selecting the broader category. This is an item-specific annotation fact rather than a general biological inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The UniProt pathway annotation 'Protein modification; protein ubiquitination' contains both option C (parent category) and option B (specific sub-pathway). Both are directly present in the annotation. HDAC6's primary enzymatic activity is deacetylation (a protein modification, supporting C), while its annotated specific pathway is protein ubiquitination (supporting B). The question asks for 'the primary pathway' but the annotation provides a hierarchical pair, making both B and C defensible depending on whether one reads 'primary' as the broad category or the specific sub-pathway."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses evidence code ECO:0000250 (similarity to Q9UBN7, the human HDAC6), meaning it is transferred by similarity rather than experimentally determined for the rat ortholog.",
    "HDAC6's recommended name is 'Protein deacetylase HDAC6' (EC 3.5.1.-), with E3 ubiquitin ligase activity (EC 2.3.2.-) listed as an alternative name. The pathway annotation emphasizing ubiquitination may not reflect the protein's dominant biological role.",
    "Option C uses a capital 'P' in 'Protein modification' matching UniProt's formatting, while option B uses lowercase 'protein ubiquitination', suggesting both were copied from the same annotation string.",
    "The question stem asks for 'the primary metabolic or signaling pathway,' but the UniProt annotation gives a single hierarchical pathway entry rather than distinguishing a 'primary' from a 'secondary' pathway."
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

**Accession:** `A0A8I6GM68` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:02.236008+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UBN7","source":"UniProtKB"}],"value":"2.3.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"E3 ubiquitin-protein ligase HDAC6"}},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UBN7","source":"UniProtKB"}],"value":"3.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Tubulin-lysine deacetylase HDAC6"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UBN7","source":"UniProtKB"}],"value":"3.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Protein deacetylase HDAC6"}}}
```

Source SHA-256: `9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:02.236008+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UBN7","source":"UniProtKB"}],"value":"Protein modification; protein ubiquitination"}]}
```

Source SHA-256: `9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:04.375301+00:00.  

```text
ID   HDAC6_RAT               Reviewed;        1183 AA.
AC   A0A8I6GM68;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   25-MAY-2022, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=Protein deacetylase HDAC6 {ECO:0000305};
DE            EC=3.5.1.- {ECO:0000250|UniProtKB:Q9UBN7};
DE   AltName: Full=E3 ubiquitin-protein ligase HDAC6 {ECO:0000305};
DE            EC=2.3.2.- {ECO:0000250|UniProtKB:Q9UBN7};
DE   AltName: Full=Tubulin-lysine deacetylase HDAC6 {ECO:0000305};
DE            EC=3.5.1.- {ECO:0000250|UniProtKB:Q9UBN7};
GN   Name=Hdac6 {ECO:0000312|RGD:619981};
OS   Rattus norvegicus (Rat).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Rattus.
OX   NCBI_TaxID=10116 {ECO:0000312|Proteomes:UP000002494};
```

Source SHA-256: `58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)  
**Locator:** `lines 131-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:04.375301+00:00.  

```text
CC   -!- PATHWAY: Protein modification; protein ubiquitination.
CC       {ECO:0000250|UniProtKB:Q9UBN7}.
```

Source SHA-256: `58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 6. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
