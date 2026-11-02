# active_site_0113

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **A** — Position 409 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNVALVFLLFQVQDGTGITLGPSKLDSKPTSLDSQQHVADKRWLATVGHYKHLAGATESTRDVSLLEERAQHRVNAQETNQRRTIFQRLLNLLRRRERDGEVSGSAADSSSRPRLSVRQRLAQLWRRAKSLFKRGIRRYFPQGRNRQRSLRAQRRRSELVFEKADSGCVIGKRILAHMQEQIGQPQALENSERLDRILTVAAWPPDVPKRFVSVTTGETRTLVRGAPLGSGGFATVYEATDVETNEELAVKVFMSEKEPTDETMLDLQRESSCYRNFSLAKTAKDAQESCRFMVPSDVVMLEGQPASTEVVIGLTTRWVPNYFLLMMRAEADMSKVISWVFGDASVNKSEFGLVVRMYLSSQAIKLVANVQAQGIVHTDIKPANFLLLKDGRLFLGDFGTYRINNSVGRAIGTPGYEPPERPFQATGITYTFPTDAWQLGITLYCIWCKERPTPADGIWDYLHFADCPSTPELVQDLIRSLLNRDPQKRMLPLQALETAAFKEMDSVVKGAAQNFEQQEHLHTE

[Multiple Choices]
A. Position 409 (Proton acceptor)
B. Position 981 (Proton acceptor; for dehydratase activity)
C. Position 6761 (Proton donor; for dehydratase activity)
D. Position 1686 (Proton acceptor)
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

> The exact sequence matches a UniProt entry annotating position 409 as the proton acceptor. That annotation is attributed to a PROSITE-ProRule computational rule; the cited literature includes Asp-409 mutagenesis, but the excerpts do not provide the experimental result establishing its catalytic role.

Citations as saved: [C5](#evidence-c5), [H7](#evidence-h7), [C15](#evidence-c15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence is 554 residues long, so position 409 is in range while positions 981, 6761, and 1686 are not. A is the only positionally possible choice for this sequence.


**Missing item-specific fact**

> The precise assignment of residue 409 as a proton acceptor is not established by sequence length alone; confirming that biochemical role would require the protein-specific catalytic-site annotation or experimental evidence.


**Reason**

> Although the precise catalytic assignment is an item-specific fact, the choices allow A to be distinguished by checking residue coordinates against the supplied sequence length.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A gives a position within the 554-residue sequence; the other listed positions cannot refer to residues in this sequence.


### Important caveats

- The explicit proton-acceptor annotation is computationally assigned by PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.
- The cited mutagenesis reference concerns Asp-409, but its citation alone does not establish the experimental finding or prove the proton-acceptor mechanism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence is 554 residues long, so position 409 is in range while positions 981, 6761, and 1686 are not. A is the only positionally possible choice for this sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise assignment of residue 409 as a proton acceptor is not established by sequence length alone; confirming that biochemical role would require the protein-specific catalytic-site annotation or experimental evidence.",
    "reason": "Although the precise catalytic assignment is an item-specific fact, the choices allow A to be distinguished by checking residue coordinates against the supplied sequence length."
  },
  "case_id": "active_site_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H7",
      "C15"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating position 409 as the proton acceptor. That annotation is attributed to a PROSITE-ProRule computational rule; the cited literature includes Asp-409 mutagenesis, but the excerpts do not provide the experimental result establishing its catalytic role."
  },
  "important_caveats": [
    "The explicit proton-acceptor annotation is computationally assigned by PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.",
    "The cited mutagenesis reference concerns Asp-409, but its citation alone does not establish the experimental finding or prove the proton-acceptor mechanism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A gives a position within the 554-residue sequence; the other listed positions cannot refer to residues in this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating position 409 as the proton acceptor. That annotation is attributed to a PROSITE-ProRule computational rule; the cited literature includes Asp-409 mutagenesis, but the excerpts do not provide the experimental result establishing its catalytic role.",
    "evidence_ids": ["C5", "H7", "C15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence is 554 residues long, so position 409 is in range while positions 981, 6761, and 1686 are not. A is the only positionally possible choice for this sequence.",
    "missing_item_specific_fact": "The precise assignment of residue 409 as a proton acceptor is not established by sequence length alone; confirming that biochemical role would require the protein-specific catalytic-site annotation or experimental evidence.",
    "reason": "Although the precise catalytic assignment is an item-specific fact, the choices allow A to be distinguished by checking residue coordinates against the supplied sequence length."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A gives a position within the 554-residue sequence; the other listed positions cannot refer to residues in this sequence."
  },
  "important_caveats": [
    "The explicit proton-acceptor annotation is computationally assigned by PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.",
    "The cited mutagenesis reference concerns Asp-409, but its citation alone does not establish the experimental finding or prove the proton-acceptor mechanism."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2PAY2 (ROP18_TOXGO, 554 AA, sequence matched) annotates position 409 as ACT_SITE with description 'Proton acceptor' (evidence ECO:0000255|PROSITE-ProRule:PRU00159, a computational motif-based assignment). This is corroborated experimentally: three independent studies (PubMed 21147463, 21203588, 24129568) report 'MUTAGENESIS OF ASP-409' confirming catalytic importance, and PDB 4JRN (2.71 Å crystal structure of residues 187-554 with ATP analog and Mg²⁺) validates the kinase domain fold. The residue at position 409 falls within the catalytic loop of this serine/threonine kinase (EC 2.7.11.1), consistent with the HRD-motif catalytic aspartate acting as proton acceptor.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C15](#evidence-c15), [C16](#evidence-c16), [C18](#evidence-c18), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The provided protein sequence is 554 amino acids long (confirmed by UniProt entry length and by direct counting). Options B (position 981), C (position 6761), and D (position 1686) all reference residue positions that exceed the total length of the supplied sequence and are therefore physically impossible. Only option A (position 409) falls within the valid range. Additionally, a student familiar with protein-kinase catalytic mechanisms could identify the HRD/catalytic-loop aspartate (the 'AD' in 'LHFADCPSTPEL' near the activation loop 'DIKPAN' motif) as the proton acceptor, further supporting position 409.


**Missing item-specific fact**

> None strictly required. The answer is determinable from the sequence itself by elimination. Knowledge of ROP18 specifically is not needed.


**Reason**

> The primary discriminating argument is trivial elimination: the protein is 554 AA, so positions 981, 6761, and 1686 cannot exist. This is a valid reasoning step from the supplied data. A secondary (but unnecessary) biological argument involves recognizing the kinase catalytic-loop aspartate. No item-specific external annotation lookup is required to distinguish the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A references a position within the 554-residue sequence. Options B, C, and D are unambiguously impossible. There is no genuine ambiguity in the answer.


### Important caveats

- The distractors (positions 981, 6761, 1686) are all beyond the 554-residue protein length, making the question trivially answerable by simple sequence-length elimination without any knowledge of enzyme active sites or kinase catalysis. This severely limits the question's diagnostic value for testing active-site prediction ability.
- The UniProt annotation for position 409 uses evidence code ECO:0000255 (PROSITE-ProRule), which is a computational/pattern-based inference rather than direct experimental determination. However, three independent mutagenesis studies and a crystal structure provide experimental corroboration of Asp-409's catalytic role.
- The question stem describes the task as identifying 'key amino acid residues that form the active site' (plural), but the correct answer lists only a single position. The phrasing is slightly inconsistent with the single-residue answer, though this does not affect correctness.
- The reviewer-only evidence confirms the sequence match (SHA-256 identical) between the benchmark input and UniProt Q2PAY2, so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The provided protein sequence is 554 amino acids long (confirmed by UniProt entry length and by direct counting). Options B (position 981), C (position 6761), and D (position 1686) all reference residue positions that exceed the total length of the supplied sequence and are therefore physically impossible. Only option A (position 409) falls within the valid range. Additionally, a student familiar with protein-kinase catalytic mechanisms could identify the HRD/catalytic-loop aspartate (the 'AD' in 'LHFADCPSTPEL' near the activation loop 'DIKPAN' motif) as the proton acceptor, further supporting position 409.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The answer is determinable from the sequence itself by elimination. Knowledge of ROP18 specifically is not needed.",
    "reason": "The primary discriminating argument is trivial elimination: the protein is 554 AA, so positions 981, 6761, and 1686 cannot exist. This is a valid reasoning step from the supplied data. A secondary (but unnecessary) biological argument involves recognizing the kinase catalytic-loop aspartate. No item-specific external annotation lookup is required to distinguish the choices."
  },
  "case_id": "active_site_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C15",
      "C16",
      "C18",
      "H1",
      "H3",
      "H4",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2PAY2 (ROP18_TOXGO, 554 AA, sequence matched) annotates position 409 as ACT_SITE with description 'Proton acceptor' (evidence ECO:0000255|PROSITE-ProRule:PRU00159, a computational motif-based assignment). This is corroborated experimentally: three independent studies (PubMed 21147463, 21203588, 24129568) report 'MUTAGENESIS OF ASP-409' confirming catalytic importance, and PDB 4JRN (2.71 Å crystal structure of residues 187-554 with ATP analog and Mg²⁺) validates the kinase domain fold. The residue at position 409 falls within the catalytic loop of this serine/threonine kinase (EC 2.7.11.1), consistent with the HRD-motif catalytic aspartate acting as proton acceptor."
  },
  "important_caveats": [
    "The distractors (positions 981, 6761, 1686) are all beyond the 554-residue protein length, making the question trivially answerable by simple sequence-length elimination without any knowledge of enzyme active sites or kinase catalysis. This severely limits the question's diagnostic value for testing active-site prediction ability.",
    "The UniProt annotation for position 409 uses evidence code ECO:0000255 (PROSITE-ProRule), which is a computational/pattern-based inference rather than direct experimental determination. However, three independent mutagenesis studies and a crystal structure provide experimental corroboration of Asp-409's catalytic role.",
    "The question stem describes the task as identifying 'key amino acid residues that form the active site' (plural), but the correct answer lists only a single position. The phrasing is slightly inconsistent with the single-residue answer, though this does not affect correctness.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) between the benchmark input and UniProt Q2PAY2, so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A references a position within the 554-residue sequence. Options B, C, and D are unambiguously impossible. There is no genuine ambiguity in the answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2PAY2 (ROP18_TOXGO, 554 AA, sequence matched) annotates position 409 as ACT_SITE with description 'Proton acceptor' (evidence ECO:0000255|PROSITE-ProRule:PRU00159, a computational motif-based assignment). This is corroborated experimentally: three independent studies (PubMed 21147463, 21203588, 24129568) report 'MUTAGENESIS OF ASP-409' confirming catalytic importance, and PDB 4JRN (2.71 Å crystal structure of residues 187-554 with ATP analog and Mg²⁺) validates the kinase domain fold. The residue at position 409 falls within the catalytic loop of this serine/threonine kinase (EC 2.7.11.1), consistent with the HRD-motif catalytic aspartate acting as proton acceptor.",
    "evidence_ids": ["C1", "C4", "C5", "C15", "C16", "C18", "H1", "H3", "H4", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The provided protein sequence is 554 amino acids long (confirmed by UniProt entry length and by direct counting). Options B (position 981), C (position 6761), and D (position 1686) all reference residue positions that exceed the total length of the supplied sequence and are therefore physically impossible. Only option A (position 409) falls within the valid range. Additionally, a student familiar with protein-kinase catalytic mechanisms could identify the HRD/catalytic-loop aspartate (the 'AD' in 'LHFADCPSTPEL' near the activation loop 'DIKPAN' motif) as the proton acceptor, further supporting position 409.",
    "missing_item_specific_fact": "None strictly required. The answer is determinable from the sequence itself by elimination. Knowledge of ROP18 specifically is not needed.",
    "reason": "The primary discriminating argument is trivial elimination: the protein is 554 AA, so positions 981, 6761, and 1686 cannot exist. This is a valid reasoning step from the supplied data. A secondary (but unnecessary) biological argument involves recognizing the kinase catalytic-loop aspartate. No item-specific external annotation lookup is required to distinguish the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A references a position within the 554-residue sequence. Options B, C, and D are unambiguously impossible. There is no genuine ambiguity in the answer."
  },
  "important_caveats": [
    "The distractors (positions 981, 6761, 1686) are all beyond the 554-residue protein length, making the question trivially answerable by simple sequence-length elimination without any knowledge of enzyme active sites or kinase catalysis. This severely limits the question's diagnostic value for testing active-site prediction ability.",
    "The UniProt annotation for position 409 uses evidence code ECO:0000255 (PROSITE-ProRule), which is a computational/pattern-based inference rather than direct experimental determination. However, three independent mutagenesis studies and a crystal structure provide experimental corroboration of Asp-409's catalytic role.",
    "The question stem describes the task as identifying 'key amino acid residues that form the active site' (plural), but the correct answer lists only a single position. The phrasing is slightly inconsistent with the single-residue answer, though this does not affect correctness.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) between the benchmark input and UniProt Q2PAY2, so the annotation applies directly to the supplied sequence."
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

**Accession:** `Q2PAY2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 128. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
"Q2PAY2"
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AFO54811.1","source":"EMBL"}],"value":"Rhoptry kinase family protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"CAJ27113.1","source":"EMBL"}],"value":"Rhoptry protein 18"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"KAF4642700.1","source":"EMBL"}],"value":"Rhoptry protein ROP18"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21147463","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21203588","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24129568","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"23144612","source":"PubMed"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"19266027","source":"PubMed"}],"value":"Serine/threonine-protein kinase ROP18"}}}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":409},"start":{"modifier":"EXACT","value":409}},"type":"Active site"}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"citation":{"authors":["Fentress S.J.","Behnke M.S.","Dunay I.R.","Mashayekhi M.","Rommereim L.M.","Fox B.A.","Bzik D.J.","Taylor G.A.","Turk B.E.","Lichti C.F.","Townsend R.R.","Qiu W.","Hui R.","Beatty W.L.","Sibley L.D."],"citationCrossReferences":[{"database":"PubMed","id":"21147463"},{"database":"DOI","id":"10.1016/j.chom.2010.11.005"}],"citationType":"journal article","firstPage":"484","id":"21147463","journal":"Cell Host Microbe","lastPage":"495","publicationDate":"2010","title":"Phosphorylation of immunity-related GTPases by a Toxoplasma gondii-secreted kinase promotes macrophage survival and virulence.","volume":"8"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","INTERACTION WITH MOUSE IRGB6 (TGTP1/TGTP2)","DISRUPTION PHENOTYPE","MUTAGENESIS OF ASP-409"]}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"citation":{"authors":["Steinfeldt T.","Koenen-Waisman S.","Tong L.","Pawlowski N.","Lamkemeyer T.","Sibley L.D.","Hunn J.P.","Howard J.C."],"citationCrossReferences":[{"database":"PubMed","id":"21203588"},{"database":"DOI","id":"10.1371/journal.pbio.1000576"}],"citationType":"journal article","firstPage":"e1000576","id":"21203588","journal":"PLoS Biol.","lastPage":"e1000576","publicationDate":"2010","title":"Phosphorylation of mouse immunity-related GTPase (IRG) resistance proteins is an evasion strategy for virulent Toxoplasma gondii.","volume":"8"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","MUTAGENESIS OF ASP-409"]}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/references/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"citation":{"authors":["Lim D.","Gold D.A.","Julien L.","Rosowski E.E.","Niedelman W.","Yaffe M.B.","Saeij J.P."],"citationCrossReferences":[{"database":"PubMed","id":"24129568"},{"database":"DOI","id":"10.1074/jbc.m113.523266"}],"citationType":"journal article","firstPage":"34968","id":"24129568","journal":"J. Biol. Chem.","lastPage":"34980","publicationDate":"2013","title":"Structure of the Toxoplasma gondii ROP18 kinase domain reveals a second ligand binding pocket required for acute virulence.","volume":"288"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4JRN","source":"PDB"}],"referenceNumber":14,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.71 ANGSTROMS) OF 187-554 IN COMPLEX WITH ATP ANALOG AND MAGNESIUM ION","FUNCTION","CATALYTIC ACTIVITY","DOMAIN","DISULFIDE BOND","MUTAGENESIS OF ASP-409"]}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
ID   ROP18_TOXGO             Reviewed;         554 AA.
AC   Q2PAY2; B9Q063; S7W304;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   07-FEB-2006, sequence version 1.
DT   28-JAN-2026, entry version 128.
DE   RecName: Full=Serine/threonine-protein kinase ROP18 {ECO:0000303|PubMed:19266027};
DE            EC=2.7.11.1 {ECO:0000269|PubMed:21147463, ECO:0000269|PubMed:21203588, ECO:0000269|PubMed:24129568, ECO:0000305|PubMed:23144612};
DE   AltName: Full=Rhoptry kinase family protein {ECO:0000312|EMBL:AFO54811.1};
DE   AltName: Full=Rhoptry protein 18 {ECO:0000312|EMBL:CAJ27113.1};
DE   AltName: Full=Rhoptry protein ROP18 {ECO:0000312|EMBL:KAF4642700.1};
GN   Name=ROP18 {ECO:0000312|EMBL:AFO54811.1};
GN   ORFNames=TGRH88_034260 {ECO:0000312|EMBL:KAF4642700.1};
OS   Toxoplasma gondii.
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;
OC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.
OX   NCBI_TaxID=5811 {ECO:0000312|EMBL:CAJ27113.1};
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 45-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, INTERACTION WITH MOUSE IRGB6 (TGTP1/TGTP2),
RP   DISRUPTION PHENOTYPE, AND MUTAGENESIS OF ASP-409.
RX   PubMed=21147463; DOI=10.1016/j.chom.2010.11.005;
RA   Fentress S.J., Behnke M.S., Dunay I.R., Mashayekhi M., Rommereim L.M.,
RA   Fox B.A., Bzik D.J., Taylor G.A., Turk B.E., Lichti C.F., Townsend R.R.,
RA   Qiu W., Hui R., Beatty W.L., Sibley L.D.;
RT   "Phosphorylation of immunity-related GTPases by a Toxoplasma gondii-
RT   secreted kinase promotes macrophage survival and virulence.";
RL   Cell Host Microbe 8:484-495(2010).
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 55-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
RN   [5] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF ASP-409.
RX   PubMed=21203588; DOI=10.1371/journal.pbio.1000576;
RA   Steinfeldt T., Koenen-Waisman S., Tong L., Pawlowski N., Lamkemeyer T.,
RA   Sibley L.D., Hunn J.P., Howard J.C.;
RT   "Phosphorylation of mouse immunity-related GTPase (IRG) resistance proteins
RT   is an evasion strategy for virulent Toxoplasma gondii.";
RL   PLoS Biol. 8:e1000576-e1000576(2010).
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 124-133`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
RN   [14] {ECO:0007744|PDB:4JRN}
RP   X-RAY CRYSTALLOGRAPHY (2.71 ANGSTROMS) OF 187-554 IN COMPLEX WITH ATP
RP   ANALOG AND MAGNESIUM ION, FUNCTION, CATALYTIC ACTIVITY, DOMAIN, DISULFIDE
RP   BOND, AND MUTAGENESIS OF ASP-409.
RX   PubMed=24129568; DOI=10.1074/jbc.m113.523266;
RA   Lim D., Gold D.A., Julien L., Rosowski E.E., Niedelman W., Yaffe M.B.,
RA   Saeij J.P.;
RT   "Structure of the Toxoplasma gondii ROP18 kinase domain reveals a second
RT   ligand binding pocket required for acute virulence.";
RL   J. Biol. Chem. 288:34968-34980(2013).
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 300-302`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
FT   ACT_SITE        409
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00159"
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 113. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
