# active_site_0038: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0038.txt)

**Task:** `active_site`  
**Author key, unchanged:** **D** — Position 215 (1)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MTSTGQDSSTRQRKSRHNPQSPLQDSSATLKRGGKKGAVPHSSPNLAEVKKKGKMKKLSQPAEEDLIVGLQGLDLNSETRVPVGTGLVFDEQLNDFHCLWDDSFPENPERLHAIKEQLILEGLLGRCVSFQARFAEKEELMLVHSLEYIDLMETTQYMNEGELRVLAGTYDSVYLHPNSYSCACLATGSVLRLVDAVMGAEIRNGMAVIRPPGHHAQRSLMDGYCMFNHLAVAARYAQKKHRIQRILIVDWDVHHGQGTQFIFDQDPSVLYFSIHRYEHGRFWPHLKASNWSTTGFGQGQGYTINVPWNQVSFCSHKLSLACFPRGSREMTDYYIAFLCLQVGMRDADYIAAFLHILLPVAFEFQPQLVLVAAGFDALHGDPKGEMSATPAGFAHLTHFLMGLAGGKLILSLEGGYNLHALAKGVSGSLHTLLGDPCPMLESPVAPCASAQTSISCTLEALEPFWEVLERSVEPQDEDEVEGDMLEDEEEEGHWEATALPMDTWPLLQNRTGLVYDERMMSHCNLWDNHHPETPQRILRIMCHLEEVGLAARCLILPARPALDSELLTCHSAEYVERLRATEKMKTRDLHREGANFESIYICPSTFACAQLATGAACRLVEAVLSGEVLNGIAIVRPPGHHAEPDAACGFCFFNSVAVAARHAQVIAGRALRILIVDWDVHHGNGTQHIFEEDPSVLYVSLHRYDRGTFFPMGDEGASSQVGRAAGTGFTVNVPWNGPRMGDADYLATWHRLVLPIAYEFNPELVLISAGFDAAQGDPLGGCQVTPEGYAHLTHLLMGLAGGRIILILEGGYNLTSISESMAACTHSLLGDPPPQLTSLRPPQSGALASISEVIQVHRKYWRSLRLMKMEDKEERSSSRLVIKKLPQSASPVSAKGMTTPKGKVLEAGMRKPTAALPTKESTLGQAKAKTAKALLAQGQSSEQAAKGTTLDLATSKDTVGGATTDQCASVAATENSANQTTSGEEASGETESFGTSPSSNASKQTTGASPLHGAAAQQSPELGLSSTLELSSEAQEVQESEEGLLGEAAGGQDMNSLMLTQGFGDFNTQDVFYAVTPLSWCPHLMAVCPIPAAGLDVSQPCKTCGSVQENWVCLTCYQVYCSRYVNAHMVCHHEASEHPLVLSCVDLSTWCYLCQAYVHHEDLQDVKNAAHQNKFGEGMPHLQ

[Multiple Choices]
A. Position 357 (For beta-ketoacyl synthase activity)
B. Position 181 (Charge relay system)
C. Position 224 (Proton donor)
D. Position 215 (1)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates position 215 as active site 1. This annotation is transferred by similarity from UniProtKB:Q9UBN7 (ECO:0000250), so it supports D but is not direct experimental evidence for this rat sequence.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a catalytic domain, but sequence motifs and general enzyme knowledge do not establish that position 215 is the annotated active-site residue rather than the other listed positions.


**Missing item-specific fact**

> The active-site annotation mapping position 215 to active site 1, or equivalent protein-specific structural or experimental evidence, is absent from the input.


**Reason**

> Selecting the keyed position requires protein-specific active-site information; recognizing the family or applying generic sequence heuristics does not establish the exact residue.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports position 215 among the listed choices. Although the sequence-matched record also annotates a second active-site position, 641, that position is not an option, and the evidence does not establish another listed choice as correct.


### Important caveats

- The annotation at position 215 is similarity-transferred from Q9UBN7, not shown here to be experimentally verified for the supplied rat protein.
- The matching record also annotates active site 2 at position 641, so the keyed choice identifies one annotated site rather than all active-site positions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a catalytic domain, but sequence motifs and general enzyme knowledge do not establish that position 215 is the annotated active-site residue rather than the other listed positions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The active-site annotation mapping position 215 to active site 1, or equivalent protein-specific structural or experimental evidence, is absent from the input.",
    "reason": "Selecting the keyed position requires protein-specific active-site information; recognizing the family or applying generic sequence heuristics does not establish the exact residue."
  },
  "case_id": "active_site_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 215 as active site 1. This annotation is transferred by similarity from UniProtKB:Q9UBN7 (ECO:0000250), so it supports D but is not direct experimental evidence for this rat sequence."
  },
  "important_caveats": [
    "The annotation at position 215 is similarity-transferred from Q9UBN7, not shown here to be experimentally verified for the supplied rat protein.",
    "The matching record also annotates active site 2 at position 641, so the keyed choice identifies one annotated site rather than all active-site positions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports position 215 among the listed choices. Although the sequence-matched record also annotates a second active-site position, 641, that position is not an option, and the evidence does not establish another listed choice as correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 215 as active site 1. This annotation is transferred by similarity from UniProtKB:Q9UBN7 (ECO:0000250), so it supports D but is not direct experimental evidence for this rat sequence.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a catalytic domain, but sequence motifs and general enzyme knowledge do not establish that position 215 is the annotated active-site residue rather than the other listed positions.",
    "missing_item_specific_fact": "The active-site annotation mapping position 215 to active site 1, or equivalent protein-specific structural or experimental evidence, is absent from the input.",
    "reason": "Selecting the keyed position requires protein-specific active-site information; recognizing the family or applying generic sequence heuristics does not establish the exact residue."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports position 215 among the listed choices. Although the sequence-matched record also annotates a second active-site position, 641, that position is not an option, and the evidence does not establish another listed choice as correct."
  },
  "important_caveats": [
    "The annotation at position 215 is similarity-transferred from Q9UBN7, not shown here to be experimentally verified for the supplied rat protein.",
    "The matching record also annotates active site 2 at position 641, so the keyed choice identifies one annotated site rather than all active-site positions."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A8I6GM68 (Rat HDAC6, sequence exactly matched) annotates position 215 as 'Active site' with label '1' in both the current entry (C5) and the historical archived entry (H2). The evidence code ECO:0000250 indicates inference by similarity from human HDAC6 (Q9UBN7), a computational transfer annotation rather than direct experimental measurement on the rat protein. However, the underlying catalytic tyrosine mechanism is well-established for HDAC family enzymes, and the annotation is consistent across entry versions. The sequence match is exact (SHA-256 confirmed), so the annotation applies to the supplied sequence.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can eliminate A (beta-ketoacyl synthase is unrelated to HDACs) and B (charge relay system is a serine-protease mechanism, not applicable to zinc-dependent deacetylases). The protein contains recognizable HDAC domain motifs (e.g., 'GMAVIRPPGHHAQRSLMDGYCMFNHLAVAARYAQKKHRIQRILIVDWDVHHGQGTQFIFDQDPSVLYFSIHRYEHGRFWPHLKASNWSTTGFGQGQGYTINVPWNQVSFCSHKLSLACFPRGSREMTDYYIAFLCLQVGMRDADYIAAFLHILLPVAFEFQPQLVLVAAGFDALHGDPKGEMSATPAGFAHLTHFLMGLAGGKLILSLEGGYNLHALAKGVSGSLHTLLGDPCPMLESPVAPCASAQTSISCTLEALEPFWEVLERSVEPQDEDEVEGDMLEDEEEEGHWEATALPMDTWPLLQNRTGLVYDERMMSHCNLWDNHHPETPQRILRIMCHLEEVGLAARCLILPARPALDSELLTCHSAEYVERLRATEKMKTRDLHREGANFESIYICPSTFACAQLATGAACRLVEAVLSGEVLNGIAIVRPPGHHAEPDAACGFCFFNSVAVAARHAQVIAGRALRILIVDWDVHHGNGTQHIFEEDPSVLYVSLHRYDRGTFFPMGDEGASSQVGRAAGTGFTVNVPWNGPRMGDADYLATWHRLVLPIAYEFNPELVLISAGFDAAQGDPLGGCQVTPEGYAHLTHLLMGLAGGRIILILEGGYNLTSISESMAACTHSLLGDPPPQLTSLRPPQSGALASISEVIQVHRKYWRSLRLMKMEDKEERSSSRLVIKKLPQSASPVSAKGMTTPKGKVLEAGMRKPTAALPTKESTLGQAKAKTAKALLAQGQSSEQAAKGTTLDLATSKDTVGGATTDQCASVAATENSANQTTSGEEASGETESFGTSPSSNASKQTTGASPLHGAAAQQSPELGLSSTLELSSEAQEVQESEEGLLGEAAGGQDMNSLMLTQGFGDFNTQDVFYAVTPLSWCPHLMAVCPIPAAGLDVSQPCKTCGSVQENWVCLTCYQVYCSRYVNAHMVCHHEASEHPLVLSCVDLSTWCYLCQAYVHHEDLQDVKNAAHQNKFGEGMPHLQ'), and one can infer a catalytic tyrosine as proton donor. However, distinguishing position 215 from position 224 (option C, which also correctly describes the mechanism as 'Proton donor') requires knowing the exact residue numbering from structural/annotation data.


**Missing item-specific fact**

> The precise residue index (215 vs 224) of the catalytic tyrosine in the rat HDAC6 DD1 domain, which is a database annotation (ECO:0000250 transfer from Q9UBN7) rather than something derivable from general sequence analysis. Additionally, the '(1)' label in option D is a UniProt annotation artifact that further signals database lookup.


**Reason**

> While the question allows elimination of A and B through general biological knowledge, the critical distinction between C (position 224, 'Proton donor') and D (position 215, '1') cannot be resolved by reasoning about the sequence alone. Both positions fall within the first deacetylase domain, and the mechanistic role ('proton donor') is identical. The exact index requires the specific UniProt annotation or structural knowledge of this particular protein. The parenthetical '(1)' in option D is a database label, not a biological descriptor, further indicating lookup dependence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C"
]
```

> Option C (Position 224, 'Proton donor') describes the correct catalytic mechanism for HDAC active-site tyrosines. A knowledgeable respondent who identifies the HDAC fold and the tyrosine-as-proton-donor mechanism but is uncertain about the exact residue index could plausibly select C. The 9-residue difference between 215 and 224 is not resolvable from sequence alone without the specific annotation. However, C is ultimately incorrect per the annotation, and the parenthetical '(1)' in D serves as a database-specific identifier that tips the balance toward D for those familiar with the annotation format.


### Important caveats

- The active site annotation uses evidence code ECO:0000250 (inferred by similarity from human HDAC6 Q9UBN7), meaning it is a computational transfer, not a direct experimental measurement on rat HDAC6.
- The protein is HDAC6, which has two catalytic domains; position 215 is the active site of DD1 and position 641 is the active site of DD2. The question does not specify which domain, but the options only reference DD1 positions.
- The '(1)' label in option D is a UniProt annotation artifact (the /note field), not a standard biological descriptor, making the option format database-specific.
- The sequence matches the UniProt entry exactly (SHA-256 confirmed), so numbering is canonical with no offset concerns.
- The question presents only single residues rather than the full catalytic triad/tetrad (tyrosine + zinc-binding residues), which is a simplification of the actual active site composition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can eliminate A (beta-ketoacyl synthase is unrelated to HDACs) and B (charge relay system is a serine-protease mechanism, not applicable to zinc-dependent deacetylases). The protein contains recognizable HDAC domain motifs (e.g., 'GMAVIRPPGHHAQRSLMDGYCMFNHLAVAARYAQKKHRIQRILIVDWDVHHGQGTQFIFDQDPSVLYFSIHRYEHGRFWPHLKASNWSTTGFGQGQGYTINVPWNQVSFCSHKLSLACFPRGSREMTDYYIAFLCLQVGMRDADYIAAFLHILLPVAFEFQPQLVLVAAGFDALHGDPKGEMSATPAGFAHLTHFLMGLAGGKLILSLEGGYNLHALAKGVSGSLHTLLGDPCPMLESPVAPCASAQTSISCTLEALEPFWEVLERSVEPQDEDEVEGDMLEDEEEEGHWEATALPMDTWPLLQNRTGLVYDERMMSHCNLWDNHHPETPQRILRIMCHLEEVGLAARCLILPARPALDSELLTCHSAEYVERLRATEKMKTRDLHREGANFESIYICPSTFACAQLATGAACRLVEAVLSGEVLNGIAIVRPPGHHAEPDAACGFCFFNSVAVAARHAQVIAGRALRILIVDWDVHHGNGTQHIFEEDPSVLYVSLHRYDRGTFFPMGDEGASSQVGRAAGTGFTVNVPWNGPRMGDADYLATWHRLVLPIAYEFNPELVLISAGFDAAQGDPLGGCQVTPEGYAHLTHLLMGLAGGRIILILEGGYNLTSISESMAACTHSLLGDPPPQLTSLRPPQSGALASISEVIQVHRKYWRSLRLMKMEDKEERSSSRLVIKKLPQSASPVSAKGMTTPKGKVLEAGMRKPTAALPTKESTLGQAKAKTAKALLAQGQSSEQAAKGTTLDLATSKDTVGGATTDQCASVAATENSANQTTSGEEASGETESFGTSPSSNASKQTTGASPLHGAAAQQSPELGLSSTLELSSEAQEVQESEEGLLGEAAGGQDMNSLMLTQGFGDFNTQDVFYAVTPLSWCPHLMAVCPIPAAGLDVSQPCKTCGSVQENWVCLTCYQVYCSRYVNAHMVCHHEASEHPLVLSCVDLSTWCYLCQAYVHHEDLQDVKNAAHQNKFGEGMPHLQ'), and one can infer a catalytic tyrosine as proton donor. However, distinguishing position 215 from position 224 (option C, which also correctly describes the mechanism as 'Proton donor') requires knowing the exact residue numbering from structural/annotation data.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise residue index (215 vs 224) of the catalytic tyrosine in the rat HDAC6 DD1 domain, which is a database annotation (ECO:0000250 transfer from Q9UBN7) rather than something derivable from general sequence analysis. Additionally, the '(1)' label in option D is a UniProt annotation artifact that further signals database lookup.",
    "reason": "While the question allows elimination of A and B through general biological knowledge, the critical distinction between C (position 224, 'Proton donor') and D (position 215, '1') cannot be resolved by reasoning about the sequence alone. Both positions fall within the first deacetylase domain, and the mechanistic role ('proton donor') is identical. The exact index requires the specific UniProt annotation or structural knowledge of this particular protein. The parenthetical '(1)' in option D is a database label, not a biological descriptor, further indicating lookup dependence."
  },
  "case_id": "active_site_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A8I6GM68 (Rat HDAC6, sequence exactly matched) annotates position 215 as 'Active site' with label '1' in both the current entry (C5) and the historical archived entry (H2). The evidence code ECO:0000250 indicates inference by similarity from human HDAC6 (Q9UBN7), a computational transfer annotation rather than direct experimental measurement on the rat protein. However, the underlying catalytic tyrosine mechanism is well-established for HDAC family enzymes, and the annotation is consistent across entry versions. The sequence match is exact (SHA-256 confirmed), so the annotation applies to the supplied sequence."
  },
  "important_caveats": [
    "The active site annotation uses evidence code ECO:0000250 (inferred by similarity from human HDAC6 Q9UBN7), meaning it is a computational transfer, not a direct experimental measurement on rat HDAC6.",
    "The protein is HDAC6, which has two catalytic domains; position 215 is the active site of DD1 and position 641 is the active site of DD2. The question does not specify which domain, but the options only reference DD1 positions.",
    "The '(1)' label in option D is a UniProt annotation artifact (the /note field), not a standard biological descriptor, making the option format database-specific.",
    "The sequence matches the UniProt entry exactly (SHA-256 confirmed), so numbering is canonical with no offset concerns.",
    "The question presents only single residues rather than the full catalytic triad/tetrad (tyrosine + zinc-binding residues), which is a simplification of the actual active site composition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C"
    ],
    "reason": "Option C (Position 224, 'Proton donor') describes the correct catalytic mechanism for HDAC active-site tyrosines. A knowledgeable respondent who identifies the HDAC fold and the tyrosine-as-proton-donor mechanism but is uncertain about the exact residue index could plausibly select C. The 9-residue difference between 215 and 224 is not resolvable from sequence alone without the specific annotation. However, C is ultimately incorrect per the annotation, and the parenthetical '(1)' in D serves as a database-specific identifier that tips the balance toward D for those familiar with the annotation format."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A8I6GM68 (Rat HDAC6, sequence exactly matched) annotates position 215 as 'Active site' with label '1' in both the current entry (C5) and the historical archived entry (H2). The evidence code ECO:0000250 indicates inference by similarity from human HDAC6 (Q9UBN7), a computational transfer annotation rather than direct experimental measurement on the rat protein. However, the underlying catalytic tyrosine mechanism is well-established for HDAC family enzymes, and the annotation is consistent across entry versions. The sequence match is exact (SHA-256 confirmed), so the annotation applies to the supplied sequence.",
    "evidence_ids": ["C5", "H2", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can eliminate A (beta-ketoacyl synthase is unrelated to HDACs) and B (charge relay system is a serine-protease mechanism, not applicable to zinc-dependent deacetylases). The protein contains recognizable HDAC domain motifs (e.g., 'GMAVIRPPGHHAQRSLMDGYCMFNHLAVAARYAQKKHRIQRILIVDWDVHHGQGTQFIFDQDPSVLYFSIHRYEHGRFWPHLKASNWSTTGFGQGQGYTINVPWNQVSFCSHKLSLACFPRGSREMTDYYIAFLCLQVGMRDADYIAAFLHILLPVAFEFQPQLVLVAAGFDALHGDPKGEMSATPAGFAHLTHFLMGLAGGKLILSLEGGYNLHALAKGVSGSLHTLLGDPCPMLESPVAPCASAQTSISCTLEALEPFWEVLERSVEPQDEDEVEGDMLEDEEEEGHWEATALPMDTWPLLQNRTGLVYDERMMSHCNLWDNHHPETPQRILRIMCHLEEVGLAARCLILPARPALDSELLTCHSAEYVERLRATEKMKTRDLHREGANFESIYICPSTFACAQLATGAACRLVEAVLSGEVLNGIAIVRPPGHHAEPDAACGFCFFNSVAVAARHAQVIAGRALRILIVDWDVHHGNGTQHIFEEDPSVLYVSLHRYDRGTFFPMGDEGASSQVGRAAGTGFTVNVPWNGPRMGDADYLATWHRLVLPIAYEFNPELVLISAGFDAAQGDPLGGCQVTPEGYAHLTHLLMGLAGGRIILILEGGYNLTSISESMAACTHSLLGDPPPQLTSLRPPQSGALASISEVIQVHRKYWRSLRLMKMEDKEERSSSRLVIKKLPQSASPVSAKGMTTPKGKVLEAGMRKPTAALPTKESTLGQAKAKTAKALLAQGQSSEQAAKGTTLDLATSKDTVGGATTDQCASVAATENSANQTTSGEEASGETESFGTSPSSNASKQTTGASPLHGAAAQQSPELGLSSTLELSSEAQEVQESEEGLLGEAAGGQDMNSLMLTQGFGDFNTQDVFYAVTPLSWCPHLMAVCPIPAAGLDVSQPCKTCGSVQENWVCLTCYQVYCSRYVNAHMVCHHEASEHPLVLSCVDLSTWCYLCQAYVHHEDLQDVKNAAHQNKFGEGMPHLQ'), and one can infer a catalytic tyrosine as proton donor. However, distinguishing position 215 from position 224 (option C, which also correctly describes the mechanism as 'Proton donor') requires knowing the exact residue numbering from structural/annotation data.",
    "missing_item_specific_fact": "The precise residue index (215 vs 224) of the catalytic tyrosine in the rat HDAC6 DD1 domain, which is a database annotation (ECO:0000250 transfer from Q9UBN7) rather than something derivable from general sequence analysis. Additionally, the '(1)' label in option D is a UniProt annotation artifact that further signals database lookup.",
    "reason": "While the question allows elimination of A and B through general biological knowledge, the critical distinction between C (position 224, 'Proton donor') and D (position 215, '1') cannot be resolved by reasoning about the sequence alone. Both positions fall within the first deacetylase domain, and the mechanistic role ('proton donor') is identical. The exact index requires the specific UniProt annotation or structural knowledge of this particular protein. The parenthetical '(1)' in option D is a database label, not a biological descriptor, further indicating lookup dependence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C"],
    "reason": "Option C (Position 224, 'Proton donor') describes the correct catalytic mechanism for HDAC active-site tyrosines. A knowledgeable respondent who identifies the HDAC fold and the tyrosine-as-proton-donor mechanism but is uncertain about the exact residue index could plausibly select C. The 9-residue difference between 215 and 224 is not resolvable from sequence alone without the specific annotation. However, C is ultimately incorrect per the annotation, and the parenthetical '(1)' in D serves as a database-specific identifier that tips the balance toward D for those familiar with the annotation format."
  },
  "important_caveats": [
    "The active site annotation uses evidence code ECO:0000250 (inferred by similarity from human HDAC6 Q9UBN7), meaning it is a computational transfer, not a direct experimental measurement on rat HDAC6.",
    "The protein is HDAC6, which has two catalytic domains; position 215 is the active site of DD1 and position 641 is the active site of DD2. The question does not specify which domain, but the options only reference DD1 positions.",
    "The '(1)' label in option D is a UniProt annotation artifact (the /note field), not a standard biological descriptor, making the option format database-specific.",
    "The sequence matches the UniProt entry exactly (SHA-256 confirmed), so numbering is canonical with no offset concerns.",
    "The question presents only single residues rather than the full catalytic triad/tetrad (tyrosine + zinc-binding residues), which is a simplification of the actual active site composition."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies position 215 as an active site, labeled "1". This is a homology-transferred annotation, not direct experimental evidence for this rat protein, so it supports the key as an annotation rather than independently establishing experimental validation.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two recognizable, homologous HDAC catalytic-domain regions. In the first domain, the conserved PP-GHH-region motif near position 215 is characteristic of the catalytic pocket of zinc-dependent histone deacetylases, providing a transferable family-level reason to favor D over the beta-ketoacyl-synthase distractor and the other proposed positions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the conserved HDAC catalytic-domain pattern and locating it in the supplied sequence gives a meaningful basis for selecting position 215; this does not require recalling this exact protein's database record. The precise annotation label is not itself derivable with certainty from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D is supported by the conserved catalytic-motif inference among the listed choices. The prompt asks for residue type and position, while the options provide positions and role labels, but that wording mismatch does not make another listed choice comparably defensible.


### Important caveats

- The source annotation is explicitly transferred by similarity to a homolog; it should not be described as direct experimental validation for this sequence.
- HDAC6 has two catalytic domains, but the offered choices include only one of the annotated active-site positions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two recognizable, homologous HDAC catalytic-domain regions. In the first domain, the conserved PP-GHH-region motif near position 215 is characteristic of the catalytic pocket of zinc-dependent histone deacetylases, providing a transferable family-level reason to favor D over the beta-ketoacyl-synthase distractor and the other proposed positions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the conserved HDAC catalytic-domain pattern and locating it in the supplied sequence gives a meaningful basis for selecting position 215; this does not require recalling this exact protein's database record. The precise annotation label is not itself derivable with certainty from sequence alone."
  },
  "case_id": "active_site_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 215 as an active site, labeled \"1\". This is a homology-transferred annotation, not direct experimental evidence for this rat protein, so it supports the key as an annotation rather than independently establishing experimental validation."
  },
  "important_caveats": [
    "The source annotation is explicitly transferred by similarity to a homolog; it should not be described as direct experimental validation for this sequence.",
    "HDAC6 has two catalytic domains, but the offered choices include only one of the annotated active-site positions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D is supported by the conserved catalytic-motif inference among the listed choices. The prompt asks for residue type and position, while the options provide positions and role labels, but that wording mismatch does not make another listed choice comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 215 as an active site, labeled \"1\". This is a homology-transferred annotation, not direct experimental evidence for this rat protein, so it supports the key as an annotation rather than independently establishing experimental validation.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two recognizable, homologous HDAC catalytic-domain regions. In the first domain, the conserved PP-GHH-region motif near position 215 is characteristic of the catalytic pocket of zinc-dependent histone deacetylases, providing a transferable family-level reason to favor D over the beta-ketoacyl-synthase distractor and the other proposed positions.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the conserved HDAC catalytic-domain pattern and locating it in the supplied sequence gives a meaningful basis for selecting position 215; this does not require recalling this exact protein's database record. The precise annotation label is not itself derivable with certainty from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D is supported by the conserved catalytic-motif inference among the listed choices. The prompt asks for residue type and position, while the options provide positions and role labels, but that wording mismatch does not make another listed choice comparably defensible."
  },
  "important_caveats": [
    "The source annotation is explicitly transferred by similarity to a homolog; it should not be described as direct experimental validation for this sequence.",
    "HDAC6 has two catalytic domains, but the offered choices include only one of the annotated active-site positions."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (rat HDAC6, A0A8I6GM68) annotates position 215 as 'Active site' with note '1', matching option D exactly. However, the annotation evidence code is ECO:0000250 (similarity to human HDAC6 Q9UBN7), meaning this is a computational transfer rather than experimental determination for this specific protein. The sequence match is confirmed (SHA256 matched). The annotation is consistent with the conserved HDAC catalytic His in the 'RPPGHHA' motif at positions 210-216, where H215 is the second His.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark HDAC catalytic motifs: 'RPPGHHA' (positions 210-216), 'IVDWDVHHG' (positions ~248-256), 'AGFD', and 'GLAGG', identifying this as a class IIb histone deacetylase (HDAC6 family). In HDAC family members (HDAC4, HDAC6, HDAC8, etc.), the His in the 'RPPGHHA' motif is the catalytic histidine that activates the zinc-bound water nucleophile for deacetylation. This is a well-established, transferable structural feature observed across multiple HDAC crystal structures. Counting from the N-terminus, the second H in 'RPPGHHA' falls at position 215. Option A is eliminated because 'beta-ketoacyl synthase' is a fatty-acid synthase enzyme unrelated to deacetylases. Option B (position 181) is a Serine in the context 'SCAC', which cannot participate in a His-Asp charge relay. Between C (Y224, 'proton donor') and D (H215), the His in 'RPPGHHA' is the residue that directly catalyzes nucleophile activation, while the Tyr in 'MDGY' acts as a proton shuttle. The 'RPPGHHA' motif is the most universally recognized HDAC catalytic signature, making H215 the primary catalytic residue.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the HDAC family by conserved motifs, identify the catalytic His in 'RPPGHHA' as the primary active-site residue from HDAC structural biology (HDAC8, HDAC4, HDAC6 literature), count to position 215, and eliminate the clearly wrong distractors (A: wrong enzyme class; B: Serine cannot be a charge relay residue). The distinction between H215 and Y224 is supported by the well-known catalytic mechanism where the His activates the water nucleophile.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C"
]
```

> Y224 (in the 'MDGY' context) is the catalytic tyrosine in HDACs, analogous to Y248 in HDAC8, and is labeled 'Proton donor' in option C. In HDAC8, UniProt annotates Y248 (not H142) as the active site. A model reasoning from HDAC8 or general HDAC mechanism knowledge could argue that the Tyr is 'the' catalytic residue. The UniProt annotation for this specific protein resolves the ambiguity in favor of H215, but the C/D distinction is subtle and depends on which HDAC family member's annotation convention is applied.


### Important caveats

- The active-site annotation at position 215 is by similarity (ECO:0000250) to human HDAC6 (Q9UBN7), not by experimental determination on rat HDAC6.
- HDAC6 has two catalytic domains (DD1 and DD2); position 641 is also annotated as an active site ('2'), but it is not offered among the choices.
- Position 215 is a Histidine (H) in the 'RPPGHHA' motif, not a Tyrosine. The option text 'Position 215 (1)' does not specify the residue type, which could confuse a model expecting a catalytic Tyr.
- The distinction between H215 and Y224 as 'the' active site residue varies among HDAC family members in database annotations (e.g., HDAC8 annotates Y248 as active site), introducing some ambiguity between options C and D.
- The reviewer-only evidence confirms sequence match and annotation but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark HDAC catalytic motifs: 'RPPGHHA' (positions 210-216), 'IVDWDVHHG' (positions ~248-256), 'AGFD', and 'GLAGG', identifying this as a class IIb histone deacetylase (HDAC6 family). In HDAC family members (HDAC4, HDAC6, HDAC8, etc.), the His in the 'RPPGHHA' motif is the catalytic histidine that activates the zinc-bound water nucleophile for deacetylation. This is a well-established, transferable structural feature observed across multiple HDAC crystal structures. Counting from the N-terminus, the second H in 'RPPGHHA' falls at position 215. Option A is eliminated because 'beta-ketoacyl synthase' is a fatty-acid synthase enzyme unrelated to deacetylases. Option B (position 181) is a Serine in the context 'SCAC', which cannot participate in a His-Asp charge relay. Between C (Y224, 'proton donor') and D (H215), the His in 'RPPGHHA' is the residue that directly catalyzes nucleophile activation, while the Tyr in 'MDGY' acts as a proton shuttle. The 'RPPGHHA' motif is the most universally recognized HDAC catalytic signature, making H215 the primary catalytic residue.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the HDAC family by conserved motifs, identify the catalytic His in 'RPPGHHA' as the primary active-site residue from HDAC structural biology (HDAC8, HDAC4, HDAC6 literature), count to position 215, and eliminate the clearly wrong distractors (A: wrong enzyme class; B: Serine cannot be a charge relay residue). The distinction between H215 and Y224 is supported by the well-known catalytic mechanism where the His activates the water nucleophile."
  },
  "case_id": "active_site_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (rat HDAC6, A0A8I6GM68) annotates position 215 as 'Active site' with note '1', matching option D exactly. However, the annotation evidence code is ECO:0000250 (similarity to human HDAC6 Q9UBN7), meaning this is a computational transfer rather than experimental determination for this specific protein. The sequence match is confirmed (SHA256 matched). The annotation is consistent with the conserved HDAC catalytic His in the 'RPPGHHA' motif at positions 210-216, where H215 is the second His."
  },
  "important_caveats": [
    "The active-site annotation at position 215 is by similarity (ECO:0000250) to human HDAC6 (Q9UBN7), not by experimental determination on rat HDAC6.",
    "HDAC6 has two catalytic domains (DD1 and DD2); position 641 is also annotated as an active site ('2'), but it is not offered among the choices.",
    "Position 215 is a Histidine (H) in the 'RPPGHHA' motif, not a Tyrosine. The option text 'Position 215 (1)' does not specify the residue type, which could confuse a model expecting a catalytic Tyr.",
    "The distinction between H215 and Y224 as 'the' active site residue varies among HDAC family members in database annotations (e.g., HDAC8 annotates Y248 as active site), introducing some ambiguity between options C and D.",
    "The reviewer-only evidence confirms sequence match and annotation but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C"
    ],
    "reason": "Y224 (in the 'MDGY' context) is the catalytic tyrosine in HDACs, analogous to Y248 in HDAC8, and is labeled 'Proton donor' in option C. In HDAC8, UniProt annotates Y248 (not H142) as the active site. A model reasoning from HDAC8 or general HDAC mechanism knowledge could argue that the Tyr is 'the' catalytic residue. The UniProt annotation for this specific protein resolves the ambiguity in favor of H215, but the C/D distinction is subtle and depends on which HDAC family member's annotation convention is applied."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (rat HDAC6, A0A8I6GM68) annotates position 215 as 'Active site' with note '1', matching option D exactly. However, the annotation evidence code is ECO:0000250 (similarity to human HDAC6 Q9UBN7), meaning this is a computational transfer rather than experimental determination for this specific protein. The sequence match is confirmed (SHA256 matched). The annotation is consistent with the conserved HDAC catalytic His in the 'RPPGHHA' motif at positions 210-216, where H215 is the second His.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark HDAC catalytic motifs: 'RPPGHHA' (positions 210-216), 'IVDWDVHHG' (positions ~248-256), 'AGFD', and 'GLAGG', identifying this as a class IIb histone deacetylase (HDAC6 family). In HDAC family members (HDAC4, HDAC6, HDAC8, etc.), the His in the 'RPPGHHA' motif is the catalytic histidine that activates the zinc-bound water nucleophile for deacetylation. This is a well-established, transferable structural feature observed across multiple HDAC crystal structures. Counting from the N-terminus, the second H in 'RPPGHHA' falls at position 215. Option A is eliminated because 'beta-ketoacyl synthase' is a fatty-acid synthase enzyme unrelated to deacetylases. Option B (position 181) is a Serine in the context 'SCAC', which cannot participate in a His-Asp charge relay. Between C (Y224, 'proton donor') and D (H215), the His in 'RPPGHHA' is the residue that directly catalyzes nucleophile activation, while the Tyr in 'MDGY' acts as a proton shuttle. The 'RPPGHHA' motif is the most universally recognized HDAC catalytic signature, making H215 the primary catalytic residue.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the HDAC family by conserved motifs, identify the catalytic His in 'RPPGHHA' as the primary active-site residue from HDAC structural biology (HDAC8, HDAC4, HDAC6 literature), count to position 215, and eliminate the clearly wrong distractors (A: wrong enzyme class; B: Serine cannot be a charge relay residue). The distinction between H215 and Y224 is supported by the well-known catalytic mechanism where the His activates the water nucleophile."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C"],
    "reason": "Y224 (in the 'MDGY' context) is the catalytic tyrosine in HDACs, analogous to Y248 in HDAC8, and is labeled 'Proton donor' in option C. In HDAC8, UniProt annotates Y248 (not H142) as the active site. A model reasoning from HDAC8 or general HDAC mechanism knowledge could argue that the Tyr is 'the' catalytic residue. The UniProt annotation for this specific protein resolves the ambiguity in favor of H215, but the C/D distinction is subtle and depends on which HDAC family member's annotation convention is applied."
  },
  "important_caveats": [
    "The active-site annotation at position 215 is by similarity (ECO:0000250) to human HDAC6 (Q9UBN7), not by experimental determination on rat HDAC6.",
    "HDAC6 has two catalytic domains (DD1 and DD2); position 641 is also annotated as an active site ('2'), but it is not offered among the choices.",
    "Position 215 is a Histidine (H) in the 'RPPGHHA' motif, not a Tyrosine. The option text 'Position 215 (1)' does not specify the residue type, which could confuse a model expecting a catalytic Tyr.",
    "The distinction between H215 and Y224 as 'the' active site residue varies among HDAC family members in database annotations (e.g., HDAC8 annotates Y248 as active site), introducing some ambiguity between options C and D.",
    "The reviewer-only evidence confirms sequence match and annotation but was not available to the evaluated model."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0A8I6GM68",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "6d9edbee508d7fe58beded1f01767c150bdc6cd16fea4e36bfc8dd392f2beb73",
  "benchmark_sequence_length": 1183,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-05-25",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "current_source_sequence_sha256": "6d9edbee508d7fe58beded1f01767c150bdc6cd16fea4e36bfc8dd392f2beb73",
  "current_source_sequence_length": 1183,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 19,
  "selected_historical_version": {
    "accession": "A0A8I6GM68",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HDAC6_RAT",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "selected_historical_source_sequence_sha256": "6d9edbee508d7fe58beded1f01767c150bdc6cd16fea4e36bfc8dd392f2beb73",
  "selected_historical_source_sequence_length": 1183,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A8I6GM68\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-05-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Rat\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002494\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9UBN7\",\"source\":\"UniProtKB\"}],\"value\":\"2.3.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"E3 ubiquitin-protein ligase HDAC6\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9UBN7\",\"source\":\"UniProtKB\"}],\"value\":\"3.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Tubulin-lysine deacetylase HDAC6\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9UBN7\",\"source\":\"UniProtKB\"}],\"value\":\"3.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Protein deacetylase HDAC6\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9UBN7\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":215},\"start\":{\"modifier\":\"EXACT\",\"value\":215}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9UBN7\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":641},\"start\":{\"modifier\":\"EXACT\",\"value\":641}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"1\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1081},\"start\":{\"modifier\":\"EXACT\",\"value\":1081}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"1\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1083},\"start\":{\"modifier\":\"EXACT\",\"value\":1083}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"2\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1101},\"start\":{\"modifier\":\"EXACT\",\"value\":1101}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/18",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"2\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1104},\"start\":{\"modifier\":\"EXACT\",\"value\":1104}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/19",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"3\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1113},\"start\":{\"modifier\":\"EXACT\",\"value\":1113}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/20",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"3\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1116},\"start\":{\"modifier\":\"EXACT\",\"value\":1116}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/21",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"2\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1121},\"start\":{\"modifier\":\"EXACT\",\"value\":1121}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/22",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"2\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1128},\"start\":{\"modifier\":\"EXACT\",\"value\":1128}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/23",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"3\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1132},\"start\":{\"modifier\":\"EXACT\",\"value\":1132}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/24",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"3\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1138},\"start\":{\"modifier\":\"EXACT\",\"value\":1138}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/25",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"1\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1151},\"start\":{\"modifier\":\"EXACT\",\"value\":1151}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GM68.json",
  "source_sha256": "9141e1d535119088234545225bc4ad0ed1a2b60ab7625fd7b063733a1ed106d1",
  "retrieved_utc": "2026-11-02T04:26:02.236008+00:00",
  "json_pointer": "/features/26",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00502\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"label\":\"1\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1154},\"start\":{\"modifier\":\"EXACT\",\"value\":1154}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   HDAC6_RAT               Reviewed;        1183 AA.\nAC   A0A8I6GM68;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-MAY-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Protein deacetylase HDAC6 {ECO:0000305};\nDE            EC=3.5.1.- {ECO:0000250|UniProtKB:Q9UBN7};\nDE   AltName: Full=E3 ubiquitin-protein ligase HDAC6 {ECO:0000305};\nDE            EC=2.3.2.- {ECO:0000250|UniProtKB:Q9UBN7};\nDE   AltName: Full=Tubulin-lysine deacetylase HDAC6 {ECO:0000305};\nDE            EC=3.5.1.- {ECO:0000250|UniProtKB:Q9UBN7};\nGN   Name=Hdac6 {ECO:0000312|RGD:619981};\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116 {ECO:0000312|Proteomes:UP000002494};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 366-368",
  "excerpt": "FT   ACT_SITE        215\nFT                   /note=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9UBN7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 369-371",
  "excerpt": "FT   ACT_SITE        641\nFT                   /note=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9UBN7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 372-376",
  "excerpt": "FT   BINDING         1081\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 377-381",
  "excerpt": "FT   BINDING         1083\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 382-386",
  "excerpt": "FT   BINDING         1101\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 387-391",
  "excerpt": "FT   BINDING         1104\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 392-396",
  "excerpt": "FT   BINDING         1113\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 397-401",
  "excerpt": "FT   BINDING         1116\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 402-406",
  "excerpt": "FT   BINDING         1121\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 407-411",
  "excerpt": "FT   BINDING         1128\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 412-416",
  "excerpt": "FT   BINDING         1132\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 417-421",
  "excerpt": "FT   BINDING         1138\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 422-426",
  "excerpt": "FT   BINDING         1151\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GM68?format=txt&versions=19",
  "source_sha256": "58fcde5c33fd6fa5c1e7ab9aba45d973ba90d90a0d5f4aec75b9a9719bb48c50",
  "retrieved_utc": "2026-11-02T04:26:04.375301+00:00",
  "source_locator": "lines 427-431",
  "excerpt": "FT   BINDING         1154\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00502\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
