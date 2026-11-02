# cofactor_0063

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Ca(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTNGADPLGRFSALTREWFTTAFAAPTPAQADAWSAISEGNNTLVIAPTGSGKTLAAFLWAIDRLADPAREPSQGTQVLYVSPLKALAVDVERNLRTPLTGITRVAERHGLPAPSITVGVRSGDTPPNQRRAMIANPPDVLITTPESLFLMLTSAARETLTSVRTVIVDEVHAVAATKRGAHLALSLERLDQLLDTPAQRIGLSATVRPPEEVARFLSGQAPTTIVCPPAAKTFDLSVQVPVPDMANLDNNSIWPDVEERIVDLVEAHNSSIVFANSRRLAERLTSRLNEIHAERSGIELPAGPNPEVGGGAPAHLMGSGQANGAPPLLARAHHGSVSKEQRAQVEDDLKSGRLRAVVATSSLELGIDMGAVDLVIQVEAPPSVASGLQRVGRAGHQVGEISQGVLFPKHRTDLIGCAVTVQRMQTGDIETLRVPANPLDVLAQHTVAVAALEPVDADAWFDAVRRSAPFATLPRSAFEATLDLLSGKYPSTEFAELRPRLVYDRDTGTLTARPGAQRLAVTSGGAIPDRGMFTVYLASETEKPSRVGELDEEMVYESRPGDVISLGATSWRITEITHDRVLVIPAPGQPARLPFWRGDSVGRPAELGAAVGAFTGELASLDRKAFDKRCQKMGFAGYATDNLHQLLREQREATGVVPSDTTFVVERFRDELGDWRVILHSPYGLRVHGPLALAVGRRLRERYGIDEKPTASDDGIIVRLPDSGDTPPGADLFVFDADEIEPIVTAEVGGSALFASRFRECAARALLLPRRHPGKRSPLWHQRQRAAQLLDIARKYPDFPIVLEAVRECLQDVYDVPALIELMHKIAQRRLRIVEVETATPSPFAASLLFGYVGAFMYEGDSPLAERRAAALALDTVLLSELLGRVELRELLDPAVVASTSAQLQHLTPERAARDAEGVADLLRLLGPLTEADIAQRCTADNIGAWLDGLHAAKRALPVTYAGQTWWAAVEDIGLLRDGIGVPVPVGVPAAFTESASDPLGDLIGRYARTRGPFTTEQTAARFGLGVRVASDVLSRMAVDGRLIRGEFAADLSGEQWCDAQVLKILRRRSLAALRAQVEPVSTDAYARFLPSWQHVGSTNTTGIDGLATVIEQLAGVPIPASAVESLVFPQRVRDYQPAMLDELLASGEVMWSGAGQIGNGDGWVAFHLADTAPLTLTHGAEIEFTDTHRVILETLGHGGAYFFRQLTDGTVEGTAGQELKQALWELIWAGWVTGDTFAPVRAVLSGPRRSGAPAHRQRQRPPRLSRYSVAHAQTRGTDPTVSGRWSALPAAEPDSTVRAHFQAELLLGRHGVLTKGAVGAEGVPGGFATLYKVLSTFEDAGRCQRGYFVESLGGAQFAVASTVDRLRSYLDNVDPERPEYHAVVLAATDPANPYGAALGWPTDSEAHRPGRKAGALVALVDGRLVWFLERGGRSLLSFGADADAQRAAAGALTDLVSAGRIPSLLVERINGVAVLDPDVDAERAVVQDALLGAGLSRTPRGLRLR

[Multiple Choices]
A. Na(+)
B. Ca(2+)
C. Co(2+)
D. Mn(2+)
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

> The sequence exactly matches the cited Lhr protein entry, which records Ca(2+) as a cofactor based on experimental evidence and says its ssDNA-dependent ATPase is most efficient with Ca(2+). This supports B as the preferred cofactor, though it does not establish that Ca(2+) is strictly required.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with an ATPase/helicase, but general ATPase knowledge does not identify calcium rather than the other listed ions as the ion giving this protein its strongest activity.


**Missing item-specific fact**

> The experimental finding that this particular Lhr ATPase is most efficient with Ca(2+), which is not supplied in the question.


**Reason**

> The sequence alone does not provide a defensible way to distinguish Ca(2+) from the other options. The decisive ion preference is a protein-specific experimental fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The cited annotation supports Ca(2+) as most efficient but also says Mn(2+) is less effective, suggesting it can support activity. Thus B is the preferred choice, but the word “required” does not clearly distinguish the preferred ion from an ion that supports lower activity.


### Important caveats

- The cofactor annotation is experimentally attributed, but “most efficient” does not mean calcium is indispensable.
- A structure described in the evidence contains Mg(2+) with an ATP analog; that observation alone does not establish Mg(2+) as the functional cofactor.
- The annotation excerpt repeats Mn(2+) as the less-effective ion; the evidence does not justify correcting that wording to another ion.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with an ATPase/helicase, but general ATPase knowledge does not identify calcium rather than the other listed ions as the ion giving this protein its strongest activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental finding that this particular Lhr ATPase is most efficient with Ca(2+), which is not supplied in the question.",
    "reason": "The sequence alone does not provide a defensible way to distinguish Ca(2+) from the other options. The decisive ion preference is a protein-specific experimental fact."
  },
  "case_id": "cofactor_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited Lhr protein entry, which records Ca(2+) as a cofactor based on experimental evidence and says its ssDNA-dependent ATPase is most efficient with Ca(2+). This supports B as the preferred cofactor, though it does not establish that Ca(2+) is strictly required."
  },
  "important_caveats": [
    "The cofactor annotation is experimentally attributed, but “most efficient” does not mean calcium is indispensable.",
    "A structure described in the evidence contains Mg(2+) with an ATP analog; that observation alone does not establish Mg(2+) as the functional cofactor.",
    "The annotation excerpt repeats Mn(2+) as the less-effective ion; the evidence does not justify correcting that wording to another ion."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The cited annotation supports Ca(2+) as most efficient but also says Mn(2+) is less effective, suggesting it can support activity. Thus B is the preferred choice, but the word “required” does not clearly distinguish the preferred ion from an ion that supports lower activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited Lhr protein entry, which records Ca(2+) as a cofactor based on experimental evidence and says its ssDNA-dependent ATPase is most efficient with Ca(2+). This supports B as the preferred cofactor, though it does not establish that Ca(2+) is strictly required.",
    "evidence_ids": ["C1", "C5", "C6", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with an ATPase/helicase, but general ATPase knowledge does not identify calcium rather than the other listed ions as the ion giving this protein its strongest activity.",
    "missing_item_specific_fact": "The experimental finding that this particular Lhr ATPase is most efficient with Ca(2+), which is not supplied in the question.",
    "reason": "The sequence alone does not provide a defensible way to distinguish Ca(2+) from the other options. The decisive ion preference is a protein-specific experimental fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The cited annotation supports Ca(2+) as most efficient but also says Mn(2+) is less effective, suggesting it can support activity. Thus B is the preferred choice, but the word “required” does not clearly distinguish the preferred ion from an ion that supports lower activity."
  },
  "important_caveats": [
    "The cofactor annotation is experimentally attributed, but “most efficient” does not mean calcium is indispensable.",
    "A structure described in the evidence contains Mg(2+) with an ATP analog; that observation alone does not establish Mg(2+) as the functional cofactor.",
    "The annotation excerpt repeats Mn(2+) as the less-effective ion; the evidence does not justify correcting that wording to another ion."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0QT91 (Lhr helicase from Mycolicibacterium smegmatis) annotates Ca(2+) as the cofactor with evidence code ECO:0000269 (direct assay) from PubMed 23549043 (Ordonez & Shuman, JBC 2013). The note states 'ssDNA-dependent ATPase is most efficient with Ca(2+); Mn(2+) and Mn(2+) are 60% less effective.' The sequence matches (SHA256 confirmed). The experimental evidence directly supports Ca(2+) as the designated cofactor.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H6](#evidence-h6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Na(+) and Co(2+) can be eliminated by general knowledge: Na(+) is not a catalytic cofactor for helicases/ATPases, and Co(2+) is rare (primarily associated with B12-dependent enzymes). However, the critical distinction is between Ca(2+) and Mn(2+), both plausible divalent cation cofactors for nucleotide-binding proteins. The Walker A motif (PTGSGKT) visible in the sequence is a generic P-loop NTPase signature that does not distinguish Ca(2+) preference from Mn(2+) preference. The specific finding that Ca(2+) is the most efficient cofactor while Mn(2+) is 60% less effective is an item-specific experimental measurement (Ordonez & Shuman 2013) that cannot be inferred from sequence features alone.


**Missing item-specific fact**

> The experimental measurement showing that this particular Lhr helicase's ssDNA-dependent ATPase activity is most efficient with Ca(2+) rather than Mn(2+), published in JBC 2013 (PMID 23549043). No sequence motif or structural feature in the provided 1507-aa sequence specifically encodes a Ca(2+)-over-Mn(2+) preference that would be recognizable without prior knowledge of this protein.


**Reason**

> While Na(+) and Co(2+) can be eliminated through general biological reasoning, the actual discrimination between Ca(2+) and Mn(2+) requires knowledge of a specific experimental result for this protein. The sequence contains a generic Walker A motif but no distinctive feature that would allow a model to predict Ca(2+) preference over Mn(2+) without memorizing the database annotation or the primary literature finding.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Mn(2+) is experimentally functional for this helicase (60% less effective than Ca(2+)), so a knowledgeable respondent might argue Mn(2+) is also a valid cofactor. However, the UniProt annotation specifically designates Ca(2+) as THE cofactor, and the question asks for 'the specific cofactor required,' making B the intended answer. The ambiguity is minor since the annotation clearly prioritizes Ca(2+).


### Important caveats

- The crystal structure (PDB 5V9X) shows Mg(2+) in the active site, but Mg(2+) is not among the answer choices, creating a slight disconnect between structural and biochemical cofactor data.
- The UniProt note contains a likely typographical error: 'Mn(2+) and Mn(2+) are 60% less effective' (Mn listed twice, possibly one should be Mg or another ion).
- The identity of this protein as Lhr from M. smegmatis was determined by reviewer-only sequence matching; the evaluated model received only the raw sequence with no organism or protein name context.
- ECO:0000269 indicates direct experimental assay, making this a robust annotation rather than computational prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Na(+) and Co(2+) can be eliminated by general knowledge: Na(+) is not a catalytic cofactor for helicases/ATPases, and Co(2+) is rare (primarily associated with B12-dependent enzymes). However, the critical distinction is between Ca(2+) and Mn(2+), both plausible divalent cation cofactors for nucleotide-binding proteins. The Walker A motif (PTGSGKT) visible in the sequence is a generic P-loop NTPase signature that does not distinguish Ca(2+) preference from Mn(2+) preference. The specific finding that Ca(2+) is the most efficient cofactor while Mn(2+) is 60% less effective is an item-specific experimental measurement (Ordonez & Shuman 2013) that cannot be inferred from sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental measurement showing that this particular Lhr helicase's ssDNA-dependent ATPase activity is most efficient with Ca(2+) rather than Mn(2+), published in JBC 2013 (PMID 23549043). No sequence motif or structural feature in the provided 1507-aa sequence specifically encodes a Ca(2+)-over-Mn(2+) preference that would be recognizable without prior knowledge of this protein.",
    "reason": "While Na(+) and Co(2+) can be eliminated through general biological reasoning, the actual discrimination between Ca(2+) and Mn(2+) requires knowledge of a specific experimental result for this protein. The sequence contains a generic Walker A motif but no distinctive feature that would allow a model to predict Ca(2+) preference over Mn(2+) without memorizing the database annotation or the primary literature finding."
  },
  "case_id": "cofactor_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0QT91 (Lhr helicase from Mycolicibacterium smegmatis) annotates Ca(2+) as the cofactor with evidence code ECO:0000269 (direct assay) from PubMed 23549043 (Ordonez & Shuman, JBC 2013). The note states 'ssDNA-dependent ATPase is most efficient with Ca(2+); Mn(2+) and Mn(2+) are 60% less effective.' The sequence matches (SHA256 confirmed). The experimental evidence directly supports Ca(2+) as the designated cofactor."
  },
  "important_caveats": [
    "The crystal structure (PDB 5V9X) shows Mg(2+) in the active site, but Mg(2+) is not among the answer choices, creating a slight disconnect between structural and biochemical cofactor data.",
    "The UniProt note contains a likely typographical error: 'Mn(2+) and Mn(2+) are 60% less effective' (Mn listed twice, possibly one should be Mg or another ion).",
    "The identity of this protein as Lhr from M. smegmatis was determined by reviewer-only sequence matching; the evaluated model received only the raw sequence with no organism or protein name context.",
    "ECO:0000269 indicates direct experimental assay, making this a robust annotation rather than computational prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Mn(2+) is experimentally functional for this helicase (60% less effective than Ca(2+)), so a knowledgeable respondent might argue Mn(2+) is also a valid cofactor. However, the UniProt annotation specifically designates Ca(2+) as THE cofactor, and the question asks for 'the specific cofactor required,' making B the intended answer. The ambiguity is minor since the annotation clearly prioritizes Ca(2+)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0QT91 (Lhr helicase from Mycolicibacterium smegmatis) annotates Ca(2+) as the cofactor with evidence code ECO:0000269 (direct assay) from PubMed 23549043 (Ordonez & Shuman, JBC 2013). The note states 'ssDNA-dependent ATPase is most efficient with Ca(2+); Mn(2+) and Mn(2+) are 60% less effective.' The sequence matches (SHA256 confirmed). The experimental evidence directly supports Ca(2+) as the designated cofactor.",
    "evidence_ids": ["C5", "C6", "H6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Na(+) and Co(2+) can be eliminated by general knowledge: Na(+) is not a catalytic cofactor for helicases/ATPases, and Co(2+) is rare (primarily associated with B12-dependent enzymes). However, the critical distinction is between Ca(2+) and Mn(2+), both plausible divalent cation cofactors for nucleotide-binding proteins. The Walker A motif (PTGSGKT) visible in the sequence is a generic P-loop NTPase signature that does not distinguish Ca(2+) preference from Mn(2+) preference. The specific finding that Ca(2+) is the most efficient cofactor while Mn(2+) is 60% less effective is an item-specific experimental measurement (Ordonez & Shuman 2013) that cannot be inferred from sequence features alone.",
    "missing_item_specific_fact": "The experimental measurement showing that this particular Lhr helicase's ssDNA-dependent ATPase activity is most efficient with Ca(2+) rather than Mn(2+), published in JBC 2013 (PMID 23549043). No sequence motif or structural feature in the provided 1507-aa sequence specifically encodes a Ca(2+)-over-Mn(2+) preference that would be recognizable without prior knowledge of this protein.",
    "reason": "While Na(+) and Co(2+) can be eliminated through general biological reasoning, the actual discrimination between Ca(2+) and Mn(2+) requires knowledge of a specific experimental result for this protein. The sequence contains a generic Walker A motif but no distinctive feature that would allow a model to predict Ca(2+) preference over Mn(2+) without memorizing the database annotation or the primary literature finding."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Mn(2+) is experimentally functional for this helicase (60% less effective than Ca(2+)), so a knowledgeable respondent might argue Mn(2+) is also a valid cofactor. However, the UniProt annotation specifically designates Ca(2+) as THE cofactor, and the question asks for 'the specific cofactor required,' making B the intended answer. The ambiguity is minor since the annotation clearly prioritizes Ca(2+)."
  },
  "important_caveats": [
    "The crystal structure (PDB 5V9X) shows Mg(2+) in the active site, but Mg(2+) is not among the answer choices, creating a slight disconnect between structural and biochemical cofactor data.",
    "The UniProt note contains a likely typographical error: 'Mn(2+) and Mn(2+) are 60% less effective' (Mn listed twice, possibly one should be Mg or another ion).",
    "The identity of this protein as Lhr from M. smegmatis was determined by reviewer-only sequence matching; the evaluated model received only the raw sequence with no organism or protein name context.",
    "ECO:0000269 indicates direct experimental assay, making this a robust annotation rather than computational prediction."
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
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.412187+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29108"},"evidences":[{"evidenceCode":"ECO:0000269","id":"23549043","source":"PubMed"}],"name":"Ca(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23549043","source":"PubMed"}],"value":"ssDNA-dependent ATPase is most efficient with Ca(2+); Mn(2+) and Mn(2+) are 60% less effective."}]}}
```

Source SHA-256: `bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.412187+00:00.  

```json
{"citation":{"authors":["Ordonez H.","Shuman S."],"citationCrossReferences":[{"database":"PubMed","id":"23549043"},{"database":"DOI","id":"10.1074/jbc.m113.466854"}],"citationType":"journal article","firstPage":"14125","id":"23549043","journal":"J. Biol. Chem.","lastPage":"14134","publicationDate":"2013","title":"Mycobacterium smegmatis Lhr Is a DNA-dependent ATPase and a 3'-to-5' DNA translocase and helicase that prefers to unwind 3'-tailed RNA:DNA hybrids.","volume":"288"},"referenceNumber":4,"referencePositions":["FUNCTION AS A HELICASE","FUNCTION AS AN ATPASE","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN"]}
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

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)  
**Locator:** `lines 128-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 131 / 1.  
**Retrieved:** 2026-11-01T06:27:42.288105+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Ca(2+); Xref=ChEBI:CHEBI:29108;
CC         Evidence={ECO:0000269|PubMed:23549043};
CC       Note=ssDNA-dependent ATPase is most efficient with Ca(2+); Mn(2+) and
CC       Mn(2+) are 60% less effective. {ECO:0000269|PubMed:23549043};
```

Source SHA-256: `63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 63. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
