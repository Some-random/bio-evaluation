# GO_cellular_component_0136

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEKDFTERSTKGQRKLANGVVENIESKLKNHLDNNNVINKSVNYEDVMCSNVKLSVHDDEYDIKNIKKDVCNLSKLSEERLSNNISLKDNNKVVKNPEIDTKTARQQYKKRLNSTQSTMNIEGNINNEKDDIIEDYDDGLIRNMDYEMSIVKNKRNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNSNNVDNRKRNKNEECYDESYCISDNLDEITSYRNKLSLYNKLRMCFNYFGPGWIVAIAYLDPGNLCSNLNVGLIRSPDPTLEKDYSGYYLLWIMVYGHMLGFIFQVLSMRLGHVTGLDLASLCSKEFDRTTSTIIYVLVQIAIWGAHIQAIIGTFIALNLIFGISVKVAIFYTLFEAIIYSFLENKSLGLLENVLSFLVGILAVSFFVNVFMTPINFKELAISILYPRIPKGKEIDALALLGSIISAHIFYLHTNLTAKKKSVICNDLSLRRYNTLGTIESGGSLFLSCLTNCIIVLTFAEVNLKSFERRDQYNLFTAYEVMRKSFGKISMYIWSFGLLSSGNNSSFMCEYASKSVVEGFLNKKINTFVRVFTFRLMLFSLLYMFLTLNKYTLDQLTNFINVIQVLLLPMATIPLYRFSIHENVLGEFRLKKFPKFAVFLIIIAIIISNVLLTFLDFVHKETSLITIFFLVIFSFLYFGFIIYFFNIPIKKNYIQRN

[Multiple Choices]
A. mannosyltransferase complex
B. side of membrane
C. membrane
D. L-cysteine desulfurase complex
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated as a multipass vacuole-membrane protein, with cited experimental evidence for that location. The entry also carries the GO annotation “membrane,” supporting choice C.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has many long hydrophobic regions consistent with multiple transmembrane helices, strongly supporting a membrane protein over either named enzyme complex. The sequence alone supports membrane localization at this broad level.


**Missing item-specific fact**

> The particular vacuolar-membrane location is an item-specific fact not established by the sequence pattern alone, but it is not needed to distinguish the broad membrane option from the listed complexes.


**Reason**

> A defensible sequence-based argument distinguishes membrane from the two unrelated protein-complex choices. The reviewer-only annotation confirms the expected broad answer but is not needed for that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein’s multiple hydrophobic segments support localization in a membrane. “Side of membrane” refers to a membrane leaflet and is not as well supported for a multipass protein spanning the bilayer; neither named complex fits the sequence evidence.


### Important caveats

- Sequence composition supports membrane association but does not by itself identify the vacuole membrane.
- The supporting UniProt subcellular-location annotation cites experimental evidence, while the GO membrane annotation is transferred by similarity; the cited primary studies were not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many long hydrophobic regions consistent with multiple transmembrane helices, strongly supporting a membrane protein over either named enzyme complex. The sequence alone supports membrane localization at this broad level.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The particular vacuolar-membrane location is an item-specific fact not established by the sequence pattern alone, but it is not needed to distinguish the broad membrane option from the listed complexes.",
    "reason": "A defensible sequence-based argument distinguishes membrane from the two unrelated protein-complex choices. The reviewer-only annotation confirms the expected broad answer but is not needed for that distinction."
  },
  "case_id": "GO_cellular_component_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a multipass vacuole-membrane protein, with cited experimental evidence for that location. The entry also carries the GO annotation “membrane,” supporting choice C."
  },
  "important_caveats": [
    "Sequence composition supports membrane association but does not by itself identify the vacuole membrane.",
    "The supporting UniProt subcellular-location annotation cites experimental evidence, while the GO membrane annotation is transferred by similarity; the cited primary studies were not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein’s multiple hydrophobic segments support localization in a membrane. “Side of membrane” refers to a membrane leaflet and is not as well supported for a multipass protein spanning the bilayer; neither named complex fits the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a multipass vacuole-membrane protein, with cited experimental evidence for that location. The entry also carries the GO annotation “membrane,” supporting choice C.",
    "evidence_ids": ["C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has many long hydrophobic regions consistent with multiple transmembrane helices, strongly supporting a membrane protein over either named enzyme complex. The sequence alone supports membrane localization at this broad level.",
    "missing_item_specific_fact": "The particular vacuolar-membrane location is an item-specific fact not established by the sequence pattern alone, but it is not needed to distinguish the broad membrane option from the listed complexes.",
    "reason": "A defensible sequence-based argument distinguishes membrane from the two unrelated protein-complex choices. The reviewer-only annotation confirms the expected broad answer but is not needed for that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein’s multiple hydrophobic segments support localization in a membrane. “Side of membrane” refers to a membrane leaflet and is not as well supported for a multipass protein spanning the bilayer; neither named complex fits the sequence evidence."
  },
  "important_caveats": [
    "Sequence composition supports membrane association but does not by itself identify the vacuole membrane.",
    "The supporting UniProt subcellular-location annotation cites experimental evidence, while the GO membrane annotation is transferred by similarity; the cited primary studies were not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8I3M7 (Divalent metal transporter 1 / FVRT1 / PfNRAMP from Plasmodium falciparum) is experimentally annotated as 'Vacuole membrane; Multi-pass membrane protein' with evidence codes ECO:0000269 from PubMed:35404116 and PubMed:39467134. The GO term GO:0016020 (membrane) is an ancestor of vacuolar membrane (GO:0005774 → GO:0098588 → GO:0031090 → GO:0016020). The explicit GO annotation GO:0016020 is present (ISS:GeneDB). Among the four provided choices, 'membrane' is the correct broad category for a multi-pass transmembrane protein residing in the vacuolar membrane.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains numerous long hydrophobic stretches (e.g., 'LLWIMVYGHMLGFIFQVLSMRLGHVTGLDLASLCSKEFDRTTSTIIYVLVQIAIWGAHIQAIIGTFIALNLIFGISVKVAIFYTLFEAIIYSFLENKSLGLLENVLSFLVGILAVSFFVNVFMTPINFKELAISILYPRIPKGKEIDALALLGSIISAHIFYLHTNLTAKKKSVICNDLSLRRYNTLGTIESGGSLFLSCLTNCIIVLTFAEVNLKSFERRDQYNLFTAYEVMRKSFGKISMYIWSFGLLSSGNNSSFMCEYASKSVVEGFLNKKINTFVRVFTFRLMLFSLLYMFLTLNKYTLDQLTNFINVIQVLLLPMATIPLYRFSIHENVLGEFRLKKFPKFAVFLIIIAIIISNVLLTFLDFVHKETSLITIFFLVIFSFLYFGFIIYFFNIPIKKNYIQRN') characteristic of multiple transmembrane helices, identifying this as a multi-pass transmembrane protein. A multi-pass TM protein spans the entire bilayer, making 'membrane' (GO:0016020) appropriate rather than 'side of membrane' (GO:0098552, which denotes association with one leaflet). The absence of mannosyltransferase or cysteine desulfurase catalytic domains eliminates options A and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The presence of multiple hydrophobic transmembrane segments is directly identifiable from the amino acid sequence. The distinction between 'membrane' (spanning the bilayer) and 'side of membrane' (one leaflet association) is standard cell biology knowledge applied to multi-pass TM topology. The elimination of mannosyltransferase complex and L-cysteine desulfurase complex requires only recognition that the sequence lacks the relevant enzymatic domains.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is unambiguously a multi-pass transmembrane protein based on sequence hydrophobicity patterns. 'Side of membrane' applies to peripheral or lipid-anchored proteins associated with one leaflet, not to proteins spanning the bilayer. The other two options (mannosyltransferase complex, L-cysteine desulfurase complex) describe specific enzymatic complexes with no structural or functional resemblance to this NRAMP-family transporter. While the most specific annotation is 'vacuolar membrane,' that term is not among the choices, and 'membrane' is its correct GO ancestor.


### Important caveats

- The most specific experimental annotation is 'Vacuole membrane' (GO:0005774), not the broad 'membrane' (GO:0016020). The GO:0016020 annotation in UniProt carries evidence code ISS:GeneDB (computational transfer), while the experimental evidence supports the more specific vacuolar membrane location.
- The identity of this protein as Q8I3M7 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence without accession or organism information.
- The GO:0005886 (plasma membrane) annotation with IBA:GO_Central evidence suggests some ambiguity in the broader GO propagation, but experimental data (PubMed:35404116, PubMed:39467134) specifically place this protein in the food vacuole membrane, not the plasma membrane.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic stretches (e.g., 'LLWIMVYGHMLGFIFQVLSMRLGHVTGLDLASLCSKEFDRTTSTIIYVLVQIAIWGAHIQAIIGTFIALNLIFGISVKVAIFYTLFEAIIYSFLENKSLGLLENVLSFLVGILAVSFFVNVFMTPINFKELAISILYPRIPKGKEIDALALLGSIISAHIFYLHTNLTAKKKSVICNDLSLRRYNTLGTIESGGSLFLSCLTNCIIVLTFAEVNLKSFERRDQYNLFTAYEVMRKSFGKISMYIWSFGLLSSGNNSSFMCEYASKSVVEGFLNKKINTFVRVFTFRLMLFSLLYMFLTLNKYTLDQLTNFINVIQVLLLPMATIPLYRFSIHENVLGEFRLKKFPKFAVFLIIIAIIISNVLLTFLDFVHKETSLITIFFLVIFSFLYFGFIIYFFNIPIKKNYIQRN') characteristic of multiple transmembrane helices, identifying this as a multi-pass transmembrane protein. A multi-pass TM protein spans the entire bilayer, making 'membrane' (GO:0016020) appropriate rather than 'side of membrane' (GO:0098552, which denotes association with one leaflet). The absence of mannosyltransferase or cysteine desulfurase catalytic domains eliminates options A and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The presence of multiple hydrophobic transmembrane segments is directly identifiable from the amino acid sequence. The distinction between 'membrane' (spanning the bilayer) and 'side of membrane' (one leaflet association) is standard cell biology knowledge applied to multi-pass TM topology. The elimination of mannosyltransferase complex and L-cysteine desulfurase complex requires only recognition that the sequence lacks the relevant enzymatic domains."
  },
  "case_id": "GO_cellular_component_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "H5",
      "H6",
      "H7",
      "H8",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8I3M7 (Divalent metal transporter 1 / FVRT1 / PfNRAMP from Plasmodium falciparum) is experimentally annotated as 'Vacuole membrane; Multi-pass membrane protein' with evidence codes ECO:0000269 from PubMed:35404116 and PubMed:39467134. The GO term GO:0016020 (membrane) is an ancestor of vacuolar membrane (GO:0005774 → GO:0098588 → GO:0031090 → GO:0016020). The explicit GO annotation GO:0016020 is present (ISS:GeneDB). Among the four provided choices, 'membrane' is the correct broad category for a multi-pass transmembrane protein residing in the vacuolar membrane."
  },
  "important_caveats": [
    "The most specific experimental annotation is 'Vacuole membrane' (GO:0005774), not the broad 'membrane' (GO:0016020). The GO:0016020 annotation in UniProt carries evidence code ISS:GeneDB (computational transfer), while the experimental evidence supports the more specific vacuolar membrane location.",
    "The identity of this protein as Q8I3M7 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence without accession or organism information.",
    "The GO:0005886 (plasma membrane) annotation with IBA:GO_Central evidence suggests some ambiguity in the broader GO propagation, but experimental data (PubMed:35404116, PubMed:39467134) specifically place this protein in the food vacuole membrane, not the plasma membrane."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is unambiguously a multi-pass transmembrane protein based on sequence hydrophobicity patterns. 'Side of membrane' applies to peripheral or lipid-anchored proteins associated with one leaflet, not to proteins spanning the bilayer. The other two options (mannosyltransferase complex, L-cysteine desulfurase complex) describe specific enzymatic complexes with no structural or functional resemblance to this NRAMP-family transporter. While the most specific annotation is 'vacuolar membrane,' that term is not among the choices, and 'membrane' is its correct GO ancestor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8I3M7 (Divalent metal transporter 1 / FVRT1 / PfNRAMP from Plasmodium falciparum) is experimentally annotated as 'Vacuole membrane; Multi-pass membrane protein' with evidence codes ECO:0000269 from PubMed:35404116 and PubMed:39467134. The GO term GO:0016020 (membrane) is an ancestor of vacuolar membrane (GO:0005774 → GO:0098588 → GO:0031090 → GO:0016020). The explicit GO annotation GO:0016020 is present (ISS:GeneDB). Among the four provided choices, 'membrane' is the correct broad category for a multi-pass transmembrane protein residing in the vacuolar membrane.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "H5", "H6", "H7", "H8", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic stretches (e.g., 'LLWIMVYGHMLGFIFQVLSMRLGHVTGLDLASLCSKEFDRTTSTIIYVLVQIAIWGAHIQAIIGTFIALNLIFGISVKVAIFYTLFEAIIYSFLENKSLGLLENVLSFLVGILAVSFFVNVFMTPINFKELAISILYPRIPKGKEIDALALLGSIISAHIFYLHTNLTAKKKSVICNDLSLRRYNTLGTIESGGSLFLSCLTNCIIVLTFAEVNLKSFERRDQYNLFTAYEVMRKSFGKISMYIWSFGLLSSGNNSSFMCEYASKSVVEGFLNKKINTFVRVFTFRLMLFSLLYMFLTLNKYTLDQLTNFINVIQVLLLPMATIPLYRFSIHENVLGEFRLKKFPKFAVFLIIIAIIISNVLLTFLDFVHKETSLITIFFLVIFSFLYFGFIIYFFNIPIKKNYIQRN') characteristic of multiple transmembrane helices, identifying this as a multi-pass transmembrane protein. A multi-pass TM protein spans the entire bilayer, making 'membrane' (GO:0016020) appropriate rather than 'side of membrane' (GO:0098552, which denotes association with one leaflet). The absence of mannosyltransferase or cysteine desulfurase catalytic domains eliminates options A and D.",
    "missing_item_specific_fact": "",
    "reason": "The presence of multiple hydrophobic transmembrane segments is directly identifiable from the amino acid sequence. The distinction between 'membrane' (spanning the bilayer) and 'side of membrane' (one leaflet association) is standard cell biology knowledge applied to multi-pass TM topology. The elimination of mannosyltransferase complex and L-cysteine desulfurase complex requires only recognition that the sequence lacks the relevant enzymatic domains."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is unambiguously a multi-pass transmembrane protein based on sequence hydrophobicity patterns. 'Side of membrane' applies to peripheral or lipid-anchored proteins associated with one leaflet, not to proteins spanning the bilayer. The other two options (mannosyltransferase complex, L-cysteine desulfurase complex) describe specific enzymatic complexes with no structural or functional resemblance to this NRAMP-family transporter. While the most specific annotation is 'vacuolar membrane,' that term is not among the choices, and 'membrane' is its correct GO ancestor."
  },
  "important_caveats": [
    "The most specific experimental annotation is 'Vacuole membrane' (GO:0005774), not the broad 'membrane' (GO:0016020). The GO:0016020 annotation in UniProt carries evidence code ISS:GeneDB (computational transfer), while the experimental evidence supports the more specific vacuolar membrane location.",
    "The identity of this protein as Q8I3M7 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence without accession or organism information.",
    "The GO:0005886 (plasma membrane) annotation with IBA:GO_Central evidence suggests some ambiguity in the broader GO propagation, but experimental data (PubMed:35404116, PubMed:39467134) specifically place this protein in the food vacuole membrane, not the plasma membrane."
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

**Accession:** `Q8I3M7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 117. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"35404116","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39467134","source":"PubMed"}],"id":"SL-0271","value":"Vacuole membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/uniProtKBCrossReferences/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000250","id":"12368867","source":"PubMed"}],"id":"GO:0016020","properties":[{"key":"GoTerm","value":"C:membrane"},{"key":"GoEvidenceType","value":"ISS:GeneDB"}]}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/uniProtKBCrossReferences/24`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"database":"GO","id":"GO:0005774","properties":[{"key":"GoTerm","value":"C:vacuolar membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"citation":{"authors":["Hall N.","Pain A.","Berriman M.","Churcher C.M.","Harris B.","Harris D.","Mungall K.L.","Bowman S.","Atkin R.","Baker S.","Barron A.","Brooks K.","Buckee C.O.","Burrows C.","Cherevach I.","Chillingworth C.","Chillingworth T.","Christodoulou Z.","Clark L.","Clark R.","Corton C.","Cronin A.","Davies R.M.","Davis P.","Dear P.","Dearden F.","Doggett J.","Feltwell T.","Goble A.","Goodhead I.","Gwilliam R.","Hamlin N.","Hance Z.","Harper D.","Hauser H.","Hornsby T.","Holroyd S.","Horrocks P.","Humphray S.","Jagels K.","James K.D.","Johnson D.","Kerhornou A.","Knights A.","Konfortov B.","Kyes S.","Larke N.","Lawson D.","Lennard N.","Line A.","Maddison M.","Mclean J.","Mooney P.","Moule S.","Murphy L.","Oliver K.","Ormond D.","Price C.","Quail M.A.","Rabbinowitsch E.","Rajandream M.A.","Rutter S.","Rutherford K.M.","Sanders M.","Simmonds M.","Seeger K.","Sharp S.","Smith R.","Squares R.","Squares S.","Stevens K.","Taylor K.","Tivey A.","Unwin L.","Whitehead S.","Woodward J.R.","Sulston J.E.","Craig A.","Newbold C.","Barrell B.G."],"citationCrossReferences":[{"database":"PubMed","id":"12368867"},{"database":"DOI","id":"10.1038/nature01095"}],"citationType":"journal article","firstPage":"527","id":"12368867","journal":"Nature","lastPage":"531","publicationDate":"2002","title":"Sequence of Plasmodium falciparum chromosomes 1, 3-9 and 13.","volume":"419"},"evidences":[{"evidenceCode":"ECO:0000312","id":"UP000001450","source":"Proteomes"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"UP000001450","source":"Proteomes"}],"type":"STRAIN","value":"3D7"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA]"]}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 83-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Vacuole membrane {ECO:0000269|PubMed:35404116,
CC       ECO:0000269|PubMed:39467134}; Multi-pass membrane protein
CC       {ECO:0000255}.
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 129-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
DR   GO; GO:0016020; C:membrane; ISS:GeneDB.
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 130-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IBA:GO_Central.
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 131-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
DR   GO; GO:0005774; C:vacuolar membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 122626-122650`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016020
name: membrane
namespace: cellular_component
alt_id: GO:0016021
alt_id: GO:0098589
alt_id: GO:0098805
def: "A lipid bilayer along with all the proteins and protein complexes embedded in it and attached to it." [GOC:dos, GOC:mah, ISBN:0815316194]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_flybase_ribbon
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_plant
subset: goslim_yeast
synonym: "integral component of membrane" NARROW []
synonym: "integral to membrane" NARROW []
synonym: "membrane region" NARROW []
synonym: "region of membrane" NARROW []
synonym: "transmembrane" RELATED [GOC:mah]
synonym: "whole membrane" NARROW []
xref: Wikipedia:Biological_membrane
xref: Wikipedia:Transmembrane_protein
is_a: GO:0110165 ! cellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
