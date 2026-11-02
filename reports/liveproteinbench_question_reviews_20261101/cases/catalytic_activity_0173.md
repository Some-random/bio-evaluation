# catalytic_activity_0173

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — 2 a 1,2-diacyl-sn-glycero-3-phospho-(1&#x27;-sn-glycerol) = a cardiolipin + glycerol

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTFNGRFRATLRGINIRNASMTSLSLTGSHAQKQTVLGSTPGALGTIPTVALNGVNPLPRYRHNLLFGTLSFGDRWDRIQRRLAVLGRASTGNVVVPFSDSADAFRRMWESVDSASDSVLWQTYICKDDFVGQKTVKKLEEAHRRGCKTELLYDCGGNITGRRRLVGDLKKSGANVIEHRPMWEHFFPYFLRGMKWELSPGIRNHRKILIVDNKLGFCGGLNIGDEYCGTSEGGNGRFRDTHCVVMGPAVMHMREVYEDTKAPKPWKWSLARWRQIASATMNLRYLEGMNVKHDYLEPTTTFVRQGGGVYLRRQMERAERSTVRMMERMRWKRQRERLNRCLLTLAKNLREGQGLVFKAATGKGDDVATTDAGSKRNNEVSHGQWKLMKRRIDEYRQRAIKNAEESFFRRLRVVNPSMRLLEDTSPVAEAEAYGQAHAAVTQVLSCNPHSRDWSIPYAFWQVSKFVHQRLWVTTPYYMPHRKLMRALQLAARRGVDVRILAGSNRTTDPWFMWYASNYITGMLMASGVRVYEYKGGQVMHAKTVVADSIWTSIGSYNWDMMSNKNMEICVCHLDHNLALTMEKQFLDDMNVSEEVNYEEYQRRSLWLRFSSWFFYTALRIAEKFTFRTFWDPDLSSEID

[Multiple Choices]
A. 2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol
B. L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)
C. norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-L-homocysteine + H(+)
D. restrictinol + glycine + H(+) = restricticin + H2O
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

> The exact sequence matches the UniProt entry for Trypanosoma brucei cardiolipin synthetase, whose curated catalytic-activity annotation gives choice A. That annotation cites a 2012 paper, but the supplied excerpts do not independently establish the experimental details.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices name distinct, specific enzyme reactions; the sequence and prompt provide no biological context or sufficiently distinctive evidence to identify this particular reaction by general reasoning alone.


**Missing item-specific fact**

> The sequence-specific identity or functional annotation linking this protein to cardiolipin synthetase and its cardiolipin-forming reaction.


**Reason**

> The reviewer-only annotation supports the key, but that protein-specific identity and reaction are absent from the evaluated input. Recognizing the sequence from a database would be lookup or memorization, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe different reactions, and the sequence-matched curated annotation specifically corresponds to A. The limitation is lack of supplied grounds to distinguish them, not evidence that multiple choices describe the same activity.


### Important caveats

- The UniProt annotation is curator-assigned and cites a publication; the excerpts do not include primary experimental results for independent assessment.
- The reviewer-only accession and annotation were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices name distinct, specific enzyme reactions; the sequence and prompt provide no biological context or sufficiently distinctive evidence to identify this particular reaction by general reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific identity or functional annotation linking this protein to cardiolipin synthetase and its cardiolipin-forming reaction.",
    "reason": "The reviewer-only annotation supports the key, but that protein-specific identity and reaction are absent from the evaluated input. Recognizing the sequence from a database would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Trypanosoma brucei cardiolipin synthetase, whose curated catalytic-activity annotation gives choice A. That annotation cites a 2012 paper, but the supplied excerpts do not independently establish the experimental details."
  },
  "important_caveats": [
    "The UniProt annotation is curator-assigned and cites a publication; the excerpts do not include primary experimental results for independent assessment.",
    "The reviewer-only accession and annotation were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe different reactions, and the sequence-matched curated annotation specifically corresponds to A. The limitation is lack of supplied grounds to distinguish them, not evidence that multiple choices describe the same activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Trypanosoma brucei cardiolipin synthetase, whose curated catalytic-activity annotation gives choice A. That annotation cites a 2012 paper, but the supplied excerpts do not independently establish the experimental details.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices name distinct, specific enzyme reactions; the sequence and prompt provide no biological context or sufficiently distinctive evidence to identify this particular reaction by general reasoning alone.",
    "missing_item_specific_fact": "The sequence-specific identity or functional annotation linking this protein to cardiolipin synthetase and its cardiolipin-forming reaction.",
    "reason": "The reviewer-only annotation supports the key, but that protein-specific identity and reaction are absent from the evaluated input. Recognizing the sequence from a database would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe different reactions, and the sequence-matched curated annotation specifically corresponds to A. The limitation is lack of supplied grounds to distinguish them, not evidence that multiple choices describe the same activity."
  },
  "important_caveats": [
    "The UniProt annotation is curator-assigned and cites a publication; the excerpts do not include primary experimental results for independent assessment.",
    "The reviewer-only accession and annotation were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches UniProt Q584D1 (CLS_TRYB2, 639 AA, Trypanosoma brucei brucei) by SHA-256. The Swiss-Prot reviewed entry annotates it as Cardiolipin synthetase (EC 2.7.8.-) with the exact catalytic reaction '2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol' (Rhea:RHEA:31451), supported by ECO:0000305 from PubMed:22451910 (Serricchio & Buetikofer, PNAS 2012), a paper that experimentally characterized this enzyme's cardiolipin-synthase function. The historical (entry v102) and current (v104) records both confirm the same annotation and sequence match.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable DRD-like motif ('GDRWDR' within 'TLSFGDRWDRIQRRLAVL'), a hallmark of the CDP-alcohol phosphatidyltransferase superfamily, which catalyzes phospholipid transfer and synthesis reactions. Among the four choices, only A describes a phospholipid condensation reaction (two phosphatidylglycerol molecules → cardiolipin + glycerol). The other three options belong to entirely different enzyme classes: B is a GNAT-fold lysine acetyltransferase reaction, C is a SAM-dependent methyltransferase reaction on an alkaloid substrate, and D is a non-ribosomal peptide-synthetase-style amide bond formation. The DRD motif and the phospholipid-chemistry context of choice A are distinguishable from the other three through general enzymology and membrane-protein biochemistry knowledge.


**Missing item-specific fact**

> None that is strictly required. Identifying the DRD motif and associating it with the CDP-alcohol phosphatidyltransferase superfamily is general biochemical knowledge, not a protein-specific database lookup.


**Reason**

> A model familiar with the DRD/DRDxxG motif of CDP-alcohol phosphatidyltransferases can scan the sequence, note the motif, infer a phospholipid-transfer/synthesis function, and eliminate the three non-phospholipid choices (acetyltransferase, methyltransferase, peptide ligase). This is a concrete, general-knowledge reasoning chain rather than a single-protein database recall.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four unrelated enzyme classes (phospholipid synthase, protein acetyltransferase, alkaloid methyltransferase, peptide ligase). The sequence's DRD motif and hydrophobic transmembrane segments clearly point to a membrane phospholipid-transfer enzyme, leaving no viable alternative among the distractors.


### Important caveats

- The annotation evidence code ECO:0000305 (inferred from direct assay / curator inference from published paper) references a 2012 PNAS study that experimentally demonstrated cardiolipin-synthase activity; the annotation is not purely computational.
- The DRD motif in this sequence reads 'GDRWDR' rather than the textbook-perfect 'DRDxxG'; a model must tolerate this variant to make the superfamily assignment.
- All UniProt evidence is reviewer-only and was absent from the evaluated model input; the reasoning argument relies on general biochemical knowledge of the DRD motif, not on access to the database entry.
- The EC number is listed as 2.7.8.- (unspecified sub-subclass), so the annotation does not pin down a single EC sub-subclass, but the Rhea reaction and PubMed reference do specify the exact transformation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable DRD-like motif ('GDRWDR' within 'TLSFGDRWDRIQRRLAVL'), a hallmark of the CDP-alcohol phosphatidyltransferase superfamily, which catalyzes phospholipid transfer and synthesis reactions. Among the four choices, only A describes a phospholipid condensation reaction (two phosphatidylglycerol molecules → cardiolipin + glycerol). The other three options belong to entirely different enzyme classes: B is a GNAT-fold lysine acetyltransferase reaction, C is a SAM-dependent methyltransferase reaction on an alkaloid substrate, and D is a non-ribosomal peptide-synthetase-style amide bond formation. The DRD motif and the phospholipid-chemistry context of choice A are distinguishable from the other three through general enzymology and membrane-protein biochemistry knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is strictly required. Identifying the DRD motif and associating it with the CDP-alcohol phosphatidyltransferase superfamily is general biochemical knowledge, not a protein-specific database lookup.",
    "reason": "A model familiar with the DRD/DRDxxG motif of CDP-alcohol phosphatidyltransferases can scan the sequence, note the motif, infer a phospholipid-transfer/synthesis function, and eliminate the three non-phospholipid choices (acetyltransferase, methyltransferase, peptide ligase). This is a concrete, general-knowledge reasoning chain rather than a single-protein database recall."
  },
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt Q584D1 (CLS_TRYB2, 639 AA, Trypanosoma brucei brucei) by SHA-256. The Swiss-Prot reviewed entry annotates it as Cardiolipin synthetase (EC 2.7.8.-) with the exact catalytic reaction '2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol' (Rhea:RHEA:31451), supported by ECO:0000305 from PubMed:22451910 (Serricchio & Buetikofer, PNAS 2012), a paper that experimentally characterized this enzyme's cardiolipin-synthase function. The historical (entry v102) and current (v104) records both confirm the same annotation and sequence match."
  },
  "important_caveats": [
    "The annotation evidence code ECO:0000305 (inferred from direct assay / curator inference from published paper) references a 2012 PNAS study that experimentally demonstrated cardiolipin-synthase activity; the annotation is not purely computational.",
    "The DRD motif in this sequence reads 'GDRWDR' rather than the textbook-perfect 'DRDxxG'; a model must tolerate this variant to make the superfamily assignment.",
    "All UniProt evidence is reviewer-only and was absent from the evaluated model input; the reasoning argument relies on general biochemical knowledge of the DRD motif, not on access to the database entry.",
    "The EC number is listed as 2.7.8.- (unspecified sub-subclass), so the annotation does not pin down a single EC sub-subclass, but the Rhea reaction and PubMed reference do specify the exact transformation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four unrelated enzyme classes (phospholipid synthase, protein acetyltransferase, alkaloid methyltransferase, peptide ligase). The sequence's DRD motif and hydrophobic transmembrane segments clearly point to a membrane phospholipid-transfer enzyme, leaving no viable alternative among the distractors."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt Q584D1 (CLS_TRYB2, 639 AA, Trypanosoma brucei brucei) by SHA-256. The Swiss-Prot reviewed entry annotates it as Cardiolipin synthetase (EC 2.7.8.-) with the exact catalytic reaction '2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol' (Rhea:RHEA:31451), supported by ECO:0000305 from PubMed:22451910 (Serricchio & Buetikofer, PNAS 2012), a paper that experimentally characterized this enzyme's cardiolipin-synthase function. The historical (entry v102) and current (v104) records both confirm the same annotation and sequence match.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable DRD-like motif ('GDRWDR' within 'TLSFGDRWDRIQRRLAVL'), a hallmark of the CDP-alcohol phosphatidyltransferase superfamily, which catalyzes phospholipid transfer and synthesis reactions. Among the four choices, only A describes a phospholipid condensation reaction (two phosphatidylglycerol molecules → cardiolipin + glycerol). The other three options belong to entirely different enzyme classes: B is a GNAT-fold lysine acetyltransferase reaction, C is a SAM-dependent methyltransferase reaction on an alkaloid substrate, and D is a non-ribosomal peptide-synthetase-style amide bond formation. The DRD motif and the phospholipid-chemistry context of choice A are distinguishable from the other three through general enzymology and membrane-protein biochemistry knowledge.",
    "missing_item_specific_fact": "None that is strictly required. Identifying the DRD motif and associating it with the CDP-alcohol phosphatidyltransferase superfamily is general biochemical knowledge, not a protein-specific database lookup.",
    "reason": "A model familiar with the DRD/DRDxxG motif of CDP-alcohol phosphatidyltransferases can scan the sequence, note the motif, infer a phospholipid-transfer/synthesis function, and eliminate the three non-phospholipid choices (acetyltransferase, methyltransferase, peptide ligase). This is a concrete, general-knowledge reasoning chain rather than a single-protein database recall."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four unrelated enzyme classes (phospholipid synthase, protein acetyltransferase, alkaloid methyltransferase, peptide ligase). The sequence's DRD motif and hydrophobic transmembrane segments clearly point to a membrane phospholipid-transfer enzyme, leaving no viable alternative among the distractors."
  },
  "important_caveats": [
    "The annotation evidence code ECO:0000305 (inferred from direct assay / curator inference from published paper) references a 2012 PNAS study that experimentally demonstrated cardiolipin-synthase activity; the annotation is not purely computational.",
    "The DRD motif in this sequence reads 'GDRWDR' rather than the textbook-perfect 'DRDxxG'; a model must tolerate this variant to make the superfamily assignment.",
    "All UniProt evidence is reviewer-only and was absent from the evaluated model input; the reasoning argument relies on general biochemical knowledge of the DRD motif, not on access to the database entry.",
    "The EC number is listed as 2.7.8.- (unspecified sub-subclass), so the annotation does not pin down a single EC sub-subclass, but the Rhea reaction and PubMed reference do specify the exact transformation."
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

**Accession:** `Q584D1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 102. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
"Q584D1"
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"22451910","source":"PubMed"}],"value":"2.7.8.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cardiolipin synthetase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"CL synthase"}]}}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"22451910","source":"PubMed"}],"name":"2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:31451"},{"database":"ChEBI","id":"CHEBI:17754"},{"database":"ChEBI","id":"CHEBI:62237"},{"database":"ChEBI","id":"CHEBI:64716"}]}}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"citation":{"authors":["Serricchio M.","Buetikofer P."],"citationCrossReferences":[{"database":"PubMed","id":"22451910"},{"database":"DOI","id":"10.1073/pnas.1121528109"}],"citationType":"journal article","firstPage":"E954","id":"22451910","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"E961","publicationDate":"2012","title":"An essential bacterial-type cardiolipin synthase mediates cardiolipin formation in a eukaryote.","volume":"109"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBUNIT","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
ID   CLS_TRYB2               Reviewed;         639 AA.
AC   Q584D1; D6XFJ2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-MAY-2005, sequence version 1.
DT   28-JAN-2026, entry version 102.
DE   RecName: Full=Cardiolipin synthetase {ECO:0000305};
DE            Short=CL synthase {ECO:0000305};
DE            EC=2.7.8.- {ECO:0000305|PubMed:22451910};
DE   Flags: Precursor;
GN   Name=CLS {ECO:0000303|PubMed:22451910};
GN   ORFNames=Tb04.1H19.1130 {ECO:0000312|EMBL:AAZ10847.1},
GN   Tb927.4.2560 {ECO:0000312|EMBL:AAX79074.1};
OS   Trypanosoma brucei brucei (strain 927/4 GUTat10.1).
OC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;
OC   Trypanosomatida; Trypanosomatidae; Trypanosoma.
OX   NCBI_TaxID=185431 {ECO:0000312|Proteomes:UP000008524};
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
DE   RecName: Full=Cardiolipin synthetase {ECO:0000305};
DE            Short=CL synthase {ECO:0000305};
DE            EC=2.7.8.- {ECO:0000305|PubMed:22451910};
DE   Flags: Precursor;
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 65-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, SUBUNIT, SUBCELLULAR LOCATION, AND DISRUPTION
RP   PHENOTYPE.
RX   PubMed=22451910; DOI=10.1073/pnas.1121528109;
RA   Serricchio M., Buetikofer P.;
RT   "An essential bacterial-type cardiolipin synthase mediates cardiolipin
RT   formation in a eukaryote.";
RL   Proc. Natl. Acad. Sci. U.S.A. 109:E954-E961(2012).
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 88-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a
CC         cardiolipin + glycerol; Xref=Rhea:RHEA:31451, ChEBI:CHEBI:17754,
CC         ChEBI:CHEBI:62237, ChEBI:CHEBI:64716;
CC         Evidence={ECO:0000305|PubMed:22451910};
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 173. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
