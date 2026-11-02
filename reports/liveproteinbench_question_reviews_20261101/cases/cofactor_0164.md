# cofactor_0164

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — &#91;2Fe-2S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTANPTSIHQRLDRRLSGFSLEQPFYTSPEVYALDLQHIFYKQWLYAVPVCQLAKAGSYTTLRVGAYEVVIVRSRDGEVRAFHNSCRHRGSLICKARQGQVAKLVCPYHQWTYELDGKLIWANDMGPDFDASKYGLKPVNLRNLDGLIYICLSDTPPDFQTFAQLARPYLEVHDLKDAKVAFTSTIIEKGNWKLVWENNRECYHCSSNHPALCRSFPLDPEVAGVQADGGVSKKLQAHFDRCEAAGTPAQFVLAGDGQYRLARMPLQEKALSYTMDGKAAVSRHLGRVAPPDAGTLLMFHYPSTWNHFLPDHSLTFRVMPISPTETEVTTTWLVHKDAVEGVDYDLKRLTEVWIATNDEDREIVETNQQGILSPAYVPGPYSPGQESGVMQFVDWYAASLERALAPRQVAAE

[Multiple Choices]
A. Fe cation
B. [2Fe-2S] cluster
C. Zn(2+)
D. pyridoxal 5'-phosphate
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact-matched protein is annotated as binding one &#91;2Fe-2S&#93; cluster per subunit, with evidence linked to experimental studies and structures.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a cysteine/histidine ligand pattern compatible with a Rieske &#91;2Fe-2S&#93; center, providing a biological basis to favor B over the other choices.


**Missing item-specific fact**

> The input does not state the protein’s experimentally established cofactor inventory or stoichiometry; those details are needed to know that it also binds a separate Fe cation.


**Reason**

> The sequence motif gives a meaningful basis for inferring a Rieske cluster, though it does not make that the protein’s only required cofactor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The matched protein is annotated as binding both one &#91;2Fe-2S&#93; cluster and one Fe cation per subunit, so both listed options are required cofactors under the wording.


### Important caveats

- The reviewer-only database and structural evidence supports the key but was not supplied to the evaluated model.
- The evidence identifies the same sequence, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine/histidine ligand pattern compatible with a Rieske [2Fe-2S] center, providing a biological basis to favor B over the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The input does not state the protein’s experimentally established cofactor inventory or stoichiometry; those details are needed to know that it also binds a separate Fe cation.",
    "reason": "The sequence motif gives a meaningful basis for inferring a Rieske cluster, though it does not make that the protein’s only required cofactor."
  },
  "case_id": "cofactor_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact-matched protein is annotated as binding one [2Fe-2S] cluster per subunit, with evidence linked to experimental studies and structures."
  },
  "important_caveats": [
    "The reviewer-only database and structural evidence supports the key but was not supplied to the evaluated model.",
    "The evidence identifies the same sequence, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The matched protein is annotated as binding both one [2Fe-2S] cluster and one Fe cation per subunit, so both listed options are required cofactors under the wording."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched protein is annotated as binding one [2Fe-2S] cluster per subunit, with evidence linked to experimental studies and structures.",
    "evidence_ids": ["C5", "C7", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a cysteine/histidine ligand pattern compatible with a Rieske [2Fe-2S] center, providing a biological basis to favor B over the other choices.",
    "missing_item_specific_fact": "The input does not state the protein’s experimentally established cofactor inventory or stoichiometry; those details are needed to know that it also binds a separate Fe cation.",
    "reason": "The sequence motif gives a meaningful basis for inferring a Rieske cluster, though it does not make that the protein’s only required cofactor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The matched protein is annotated as binding both one [2Fe-2S] cluster and one Fe cation per subunit, so both listed options are required cofactors under the wording."
  },
  "important_caveats": [
    "The reviewer-only database and structural evidence supports the key but was not supplied to the evaluated model.",
    "The evidence identifies the same sequence, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q92ZP9 (Stachydrine N-demethylase, STC2_RHIME) explicitly annotates a &#91;2Fe-2S&#93; cluster as a cofactor with experimental evidence (ECO:0000269, X-ray crystallography at 1.59 Å and 2.20 Å in complex with iron and iron-sulfur 2Fe-2S). The protein is named 'Rieske-type mononuclear non-heme enzyme,' and Rieske-type enzymes characteristically contain a &#91;2Fe-2S&#93; cluster. However, the same entry also annotates a mononuclear Fe cation (CHEBI:24875) as a cofactor with the same experimental evidence (C6, H7). Thus B is supported but not uniquely so.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could argue that recognizing the Rieske-type CxxHxxH motif from sequence would point to a &#91;2Fe-2S&#93; cluster. However, the sequence does not present a clean, textbook-canonical Rieske motif that is unambiguously recognizable without prior knowledge of Rieske-type mononuclear non-heme oxygenases. Moreover, even if the Rieske cluster were identified, the same enzyme also requires a mononuclear Fe cation at its catalytic center, so the sequence provides no grounds to prefer &#91;2Fe-2S&#93; over Fe cation as 'the' cofactor.


**Missing item-specific fact**

> The specific identity of the protein (Stachydrine N-demethylase, EC 1.14.13.247) and the experimental determination that it binds both a &#91;2Fe-2S&#93; cluster and a mononuclear Fe cation are not derivable from the sequence alone. The question requires knowing which of the two experimentally verified cofactors the author considers 'the' answer.


**Reason**

> Selection of B over A depends on knowing the protein is a Rieske-type enzyme and on the author's choice to treat the &#91;2Fe-2S&#93; cluster as the primary cofactor despite the mononuclear Fe cation being equally annotated. Neither the sequence nor general biology cleanly resolves which of the two experimentally confirmed cofactors is 'the correct' answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The UniProt entry lists both &#91;2Fe-2S&#93; cluster (C5/H6) and Fe cation (C6/H7) as cofactors, each with the same experimental evidence (X-ray crystallography, PubMed 22224443 and 26996959). The protein is a Rieske-type mononuclear non-heme enzyme, meaning it uses both a Rieske &#91;2Fe-2S&#93; cluster for electron transfer and a mononuclear Fe at the active site for catalysis. Both are essential for catalytic activity. The question's phrasing ('the specific cofactor') implies a single answer, but the evidence supports both A and B as required cofactors.


### Important caveats

- The author's key (B) is not contradicted — &#91;2Fe-2S&#93; is indeed a cofactor — but option A (Fe cation) is equally supported by the same experimental evidence, creating a genuine ambiguity.
- The Rieske-type designation is the key contextual clue that links the protein to a &#91;2Fe-2S&#93; cluster, but this designation is not provided in the model input and must be inferred from sequence or recalled from database knowledge.
- The sequence-match is confirmed (SHA-256 identical between benchmark and UniProt Q92ZP9), so the annotations apply directly to the supplied sequence.
- The entry was first public in April 2025; the author's source snapshot date is unknown, but the historical entry version 138 (Jan 2026) already contains both cofactor annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could argue that recognizing the Rieske-type CxxHxxH motif from sequence would point to a [2Fe-2S] cluster. However, the sequence does not present a clean, textbook-canonical Rieske motif that is unambiguously recognizable without prior knowledge of Rieske-type mononuclear non-heme oxygenases. Moreover, even if the Rieske cluster were identified, the same enzyme also requires a mononuclear Fe cation at its catalytic center, so the sequence provides no grounds to prefer [2Fe-2S] over Fe cation as 'the' cofactor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of the protein (Stachydrine N-demethylase, EC 1.14.13.247) and the experimental determination that it binds both a [2Fe-2S] cluster and a mononuclear Fe cation are not derivable from the sequence alone. The question requires knowing which of the two experimentally verified cofactors the author considers 'the' answer.",
    "reason": "Selection of B over A depends on knowing the protein is a Rieske-type enzyme and on the author's choice to treat the [2Fe-2S] cluster as the primary cofactor despite the mononuclear Fe cation being equally annotated. Neither the sequence nor general biology cleanly resolves which of the two experimentally confirmed cofactors is 'the correct' answer."
  },
  "case_id": "cofactor_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q92ZP9 (Stachydrine N-demethylase, STC2_RHIME) explicitly annotates a [2Fe-2S] cluster as a cofactor with experimental evidence (ECO:0000269, X-ray crystallography at 1.59 Å and 2.20 Å in complex with iron and iron-sulfur 2Fe-2S). The protein is named 'Rieske-type mononuclear non-heme enzyme,' and Rieske-type enzymes characteristically contain a [2Fe-2S] cluster. However, the same entry also annotates a mononuclear Fe cation (CHEBI:24875) as a cofactor with the same experimental evidence (C6, H7). Thus B is supported but not uniquely so."
  },
  "important_caveats": [
    "The author's key (B) is not contradicted — [2Fe-2S] is indeed a cofactor — but option A (Fe cation) is equally supported by the same experimental evidence, creating a genuine ambiguity.",
    "The Rieske-type designation is the key contextual clue that links the protein to a [2Fe-2S] cluster, but this designation is not provided in the model input and must be inferred from sequence or recalled from database knowledge.",
    "The sequence-match is confirmed (SHA-256 identical between benchmark and UniProt Q92ZP9), so the annotations apply directly to the supplied sequence.",
    "The entry was first public in April 2025; the author's source snapshot date is unknown, but the historical entry version 138 (Jan 2026) already contains both cofactor annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The UniProt entry lists both [2Fe-2S] cluster (C5/H6) and Fe cation (C6/H7) as cofactors, each with the same experimental evidence (X-ray crystallography, PubMed 22224443 and 26996959). The protein is a Rieske-type mononuclear non-heme enzyme, meaning it uses both a Rieske [2Fe-2S] cluster for electron transfer and a mononuclear Fe at the active site for catalysis. Both are essential for catalytic activity. The question's phrasing ('the specific cofactor') implies a single answer, but the evidence supports both A and B as required cofactors."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q92ZP9 (Stachydrine N-demethylase, STC2_RHIME) explicitly annotates a [2Fe-2S] cluster as a cofactor with experimental evidence (ECO:0000269, X-ray crystallography at 1.59 Å and 2.20 Å in complex with iron and iron-sulfur 2Fe-2S). The protein is named 'Rieske-type mononuclear non-heme enzyme,' and Rieske-type enzymes characteristically contain a [2Fe-2S] cluster. However, the same entry also annotates a mononuclear Fe cation (CHEBI:24875) as a cofactor with the same experimental evidence (C6, H7). Thus B is supported but not uniquely so.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could argue that recognizing the Rieske-type CxxHxxH motif from sequence would point to a [2Fe-2S] cluster. However, the sequence does not present a clean, textbook-canonical Rieske motif that is unambiguously recognizable without prior knowledge of Rieske-type mononuclear non-heme oxygenases. Moreover, even if the Rieske cluster were identified, the same enzyme also requires a mononuclear Fe cation at its catalytic center, so the sequence provides no grounds to prefer [2Fe-2S] over Fe cation as 'the' cofactor.",
    "missing_item_specific_fact": "The specific identity of the protein (Stachydrine N-demethylase, EC 1.14.13.247) and the experimental determination that it binds both a [2Fe-2S] cluster and a mononuclear Fe cation are not derivable from the sequence alone. The question requires knowing which of the two experimentally verified cofactors the author considers 'the' answer.",
    "reason": "Selection of B over A depends on knowing the protein is a Rieske-type enzyme and on the author's choice to treat the [2Fe-2S] cluster as the primary cofactor despite the mononuclear Fe cation being equally annotated. Neither the sequence nor general biology cleanly resolves which of the two experimentally confirmed cofactors is 'the correct' answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The UniProt entry lists both [2Fe-2S] cluster (C5/H6) and Fe cation (C6/H7) as cofactors, each with the same experimental evidence (X-ray crystallography, PubMed 22224443 and 26996959). The protein is a Rieske-type mononuclear non-heme enzyme, meaning it uses both a Rieske [2Fe-2S] cluster for electron transfer and a mononuclear Fe at the active site for catalysis. Both are essential for catalytic activity. The question's phrasing ('the specific cofactor') implies a single answer, but the evidence supports both A and B as required cofactors."
  },
  "important_caveats": [
    "The author's key (B) is not contradicted — [2Fe-2S] is indeed a cofactor — but option A (Fe cation) is equally supported by the same experimental evidence, creating a genuine ambiguity.",
    "The Rieske-type designation is the key contextual clue that links the protein to a [2Fe-2S] cluster, but this designation is not provided in the model input and must be inferred from sequence or recalled from database knowledge.",
    "The sequence-match is confirmed (SHA-256 identical between benchmark and UniProt Q92ZP9), so the annotations apply directly to the supplied sequence.",
    "The entry was first public in April 2025; the author's source snapshot date is unknown, but the historical entry version 138 (Jan 2026) already contains both cofactor annotations."
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

**Accession:** `Q92ZP9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 138. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:35.950168+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:190135"},"evidences":[{"evidenceCode":"ECO:0000269","id":"22224443","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26996959","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"Ref.5","source":"Reference"}],"name":"[2Fe-2S] cluster"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22224443","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26996959","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"Ref.5","source":"Reference"}],"value":"Binds 1 [2Fe-2S] cluster per subunit."}]}}
```

Source SHA-256: `276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:35.950168+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:24875"},"evidences":[{"evidenceCode":"ECO:0000269","id":"22224443","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26996959","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"Ref.5","source":"Reference"}],"name":"Fe cation"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22224443","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26996959","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"Ref.5","source":"Reference"}],"value":"Binds 1 Fe cation per subunit."}]}}
```

Source SHA-256: `276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:35.950168+00:00.  

```json
{"citation":{"authors":["Daughtry K.D.","Xiao Y.","Stoner-Ma D.","Cho E.","Orville A.M.","Liu P.","Allen K.N."],"citationCrossReferences":[{"database":"PubMed","id":"22224443"},{"database":"DOI","id":"10.1021/ja2111898"}],"citationType":"journal article","firstPage":"2823","id":"22224443","journal":"J. Am. Chem. Soc.","lastPage":"2834","publicationDate":"2012","title":"Quaternary ammonium oxidative demethylation: X-ray crystallographic, resonance Raman, and UV-visible spectroscopic analysis of a Rieske-type demethylase.","volume":"134"},"evidences":[{"evidenceCode":"ECO:0007744","id":"3VCA","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"3VCP","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"1021"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.59 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR (2FE-2S)","FUNCTION","CATALYTIC ACTIVITY","REACTION MECHANISM","COFACTOR","SUBUNIT"]}
```

Source SHA-256: `276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:35.950168+00:00.  

```json
{"citation":{"authors":["Roessler C.G.","Agarwal R.","Allaire M.","Alonso-Mori R.","Andi B.","Bachega J.F.","Bommer M.","Brewster A.S.","Browne M.C.","Chatterjee R.","Cho E.","Cohen A.E.","Cowan M.","Datwani S.","Davidson V.L.","Defever J.","Eaton B.","Ellson R.","Feng Y.","Ghislain L.P.","Glownia J.M.","Han G.","Hattne J.","Hellmich J.","Heroux A.","Ibrahim M.","Kern J.","Kuczewski A.","Lemke H.T.","Liu P.","Majlof L.","McClintock W.M.","Myers S.","Nelsen S.","Olechno J.","Orville A.M.","Sauter N.K.","Soares A.S.","Soltis S.M.","Song H.","Stearns R.G.","Tran R.","Tsai Y.","Uervirojnangkoorn M.","Wilmot C.M.","Yachandra V.","Yano J.","Yukl E.T.","Zhu D.","Zouni A."],"citationCrossReferences":[{"database":"PubMed","id":"26996959"},{"database":"DOI","id":"10.1016/j.str.2016.02.007"}],"citationType":"journal article","firstPage":"631","id":"26996959","journal":"Structure","lastPage":"640","publicationDate":"2016","title":"Acoustic Injectors for Drop-On-Demand Serial Femtosecond Crystallography.","volume":"24"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5HL4","source":"PDB"}],"referenceNumber":6,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR (2FE-2S)","COFACTOR"]}
```

Source SHA-256: `276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)  
**Locator:** `lines 56-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 138 / 1.  
**Retrieved:** 2026-11-02T04:32:39.981731+00:00.  

```text
RN   [4] {ECO:0007744|PDB:3VCA, ECO:0007744|PDB:3VCP}
RP   X-RAY CRYSTALLOGRAPHY (1.59 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR
RP   (2FE-2S), FUNCTION, CATALYTIC ACTIVITY, REACTION MECHANISM, COFACTOR, AND
RP   SUBUNIT.
RC   STRAIN=1021;
RX   PubMed=22224443; DOI=10.1021/ja2111898;
RA   Daughtry K.D., Xiao Y., Stoner-Ma D., Cho E., Orville A.M., Liu P.,
RA   Allen K.N.;
RT   "Quaternary ammonium oxidative demethylation: X-ray crystallographic,
RT   resonance Raman, and UV-visible spectroscopic analysis of a Rieske-type
RT   demethylase.";
RL   J. Am. Chem. Soc. 134:2823-2834(2012).
```

Source SHA-256: `654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)  
**Locator:** `lines 74-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 138 / 1.  
**Retrieved:** 2026-11-02T04:32:39.981731+00:00.  

```text
RN   [6] {ECO:0007744|PDB:5HL4}
RP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR
RP   (2FE-2S), AND COFACTOR.
RX   PubMed=26996959; DOI=10.1016/j.str.2016.02.007;
RA   Roessler C.G., Agarwal R., Allaire M., Alonso-Mori R., Andi B.,
RA   Bachega J.F., Bommer M., Brewster A.S., Browne M.C., Chatterjee R., Cho E.,
RA   Cohen A.E., Cowan M., Datwani S., Davidson V.L., Defever J., Eaton B.,
RA   Ellson R., Feng Y., Ghislain L.P., Glownia J.M., Han G., Hattne J.,
RA   Hellmich J., Heroux A., Ibrahim M., Kern J., Kuczewski A., Lemke H.T.,
RA   Liu P., Majlof L., McClintock W.M., Myers S., Nelsen S., Olechno J.,
RA   Orville A.M., Sauter N.K., Soares A.S., Soltis S.M., Song H., Stearns R.G.,
RA   Tran R., Tsai Y., Uervirojnangkoorn M., Wilmot C.M., Yachandra V., Yano J.,
RA   Yukl E.T., Zhu D., Zouni A.;
RT   "Acoustic Injectors for Drop-On-Demand Serial Femtosecond
RT   Crystallography.";
RL   Structure 24:631-640(2016).
```

Source SHA-256: `654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)  
**Locator:** `lines 111-117`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 138 / 1.  
**Retrieved:** 2026-11-02T04:32:39.981731+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[2Fe-2S] cluster; Xref=ChEBI:CHEBI:190135;
CC         Evidence={ECO:0000269|PubMed:22224443, ECO:0000269|PubMed:26996959,
CC         ECO:0000269|Ref.5};
CC       Note=Binds 1 [2Fe-2S] cluster per subunit.
CC       {ECO:0000269|PubMed:22224443, ECO:0000269|PubMed:26996959,
CC       ECO:0000269|Ref.5};
```

Source SHA-256: `654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)  
**Locator:** `lines 118-123`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 138 / 1.  
**Retrieved:** 2026-11-02T04:32:39.981731+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Fe cation; Xref=ChEBI:CHEBI:24875;
CC         Evidence={ECO:0000269|PubMed:22224443, ECO:0000269|PubMed:26996959,
CC         ECO:0000269|Ref.5};
CC       Note=Binds 1 Fe cation per subunit. {ECO:0000269|PubMed:22224443,
CC       ECO:0000269|PubMed:26996959, ECO:0000269|Ref.5};
```

Source SHA-256: `654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 164. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
