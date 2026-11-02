# cofactor_0109

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAISPEVEHPNKAFGFAARDPSGLLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSQDLENYCPDQILTYSATYTDGTTTYGGYSSLMVADEHFVIRWPENLPMDIGAPLLCAGITTYSPLRHFGLDKPGTHVGIVGLGGLGHVAVKFAKAFGAKVTVISTSEGKKQEAVEKLGADAFLVSRDPEQMQAAAATLDGIIDTVSAVHPILPLVNLLKSQGKLIMVGAPEKPIELPVFPLLLGRKIVAGSAIGGLKETQDMIDFAAKHNILPDVELIPMDYVNTAMERLLKADVKYRFVIDICNTLKSA

[Multiple Choices]
A. heme b
B. Zn(2+)
C. NAD(+)
D. Fe(2+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry for vomilenine reductase, which annotates Zn(2+) and says it binds two zinc ions per subunit. However, this cofactor annotation is transferred from a homolog (ECO:0000250), not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains conspicuous Cys/His-rich regions, including a Cys/His cluster near the N-terminus and another Cys-rich segment, consistent with metal coordination and favoring Zn(2+) over heme b or NAD(+).


**Missing item-specific fact**

> No external fact is strictly needed for a defensible inference from the sequence, although the zinc annotation and its two-ion stoichiometry are not supplied to the model.


**Reason**

> The Cys/His-rich sequence provides a concrete metal-binding clue that meaningfully favors zinc among the choices. It supports an inference, not certainty or direct experimental confirmation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence’s metal-binding pattern favors Zn(2+); the supplied evidence does not establish another listed option as an equally defensible answer.


### Important caveats

- The database annotation is sequence-matched but based on transfer from a homolog rather than direct experimental evidence for this protein.
- A metal-binding motif supports prediction but alone does not prove the metal identity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains conspicuous Cys/His-rich regions, including a Cys/His cluster near the N-terminus and another Cys-rich segment, consistent with metal coordination and favoring Zn(2+) over heme b or NAD(+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external fact is strictly needed for a defensible inference from the sequence, although the zinc annotation and its two-ion stoichiometry are not supplied to the model.",
    "reason": "The Cys/His-rich sequence provides a concrete metal-binding clue that meaningfully favors zinc among the choices. It supports an inference, not certainty or direct experimental confirmation."
  },
  "case_id": "cofactor_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for vomilenine reductase, which annotates Zn(2+) and says it binds two zinc ions per subunit. However, this cofactor annotation is transferred from a homolog (ECO:0000250), not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The database annotation is sequence-matched but based on transfer from a homolog rather than direct experimental evidence for this protein.",
    "A metal-binding motif supports prediction but alone does not prove the metal identity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence’s metal-binding pattern favors Zn(2+); the supplied evidence does not establish another listed option as an equally defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for vomilenine reductase, which annotates Zn(2+) and says it binds two zinc ions per subunit. However, this cofactor annotation is transferred from a homolog (ECO:0000250), not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains conspicuous Cys/His-rich regions, including a Cys/His cluster near the N-terminus and another Cys-rich segment, consistent with metal coordination and favoring Zn(2+) over heme b or NAD(+).",
    "missing_item_specific_fact": "No external fact is strictly needed for a defensible inference from the sequence, although the zinc annotation and its two-ion stoichiometry are not supplied to the model.",
    "reason": "The Cys/His-rich sequence provides a concrete metal-binding clue that meaningfully favors zinc among the choices. It supports an inference, not certainty or direct experimental confirmation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence’s metal-binding pattern favors Zn(2+); the supplied evidence does not establish another listed option as an equally defensible answer."
  },
  "important_caveats": [
    "The database annotation is sequence-matched but based on transfer from a homolog rather than direct experimental evidence for this protein.",
    "A metal-binding motif supports prediction but alone does not prove the metal identity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXJ3 (vomilenine reductase, EC 1.5.1.32, CAD2-homolog) annotates Zn(2+) as the cofactor, noting 'Binds 2 Zn(2+) ions per subunit' (C5, H5). This is consistent with the protein being a member of the alcohol dehydrogenase/reductase superfamily, which characteristically uses Zn(2+) as a catalytic metal cofactor. However, the evidence code is ECO:0000250 (inferred by similarity from P06525), meaning the Zn(2+) assignment is a computational transfer annotation rather than direct experimental measurement on this specific enzyme. The sequence contains Cys/His-rich motifs (e.g., 'LYCGICHSDLHM', 'GCLVGSCRKCDMCSQ') consistent with Zn coordination in the ADH family, providing indirect sequence-level support.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains both Zn-binding motifs (Cys/His clusters such as 'LYCGICHSDLHM' and 'GCLVGSCRKCDMCSQ') and a Rossmann-fold NAD-binding motif ('GGLGHVAVKFAKAFG'). A model could reason that alcohol-dehydrogenase-family enzymes use Zn(2+) as the catalytic cofactor while NAD+ serves as a co-substrate, and that the question asks for 'cofactor' in the strict metal-ion sense. However, this reasoning requires (a) correct family assignment from a 360-aa plant sequence without a BLAST-like tool, and (b) application of the cofactor-vs-co-substrate convention to override the EC 1.5.1.32 classification, which explicitly designates NAD+ as the electron acceptor.


**Missing item-specific fact**

> The Zn(2+) annotation is based on similarity transfer (ECO:0000250 from P06525), not direct experimental evidence on this enzyme. The EC number 1.5.1.32 ('with NAD+ or NADP+ as acceptor') is derivable from the protein's identity but is not provided in the input. Without knowing the specific protein identity or the benchmark's convention for 'cofactor' vs. 'co-substrate,' a model must either recognize the exact sequence as a CAD2-homolog/vomilenine reductase or infer family membership from motifs alone—both of which lean toward memorization or pattern-matching rather than first-principles deduction.


**Reason**

> While the sequence carries suggestive ADH-family motifs, the critical decision between Zn(2+) (option B) and NAD+ (option C) hinges on (i) correctly assigning the protein to the alcohol dehydrogenase family from raw sequence, and (ii) applying the biochemical convention that metal ions are 'cofactors' while NAD+ is a 'co-substrate.' The EC 1.5.1.32 designation, which the model cannot see but which defines the enzyme, explicitly involves NAD+, making option C a defensible alternative. The Zn(2+) annotation itself is similarity-based, not experimentally confirmed for this protein. Selection therefore depends on protein-specific database knowledge or exact sequence recognition rather than purely general reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> EC 1.5.1.32 explicitly classifies this enzyme as an oxidoreductase 'with NAD+ or NADP+ as acceptor,' making NAD+ (C) a biochemically defensible 'cofactor' under broader usage. The sequence contains a clear Rossmann-fold NAD-binding motif ('GGLGH'). The Zn(2+) assignment rests on similarity transfer (ECO:0000250) and the convention that metal ions are cofactors while NAD+ is a co-substrate—a convention not stated in the question. Without that convention or the EC number, both B and C are reasonable answers.


### Important caveats

- The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (similarity to P06525), not direct experimental evidence for this specific vomilenine reductase. No experimental Zn-binding data for P0DXJ3 is present in the supplied evidence.
- The EC number 1.5.1.32 is not provided to the evaluated model but is intrinsic to the enzyme's identity and explicitly involves NAD+, creating genuine ambiguity with option C.
- The UniProt entry was first public in June 2025; the historical archived version (entry v2, Jan 2026) confirms the same Zn(2+) annotation, but the author's exact source snapshot is unknown.
- Sequence match is confirmed (SHA-256 match, 360 aa) between the benchmark input and both current and historical UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains both Zn-binding motifs (Cys/His clusters such as 'LYCGICHSDLHM' and 'GCLVGSCRKCDMCSQ') and a Rossmann-fold NAD-binding motif ('GGLGHVAVKFAKAFG'). A model could reason that alcohol-dehydrogenase-family enzymes use Zn(2+) as the catalytic cofactor while NAD+ serves as a co-substrate, and that the question asks for 'cofactor' in the strict metal-ion sense. However, this reasoning requires (a) correct family assignment from a 360-aa plant sequence without a BLAST-like tool, and (b) application of the cofactor-vs-co-substrate convention to override the EC 1.5.1.32 classification, which explicitly designates NAD+ as the electron acceptor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The Zn(2+) annotation is based on similarity transfer (ECO:0000250 from P06525), not direct experimental evidence on this enzyme. The EC number 1.5.1.32 ('with NAD+ or NADP+ as acceptor') is derivable from the protein's identity but is not provided in the input. Without knowing the specific protein identity or the benchmark's convention for 'cofactor' vs. 'co-substrate,' a model must either recognize the exact sequence as a CAD2-homolog/vomilenine reductase or infer family membership from motifs alone—both of which lean toward memorization or pattern-matching rather than first-principles deduction.",
    "reason": "While the sequence carries suggestive ADH-family motifs, the critical decision between Zn(2+) (option B) and NAD+ (option C) hinges on (i) correctly assigning the protein to the alcohol dehydrogenase family from raw sequence, and (ii) applying the biochemical convention that metal ions are 'cofactors' while NAD+ is a 'co-substrate.' The EC 1.5.1.32 designation, which the model cannot see but which defines the enzyme, explicitly involves NAD+, making option C a defensible alternative. The Zn(2+) annotation itself is similarity-based, not experimentally confirmed for this protein. Selection therefore depends on protein-specific database knowledge or exact sequence recognition rather than purely general reasoning from the supplied information."
  },
  "case_id": "cofactor_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ3 (vomilenine reductase, EC 1.5.1.32, CAD2-homolog) annotates Zn(2+) as the cofactor, noting 'Binds 2 Zn(2+) ions per subunit' (C5, H5). This is consistent with the protein being a member of the alcohol dehydrogenase/reductase superfamily, which characteristically uses Zn(2+) as a catalytic metal cofactor. However, the evidence code is ECO:0000250 (inferred by similarity from P06525), meaning the Zn(2+) assignment is a computational transfer annotation rather than direct experimental measurement on this specific enzyme. The sequence contains Cys/His-rich motifs (e.g., 'LYCGICHSDLHM', 'GCLVGSCRKCDMCSQ') consistent with Zn coordination in the ADH family, providing indirect sequence-level support."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (similarity to P06525), not direct experimental evidence for this specific vomilenine reductase. No experimental Zn-binding data for P0DXJ3 is present in the supplied evidence.",
    "The EC number 1.5.1.32 is not provided to the evaluated model but is intrinsic to the enzyme's identity and explicitly involves NAD+, creating genuine ambiguity with option C.",
    "The UniProt entry was first public in June 2025; the historical archived version (entry v2, Jan 2026) confirms the same Zn(2+) annotation, but the author's exact source snapshot is unknown.",
    "Sequence match is confirmed (SHA-256 match, 360 aa) between the benchmark input and both current and historical UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "EC 1.5.1.32 explicitly classifies this enzyme as an oxidoreductase 'with NAD+ or NADP+ as acceptor,' making NAD+ (C) a biochemically defensible 'cofactor' under broader usage. The sequence contains a clear Rossmann-fold NAD-binding motif ('GGLGH'). The Zn(2+) assignment rests on similarity transfer (ECO:0000250) and the convention that metal ions are cofactors while NAD+ is a co-substrate—a convention not stated in the question. Without that convention or the EC number, both B and C are reasonable answers."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ3 (vomilenine reductase, EC 1.5.1.32, CAD2-homolog) annotates Zn(2+) as the cofactor, noting 'Binds 2 Zn(2+) ions per subunit' (C5, H5). This is consistent with the protein being a member of the alcohol dehydrogenase/reductase superfamily, which characteristically uses Zn(2+) as a catalytic metal cofactor. However, the evidence code is ECO:0000250 (inferred by similarity from P06525), meaning the Zn(2+) assignment is a computational transfer annotation rather than direct experimental measurement on this specific enzyme. The sequence contains Cys/His-rich motifs (e.g., 'LYCGICHSDLHM', 'GCLVGSCRKCDMCSQ') consistent with Zn coordination in the ADH family, providing indirect sequence-level support.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains both Zn-binding motifs (Cys/His clusters such as 'LYCGICHSDLHM' and 'GCLVGSCRKCDMCSQ') and a Rossmann-fold NAD-binding motif ('GGLGHVAVKFAKAFG'). A model could reason that alcohol-dehydrogenase-family enzymes use Zn(2+) as the catalytic cofactor while NAD+ serves as a co-substrate, and that the question asks for 'cofactor' in the strict metal-ion sense. However, this reasoning requires (a) correct family assignment from a 360-aa plant sequence without a BLAST-like tool, and (b) application of the cofactor-vs-co-substrate convention to override the EC 1.5.1.32 classification, which explicitly designates NAD+ as the electron acceptor.",
    "missing_item_specific_fact": "The Zn(2+) annotation is based on similarity transfer (ECO:0000250 from P06525), not direct experimental evidence on this enzyme. The EC number 1.5.1.32 ('with NAD+ or NADP+ as acceptor') is derivable from the protein's identity but is not provided in the input. Without knowing the specific protein identity or the benchmark's convention for 'cofactor' vs. 'co-substrate,' a model must either recognize the exact sequence as a CAD2-homolog/vomilenine reductase or infer family membership from motifs alone—both of which lean toward memorization or pattern-matching rather than first-principles deduction.",
    "reason": "While the sequence carries suggestive ADH-family motifs, the critical decision between Zn(2+) (option B) and NAD+ (option C) hinges on (i) correctly assigning the protein to the alcohol dehydrogenase family from raw sequence, and (ii) applying the biochemical convention that metal ions are 'cofactors' while NAD+ is a 'co-substrate.' The EC 1.5.1.32 designation, which the model cannot see but which defines the enzyme, explicitly involves NAD+, making option C a defensible alternative. The Zn(2+) annotation itself is similarity-based, not experimentally confirmed for this protein. Selection therefore depends on protein-specific database knowledge or exact sequence recognition rather than purely general reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "EC 1.5.1.32 explicitly classifies this enzyme as an oxidoreductase 'with NAD+ or NADP+ as acceptor,' making NAD+ (C) a biochemically defensible 'cofactor' under broader usage. The sequence contains a clear Rossmann-fold NAD-binding motif ('GGLGH'). The Zn(2+) assignment rests on similarity transfer (ECO:0000250) and the convention that metal ions are cofactors while NAD+ is a co-substrate—a convention not stated in the question. Without that convention or the EC number, both B and C are reasonable answers."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (similarity to P06525), not direct experimental evidence for this specific vomilenine reductase. No experimental Zn-binding data for P0DXJ3 is present in the supplied evidence.",
    "The EC number 1.5.1.32 is not provided to the evaluated model but is intrinsic to the enzyme's identity and explicitly involves NAD+, creating genuine ambiguity with option C.",
    "The UniProt entry was first public in June 2025; the historical archived version (entry v2, Jan 2026) confirms the same Zn(2+) annotation, but the author's exact source snapshot is unknown.",
    "Sequence match is confirmed (SHA-256 match, 360 aa) between the benchmark input and both current and historical UniProt records."
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

**Accession:** `P0DXJ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
"P0DXJ3"
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"CAD2-homolog protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Protein RR6-2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsRR6-2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11937349","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.5.1.32"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"38212296","source":"PubMed"}],"value":"Vomilenine reductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"38212296","source":"PubMed"}],"value":"RsVR"}]}}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P06525","source":"UniProtKB"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P06525","source":"UniProtKB"}],"value":"Binds 2 Zn(2+) ions per subunit."}]}}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.682731+00:00.  

```text
ID   VOR1_RAUSE              Reviewed;         360 AA.
AC   P0DXJ3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};
DE            Short=RsVR {ECO:0000305|PubMed:38212296};
DE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};
DE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};
DE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};
DE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};
GN   Name=VR {ECO:0000305|PubMed:38212296};
GN   Synonyms=RR6-2 {ECO:0000303|PubMed:38212296};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.682731+00:00.  

```text
DE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};
DE            Short=RsVR {ECO:0000305|PubMed:38212296};
DE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};
DE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};
DE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};
DE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};
```

Source SHA-256: `8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)  
**Locator:** `lines 58-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.682731+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000250|UniProtKB:P06525};
CC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000250|UniProtKB:P06525};
```

Source SHA-256: `8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
