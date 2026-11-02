# cofactor_0077

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Mg(2+)

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
A. pantetheine 4'-phosphate
B. Co(2+)
C. pyridoxal 5'-phosphate
D. Mg(2+)
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

> The sequence matches a UniProt entry annotated as a PP2C phosphatase with Mg(2+) as a cofactor, citing experimental evidence. The annotation says the enzyme has highest activity with magnesium, while also noting manganese binding and calcium activity; thus Mg(2+) supports the key among the listed options.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a PP2C-like catalytic domain with conserved acidic residues associated with metal-dependent phosphatase catalysis. General knowledge of PP2C phosphatases supports a divalent metal cofactor, particularly Mg(2+), distinguishing it from pantetheine phosphate, PLP, and Co(2+) among these choices.


**Missing item-specific fact**

> The exact experimental comparison of magnesium with other active ions is not supplied; it is not needed to distinguish Mg(2+) from the listed alternatives by the family-level argument.


**Reason**

> The sequence provides a defensible route to recognizing a metal-dependent PP2C phosphatase and selecting magnesium from these choices. The reviewer-only annotation supports the key but is not being treated as input available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Mg(2+) is the only listed option supported by the family-level inference. The wording's singular 'required' simplifies the annotation, which also reports manganese binding and calcium activity, but neither appears among the choices.


### Important caveats

- The reviewer evidence is a UniProt annotation citing a publication; the underlying experimental results were not independently examined here.
- The annotation reports highest activity with magnesium, not exclusive activity with magnesium.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a PP2C-like catalytic domain with conserved acidic residues associated with metal-dependent phosphatase catalysis. General knowledge of PP2C phosphatases supports a divalent metal cofactor, particularly Mg(2+), distinguishing it from pantetheine phosphate, PLP, and Co(2+) among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact experimental comparison of magnesium with other active ions is not supplied; it is not needed to distinguish Mg(2+) from the listed alternatives by the family-level argument.",
    "reason": "The sequence provides a defensible route to recognizing a metal-dependent PP2C phosphatase and selecting magnesium from these choices. The reviewer-only annotation supports the key but is not being treated as input available to the evaluated model."
  },
  "case_id": "cofactor_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches a UniProt entry annotated as a PP2C phosphatase with Mg(2+) as a cofactor, citing experimental evidence. The annotation says the enzyme has highest activity with magnesium, while also noting manganese binding and calcium activity; thus Mg(2+) supports the key among the listed options."
  },
  "important_caveats": [
    "The reviewer evidence is a UniProt annotation citing a publication; the underlying experimental results were not independently examined here.",
    "The annotation reports highest activity with magnesium, not exclusive activity with magnesium."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Mg(2+) is the only listed option supported by the family-level inference. The wording's singular 'required' simplifies the annotation, which also reports manganese binding and calcium activity, but neither appears among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches a UniProt entry annotated as a PP2C phosphatase with Mg(2+) as a cofactor, citing experimental evidence. The annotation says the enzyme has highest activity with magnesium, while also noting manganese binding and calcium activity; thus Mg(2+) supports the key among the listed options.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a PP2C-like catalytic domain with conserved acidic residues associated with metal-dependent phosphatase catalysis. General knowledge of PP2C phosphatases supports a divalent metal cofactor, particularly Mg(2+), distinguishing it from pantetheine phosphate, PLP, and Co(2+) among these choices.",
    "missing_item_specific_fact": "The exact experimental comparison of magnesium with other active ions is not supplied; it is not needed to distinguish Mg(2+) from the listed alternatives by the family-level argument.",
    "reason": "The sequence provides a defensible route to recognizing a metal-dependent PP2C phosphatase and selecting magnesium from these choices. The reviewer-only annotation supports the key but is not being treated as input available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Mg(2+) is the only listed option supported by the family-level inference. The wording's singular 'required' simplifies the annotation, which also reports manganese binding and calcium activity, but neither appears among the choices."
  },
  "important_caveats": [
    "The reviewer evidence is a UniProt annotation citing a publication; the underlying experimental results were not independently examined here.",
    "The annotation reports highest activity with magnesium, not exclusive activity with magnesium."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B8NLZ3 (PP2C-1, EC 3.1.3.16, Aspergillus flavus) annotates Mg(2+) as a cofactor with experimental evidence (ECO:0000269|PubMed:37754565). The COFACTOR note states the protein 'binds 2 magnesium or manganese ions per subunit' and 'has highest activity with magnesium.' Mn(2+) is also listed but is not among the answer choices, so Mg(2+) is unambiguously the correct answer among the four options. The PP2C superfamily's Mg(2+) dependence is a well-established biochemical property.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable PP2C-domain motifs (e.g., the conserved 'DGLWDV' and 'DPSMDVEHG' stretches with strategically placed acidic residues characteristic of the PP2C metal-binding site). PP2C-type serine/threonine phosphatases are universally and definitionally Mg(2+)-dependent enzymes; this is a general, textbook-level biochemical property of the superfamily, not a protein-specific fact. The other options can be eliminated by general knowledge: pantetheine 4'-phosphate is associated with CoA-dependent acyltransferases; Co(2+) is a cofactor for specific radical SAM or B12-dependent enzymes; pyridoxal 5'-phosphate (PLP) is the hallmark cofactor of transaminases and decarboxylases. None of these are associated with phosphatase chemistry. Thus, identifying the enzyme class from sequence motifs and applying the general cofactor requirement of that class suffices.


**Missing item-specific fact**

> None required. The Mg(2+) dependence is a defining, general property of the PP2C phosphatase superfamily, not an item-specific experimental measurement.


**Reason**

> A knowledgeable model can (a) recognize PP2C-like sequence features from conserved acidic-residue motifs, (b) recall that PP2C phosphatases are Mg(2+)-dependent as a class-wide biochemical fact, and (c) eliminate the other three cofactors because they belong to entirely different enzyme classes. This constitutes a concrete biological reasoning chain, not reliance on a single protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry lists both Mg(2+) and Mn(2+) as cofactors, Mn(2+) does not appear among the four choices. The annotation further specifies 'highest activity with magnesium.' Among A–D, only Mg(2+) is a recognized PP2C cofactor; the other three are associated with unrelated enzyme classes. No ambiguity exists.


### Important caveats

- The UniProt annotation lists Mn(2+) as an alternative cofactor; had Mn(2+) been an option, the question would need the 'highest activity with magnesium' qualifier to be unambiguous.
- The sequence itself does not carry an explicit label identifying it as PP2C; recognition relies on the model's familiarity with PP2C domain motifs and the general biochemistry of the superfamily.
- The experimental evidence (PubMed:37754565, 2023) post-dates the original sequence deposition (2009), but the PP2C Mg(2+) dependence is a long-standing, class-level fact independent of this specific paper.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable PP2C-domain motifs (e.g., the conserved 'DGLWDV' and 'DPSMDVEHG' stretches with strategically placed acidic residues characteristic of the PP2C metal-binding site). PP2C-type serine/threonine phosphatases are universally and definitionally Mg(2+)-dependent enzymes; this is a general, textbook-level biochemical property of the superfamily, not a protein-specific fact. The other options can be eliminated by general knowledge: pantetheine 4'-phosphate is associated with CoA-dependent acyltransferases; Co(2+) is a cofactor for specific radical SAM or B12-dependent enzymes; pyridoxal 5'-phosphate (PLP) is the hallmark cofactor of transaminases and decarboxylases. None of these are associated with phosphatase chemistry. Thus, identifying the enzyme class from sequence motifs and applying the general cofactor requirement of that class suffices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The Mg(2+) dependence is a defining, general property of the PP2C phosphatase superfamily, not an item-specific experimental measurement.",
    "reason": "A knowledgeable model can (a) recognize PP2C-like sequence features from conserved acidic-residue motifs, (b) recall that PP2C phosphatases are Mg(2+)-dependent as a class-wide biochemical fact, and (c) eliminate the other three cofactors because they belong to entirely different enzyme classes. This constitutes a concrete biological reasoning chain, not reliance on a single protein's database annotation."
  },
  "case_id": "cofactor_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B8NLZ3 (PP2C-1, EC 3.1.3.16, Aspergillus flavus) annotates Mg(2+) as a cofactor with experimental evidence (ECO:0000269|PubMed:37754565). The COFACTOR note states the protein 'binds 2 magnesium or manganese ions per subunit' and 'has highest activity with magnesium.' Mn(2+) is also listed but is not among the answer choices, so Mg(2+) is unambiguously the correct answer among the four options. The PP2C superfamily's Mg(2+) dependence is a well-established biochemical property."
  },
  "important_caveats": [
    "The UniProt annotation lists Mn(2+) as an alternative cofactor; had Mn(2+) been an option, the question would need the 'highest activity with magnesium' qualifier to be unambiguous.",
    "The sequence itself does not carry an explicit label identifying it as PP2C; recognition relies on the model's familiarity with PP2C domain motifs and the general biochemistry of the superfamily.",
    "The experimental evidence (PubMed:37754565, 2023) post-dates the original sequence deposition (2009), but the PP2C Mg(2+) dependence is a long-standing, class-level fact independent of this specific paper."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry lists both Mg(2+) and Mn(2+) as cofactors, Mn(2+) does not appear among the four choices. The annotation further specifies 'highest activity with magnesium.' Among A–D, only Mg(2+) is a recognized PP2C cofactor; the other three are associated with unrelated enzyme classes. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B8NLZ3 (PP2C-1, EC 3.1.3.16, Aspergillus flavus) annotates Mg(2+) as a cofactor with experimental evidence (ECO:0000269|PubMed:37754565). The COFACTOR note states the protein 'binds 2 magnesium or manganese ions per subunit' and 'has highest activity with magnesium.' Mn(2+) is also listed but is not among the answer choices, so Mg(2+) is unambiguously the correct answer among the four options. The PP2C superfamily's Mg(2+) dependence is a well-established biochemical property.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable PP2C-domain motifs (e.g., the conserved 'DGLWDV' and 'DPSMDVEHG' stretches with strategically placed acidic residues characteristic of the PP2C metal-binding site). PP2C-type serine/threonine phosphatases are universally and definitionally Mg(2+)-dependent enzymes; this is a general, textbook-level biochemical property of the superfamily, not a protein-specific fact. The other options can be eliminated by general knowledge: pantetheine 4'-phosphate is associated with CoA-dependent acyltransferases; Co(2+) is a cofactor for specific radical SAM or B12-dependent enzymes; pyridoxal 5'-phosphate (PLP) is the hallmark cofactor of transaminases and decarboxylases. None of these are associated with phosphatase chemistry. Thus, identifying the enzyme class from sequence motifs and applying the general cofactor requirement of that class suffices.",
    "missing_item_specific_fact": "None required. The Mg(2+) dependence is a defining, general property of the PP2C phosphatase superfamily, not an item-specific experimental measurement.",
    "reason": "A knowledgeable model can (a) recognize PP2C-like sequence features from conserved acidic-residue motifs, (b) recall that PP2C phosphatases are Mg(2+)-dependent as a class-wide biochemical fact, and (c) eliminate the other three cofactors because they belong to entirely different enzyme classes. This constitutes a concrete biological reasoning chain, not reliance on a single protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry lists both Mg(2+) and Mn(2+) as cofactors, Mn(2+) does not appear among the four choices. The annotation further specifies 'highest activity with magnesium.' Among A–D, only Mg(2+) is a recognized PP2C cofactor; the other three are associated with unrelated enzyme classes. No ambiguity exists."
  },
  "important_caveats": [
    "The UniProt annotation lists Mn(2+) as an alternative cofactor; had Mn(2+) been an option, the question would need the 'highest activity with magnesium' qualifier to be unambiguous.",
    "The sequence itself does not carry an explicit label identifying it as PP2C; recognition relies on the model's familiarity with PP2C domain motifs and the general biochemistry of the superfamily.",
    "The experimental evidence (PubMed:37754565, 2023) post-dates the original sequence deposition (2009), but the PP2C Mg(2+) dependence is a long-standing, class-level fact independent of this specific paper."
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
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:25.884972+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000269","id":"37754565","source":"PubMed"}],"name":"Mg(2+)"},{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29035"},"evidences":[{"evidenceCode":"ECO:0000269","id":"37754565","source":"PubMed"}],"name":"Mn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01082","source":"PROSITE-ProRule"},{"evidenceCode":"ECO:0000269","id":"37754565","source":"PubMed"}],"value":"Binds 2 magnesium or manganese ions per subunit (By similarity). Has highest activity with magnesium, but also has activity with calcium (PubMed:37754565)."}]}}
```

Source SHA-256: `a923d0b87775c86363af2f32117cbaa4b3b19dd82d48b975eb0997609aba449a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8NLZ3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:25.884972+00:00.  

```json
{"citation":{"authors":["Zhu Z.","Yang M.","Yang G.","Zhang B.","Cao X.","Yuan J.","Ge F.","Wang S."],"citationCrossReferences":[{"database":"PubMed","id":"37754565"},{"database":"DOI","id":"10.1128/mbio.00977-23"}],"citationType":"journal article","firstPage":"e0097723","id":"37754565","journal":"MBio","lastPage":"e0097723","publicationDate":"2023","title":"PP2C phosphatases Ptc1 and Ptc2 dephosphorylate PGK1 to regulate autophagy and aflatoxin synthesis in the pathogenic fungus Aspergillus flavus.","volume":"14"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE","MUTAGENESIS OF ASP-204; ASP-338 AND ASP-422"]}
```

Source SHA-256: `a923d0b87775c86363af2f32117cbaa4b3b19dd82d48b975eb0997609aba449a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8NLZ3?format=txt&versions=90)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:27:29.637546+00:00.  

```text
ID   PP2C1_ASPFN             Reviewed;         570 AA.
AC   B8NLZ3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAR-2009, sequence version 1.
DT   28-JAN-2026, entry version 90.
DE   RecName: Full=Protein phosphatase 2C homolog 1 {ECO:0000303|PubMed:37754565};
DE            Short=PP2C-1;
DE            EC=3.1.3.16 {ECO:0000269|PubMed:37754565};
GN   Name=ptc1 {ECO:0000303|PubMed:37754565};
GN   ORFNames=F9C07_9134 {ECO:0000312|EMBL:QRD84879.1};
OS   Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357
OS   / JCM 12722 / SRRC 167).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=332952 {ECO:0000312|Proteomes:UP000596276};
```

Source SHA-256: `bea04bbd31835e19259854f2e42627d0cb34cb3b47749e8af3e5d4aae56f53bb`.

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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8NLZ3?format=txt&versions=90)  
**Locator:** `lines 27-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:27:29.637546+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBCELLULAR LOCATION, DISRUPTION
RP   PHENOTYPE, AND MUTAGENESIS OF ASP-204; ASP-338 AND ASP-422.
RX   PubMed=37754565; DOI=10.1128/mbio.00977-23;
RA   Zhu Z., Yang M., Yang G., Zhang B., Cao X., Yuan J., Ge F., Wang S.;
RT   "PP2C phosphatases Ptc1 and Ptc2 dephosphorylate PGK1 to regulate autophagy
RT   and aflatoxin synthesis in the pathogenic fungus Aspergillus flavus.";
RL   MBio 14:e0097723-e0097723(2023).
```

Source SHA-256: `bea04bbd31835e19259854f2e42627d0cb34cb3b47749e8af3e5d4aae56f53bb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8NLZ3?format=txt&versions=90)  
**Locator:** `lines 57-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:27:29.637546+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000269|PubMed:37754565};
CC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;
CC         Evidence={ECO:0000269|PubMed:37754565};
CC       Note=Binds 2 magnesium or manganese ions per subunit (By similarity).
CC       Has highest activity with magnesium, but also has activity with calcium
CC       (PubMed:37754565). {ECO:0000255|PROSITE-ProRule:PRU01082,
CC       ECO:0000269|PubMed:37754565};
```

Source SHA-256: `bea04bbd31835e19259854f2e42627d0cb34cb3b47749e8af3e5d4aae56f53bb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 77. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
