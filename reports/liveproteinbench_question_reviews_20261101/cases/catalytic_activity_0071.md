# catalytic_activity_0071

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — N(6)-acetyl-L-lysyl-&#91;protein&#93; + H2O = L-lysyl-&#91;protein&#93; + acetate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSTGQDSSTRQRKSRHNPQSPLQDSSATLKRGGKKGAVPHSSPNLAEVKKKGKMKKLSQPAEEDLIVGLQGLDLNSETRVPVGTGLVFDEQLNDFHCLWDDSFPENPERLHAIKEQLILEGLLGRCVSFQARFAEKEELMLVHSLEYIDLMETTQYMNEGELRVLAGTYDSVYLHPNSYSCACLATGSVLRLVDAVMGAEIRNGMAVIRPPGHHAQRSLMDGYCMFNHLAVAARYAQKKHRIQRILIVDWDVHHGQGTQFIFDQDPSVLYFSIHRYEHGRFWPHLKASNWSTTGFGQGQGYTINVPWNQVSFCSHKLSLACFPRGSREMTDYYIAFLCLQVGMRDADYIAAFLHILLPVAFEFQPQLVLVAAGFDALHGDPKGEMSATPAGFAHLTHFLMGLAGGKLILSLEGGYNLHALAKGVSGSLHTLLGDPCPMLESPVAPCASAQTSISCTLEALEPFWEVLERSVEPQDEDEVEGDMLEDEEEEGHWEATALPMDTWPLLQNRTGLVYDERMMSHCNLWDNHHPETPQRILRIMCHLEEVGLAARCLILPARPALDSELLTCHSAEYVERLRATEKMKTRDLHREGANFESIYICPSTFACAQLATGAACRLVEAVLSGEVLNGIAIVRPPGHHAEPDAACGFCFFNSVAVAARHAQVIAGRALRILIVDWDVHHGNGTQHIFEEDPSVLYVSLHRYDRGTFFPMGDEGASSQVGRAAGTGFTVNVPWNGPRMGDADYLATWHRLVLPIAYEFNPELVLISAGFDAAQGDPLGGCQVTPEGYAHLTHLLMGLAGGRIILILEGGYNLTSISESMAACTHSLLGDPPPQLTSLRPPQSGALASISEVIQVHRKYWRSLRLMKMEDKEERSSSRLVIKKLPQSASPVSAKGMTTPKGKVLEAGMRKPTAALPTKESTLGQAKAKTAKALLAQGQSSEQAAKGTTLDLATSKDTVGGATTDQCASVAATENSANQTTSGEEASGETESFGTSPSSNASKQTTGASPLHGAAAQQSPELGLSSTLELSSEAQEVQESEEGLLGEAAGGQDMNSLMLTQGFGDFNTQDVFYAVTPLSWCPHLMAVCPIPAAGLDVSQPCKTCGSVQENWVCLTCYQVYCSRYVNAHMVCHHEASEHPLVLSCVDLSTWCYLCQAYVHHEDLQDVKNAAHQNKFGEGMPHLQ

[Multiple Choices]
A. N(6)-acetyl-L-lysyl-[protein] + H2O = L-lysyl-[protein] + acetate
B. N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
C. nicotinate beta-D-ribonucleotide + ATP + H(+) = deamido-NAD(+) + diphosphate
D. D-mannitol + NADP(+) = D-fructose + NADPH + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence matches the rat HDAC6 entry, whose annotation gives the N(6)-acetyl-lysyl protein hydrolysis reaction as choice A. The annotation is transferred by similarity from UniProtKB:Q9UBN7, so it supports the key but is not direct experimental evidence for this rat sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two homologous catalytic domains characteristic of histone deacetylase-family enzymes. That provides a defensible basis for identifying protein lysine deacetylation, which distinguishes A from the amine methylation, NAD biosynthesis, and mannitol oxidation reactions.


**Missing item-specific fact**

> The precise HDAC6 annotation and any direct experimental confirmation for this particular rat protein are not supplied, but the broad deacetylase-family function meaningfully distinguishes the listed choices.


**Reason**

> The sequence-family signal supports the reaction class needed to select A among these options; selection need not depend solely on recalling the exact database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice A describes protein lysine deacetylation; the other choices are chemically and enzymatically distinct.


### Important caveats

- Reviewer-only database evidence was not available to the evaluated model.
- The cited UniProt reaction annotation is similarity-transferred, and the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two homologous catalytic domains characteristic of histone deacetylase-family enzymes. That provides a defensible basis for identifying protein lysine deacetylation, which distinguishes A from the amine methylation, NAD biosynthesis, and mannitol oxidation reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise HDAC6 annotation and any direct experimental confirmation for this particular rat protein are not supplied, but the broad deacetylase-family function meaningfully distinguishes the listed choices.",
    "reason": "The sequence-family signal supports the reaction class needed to select A among these options; selection need not depend solely on recalling the exact database entry."
  },
  "case_id": "catalytic_activity_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the rat HDAC6 entry, whose annotation gives the N(6)-acetyl-lysyl protein hydrolysis reaction as choice A. The annotation is transferred by similarity from UniProtKB:Q9UBN7, so it supports the key but is not direct experimental evidence for this rat sequence."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The cited UniProt reaction annotation is similarity-transferred, and the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice A describes protein lysine deacetylation; the other choices are chemically and enzymatically distinct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the rat HDAC6 entry, whose annotation gives the N(6)-acetyl-lysyl protein hydrolysis reaction as choice A. The annotation is transferred by similarity from UniProtKB:Q9UBN7, so it supports the key but is not direct experimental evidence for this rat sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two homologous catalytic domains characteristic of histone deacetylase-family enzymes. That provides a defensible basis for identifying protein lysine deacetylation, which distinguishes A from the amine methylation, NAD biosynthesis, and mannitol oxidation reactions.",
    "missing_item_specific_fact": "The precise HDAC6 annotation and any direct experimental confirmation for this particular rat protein are not supplied, but the broad deacetylase-family function meaningfully distinguishes the listed choices.",
    "reason": "The sequence-family signal supports the reaction class needed to select A among these options; selection need not depend solely on recalling the exact database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice A describes protein lysine deacetylation; the other choices are chemically and enzymatically distinct."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The cited UniProt reaction annotation is similarity-transferred, and the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A8I6GM68 (HDAC6_RAT, 1183 AA, SHA256 confirmed). The UniProt annotation lists the catalytic reaction 'N(6)-acetyl-L-lysyl-&#91;protein&#93; + H2O = L-lysyl-&#91;protein&#93; + acetate' (RHEA:58108) as the recommended-name reaction, exactly matching Choice A. The evidence code is ECO:0000250 (inferred by similarity from human HDAC6, Q9UBN7), so this is a transferred/computational annotation rather than direct experimental evidence, but it is the accepted database annotation for this entry.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two copies of the class I/II histone deacetylase catalytic domain signature, including the conserved 'VDW' motif (RILIVDWDVHHGQGTQ and RILIVDWDVHHGNGTQH), the 'HHA' motif (HHAQRSLMDGYCMFNHLAVAARY and HHAEPDAACGFCFFNSVAVAARH), and the zinc-binding His/Asp/His triad. These are well-established hallmarks of zinc-dependent protein lysine deacetylases. The four distractors represent entirely different enzyme classes: B is an O-methyltransferase (would require a SAM-binding Rossmann fold), C is an NAD synthetase (would require a synthetase/ligase fold), and D is a mannitol dehydrogenase (would require a short-chain dehydrogenase/reductase fold). Recognizing the HDAC catalytic domain motifs is sufficient to select the deacetylase reaction (A) over the other three mechanistically unrelated reactions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HDAC catalytic domain has well-characterized sequence signatures (VDW, HHA, zinc-binding triad) that are part of standard biochemistry knowledge. These motifs are visibly present in the supplied sequence and are diagnostic of a deacetylase, cleanly distinguishing Choice A from the methyltransferase, synthetase, and dehydrogenase distractors. No protein-specific experimental measurement or obscure annotation is required to make this class-level distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice A is the only deacetylase reaction among the four options. The UniProt entry also lists a tubulin-specific variant (N(6)-acetyl-L-lysyl-&#91;alpha-tubulin&#93;), but Choice A uses the general '&#91;protein&#93;' form, which is the recommended-name reaction and is not contradicted by the tubulin-specific annotation. The other three choices belong to unrelated enzyme classes with no plausible overlap.


### Important caveats

- The catalytic activity annotation carries evidence code ECO:0000250 (inferred by similarity from human HDAC6, Q9UBN7), meaning it is a transferred annotation, not direct experimental evidence for the rat protein specifically.
- The UniProt entry was first publicly released 2025-04-09; the historical snapshot used (entry version 19, 2026-01-28) is the earliest reviewed version. The author's exact source snapshot is unknown.
- The identity of this sequence as HDAC6 was inferred by the reviewer from dataset metadata (accession A0A8I6GM68); this accession was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two copies of the class I/II histone deacetylase catalytic domain signature, including the conserved 'VDW' motif (RILIVDWDVHHGQGTQ and RILIVDWDVHHGNGTQH), the 'HHA' motif (HHAQRSLMDGYCMFNHLAVAARY and HHAEPDAACGFCFFNSVAVAARH), and the zinc-binding His/Asp/His triad. These are well-established hallmarks of zinc-dependent protein lysine deacetylases. The four distractors represent entirely different enzyme classes: B is an O-methyltransferase (would require a SAM-binding Rossmann fold), C is an NAD synthetase (would require a synthetase/ligase fold), and D is a mannitol dehydrogenase (would require a short-chain dehydrogenase/reductase fold). Recognizing the HDAC catalytic domain motifs is sufficient to select the deacetylase reaction (A) over the other three mechanistically unrelated reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HDAC catalytic domain has well-characterized sequence signatures (VDW, HHA, zinc-binding triad) that are part of standard biochemistry knowledge. These motifs are visibly present in the supplied sequence and are diagnostic of a deacetylase, cleanly distinguishing Choice A from the methyltransferase, synthetase, and dehydrogenase distractors. No protein-specific experimental measurement or obscure annotation is required to make this class-level distinction."
  },
  "case_id": "catalytic_activity_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A8I6GM68 (HDAC6_RAT, 1183 AA, SHA256 confirmed). The UniProt annotation lists the catalytic reaction 'N(6)-acetyl-L-lysyl-[protein] + H2O = L-lysyl-[protein] + acetate' (RHEA:58108) as the recommended-name reaction, exactly matching Choice A. The evidence code is ECO:0000250 (inferred by similarity from human HDAC6, Q9UBN7), so this is a transferred/computational annotation rather than direct experimental evidence, but it is the accepted database annotation for this entry."
  },
  "important_caveats": [
    "The catalytic activity annotation carries evidence code ECO:0000250 (inferred by similarity from human HDAC6, Q9UBN7), meaning it is a transferred annotation, not direct experimental evidence for the rat protein specifically.",
    "The UniProt entry was first publicly released 2025-04-09; the historical snapshot used (entry version 19, 2026-01-28) is the earliest reviewed version. The author's exact source snapshot is unknown.",
    "The identity of this sequence as HDAC6 was inferred by the reviewer from dataset metadata (accession A0A8I6GM68); this accession was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is the only deacetylase reaction among the four options. The UniProt entry also lists a tubulin-specific variant (N(6)-acetyl-L-lysyl-[alpha-tubulin]), but Choice A uses the general '[protein]' form, which is the recommended-name reaction and is not contradicted by the tubulin-specific annotation. The other three choices belong to unrelated enzyme classes with no plausible overlap."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A8I6GM68 (HDAC6_RAT, 1183 AA, SHA256 confirmed). The UniProt annotation lists the catalytic reaction 'N(6)-acetyl-L-lysyl-[protein] + H2O = L-lysyl-[protein] + acetate' (RHEA:58108) as the recommended-name reaction, exactly matching Choice A. The evidence code is ECO:0000250 (inferred by similarity from human HDAC6, Q9UBN7), so this is a transferred/computational annotation rather than direct experimental evidence, but it is the accepted database annotation for this entry.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two copies of the class I/II histone deacetylase catalytic domain signature, including the conserved 'VDW' motif (RILIVDWDVHHGQGTQ and RILIVDWDVHHGNGTQH), the 'HHA' motif (HHAQRSLMDGYCMFNHLAVAARY and HHAEPDAACGFCFFNSVAVAARH), and the zinc-binding His/Asp/His triad. These are well-established hallmarks of zinc-dependent protein lysine deacetylases. The four distractors represent entirely different enzyme classes: B is an O-methyltransferase (would require a SAM-binding Rossmann fold), C is an NAD synthetase (would require a synthetase/ligase fold), and D is a mannitol dehydrogenase (would require a short-chain dehydrogenase/reductase fold). Recognizing the HDAC catalytic domain motifs is sufficient to select the deacetylase reaction (A) over the other three mechanistically unrelated reactions.",
    "missing_item_specific_fact": "",
    "reason": "The HDAC catalytic domain has well-characterized sequence signatures (VDW, HHA, zinc-binding triad) that are part of standard biochemistry knowledge. These motifs are visibly present in the supplied sequence and are diagnostic of a deacetylase, cleanly distinguishing Choice A from the methyltransferase, synthetase, and dehydrogenase distractors. No protein-specific experimental measurement or obscure annotation is required to make this class-level distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is the only deacetylase reaction among the four options. The UniProt entry also lists a tubulin-specific variant (N(6)-acetyl-L-lysyl-[alpha-tubulin]), but Choice A uses the general '[protein]' form, which is the recommended-name reaction and is not contradicted by the tubulin-specific annotation. The other three choices belong to unrelated enzyme classes with no plausible overlap."
  },
  "important_caveats": [
    "The catalytic activity annotation carries evidence code ECO:0000250 (inferred by similarity from human HDAC6, Q9UBN7), meaning it is a transferred annotation, not direct experimental evidence for the rat protein specifically.",
    "The UniProt entry was first publicly released 2025-04-09; the historical snapshot used (entry version 19, 2026-01-28) is the earliest reviewed version. The author's exact source snapshot is unknown.",
    "The identity of this sequence as HDAC6 was inferred by the reviewer from dataset metadata (accession A0A8I6GM68); this accession was not provided to the evaluated model."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:02.236008+00:00.  

```json
"A0A8I6GM68"
```

Source SHA-256: `9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1`.

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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:02.236008+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UBN7","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:58109"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UBN7","source":"UniProtKB"}],"name":"N(6)-acetyl-L-lysyl-[protein] + H2O = L-lysyl-[protein] + acetate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58108"},{"database":"Rhea","id":"RHEA-COMP:9752"},{"database":"Rhea","id":"RHEA-COMP:10731"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29969"},{"database":"ChEBI","id":"CHEBI:30089"},{"database":"ChEBI","id":"CHEBI:61930"}]}}
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
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:04.375301+00:00.  

```text
DE   RecName: Full=Protein deacetylase HDAC6 {ECO:0000305};
DE            EC=3.5.1.- {ECO:0000250|UniProtKB:Q9UBN7};
DE   AltName: Full=E3 ubiquitin-protein ligase HDAC6 {ECO:0000305};
DE            EC=2.3.2.- {ECO:0000250|UniProtKB:Q9UBN7};
DE   AltName: Full=Tubulin-lysine deacetylase HDAC6 {ECO:0000305};
DE            EC=3.5.1.- {ECO:0000250|UniProtKB:Q9UBN7};
```

Source SHA-256: `58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)  
**Locator:** `lines 112-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:04.375301+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(6)-acetyl-L-lysyl-[protein] + H2O = L-lysyl-[protein] +
CC         acetate; Xref=Rhea:RHEA:58108, Rhea:RHEA-COMP:9752, Rhea:RHEA-
CC         COMP:10731, ChEBI:CHEBI:15377, ChEBI:CHEBI:29969, ChEBI:CHEBI:30089,
CC         ChEBI:CHEBI:61930; Evidence={ECO:0000250|UniProtKB:Q9UBN7};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:58109;
CC         Evidence={ECO:0000250|UniProtKB:Q9UBN7};
```

Source SHA-256: `58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 71. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
