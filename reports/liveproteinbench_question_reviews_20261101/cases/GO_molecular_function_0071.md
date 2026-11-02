# GO_molecular_function_0071

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — GTPase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRAGRVRPLRASDMKKDVRILLVGEPRVGKTSLIMSLVSEEFPEEVPPRAEEITIPADVTPERVPTHIVDYSEAEQSDEQLHQEISQANVICIVYAVNNKHSIDKVTSRWIPLINERTDKDSRLPLILVGNKSDLVEYSSMETILPIMNQYTEIETCVECSAKNLKNISELFYYAQKAVLHPTGPLYCPEEKEMKPACIKALTRIFKISDQDNDGTLNDAELNFFQRICFNTPLAPQALEDVKNVVRKHLSDGVADSGLTLRGFLFLHTLFIQRGRHETTWTVLRRFGYDDDLDLTPEYLFPLLKIPPDCTTELNHHAYLFLQSTFDKHDLDRDCALSPDELKDLFQVFPYIPWGPDVNNTVCTNESGWITYQGFLSQWTLTTYLDVQRCLEYLGYLGYSILTEQESQASAITVTRDKKIDLQKKQTQRNVFRCNVIGVKGCGKTGVLQSLLGRNLMRQKKIRDDHKSYYAINTVYVYGQEKYLLLHDISESEFLTEAEIVCDVVCLVYDVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLKSSTFWLRASFGATVFAVVGFAMYRALLKQR

[Multiple Choices]
A. DNA nuclease activity
B. transcription cis-regulatory region binding
C. GTPase activity
D. RNA methyltransferase activity
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

> The exact sequence matches the rat MIRO-1 entry, which annotates GTPase activity and describes GTP hydrolysis. The catalytic and GO annotations are inferred by similarity rather than presented here as direct experimental evidence for this sequence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C13](#evidence-c13), [H2](#evidence-h2), [H3](#evidence-h3), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains P-loop-like nucleotide-binding motifs, including a GxxxxGKT-like segment, supporting a nucleotide-triphosphatase function. Of the choices, GTPase activity is the fitting broad function; the other options describe DNA cleavage, regulatory DNA binding, or RNA methylation.


**Missing item-specific fact**

> The protein's specific family identity and direct catalytic characterization are not provided, but are not necessary to distinguish the broad GTPase option from these alternatives.


**Reason**

> The sequence offers a meaningful nucleotide-binding/hydrolysis clue, although motifs alone do not establish GTP specificity with certainty. The choice is supported by biological inference, not merely by recognizing a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed alternatives are functionally distinct, and the sequence motifs favor a nucleotide-triphosphatase/GTPase interpretation over the other choices.


### Important caveats

- The cited UniProt catalytic and GO annotations rely on similarity-based evidence; they are not direct experimental measurements for this exact protein.
- A P-loop motif supports nucleotide binding but, by itself, does not prove which nucleotide is hydrolyzed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains P-loop-like nucleotide-binding motifs, including a GxxxxGKT-like segment, supporting a nucleotide-triphosphatase function. Of the choices, GTPase activity is the fitting broad function; the other options describe DNA cleavage, regulatory DNA binding, or RNA methylation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The protein's specific family identity and direct catalytic characterization are not provided, but are not necessary to distinguish the broad GTPase option from these alternatives.",
    "reason": "The sequence offers a meaningful nucleotide-binding/hydrolysis clue, although motifs alone do not establish GTP specificity with certainty. The choice is supported by biological inference, not merely by recognizing a database entry."
  },
  "case_id": "GO_molecular_function_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C13",
      "H2",
      "H3",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the rat MIRO-1 entry, which annotates GTPase activity and describes GTP hydrolysis. The catalytic and GO annotations are inferred by similarity rather than presented here as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The cited UniProt catalytic and GO annotations rely on similarity-based evidence; they are not direct experimental measurements for this exact protein.",
    "A P-loop motif supports nucleotide binding but, by itself, does not prove which nucleotide is hydrolyzed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives are functionally distinct, and the sequence motifs favor a nucleotide-triphosphatase/GTPase interpretation over the other choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the rat MIRO-1 entry, which annotates GTPase activity and describes GTP hydrolysis. The catalytic and GO annotations are inferred by similarity rather than presented here as direct experimental evidence for this sequence.",
    "evidence_ids": ["C5", "C6", "C13", "H2", "H3", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains P-loop-like nucleotide-binding motifs, including a GxxxxGKT-like segment, supporting a nucleotide-triphosphatase function. Of the choices, GTPase activity is the fitting broad function; the other options describe DNA cleavage, regulatory DNA binding, or RNA methylation.",
    "missing_item_specific_fact": "The protein's specific family identity and direct catalytic characterization are not provided, but are not necessary to distinguish the broad GTPase option from these alternatives.",
    "reason": "The sequence offers a meaningful nucleotide-binding/hydrolysis clue, although motifs alone do not establish GTP specificity with certainty. The choice is supported by biological inference, not merely by recognizing a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives are functionally distinct, and the sequence motifs favor a nucleotide-triphosphatase/GTPase interpretation over the other choices."
  },
  "important_caveats": [
    "The cited UniProt catalytic and GO annotations rely on similarity-based evidence; they are not direct experimental measurements for this exact protein.",
    "A P-loop motif supports nucleotide binding but, by itself, does not prove which nucleotide is hydrolyzed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A1L1L6 (MIRO1_RAT, Mitochondrial Rho GTPase). The entry explicitly annotates GTPase activity (GO:0003924, ISS:UniProtKB), GTP binding (GO:0005525), GDP binding (GO:0019003), and catalytic activity GTP + H2O = GDP + phosphate + H(+). The recommended name is 'Mitochondrial Rho GTPase' with EC 3.6.5.-. None of the other three options (DNA nuclease, transcription cis-regulatory region binding, RNA methyltransferase) appear in the annotation. The evidence code is ISS (transferred from human Q8IXI2), so the rat-specific annotation is computational rather than directly experimental, but the protein family assignment is robust.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C12](#evidence-c12), [C13](#evidence-c13), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H9](#evidence-h9), [H10](#evidence-h10), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable Ras-superfamily GTPase signature motifs: a G1 P-loop (GKTSLIMSLV, ~residues 17-26), a G3 box (GNKSD, ~residues 128-132), a G4 box (CSAKN, ~residues 152-156), and a second GTPase domain with its own P-loop (VKGCGKT, ~residues 410-418). These conserved motifs (GXXXXGKS, NKxD, SAK) are textbook identifiers of small GTPases and are well-known in general biochemistry. Additionally, the presence of EF-hand-like calcium-binding regions between the two GTPase domains is characteristic of the MIRO/RHOT family. A model with standard protein-domain knowledge could identify the GTPase motifs and rule out DNA nuclease (no nuclease catalytic residues like DEDDh or HNH), transcription DNA-binding (no zinc finger, helix-turn-helix, or bZIP motifs), and RNA methyltransferase (no Rossmann-fold methyltransferase motifs or target recognition domain).


**Missing item-specific fact**

> None critical. The GTPase motifs are present in the supplied sequence and identifiable through general domain-knowledge. The exact protein identity (MIRO1_RAT) is not required; recognizing the Ras-superfamily GTPase fold from its conserved motifs is sufficient.


**Reason**

> The four choices span very different functional classes (nuclease, DNA-binding transcription factor, GTPase, methyltransferase). The sequence contains canonical GTPase P-loop and switch-region motifs that are part of standard protein-domain curricula. Distinguishing among the options does not require memorizing this particular protein's database entry; it requires recognizing well-known conserved sequence signatures of the Ras superfamily and the absence of motifs for the other three functional classes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mutually exclusive molecular function classes. The protein is annotated as a GTPase and shows no evidence of nuclease, sequence-specific DNA binding, or methyltransferase activity. No other option is defensible.


### Important caveats

- The GTPase GO annotation carries ISS evidence code (transferred from human MIRO1, Q8IXI2), not direct experimental validation on the rat protein. However, the protein family assignment is well-established and the sequence motifs are unambiguous.
- The protein also hydrolyzes ATP and UTP (C7, C8), but among the four choices only 'GTPase activity' is relevant; the question asks for the primary molecular function, and the protein is classified as a GTPase.
- The sequence is 631 aa and contains two GTPase domains flanked by EF-hand regions; a model focusing only on the C-terminal region might miss the N-terminal GTPase motifs, but the P-loop 'GKT' appears early enough to be detected.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable Ras-superfamily GTPase signature motifs: a G1 P-loop (GKTSLIMSLV, ~residues 17-26), a G3 box (GNKSD, ~residues 128-132), a G4 box (CSAKN, ~residues 152-156), and a second GTPase domain with its own P-loop (VKGCGKT, ~residues 410-418). These conserved motifs (GXXXXGKS, NKxD, SAK) are textbook identifiers of small GTPases and are well-known in general biochemistry. Additionally, the presence of EF-hand-like calcium-binding regions between the two GTPase domains is characteristic of the MIRO/RHOT family. A model with standard protein-domain knowledge could identify the GTPase motifs and rule out DNA nuclease (no nuclease catalytic residues like DEDDh or HNH), transcription DNA-binding (no zinc finger, helix-turn-helix, or bZIP motifs), and RNA methyltransferase (no Rossmann-fold methyltransferase motifs or target recognition domain).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The GTPase motifs are present in the supplied sequence and identifiable through general domain-knowledge. The exact protein identity (MIRO1_RAT) is not required; recognizing the Ras-superfamily GTPase fold from its conserved motifs is sufficient.",
    "reason": "The four choices span very different functional classes (nuclease, DNA-binding transcription factor, GTPase, methyltransferase). The sequence contains canonical GTPase P-loop and switch-region motifs that are part of standard protein-domain curricula. Distinguishing among the options does not require memorizing this particular protein's database entry; it requires recognizing well-known conserved sequence signatures of the Ras superfamily and the absence of motifs for the other three functional classes."
  },
  "case_id": "GO_molecular_function_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C12",
      "C13",
      "H1",
      "H2",
      "H3",
      "H9",
      "H10",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A1L1L6 (MIRO1_RAT, Mitochondrial Rho GTPase). The entry explicitly annotates GTPase activity (GO:0003924, ISS:UniProtKB), GTP binding (GO:0005525), GDP binding (GO:0019003), and catalytic activity GTP + H2O = GDP + phosphate + H(+). The recommended name is 'Mitochondrial Rho GTPase' with EC 3.6.5.-. None of the other three options (DNA nuclease, transcription cis-regulatory region binding, RNA methyltransferase) appear in the annotation. The evidence code is ISS (transferred from human Q8IXI2), so the rat-specific annotation is computational rather than directly experimental, but the protein family assignment is robust."
  },
  "important_caveats": [
    "The GTPase GO annotation carries ISS evidence code (transferred from human MIRO1, Q8IXI2), not direct experimental validation on the rat protein. However, the protein family assignment is well-established and the sequence motifs are unambiguous.",
    "The protein also hydrolyzes ATP and UTP (C7, C8), but among the four choices only 'GTPase activity' is relevant; the question asks for the primary molecular function, and the protein is classified as a GTPase.",
    "The sequence is 631 aa and contains two GTPase domains flanked by EF-hand regions; a model focusing only on the C-terminal region might miss the N-terminal GTPase motifs, but the P-loop 'GKT' appears early enough to be detected."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mutually exclusive molecular function classes. The protein is annotated as a GTPase and shows no evidence of nuclease, sequence-specific DNA binding, or methyltransferase activity. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A1L1L6 (MIRO1_RAT, Mitochondrial Rho GTPase). The entry explicitly annotates GTPase activity (GO:0003924, ISS:UniProtKB), GTP binding (GO:0005525), GDP binding (GO:0019003), and catalytic activity GTP + H2O = GDP + phosphate + H(+). The recommended name is 'Mitochondrial Rho GTPase' with EC 3.6.5.-. None of the other three options (DNA nuclease, transcription cis-regulatory region binding, RNA methyltransferase) appear in the annotation. The evidence code is ISS (transferred from human Q8IXI2), so the rat-specific annotation is computational rather than directly experimental, but the protein family assignment is robust.",
    "evidence_ids": ["C4", "C5", "C6", "C12", "C13", "H1", "H2", "H3", "H9", "H10", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable Ras-superfamily GTPase signature motifs: a G1 P-loop (GKTSLIMSLV, ~residues 17-26), a G3 box (GNKSD, ~residues 128-132), a G4 box (CSAKN, ~residues 152-156), and a second GTPase domain with its own P-loop (VKGCGKT, ~residues 410-418). These conserved motifs (GXXXXGKS, NKxD, SAK) are textbook identifiers of small GTPases and are well-known in general biochemistry. Additionally, the presence of EF-hand-like calcium-binding regions between the two GTPase domains is characteristic of the MIRO/RHOT family. A model with standard protein-domain knowledge could identify the GTPase motifs and rule out DNA nuclease (no nuclease catalytic residues like DEDDh or HNH), transcription DNA-binding (no zinc finger, helix-turn-helix, or bZIP motifs), and RNA methyltransferase (no Rossmann-fold methyltransferase motifs or target recognition domain).",
    "missing_item_specific_fact": "None critical. The GTPase motifs are present in the supplied sequence and identifiable through general domain-knowledge. The exact protein identity (MIRO1_RAT) is not required; recognizing the Ras-superfamily GTPase fold from its conserved motifs is sufficient.",
    "reason": "The four choices span very different functional classes (nuclease, DNA-binding transcription factor, GTPase, methyltransferase). The sequence contains canonical GTPase P-loop and switch-region motifs that are part of standard protein-domain curricula. Distinguishing among the options does not require memorizing this particular protein's database entry; it requires recognizing well-known conserved sequence signatures of the Ras superfamily and the absence of motifs for the other three functional classes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mutually exclusive molecular function classes. The protein is annotated as a GTPase and shows no evidence of nuclease, sequence-specific DNA binding, or methyltransferase activity. No other option is defensible."
  },
  "important_caveats": [
    "The GTPase GO annotation carries ISS evidence code (transferred from human MIRO1, Q8IXI2), not direct experimental validation on the rat protein. However, the protein family assignment is well-established and the sequence motifs are unambiguous.",
    "The protein also hydrolyzes ATP and UTP (C7, C8), but among the four choices only 'GTPase activity' is relevant; the question asks for the primary molecular function, and the protein is classified as a GTPase.",
    "The sequence is 631 aa and contains two GTPase domains flanked by EF-hand regions; a model focusing only on the C-terminal region might miss the N-terminal GTPase motifs, but the P-loop 'GKT' appears early enough to be detected."
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

**Accession:** `A1L1L6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 147. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"1307023","source":"RGD"}],"value":"Ras homolog gene family member T1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"value":"3.6.5.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"PIRNR037488","source":"PIRNR"}],"value":"Mitochondrial Rho GTPase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"MIRO-1"}]}}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"value":"Atypical mitochondrial nucleoside-triphosphatase (NTPase) involved in mitochondrial trafficking. Probably involved in control of anterograde transport of mitochondria and their subcellular distribution. Promotes mitochondrial fission during high calcium conditions. Can hydrolyze GTP, ATP and UTP"}]}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:19670"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"name":"GTP + H2O = GDP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19669"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:37565"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:58189"}]}}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13066"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"name":"ATP + H2O = ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13065"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:64901"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"name":"UTP + H2O = UDP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:64900"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:46398"},{"database":"ChEBI","id":"CHEBI:58223"}]}}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/uniProtKBCrossReferences/29`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"database":"GO","id":"GO:0005525","properties":[{"key":"GoTerm","value":"F:GTP binding"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/uniProtKBCrossReferences/30`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"database":"GO","id":"GO:0003924","properties":[{"key":"GoTerm","value":"F:GTPase activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:26:49.663865+00:00.  

```text
ID   MIRO1_RAT               Reviewed;         631 AA.
AC   A1L1L6;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   06-FEB-2007, sequence version 1.
DT   28-JAN-2026, entry version 147.
DE   RecName: Full=Mitochondrial Rho GTPase {ECO:0000255|PIRNR:PIRNR037488};
DE            Short=MIRO-1 {ECO:0000305};
DE            EC=3.6.5.- {ECO:0000250|UniProtKB:Q8IXI2};
DE   AltName: Full=Ras homolog gene family member T1 {ECO:0000312|RGD:1307023};
GN   Name=Rhot1 {ECO:0000312|RGD:1307023};
GN   Synonyms=Rnf135 {ECO:0000312|RGD:1307023};
OS   Rattus norvegicus (Rat).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Rattus.
OX   NCBI_TaxID=10116 {ECO:0000312|EMBL:AAI29124.1};
```

Source SHA-256: `f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)  
**Locator:** `lines 40-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:26:49.663865+00:00.  

```text
CC   -!- FUNCTION: Atypical mitochondrial nucleoside-triphosphatase (NTPase)
CC       involved in mitochondrial trafficking. Probably involved in control of
CC       anterograde transport of mitochondria and their subcellular
CC       distribution. Promotes mitochondrial fission during high calcium
CC       conditions. Can hydrolyze GTP, ATP and UTP.
CC       {ECO:0000250|UniProtKB:Q8IXI2}.
```

Source SHA-256: `f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)  
**Locator:** `lines 46-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:26:49.663865+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=GTP + H2O = GDP + phosphate + H(+); Xref=Rhea:RHEA:19669,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:37565,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:58189;
CC         Evidence={ECO:0000250|UniProtKB:Q8IXI2};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19670;
CC         Evidence={ECO:0000250|UniProtKB:Q8IXI2};
```

Source SHA-256: `f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)  
**Locator:** `lines 120-120`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:26:49.663865+00:00.  

```text
DR   GO; GO:0005525; F:GTP binding; ISS:UniProtKB.
```

Source SHA-256: `f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)  
**Locator:** `lines 121-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:26:49.663865+00:00.  

```text
DR   GO; GO:0003924; F:GTPase activity; ISS:UniProtKB.
```

Source SHA-256: `f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 31441-31534`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0003924
name: GTPase activity
namespace: molecular_function
alt_id: GO:0061745
def: "Catalysis of the reaction: GTP + H2O = GDP + H+ + phosphate." [PMID:26832457, PMID:27218782]
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_generic
subset: goslim_prokaryote
subset: goslim_yeast
synonym: "ARF small monomeric GTPase activity" NARROW []
synonym: "dynamin GTPase activity" NARROW []
synonym: "GTPase activity, coupled" RELATED []
synonym: "heterotrimeric G-protein GTPase activity" NARROW []
synonym: "heterotrimeric G-protein GTPase, alpha-subunit" RELATED []
synonym: "heterotrimeric G-protein GTPase, beta-subunit" RELATED []
synonym: "heterotrimeric G-protein GTPase, gamma-subunit" RELATED []
synonym: "hydrolase activity, acting on acid anhydrides, acting on GTP, involved in cellular and subcellular movement" BROAD []
synonym: "protein-synthesizing GTPase activity" NARROW []
synonym: "protein-synthesizing GTPase activity, elongation" NARROW []
synonym: "protein-synthesizing GTPase activity, initiation" NARROW []
synonym: "protein-synthesizing GTPase activity, termination" NARROW []
synonym: "Rab small monomeric GTPase activity" NARROW []
synonym: "Ran small monomeric GTPase activity" NARROW []
synonym: "Ras small monomeric GTPase activity" NARROW []
synonym: "RHEB small monomeric GTPase activity" NARROW []
synonym: "Rho small monomeric GTPase activity" NARROW []
synonym: "Sar small monomeric GTPase activity" NARROW []
synonym: "signal-recognition-particle GTPase activity" NARROW []
synonym: "small monomeric GTPase activity" NARROW []
synonym: "tubulin GTPase activity" NARROW []
xref: MetaCyc:RXN0-5462
xref: Reactome:R-HSA-1445143 "RAB8A,10,13,14 hydrolyze GTP"
xref: Reactome:R-HSA-1458485 "RALA hydrolyzes GTP"
xref: Reactome:R-HSA-156923 "Hydrolysis of eEF1A:GTP"
xref: Reactome:R-HSA-164381 "G alpha (s) auto-inactivates by hydrolysing GTP to GDP"
xref: Reactome:R-HSA-165055 "Hydrolysis of Ran:GTP to Ran:GDP"
xref: Reactome:R-HSA-167415 "G-protein alpha subunit is inactivated"
xref: Reactome:R-HSA-170666 "Adenylate cyclase increases the GTPase activity of G alpha-olf"
xref: Reactome:R-HSA-170685 "Adenylaye cyclase increases the GTPase activity of G alpha-olf"
xref: Reactome:R-HSA-170686 "Adenylate cyclase increases the GTPase activity of Gi alpha"
xref: Reactome:R-HSA-177501 "Endocytosis (internalization) of clathrin-coated vesicle"
xref: Reactome:R-HSA-203973 "Vesicle budding"
xref: Reactome:R-HSA-2130641 "Translocation of TGN-lysosome vesicle to lysosome"
xref: Reactome:R-HSA-2130725 "Internalization of MHC II:Ii clathrin coated vesicle"
xref: Reactome:R-HSA-2584246 "GNAT1-GTP hydrolyses its bound GTP to GDP"
xref: Reactome:R-HSA-380979 "RHEB in mTORC1:RHEB:GTP hydrolyses GTP"
xref: Reactome:R-HSA-392133 "G alpha (z) auto-inactivates by hydrolysing GTP to GDP"
xref: Reactome:R-HSA-392212 "G alpha (i) auto-inactivates by hydrolysing GTP to GDP"
xref: Reactome:R-HSA-418574 "G alpha (12/13) auto-inactivates by hydrolysing GTP to GDP"
xref: Reactome:R-HSA-418582 "G alpha (q) auto-inactivates by hydrolysing GTP to GDP"
xref: Reactome:R-HSA-421835 "trans-Golgi Network Vesicle Scission"
xref: Reactome:R-HSA-428941 "P2Y purinoceptor 1 activates MAP kinase p38 alpha"
xref: Reactome:R-HSA-432707 "trans-Golgi Network Lysosomal Vesicle Scission"
xref: Reactome:R-HSA-5333615 "80S:Met-tRNAi:mRNA:SECISBP2:Sec-tRNA(Sec):EEFSEC:GTP is hydrolysed to 80S:Met-tRNAi:mRNA:SECISBP2:Sec and EEFSEC:GDP by EEFSEC"
xref: Reactome:R-HSA-5389839 "39S subunit binds 28S subunit:mRNA:fMet-tRNA"
xref: Reactome:R-HSA-5389842 "TUFM hydrolyzes GTP and TUFM:GDP dissociates from 55S ribosome"
xref: Reactome:R-HSA-5419273 "Hydrolysis of GTP and dissociation of 28S and 39S subunits"
xref: Reactome:R-HSA-5419279 "Translocation of peptidyl-tRNA from A-site to P-site (and translocation of 55S ribosome by 3 bases along mRNA)"
xref: Reactome:R-HSA-555065 "Formation of clathrin coated vesicle"
xref: Reactome:R-HSA-5623513 "ASAP1 stimulates GTPase activity of ARF4"
xref: Reactome:R-HSA-5638006 "ARL3 hydrolyzes GTP"
xref: Reactome:R-HSA-5658231 "RAS GAPs stimulate RAS GTPase activity"
xref: Reactome:R-HSA-5665809 "SRGAP2 stimulates RAC1 GTP-ase activity and ends FMNL1-mediated elongation of actin filaments"
xref: Reactome:R-HSA-5672017 "Rheb in the MTORC1 complex hydrolyses GTP"
xref: Reactome:R-HSA-5694527 "Loss of SAR1B GTPase"
xref: Reactome:R-HSA-6807877 "ARFGAPs stimulate ARF GTPase activity"
xref: Reactome:R-HSA-6814833 "TBC1D20 stimulates GTPase activity of RAB1, resulting in hydrolysis of GTP"
xref: Reactome:R-HSA-8847534 "RAB43 hydrolyses GTP"
xref: Reactome:R-HSA-8847883 "CYTH proteins stimulate ARF1 GTPase activity"
xref: Reactome:R-HSA-8849082 "ARHGAP35 stimulates RHOA GTPase activity"
xref: Reactome:R-HSA-8854173 "TBC RabGAPs accelerate GTP hydrolysis by RAB35"
xref: Reactome:R-HSA-8854255 "TBC1D2A accelerates GTP hydrolysis by RAB7"
xref: Reactome:R-HSA-8854329 "TBC1D15 accelerates GTP hydrolysis by RAB7"
xref: Reactome:R-HSA-8854604 "TBC1D16 accelerates GTP hydrolysis by RAB4A"
xref: Reactome:R-HSA-8854612 "TBC1D25 accelerates GTP hydrolysis by RAB33B"
xref: Reactome:R-HSA-8868661 "Dynamin-mediated GTP hydrolysis promotes vesicle scission"
xref: Reactome:R-HSA-8981353 "RASA1 stimulates RAS GTPase activity"
xref: Reactome:R-HSA-8982020 "G alpha (i)i1/i2/i3 in G (i):RGS complex is inactivated"
xref: Reactome:R-HSA-8982021 "G alpha (z) in G alpha (z):RGS complex is inactivated"
xref: Reactome:R-HSA-8982025 "G alpha (q) in G (q):RGS complex is inactivated"
xref: Reactome:R-HSA-9018814 "RHOT1 hydrolyzes GTP"
xref: Reactome:R-HSA-9018826 "RHOT2 hydrolyzes GTP"
xref: Reactome:R-HSA-9640195 "RRAGA,B hydrolyzes GTP"
xref: Reactome:R-HSA-9645598 "RRAGC,D hydrolyzes GTP"
xref: Reactome:R-HSA-9649736 "RAS intrinsic GTPase activity hydrolyzes GTP to GDP"
xref: Reactome:R-HSA-983422 "Disassembly of COPII coated vesicle"
xref: Reactome:R-HSA-9947842 "GBP1 hydrolyzes GTP forming GBP1 oligomers"
xref: Reactome:R-HSA-9954919 "ABCE1:ATP binds PELO:HBS1L-1:GTP:80S ribosome:non-stop mRNA:peptidyl-tRNA with nascent peptide and HBS1L-1:GDP is released"
xref: RHEA:19669
is_a: GO:0017111 ! ribonucleoside triphosphate phosphatase activity
property_value: skos:exactMatch RHEA:19669

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 71. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
