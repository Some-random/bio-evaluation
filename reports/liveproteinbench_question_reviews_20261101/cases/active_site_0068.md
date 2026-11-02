# active_site_0068

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **A** — Position 186 (Proton donor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGRNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAINSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPESYSNFFGVAYDTPPKAHALKASRLLVPTTVARPSKPVRVFASTADPGTTTADQVYKVGHNLLLAHAAAIQVYRDKFQNTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQLLGPRLREFTPDQKKLLIGSYDYVGVNYYTATYVSSAQPPHDKKKAVFHTDGNFYTTDSKDGVLIGPLAGPAWLNIVPEGIYHVLQDIKENYEDPVIYITENGVYEVNDTAKTLSEARVDTTRLHYLQDHLSKVLEARHQGVRVQGYLVWSLMDNWELRAGYTSRFGLIHIDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKARPQEDDGAFDTPRKRLRKY

[Multiple Choices]
A. Position 186 (Proton donor)
B. Position 17 (Proton acceptor)
C. Position 255 (Proton acceptor)
D. Position 51 (Proton donor (in beta-elimination))
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact-matching sequence is annotated at position 186 as an active-site proton donor. This supports choice A as a database annotation, but the annotation is transferred by similarity from UniProtKB:Q7XSK0 (ECO:0000250), not direct experimental evidence for this sequence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may be compatible with a glycosidase, where acidic residues often perform catalytic roles, but that general knowledge does not establish which listed position is the proton donor.


**Missing item-specific fact**

> The protein's active-site annotation assigning position 186 as the proton donor, or equivalent protein-specific experimental or homology evidence.


**Reason**

> The input supplies a sequence but no protein identity, enzyme-family annotation, structure, or catalytic data. Selecting position 186's specific role depends on item-specific knowledge; recognizing or predicting the sequence's annotation is not reasoning supplied by the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence specifically supports position 186 as the proton donor, and does not support the other listed options. The support is transferred annotation rather than direct experimental confirmation.


### Important caveats

- The sequence matches the cited UniProt record, but the active-site annotation is based on similarity to Q7XSK0 rather than direct experimental evidence for this protein.
- The benchmark's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may be compatible with a glycosidase, where acidic residues often perform catalytic roles, but that general knowledge does not establish which listed position is the proton donor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's active-site annotation assigning position 186 as the proton donor, or equivalent protein-specific experimental or homology evidence.",
    "reason": "The input supplies a sequence but no protein identity, enzyme-family annotation, structure, or catalytic data. Selecting position 186's specific role depends on item-specific knowledge; recognizing or predicting the sequence's annotation is not reasoning supplied by the question."
  },
  "case_id": "active_site_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-matching sequence is annotated at position 186 as an active-site proton donor. This supports choice A as a database annotation, but the annotation is transferred by similarity from UniProtKB:Q7XSK0 (ECO:0000250), not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the active-site annotation is based on similarity to Q7XSK0 rather than direct experimental evidence for this protein.",
    "The benchmark's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence specifically supports position 186 as the proton donor, and does not support the other listed options. The support is transferred annotation rather than direct experimental confirmation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching sequence is annotated at position 186 as an active-site proton donor. This supports choice A as a database annotation, but the annotation is transferred by similarity from UniProtKB:Q7XSK0 (ECO:0000250), not direct experimental evidence for this sequence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may be compatible with a glycosidase, where acidic residues often perform catalytic roles, but that general knowledge does not establish which listed position is the proton donor.",
    "missing_item_specific_fact": "The protein's active-site annotation assigning position 186 as the proton donor, or equivalent protein-specific experimental or homology evidence.",
    "reason": "The input supplies a sequence but no protein identity, enzyme-family annotation, structure, or catalytic data. Selecting position 186's specific role depends on item-specific knowledge; recognizing or predicting the sequence's annotation is not reasoning supplied by the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence specifically supports position 186 as the proton donor, and does not support the other listed options. The support is transferred annotation rather than direct experimental confirmation."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the active-site annotation is based on similarity to Q7XSK0 rather than direct experimental evidence for this protein.",
    "The benchmark's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B6ZKM3 (Ipecoside beta-D-glucosidase IpeGLU1, EC 3.2.1.220) annotates position 186 as an Active site with description 'Proton donor' (C5, H3). The residue at position 186 in the supplied sequence is Glu (E), consistent with the NEP motif (N185-E186-P187) characteristic of the proton donor in glycosyl hydrolase family 1 (GH1) beta-glucosidases. The annotation evidence code is ECO:0000250 (similarity transfer from Q7XSK0), so this is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein, but it is the authoritative database annotation and is chemically consistent with the sequence context.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the FHWD motif (~positions 141-144) diagnostic of glycosidases, and the N-E-P triad at positions 185-187 (N185, E186, P187) is the hallmark proton-donor motif of GH1 beta-glucosidases. A model with glycosidase biochemistry knowledge can identify this motif and assign Glu-186 as the proton donor. Furthermore, all three distractors can be eliminated by basic residue chemistry: position 17 is Ile (hydrophobic, not a proton acceptor), position 51 is Trp (aromatic, not a proton donor), and position 255 is Ala (non-functional side chain, not a proton acceptor). None of these residues have side chains capable of proton transfer, making them implausible catalytic residues regardless of enzyme identity.


**Missing item-specific fact**

> The question does not state the enzyme class or family. Identifying the NEP motif as specifically the proton donor (rather than, say, a binding residue) requires knowledge of GH1 catalytic mechanisms. However, the residue chemistry of the distractors (Ile, Ala, Trp) provides an independent elimination pathway that does not require family-specific knowledge.


**Reason**

> A knowledgeable reasoner can (a) recognize glycosidase-like motifs in the sequence, (b) identify the NEP proton-donor motif at positions 185-187, and (c) eliminate all distractors because Ile, Ala, and Trp lack side-chain functionality for proton transfer. This constitutes a concrete biological argument from the supplied sequence. The specialized knowledge of GH1 catalytic mechanisms is domain expertise but is not an item-specific external fact absent from the input; the relevant sequence features (NEP motif, FHWD motif) are present in the provided sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The catalytic center of this GH1 beta-glucosidase comprises two residues: Glu-186 (proton donor) and Glu-422 (nucleophile, C6/H4). Only position 186 appears among the choices. The three distractors (positions 17, 51, 255) correspond to Ile, Trp, and Ala respectively—none of which are plausible catalytic residues in any glycosidase mechanism. No other option is defensible.


### Important caveats

- The active-site annotation at position 186 carries evidence code ECO:0000250 (similarity transfer from UniProtKB:Q7XSK0), not direct experimental validation on IpeGLU1 itself. The PubMed reference (18927081) characterizes function and catalytic activity but the residue-level assignment is by homology.
- The question asks for 'the enzyme's catalytic center' but each option lists only a single residue. The full catalytic center includes both the proton donor (186) and the nucleophile (422). This is a minor wording imprecision; since only 186 appears as a valid option, it does not create ambiguity.
- The protein is a beta-glucosidase (EC 3.2.1.220) from Carapichea ipecacuanha involved in ipecac alkaloid biosynthesis. The sequence is 543 AA and matches the UniProt canonical entry exactly.
- The annotation was first integrated into Swiss-Prot in June 2025; the author's source snapshot is unknown. The historical entry (version 51, released January 2026) contains the same annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the FHWD motif (~positions 141-144) diagnostic of glycosidases, and the N-E-P triad at positions 185-187 (N185, E186, P187) is the hallmark proton-donor motif of GH1 beta-glucosidases. A model with glycosidase biochemistry knowledge can identify this motif and assign Glu-186 as the proton donor. Furthermore, all three distractors can be eliminated by basic residue chemistry: position 17 is Ile (hydrophobic, not a proton acceptor), position 51 is Trp (aromatic, not a proton donor), and position 255 is Ala (non-functional side chain, not a proton acceptor). None of these residues have side chains capable of proton transfer, making them implausible catalytic residues regardless of enzyme identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The question does not state the enzyme class or family. Identifying the NEP motif as specifically the proton donor (rather than, say, a binding residue) requires knowledge of GH1 catalytic mechanisms. However, the residue chemistry of the distractors (Ile, Ala, Trp) provides an independent elimination pathway that does not require family-specific knowledge.",
    "reason": "A knowledgeable reasoner can (a) recognize glycosidase-like motifs in the sequence, (b) identify the NEP proton-donor motif at positions 185-187, and (c) eliminate all distractors because Ile, Ala, and Trp lack side-chain functionality for proton transfer. This constitutes a concrete biological argument from the supplied sequence. The specialized knowledge of GH1 catalytic mechanisms is domain expertise but is not an item-specific external fact absent from the input; the relevant sequence features (NEP motif, FHWD motif) are present in the provided sequence."
  },
  "case_id": "active_site_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B6ZKM3 (Ipecoside beta-D-glucosidase IpeGLU1, EC 3.2.1.220) annotates position 186 as an Active site with description 'Proton donor' (C5, H3). The residue at position 186 in the supplied sequence is Glu (E), consistent with the NEP motif (N185-E186-P187) characteristic of the proton donor in glycosyl hydrolase family 1 (GH1) beta-glucosidases. The annotation evidence code is ECO:0000250 (similarity transfer from Q7XSK0), so this is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein, but it is the authoritative database annotation and is chemically consistent with the sequence context."
  },
  "important_caveats": [
    "The active-site annotation at position 186 carries evidence code ECO:0000250 (similarity transfer from UniProtKB:Q7XSK0), not direct experimental validation on IpeGLU1 itself. The PubMed reference (18927081) characterizes function and catalytic activity but the residue-level assignment is by homology.",
    "The question asks for 'the enzyme's catalytic center' but each option lists only a single residue. The full catalytic center includes both the proton donor (186) and the nucleophile (422). This is a minor wording imprecision; since only 186 appears as a valid option, it does not create ambiguity.",
    "The protein is a beta-glucosidase (EC 3.2.1.220) from Carapichea ipecacuanha involved in ipecac alkaloid biosynthesis. The sequence is 543 AA and matches the UniProt canonical entry exactly.",
    "The annotation was first integrated into Swiss-Prot in June 2025; the author's source snapshot is unknown. The historical entry (version 51, released January 2026) contains the same annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The catalytic center of this GH1 beta-glucosidase comprises two residues: Glu-186 (proton donor) and Glu-422 (nucleophile, C6/H4). Only position 186 appears among the choices. The three distractors (positions 17, 51, 255) correspond to Ile, Trp, and Ala respectively—none of which are plausible catalytic residues in any glycosidase mechanism. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B6ZKM3 (Ipecoside beta-D-glucosidase IpeGLU1, EC 3.2.1.220) annotates position 186 as an Active site with description 'Proton donor' (C5, H3). The residue at position 186 in the supplied sequence is Glu (E), consistent with the NEP motif (N185-E186-P187) characteristic of the proton donor in glycosyl hydrolase family 1 (GH1) beta-glucosidases. The annotation evidence code is ECO:0000250 (similarity transfer from Q7XSK0), so this is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein, but it is the authoritative database annotation and is chemically consistent with the sequence context.",
    "evidence_ids": ["C5", "H3", "C4", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the FHWD motif (~positions 141-144) diagnostic of glycosidases, and the N-E-P triad at positions 185-187 (N185, E186, P187) is the hallmark proton-donor motif of GH1 beta-glucosidases. A model with glycosidase biochemistry knowledge can identify this motif and assign Glu-186 as the proton donor. Furthermore, all three distractors can be eliminated by basic residue chemistry: position 17 is Ile (hydrophobic, not a proton acceptor), position 51 is Trp (aromatic, not a proton donor), and position 255 is Ala (non-functional side chain, not a proton acceptor). None of these residues have side chains capable of proton transfer, making them implausible catalytic residues regardless of enzyme identity.",
    "missing_item_specific_fact": "The question does not state the enzyme class or family. Identifying the NEP motif as specifically the proton donor (rather than, say, a binding residue) requires knowledge of GH1 catalytic mechanisms. However, the residue chemistry of the distractors (Ile, Ala, Trp) provides an independent elimination pathway that does not require family-specific knowledge.",
    "reason": "A knowledgeable reasoner can (a) recognize glycosidase-like motifs in the sequence, (b) identify the NEP proton-donor motif at positions 185-187, and (c) eliminate all distractors because Ile, Ala, and Trp lack side-chain functionality for proton transfer. This constitutes a concrete biological argument from the supplied sequence. The specialized knowledge of GH1 catalytic mechanisms is domain expertise but is not an item-specific external fact absent from the input; the relevant sequence features (NEP motif, FHWD motif) are present in the provided sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The catalytic center of this GH1 beta-glucosidase comprises two residues: Glu-186 (proton donor) and Glu-422 (nucleophile, C6/H4). Only position 186 appears among the choices. The three distractors (positions 17, 51, 255) correspond to Ile, Trp, and Ala respectively—none of which are plausible catalytic residues in any glycosidase mechanism. No other option is defensible."
  },
  "important_caveats": [
    "The active-site annotation at position 186 carries evidence code ECO:0000250 (similarity transfer from UniProtKB:Q7XSK0), not direct experimental validation on IpeGLU1 itself. The PubMed reference (18927081) characterizes function and catalytic activity but the residue-level assignment is by homology.",
    "The question asks for 'the enzyme's catalytic center' but each option lists only a single residue. The full catalytic center includes both the proton donor (186) and the nucleophile (422). This is a minor wording imprecision; since only 186 appears as a valid option, it does not create ambiguity.",
    "The protein is a beta-glucosidase (EC 3.2.1.220) from Carapichea ipecacuanha involved in ipecac alkaloid biosynthesis. The sequence is 543 AA and matches the UniProt canonical entry exactly.",
    "The annotation was first integrated into Swiss-Prot in June 2025; the author's source snapshot is unknown. The historical entry (version 51, released January 2026) contains the same annotation."
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

**Accession:** `B6ZKM3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
"B6ZKM3"
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Ipecac alkaloid beta-glucosidase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"},{"evidenceCode":"ECO:0000312","id":"BAH02544.1","source":"EMBL"}],"value":"IpeGLU1"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"3.2.1.105"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Strictosidine beta-glucosidase IpeGLU1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"3.2.1.220"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Ipecoside beta-D-glucosidase IpeGLU1"}}}
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000250","id":"Q7XSK0","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":186},"start":{"modifier":"EXACT","value":186}},"type":"Active site"}
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
{"description":"Nucleophile","evidences":[{"evidenceCode":"ECO:0000250","id":"Q7XSK0","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":422},"start":{"modifier":"EXACT","value":422}},"type":"Active site"}
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51)  
**Locator:** `lines 212-214`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:27:52.619495+00:00.  

```text
FT   ACT_SITE        186
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000250|UniProtKB:Q7XSK0"
```

Source SHA-256: `90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51)  
**Locator:** `lines 215-217`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:27:52.619495+00:00.  

```text
FT   ACT_SITE        422
FT                   /note="Nucleophile"
FT                   /evidence="ECO:0000250|UniProtKB:Q7XSK0"
```

Source SHA-256: `90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 68. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
