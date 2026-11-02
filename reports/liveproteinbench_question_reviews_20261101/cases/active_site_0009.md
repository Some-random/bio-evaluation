# active_site_0009

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **D** — Position 154 (Acyl-thioester intermediate)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTPSKKRCGVLGATGAVGTRFILLLEQSPLLELVAVGASERSAGKKYRDAVRWKQASPMPASVADLTVRRCAPSEFSDCDIIFSGLDPVAAGDIEMAFLKANFAVFSNAKNYRLDPIVPLVVPLVNAGHIDVIPAQRKHYGLDKGLIVCNSNCAVVGLVIPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPFIPGEEGKIATESRKILGNLNPDLAGFSDQQPLQVSVACNRVPVLDGHTVCASLRFVNRPAPTASQVRDALREYKSEVQLLGCPSAPRQAIHVLDDVDRPQPRLDRDTEAGYACSVGRIREDDSGVFDIQFVALSHNTVLGASGSSILNAESAILKGYI

[Multiple Choices]
A. Position 148 (Proton acceptor)
B. Position 159 (Proton donor)
C. Position 308 (Proton acceptor)
D. Position 154 (Acyl-thioester intermediate)
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

> The sequence-matched UniProt annotation assigns position 154 the active-site role “Acyl-thioester intermediate,” supporting D. This annotation is computationally inferred from a PIRSR rule, not direct experimental evidence for this residue.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Position 154 is cysteine, whose thiol can form an acyl-thioester intermediate, making D biochemically plausible and less plausible than the hydrophobic residues at positions 148 and 159 for the stated proton-transfer roles.


**Missing item-specific fact**

> The input does not establish that this particular enzyme uses Cys154 as its catalytic thioester-forming residue, nor resolve whether the Asp at position 308 has the stated proton-acceptor role; that requires enzyme-specific mechanism or active-site annotation.


**Reason**

> Residue chemistry provides a useful clue but does not by itself establish which listed position is an active-site residue. Selecting the annotated catalytic position depends on a protein-specific fact absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence alone leaves the precise active-site assignment underdetermined, but the reviewer evidence supports D and does not support another listed option as the correct annotated answer.


### Important caveats

- The sequence matches the cited UniProt record, but the exact source snapshot used by the question author is unknown.
- The supporting active-site annotation is computationally inferred; it should not be described as experimentally established by the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Position 154 is cysteine, whose thiol can form an acyl-thioester intermediate, making D biochemically plausible and less plausible than the hydrophobic residues at positions 148 and 159 for the stated proton-transfer roles.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The input does not establish that this particular enzyme uses Cys154 as its catalytic thioester-forming residue, nor resolve whether the Asp at position 308 has the stated proton-acceptor role; that requires enzyme-specific mechanism or active-site annotation.",
    "reason": "Residue chemistry provides a useful clue but does not by itself establish which listed position is an active-site residue. Selecting the annotated catalytic position depends on a protein-specific fact absent from the question."
  },
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 154 the active-site role “Acyl-thioester intermediate,” supporting D. This annotation is computationally inferred from a PIRSR rule, not direct experimental evidence for this residue."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the exact source snapshot used by the question author is unknown.",
    "The supporting active-site annotation is computationally inferred; it should not be described as experimentally established by the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone leaves the precise active-site assignment underdetermined, but the reviewer evidence supports D and does not support another listed option as the correct annotated answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 154 the active-site role “Acyl-thioester intermediate,” supporting D. This annotation is computationally inferred from a PIRSR rule, not direct experimental evidence for this residue.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Position 154 is cysteine, whose thiol can form an acyl-thioester intermediate, making D biochemically plausible and less plausible than the hydrophobic residues at positions 148 and 159 for the stated proton-transfer roles.",
    "missing_item_specific_fact": "The input does not establish that this particular enzyme uses Cys154 as its catalytic thioester-forming residue, nor resolve whether the Asp at position 308 has the stated proton-acceptor role; that requires enzyme-specific mechanism or active-site annotation.",
    "reason": "Residue chemistry provides a useful clue but does not by itself establish which listed position is an active-site residue. Selecting the annotated catalytic position depends on a protein-specific fact absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone leaves the precise active-site assignment underdetermined, but the reviewer evidence supports D and does not support another listed option as the correct annotated answer."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the exact source snapshot used by the question author is unknown.",
    "The supporting active-site annotation is computationally inferred; it should not be described as experimentally established by the supplied evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A179UL48 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Blastomyces gilchristii, 362 aa, sequence matched) annotates position 154 as an active site forming an 'Acyl-thioester intermediate' (evidence ECO:0000255|PIRSR:PIRSR000148-1, i.e. pro-rule/similarity-based inference). The supplied sequence at position 154 is indeed Cys (C), consistent with the well-established ASADH catalytic mechanism in which a catalytic cysteine forms the acyl-thioester intermediate. The companion proton-acceptor active site is annotated at position 251 (His), not at any of the distractor positions. The annotation is computational (PIRSR) rather than directly experimentally validated on this ortholog, but the Cys-His dyad mechanism is a hallmark of the ASADH family and is corroborated by X-ray structures (PDB 6C8W) of this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The amino-acid identities at the four candidate positions, read directly from the supplied sequence, eliminate three of the four options on purely chemical grounds: position 148 is Ile (cannot serve as a proton acceptor), position 159 is Leu (cannot serve as a proton donor), and position 308 is Asp (not the catalytic proton acceptor in the ASADH Cys-His dyad; the actual proton acceptor is His-251). Only position 154 is a Cys, and formation of an acyl-thioester intermediate requires a thiol nucleophile, a property unique to cysteine among the standard amino acids. Thus, even without knowing the exact protein identity, a model applying general biochemistry (thioester chemistry requires Cys; Ile and Leu lack ionizable side chains suitable for proton transfer) can single out D.


**Missing item-specific fact**

> None essential. Recognizing the protein as ASADH would confirm the Cys-His dyad mechanism, but the chemical logic of thioester formation from a cysteine thiol is sufficient to distinguish the correct answer from the distractors given the residue identities visible in the sequence.


**Reason**

> The question supplies the full sequence, so the model can count to each candidate position and read the residue type. General biochemical knowledge (only Cys forms thioesters; Ile and Leu are non-polar aliphatic residues incapable of proton transfer; the catalytic proton acceptor in a dehydrogenase acting via a thioester intermediate is typically His, not Asp at a distant position) meaningfully separates the four choices without requiring recall of a specific database annotation for this ortholog.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor assigns a catalytic role to an amino acid that is chemically incapable of performing that role (Ile as proton acceptor, Leu as proton donor, Asp at a non-catalytic position as the proton acceptor). Only Cys-154 can form an acyl-thioester intermediate. The options are cleanly distinguishable.


### Important caveats

- The active-site annotation carries evidence code ECO:0000255 (by similarity / PIRSR pro-rule), meaning it is a computational/pro-rule inference transferred from the ASADH family pattern, not a site-directed mutagenesis or kinetic measurement on this specific Blastomyces ortholog.
- The UniProt entry was first released in February 2025 (sequence version 2); the author's construction snapshot is unknown, though the sequence matches the current and historical (entry v26) records.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning-supported judgment rests solely on information present in the original question (sequence + choices).
- The question lists a single residue per option rather than the full catalytic dyad (Cys-154 + His-251); this is a simplification but does not create ambiguity among the four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The amino-acid identities at the four candidate positions, read directly from the supplied sequence, eliminate three of the four options on purely chemical grounds: position 148 is Ile (cannot serve as a proton acceptor), position 159 is Leu (cannot serve as a proton donor), and position 308 is Asp (not the catalytic proton acceptor in the ASADH Cys-His dyad; the actual proton acceptor is His-251). Only position 154 is a Cys, and formation of an acyl-thioester intermediate requires a thiol nucleophile, a property unique to cysteine among the standard amino acids. Thus, even without knowing the exact protein identity, a model applying general biochemistry (thioester chemistry requires Cys; Ile and Leu lack ionizable side chains suitable for proton transfer) can single out D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None essential. Recognizing the protein as ASADH would confirm the Cys-His dyad mechanism, but the chemical logic of thioester formation from a cysteine thiol is sufficient to distinguish the correct answer from the distractors given the residue identities visible in the sequence.",
    "reason": "The question supplies the full sequence, so the model can count to each candidate position and read the residue type. General biochemical knowledge (only Cys forms thioesters; Ile and Leu are non-polar aliphatic residues incapable of proton transfer; the catalytic proton acceptor in a dehydrogenase acting via a thioester intermediate is typically His, not Asp at a distant position) meaningfully separates the four choices without requiring recall of a specific database annotation for this ortholog."
  },
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H4",
      "H5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A179UL48 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Blastomyces gilchristii, 362 aa, sequence matched) annotates position 154 as an active site forming an 'Acyl-thioester intermediate' (evidence ECO:0000255|PIRSR:PIRSR000148-1, i.e. pro-rule/similarity-based inference). The supplied sequence at position 154 is indeed Cys (C), consistent with the well-established ASADH catalytic mechanism in which a catalytic cysteine forms the acyl-thioester intermediate. The companion proton-acceptor active site is annotated at position 251 (His), not at any of the distractor positions. The annotation is computational (PIRSR) rather than directly experimentally validated on this ortholog, but the Cys-His dyad mechanism is a hallmark of the ASADH family and is corroborated by X-ray structures (PDB 6C8W) of this protein."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (by similarity / PIRSR pro-rule), meaning it is a computational/pro-rule inference transferred from the ASADH family pattern, not a site-directed mutagenesis or kinetic measurement on this specific Blastomyces ortholog.",
    "The UniProt entry was first released in February 2025 (sequence version 2); the author's construction snapshot is unknown, though the sequence matches the current and historical (entry v26) records.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning-supported judgment rests solely on information present in the original question (sequence + choices).",
    "The question lists a single residue per option rather than the full catalytic dyad (Cys-154 + His-251); this is a simplification but does not create ambiguity among the four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor assigns a catalytic role to an amino acid that is chemically incapable of performing that role (Ile as proton acceptor, Leu as proton donor, Asp at a non-catalytic position as the proton acceptor). Only Cys-154 can form an acyl-thioester intermediate. The options are cleanly distinguishable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A179UL48 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Blastomyces gilchristii, 362 aa, sequence matched) annotates position 154 as an active site forming an 'Acyl-thioester intermediate' (evidence ECO:0000255|PIRSR:PIRSR000148-1, i.e. pro-rule/similarity-based inference). The supplied sequence at position 154 is indeed Cys (C), consistent with the well-established ASADH catalytic mechanism in which a catalytic cysteine forms the acyl-thioester intermediate. The companion proton-acceptor active site is annotated at position 251 (His), not at any of the distractor positions. The annotation is computational (PIRSR) rather than directly experimentally validated on this ortholog, but the Cys-His dyad mechanism is a hallmark of the ASADH family and is corroborated by X-ray structures (PDB 6C8W) of this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H4", "H5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The amino-acid identities at the four candidate positions, read directly from the supplied sequence, eliminate three of the four options on purely chemical grounds: position 148 is Ile (cannot serve as a proton acceptor), position 159 is Leu (cannot serve as a proton donor), and position 308 is Asp (not the catalytic proton acceptor in the ASADH Cys-His dyad; the actual proton acceptor is His-251). Only position 154 is a Cys, and formation of an acyl-thioester intermediate requires a thiol nucleophile, a property unique to cysteine among the standard amino acids. Thus, even without knowing the exact protein identity, a model applying general biochemistry (thioester chemistry requires Cys; Ile and Leu lack ionizable side chains suitable for proton transfer) can single out D.",
    "missing_item_specific_fact": "None essential. Recognizing the protein as ASADH would confirm the Cys-His dyad mechanism, but the chemical logic of thioester formation from a cysteine thiol is sufficient to distinguish the correct answer from the distractors given the residue identities visible in the sequence.",
    "reason": "The question supplies the full sequence, so the model can count to each candidate position and read the residue type. General biochemical knowledge (only Cys forms thioesters; Ile and Leu are non-polar aliphatic residues incapable of proton transfer; the catalytic proton acceptor in a dehydrogenase acting via a thioester intermediate is typically His, not Asp at a distant position) meaningfully separates the four choices without requiring recall of a specific database annotation for this ortholog."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor assigns a catalytic role to an amino acid that is chemically incapable of performing that role (Ile as proton acceptor, Leu as proton donor, Asp at a non-catalytic position as the proton acceptor). Only Cys-154 can form an acyl-thioester intermediate. The options are cleanly distinguishable."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (by similarity / PIRSR pro-rule), meaning it is a computational/pro-rule inference transferred from the ASADH family pattern, not a site-directed mutagenesis or kinetic measurement on this specific Blastomyces ortholog.",
    "The UniProt entry was first released in February 2025 (sequence version 2); the author's construction snapshot is unknown, though the sequence matches the current and historical (entry v26) records.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning-supported judgment rests solely on information present in the original question (sequence + choices).",
    "The question lists a single residue per option rather than the full catalytic dyad (Cys-154 + His-251); this is a simplification but does not create ambiguity among the four choices."
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

**Accession:** `A0A179UL48` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
"A0A179UL48"
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30107909","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
{"description":"Acyl-thioester intermediate","evidences":[{"evidenceCode":"ECO:0000255","id":"PIRSR000148-1","source":"PIRSR"}],"location":{"end":{"modifier":"EXACT","value":154},"start":{"modifier":"EXACT","value":154}},"type":"Active site"}
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:30.243142+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255","id":"PIRSR000148-1","source":"PIRSR"}],"location":{"end":{"modifier":"EXACT","value":251},"start":{"modifier":"EXACT","value":251}},"type":"Active site"}
```

Source SHA-256: `bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
ID   DHAS_BLAGS              Reviewed;         362 AA.
AC   A0A179UL48;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 2.
DT   28-JAN-2026, entry version 26.
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};
GN   ORFNames=BDBG_16922 {ECO:0000312|EMBL:OAT07949.1};
OS   Blastomyces gilchristii (strain SLH14081) (Blastomyces dermatitidis).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Onygenales; Ajellomycetaceae; Blastomyces.
OX   NCBI_TaxID=559298 {ECO:0000312|Proteomes:UP000002038};
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 32-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
RN   [3] {ECO:0007744|PDB:6C85, ECO:0007744|PDB:6C8W}
RP   X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND
RP   NADP(+), FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION,
RP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.
RX   PubMed=30107909; DOI=10.1016/j.bbrc.2018.08.053;
RA   Dahal G.P., Viola R.E.;
RT   "Structural insights into inhibitor binding to a fungal ortholog of
RT   aspartate semialdehyde dehydrogenase.";
RL   Biochem. Biophys. Res. Commun. 503:2848-2854(2018).
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 133-135`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
FT   ACT_SITE        154
FT                   /note="Acyl-thioester intermediate"
FT                   /evidence="ECO:0000255|PIRSR:PIRSR000148-1"
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)  
**Locator:** `lines 136-138`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 2.  
**Retrieved:** 2026-11-02T04:24:32.458235+00:00.  

```text
FT   ACT_SITE        251
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255|PIRSR:PIRSR000148-1"
```

Source SHA-256: `4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
