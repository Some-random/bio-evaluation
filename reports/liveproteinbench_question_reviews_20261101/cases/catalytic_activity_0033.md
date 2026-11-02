# catalytic_activity_0033

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — ATP + H2O = ADP + phosphate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIRFAQREYTDEEIYEILADPVREWFRGKFGTFTPPQRYAVIEIHKGENVLISSPTGSGKTLSAFLAAINELILLGKEGKLEDKIYVLYVSPLRALNNDIRRNLEEPLREIREVAHEMGYDLPEIRVAVRTSDTSSYEKQKMVKKPPHILITTPESLAIALNAPKFSERLKTVKYVIVDEVHALAENKRGTHLMLSLERLQNLAGDFVRIGLSATIHPLEEVAKFVFGFNDDGTPRSGLIVDVSFAKKTEIKVESVVGDLVYTDAATLSEALYKRLDELIEQHRTTLIFTNTRSGAERVAYHLKKKFPKYAELIEAHHSSLSRDVRLEVEEKLKKGELRCVVSSTSLELGIDIGSIDLVVLIGSPKSVNRALQRIGRAGHRLHEVSKGIILVLDRDDLVECTVLAYNARNRRLDRIKIPQNPLDVLVQHLLGMALEKVWDINEAYKLVRRAYPYHNLSFEDFMSVLRYLAGEYAGLEEKKVYAKIWLDEKEGKFGRRGKMTRAIYYMNTGTIPDEAKIEVYTLDRRFIGTVEEEFAERLMPGDIFVLAGRTYEFKKSRGNRIYVEPKEGAKPTIPAWFSEMLPLSFDLALDVQRFRKEVKELLNNPKAEQILMEKYRIDEKAAKAILGYFREQAKYSTIPDDGILLVEEVLEERRAKYFFHTLIGRRANEALSRAFAYLVSKKKRCNVGIAISDNGFMLILPREKRLSEEDIRTLFQLEDLRETLKKALDNTELLKRRFRHVANRGLLILRRYMGRKKSLSRQQLNAQTLLRLLKKNYPDFPLLKEVYREIMEDKMDIKNAELFLSWVKEGKIKIVFEQNELPSPFAFNLEIIGASDVVLMEDRRELIKQLHRKIMAMIGELE

[Multiple Choices]
A. desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)
B. ATP + H2O = ADP + phosphate + H(+)
C. a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)
D. pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)
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

> The exact sequence matches the annotated Thermococcus barophilus ATP-dependent helicase Lhr-Core protein 2, whose catalytic-activity annotation lists ATP hydrolysis to ADP and phosphate. The cited evidence code is curator inference from a publication, so this supports the key but is not itself a direct experimental measurement.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Walker A/P-loop-like ATP-binding motif (…SSPTGSGKT…), consistent with an ATPase; the ATP hydrolysis option is therefore meaningfully distinguished from the methylation, phospholipid hydrolysis, and amide hydrolysis alternatives.


**Missing item-specific fact**

> The protein-specific database annotation or publication is absent, but it is not necessary to distinguish the ATPase reaction from these alternatives.


**Reason**

> A recognizable nucleotide-binding motif in the supplied sequence, combined with the reaction choices, provides a concrete biological basis for selecting ATP hydrolysis; this is more than identifying the exact sequence from memory.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The ATPase motif supports option B, while the other choices describe chemically distinct reactions not indicated by the sequence.


### Important caveats

- The sequence match establishes applicability of the reviewer-only annotation, but the author's exact source snapshot is unknown.
- The cited UniProt catalytic-activity evidence is coded as curator inference from a publication; the primary study was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Walker A/P-loop-like ATP-binding motif (…SSPTGSGKT…), consistent with an ATPase; the ATP hydrolysis option is therefore meaningfully distinguished from the methylation, phospholipid hydrolysis, and amide hydrolysis alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The protein-specific database annotation or publication is absent, but it is not necessary to distinguish the ATPase reaction from these alternatives.",
    "reason": "A recognizable nucleotide-binding motif in the supplied sequence, combined with the reaction choices, provides a concrete biological basis for selecting ATP hydrolysis; this is more than identifying the exact sequence from memory."
  },
  "case_id": "catalytic_activity_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Thermococcus barophilus ATP-dependent helicase Lhr-Core protein 2, whose catalytic-activity annotation lists ATP hydrolysis to ADP and phosphate. The cited evidence code is curator inference from a publication, so this supports the key but is not itself a direct experimental measurement."
  },
  "important_caveats": [
    "The sequence match establishes applicability of the reviewer-only annotation, but the author's exact source snapshot is unknown.",
    "The cited UniProt catalytic-activity evidence is coded as curator inference from a publication; the primary study was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The ATPase motif supports option B, while the other choices describe chemically distinct reactions not indicated by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Thermococcus barophilus ATP-dependent helicase Lhr-Core protein 2, whose catalytic-activity annotation lists ATP hydrolysis to ADP and phosphate. The cited evidence code is curator inference from a publication, so this supports the key but is not itself a direct experimental measurement.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Walker A/P-loop-like ATP-binding motif (…SSPTGSGKT…), consistent with an ATPase; the ATP hydrolysis option is therefore meaningfully distinguished from the methylation, phospholipid hydrolysis, and amide hydrolysis alternatives.",
    "missing_item_specific_fact": "The protein-specific database annotation or publication is absent, but it is not necessary to distinguish the ATPase reaction from these alternatives.",
    "reason": "A recognizable nucleotide-binding motif in the supplied sequence, combined with the reaction choices, provides a concrete biological basis for selecting ATP hydrolysis; this is more than identifying the exact sequence from memory."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The ATPase motif supports option B, while the other choices describe chemically distinct reactions not indicated by the sequence."
  },
  "important_caveats": [
    "The sequence match establishes applicability of the reviewer-only annotation, but the author's exact source snapshot is unknown.",
    "The cited UniProt catalytic-activity evidence is coded as curator inference from a publication; the primary study was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry F0LJX3 (LHRC2_THEBM, 863 AA, sequence SHA256 matched) annotates the protein as 'ATP-dependent helicase Lhr-Core protein 2' (aLhr2) with EC 3.6.4.- and 5.6.2.-. The CATALYTIC ACTIVITY comment explicitly states 'ATP + H2O = ADP + phosphate + H(+)' (Rhea:RHEA:13065), backed by experimental evidence from PubMed:34206878 (Hajj et al., Biomolecules 2021), which documents 'FUNCTION AS HELICASE, FUNCTION AS AN ATPASE, CATALYTIC ACTIVITY.' The expected answer B matches this annotation exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable Walker A (P-loop) motif 'GSGKT' (residues ~40-44: 'SGSGKTLSAFLAAIN') and a Walker B motif with the conserved 'DE' pair ('VIVDEVHALAEN', ~residues 140-150), plus additional GxxGxGK-like elements near the C-terminus ('GKFGRRGKM'). These are hallmark motifs of P-loop NTPases, the superfamily encompassing helicases and ATPases. Among the four choices, only B (ATP hydrolysis) corresponds to a P-loop NTPase reaction. Choice A (SAM-dependent methyltransferase) requires a Rossmann-fold MTase domain; Choice C (phospholipase) requires a lipase/PLD-like fold; Choice D (amide hydrolase) requires a hydrolase catalytic triad or similar. None of these enzyme classes feature Walker A/B motifs. A knowledgeable reader can identify the P-loop architecture and eliminate A, C, and D.


**Missing item-specific fact**

> None required beyond general P-loop NTPase biochemistry. The specific protein identity (aLhr2 from Thermococcus barophilus) and its exact helicase directionality are not needed to select B over the other three choices.


**Reason**

> The Walker A/B motif identification is a well-established, general biochemical principle applicable to any sequence. It meaningfully distinguishes an NTPase (B) from a methyltransferase (A), phospholipase (C), and amide hydrolase (D), all of which belong to entirely different structural and mechanistic classes. This constitutes a concrete biological argument from the supplied sequence rather than a lookup of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Walker A/B motifs clearly indicate a P-loop NTPase. The three distractors represent fundamentally different enzyme classes (SAM-MTase, phospholipase, amide hydrolase) with incompatible structural requirements. No ambiguity exists among the choices given the sequence evidence.


### Important caveats

- The catalytic activity annotation carries evidence code ECO:0000305 (inferred by curator) referencing PubMed:34206878, while the EC numbers carry ECO:0000269 (experimental). Both trace to the same 2021 experimental paper documenting ATPase and helicase activities.
- The protein is from Thermococcus barophilus (Archaea, Thermococcales). The entry was first public in June 2025, relatively recent.
- The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence-level reasoning.
- The question asks for the catalytic reaction, not the helicase unwinding activity per se. The ATP hydrolysis reaction (B) is the fundamental chemical transformation, consistent with both EC 3.6.4.- (ATPase) and EC 5.6.2.- (helicase) annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable Walker A (P-loop) motif 'GSGKT' (residues ~40-44: 'SGSGKTLSAFLAAIN') and a Walker B motif with the conserved 'DE' pair ('VIVDEVHALAEN', ~residues 140-150), plus additional GxxGxGK-like elements near the C-terminus ('GKFGRRGKM'). These are hallmark motifs of P-loop NTPases, the superfamily encompassing helicases and ATPases. Among the four choices, only B (ATP hydrolysis) corresponds to a P-loop NTPase reaction. Choice A (SAM-dependent methyltransferase) requires a Rossmann-fold MTase domain; Choice C (phospholipase) requires a lipase/PLD-like fold; Choice D (amide hydrolase) requires a hydrolase catalytic triad or similar. None of these enzyme classes feature Walker A/B motifs. A knowledgeable reader can identify the P-loop architecture and eliminate A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required beyond general P-loop NTPase biochemistry. The specific protein identity (aLhr2 from Thermococcus barophilus) and its exact helicase directionality are not needed to select B over the other three choices.",
    "reason": "The Walker A/B motif identification is a well-established, general biochemical principle applicable to any sequence. It meaningfully distinguishes an NTPase (B) from a methyltransferase (A), phospholipase (C), and amide hydrolase (D), all of which belong to entirely different structural and mechanistic classes. This constitutes a concrete biological argument from the supplied sequence rather than a lookup of a specific database entry."
  },
  "case_id": "catalytic_activity_0033",
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
    "reason": "UniProt entry F0LJX3 (LHRC2_THEBM, 863 AA, sequence SHA256 matched) annotates the protein as 'ATP-dependent helicase Lhr-Core protein 2' (aLhr2) with EC 3.6.4.- and 5.6.2.-. The CATALYTIC ACTIVITY comment explicitly states 'ATP + H2O = ADP + phosphate + H(+)' (Rhea:RHEA:13065), backed by experimental evidence from PubMed:34206878 (Hajj et al., Biomolecules 2021), which documents 'FUNCTION AS HELICASE, FUNCTION AS AN ATPASE, CATALYTIC ACTIVITY.' The expected answer B matches this annotation exactly."
  },
  "important_caveats": [
    "The catalytic activity annotation carries evidence code ECO:0000305 (inferred by curator) referencing PubMed:34206878, while the EC numbers carry ECO:0000269 (experimental). Both trace to the same 2021 experimental paper documenting ATPase and helicase activities.",
    "The protein is from Thermococcus barophilus (Archaea, Thermococcales). The entry was first public in June 2025, relatively recent.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence-level reasoning.",
    "The question asks for the catalytic reaction, not the helicase unwinding activity per se. The ATP hydrolysis reaction (B) is the fundamental chemical transformation, consistent with both EC 3.6.4.- (ATPase) and EC 5.6.2.- (helicase) annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Walker A/B motifs clearly indicate a P-loop NTPase. The three distractors represent fundamentally different enzyme classes (SAM-MTase, phospholipase, amide hydrolase) with incompatible structural requirements. No ambiguity exists among the choices given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry F0LJX3 (LHRC2_THEBM, 863 AA, sequence SHA256 matched) annotates the protein as 'ATP-dependent helicase Lhr-Core protein 2' (aLhr2) with EC 3.6.4.- and 5.6.2.-. The CATALYTIC ACTIVITY comment explicitly states 'ATP + H2O = ADP + phosphate + H(+)' (Rhea:RHEA:13065), backed by experimental evidence from PubMed:34206878 (Hajj et al., Biomolecules 2021), which documents 'FUNCTION AS HELICASE, FUNCTION AS AN ATPASE, CATALYTIC ACTIVITY.' The expected answer B matches this annotation exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable Walker A (P-loop) motif 'GSGKT' (residues ~40-44: 'SGSGKTLSAFLAAIN') and a Walker B motif with the conserved 'DE' pair ('VIVDEVHALAEN', ~residues 140-150), plus additional GxxGxGK-like elements near the C-terminus ('GKFGRRGKM'). These are hallmark motifs of P-loop NTPases, the superfamily encompassing helicases and ATPases. Among the four choices, only B (ATP hydrolysis) corresponds to a P-loop NTPase reaction. Choice A (SAM-dependent methyltransferase) requires a Rossmann-fold MTase domain; Choice C (phospholipase) requires a lipase/PLD-like fold; Choice D (amide hydrolase) requires a hydrolase catalytic triad or similar. None of these enzyme classes feature Walker A/B motifs. A knowledgeable reader can identify the P-loop architecture and eliminate A, C, and D.",
    "missing_item_specific_fact": "None required beyond general P-loop NTPase biochemistry. The specific protein identity (aLhr2 from Thermococcus barophilus) and its exact helicase directionality are not needed to select B over the other three choices.",
    "reason": "The Walker A/B motif identification is a well-established, general biochemical principle applicable to any sequence. It meaningfully distinguishes an NTPase (B) from a methyltransferase (A), phospholipase (C), and amide hydrolase (D), all of which belong to entirely different structural and mechanistic classes. This constitutes a concrete biological argument from the supplied sequence rather than a lookup of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Walker A/B motifs clearly indicate a P-loop NTPase. The three distractors represent fundamentally different enzyme classes (SAM-MTase, phospholipase, amide hydrolase) with incompatible structural requirements. No ambiguity exists among the choices given the sequence evidence."
  },
  "important_caveats": [
    "The catalytic activity annotation carries evidence code ECO:0000305 (inferred by curator) referencing PubMed:34206878, while the EC numbers carry ECO:0000269 (experimental). Both trace to the same 2021 experimental paper documenting ATPase and helicase activities.",
    "The protein is from Thermococcus barophilus (Archaea, Thermococcales). The entry was first public in June 2025, relatively recent.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence-level reasoning.",
    "The question asks for the catalytic reaction, not the helicase unwinding activity per se. The ATP hydrolysis reaction (B) is the fundamental chemical transformation, consistent with both EC 3.6.4.- (ATPase) and EC 5.6.2.- (helicase) annotations."
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

**Accession:** `F0LJX3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 68. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F0LJX3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.455189+00:00.  

```json
"F0LJX3"
```

Source SHA-256: `6a4113943b2aa8c087b20ace63be065aa1db6311203ba80801b7e3dffa8ad7be`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F0LJX3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.455189+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Large helicase related protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"RNA:DNA 3'-5' helicase Lhr-Core"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34206878","source":"PubMed"}],"value":"3.6.4.-"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"34206878","source":"PubMed"}],"value":"5.6.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"ATP-dependent helicase Lhr-Core protein 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34206878","source":"PubMed"}],"value":"aLhr2"}]}}
```

Source SHA-256: `6a4113943b2aa8c087b20ace63be065aa1db6311203ba80801b7e3dffa8ad7be`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F0LJX3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.455189+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"34206878","source":"PubMed"}],"name":"ATP + H2O = ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13065"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `6a4113943b2aa8c087b20ace63be065aa1db6311203ba80801b7e3dffa8ad7be`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F0LJX3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.455189+00:00.  

```json
{"citation":{"authors":["Hajj M.","Langendijk-Genevaux P.","Batista M.","Quentin Y.","Laurent S.","Capeyrou R.","Abdel-Razzak Z.","Flament D.","Chamieh H.","Fichant G.","Clouet-d'Orval B.","Bouvier M."],"citationCrossReferences":[{"database":"PubMed","id":"34206878"},{"database":"DOI","id":"10.3390/biom11070950"}],"citationType":"journal article","firstPage":"0","id":"34206878","journal":"Biomolecules","lastPage":"0","publicationDate":"2021","title":"Phylogenetic Diversity of Lhr Proteins and Biochemical Activities of the Thermococcales aLhr2 DNA/RNA Helicase.","volume":"11"},"referenceComments":[{"type":"STRAIN","value":"DSM 11836 / MP"}],"referenceNumber":2,"referencePositions":["FUNCTION AS HELICASE","FUNCTION AS AN ATPASE","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN","DNA-BINDING","RNA-BINDING","MUTAGENESIS OF THR-215; ILE-512 AND TRP-577"]}
```

Source SHA-256: `6a4113943b2aa8c087b20ace63be065aa1db6311203ba80801b7e3dffa8ad7be`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F0LJX3?format=txt&versions=68)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:28:16.649290+00:00.  

```text
ID   LHRC2_THEBM             Reviewed;         863 AA.
AC   F0LJX3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2011, sequence version 1.
DT   28-JAN-2026, entry version 68.
DE   RecName: Full=ATP-dependent helicase Lhr-Core protein 2 {ECO:0000305};
DE            Short=aLhr2 {ECO:0000303|PubMed:34206878};
DE            EC=3.6.4.- {ECO:0000269|PubMed:34206878};
DE            EC=5.6.2.- {ECO:0000269|PubMed:34206878};
DE   AltName: Full=Large helicase related protein;
DE   AltName: Full=RNA:DNA 3'-5' helicase Lhr-Core {ECO:0000305};
GN   Name=alhr2 {ECO:0000303|PubMed:34206878};
GN   OrderedLocusNames=TERMP_00533 {ECO:0000312|EMBL:ADT83510.1};
OS   Thermococcus barophilus (strain DSM 11836 / MP).
OC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;
OC   Thermococcaceae; Thermococcus.
OX   NCBI_TaxID=391623;
```

Source SHA-256: `e876dcee6e7fcdc31d12b5dda92d74b1267f580bc364a89c7899b1f1e2ba416b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F0LJX3?format=txt&versions=68)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:28:16.649290+00:00.  

```text
DE   RecName: Full=ATP-dependent helicase Lhr-Core protein 2 {ECO:0000305};
DE            Short=aLhr2 {ECO:0000303|PubMed:34206878};
DE            EC=3.6.4.- {ECO:0000269|PubMed:34206878};
DE            EC=5.6.2.- {ECO:0000269|PubMed:34206878};
DE   AltName: Full=Large helicase related protein;
DE   AltName: Full=RNA:DNA 3'-5' helicase Lhr-Core {ECO:0000305};
```

Source SHA-256: `e876dcee6e7fcdc31d12b5dda92d74b1267f580bc364a89c7899b1f1e2ba416b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F0LJX3?format=txt&versions=68)  
**Locator:** `lines 26-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:28:16.649290+00:00.  

```text
RN   [2]
RP   FUNCTION AS HELICASE, FUNCTION AS AN ATPASE, CATALYTIC ACTIVITY, ACTIVITY
RP   REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, DOMAIN, DNA-BINDING,
RP   RNA-BINDING, AND MUTAGENESIS OF THR-215; ILE-512 AND TRP-577.
RC   STRAIN=DSM 11836 / MP;
RX   PubMed=34206878; DOI=10.3390/biom11070950;
RA   Hajj M., Langendijk-Genevaux P., Batista M., Quentin Y., Laurent S.,
RA   Capeyrou R., Abdel-Razzak Z., Flament D., Chamieh H., Fichant G.,
RA   Clouet-d'Orval B., Bouvier M.;
RT   "Phylogenetic Diversity of Lhr Proteins and Biochemical Activities of the
RT   Thermococcales aLhr2 DNA/RNA Helicase.";
RL   Biomolecules 11:0-0(2021).
```

Source SHA-256: `e876dcee6e7fcdc31d12b5dda92d74b1267f580bc364a89c7899b1f1e2ba416b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F0LJX3?format=txt&versions=68)  
**Locator:** `lines 49-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 68 / 1.  
**Retrieved:** 2026-11-02T04:28:16.649290+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP + H2O = ADP + phosphate + H(+); Xref=Rhea:RHEA:13065,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000305|PubMed:34206878};
```

Source SHA-256: `e876dcee6e7fcdc31d12b5dda92d74b1267f580bc364a89c7899b1f1e2ba416b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
