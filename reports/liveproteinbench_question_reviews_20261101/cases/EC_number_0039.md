# EC_number_0039

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 3.1.3.16

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFSGSSSPPKDKSNSVPHSGAVDTQSLSVHPEEGSAAQTSKSLPSGGFFTRRTSEDQAPAGEKKRRSSTVTKAATFFTNAKNSLSLSSSPRESSSFNYTVRSPQTLQSLGSMDPALSVPQGSLNNSAGDSLPTPRSSFKVGVTEDRNRKCRRTMEDTHAYLYNFLGTPAPLARADGENEAGSSLAPDEASSVVETDNGYFAIFDGHAGTFAAEWCGKKLHLILEDIMKKNPNTPVPELLDQTFTTVDQQLEKLPVKNSGCTAVIALLRWEDRIPSSHSATGSSALAPAAAAAAAAKGDSNSEADDTPTQATSSGPSILPKLQEKAIRQRVLYTANVGDARIILCRNGKALRLSYDHKGSDENEGKRIANAGGLILNNRVNGVLAVTRALGDAYLKDLVTGHPYTTETVVQPDSDEFIILACDGLWDVCTDQEAVDLVRNVPDAQEASKILVDYALARFSTDNLSCMVIRLDTNRVKEVINKTAEPIGVAGDPSMDVEHGVSEADKIIEGARKSMANADIADDGETAEKGKNDILHKMVDGEPGPEMSLDDSNDAPTVSHLNKTNANNGIP

[Multiple Choices]
A. 3.1.3.2
B. 2.1.1.27
C. 3.1.3.16
D. 4.1.1.129
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt entry annotated as protein phosphatase 2C homolog 1 with EC 3.1.3.16. The entry assigns that EC number to protein serine/threonine dephosphorylation and cites ECO:0000269 evidence linked to a PubMed paper; this supports the key, though the annotation is not itself an independent review of the experiment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conserved PP2C-like catalytic region, including characteristic metal-dependent phosphatase motifs, supporting a protein phosphatase rather than the methyltransferase or decarboxylase choices. The PP2C family assignment also distinguishes it from the acid-phosphatase choice and points to EC 3.1.3.16.


**Missing item-specific fact**

> No indispensable external, item-specific fact is needed to distinguish the choices; the PP2C-like sequence signature provides a defensible family-level inference.


**Reason**

> The options are separated by enzyme family and reaction class, and the catalytic-domain sequence provides meaningful evidence for the PP2C phosphatase option. This is more than recognition of a database entry, although the annotation and cited experimental evidence strengthen confirmation of the precise EC assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PP2C-like catalytic signature supports the protein-phosphatase option; the other listed choices describe distinct enzyme classes.


### Important caveats

- The reviewer-only UniProt evidence is not information supplied to the evaluated model.
- The cited evidence supports a database annotation, but the primary paper was not independently retrieved and comprehensively assessed here.
- The sequence match is exact; the author’s precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conserved PP2C-like catalytic region, including characteristic metal-dependent phosphatase motifs, supporting a protein phosphatase rather than the methyltransferase or decarboxylase choices. The PP2C family assignment also distinguishes it from the acid-phosphatase choice and points to EC 3.1.3.16.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No indispensable external, item-specific fact is needed to distinguish the choices; the PP2C-like sequence signature provides a defensible family-level inference.",
    "reason": "The options are separated by enzyme family and reaction class, and the catalytic-domain sequence provides meaningful evidence for the PP2C phosphatase option. This is more than recognition of a database entry, although the annotation and cited experimental evidence strengthen confirmation of the precise EC assignment."
  },
  "case_id": "EC_number_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as protein phosphatase 2C homolog 1 with EC 3.1.3.16. The entry assigns that EC number to protein serine/threonine dephosphorylation and cites ECO:0000269 evidence linked to a PubMed paper; this supports the key, though the annotation is not itself an independent review of the experiment."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence is not information supplied to the evaluated model.",
    "The cited evidence supports a database annotation, but the primary paper was not independently retrieved and comprehensively assessed here.",
    "The sequence match is exact; the author’s precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PP2C-like catalytic signature supports the protein-phosphatase option; the other listed choices describe distinct enzyme classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as protein phosphatase 2C homolog 1 with EC 3.1.3.16. The entry assigns that EC number to protein serine/threonine dephosphorylation and cites ECO:0000269 evidence linked to a PubMed paper; this supports the key, though the annotation is not itself an independent review of the experiment.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conserved PP2C-like catalytic region, including characteristic metal-dependent phosphatase motifs, supporting a protein phosphatase rather than the methyltransferase or decarboxylase choices. The PP2C family assignment also distinguishes it from the acid-phosphatase choice and points to EC 3.1.3.16.",
    "missing_item_specific_fact": "No indispensable external, item-specific fact is needed to distinguish the choices; the PP2C-like sequence signature provides a defensible family-level inference.",
    "reason": "The options are separated by enzyme family and reaction class, and the catalytic-domain sequence provides meaningful evidence for the PP2C phosphatase option. This is more than recognition of a database entry, although the annotation and cited experimental evidence strengthen confirmation of the precise EC assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PP2C-like catalytic signature supports the protein-phosphatase option; the other listed choices describe distinct enzyme classes."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence is not information supplied to the evaluated model.",
    "The cited evidence supports a database annotation, but the primary paper was not independently retrieved and comprehensively assessed here.",
    "The sequence match is exact; the author’s precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B8NLZ3 (PP2C1_ASPFN, Aspergillus flavus) is annotated with EC 3.1.3.16 supported by experimental evidence (ECO:0000269, PubMed:37754565). The catalytic activities documented are O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate and O-phospho-L-threonyl-&#91;protein&#93; + H2O = L-threonyl-&#91;protein&#93; + phosphate, both assigned EC 3.1.3.16. The sequence in the question matches the UniProt entry exactly (SHA256 confirmed). The annotation is backed by a 2023 MBio paper documenting functional characterization, catalytic activity, and mutagenesis of key aspartate residues (D204, D338, D422).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark PP2C-type phosphatase catalytic motif 'DGHAG' (residues ~190-194) along with additional conserved active-site aspartates ('DGLWDV' and 'DTNRV' regions), which together form the characteristic PP2C-domain active site architecture. PP2C-type phosphatases are universally classified under EC 3.1.3.16 (protein serine/threonine phosphatase). This distinguishes the protein from alkaline phosphatase (3.1.3.2), which uses a completely different fold with Zn²⁺/Mg²⁺-dependent catalysis and lacks the DxHAG motif. Options B (2.1.1.27, a methyltransferase) and D (4.1.1.129, a dioxygenase/lyase) belong to entirely different EC top-level classes (transferase, lyase) and are incompatible with a phosphatase domain.


**Missing item-specific fact**

> None critical. Recognition of the PP2C DxHAG signature and its universal association with EC 3.1.3.16 is established biochemical knowledge. Distinguishing PP2C from alkaline phosphatase requires knowing their distinct structural families, but this is general enzymology rather than a protein-specific lookup.


**Reason**

> A scientist familiar with phosphatase structural families can identify the PP2C domain from the DxHAG motif and conserved aspartate arrangement, then assign EC 3.1.3.16 by family-level knowledge. The other three options are eliminable by class-level reasoning (wrong EC top-level class or wrong phosphatase family). The reasoning path is concrete and does not require memorizing this particular protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (transferase) and D (lyase) are clearly incompatible with a phosphatase domain. Option A (3.1.3.2, alkaline phosphatase) is the only other phosphatase but belongs to a structurally and mechanistically distinct enzyme family lacking the PP2C DxHAG motif. No genuine ambiguity remains for a knowledgeable reader.


### Important caveats

- The PP2C motif recognition, while well-established biochemistry, still requires specific domain-family knowledge rather than purely first-principles reasoning from sequence composition alone.
- The UniProt annotation carries experimental evidence (ECO:0000269) from a 2023 publication, making the EC assignment robust rather than purely computational.
- The author source snapshot is unknown; however, the sequence has been unchanged since 2009 (sequence version 1), and the EC annotation has been present since the Swiss-Prot integration in Feb 2025.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark PP2C-type phosphatase catalytic motif 'DGHAG' (residues ~190-194) along with additional conserved active-site aspartates ('DGLWDV' and 'DTNRV' regions), which together form the characteristic PP2C-domain active site architecture. PP2C-type phosphatases are universally classified under EC 3.1.3.16 (protein serine/threonine phosphatase). This distinguishes the protein from alkaline phosphatase (3.1.3.2), which uses a completely different fold with Zn²⁺/Mg²⁺-dependent catalysis and lacks the DxHAG motif. Options B (2.1.1.27, a methyltransferase) and D (4.1.1.129, a dioxygenase/lyase) belong to entirely different EC top-level classes (transferase, lyase) and are incompatible with a phosphatase domain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of the PP2C DxHAG signature and its universal association with EC 3.1.3.16 is established biochemical knowledge. Distinguishing PP2C from alkaline phosphatase requires knowing their distinct structural families, but this is general enzymology rather than a protein-specific lookup.",
    "reason": "A scientist familiar with phosphatase structural families can identify the PP2C domain from the DxHAG motif and conserved aspartate arrangement, then assign EC 3.1.3.16 by family-level knowledge. The other three options are eliminable by class-level reasoning (wrong EC top-level class or wrong phosphatase family). The reasoning path is concrete and does not require memorizing this particular protein's database entry."
  },
  "case_id": "EC_number_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B8NLZ3 (PP2C1_ASPFN, Aspergillus flavus) is annotated with EC 3.1.3.16 supported by experimental evidence (ECO:0000269, PubMed:37754565). The catalytic activities documented are O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate and O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate, both assigned EC 3.1.3.16. The sequence in the question matches the UniProt entry exactly (SHA256 confirmed). The annotation is backed by a 2023 MBio paper documenting functional characterization, catalytic activity, and mutagenesis of key aspartate residues (D204, D338, D422)."
  },
  "important_caveats": [
    "The PP2C motif recognition, while well-established biochemistry, still requires specific domain-family knowledge rather than purely first-principles reasoning from sequence composition alone.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2023 publication, making the EC assignment robust rather than purely computational.",
    "The author source snapshot is unknown; however, the sequence has been unchanged since 2009 (sequence version 1), and the EC annotation has been present since the Swiss-Prot integration in Feb 2025."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (transferase) and D (lyase) are clearly incompatible with a phosphatase domain. Option A (3.1.3.2, alkaline phosphatase) is the only other phosphatase but belongs to a structurally and mechanistically distinct enzyme family lacking the PP2C DxHAG motif. No genuine ambiguity remains for a knowledgeable reader."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B8NLZ3 (PP2C1_ASPFN, Aspergillus flavus) is annotated with EC 3.1.3.16 supported by experimental evidence (ECO:0000269, PubMed:37754565). The catalytic activities documented are O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate and O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate, both assigned EC 3.1.3.16. The sequence in the question matches the UniProt entry exactly (SHA256 confirmed). The annotation is backed by a 2023 MBio paper documenting functional characterization, catalytic activity, and mutagenesis of key aspartate residues (D204, D338, D422).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark PP2C-type phosphatase catalytic motif 'DGHAG' (residues ~190-194) along with additional conserved active-site aspartates ('DGLWDV' and 'DTNRV' regions), which together form the characteristic PP2C-domain active site architecture. PP2C-type phosphatases are universally classified under EC 3.1.3.16 (protein serine/threonine phosphatase). This distinguishes the protein from alkaline phosphatase (3.1.3.2), which uses a completely different fold with Zn²⁺/Mg²⁺-dependent catalysis and lacks the DxHAG motif. Options B (2.1.1.27, a methyltransferase) and D (4.1.1.129, a dioxygenase/lyase) belong to entirely different EC top-level classes (transferase, lyase) and are incompatible with a phosphatase domain.",
    "missing_item_specific_fact": "None critical. Recognition of the PP2C DxHAG signature and its universal association with EC 3.1.3.16 is established biochemical knowledge. Distinguishing PP2C from alkaline phosphatase requires knowing their distinct structural families, but this is general enzymology rather than a protein-specific lookup.",
    "reason": "A scientist familiar with phosphatase structural families can identify the PP2C domain from the DxHAG motif and conserved aspartate arrangement, then assign EC 3.1.3.16 by family-level knowledge. The other three options are eliminable by class-level reasoning (wrong EC top-level class or wrong phosphatase family). The reasoning path is concrete and does not require memorizing this particular protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (transferase) and D (lyase) are clearly incompatible with a phosphatase domain. Option A (3.1.3.2, alkaline phosphatase) is the only other phosphatase but belongs to a structurally and mechanistically distinct enzyme family lacking the PP2C DxHAG motif. No genuine ambiguity remains for a knowledgeable reader."
  },
  "important_caveats": [
    "The PP2C motif recognition, while well-established biochemistry, still requires specific domain-family knowledge rather than purely first-principles reasoning from sequence composition alone.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2023 publication, making the EC assignment robust rather than purely computational.",
    "The author source snapshot is unknown; however, the sequence has been unchanged since 2009 (sequence version 1), and the EC annotation has been present since the Swiss-Prot integration in Feb 2025."
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

**Accession:** `B8NLZ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 90. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8NLZ3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:25.884972+00:00.  

```json
"B8NLZ3"
```

Source SHA-256: `a923d0b87775c86363af2f32117cbaa4b3b19dd82d48b975eb0997609aba449a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8NLZ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:25.884972+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"37754565","source":"PubMed"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37754565","source":"PubMed"}],"value":"Protein phosphatase 2C homolog 1"},"shortNames":[{"value":"PP2C-1"}]}}
```

Source SHA-256: `a923d0b87775c86363af2f32117cbaa4b3b19dd82d48b975eb0997609aba449a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8NLZ3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:25.884972+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"37754565","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000269","id":"37754565","source":"PubMed"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `a923d0b87775c86363af2f32117cbaa4b3b19dd82d48b975eb0997609aba449a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8NLZ3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:25.884972+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"37754565","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:47005"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"37754565","source":"PubMed"}],"name":"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:47004"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:61977"}]}}
```

Source SHA-256: `a923d0b87775c86363af2f32117cbaa4b3b19dd82d48b975eb0997609aba449a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8NLZ3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:25.884972+00:00.  

```json
{"citation":{"authors":["Zhu Z.","Yang M.","Yang G.","Zhang B.","Cao X.","Yuan J.","Ge F.","Wang S."],"citationCrossReferences":[{"database":"PubMed","id":"37754565"},{"database":"DOI","id":"10.1128/mbio.00977-23"}],"citationType":"journal article","firstPage":"e0097723","id":"37754565","journal":"MBio","lastPage":"e0097723","publicationDate":"2023","title":"PP2C phosphatases Ptc1 and Ptc2 dephosphorylate PGK1 to regulate autophagy and aflatoxin synthesis in the pathogenic fungus Aspergillus flavus.","volume":"14"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE","MUTAGENESIS OF ASP-204; ASP-338 AND ASP-422"]}
```

Source SHA-256: `a923d0b87775c86363af2f32117cbaa4b3b19dd82d48b975eb0997609aba449a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8NLZ3?format=txt&versions=90)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:27:29.637546+00:00.  

```text
DE   RecName: Full=Protein phosphatase 2C homolog 1 {ECO:0000303|PubMed:37754565};
DE            Short=PP2C-1;
DE            EC=3.1.3.16 {ECO:0000269|PubMed:37754565};
```

Source SHA-256: `bea04bbd31835e19259854f2e42627d0cb34cb3b47749e8af3e5d4aae56f53bb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8NLZ3?format=txt&versions=90)  
**Locator:** `lines 41-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:27:29.637546+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16;
CC         Evidence={ECO:0000269|PubMed:37754565};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000269|PubMed:37754565};
```

Source SHA-256: `bea04bbd31835e19259854f2e42627d0cb34cb3b47749e8af3e5d4aae56f53bb`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8NLZ3?format=txt&versions=90)  
**Locator:** `lines 49-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:27:29.637546+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:61977; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:37754565};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;
CC         Evidence={ECO:0000305|PubMed:37754565};
```

Source SHA-256: `bea04bbd31835e19259854f2e42627d0cb34cb3b47749e8af3e5d4aae56f53bb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 39. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
