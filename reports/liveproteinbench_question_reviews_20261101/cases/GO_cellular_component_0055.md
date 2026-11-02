# GO_cellular_component_0055

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — mitochondrial membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSFYNKCFTNKLISAHSLFCQHVSTLKNNKKECFEDVKRSNRISDEFYSSFLYHSYIENLKSTKEYVYFIYLQDIYYNINIFKNKGRLYISNNGLCNDKLKDNNNNNNINSNNFGNSYNAYTKKKSFYHSFNDLNEAKEIRKKRKNEKSEKNIVEYLLCNIINPNENYHIQNIYNHNLNNNVSIEIHKKNDSVMYHYNNEKKTKTSKMTTDIKLKQINNVYIKYVPYKNKIITLACPNKYYPTLYRYFSSHTNKKEDAEENDKNKNININNVDNRYKEDFMYGCENKNDSEKHKKTTNNNFGDEFEKLKVKELDKILNKLEMLYDNKNNKMNINVKILGYIFKNFLLKNKELKRKIFCSLFFLLCSKMAIIYTPILLSTFIENVNLQKSLSNNIDIYSTNKSSVLLLCAYVFSRVLSSTMNELRNSVFSNISQKISTFVSKLFFYKIHNLNLTYILSKKNGELSFIFNRGCKSITNLLNVMVFQIIPIIIEFILYLYILTYKIHYTVSLVTCFNMFLYVLFTTLITKRRTIIRKHMNKAEQNTFNIFLDSIQNVEQVKYYTNEIHELKKFIKEQKKYEKEAINVQKSLSFLNFGQQIILNTNLFLCMYLTYLNIANDIFPFSYLILVNTLLFQLAMPLNMFGTIYRETKLSLVDIESMIKILVKKIKSPDYGNQMLIKNGNIKFENVYFKYPLNEDINGLEQNYQAKEKDPNIINNINNINNINNINNINNINSINNIYTFESNVKNISSTNMITSSINKLKKWYLDKVKDNKKNVQYNNNDVKKTNPNITKNLNKEIKENINTHLKNHKIINNSPNYNNNNYLFQNFTCNIENGEKVAIIGKSGSGKSSLIKLLLKFYEVNSGNIYIDNKNIDDIDLYTLRKNISVVPQDTILFNNTISYNIKYGNFQCTDKQMIQASIKAELHDKIMKMENKYDTIVGERGTKLSIGEKQRICIARCFLKDSKIIVLDEHASNLDNENKKAIEKALTKLCMGKTTFIITHVMENLKHMDKIIFFCGKNIYVGSHKNLMDDNHFYREYYDSKNNKML

[Multiple Choices]
A. inclusion body
B. ATP-binding cassette (ABC) transporter complex
C. mitochondrial membrane
D. transcription regulator complex
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

> The sequence matches the UniProt entry for Plasmodium falciparum ATM1, which annotates the protein to the mitochondrial membrane and describes it as a multipass membrane protein. The annotation cites a 2024 paper; this supports the key, though the paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C9](#evidence-c9), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic regions and a C-terminal ABC-type ATP-binding domain, supporting a membrane-associated ABC transporter rather than an inclusion body or transcription regulator complex. Those features do not reliably distinguish mitochondrial membrane from another membrane.


**Missing item-specific fact**

> The protein-specific evidence that this Plasmodium ATM1 transporter localizes to the mitochondrial membrane.


**Reason**

> The sequence supports membrane-protein identity, but the mitochondrial assignment requires item-specific localization knowledge; recognizing the exact protein would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices mix a localization with a transporter complex identity, but the question asks where the protein resides. The sequence supports membrane association, while the evidence identifies the mitochondrial membrane as the location.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but the author's original source snapshot is unknown.
- The cited subcellular-location annotation is manually supported in UniProt; the cited primary paper was not independently examined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic regions and a C-terminal ABC-type ATP-binding domain, supporting a membrane-associated ABC transporter rather than an inclusion body or transcription regulator complex. Those features do not reliably distinguish mitochondrial membrane from another membrane.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific evidence that this Plasmodium ATM1 transporter localizes to the mitochondrial membrane.",
    "reason": "The sequence supports membrane-protein identity, but the mitochondrial assignment requires item-specific localization knowledge; recognizing the exact protein would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "GO_cellular_component_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C9",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for Plasmodium falciparum ATM1, which annotates the protein to the mitochondrial membrane and describes it as a multipass membrane protein. The annotation cites a 2024 paper; this supports the key, though the paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but the author's original source snapshot is unknown.",
    "The cited subcellular-location annotation is manually supported in UniProt; the cited primary paper was not independently examined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices mix a localization with a transporter complex identity, but the question asks where the protein resides. The sequence supports membrane association, while the evidence identifies the mitochondrial membrane as the location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for Plasmodium falciparum ATM1, which annotates the protein to the mitochondrial membrane and describes it as a multipass membrane protein. The annotation cites a 2024 paper; this supports the key, though the paper was not independently reviewed here.",
    "evidence_ids": ["C5", "C9", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic regions and a C-terminal ABC-type ATP-binding domain, supporting a membrane-associated ABC transporter rather than an inclusion body or transcription regulator complex. Those features do not reliably distinguish mitochondrial membrane from another membrane.",
    "missing_item_specific_fact": "The protein-specific evidence that this Plasmodium ATM1 transporter localizes to the mitochondrial membrane.",
    "reason": "The sequence supports membrane-protein identity, but the mitochondrial assignment requires item-specific localization knowledge; recognizing the exact protein would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices mix a localization with a transporter complex identity, but the question asks where the protein resides. The sequence supports membrane association, while the evidence identifies the mitochondrial membrane as the location."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but the author's original source snapshot is unknown.",
    "The cited subcellular-location annotation is manually supported in UniProt; the cited primary paper was not independently examined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8IDH9 (ATM1_PLAF7) explicitly annotates the subcellular location as 'Mitochondrion membrane' with evidence code ECO:0000305|PubMed:39348385 (direct experimental evidence from the 2024 PLoS Pathogens paper by Shrivastava et al., which experimentally determined mitochondrial membrane localization). The GO cross-reference GO:0031966 (mitochondrial membrane) is also present. The protein is a multi-pass membrane protein (ECO:0000255). The sequence matches the benchmark exactly (1049 aa, SHA256 confirmed). The expected answer C (mitochondrial membrane) is directly supported by experimental annotation.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [C9](#evidence-c9), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence clearly encodes a multi-pass membrane protein (multiple hydrophobic stretches spanning ~50-60 residues) with an intact ABC transporter nucleotide-binding domain (Walker A motif GKSGSGKS, Walker B motif LLDE, ABC signature). This eliminates A (inclusion body) and D (transcription regulator complex) since the protein is membrane-integrated, not aggregated or nuclear. Option B (ABC transporter complex, GO:0043190) is defined as a multi-subunit complex forming a pore through the plasma membrane, typically with four core domains (two TMDs + two NBDs). This protein is a single-polypeptide half-transporter (one TMD + one NBD), architecturally inconsistent with the 'complex' definition. By elimination and by recognizing that half-transporter ABCB-type proteins are characteristically mitochondrial, C (mitochondrial membrane) is the most defensible answer.


**Missing item-specific fact**

> Positive confirmation of mitochondrial (rather than ER or other internal membrane) targeting is not trivially derivable from the sequence alone, as Plasmodium uses non-classical mitochondrial targeting signals. However, the elimination logic via GO term definitions and half-transporter architecture provides a defensible reasoning path.


**Reason**

> The sequence provides sufficient information to eliminate options A and D (membrane protein features), and the GO ontology definition of GO:0043190 (plasma membrane multi-subunit complex) combined with the observed half-transporter architecture (single NBD + single TMD) provides a concrete biological argument to eliminate B. General knowledge that ABCB-family half-transporters are typically mitochondrial supports the positive selection of C. The reasoning chain does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the protein is functionally an ABC transporter, the GO term GO:0043190 (option B) specifically denotes a plasma membrane multi-subunit complex, which is architecturally and topologically distinct from a single-polypeptide half-transporter in an internal membrane. Once the GO term definition is understood, B is clearly distinguishable from C. The remaining options (A, D) are eliminated by the obvious membrane-protein and transporter-domain features.


### Important caveats

- The experimental evidence for mitochondrial membrane localization (PubMed:39348385, 2024) post-dates the original genome publication (2003). The author's annotation source snapshot is unknown; if the question was constructed before 2024, the localization may have been inferred computationally rather than experimentally.
- The mitochondrial targeting signal in Plasmodium is non-classical and not readily identifiable by standard prediction tools from the N-terminal sequence, making positive identification of 'mitochondrial' (vs. ER or other internal membrane) more challenging from sequence alone.
- The GO term GO:0043190 definition explicitly restricts to plasma membrane complexes, but a model unfamiliar with this specific GO definition might not apply this distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly encodes a multi-pass membrane protein (multiple hydrophobic stretches spanning ~50-60 residues) with an intact ABC transporter nucleotide-binding domain (Walker A motif GKSGSGKS, Walker B motif LLDE, ABC signature). This eliminates A (inclusion body) and D (transcription regulator complex) since the protein is membrane-integrated, not aggregated or nuclear. Option B (ABC transporter complex, GO:0043190) is defined as a multi-subunit complex forming a pore through the plasma membrane, typically with four core domains (two TMDs + two NBDs). This protein is a single-polypeptide half-transporter (one TMD + one NBD), architecturally inconsistent with the 'complex' definition. By elimination and by recognizing that half-transporter ABCB-type proteins are characteristically mitochondrial, C (mitochondrial membrane) is the most defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive confirmation of mitochondrial (rather than ER or other internal membrane) targeting is not trivially derivable from the sequence alone, as Plasmodium uses non-classical mitochondrial targeting signals. However, the elimination logic via GO term definitions and half-transporter architecture provides a defensible reasoning path.",
    "reason": "The sequence provides sufficient information to eliminate options A and D (membrane protein features), and the GO ontology definition of GO:0043190 (plasma membrane multi-subunit complex) combined with the observed half-transporter architecture (single NBD + single TMD) provides a concrete biological argument to eliminate B. General knowledge that ABCB-family half-transporters are typically mitochondrial supports the positive selection of C. The reasoning chain does not require memorizing this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5",
      "C9",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8IDH9 (ATM1_PLAF7) explicitly annotates the subcellular location as 'Mitochondrion membrane' with evidence code ECO:0000305|PubMed:39348385 (direct experimental evidence from the 2024 PLoS Pathogens paper by Shrivastava et al., which experimentally determined mitochondrial membrane localization). The GO cross-reference GO:0031966 (mitochondrial membrane) is also present. The protein is a multi-pass membrane protein (ECO:0000255). The sequence matches the benchmark exactly (1049 aa, SHA256 confirmed). The expected answer C (mitochondrial membrane) is directly supported by experimental annotation."
  },
  "important_caveats": [
    "The experimental evidence for mitochondrial membrane localization (PubMed:39348385, 2024) post-dates the original genome publication (2003). The author's annotation source snapshot is unknown; if the question was constructed before 2024, the localization may have been inferred computationally rather than experimentally.",
    "The mitochondrial targeting signal in Plasmodium is non-classical and not readily identifiable by standard prediction tools from the N-terminal sequence, making positive identification of 'mitochondrial' (vs. ER or other internal membrane) more challenging from sequence alone.",
    "The GO term GO:0043190 definition explicitly restricts to plasma membrane complexes, but a model unfamiliar with this specific GO definition might not apply this distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the protein is functionally an ABC transporter, the GO term GO:0043190 (option B) specifically denotes a plasma membrane multi-subunit complex, which is architecturally and topologically distinct from a single-polypeptide half-transporter in an internal membrane. Once the GO term definition is understood, B is clearly distinguishable from C. The remaining options (A, D) are eliminated by the obvious membrane-protein and transporter-domain features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IDH9 (ATM1_PLAF7) explicitly annotates the subcellular location as 'Mitochondrion membrane' with evidence code ECO:0000305|PubMed:39348385 (direct experimental evidence from the 2024 PLoS Pathogens paper by Shrivastava et al., which experimentally determined mitochondrial membrane localization). The GO cross-reference GO:0031966 (mitochondrial membrane) is also present. The protein is a multi-pass membrane protein (ECO:0000255). The sequence matches the benchmark exactly (1049 aa, SHA256 confirmed). The expected answer C (mitochondrial membrane) is directly supported by experimental annotation.",
    "evidence_ids": ["C5", "C7", "H3", "H5", "C9", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence clearly encodes a multi-pass membrane protein (multiple hydrophobic stretches spanning ~50-60 residues) with an intact ABC transporter nucleotide-binding domain (Walker A motif GKSGSGKS, Walker B motif LLDE, ABC signature). This eliminates A (inclusion body) and D (transcription regulator complex) since the protein is membrane-integrated, not aggregated or nuclear. Option B (ABC transporter complex, GO:0043190) is defined as a multi-subunit complex forming a pore through the plasma membrane, typically with four core domains (two TMDs + two NBDs). This protein is a single-polypeptide half-transporter (one TMD + one NBD), architecturally inconsistent with the 'complex' definition. By elimination and by recognizing that half-transporter ABCB-type proteins are characteristically mitochondrial, C (mitochondrial membrane) is the most defensible answer.",
    "missing_item_specific_fact": "Positive confirmation of mitochondrial (rather than ER or other internal membrane) targeting is not trivially derivable from the sequence alone, as Plasmodium uses non-classical mitochondrial targeting signals. However, the elimination logic via GO term definitions and half-transporter architecture provides a defensible reasoning path.",
    "reason": "The sequence provides sufficient information to eliminate options A and D (membrane protein features), and the GO ontology definition of GO:0043190 (plasma membrane multi-subunit complex) combined with the observed half-transporter architecture (single NBD + single TMD) provides a concrete biological argument to eliminate B. General knowledge that ABCB-family half-transporters are typically mitochondrial supports the positive selection of C. The reasoning chain does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the protein is functionally an ABC transporter, the GO term GO:0043190 (option B) specifically denotes a plasma membrane multi-subunit complex, which is architecturally and topologically distinct from a single-polypeptide half-transporter in an internal membrane. Once the GO term definition is understood, B is clearly distinguishable from C. The remaining options (A, D) are eliminated by the obvious membrane-protein and transporter-domain features."
  },
  "important_caveats": [
    "The experimental evidence for mitochondrial membrane localization (PubMed:39348385, 2024) post-dates the original genome publication (2003). The author's annotation source snapshot is unknown; if the question was constructed before 2024, the localization may have been inferred computationally rather than experimentally.",
    "The mitochondrial targeting signal in Plasmodium is non-classical and not readily identifiable by standard prediction tools from the N-terminal sequence, making positive identification of 'mitochondrial' (vs. ER or other internal membrane) more challenging from sequence alone.",
    "The GO term GO:0043190 definition explicitly restricts to plasma membrane complexes, but a model unfamiliar with this specific GO definition might not apply this distinction."
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

**Accession:** `Q8IDH9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 148. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"39348385","source":"PubMed"}],"id":"SL-0171","value":"Mitochondrion membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/uniProtKBCrossReferences/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"database":"GO","id":"GO:0031966","properties":[{"key":"GoTerm","value":"C:mitochondrial membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"citation":{"authors":["Shrivastava D.","Abboud E.","Ramchandra J.P.","Jha A.","Marq J.B.","Chaurasia A.","Mitra K.","Sadik M.","Siddiqi M.I.","Soldati-Favre D.","Kloehn J.","Habib S."],"citationCrossReferences":[{"database":"PubMed","id":"39348385"},{"database":"DOI","id":"10.1371/journal.ppat.1012593"}],"citationType":"journal article","firstPage":"e1012593","id":"39348385","journal":"PLoS Pathog.","lastPage":"e1012593","publicationDate":"2024","title":"ATM1, an essential conserved transporter in Apicomplexa, bridges mitochondrial and cytosolic [Fe-S] biogenesis.","volume":"20"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","INTERACTION WITH ISCU; ISCA2; MHCF101/CFD1 AND NBP35","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE","MUTAGENESIS OF ARG-534 AND GLU-972"]}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 53-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, SUBUNIT, INTERACTION WITH ISCU; ISCA2; MHCF101/CFD1 AND NBP35,
RP   SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF ARG-534 AND
RP   GLU-972.
RX   PubMed=39348385; DOI=10.1371/journal.ppat.1012593;
RA   Shrivastava D., Abboud E., Ramchandra J.P., Jha A., Marq J.B.,
RA   Chaurasia A., Mitra K., Sadik M., Siddiqi M.I., Soldati-Favre D.,
RA   Kloehn J., Habib S.;
RT   "ATM1, an essential conserved transporter in Apicomplexa, bridges
RT   mitochondrial and cytosolic [Fe-S] biogenesis.";
RL   PLoS Pathog. 20:e1012593-e1012593(2024).
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 85-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion membrane
CC       {ECO:0000305|PubMed:39348385}; Multi-pass membrane protein
CC       {ECO:0000255}.
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 116-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
DR   GO; GO:0031966; C:mitochondrial membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
