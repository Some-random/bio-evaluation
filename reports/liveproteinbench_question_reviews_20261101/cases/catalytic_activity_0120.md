# catalytic_activity_0120

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3&#x27;-5&#x27; direction.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTNGADPLGRFSALTREWFTTAFAAPTPAQADAWSAISEGNNTLVIAPTGSGKTLAAFLWAIDRLADPAREPSQGTQVLYVSPLKALAVDVERNLRTPLTGITRVAERHGLPAPSITVGVRSGDTPPNQRRAMIANPPDVLITTPESLFLMLTSAARETLTSVRTVIVDEVHAVAATKRGAHLALSLERLDQLLDTPAQRIGLSATVRPPEEVARFLSGQAPTTIVCPPAAKTFDLSVQVPVPDMANLDNNSIWPDVEERIVDLVEAHNSSIVFANSRRLAERLTSRLNEIHAERSGIELPAGPNPEVGGGAPAHLMGSGQANGAPPLLARAHHGSVSKEQRAQVEDDLKSGRLRAVVATSSLELGIDMGAVDLVIQVEAPPSVASGLQRVGRAGHQVGEISQGVLFPKHRTDLIGCAVTVQRMQTGDIETLRVPANPLDVLAQHTVAVAALEPVDADAWFDAVRRSAPFATLPRSAFEATLDLLSGKYPSTEFAELRPRLVYDRDTGTLTARPGAQRLAVTSGGAIPDRGMFTVYLASETEKPSRVGELDEEMVYESRPGDVISLGATSWRITEITHDRVLVIPAPGQPARLPFWRGDSVGRPAELGAAVGAFTGELASLDRKAFDKRCQKMGFAGYATDNLHQLLREQREATGVVPSDTTFVVERFRDELGDWRVILHSPYGLRVHGPLALAVGRRLRERYGIDEKPTASDDGIIVRLPDSGDTPPGADLFVFDADEIEPIVTAEVGGSALFASRFRECAARALLLPRRHPGKRSPLWHQRQRAAQLLDIARKYPDFPIVLEAVRECLQDVYDVPALIELMHKIAQRRLRIVEVETATPSPFAASLLFGYVGAFMYEGDSPLAERRAAALALDTVLLSELLGRVELRELLDPAVVASTSAQLQHLTPERAARDAEGVADLLRLLGPLTEADIAQRCTADNIGAWLDGLHAAKRALPVTYAGQTWWAAVEDIGLLRDGIGVPVPVGVPAAFTESASDPLGDLIGRYARTRGPFTTEQTAARFGLGVRVASDVLSRMAVDGRLIRGEFAADLSGEQWCDAQVLKILRRRSLAALRAQVEPVSTDAYARFLPSWQHVGSTNTTGIDGLATVIEQLAGVPIPASAVESLVFPQRVRDYQPAMLDELLASGEVMWSGAGQIGNGDGWVAFHLADTAPLTLTHGAEIEFTDTHRVILETLGHGGAYFFRQLTDGTVEGTAGQELKQALWELIWAGWVTGDTFAPVRAVLSGPRRSGAPAHRQRQRPPRLSRYSVAHAQTRGTDPTVSGRWSALPAAEPDSTVRAHFQAELLLGRHGVLTKGAVGAEGVPGGFATLYKVLSTFEDAGRCQRGYFVESLGGAQFAVASTVDRLRSYLDNVDPERPEYHAVVLAATDPANPYGAALGWPTDSEAHRPGRKAGALVALVDGRLVWFLERGGRSLLSFGADADAQRAAAGALTDLVSAGRIPSLLVERINGVAVLDPDVDAERAVVQDALLGAGLSRTPRGLRLR

[Multiple Choices]
A. Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction.
B. L-proline betaine + NADH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NAD(+) + H2O
C. ajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)
D. [molybdopterin-synthase sulfur-carrier protein]-C-terminal Gly-Gly-AMP + S-sulfanyl-L-cysteinyl-[cysteine desulfurase] + AH2 = [molybdopterin-synthase sulfur-carrier protein]-C-terminal-Gly-aminoethanethioate + L-cysteinyl-[cysteine desulfurase] + A + AMP + 2 H(+)
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

> The sequence exactly matches the UniProt entry for Mycolicibacterium smegmatis Lhr. Its catalytic-activity annotation gives the reaction in choice A and cites experimental evidence; the cited literature also identifies Lhr as a 3′-to-5′ DNA translocase and helicase. The primary studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C8](#evidence-c8), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a P-loop-like nucleotide-binding motif (…APTGSGKT…) and helicase-associated features, consistent with an ATP-dependent nucleic-acid motor. That meaningfully distinguishes the helicase reaction in A from the methylation and sulfur-transfer reactions in B–D.


**Missing item-specific fact**

> The sequence motifs alone do not establish the precise 3′-to-5′ translocation direction; that detail is protein-specific and supported here by external experimental annotation.


**Reason**

> The sequence provides meaningful grounds to select the helicase option over the chemically unrelated alternatives, though the exact polarity is not independently determined by the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A describes an ATP-coupled DNA helicase reaction; B–D describe unrelated enzyme activities.


### Important caveats

- Reviewer-only accession and annotation evidence were not supplied to the evaluated model.
- The sequence evidence supports a helicase-like ATP-driven motor, but does not by itself prove the stated translocation direction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a P-loop-like nucleotide-binding motif (…APTGSGKT…) and helicase-associated features, consistent with an ATP-dependent nucleic-acid motor. That meaningfully distinguishes the helicase reaction in A from the methylation and sulfur-transfer reactions in B–D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence motifs alone do not establish the precise 3′-to-5′ translocation direction; that detail is protein-specific and supported here by external experimental annotation.",
    "reason": "The sequence provides meaningful grounds to select the helicase option over the chemically unrelated alternatives, though the exact polarity is not independently determined by the supplied input."
  },
  "case_id": "catalytic_activity_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C8",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for Mycolicibacterium smegmatis Lhr. Its catalytic-activity annotation gives the reaction in choice A and cites experimental evidence; the cited literature also identifies Lhr as a 3′-to-5′ DNA translocase and helicase. The primary studies were not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only accession and annotation evidence were not supplied to the evaluated model.",
    "The sequence evidence supports a helicase-like ATP-driven motor, but does not by itself prove the stated translocation direction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A describes an ATP-coupled DNA helicase reaction; B–D describe unrelated enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for Mycolicibacterium smegmatis Lhr. Its catalytic-activity annotation gives the reaction in choice A and cites experimental evidence; the cited literature also identifies Lhr as a 3′-to-5′ DNA translocase and helicase. The primary studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C8", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a P-loop-like nucleotide-binding motif (…APTGSGKT…) and helicase-associated features, consistent with an ATP-dependent nucleic-acid motor. That meaningfully distinguishes the helicase reaction in A from the methylation and sulfur-transfer reactions in B–D.",
    "missing_item_specific_fact": "The sequence motifs alone do not establish the precise 3′-to-5′ translocation direction; that detail is protein-specific and supported here by external experimental annotation.",
    "reason": "The sequence provides meaningful grounds to select the helicase option over the chemically unrelated alternatives, though the exact polarity is not independently determined by the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A describes an ATP-coupled DNA helicase reaction; B–D describe unrelated enzyme activities."
  },
  "important_caveats": [
    "Reviewer-only accession and annotation evidence were not supplied to the evaluated model.",
    "The sequence evidence supports a helicase-like ATP-driven motor, but does not by itself prove the stated translocation direction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0QT91 (Lhr helicase from Mycolicibacterium smegmatis, sequence matched) explicitly annotates the catalytic activity 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction' (EC 5.6.2.4) with experimental evidence codes ECO:0000269 from PubMed 23549043 and 36610794. Multiple independent experimental studies (Ordonez & Shuman 2013; Warren et al. 2023; Ejaz et al. 2018 with PDB 5V9X crystal structure) confirm this activity. The sequence is 1507 aa, consistent with a large bacterial helicase.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable Walker A motif (PTGSGKTLAAFLW, residues ~38-42: GSGKT) indicating an ATP-binding protein. The protein is very large (1507 aa), consistent with a helicase architecture. The three distractors describe completely unrelated enzyme classes: B is a proline betaine demethylase (oxidase), C is an O-methyltransferase, D is a molybdopterin sulfur-transferase. None of these enzyme classes are consistent with a Walker A-containing large protein. Eliminating B, C, and D leaves only A as a plausible helicase/ATPase reaction. The 3'-5' directionality is the only helicase option provided, so it does not need independent determination from sequence.


**Missing item-specific fact**

> The specific 3'-5' translocation directionality cannot be independently determined from sequence alone without knowledge of which helicase superfamily (SF1/SF3) this protein belongs to. However, since it is the only helicase option among the choices, this does not impede answer selection.


**Reason**

> A knowledgeable biologist can identify the Walker A motif, note the large protein size consistent with a helicase, and eliminate the three clearly unrelated enzyme-class distractors. The remaining option (A) is the only one describing an ATP-dependent nucleic-acid motor reaction. The directionality detail, while not independently derivable from sequence, does not need to be resolved because no competing helicase-direction option exists.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices B, C, and D describe enzyme classes (demethylase/oxidase, methyltransferase, sulfur-transferase) that are entirely incompatible with a Walker A-containing 1507-aa protein. Only A describes a nucleic-acid motor/helicase reaction, making it the sole defensible answer.


### Important caveats

- The protein also carries a 'probable uracil glycosylase' annotation (EC 3.2.2.27), but this is annotated with ECO:0000250 (inferred by similarity to P30015), not experimental evidence. This secondary activity does not conflict with the primary helicase activity and is not offered as a choice.
- The 3'-5' directionality in Choice A is experimentally supported but not trivially derivable from sequence motifs alone; it relies on the fact that no alternative directionality option is presented.
- The Walker A motif is present but embedded in a 1507-aa sequence; identification requires either trained motif-recognition or general helicase-domain knowledge rather than trivial sequence inspection.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable Walker A motif (PTGSGKTLAAFLW, residues ~38-42: GSGKT) indicating an ATP-binding protein. The protein is very large (1507 aa), consistent with a helicase architecture. The three distractors describe completely unrelated enzyme classes: B is a proline betaine demethylase (oxidase), C is an O-methyltransferase, D is a molybdopterin sulfur-transferase. None of these enzyme classes are consistent with a Walker A-containing large protein. Eliminating B, C, and D leaves only A as a plausible helicase/ATPase reaction. The 3'-5' directionality is the only helicase option provided, so it does not need independent determination from sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific 3'-5' translocation directionality cannot be independently determined from sequence alone without knowledge of which helicase superfamily (SF1/SF3) this protein belongs to. However, since it is the only helicase option among the choices, this does not impede answer selection.",
    "reason": "A knowledgeable biologist can identify the Walker A motif, note the large protein size consistent with a helicase, and eliminate the three clearly unrelated enzyme-class distractors. The remaining option (A) is the only one describing an ATP-dependent nucleic-acid motor reaction. The directionality detail, while not independently derivable from sequence, does not need to be resolved because no competing helicase-direction option exists."
  },
  "case_id": "catalytic_activity_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C8",
      "C9",
      "C10",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0QT91 (Lhr helicase from Mycolicibacterium smegmatis, sequence matched) explicitly annotates the catalytic activity 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction' (EC 5.6.2.4) with experimental evidence codes ECO:0000269 from PubMed 23549043 and 36610794. Multiple independent experimental studies (Ordonez & Shuman 2013; Warren et al. 2023; Ejaz et al. 2018 with PDB 5V9X crystal structure) confirm this activity. The sequence is 1507 aa, consistent with a large bacterial helicase."
  },
  "important_caveats": [
    "The protein also carries a 'probable uracil glycosylase' annotation (EC 3.2.2.27), but this is annotated with ECO:0000250 (inferred by similarity to P30015), not experimental evidence. This secondary activity does not conflict with the primary helicase activity and is not offered as a choice.",
    "The 3'-5' directionality in Choice A is experimentally supported but not trivially derivable from sequence motifs alone; it relies on the fact that no alternative directionality option is presented.",
    "The Walker A motif is present but embedded in a 1507-aa sequence; identification requires either trained motif-recognition or general helicase-domain knowledge rather than trivial sequence inspection."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B, C, and D describe enzyme classes (demethylase/oxidase, methyltransferase, sulfur-transferase) that are entirely incompatible with a Walker A-containing 1507-aa protein. Only A describes a nucleic-acid motor/helicase reaction, making it the sole defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0QT91 (Lhr helicase from Mycolicibacterium smegmatis, sequence matched) explicitly annotates the catalytic activity 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction' (EC 5.6.2.4) with experimental evidence codes ECO:0000269 from PubMed 23549043 and 36610794. Multiple independent experimental studies (Ordonez & Shuman 2013; Warren et al. 2023; Ejaz et al. 2018 with PDB 5V9X crystal structure) confirm this activity. The sequence is 1507 aa, consistent with a large bacterial helicase.",
    "evidence_ids": ["C5", "H6", "C8", "C9", "C10", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable Walker A motif (PTGSGKTLAAFLW, residues ~38-42: GSGKT) indicating an ATP-binding protein. The protein is very large (1507 aa), consistent with a helicase architecture. The three distractors describe completely unrelated enzyme classes: B is a proline betaine demethylase (oxidase), C is an O-methyltransferase, D is a molybdopterin sulfur-transferase. None of these enzyme classes are consistent with a Walker A-containing large protein. Eliminating B, C, and D leaves only A as a plausible helicase/ATPase reaction. The 3'-5' directionality is the only helicase option provided, so it does not need independent determination from sequence.",
    "missing_item_specific_fact": "The specific 3'-5' translocation directionality cannot be independently determined from sequence alone without knowledge of which helicase superfamily (SF1/SF3) this protein belongs to. However, since it is the only helicase option among the choices, this does not impede answer selection.",
    "reason": "A knowledgeable biologist can identify the Walker A motif, note the large protein size consistent with a helicase, and eliminate the three clearly unrelated enzyme-class distractors. The remaining option (A) is the only one describing an ATP-dependent nucleic-acid motor reaction. The directionality detail, while not independently derivable from sequence, does not need to be resolved because no competing helicase-direction option exists."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B, C, and D describe enzyme classes (demethylase/oxidase, methyltransferase, sulfur-transferase) that are entirely incompatible with a Walker A-containing 1507-aa protein. Only A describes a nucleic-acid motor/helicase reaction, making it the sole defensible answer."
  },
  "important_caveats": [
    "The protein also carries a 'probable uracil glycosylase' annotation (EC 3.2.2.27), but this is annotated with ECO:0000250 (inferred by similarity to P30015), not experimental evidence. This secondary activity does not conflict with the primary helicase activity and is not offered as a choice.",
    "The 3'-5' directionality in Choice A is experimentally supported but not trivially derivable from sequence motifs alone; it relies on the fact that no alternative directionality option is presented.",
    "The Walker A motif is present but embedded in a 1507-aa sequence; identification requires either trained motif-recognition or general helicase-domain knowledge rather than trivial sequence inspection."
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

**Accession:** `A0QT91` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 131. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.412187+00:00.  

```json
"A0QT91"
```

Source SHA-256: `bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.412187+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.6.2.4","evidences":[{"evidenceCode":"ECO:0000269","id":"23549043","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36610794","source":"PubMed"}],"name":"Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction."}}
```

Source SHA-256: `bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.412187+00:00.  

```json
{"citation":{"authors":["Ordonez H.","Shuman S."],"citationCrossReferences":[{"database":"PubMed","id":"23549043"},{"database":"DOI","id":"10.1074/jbc.m113.466854"}],"citationType":"journal article","firstPage":"14125","id":"23549043","journal":"J. Biol. Chem.","lastPage":"14134","publicationDate":"2013","title":"Mycobacterium smegmatis Lhr Is a DNA-dependent ATPase and a 3'-to-5' DNA translocase and helicase that prefers to unwind 3'-tailed RNA:DNA hybrids.","volume":"288"},"referenceNumber":4,"referencePositions":["FUNCTION AS A HELICASE","FUNCTION AS AN ATPASE","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN"]}
```

Source SHA-256: `bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.412187+00:00.  

```json
{"citation":{"authors":["Warren G.M.","Ejaz A.","Fay A.","Glickman M.S.","Shuman S."],"citationCrossReferences":[{"database":"PubMed","id":"36610794"},{"database":"DOI","id":"10.1093/nar/gkac1222"}],"citationType":"journal article","firstPage":"218","id":"36610794","journal":"Nucleic Acids Res.","lastPage":"235","publicationDate":"2023","title":"Mycobacterial helicase Lhr abets resistance to DNA crosslinking agents mitomycin C and cisplatin.","volume":"51"},"referenceComments":[{"type":"STRAIN","value":"ATCC 700084 / mc(2)155"}],"referenceNumber":5,"referencePositions":["FUNCTION AS A HELICASE","CATALYTIC ACTIVITY","DOMAIN","INDUCTION","DISRUPTION PHENOTYPE","MUTAGENESIS OF 170-ASP-GLU-171; TRP-597; 1199-HIS--ARG-1206 AND ARG-1286"]}
```

Source SHA-256: `bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.412187+00:00.  

```json
{"citation":{"authors":["Ejaz A.","Ordonez H.","Jacewicz A.","Ferrao R.","Shuman S."],"citationCrossReferences":[{"database":"PubMed","id":"29165676"},{"database":"DOI","id":"10.1093/nar/gkx1163"}],"citationType":"journal article","firstPage":"442","id":"29165676","journal":"Nucleic Acids Res.","lastPage":"455","publicationDate":"2018","title":"Structure of mycobacterial 3'-to-5' RNA:DNA helicase Lhr bound to a ssDNA tracking strand highlights distinctive features of a novel family of bacterial helicases.","volume":"46"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5V9X","source":"PDB"}],"referenceNumber":7,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.80 ANGSTROMS) OF 1-856 IN COMPLEX WITH SSDNA; MG(2+) AND ATP ANALOG","FUNCTION","CATALYTIC ACTIVITY","DOMAIN","MUTAGENESIS OF ARG-122; THR-145; SER-148; ARG-279; ILE-528; GLU-550; TRP-597 AND ARG-777","ATP-BINDING","DNA-BINDING"]}
```

Source SHA-256: `bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)  
**Locator:** `lines 44-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 131 / 1.  
**Retrieved:** 2026-11-01T06:27:42.288105+00:00.  

```text
RN   [4]
RP   FUNCTION AS A HELICASE, FUNCTION AS AN ATPASE, CATALYTIC ACTIVITY,
RP   COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND DOMAIN.
RX   PubMed=23549043; DOI=10.1074/jbc.m113.466854;
RA   Ordonez H., Shuman S.;
RT   "Mycobacterium smegmatis Lhr Is a DNA-dependent ATPase and a 3'-to-5' DNA
RT   translocase and helicase that prefers to unwind 3'-tailed RNA:DNA
RT   hybrids.";
RL   J. Biol. Chem. 288:14125-14134(2013).
```

Source SHA-256: `63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)  
**Locator:** `lines 53-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 131 / 1.  
**Retrieved:** 2026-11-01T06:27:42.288105+00:00.  

```text
RN   [5]
RP   FUNCTION AS A HELICASE, CATALYTIC ACTIVITY, DOMAIN, INDUCTION, DISRUPTION
RP   PHENOTYPE, AND MUTAGENESIS OF 170-ASP-GLU-171; TRP-597; 1199-HIS--ARG-1206
RP   AND ARG-1286.
RC   STRAIN=ATCC 700084 / mc(2)155;
RX   PubMed=36610794; DOI=10.1093/nar/gkac1222;
RA   Warren G.M., Ejaz A., Fay A., Glickman M.S., Shuman S.;
RT   "Mycobacterial helicase Lhr abets resistance to DNA crosslinking agents
RT   mitomycin C and cisplatin.";
RL   Nucleic Acids Res. 51:218-235(2023).
```

Source SHA-256: `63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)  
**Locator:** `lines 72-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 131 / 1.  
**Retrieved:** 2026-11-01T06:27:42.288105+00:00.  

```text
RN   [7] {ECO:0007744|PDB:5V9X}
RP   X-RAY CRYSTALLOGRAPHY (2.80 ANGSTROMS) OF 1-856 IN COMPLEX WITH SSDNA;
RP   MG(2+) AND ATP ANALOG, FUNCTION, CATALYTIC ACTIVITY, DOMAIN, MUTAGENESIS OF
RP   ARG-122; THR-145; SER-148; ARG-279; ILE-528; GLU-550; TRP-597 AND ARG-777,
RP   ATP-BINDING, AND DNA-BINDING.
RX   PubMed=29165676; DOI=10.1093/nar/gkx1163;
RA   Ejaz A., Ordonez H., Jacewicz A., Ferrao R., Shuman S.;
RT   "Structure of mycobacterial 3'-to-5' RNA:DNA helicase Lhr bound to a ssDNA
RT   tracking strand highlights distinctive features of a novel family of
RT   bacterial helicases.";
RL   Nucleic Acids Res. 46:442-455(2018).
```

Source SHA-256: `63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)  
**Locator:** `lines 115-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 131 / 1.  
**Retrieved:** 2026-11-01T06:27:42.288105+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Couples ATP hydrolysis with the unwinding of duplex DNA by
CC         translocating in the 3'-5' direction.; EC=5.6.2.4;
CC         Evidence={ECO:0000269|PubMed:23549043, ECO:0000269|PubMed:36610794};
```

Source SHA-256: `63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 120. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
