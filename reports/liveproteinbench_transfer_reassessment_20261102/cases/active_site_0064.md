# active_site_0064: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0064.txt)

**Task:** `active_site`  
**Author key, unchanged:** **B** — Position 64 (Nucleophile (Probable))

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MTEELTTVRDACARTLENTARTLHLGASGTEFVAAFRAMTDHWGAARPHDLPLSDVSPDGSPVEYAVDLGGLAPALQFAMEPLTAGVPARDPLAARAIMPLLAGRYGADATRWSALADRLLPDDAHGPHVSMYGAEVRAGAPIRFKAWFYLNVTGPDGAFNLLYSALERMGTTHLWPVVQAHVHRAGEDVPFLLSLDLSDDPAARVKVYFRHFAADVEEVAAVLKAYPGFEPGEVRAFCKVMMGGRRRFSDQPAVTCVSLLDAQTFDRTAATLYVPLWTYAEHDGEVRQRVHRTLAAWPEALYRYDSVLAGIAHRGLDAGTGIHNYISWQPGRTRPRMKVYLSPEMHDVTPPPLGVSQQHHLSGQTTARGRTE

[Multiple Choices]
A. Position 213 (Proton acceptor)
B. Position 64 (Nucleophile (Probable))
C. Position 931 (Proton acceptor)
D. Position 268 (Proton acceptor)
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

> The sequence exactly matches the UniProt CymD entry, which annotates residue 64 as a probable nucleophile. The same annotation appears in a historical entry predating the benchmark cutoff. This supports B as an annotation-backed answer, while the qualifier “probable” should be retained; the excerpts do not independently establish direct experimental proof of the nucleophile assignment.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C23](#evidence-c23), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence allows residue numbering and identifies residue 64 as Glu, but the supplied sequence and choices do not provide a reliable general principle for assigning this specific residue the proposed nucleophile role. Position 931 is outside the 373-residue sequence, an easy elimination that does not distinguish B from the other in-range choices.


**Missing item-specific fact**

> The protein-specific CymD active-site annotation or structural/mechanistic evidence assigning residue 64 as a probable nucleophile.


**Reason**

> Selecting B over the in-range alternatives depends on protein-specific active-site knowledge absent from the input; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only matched-sequence annotation supports B, and the supplied evidence does not establish another listed option as an equally defensible active-site assignment. The out-of-range position 931 is not a plausible coordinate for this sequence.


### Important caveats

- The active-site label is explicitly qualified as “Probable” and is evidence-linked to a publication; the excerpts do not independently validate the underlying mechanistic claim.
- The historical sequence match supports applicability, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence allows residue numbering and identifies residue 64 as Glu, but the supplied sequence and choices do not provide a reliable general principle for assigning this specific residue the proposed nucleophile role. Position 931 is outside the 373-residue sequence, an easy elimination that does not distinguish B from the other in-range choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific CymD active-site annotation or structural/mechanistic evidence assigning residue 64 as a probable nucleophile.",
    "reason": "Selecting B over the in-range alternatives depends on protein-specific active-site knowledge absent from the input; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the supplied information."
  },
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C23",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt CymD entry, which annotates residue 64 as a probable nucleophile. The same annotation appears in a historical entry predating the benchmark cutoff. This supports B as an annotation-backed answer, while the qualifier “probable” should be retained; the excerpts do not independently establish direct experimental proof of the nucleophile assignment."
  },
  "important_caveats": [
    "The active-site label is explicitly qualified as “Probable” and is evidence-linked to a publication; the excerpts do not independently validate the underlying mechanistic claim.",
    "The historical sequence match supports applicability, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports B, and the supplied evidence does not establish another listed option as an equally defensible active-site assignment. The out-of-range position 931 is not a plausible coordinate for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt CymD entry, which annotates residue 64 as a probable nucleophile. The same annotation appears in a historical entry predating the benchmark cutoff. This supports B as an annotation-backed answer, while the qualifier “probable” should be retained; the excerpts do not independently establish direct experimental proof of the nucleophile assignment.",
    "evidence_ids": ["C5", "H6", "C23", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence allows residue numbering and identifies residue 64 as Glu, but the supplied sequence and choices do not provide a reliable general principle for assigning this specific residue the proposed nucleophile role. Position 931 is outside the 373-residue sequence, an easy elimination that does not distinguish B from the other in-range choices.",
    "missing_item_specific_fact": "The protein-specific CymD active-site annotation or structural/mechanistic evidence assigning residue 64 as a probable nucleophile.",
    "reason": "Selecting B over the in-range alternatives depends on protein-specific active-site knowledge absent from the input; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports B, and the supplied evidence does not establish another listed option as an equally defensible active-site assignment. The out-of-range position 931 is not a plausible coordinate for this sequence."
  },
  "important_caveats": [
    "The active-site label is explicitly qualified as “Probable” and is evidence-linked to a publication; the excerpts do not independently validate the underlying mechanistic claim.",
    "The historical sequence match supports applicability, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A8M6W6 (CymD, Dimethylallyltryptophan synthase) annotates position 64 as 'Nucleophile (Probable)' active site (evidence ECO:0000303, citing PubMed:31251043, the 2019 Roose & Christianson crystallography paper). Position 64 in the supplied 373-aa sequence is E (glutamic acid), consistent with a carboxylate nucleophile attacking DMAPP. The binding-site annotation at 64 for L-tryptophan is additionally supported by experimental evidence (ECO:0000269) and PDB structures 6OS5/6OS6. The '(Probable)' qualifier indicates structural inference rather than definitive experimental proof of nucleophilic role, but the annotation is consistent and the answer matches the database record exactly.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H6](#evidence-h6), [H9](#evidence-h9), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> By counting residues in the supplied sequence: position 64 is E (glutamate), position 213 is F (phenylalanine), position 268 is R (arginine), and position 931 exceeds the 373-residue sequence length. General amino-acid chemistry provides meaningful discrimination: (1) position 931 is impossible, eliminating C; (2) phenylalanine has no ionizable side chain and cannot serve as a proton acceptor, eliminating A; (3) arginine's guanidinium group is a proton donor, not acceptor, eliminating D; (4) glutamate's carboxylate is a well-established nucleophile in enzymatic catalysis (e.g., serine protease catalytic triad, prenyltransferase mechanisms), making B the only chemically coherent option. The label 'Nucleophile (Probable)' aligns with a carboxylate attacking the allylic carbon of DMAPP in a prenyltransferase reaction.


**Missing item-specific fact**

> The specific mechanistic assignment of E64 as the nucleophile (rather than another glutamate or aspartate elsewhere in the sequence) derives from the 2019 crystallographic structure (PDB 6OS5/6OS6) of CymD. A general biologist could identify E as the most chemically plausible catalytic residue among the four choices, but confirming that this particular E64 (not, e.g., E81 or E234) is THE catalytic nucleophile requires protein-specific structural knowledge.


**Reason**

> The constrained multiple-choice format allows discrimination through general amino-acid chemistry: F and R are implausible proton acceptors, position 931 is out of range, and E is the only chemically sensible nucleophile among the options. This constitutes a concrete biological argument from the sequence and choices. However, the precise mechanistic role ('Nucleophile' vs. 'Proton acceptor') and the '(Probable)' qualifier are protein-specific annotations from the 2019 crystallography study, adding a lookup component for full confidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C (position 931) is trivially impossible given the 373-residue sequence. Options A (F213 as proton acceptor) and D (R268 as proton acceptor) are chemically implausible for the stated roles. Only B (E64 as nucleophile) is chemically coherent. No other option is defensible.


### Important caveats

- The active-site annotation carries the '(Probable)' qualifier and evidence code ECO:0000303 (inferred from assertion in database record), indicating structural inference rather than direct experimental proof of nucleophilic catalysis at E64.
- The binding-site annotation at position 64 for L-tryptophan is experimentally supported (ECO:0000269, PDB 6OS5/6OS6), but the specific assignment as 'Nucleophile' is a mechanistic interpretation from the crystallographic study.
- The sequence-to-accession mapping (A8M6W6) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the sequence alone.
- While the reasoning path through amino-acid chemistry is valid, the specific identification of E64 as THE catalytic nucleophile (vs. other acidic residues in the sequence) ultimately rests on protein-specific structural data from PubMed:31251043.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "By counting residues in the supplied sequence: position 64 is E (glutamate), position 213 is F (phenylalanine), position 268 is R (arginine), and position 931 exceeds the 373-residue sequence length. General amino-acid chemistry provides meaningful discrimination: (1) position 931 is impossible, eliminating C; (2) phenylalanine has no ionizable side chain and cannot serve as a proton acceptor, eliminating A; (3) arginine's guanidinium group is a proton donor, not acceptor, eliminating D; (4) glutamate's carboxylate is a well-established nucleophile in enzymatic catalysis (e.g., serine protease catalytic triad, prenyltransferase mechanisms), making B the only chemically coherent option. The label 'Nucleophile (Probable)' aligns with a carboxylate attacking the allylic carbon of DMAPP in a prenyltransferase reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific mechanistic assignment of E64 as the nucleophile (rather than another glutamate or aspartate elsewhere in the sequence) derives from the 2019 crystallographic structure (PDB 6OS5/6OS6) of CymD. A general biologist could identify E as the most chemically plausible catalytic residue among the four choices, but confirming that this particular E64 (not, e.g., E81 or E234) is THE catalytic nucleophile requires protein-specific structural knowledge.",
    "reason": "The constrained multiple-choice format allows discrimination through general amino-acid chemistry: F and R are implausible proton acceptors, position 931 is out of range, and E is the only chemically sensible nucleophile among the options. This constitutes a concrete biological argument from the sequence and choices. However, the precise mechanistic role ('Nucleophile' vs. 'Proton acceptor') and the '(Probable)' qualifier are protein-specific annotations from the 2019 crystallography study, adding a lookup component for full confidence."
  },
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H6",
      "H9",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A8M6W6 (CymD, Dimethylallyltryptophan synthase) annotates position 64 as 'Nucleophile (Probable)' active site (evidence ECO:0000303, citing PubMed:31251043, the 2019 Roose & Christianson crystallography paper). Position 64 in the supplied 373-aa sequence is E (glutamic acid), consistent with a carboxylate nucleophile attacking DMAPP. The binding-site annotation at 64 for L-tryptophan is additionally supported by experimental evidence (ECO:0000269) and PDB structures 6OS5/6OS6. The '(Probable)' qualifier indicates structural inference rather than definitive experimental proof of nucleophilic role, but the annotation is consistent and the answer matches the database record exactly."
  },
  "important_caveats": [
    "The active-site annotation carries the '(Probable)' qualifier and evidence code ECO:0000303 (inferred from assertion in database record), indicating structural inference rather than direct experimental proof of nucleophilic catalysis at E64.",
    "The binding-site annotation at position 64 for L-tryptophan is experimentally supported (ECO:0000269, PDB 6OS5/6OS6), but the specific assignment as 'Nucleophile' is a mechanistic interpretation from the crystallographic study.",
    "The sequence-to-accession mapping (A8M6W6) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the sequence alone.",
    "While the reasoning path through amino-acid chemistry is valid, the specific identification of E64 as THE catalytic nucleophile (vs. other acidic residues in the sequence) ultimately rests on protein-specific structural data from PubMed:31251043."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (position 931) is trivially impossible given the 373-residue sequence. Options A (F213 as proton acceptor) and D (R268 as proton acceptor) are chemically implausible for the stated roles. Only B (E64 as nucleophile) is chemically coherent. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A8M6W6 (CymD, Dimethylallyltryptophan synthase) annotates position 64 as 'Nucleophile (Probable)' active site (evidence ECO:0000303, citing PubMed:31251043, the 2019 Roose & Christianson crystallography paper). Position 64 in the supplied 373-aa sequence is E (glutamic acid), consistent with a carboxylate nucleophile attacking DMAPP. The binding-site annotation at 64 for L-tryptophan is additionally supported by experimental evidence (ECO:0000269) and PDB structures 6OS5/6OS6. The '(Probable)' qualifier indicates structural inference rather than definitive experimental proof of nucleophilic role, but the annotation is consistent and the answer matches the database record exactly.",
    "evidence_ids": ["C5", "C8", "H6", "H9", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "By counting residues in the supplied sequence: position 64 is E (glutamate), position 213 is F (phenylalanine), position 268 is R (arginine), and position 931 exceeds the 373-residue sequence length. General amino-acid chemistry provides meaningful discrimination: (1) position 931 is impossible, eliminating C; (2) phenylalanine has no ionizable side chain and cannot serve as a proton acceptor, eliminating A; (3) arginine's guanidinium group is a proton donor, not acceptor, eliminating D; (4) glutamate's carboxylate is a well-established nucleophile in enzymatic catalysis (e.g., serine protease catalytic triad, prenyltransferase mechanisms), making B the only chemically coherent option. The label 'Nucleophile (Probable)' aligns with a carboxylate attacking the allylic carbon of DMAPP in a prenyltransferase reaction.",
    "missing_item_specific_fact": "The specific mechanistic assignment of E64 as the nucleophile (rather than another glutamate or aspartate elsewhere in the sequence) derives from the 2019 crystallographic structure (PDB 6OS5/6OS6) of CymD. A general biologist could identify E as the most chemically plausible catalytic residue among the four choices, but confirming that this particular E64 (not, e.g., E81 or E234) is THE catalytic nucleophile requires protein-specific structural knowledge.",
    "reason": "The constrained multiple-choice format allows discrimination through general amino-acid chemistry: F and R are implausible proton acceptors, position 931 is out of range, and E is the only chemically sensible nucleophile among the options. This constitutes a concrete biological argument from the sequence and choices. However, the precise mechanistic role ('Nucleophile' vs. 'Proton acceptor') and the '(Probable)' qualifier are protein-specific annotations from the 2019 crystallography study, adding a lookup component for full confidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (position 931) is trivially impossible given the 373-residue sequence. Options A (F213 as proton acceptor) and D (R268 as proton acceptor) are chemically implausible for the stated roles. Only B (E64 as nucleophile) is chemically coherent. No other option is defensible."
  },
  "important_caveats": [
    "The active-site annotation carries the '(Probable)' qualifier and evidence code ECO:0000303 (inferred from assertion in database record), indicating structural inference rather than direct experimental proof of nucleophilic catalysis at E64.",
    "The binding-site annotation at position 64 for L-tryptophan is experimentally supported (ECO:0000269, PDB 6OS5/6OS6), but the specific assignment as 'Nucleophile' is a mechanistic interpretation from the crystallographic study.",
    "The sequence-to-accession mapping (A8M6W6) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the sequence alone.",
    "While the reasoning path through amino-acid chemistry is valid, the specific identification of E64 as THE catalytic nucleophile (vs. other acidic residues in the sequence) ultimately rests on protein-specific structural data from PubMed:31251043."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matching UniProt entry annotates position 64 as a probable nucleophile, citing a publication, and the archived record carries the same annotation. This supports the keyed choice, though the qualifier “probable” means it is not presented as definitive experimental proof.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable solver could recognize the sequence as consistent with an aromatic prenyltransferase family and use transferable family knowledge that a conserved catalytic residue can participate directly in prenylation. Position 64 is a tyrosine in this sequence, making the offered probable-nucleophile assignment plausible; position 931 is outside the 373-residue sequence. This is a family-based, probabilistic inference, not proof that this exact residue has the annotated role.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level sequence and catalytic-residue pattern offers a meaningful basis for preferring B among these choices without needing to recall this protein’s database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports position 64 as the probable nucleophile. No other offered option is comparably supported as the catalytic residue; position 931 is beyond the sequence length.


### Important caveats

- The active-site annotation is explicitly qualified as probable.
- The reviewer-only source supports applicability to the supplied sequence, but that source identity and annotation were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable solver could recognize the sequence as consistent with an aromatic prenyltransferase family and use transferable family knowledge that a conserved catalytic residue can participate directly in prenylation. Position 64 is a tyrosine in this sequence, making the offered probable-nucleophile assignment plausible; position 931 is outside the 373-residue sequence. This is a family-based, probabilistic inference, not proof that this exact residue has the annotated role.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level sequence and catalytic-residue pattern offers a meaningful basis for preferring B among these choices without needing to recall this protein’s database record."
  },
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The matching UniProt entry annotates position 64 as a probable nucleophile, citing a publication, and the archived record carries the same annotation. This supports the keyed choice, though the qualifier “probable” means it is not presented as definitive experimental proof."
  },
  "important_caveats": [
    "The active-site annotation is explicitly qualified as probable.",
    "The reviewer-only source supports applicability to the supplied sequence, but that source identity and annotation were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports position 64 as the probable nucleophile. No other offered option is comparably supported as the catalytic residue; position 931 is beyond the sequence length."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matching UniProt entry annotates position 64 as a probable nucleophile, citing a publication, and the archived record carries the same annotation. This supports the keyed choice, though the qualifier “probable” means it is not presented as definitive experimental proof.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable solver could recognize the sequence as consistent with an aromatic prenyltransferase family and use transferable family knowledge that a conserved catalytic residue can participate directly in prenylation. Position 64 is a tyrosine in this sequence, making the offered probable-nucleophile assignment plausible; position 931 is outside the 373-residue sequence. This is a family-based, probabilistic inference, not proof that this exact residue has the annotated role.",
    "missing_item_specific_fact": "",
    "reason": "The family-level sequence and catalytic-residue pattern offers a meaningful basis for preferring B among these choices without needing to recall this protein’s database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports position 64 as the probable nucleophile. No other offered option is comparably supported as the catalytic residue; position 931 is beyond the sequence length."
  },
  "important_caveats": [
    "The active-site annotation is explicitly qualified as probable.",
    "The reviewer-only source supports applicability to the supplied sequence, but that source identity and annotation were not part of the original model input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates position 64 (Glu) as 'Nucleophile (Probable)' active site (evidence ECO:0000303|PubMed:31251043, Roose & Christianson 2019, supported by X-ray crystallography PDB 6OS3/6OS5/6OS6). The sequence at position 64 is E (Glutamate), consistent with the annotation. The 'Probable' qualifier indicates structural inference rather than direct experimental proof of nucleophilic attack, but the annotation is well-supported by the primary literature.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C23](#evidence-c23), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent lines of reasoning from the original inputs and general biochemistry eliminate options A, C, and D: (1) The protein is 373 amino acids long, so position 931 (Option C) is physically impossible. (2) Position 213 is Phenylalanine (F), which has no ionizable side chain and cannot function as a proton acceptor. (3) Position 268 is Arginine (R), whose guanidinium group is positively charged and acts as a proton donor, not acceptor. Only position 64 is Glutamate (E), whose carboxylate side chain is a well-known nucleophile in enzyme catalysis. Additionally, glutamate residues are established catalytic participants in the DMATS (dimethylallyltryptophan synthase) prenyltransferase family, where they can attack DMAPP or activate the substrate nitrogen. The protein sequence itself reveals a prenyltransferase-like architecture (tryptophan-binding motifs, DMAPP-binding residues), supporting the family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate three of four options using the protein length (373 aa eliminates position 931), amino acid chemistry (Phe cannot accept a proton; Arg is a proton donor not acceptor), and the known catalytic role of glutamate in prenyltransferase families. The remaining option B (Glu64 as nucleophile) is the only chemically and structurally plausible choice without needing to recall this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option survives basic chemical and physical constraints: position 931 exceeds protein length, Phe cannot be a proton acceptor, and Arg is not a proton acceptor. Glu as a nucleophile is the sole chemically coherent answer.


### Important caveats

- The 'Probable' qualifier on the nucleophile annotation indicates structural inference from crystallography rather than direct experimental demonstration of covalent intermediate formation.
- The evidence code ECO:0000303 indicates the annotation derives from the primary literature (Roose & Christianson 2019) rather than direct mutagenesis or kinetics proving nucleophilic role.
- Position 213 (F) is near annotated L-tryptophan binding residues (211, 326) but is not itself the catalytic center.
- The protein length constraint (373 aa) making option C impossible is the strongest single discriminator available from the raw input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent lines of reasoning from the original inputs and general biochemistry eliminate options A, C, and D: (1) The protein is 373 amino acids long, so position 931 (Option C) is physically impossible. (2) Position 213 is Phenylalanine (F), which has no ionizable side chain and cannot function as a proton acceptor. (3) Position 268 is Arginine (R), whose guanidinium group is positively charged and acts as a proton donor, not acceptor. Only position 64 is Glutamate (E), whose carboxylate side chain is a well-known nucleophile in enzyme catalysis. Additionally, glutamate residues are established catalytic participants in the DMATS (dimethylallyltryptophan synthase) prenyltransferase family, where they can attack DMAPP or activate the substrate nitrogen. The protein sequence itself reveals a prenyltransferase-like architecture (tryptophan-binding motifs, DMAPP-binding residues), supporting the family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate three of four options using the protein length (373 aa eliminates position 931), amino acid chemistry (Phe cannot accept a proton; Arg is a proton donor not acceptor), and the known catalytic role of glutamate in prenyltransferase families. The remaining option B (Glu64 as nucleophile) is the only chemically and structurally plausible choice without needing to recall this specific protein's database annotation."
  },
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C23",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates position 64 (Glu) as 'Nucleophile (Probable)' active site (evidence ECO:0000303|PubMed:31251043, Roose & Christianson 2019, supported by X-ray crystallography PDB 6OS3/6OS5/6OS6). The sequence at position 64 is E (Glutamate), consistent with the annotation. The 'Probable' qualifier indicates structural inference rather than direct experimental proof of nucleophilic attack, but the annotation is well-supported by the primary literature."
  },
  "important_caveats": [
    "The 'Probable' qualifier on the nucleophile annotation indicates structural inference from crystallography rather than direct experimental demonstration of covalent intermediate formation.",
    "The evidence code ECO:0000303 indicates the annotation derives from the primary literature (Roose & Christianson 2019) rather than direct mutagenesis or kinetics proving nucleophilic role.",
    "Position 213 (F) is near annotated L-tryptophan binding residues (211, 326) but is not itself the catalytic center.",
    "The protein length constraint (373 aa) making option C impossible is the strongest single discriminator available from the raw input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option survives basic chemical and physical constraints: position 931 exceeds protein length, Phe cannot be a proton acceptor, and Arg is not a proton acceptor. Glu as a nucleophile is the sole chemically coherent answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates position 64 (Glu) as 'Nucleophile (Probable)' active site (evidence ECO:0000303|PubMed:31251043, Roose & Christianson 2019, supported by X-ray crystallography PDB 6OS3/6OS5/6OS6). The sequence at position 64 is E (Glutamate), consistent with the annotation. The 'Probable' qualifier indicates structural inference rather than direct experimental proof of nucleophilic attack, but the annotation is well-supported by the primary literature.",
    "evidence_ids": ["C5", "H6", "C23", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent lines of reasoning from the original inputs and general biochemistry eliminate options A, C, and D: (1) The protein is 373 amino acids long, so position 931 (Option C) is physically impossible. (2) Position 213 is Phenylalanine (F), which has no ionizable side chain and cannot function as a proton acceptor. (3) Position 268 is Arginine (R), whose guanidinium group is positively charged and acts as a proton donor, not acceptor. Only position 64 is Glutamate (E), whose carboxylate side chain is a well-known nucleophile in enzyme catalysis. Additionally, glutamate residues are established catalytic participants in the DMATS (dimethylallyltryptophan synthase) prenyltransferase family, where they can attack DMAPP or activate the substrate nitrogen. The protein sequence itself reveals a prenyltransferase-like architecture (tryptophan-binding motifs, DMAPP-binding residues), supporting the family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate three of four options using the protein length (373 aa eliminates position 931), amino acid chemistry (Phe cannot accept a proton; Arg is a proton donor not acceptor), and the known catalytic role of glutamate in prenyltransferase families. The remaining option B (Glu64 as nucleophile) is the only chemically and structurally plausible choice without needing to recall this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option survives basic chemical and physical constraints: position 931 exceeds protein length, Phe cannot be a proton acceptor, and Arg is not a proton acceptor. Glu as a nucleophile is the sole chemically coherent answer."
  },
  "important_caveats": [
    "The 'Probable' qualifier on the nucleophile annotation indicates structural inference from crystallography rather than direct experimental demonstration of covalent intermediate formation.",
    "The evidence code ECO:0000303 indicates the annotation derives from the primary literature (Roose & Christianson 2019) rather than direct mutagenesis or kinetics proving nucleophilic role.",
    "Position 213 (F) is near annotated L-tryptophan binding residues (211, 326) but is not itself the catalytic center.",
    "The protein length constraint (373 aa) making option C impossible is the strongest single discriminator available from the raw input."
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
  "requested_accession": "A8M6W6",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "c6494f8ce6bfbaecdb19e4e2579661bdd6cbc9b83eb2bcdd2c51a5dbc1b7af98",
  "benchmark_sequence_length": 373,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 69,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-12-04",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "current_source_sequence_sha256": "c6494f8ce6bfbaecdb19e4e2579661bdd6cbc9b83eb2bcdd2c51a5dbc1b7af98",
  "current_source_sequence_length": 373,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 67,
  "selected_historical_version": {
    "accession": "A8M6W6",
    "database": "Swiss-Prot",
    "entryVersion": 67,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CYMD_SALAI",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "selected_historical_source_sequence_sha256": "c6494f8ce6bfbaecdb19e4e2579661bdd6cbc9b83eb2bcdd2c51a5dbc1b7af98",
  "selected_historical_source_sequence_length": 373,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A8M6W6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":69,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-12-04\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Micromonosporales\",\"Micromonosporaceae\",\"Salinispora\"],\"scientificName\":\"Salinispora arenicola (strain CNS-205)\",\"taxonId\":391037}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20055491\",\"source\":\"PubMed\"}],\"value\":\"Cyclomarin/cyclomarazine N-prenyltransferase\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18331040\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20055491\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22935004\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"18331040\",\"source\":\"PubMed\"}],\"value\":\"Tryptophan N-prenyltransferase\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22935004\",\"source\":\"PubMed\"}],\"value\":\"Dimethylallyltryptophan synthase CymD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Nucleophile (Probable)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"31251043\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":64},\"start\":{\"modifier\":\"EXACT\",\"value\":64}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57912\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57912\",\"name\":\"L-tryptophan\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":55},\"start\":{\"modifier\":\"EXACT\",\"value\":55}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57912\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57912\",\"name\":\"L-tryptophan\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":56},\"start\":{\"modifier\":\"EXACT\",\"value\":56}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57912\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57912\",\"name\":\"L-tryptophan\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":64},\"start\":{\"modifier\":\"EXACT\",\"value\":64}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":77},\"start\":{\"modifier\":\"EXACT\",\"value\":77}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":146},\"start\":{\"modifier\":\"EXACT\",\"value\":146}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":148},\"start\":{\"modifier\":\"EXACT\",\"value\":148}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":205},\"start\":{\"modifier\":\"EXACT\",\"value\":205}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":207},\"start\":{\"modifier\":\"EXACT\",\"value\":207}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57912\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57912\",\"name\":\"L-tryptophan\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":211},\"start\":{\"modifier\":\"EXACT\",\"value\":211}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":274},\"start\":{\"modifier\":\"EXACT\",\"value\":274}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57912\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57912\",\"name\":\"L-tryptophan\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":326},\"start\":{\"modifier\":\"EXACT\",\"value\":326}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":337},\"start\":{\"modifier\":\"EXACT\",\"value\":337}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":339},\"start\":{\"modifier\":\"EXACT\",\"value\":339}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/features/18",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31251043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57623\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57623\",\"name\":\"dimethylallyl diphosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":341},\"start\":{\"modifier\":\"EXACT\",\"value\":341}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Schultz A.W.\",\"Oh D.C.\",\"Carney J.R.\",\"Williamson R.T.\",\"Udwary D.W.\",\"Jensen P.R.\",\"Gould S.J.\",\"Fenical W.\",\"Moore B.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18331040\"},{\"database\":\"DOI\",\"id\":\"10.1021/ja711188x\"}],\"citationType\":\"journal article\",\"firstPage\":\"4507\",\"id\":\"18331040\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"4516\",\"publicationDate\":\"2008\",\"title\":\"Biosynthesis and structures of cyclomarins and cyclomarazines, prenylated cyclic peptides of marine actinobacterial origin.\",\"volume\":\"130\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C21",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Schultz A.W.\",\"Lewis C.A.\",\"Luzung M.R.\",\"Baran P.S.\",\"Moore B.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20055491\"},{\"database\":\"DOI\",\"id\":\"10.1021/np9006876\"}],\"citationType\":\"journal article\",\"firstPage\":\"373\",\"id\":\"20055491\",\"journal\":\"J. Nat. Prod.\",\"lastPage\":\"377\",\"publicationDate\":\"2010\",\"title\":\"Functional characterization of the cyclomarin/cyclomarazine prenyltransferase CymD directs the biosynthesis of unnatural cyclic peptides.\",\"volume\":\"73\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C22",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Qian Q.\",\"Schultz A.W.\",\"Moore B.S.\",\"Tanner M.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22935004\"},{\"database\":\"DOI\",\"id\":\"10.1021/bi3009054\"}],\"citationType\":\"journal article\",\"firstPage\":\"7733\",\"id\":\"22935004\",\"journal\":\"Biochemistry\",\"lastPage\":\"7739\",\"publicationDate\":\"2012\",\"title\":\"Mechanistic studies on CymD: a tryptophan reverse N-prenyltransferase.\",\"volume\":\"51\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)

```json
{
  "evidence_id": "C23",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A8M6W6.json",
  "source_sha256": "430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6",
  "retrieved_utc": "2026-11-02T04:27:12.008171+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Roose B.W.\",\"Christianson D.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31251043\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.9b00399\"}],\"citationType\":\"journal article\",\"firstPage\":\"3232\",\"id\":\"31251043\",\"journal\":\"Biochemistry\",\"lastPage\":\"3242\",\"publicationDate\":\"2019\",\"title\":\"Structural Basis of Tryptophan Reverse N-Prenylation Catalyzed by CymD.\",\"volume\":\"58\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS3\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6OS6\",\"source\":\"PDB\"}],\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.33 ANGSTROMS) OF 2-373 IN APO FORM AND IN COMPLEXES WITH L-TRYPTOPHAN AND DIMETHYLALLYL S-THIOLODIPHOSPHATE\",\"FUNCTION\",\"ACTIVE SITE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   CYMD_SALAI              Reviewed;         373 AA.\nAC   A8M6W6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   04-DEC-2007, sequence version 1.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Dimethylallyltryptophan synthase CymD {ECO:0000303|PubMed:22935004};\nDE   AltName: Full=Cyclomarin/cyclomarazine N-prenyltransferase {ECO:0000303|PubMed:20055491};\nDE   AltName: Full=Tryptophan N-prenyltransferase {ECO:0000305|PubMed:18331040};\nDE            EC=2.5.1.- {ECO:0000269|PubMed:18331040, ECO:0000269|PubMed:20055491, ECO:0000269|PubMed:22935004};\nGN   Name=cymD {ECO:0000303|PubMed:18331040};\nGN   OrderedLocusNames=Sare_4565 {ECO:0000312|EMBL:ABW00334.1};\nOS   Salinispora arenicola (strain CNS-205).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micromonosporales;\nOC   Micromonosporaceae; Salinispora.\nOX   NCBI_TaxID=391037;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 26-33",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=18331040; DOI=10.1021/ja711188x;\nRA   Schultz A.W., Oh D.C., Carney J.R., Williamson R.T., Udwary D.W.,\nRA   Jensen P.R., Gould S.J., Fenical W., Moore B.S.;\nRT   \"Biosynthesis and structures of cyclomarins and cyclomarazines, prenylated\nRT   cyclic peptides of marine actinobacterial origin.\";\nRL   J. Am. Chem. Soc. 130:4507-4516(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 34-41",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=20055491; DOI=10.1021/np9006876;\nRA   Schultz A.W., Lewis C.A., Luzung M.R., Baran P.S., Moore B.S.;\nRT   \"Functional characterization of the cyclomarin/cyclomarazine\nRT   prenyltransferase CymD directs the biosynthesis of unnatural cyclic\nRT   peptides.\";\nRL   J. Nat. Prod. 73:373-377(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 42-47",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=22935004; DOI=10.1021/bi3009054;\nRA   Qian Q., Schultz A.W., Moore B.S., Tanner M.E.;\nRT   \"Mechanistic studies on CymD: a tryptophan reverse N-prenyltransferase.\";\nRL   Biochemistry 51:7733-7739(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 48-55",
  "excerpt": "RN   [5] {ECO:0007744|PDB:6OS3, ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6}\nRP   X-RAY CRYSTALLOGRAPHY (1.33 ANGSTROMS) OF 2-373 IN APO FORM AND IN\nRP   COMPLEXES WITH L-TRYPTOPHAN AND DIMETHYLALLYL S-THIOLODIPHOSPHATE,\nRP   FUNCTION, AND ACTIVE SITE.\nRX   PubMed=31251043; DOI=10.1021/acs.biochem.9b00399;\nRA   Roose B.W., Christianson D.W.;\nRT   \"Structural Basis of Tryptophan Reverse N-Prenylation Catalyzed by CymD.\";\nRL   Biochemistry 58:3232-3242(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 130-132",
  "excerpt": "FT   ACT_SITE        64\nFT                   /note=\"Nucleophile (Probable)\"\nFT                   /evidence=\"ECO:0000303|PubMed:31251043\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 133-137",
  "excerpt": "FT   BINDING         55\nFT                   /ligand=\"L-tryptophan\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57912\"\nFT                   /evidence=\"ECO:0000269|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 138-142",
  "excerpt": "FT   BINDING         56\nFT                   /ligand=\"L-tryptophan\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57912\"\nFT                   /evidence=\"ECO:0000269|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 143-147",
  "excerpt": "FT   BINDING         64\nFT                   /ligand=\"L-tryptophan\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57912\"\nFT                   /evidence=\"ECO:0000269|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 148-152",
  "excerpt": "FT   BINDING         77\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 153-157",
  "excerpt": "FT   BINDING         146\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 158-162",
  "excerpt": "FT   BINDING         148\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 163-167",
  "excerpt": "FT   BINDING         205\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 168-172",
  "excerpt": "FT   BINDING         207\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 173-177",
  "excerpt": "FT   BINDING         211\nFT                   /ligand=\"L-tryptophan\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57912\"\nFT                   /evidence=\"ECO:0000269|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 178-182",
  "excerpt": "FT   BINDING         274\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 183-187",
  "excerpt": "FT   BINDING         326\nFT                   /ligand=\"L-tryptophan\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57912\"\nFT                   /evidence=\"ECO:0000269|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 188-192",
  "excerpt": "FT   BINDING         337\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H19",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 193-197",
  "excerpt": "FT   BINDING         339\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)

```json
{
  "evidence_id": "H20",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67",
  "source_sha256": "eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6",
  "retrieved_utc": "2026-11-02T04:27:14.657088+00:00",
  "source_locator": "lines 198-202",
  "excerpt": "FT   BINDING         341\nFT                   /ligand=\"dimethylallyl diphosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57623\"\nFT                   /evidence=\"ECO:0000305|PubMed:31251043,\nFT                   ECO:0007744|PDB:6OS6\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
