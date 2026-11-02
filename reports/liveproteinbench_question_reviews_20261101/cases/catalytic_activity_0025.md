# catalytic_activity_0025

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGRNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAINSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPESYSNFFGVAYDTPPKAHALKASRLLVPTTVARPSKPVRVFASTADPGTTTADQVYKVGHNLLLAHAAAIQVYRDKFQNTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQLLGPRLREFTPDQKKLLIGSYDYVGVNYYTATYVSSAQPPHDKKKAVFHTDGNFYTTDSKDGVLIGPLAGPAWLNIVPEGIYHVLHDIKENYEDPVIYITENGVYEVNDTAKTLSEARVDTTRLHYLQDHLSKVLEARHQGVRVQGYLVWSLMDNWELRAGYTSRFGLIHVDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKARPQEDDGAFDTPRKRLRKY

[Multiple Choices]
A. adenosine(in) + H(+)(in) = adenosine(out) + H(+)(out)
B. deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose
C. Co(2+)(in) = Co(2+)(out)
D. 3-desmethyl okaramine B + S-adenosyl-L-methionine = okaramine B + S-adenosyl-L-homocysteine + H(+)
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

> The exact 543-aa sequence matches the UniProt entry annotated with the reaction in choice B. That catalytic-activity annotation cites ECO:0000269 (PubMed 18927081), indicating experimental evidence; the historical matched entry reports the same reaction. The primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The soluble sequence and its TENG motif are consistent with a glycoside hydrolase, favoring hydrolysis over the transport and methyl-transfer alternatives. That supports the broad reaction class, not the specific deacetylipecoside substrate and products.


**Missing item-specific fact**

> The sequence alone does not establish that this particular enzyme hydrolyzes deacetylipecoside to the named aglycone and D-glucose; that substrate-specific activity requires an item-specific annotation or experimental result.


**Reason**

> The choices make a broad enzyme-class inference plausible, but the question asks for a specific chemical reaction. Identifying the exact substrate-specific reaction depends on information not supplied with the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports choice B; no other listed reaction is supported for this sequence.


### Important caveats

- The supporting UniProt record is a reviewer-only source, not information available in the original question.
- The database annotation cites experimental evidence, but the cited primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The soluble sequence and its TENG motif are consistent with a glycoside hydrolase, favoring hydrolysis over the transport and methyl-transfer alternatives. That supports the broad reaction class, not the specific deacetylipecoside substrate and products.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence alone does not establish that this particular enzyme hydrolyzes deacetylipecoside to the named aglycone and D-glucose; that substrate-specific activity requires an item-specific annotation or experimental result.",
    "reason": "The choices make a broad enzyme-class inference plausible, but the question asks for a specific chemical reaction. Identifying the exact substrate-specific reaction depends on information not supplied with the sequence."
  },
  "case_id": "catalytic_activity_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 543-aa sequence matches the UniProt entry annotated with the reaction in choice B. That catalytic-activity annotation cites ECO:0000269 (PubMed 18927081), indicating experimental evidence; the historical matched entry reports the same reaction. The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The supporting UniProt record is a reviewer-only source, not information available in the original question.",
    "The database annotation cites experimental evidence, but the cited primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports choice B; no other listed reaction is supported for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 543-aa sequence matches the UniProt entry annotated with the reaction in choice B. That catalytic-activity annotation cites ECO:0000269 (PubMed 18927081), indicating experimental evidence; the historical matched entry reports the same reaction. The primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The soluble sequence and its TENG motif are consistent with a glycoside hydrolase, favoring hydrolysis over the transport and methyl-transfer alternatives. That supports the broad reaction class, not the specific deacetylipecoside substrate and products.",
    "missing_item_specific_fact": "The sequence alone does not establish that this particular enzyme hydrolyzes deacetylipecoside to the named aglycone and D-glucose; that substrate-specific activity requires an item-specific annotation or experimental result.",
    "reason": "The choices make a broad enzyme-class inference plausible, but the question asks for a specific chemical reaction. Identifying the exact substrate-specific reaction depends on information not supplied with the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports choice B; no other listed reaction is supported for this sequence."
  },
  "important_caveats": [
    "The supporting UniProt record is a reviewer-only source, not information available in the original question.",
    "The database annotation cites experimental evidence, but the cited primary study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B6ZKM4 (Ipecac alkaloid beta-glucosidase 2, IpeGLU2) carries the catalytic activity annotation 'deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose' with evidence code ECO:0000269 (inferred from direct assay) from PubMed:18927081 (Nomura et al., J. Biol. Chem. 2008). The benchmark sequence matches the canonical 543-aa entry exactly. The EC classification 3.2.1.- (glycosidase) is consistent with the reaction. The expected answer B is directly and experimentally supported.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of glycoside hydrolase family 3 (GH3): the WDT motif ('IWDTFTHTHPE'), the NEP acid/base motif ('WITINEPESYSN'), and the GHN motif ('VYKVGHNLLLAHAAAIQVY'). These are well-established diagnostic features of GH3 beta-glucosidases in the biochemistry literature. A model recognizing these motifs can conclude the enzyme is a glycosidase. Among the four choices, only B represents a glycosidase reaction (hydrolysis of a β-glucosidic bond releasing D-glucose). Choices A and C are transporter reactions (adenosine and Co²⁺ translocation), and D is a SAM-dependent methyltransferase reaction. Identifying the enzyme family from sequence motifs is sufficient to select B without knowing the protein's exact identity or its specific natural substrate name.


**Missing item-specific fact**

> None critical. The specific substrate name 'deacetylipecoside' is not derivable from sequence alone, but it is not needed to distinguish B from the other three choices, which belong to entirely different enzyme classes (transporter, transporter, methyltransferase).


**Reason**

> The question provides a 543-aa sequence containing recognizable GH3 catalytic motifs. General knowledge of glycosidase family signatures allows identification of the enzyme as a glycoside hydrolase, which uniquely matches choice B among the four options spanning transport, glycosidase, and methyltransferase classes. No protein-specific database lookup is required to make the correct selection.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent three distinct enzyme classes (two transporters, one glycosidase, one methyltransferase). Once the enzyme is identified as a glycosidase from sequence motifs, only B is consistent. The distractors are from clearly different functional categories and are not defensible alternatives.


### Important caveats

- The UniProt Swiss-Prot entry B6ZKM4 was only integrated on 2025-06-18, though the underlying experimental evidence dates to 2008 (PubMed:18927081). The annotation uses ECO:0000269 (direct assay), indicating experimental validation rather than computational inference.
- The enzyme also catalyzes a second reaction (deacetylisoipecoside hydrolysis, C6/H5), but this is not among the choices and does not create ambiguity.
- The EC number is listed as 3.2.1.- (incomplete), reflecting that the enzyme's precise EC subclassification was not finalized at annotation time.
- The specific substrate 'deacetylipecoside' is a terpenoid-isoquinoline alkaloid glucoside specific to Ipecac biosynthesis; this specificity is not inferable from sequence motifs alone, but is unnecessary for selecting the correct answer among the given options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of glycoside hydrolase family 3 (GH3): the WDT motif ('IWDTFTHTHPE'), the NEP acid/base motif ('WITINEPESYSN'), and the GHN motif ('VYKVGHNLLLAHAAAIQVY'). These are well-established diagnostic features of GH3 beta-glucosidases in the biochemistry literature. A model recognizing these motifs can conclude the enzyme is a glycosidase. Among the four choices, only B represents a glycosidase reaction (hydrolysis of a β-glucosidic bond releasing D-glucose). Choices A and C are transporter reactions (adenosine and Co²⁺ translocation), and D is a SAM-dependent methyltransferase reaction. Identifying the enzyme family from sequence motifs is sufficient to select B without knowing the protein's exact identity or its specific natural substrate name.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific substrate name 'deacetylipecoside' is not derivable from sequence alone, but it is not needed to distinguish B from the other three choices, which belong to entirely different enzyme classes (transporter, transporter, methyltransferase).",
    "reason": "The question provides a 543-aa sequence containing recognizable GH3 catalytic motifs. General knowledge of glycosidase family signatures allows identification of the enzyme as a glycoside hydrolase, which uniquely matches choice B among the four options spanning transport, glycosidase, and methyltransferase classes. No protein-specific database lookup is required to make the correct selection."
  },
  "case_id": "catalytic_activity_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKM4 (Ipecac alkaloid beta-glucosidase 2, IpeGLU2) carries the catalytic activity annotation 'deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose' with evidence code ECO:0000269 (inferred from direct assay) from PubMed:18927081 (Nomura et al., J. Biol. Chem. 2008). The benchmark sequence matches the canonical 543-aa entry exactly. The EC classification 3.2.1.- (glycosidase) is consistent with the reaction. The expected answer B is directly and experimentally supported."
  },
  "important_caveats": [
    "The UniProt Swiss-Prot entry B6ZKM4 was only integrated on 2025-06-18, though the underlying experimental evidence dates to 2008 (PubMed:18927081). The annotation uses ECO:0000269 (direct assay), indicating experimental validation rather than computational inference.",
    "The enzyme also catalyzes a second reaction (deacetylisoipecoside hydrolysis, C6/H5), but this is not among the choices and does not create ambiguity.",
    "The EC number is listed as 3.2.1.- (incomplete), reflecting that the enzyme's precise EC subclassification was not finalized at annotation time.",
    "The specific substrate 'deacetylipecoside' is a terpenoid-isoquinoline alkaloid glucoside specific to Ipecac biosynthesis; this specificity is not inferable from sequence motifs alone, but is unnecessary for selecting the correct answer among the given options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent three distinct enzyme classes (two transporters, one glycosidase, one methyltransferase). Once the enzyme is identified as a glycosidase from sequence motifs, only B is consistent. The distractors are from clearly different functional categories and are not defensible alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKM4 (Ipecac alkaloid beta-glucosidase 2, IpeGLU2) carries the catalytic activity annotation 'deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose' with evidence code ECO:0000269 (inferred from direct assay) from PubMed:18927081 (Nomura et al., J. Biol. Chem. 2008). The benchmark sequence matches the canonical 543-aa entry exactly. The EC classification 3.2.1.- (glycosidase) is consistent with the reaction. The expected answer B is directly and experimentally supported.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of glycoside hydrolase family 3 (GH3): the WDT motif ('IWDTFTHTHPE'), the NEP acid/base motif ('WITINEPESYSN'), and the GHN motif ('VYKVGHNLLLAHAAAIQVY'). These are well-established diagnostic features of GH3 beta-glucosidases in the biochemistry literature. A model recognizing these motifs can conclude the enzyme is a glycosidase. Among the four choices, only B represents a glycosidase reaction (hydrolysis of a β-glucosidic bond releasing D-glucose). Choices A and C are transporter reactions (adenosine and Co²⁺ translocation), and D is a SAM-dependent methyltransferase reaction. Identifying the enzyme family from sequence motifs is sufficient to select B without knowing the protein's exact identity or its specific natural substrate name.",
    "missing_item_specific_fact": "None critical. The specific substrate name 'deacetylipecoside' is not derivable from sequence alone, but it is not needed to distinguish B from the other three choices, which belong to entirely different enzyme classes (transporter, transporter, methyltransferase).",
    "reason": "The question provides a 543-aa sequence containing recognizable GH3 catalytic motifs. General knowledge of glycosidase family signatures allows identification of the enzyme as a glycoside hydrolase, which uniquely matches choice B among the four options spanning transport, glycosidase, and methyltransferase classes. No protein-specific database lookup is required to make the correct selection."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent three distinct enzyme classes (two transporters, one glycosidase, one methyltransferase). Once the enzyme is identified as a glycosidase from sequence motifs, only B is consistent. The distractors are from clearly different functional categories and are not defensible alternatives."
  },
  "important_caveats": [
    "The UniProt Swiss-Prot entry B6ZKM4 was only integrated on 2025-06-18, though the underlying experimental evidence dates to 2008 (PubMed:18927081). The annotation uses ECO:0000269 (direct assay), indicating experimental validation rather than computational inference.",
    "The enzyme also catalyzes a second reaction (deacetylisoipecoside hydrolysis, C6/H5), but this is not among the choices and does not create ambiguity.",
    "The EC number is listed as 3.2.1.- (incomplete), reflecting that the enzyme's precise EC subclassification was not finalized at annotation time.",
    "The specific substrate 'deacetylipecoside' is a terpenoid-isoquinoline alkaloid glucoside specific to Ipecac biosynthesis; this specificity is not inferable from sequence motifs alone, but is unnecessary for selecting the correct answer among the given options."
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

**Accession:** `B6ZKM4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 44. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.131375+00:00.  

```json
"B6ZKM4"
```

Source SHA-256: `354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.131375+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"3.2.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Ipecac alkaloid beta-glucosidase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"IpeGLU2"}]}}
```

Source SHA-256: `354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.131375+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:78764"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"name":"deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78763"},{"database":"ChEBI","id":"CHEBI:4167"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:58379"},{"database":"ChEBI","id":"CHEBI:229554"}]}}
```

Source SHA-256: `354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.131375+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:78888"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"name":"deacetylisoipecoside + H2O = deacetylisoipecoside aglycone + D-glucose","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78887"},{"database":"ChEBI","id":"CHEBI:4167"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:58091"},{"database":"ChEBI","id":"CHEBI:229557"}]}}
```

Source SHA-256: `354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.131375+00:00.  

```json
{"citation":{"authors":["Nomura T.","Quesada A.L.","Kutchan T.M."],"citationCrossReferences":[{"database":"PubMed","id":"18927081"},{"database":"DOI","id":"10.1074/jbc.m806953200"}],"citationType":"journal article","firstPage":"34650","id":"18927081","journal":"J. Biol. Chem.","lastPage":"34659","publicationDate":"2008","title":"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.","volume":"283"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAH02545.1","source":"EMBL"}],"referenceComments":[{"type":"TISSUE","value":"Root"},{"type":"TISSUE","value":"Shoot"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-01T06:27:55.242337+00:00.  

```text
ID   GLU2_CARIP              Reviewed;         543 AA.
AC   B6ZKM4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-FEB-2009, sequence version 1.
DT   28-JAN-2026, entry version 44.
DE   RecName: Full=Ipecac alkaloid beta-glucosidase 2 {ECO:0000303|PubMed:18927081};
DE            Short=IpeGLU2 {ECO:0000303|PubMed:18927081};
DE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};
GN   Name=GLU2 {ECO:0000303|PubMed:18927081};
OS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;
OC   Carapichea.
OX   NCBI_TaxID=77880;
```

Source SHA-256: `dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-01T06:27:55.242337+00:00.  

```text
DE   RecName: Full=Ipecac alkaloid beta-glucosidase 2 {ECO:0000303|PubMed:18927081};
DE            Short=IpeGLU2 {ECO:0000303|PubMed:18927081};
DE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};
```

Source SHA-256: `dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)  
**Locator:** `lines 27-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-01T06:27:55.242337+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=deacetylipecoside + H2O = deacetylipecoside aglycone + D-
CC         glucose; Xref=Rhea:RHEA:78763, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:58379, ChEBI:CHEBI:229554;
CC         Evidence={ECO:0000269|PubMed:18927081};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78764;
CC         Evidence={ECO:0000269|PubMed:18927081};
```

Source SHA-256: `dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-01T06:27:55.242337+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=deacetylisoipecoside + H2O = deacetylisoipecoside aglycone +
CC         D-glucose; Xref=Rhea:RHEA:78887, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:58091, ChEBI:CHEBI:229557;
CC         Evidence={ECO:0000269|PubMed:18927081};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78888;
CC         Evidence={ECO:0000269|PubMed:18927081};
```

Source SHA-256: `dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
