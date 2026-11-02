# catalytic_activity_0149

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — 5-O-(ADP-D-ribosyl)-L-glutamyl-&#91;protein&#93; + H2O = L-glutamyl-&#91;protein&#93; + ADP-D-ribose + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRTTLTGTASVLDTTLTRLIDDVIENGSSFLADDENLQHYKQHLSHLETASKIALLRECLCVRPPLPLLPEDLLQNVDSILTRVRQHKILTPIFSLSPSRLIKHGDLGATRIHLWRGDITTLTGVTAITNAANSQGLGCFQPTHRCIDNIIHAEAGPRLREECFQRMQARGKELEPGEVLVTEGHALFASSVMHTVGPQLKRGASPTETERRQLAKCYESILEALELLPSDEDGSKSIALCCISTGLFAFPADEAAEIAVSTVTSWLQKHPSTTITDVIFNTFTQSDTEFYSKLLGPSHTKSISPVENTPQGSLSLAREWLSSADAVLVTAGAGLSAAEGLDYHSRDLFKRNFPGCLKFGLTSLYSVFGFNDWPSEEHRWGYFFTHLNMVANWSNTPTYQILIPWLRNFGQDAFVRTSNADGLFLANGWPKEQLSTPQGSYGYLQCLNNCRVDAVVPSAPLVADAMPHIDKATQKLMDPSKIPLCRFCGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKKNLVILELGVGMNTPGVLRWPNEDLVMRSDGRVKLIRVGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE

[Multiple Choices]
A. (2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O
B. deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose
C. dopamine + S-adenosyl-L-methionine = N-methyl-dopamine + S-adenosyl-L-homocysteine + H(+)
D. 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the reviewed protein sequence, and its catalytic-activity annotation gives the reaction in choice D with ECO:0000269 evidence linked to a 2024 publication. The source also cites structural and mutagenesis work. This supports D for this protein, while distinguishing the evidence as an annotation tied to published experimental work rather than something established from the sequence alone.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a protein with ADP-ribose-related domains, but the input does not establish the specific substrate or hydrolysis of ADP-ribose from glutamylated protein. The precise reaction cannot be reliably selected from sequence inspection alone.


**Missing item-specific fact**

> The protein-specific catalytic activity: hydrolysis of 5-O-(ADP-D-ribosyl)-L-glutamyl-&#91;protein&#93;.


**Reason**

> Choosing D requires knowing this protein's experimentally characterized or database-annotated activity, which is absent from the question input; recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed reactions, D matches the supported catalytic activity; the other choices describe distinct reactions.


### Important caveats

- The reviewer-only source records an exact sequence match and an experimental-evidence code for the catalytic activity, but the primary paper was not independently reviewed here.
- The author’s exact source snapshot is unknown; the historical record checked also matches the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a protein with ADP-ribose-related domains, but the input does not establish the specific substrate or hydrolysis of ADP-ribose from glutamylated protein. The precise reaction cannot be reliably selected from sequence inspection alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity: hydrolysis of 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein].",
    "reason": "Choosing D requires knowing this protein's experimentally characterized or database-annotated activity, which is absent from the question input; recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied evidence."
  },
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed protein sequence, and its catalytic-activity annotation gives the reaction in choice D with ECO:0000269 evidence linked to a 2024 publication. The source also cites structural and mutagenesis work. This supports D for this protein, while distinguishing the evidence as an annotation tied to published experimental work rather than something established from the sequence alone."
  },
  "important_caveats": [
    "The reviewer-only source records an exact sequence match and an experimental-evidence code for the catalytic activity, but the primary paper was not independently reviewed here.",
    "The author’s exact source snapshot is unknown; the historical record checked also matches the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, D matches the supported catalytic activity; the other choices describe distinct reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed protein sequence, and its catalytic-activity annotation gives the reaction in choice D with ECO:0000269 evidence linked to a 2024 publication. The source also cites structural and mutagenesis work. This supports D for this protein, while distinguishing the evidence as an annotation tied to published experimental work rather than something established from the sequence alone.",
    "evidence_ids": ["C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a protein with ADP-ribose-related domains, but the input does not establish the specific substrate or hydrolysis of ADP-ribose from glutamylated protein. The precise reaction cannot be reliably selected from sequence inspection alone.",
    "missing_item_specific_fact": "The protein-specific catalytic activity: hydrolysis of 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein].",
    "reason": "Choosing D requires knowing this protein's experimentally characterized or database-annotated activity, which is absent from the question input; recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, D matches the supported catalytic activity; the other choices describe distinct reactions."
  },
  "important_caveats": [
    "The reviewer-only source records an exact sequence match and an experimental-evidence code for the catalytic activity, but the primary paper was not independently reviewed here.",
    "The author’s exact source snapshot is unknown; the historical record checked also matches the sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProt A0A559KX76 (ADRHT_FUSOC) exactly (SHA256 confirmed). The UniProt entry explicitly annotates the catalytic activity as '5-O-(ADP-D-ribosyl)-L-glutamyl-&#91;protein&#93; + H2O = L-glutamyl-&#91;protein&#93; + ADP-D-ribose + H(+)' with evidence code ECO:0000269 (inferred from direct assay), supported by a 2024 JBC paper (PMID 39270823) and X-ray crystallography at 2.22 Å in complex with Zn(2+). The reaction in option D matches the annotated reaction verbatim.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable macrodomain-fold motifs (e.g., the conserved 'GAGLSAA' β-strand region and 'CGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKK' segment), which are hallmarks of ADP-ribose-interacting proteins. Among the four options, only D involves ADP-ribose chemistry; the others describe a dihydroxy-acid dehydratase (A), a glycosidase (B), and a SAM-dependent methyltransferase (C), none of whose characteristic motifs (e.g., ilvD active-site residues, glycosidase catalytic Glu/Asp, COMT SAM-binding pocket) are present in this sequence. Recognizing the macrodomain fold and associating it with ADP-ribose metabolism is a legitimate general-biology inference that eliminates A, B, and C.


**Missing item-specific fact**

> Distinguishing the hydrolase (removal) activity from the transferase (addition) activity of this particular bifunctional macrodomain/SirTM protein cannot be resolved from sequence alone; however, since no option describes a transferase reaction, this distinction is not required to select D.


**Reason**

> A model with knowledge of the macrodomain fold and its association with ADP-ribose metabolism can eliminate the three non-ADP-ribose options through general biological reasoning. The reasoning does not require memorizing this specific Fusarium protein's database entry, though it does require recognizing a somewhat specialized fold motif.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is annotated as bifunctional (hydrolase + probable transferase), but no option describes the transferase reaction. Option D is the only ADP-ribose-related reaction and matches the experimentally confirmed catalytic activity exactly. The other three options correspond to unrelated enzyme classes with no sequence support.


### Important caveats

- The UniProt entry was first published 2025-06-18; the historical Swiss-Prot record (version 22) was first released in January 2026. If the benchmark was constructed before that date, the annotation may not have been publicly available, though the sequence itself was.
- The transferase activity (EC 2.4.2.-) is annotated only by similarity (ECO:0000250, inferred from P0DN71), not experimentally confirmed. The hydrolase activity (EC 3.2.1.-) is experimentally confirmed (ECO:0000269).
- Recognition of the macrodomain fold from linear sequence is a specialized but legitimate biological skill; it is less universally taught than, e.g., Rossmann or Walker A motifs, so the reasoning argument, while valid, requires some domain-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable macrodomain-fold motifs (e.g., the conserved 'GAGLSAA' β-strand region and 'CGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKK' segment), which are hallmarks of ADP-ribose-interacting proteins. Among the four options, only D involves ADP-ribose chemistry; the others describe a dihydroxy-acid dehydratase (A), a glycosidase (B), and a SAM-dependent methyltransferase (C), none of whose characteristic motifs (e.g., ilvD active-site residues, glycosidase catalytic Glu/Asp, COMT SAM-binding pocket) are present in this sequence. Recognizing the macrodomain fold and associating it with ADP-ribose metabolism is a legitimate general-biology inference that eliminates A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Distinguishing the hydrolase (removal) activity from the transferase (addition) activity of this particular bifunctional macrodomain/SirTM protein cannot be resolved from sequence alone; however, since no option describes a transferase reaction, this distinction is not required to select D.",
    "reason": "A model with knowledge of the macrodomain fold and its association with ADP-ribose metabolism can eliminate the three non-ADP-ribose options through general biological reasoning. The reasoning does not require memorizing this specific Fusarium protein's database entry, though it does require recognizing a somewhat specialized fold motif."
  },
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt A0A559KX76 (ADRHT_FUSOC) exactly (SHA256 confirmed). The UniProt entry explicitly annotates the catalytic activity as '5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)' with evidence code ECO:0000269 (inferred from direct assay), supported by a 2024 JBC paper (PMID 39270823) and X-ray crystallography at 2.22 Å in complex with Zn(2+). The reaction in option D matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The UniProt entry was first published 2025-06-18; the historical Swiss-Prot record (version 22) was first released in January 2026. If the benchmark was constructed before that date, the annotation may not have been publicly available, though the sequence itself was.",
    "The transferase activity (EC 2.4.2.-) is annotated only by similarity (ECO:0000250, inferred from P0DN71), not experimentally confirmed. The hydrolase activity (EC 3.2.1.-) is experimentally confirmed (ECO:0000269).",
    "Recognition of the macrodomain fold from linear sequence is a specialized but legitimate biological skill; it is less universally taught than, e.g., Rossmann or Walker A motifs, so the reasoning argument, while valid, requires some domain-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is annotated as bifunctional (hydrolase + probable transferase), but no option describes the transferase reaction. Option D is the only ADP-ribose-related reaction and matches the experimentally confirmed catalytic activity exactly. The other three options correspond to unrelated enzyme classes with no sequence support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt A0A559KX76 (ADRHT_FUSOC) exactly (SHA256 confirmed). The UniProt entry explicitly annotates the catalytic activity as '5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)' with evidence code ECO:0000269 (inferred from direct assay), supported by a 2024 JBC paper (PMID 39270823) and X-ray crystallography at 2.22 Å in complex with Zn(2+). The reaction in option D matches the annotated reaction verbatim.",
    "evidence_ids": ["C5", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable macrodomain-fold motifs (e.g., the conserved 'GAGLSAA' β-strand region and 'CGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKK' segment), which are hallmarks of ADP-ribose-interacting proteins. Among the four options, only D involves ADP-ribose chemistry; the others describe a dihydroxy-acid dehydratase (A), a glycosidase (B), and a SAM-dependent methyltransferase (C), none of whose characteristic motifs (e.g., ilvD active-site residues, glycosidase catalytic Glu/Asp, COMT SAM-binding pocket) are present in this sequence. Recognizing the macrodomain fold and associating it with ADP-ribose metabolism is a legitimate general-biology inference that eliminates A, B, and C.",
    "missing_item_specific_fact": "Distinguishing the hydrolase (removal) activity from the transferase (addition) activity of this particular bifunctional macrodomain/SirTM protein cannot be resolved from sequence alone; however, since no option describes a transferase reaction, this distinction is not required to select D.",
    "reason": "A model with knowledge of the macrodomain fold and its association with ADP-ribose metabolism can eliminate the three non-ADP-ribose options through general biological reasoning. The reasoning does not require memorizing this specific Fusarium protein's database entry, though it does require recognizing a somewhat specialized fold motif."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is annotated as bifunctional (hydrolase + probable transferase), but no option describes the transferase reaction. Option D is the only ADP-ribose-related reaction and matches the experimentally confirmed catalytic activity exactly. The other three options correspond to unrelated enzyme classes with no sequence support."
  },
  "important_caveats": [
    "The UniProt entry was first published 2025-06-18; the historical Swiss-Prot record (version 22) was first released in January 2026. If the benchmark was constructed before that date, the annotation may not have been publicly available, though the sequence itself was.",
    "The transferase activity (EC 2.4.2.-) is annotated only by similarity (ECO:0000250, inferred from P0DN71), not experimentally confirmed. The hydrolase activity (EC 3.2.1.-) is experimentally confirmed (ECO:0000269).",
    "Recognition of the macrodomain fold from linear sequence is a specialized but legitimate biological skill; it is less universally taught than, e.g., Rossmann or Walker A motifs, so the reasoning argument, while valid, requires some domain-specific knowledge."
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

**Accession:** `A0A559KX76` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 22. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:25.184799+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"}],"name":"5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58248"},{"database":"Rhea","id":"RHEA-COMP:10208"},{"database":"Rhea","id":"RHEA-COMP:15089"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29973"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:142540"}]}}
```

Source SHA-256: `52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:25.184799+00:00.  

```json
{"citation":{"authors":["Ariza A.","Liu Q.","Cowieson N.P.","Ahel I.","Filippov D.V.","Rack J.G.M."],"citationCrossReferences":[{"database":"PubMed","id":"39270823"},{"database":"DOI","id":"10.1016/j.jbc.2024.107770"}],"citationType":"journal article","firstPage":"107770","id":"39270823","journal":"J. Biol. Chem.","lastPage":"107770","publicationDate":"2024","title":"Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-dependent macrodomains.","volume":"300"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8RSN","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"race 1 / IMI 141109"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS) IN COMPLEX WITH ZN(2+)","FUNCTION AS AN HYDROLASE","CATALYTIC ACTIVITY","COFACTOR","SUBUNIT","MUTAGENESIS OF CYS-61 AND HIS-144"]}
```

Source SHA-256: `52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
RN   [2] {ECO:0007744|PDB:8RSN}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS)
RP   IN COMPLEX WITH ZN(2+), FUNCTION AS AN HYDROLASE, CATALYTIC ACTIVITY,
RP   COFACTOR, SUBUNIT, AND MUTAGENESIS OF CYS-61 AND HIS-144.
RC   STRAIN=race 1 / IMI 141109;
RX   PubMed=39270823; DOI=10.1016/j.jbc.2024.107770;
RA   Ariza A., Liu Q., Cowieson N.P., Ahel I., Filippov D.V., Rack J.G.M.;
RT   "Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-
RT   dependent macrodomains.";
RL   J. Biol. Chem. 300:107770-107770(2024).
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 49-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-
CC         [protein] + ADP-D-ribose + H(+); Xref=Rhea:RHEA:58248, Rhea:RHEA-
CC         COMP:10208, Rhea:RHEA-COMP:15089, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29973, ChEBI:CHEBI:57967,
CC         ChEBI:CHEBI:142540; Evidence={ECO:0000269|PubMed:39270823};
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
