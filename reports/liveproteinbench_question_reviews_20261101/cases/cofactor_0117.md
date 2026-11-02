# cofactor_0117

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTLWTVSPPAVSSEAEEKPVQDTVSLTAADQTWQVCVPLPIAALDFAAPHGYVGEVPLGCRVAVPWRGGEIRVGLVVGAGSSMGRHRLREALALLDSPEAPWVAPGTARGLTAWAEEAHLPPGLVWDDLLCTGWEPAHRHEVRAVPGADLSPYGETLPDTDWSRADLYPPALLDAAREQGLLDDRFLPDPPQVNRVVARDLNDVPPAARTQVVVTAQPWEAADPALCTPPHWEAVTGEGALTAKQQQAHDWLRAHGPQPSLGAWASGAKVGLPVVRKVADLGWAQEHPQAVPPPPAWKWLREHGPVASPAAWASAAGVRPAEVRRLMEGGAADYTFTPVTPPAAWAWLREHGPAETVSAWATGAGVSPSVAAGLLARGWAAQVQMPAPPPELPAAPLWAGPPLDELTALAADALPEEDRWRLHGGRPASRFAALAPRVARLLAQGRSVLILAPDHATLRRAWAGLGGLAALAGTRAALLSGQLSPRQREEIWRQVRAGDVRLVIGSALALSAPLPDLALLVVLEEGSDAYKLLSGSRAFVPDVAARVARSLRAALGLVGSVPAVESVPLPGLVLAPPRARVHVVDYAQPPAQPELGPLSSVHLTPGDLGYPISHDLARLLRQVQERGRQAALLAPRRGYSALLRCPRCDHVPGCPNCDVPLRFHQDRRQMECHQCGHHQSVPDRCDECGEQMWKARGPGTEWIAAEVEKLLPGFPVYRLDKDHQDDLAPLHAGEAGVVVGTQLLLAQPSPPNLALIGVTLADTWLGVSDFRASERYHRLLRQLAEWHPSRAPLLVVQTFQGDHPALKVLETGRDALAYPAAEERVRAELFYPPHARLAQIEVAARDRDRAKVAAQALADALHGAGAVATEVLGPAHAAVARVRGAYLYQLLLRARNDARLAELLGVLDTRSWGARVRVDVNPRST

[Multiple Choices]
A. NAD(+)
B. Zn(2+)
C. pantetheine 4'-phosphate
D. pyridoxal 5'-phosphate
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

> The sequence-matched UniProt record annotates Zn(2+) and says the protein binds two zinc ions per subunit. This is a HAMAP computational annotation, not experimental confirmation. A cited study describes this PriA as lacking helicase and ATPase activity, so the evidence supports zinc as an annotated cofactor but does not establish that it is required for catalytic activity.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conspicuous Cys/His-rich region near its C-terminus, consistent with a zinc-binding site. Among the choices, Zn(2+) is the biologically plausible match; the other options are not suggested by this motif.


**Missing item-specific fact**

> Whether zinc is experimentally bound or required for a catalytic activity is not established by the sequence motif alone.


**Reason**

> The motif provides meaningful grounds to distinguish zinc from the alternatives without needing to recognize the exact protein. It supports likely metal binding, though not the prompt's stronger claim about catalytic necessity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The zinc-binding motif makes Zn(2+) the distinct choice among those listed. However, describing this protein's cofactor as required for catalytic activity is potentially misleading given the cited lack of helicase and ATPase activity.


### Important caveats

- The database cofactor annotation is computational (HAMAP-rule evidence), not experimental evidence in the supplied excerpts.
- The sequence match is exact, but the annotation establishes a predicted zinc cofactor/binding assignment, not its necessity for catalysis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conspicuous Cys/His-rich region near its C-terminus, consistent with a zinc-binding site. Among the choices, Zn(2+) is the biologically plausible match; the other options are not suggested by this motif.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Whether zinc is experimentally bound or required for a catalytic activity is not established by the sequence motif alone.",
    "reason": "The motif provides meaningful grounds to distinguish zinc from the alternatives without needing to recognize the exact protein. It supports likely metal binding, though not the prompt's stronger claim about catalytic necessity."
  },
  "case_id": "cofactor_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Zn(2+) and says the protein binds two zinc ions per subunit. This is a HAMAP computational annotation, not experimental confirmation. A cited study describes this PriA as lacking helicase and ATPase activity, so the evidence supports zinc as an annotated cofactor but does not establish that it is required for catalytic activity."
  },
  "important_caveats": [
    "The database cofactor annotation is computational (HAMAP-rule evidence), not experimental evidence in the supplied excerpts.",
    "The sequence match is exact, but the annotation establishes a predicted zinc cofactor/binding assignment, not its necessity for catalysis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The zinc-binding motif makes Zn(2+) the distinct choice among those listed. However, describing this protein's cofactor as required for catalytic activity is potentially misleading given the cited lack of helicase and ATPase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Zn(2+) and says the protein binds two zinc ions per subunit. This is a HAMAP computational annotation, not experimental confirmation. A cited study describes this PriA as lacking helicase and ATPase activity, so the evidence supports zinc as an annotated cofactor but does not establish that it is required for catalytic activity.",
    "evidence_ids": ["C1", "C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conspicuous Cys/His-rich region near its C-terminus, consistent with a zinc-binding site. Among the choices, Zn(2+) is the biologically plausible match; the other options are not suggested by this motif.",
    "missing_item_specific_fact": "Whether zinc is experimentally bound or required for a catalytic activity is not established by the sequence motif alone.",
    "reason": "The motif provides meaningful grounds to distinguish zinc from the alternatives without needing to recognize the exact protein. It supports likely metal binding, though not the prompt's stronger claim about catalytic necessity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The zinc-binding motif makes Zn(2+) the distinct choice among those listed. However, describing this protein's cofactor as required for catalytic activity is potentially misleading given the cited lack of helicase and ATPase activity."
  },
  "important_caveats": [
    "The database cofactor annotation is computational (HAMAP-rule evidence), not experimental evidence in the supplied excerpts.",
    "The sequence match is exact, but the annotation establishes a predicted zinc cofactor/binding assignment, not its necessity for catalysis."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXX8 (sequence matched, 925 AA) for Deinococcus radiodurans PriA (Pseudohelicase PriA) explicitly annotates Zn(2+) as a cofactor: 'Binds 2 zinc ions per subunit.' The evidence code is ECO:0000255 (HAMAP-Rule:MF_00983), indicating a computational inference by rule-based similarity rather than direct experimental measurement. The sequence contains a prominent Cys-rich zinc-binding motif (CPRCDHVPGCPNCDVPLRFHQDRRQMECHQCGHHQSVPDRCDECGEQ) consistent with structural Zn(2+) coordination. Notably, the protein is characterized as a 'pseudohelicase' lacking helicase and ATPase activity (PubMed:26182205), so the Zn(2+) is structural rather than catalytic, but the database annotation still lists it as the cofactor.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an unmistakable Cys-rich zinc-binding domain (~residues 580-630): 'LRCPRCDHVPGCPNCDVPLRFHQDRRQMECHQCGHHQSVPDRCDECGEQ', featuring multiple C-x-C and C-x-x-C cysteine pairings characteristic of zinc coordination sites. In contrast, no canonical Rossmann-fold motif (GxGxxG in a β-α-β context) is present to support NAD+ binding; the 'GAGSSMGR' near the N-terminus is too short and lacks the surrounding structural context of a dehydrogenase fold. No PLP-binding lysine in the characteristic 'T-x-x-x-x-x-K-x-x-x-x-x-x-x-x-x' motif or the conserved catalytic residues of PLP-dependent enzymes are identifiable. No pantetheine-4'-phosphate binding site (e.g., the 'GxGxG' and acyl-CoA-binding motifs of phosphopantetheinyl transferases or acyltransferases) is present. A model could therefore eliminate A, C, and D by motif absence and select B by motif presence.


**Missing item-specific fact**

> None strictly required. The zinc-binding Cys-rich motif is visible in the supplied sequence. However, confirming that Zn(2+) is the *annotated cofactor* (as opposed to merely a structural metal) and that the protein is a PriA-family pseudohelicase does rely on database knowledge, though the motif-based reasoning is independently sufficient to favor B.


**Reason**

> The zinc-binding motif is a concrete, identifiable sequence feature that distinguishes B from the other options. The absence of NAD-binding, PLP-binding, and pantetheine-binding motifs provides additional discriminative grounds. While recognizing the protein as PriA would shortcut the analysis, the motif-level reasoning is available from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The zinc-binding Cys-rich motif is clearly present and no competing cofactor motif is identifiable. The 'GAGSSMGR' N-terminal fragment is too weak and contextually insufficient to support an NAD+ assignment. The pseudohelicase nature of the protein (lacking catalytic activity) introduces a philosophical wrinkle about whether any cofactor is 'required for catalytic activity,' but among the four choices Zn(2+) remains the only one with a supporting structural motif in the sequence.


### Important caveats

- The Zn(2+) annotation carries evidence code ECO:0000255 (HAMAP-Rule inference by similarity), not direct experimental validation for this specific protein.
- The protein is a 'Pseudohelicase PriA' shown to lack helicase and ATPase activity (PubMed:26182205), so the question's premise of 'cofactor required for catalytic activity' is somewhat inapposite; Zn(2+) here is structural.
- The accession P0DXX8 was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model had only the raw sequence and choices.
- The entry was first public 2025-04-09; the benchmark's author source snapshot is unknown, but sequence match is confirmed across available versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an unmistakable Cys-rich zinc-binding domain (~residues 580-630): 'LRCPRCDHVPGCPNCDVPLRFHQDRRQMECHQCGHHQSVPDRCDECGEQ', featuring multiple C-x-C and C-x-x-C cysteine pairings characteristic of zinc coordination sites. In contrast, no canonical Rossmann-fold motif (GxGxxG in a β-α-β context) is present to support NAD+ binding; the 'GAGSSMGR' near the N-terminus is too short and lacks the surrounding structural context of a dehydrogenase fold. No PLP-binding lysine in the characteristic 'T-x-x-x-x-x-K-x-x-x-x-x-x-x-x-x' motif or the conserved catalytic residues of PLP-dependent enzymes are identifiable. No pantetheine-4'-phosphate binding site (e.g., the 'GxGxG' and acyl-CoA-binding motifs of phosphopantetheinyl transferases or acyltransferases) is present. A model could therefore eliminate A, C, and D by motif absence and select B by motif presence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The zinc-binding Cys-rich motif is visible in the supplied sequence. However, confirming that Zn(2+) is the *annotated cofactor* (as opposed to merely a structural metal) and that the protein is a PriA-family pseudohelicase does rely on database knowledge, though the motif-based reasoning is independently sufficient to favor B.",
    "reason": "The zinc-binding motif is a concrete, identifiable sequence feature that distinguishes B from the other options. The absence of NAD-binding, PLP-binding, and pantetheine-binding motifs provides additional discriminative grounds. While recognizing the protein as PriA would shortcut the analysis, the motif-level reasoning is available from the sequence alone."
  },
  "case_id": "cofactor_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXX8 (sequence matched, 925 AA) for Deinococcus radiodurans PriA (Pseudohelicase PriA) explicitly annotates Zn(2+) as a cofactor: 'Binds 2 zinc ions per subunit.' The evidence code is ECO:0000255 (HAMAP-Rule:MF_00983), indicating a computational inference by rule-based similarity rather than direct experimental measurement. The sequence contains a prominent Cys-rich zinc-binding motif (CPRCDHVPGCPNCDVPLRFHQDRRQMECHQCGHHQSVPDRCDECGEQ) consistent with structural Zn(2+) coordination. Notably, the protein is characterized as a 'pseudohelicase' lacking helicase and ATPase activity (PubMed:26182205), so the Zn(2+) is structural rather than catalytic, but the database annotation still lists it as the cofactor."
  },
  "important_caveats": [
    "The Zn(2+) annotation carries evidence code ECO:0000255 (HAMAP-Rule inference by similarity), not direct experimental validation for this specific protein.",
    "The protein is a 'Pseudohelicase PriA' shown to lack helicase and ATPase activity (PubMed:26182205), so the question's premise of 'cofactor required for catalytic activity' is somewhat inapposite; Zn(2+) here is structural.",
    "The accession P0DXX8 was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model had only the raw sequence and choices.",
    "The entry was first public 2025-04-09; the benchmark's author source snapshot is unknown, but sequence match is confirmed across available versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The zinc-binding Cys-rich motif is clearly present and no competing cofactor motif is identifiable. The 'GAGSSMGR' N-terminal fragment is too weak and contextually insufficient to support an NAD+ assignment. The pseudohelicase nature of the protein (lacking catalytic activity) introduces a philosophical wrinkle about whether any cofactor is 'required for catalytic activity,' but among the four choices Zn(2+) remains the only one with a supporting structural motif in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXX8 (sequence matched, 925 AA) for Deinococcus radiodurans PriA (Pseudohelicase PriA) explicitly annotates Zn(2+) as a cofactor: 'Binds 2 zinc ions per subunit.' The evidence code is ECO:0000255 (HAMAP-Rule:MF_00983), indicating a computational inference by rule-based similarity rather than direct experimental measurement. The sequence contains a prominent Cys-rich zinc-binding motif (CPRCDHVPGCPNCDVPLRFHQDRRQMECHQCGHHQSVPDRCDECGEQ) consistent with structural Zn(2+) coordination. Notably, the protein is characterized as a 'pseudohelicase' lacking helicase and ATPase activity (PubMed:26182205), so the Zn(2+) is structural rather than catalytic, but the database annotation still lists it as the cofactor.",
    "evidence_ids": ["C5", "H4", "C4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an unmistakable Cys-rich zinc-binding domain (~residues 580-630): 'LRCPRCDHVPGCPNCDVPLRFHQDRRQMECHQCGHHQSVPDRCDECGEQ', featuring multiple C-x-C and C-x-x-C cysteine pairings characteristic of zinc coordination sites. In contrast, no canonical Rossmann-fold motif (GxGxxG in a β-α-β context) is present to support NAD+ binding; the 'GAGSSMGR' near the N-terminus is too short and lacks the surrounding structural context of a dehydrogenase fold. No PLP-binding lysine in the characteristic 'T-x-x-x-x-x-K-x-x-x-x-x-x-x-x-x' motif or the conserved catalytic residues of PLP-dependent enzymes are identifiable. No pantetheine-4'-phosphate binding site (e.g., the 'GxGxG' and acyl-CoA-binding motifs of phosphopantetheinyl transferases or acyltransferases) is present. A model could therefore eliminate A, C, and D by motif absence and select B by motif presence.",
    "missing_item_specific_fact": "None strictly required. The zinc-binding Cys-rich motif is visible in the supplied sequence. However, confirming that Zn(2+) is the *annotated cofactor* (as opposed to merely a structural metal) and that the protein is a PriA-family pseudohelicase does rely on database knowledge, though the motif-based reasoning is independently sufficient to favor B.",
    "reason": "The zinc-binding motif is a concrete, identifiable sequence feature that distinguishes B from the other options. The absence of NAD-binding, PLP-binding, and pantetheine-binding motifs provides additional discriminative grounds. While recognizing the protein as PriA would shortcut the analysis, the motif-level reasoning is available from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The zinc-binding Cys-rich motif is clearly present and no competing cofactor motif is identifiable. The 'GAGSSMGR' N-terminal fragment is too weak and contextually insufficient to support an NAD+ assignment. The pseudohelicase nature of the protein (lacking catalytic activity) introduces a philosophical wrinkle about whether any cofactor is 'required for catalytic activity,' but among the four choices Zn(2+) remains the only one with a supporting structural motif in the sequence."
  },
  "important_caveats": [
    "The Zn(2+) annotation carries evidence code ECO:0000255 (HAMAP-Rule inference by similarity), not direct experimental validation for this specific protein.",
    "The protein is a 'Pseudohelicase PriA' shown to lack helicase and ATPase activity (PubMed:26182205), so the question's premise of 'cofactor required for catalytic activity' is somewhat inapposite; Zn(2+) here is structural.",
    "The accession P0DXX8 was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model had only the raw sequence and choices.",
    "The entry was first public 2025-04-09; the benchmark's author source snapshot is unknown, but sequence match is confirmed across available versions."
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

**Accession:** `P0DXX8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:55.357414+00:00.  

```json
"P0DXX8"
```

Source SHA-256: `54601d21cb8c2a14ec396969dc99ba7390929578f335b0b71a8892d49744d93a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:55.357414+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26182205","source":"PubMed"}],"value":"Pseudohelicase PriA"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"}],"value":"Putative ATP-dependent DNA helicase PriA"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"}],"value":"Probable replication restart protein PriA"}}}
```

Source SHA-256: `54601d21cb8c2a14ec396969dc99ba7390929578f335b0b71a8892d49744d93a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:55.357414+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"}],"value":"Binds 2 zinc ions per subunit."}]}}
```

Source SHA-256: `54601d21cb8c2a14ec396969dc99ba7390929578f335b0b71a8892d49744d93a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:55.357414+00:00.  

```json
{"citation":{"authors":["Lopper M.E.","Boone J.","Morrow C."],"citationCrossReferences":[{"database":"PubMed","id":"26182205"},{"database":"DOI","id":"10.1371/journal.pone.0133419"}],"citationType":"journal article","firstPage":"e0133419","id":"26182205","journal":"PLoS ONE","lastPage":"e0133419","publicationDate":"2015","title":"Deinococcus radiodurans PriA is a Pseudohelicase.","volume":"10"},"referenceComments":[{"type":"STRAIN","value":"ATCC 13939 / DSM 20539 / JCM 16871 / CCUG 27074 / LMG 4051 / NBRC 15346 / NCIMB 9279 / VKM B-1422 / R1"}],"referenceNumber":2,"referencePositions":["LACK OF HELICASE AND ATPASE ACTIVITY","SUBUNIT","PROBABLE INTERACTION WITH DNAB","DNA-BINDING"]}
```

Source SHA-256: `54601d21cb8c2a14ec396969dc99ba7390929578f335b0b71a8892d49744d93a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXX8?format=txt&versions=3)  
**Locator:** `lines 30-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:57.642475+00:00.  

```text
RN   [2]
RP   LACK OF HELICASE AND ATPASE ACTIVITY, SUBUNIT, PROBABLE INTERACTION WITH
RP   DNAB, AND DNA-BINDING.
RC   STRAIN=ATCC 13939 / DSM 20539 / JCM 16871 / CCUG 27074 / LMG 4051 / NBRC
RC   15346 / NCIMB 9279 / VKM B-1422 / R1;
RX   PubMed=26182205; DOI=10.1371/journal.pone.0133419;
RA   Lopper M.E., Boone J., Morrow C.;
RT   "Deinococcus radiodurans PriA is a Pseudohelicase.";
RL   PLoS ONE 10:e0133419-e0133419(2015).
```

Source SHA-256: `b0a44577402ca1654934a50ecb162bfae04945493135af6018f9f913b5d1e29b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXX8?format=txt&versions=3)  
**Locator:** `lines 48-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:57.642475+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000255|HAMAP-Rule:MF_00983};
CC       Note=Binds 2 zinc ions per subunit. {ECO:0000255|HAMAP-Rule:MF_00983};
```

Source SHA-256: `b0a44577402ca1654934a50ecb162bfae04945493135af6018f9f913b5d1e29b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
