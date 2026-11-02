# GO_cellular_component_0114

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — SAGA-type complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQSLDSSCQEADFIINDTLKKLKGSSNADHVQGLAVHAHGSGVHQTQFVQYGTSGSSPQLQPQQSYHQLHPTLQQQQFASSSSKSYLETSLLQAIPQIPAQPPICIFDDDESPTEGTGGSLGSLLTEPTSATPSGLPTAIAPSPSSCSSSTTTMSNFNSITSPSPVVPDLLLSTPPGVNSSLSNSSTGAASVSSKKSEKRPPSANSTASGGGHHLHHHHLHQTHNHHVLASPTSSPSKRQKSNSSSKESSSSSRSSAIPAASVSTATSSSQSARAGAGAASSNSNSKPPSSVCQSGNSKFFNLHEKIRDLYLQLLSNDLNYFAETGLKQRTRSFTLERLVDREKLNTIVVNLYPGNKGYSLALHYDEHMVLNPQTNEWSPTDKDETSSDAAGLGTGTGSHRSRPKPLAQDESQSKTEAGHAKHDFGLVEVLRWPYENDLLLQCIDREMLPEFLMDLLVAETVSLSDGEGTRVYAKPSVFYAGCVIAQIRDFRQTFATSTNICDMKHILLRPTNATLFAEVQQMGSQLPAEDKLALESQLVLATAEPLCLEPDPSIGRQAINSQHQRQLYNSHELRRQMKKFTQTAINRKRKLDQFTHHHGLELCDYLARLRQRPRTGSSSGGANATPATAPTNNPLVGAMLSSFTSKVPRRPHEVIRPIRPPTLEYPANLKVPEHVISVEKYAKAYEPLNEFSEACKDGCQPNCRHNFQPQLVEEYILETEREASEGRRALYHIKLSIFQRPSDAEYLGELYVDRDYREGERNGESCRFALGTRVHANRYIQQFREIFTEEGRKAVKITHLIPGHMPIVTHTGLTNEQRILLQQQQQQQQRQAQMQQQQQQQQQQVVVVANQQQQSQQQQQTQQAGQQLSATVHHVALPRQQITQKTLNLAGSNVINVQQNFRQQSAQQQQPQTYTIEAPQQQAAAQIVPQQQQQQQQQQQQHIHLQQLATGSSNTSTTTHQVSLSNGSLVLVQQQQPQQQSQQLAQALQHSGITIQPATIQQQQQQVKGTSVVGANSALRAQLNSNVPILQTQLKVQQQQIMQKQQQQQTTATSNNNNNNNNNNNMNNNTAIHPNPAINAIVNSIMNSANQYQQQQQQQHQQQHQQQTGNTSSNNNAAGSGGSTNNNGSSTSATTLKNSSNASILNLLNSAPAAMTSTPVASGTFTTSTGQQQPQTLTLVQHQQQSTPNTADAATATYVQTTRGTPTLVSTQRKQQSSEVLQNLLNANRKIGGGGTTTTTFRTNSAGNLIAVNLNQAGQSHHQQTGDGSQTVRVSMSALASQLASPPAVMTNPTTSYTVISSGNSAAAAAAWIQSPTGPVQQRILSSLRRDSTTAPPNAIVVGMAAPSPGSDSNASNASGFAVPNNLASTSSGGGGGGGALSALLTNAATPSPSGSDHSQSSQTHQNQALLERLSNVTSNVSAVSMPHMSPQQPQPTQQFITKTIVHSPATSSIHSPMSSPHPQPSASPQQQQQQQQQQTTATLNLQGINLSQLQGAMANFAGLQNVQVQIPGFTQPISLQFSGNSLQQQQSGNTATGAGTAQGQQRSVLVSVPVSSQQQQLPHTITLQTQSAPHHQQQHQQTQQQHAPPTGTIVSLPSSGPGTQTVVITNNSGGGVTAGSSTSGSAGGGGGSGATTAMLTLPIAQIVGAGVQKLNPQTIRTSNVGGGIGIAQQTVQQQTIQSQSGGNSTAAIQLLGTIQPRARNVQVVGTKQLANRQLITTQRQIGGSTLKIATTPVNAANVVTSSANLTTTPIVMSAQKLQLKTVKAPVQQQQQPQQQQQQLQQQHRILNQQSTATVSSQTLPSPNQVQVAQQQQQQQQQLQHIQIAGRATTASGAISQRTLTALAAAKQQQQQQQAAVNRRRSTTDATK

[Multiple Choices]
A. host cell nucleolus
B. SAGA-type complex
C. caveola
D. peroxisomal membrane
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

> The sequence matches the Drosophila Spt20 entry, which has an experimentally supported GO annotation to SAGA-type complex (IDA:FlyBase), matching choice B.

Citations as saved: [C8](#evidence-c8), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is long and rich in low-complexity regions, with no clear sequence feature that specifically identifies SAGA-complex membership over the listed choices.


**Missing item-specific fact**

> The protein-specific finding that this protein is a SAGA-complex subunit.


**Reason**

> Distinguishing B requires the protein's experimentally established complex membership, which is not supplied by the sequence context alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is supported by a matching SAGA-type-complex annotation; the supplied evidence does not support the more specific nucleolar option.


### Important caveats

- The prompt describes predicting a cellular location, but SAGA-type complex denotes complex membership rather than a cellular compartment. The matching protein is also annotated to the nucleus, which is not one of the listed choices.
- The cited annotations are reviewer-only evidence and were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is long and rich in low-complexity regions, with no clear sequence feature that specifically identifies SAGA-complex membership over the listed choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that this protein is a SAGA-complex subunit.",
    "reason": "Distinguishing B requires the protein's experimentally established complex membership, which is not supplied by the sequence context alone."
  },
  "case_id": "GO_cellular_component_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila Spt20 entry, which has an experimentally supported GO annotation to SAGA-type complex (IDA:FlyBase), matching choice B."
  },
  "important_caveats": [
    "The prompt describes predicting a cellular location, but SAGA-type complex denotes complex membership rather than a cellular compartment. The matching protein is also annotated to the nucleus, which is not one of the listed choices.",
    "The cited annotations are reviewer-only evidence and were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is supported by a matching SAGA-type-complex annotation; the supplied evidence does not support the more specific nucleolar option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila Spt20 entry, which has an experimentally supported GO annotation to SAGA-type complex (IDA:FlyBase), matching choice B.",
    "evidence_ids": ["C8", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is long and rich in low-complexity regions, with no clear sequence feature that specifically identifies SAGA-complex membership over the listed choices.",
    "missing_item_specific_fact": "The protein-specific finding that this protein is a SAGA-complex subunit.",
    "reason": "Distinguishing B requires the protein's experimentally established complex membership, which is not supplied by the sequence context alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is supported by a matching SAGA-type-complex annotation; the supplied evidence does not support the more specific nucleolar option."
  },
  "important_caveats": [
    "The prompt describes predicting a cellular location, but SAGA-type complex denotes complex membership rather than a cellular compartment. The matching protein is also annotated to the nucleus, which is not one of the listed choices.",
    "The cited annotations are reviewer-only evidence and were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9VU86 (Spt20_DROME, SAGA complex subunit Spt20). GO annotation GO:0070461 (C:SAGA-type complex) is assigned with IDA:FlyBase evidence (Inferred by Direct Assay), supported by mass spectrometry identification in the SAGA complex (PubMed:20008933, PubMed:21764853, PubMed:24493646). The protein is also annotated GO:0000124 (SAGA complex), which is_a GO:0070461. The expected answer B is directly supported by experimental evidence.

Citations as saved: [C4](#evidence-c4), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [H6](#evidence-h6), [H7](#evidence-h7), [GO5](#evidence-go5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can eliminate C (caveola) and D (peroxisomal membrane) by noting the absence of transmembrane domains, lipid-anchor motifs, and peroxisomal targeting signals (PTS1/PTS2). One can weakly argue against A (host cell nucleolus) because the protein lacks nucleolar localization signals and the term 'host cell nucleolus' is specific to viral-host interaction contexts. However, the positive identification of 'SAGA-type complex' specifically requires recognizing this as Spt20 or knowing that its histone fold domain places it in the SAGA complex rather than other histone-fold-containing chromatin complexes (TFIID, NuA4, etc.).


**Missing item-specific fact**

> The specific identity of this protein as Spt20, a SAGA complex subunit that replaces TAF6 in Drosophila, is required to positively identify the SAGA-type complex. A histone fold domain in a large, low-complexity-rich protein is consistent with multiple chromatin/transcription complexes; only database or literature knowledge distinguishes SAGA from TFIID, NuA4, or other HAT complexes.


**Reason**

> While general reasoning can eliminate membrane-associated options (C, D) and the unlikely nucleolar option (A), the positive assignment to 'SAGA-type complex' over other nuclear/chromatin complexes depends on recognizing the specific protein identity. The sequence alone (1873 aa, histone fold domain, extensive glutamine/serine-rich low-complexity regions) does not uniquely specify SAGA membership without item-specific annotation knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only B is a nuclear transcription-complex term. The protein is annotated with 'nucleus' (GO:0005634), but that term is not offered. GO:0000124 (SAGA complex) is_a GO:0070461 (SAGA-type complex), so both annotations are consistent with B. No other option is supported by any annotation for this protein.


### Important caveats

- The protein is also annotated with GO:0005634 (nucleus) with IDA evidence. The question asks for 'primary Cellular Component' and offers the more specific SAGA-type complex as the correct answer, which is defensible as a more granular and functionally informative annotation.
- The 'host cell nucleolus' option (A) uses a GO term (GO:0044196) whose definition refers to nucleoli in viral-infected host cells; this is an unusual and context-specific term that does not apply to a normal Drosophila nuclear protein.
- The histone fold domain identification in the sequence is based on the literature (PubMed:20008933 title mentions 'histone fold domain-containing protein'); this feature alone is not unique to SAGA.
- Sequence identity was confirmed by SHA-256 match to both current and historical (entry v172) UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can eliminate C (caveola) and D (peroxisomal membrane) by noting the absence of transmembrane domains, lipid-anchor motifs, and peroxisomal targeting signals (PTS1/PTS2). One can weakly argue against A (host cell nucleolus) because the protein lacks nucleolar localization signals and the term 'host cell nucleolus' is specific to viral-host interaction contexts. However, the positive identification of 'SAGA-type complex' specifically requires recognizing this as Spt20 or knowing that its histone fold domain places it in the SAGA complex rather than other histone-fold-containing chromatin complexes (TFIID, NuA4, etc.).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as Spt20, a SAGA complex subunit that replaces TAF6 in Drosophila, is required to positively identify the SAGA-type complex. A histone fold domain in a large, low-complexity-rich protein is consistent with multiple chromatin/transcription complexes; only database or literature knowledge distinguishes SAGA from TFIID, NuA4, or other HAT complexes.",
    "reason": "While general reasoning can eliminate membrane-associated options (C, D) and the unlikely nucleolar option (A), the positive assignment to 'SAGA-type complex' over other nuclear/chromatin complexes depends on recognizing the specific protein identity. The sequence alone (1873 aa, histone fold domain, extensive glutamine/serine-rich low-complexity regions) does not uniquely specify SAGA membership without item-specific annotation knowledge."
  },
  "case_id": "GO_cellular_component_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "H6",
      "H7",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VU86 (Spt20_DROME, SAGA complex subunit Spt20). GO annotation GO:0070461 (C:SAGA-type complex) is assigned with IDA:FlyBase evidence (Inferred by Direct Assay), supported by mass spectrometry identification in the SAGA complex (PubMed:20008933, PubMed:21764853, PubMed:24493646). The protein is also annotated GO:0000124 (SAGA complex), which is_a GO:0070461. The expected answer B is directly supported by experimental evidence."
  },
  "important_caveats": [
    "The protein is also annotated with GO:0005634 (nucleus) with IDA evidence. The question asks for 'primary Cellular Component' and offers the more specific SAGA-type complex as the correct answer, which is defensible as a more granular and functionally informative annotation.",
    "The 'host cell nucleolus' option (A) uses a GO term (GO:0044196) whose definition refers to nucleoli in viral-infected host cells; this is an unusual and context-specific term that does not apply to a normal Drosophila nuclear protein.",
    "The histone fold domain identification in the sequence is based on the literature (PubMed:20008933 title mentions 'histone fold domain-containing protein'); this feature alone is not unique to SAGA.",
    "Sequence identity was confirmed by SHA-256 match to both current and historical (entry v172) UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only B is a nuclear transcription-complex term. The protein is annotated with 'nucleus' (GO:0005634), but that term is not offered. GO:0000124 (SAGA complex) is_a GO:0070461 (SAGA-type complex), so both annotations are consistent with B. No other option is supported by any annotation for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VU86 (Spt20_DROME, SAGA complex subunit Spt20). GO annotation GO:0070461 (C:SAGA-type complex) is assigned with IDA:FlyBase evidence (Inferred by Direct Assay), supported by mass spectrometry identification in the SAGA complex (PubMed:20008933, PubMed:21764853, PubMed:24493646). The protein is also annotated GO:0000124 (SAGA complex), which is_a GO:0070461. The expected answer B is directly supported by experimental evidence.",
    "evidence_ids": ["C4", "C7", "C8", "C9", "C10", "C11", "H6", "H7", "GO5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can eliminate C (caveola) and D (peroxisomal membrane) by noting the absence of transmembrane domains, lipid-anchor motifs, and peroxisomal targeting signals (PTS1/PTS2). One can weakly argue against A (host cell nucleolus) because the protein lacks nucleolar localization signals and the term 'host cell nucleolus' is specific to viral-host interaction contexts. However, the positive identification of 'SAGA-type complex' specifically requires recognizing this as Spt20 or knowing that its histone fold domain places it in the SAGA complex rather than other histone-fold-containing chromatin complexes (TFIID, NuA4, etc.).",
    "missing_item_specific_fact": "The specific identity of this protein as Spt20, a SAGA complex subunit that replaces TAF6 in Drosophila, is required to positively identify the SAGA-type complex. A histone fold domain in a large, low-complexity-rich protein is consistent with multiple chromatin/transcription complexes; only database or literature knowledge distinguishes SAGA from TFIID, NuA4, or other HAT complexes.",
    "reason": "While general reasoning can eliminate membrane-associated options (C, D) and the unlikely nucleolar option (A), the positive assignment to 'SAGA-type complex' over other nuclear/chromatin complexes depends on recognizing the specific protein identity. The sequence alone (1873 aa, histone fold domain, extensive glutamine/serine-rich low-complexity regions) does not uniquely specify SAGA membership without item-specific annotation knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only B is a nuclear transcription-complex term. The protein is annotated with 'nucleus' (GO:0005634), but that term is not offered. GO:0000124 (SAGA complex) is_a GO:0070461 (SAGA-type complex), so both annotations are consistent with B. No other option is supported by any annotation for this protein."
  },
  "important_caveats": [
    "The protein is also annotated with GO:0005634 (nucleus) with IDA evidence. The question asks for 'primary Cellular Component' and offers the more specific SAGA-type complex as the correct answer, which is defensible as a more granular and functionally informative annotation.",
    "The 'host cell nucleolus' option (A) uses a GO term (GO:0044196) whose definition refers to nucleoli in viral-infected host cells; this is an unusual and context-specific term that does not apply to a normal Drosophila nuclear protein.",
    "The histone fold domain identification in the sequence is based on the literature (PubMed:20008933 title mentions 'histone fold domain-containing protein'); this feature alone is not unique to SAGA.",
    "Sequence identity was confirmed by SHA-256 match to both current and historical (entry v172) UniProt records."
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

**Accession:** `Q9VU86` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 172. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU86.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:45.245152+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"SAGA complex subunit Spt20"}}}
```

Source SHA-256: `84790c11c369b730b854b94d5600e08bbde34cfb617f3a1f70fc037afd40f965`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU86.json)  
**Locator:** `/uniProtKBCrossReferences/37`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:45.245152+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"21764853","source":"PubMed"}],"id":"GO:0000124","properties":[{"key":"GoTerm","value":"C:SAGA complex"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `84790c11c369b730b854b94d5600e08bbde34cfb617f3a1f70fc037afd40f965`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU86.json)  
**Locator:** `/uniProtKBCrossReferences/38`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:45.245152+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"20008933","source":"PubMed"}],"id":"GO:0070461","properties":[{"key":"GoTerm","value":"C:SAGA-type complex"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `84790c11c369b730b854b94d5600e08bbde34cfb617f3a1f70fc037afd40f965`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU86.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:45.245152+00:00.  

```json
{"citation":{"authors":["Weake V.M.","Swanson S.K.","Mushegian A.","Florens L.","Washburn M.P.","Abmayr S.M.","Workman J.L."],"citationCrossReferences":[{"database":"PubMed","id":"20008933"},{"database":"DOI","id":"10.1101/gad.1846409"}],"citationType":"journal article","firstPage":"2818","id":"20008933","journal":"Genes Dev.","lastPage":"2823","publicationDate":"2009","title":"A novel histone fold domain-containing protein that replaces TAF6 in Drosophila SAGA is required for SAGA-dependent gene expression.","volume":"23"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","IDENTIFICATION IN SAGA COMPLEX","SUBCELLULAR LOCATION","IDENTIFICATION BY MASS SPECTROMETRY"]}
```

Source SHA-256: `84790c11c369b730b854b94d5600e08bbde34cfb617f3a1f70fc037afd40f965`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU86.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:45.245152+00:00.  

```json
{"citation":{"authors":["Weake V.M.","Dyer J.O.","Seidel C.","Box A.","Swanson S.K.","Peak A.","Florens L.","Washburn M.P.","Abmayr S.M.","Workman J.L."],"citationCrossReferences":[{"database":"PubMed","id":"21764853"},{"database":"DOI","id":"10.1101/gad.2046211"}],"citationType":"journal article","firstPage":"1499","id":"21764853","journal":"Genes Dev.","lastPage":"1509","publicationDate":"2011","title":"Post-transcription initiation function of the ubiquitous SAGA complex in tissue-specific gene activation.","volume":"25"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":6,"referencePositions":["FUNCTION","IDENTIFICATION IN SAGA COMPLEX","DEVELOPMENTAL STAGE","IDENTIFICATION BY MASS SPECTROMETRY"]}
```

Source SHA-256: `84790c11c369b730b854b94d5600e08bbde34cfb617f3a1f70fc037afd40f965`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU86.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:45.245152+00:00.  

```json
{"citation":{"authors":["Mohan R.D.","Dialynas G.","Weake V.M.","Liu J.","Martin-Brown S.","Florens L.","Washburn M.P.","Workman J.L.","Abmayr S.M."],"citationCrossReferences":[{"database":"PubMed","id":"24493646"},{"database":"DOI","id":"10.1101/gad.225151.113"}],"citationType":"journal article","firstPage":"259","id":"24493646","journal":"Genes Dev.","lastPage":"272","publicationDate":"2014","title":"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination and leads to neural and retinal degeneration.","volume":"28"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":7,"referencePositions":["FUNCTION","IDENTIFICATION IN THE SAGA COMPLEX","SUBCELLULAR LOCATION","IDENTIFICATION BY MASS SPECTROMETRY"]}
```

Source SHA-256: `84790c11c369b730b854b94d5600e08bbde34cfb617f3a1f70fc037afd40f965`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU86?format=txt&versions=172)  
**Locator:** `lines 180-180`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 172 / 3.  
**Retrieved:** 2026-11-02T04:33:48.179096+00:00.  

```text
DR   GO; GO:0000124; C:SAGA complex; IDA:FlyBase.
```

Source SHA-256: `2d0ee01b7ce507696ca4821c338d4a589d067b28ccb6080cb6a49a18ca2a4dba`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU86?format=txt&versions=172)  
**Locator:** `lines 181-181`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 172 / 3.  
**Retrieved:** 2026-11-02T04:33:48.179096+00:00.  

```text
DR   GO; GO:0070461; C:SAGA-type complex; IDA:FlyBase.
```

Source SHA-256: `2d0ee01b7ce507696ca4821c338d4a589d067b28ccb6080cb6a49a18ca2a4dba`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 367910-367917`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0070461
name: SAGA-type complex
namespace: cellular_component
def: "A histone acetyltransferase complex that acetylates nucleosomal histones H2B, H3, or H4 and is required for the expression of a subset of Pol II-transcribed genes. This complex includes the acetyltransferases GCN5/KAT2A or PCAF/KAT2B, several proteins of the ADA, SGF and SPT families, and several TBP-associate proteins (TAFs)." [GOC:mah, PMID:10637607, PMID:17337012]
synonym: "SAGA family complex" EXACT [PMID:17337012]
is_a: GO:0000123 ! histone acetyltransferase complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 114. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
